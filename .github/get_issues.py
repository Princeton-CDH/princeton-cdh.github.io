import argparse
import csv
import datetime
import json
import os
import subprocess

from ghub_zhub import GitHubAPI, ZenHubAPI


EXCLUDE_REPOS = [
    "bitKlavier",
    "mapping-expatriate-paris",
    "davilajs",
    "bluemountainsprings",
    "bluemountain-transcriptions",
    "mepApp",
    "mep-beach-logbooks",
    "abcbooks",
]


# file where data will be stored
DATA_FILENAME = "data/issues.json"


def get_issues(all_issues=False, limit_repos=None):
    """
    Use ZenHub and GitHub API to generate a CSV of all issues in
    all repositories in this GitHub organization, excluding any in the
    EXCLUDE_REPOS list. If the CSV already exists, use the file last
    modification date and update based on issues modified since then.
    File is saved as `data/issues.csv`.
    """

    # Get APIs
    ghub = GitHubAPI(os.environ["GITHUB_USERNAME"], os.environ["GITHUB_API_TOKEN"])
    zhub = ZenHubAPI(os.environ["ZENHUB_API_TOKEN"])

    date_since = None
    issue_count = 0

    # if the file exists and not retrieving all issues,
    # determine last commit
    if os.path.exists(DATA_FILENAME) and not all_issues:
        # get the last modification of the file in git
        last_commit_date = subprocess.check_output(
            ["git", "log", "-1", "--date=short", "--pretty=%ad", DATA_FILENAME]
        )
        # convert bytes to string
        last_commit_date = last_commit_date.decode().strip()
        if last_commit_date:
            date_since = datetime.datetime.strptime(last_commit_date, "%Y-%m-%d")

    github_org = os.environ["GITHUB_REPOSITORY"].split("/")[0]
    repos = ghub.get_org_repos(github_org)
    # if specified, limit to specific repos
    if limit_repos:
        repos = {key: val for key, val in repos.items() if key in limit_repos}

    # NOTE: possible/useful to only include closed issues?
    get_issue_params = {}
    if date_since:
        get_issue_params["since"] = date_since.isoformat()

    # open file and load all previous issues
    with open(DATA_FILENAME) as datafile:
        data = json.load(datafile)

    # load into a dict keyed on issue url to uniquify and allow updating
    issues = {}
    for issue in data:
        issues[issue["url"]] = issue

    for repo, repo_id in repos.items():
        if repo in EXCLUDE_REPOS:
            print("Skipping %s" % repo)
            continue

        for issue in ghub.get_repo_issues(github_org, repo, params=get_issue_params):
            # github returns pull requests in issue list,
            # but we don't currently report on them
            if "pull_request" in issue:
                continue

            zhub_info = zhub.get_issue(repo_id, issue["number"])
            milestone = issue["milestone"]
            info = {
                "issue": issue["title"],
                "project": repo,
                "url": issue["url"],
                "estimate": zhub_info.get("estimate", {}).get("value", ""),
                "closed": issue["closed_at"],
                "labels": [l["name"] for l in issue["labels"]],
                "milestone": milestone["title"] if milestone else "",
                "assignees": [a["login"] for a in issue["assignees"]],
                # zenhub pipelines indicate status; get unique list of pipeline names
                "pipeline": list(
                    set(p["name"] for p in zhub_info.get("pipelines", []))
                ),
            }
            # add/update issue info in issue data dict
            issues[info["url"]] = info

            issue_count += 1

    print("Downloaded updated data for %d issues" % issue_count)

    # write updated data file as a list of issues sorted by issue url
    with open(DATA_FILENAME, "w") as datafile:
        json.dump([issues[url] for url in sorted(issues.keys())], datafile, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Gather issue information from GitHub and ZenHub."
    )
    parser.add_argument(
        "--all",
        "-a",
        action="store_true",
        default=False,
        help="Get all issues (by default only gets issues since "
        + "data file was last changed in git)",
    )
    parser.add_argument(
        "--repo", action="append", help="Only get issues for specified repository"
    )

    args = parser.parse_args()
    get_issues(all_issues=args.all, limit_repos=args.repo)
