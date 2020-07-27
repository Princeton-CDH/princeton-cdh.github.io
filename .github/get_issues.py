import argparse
import csv
import datetime
import os
import subprocess

from ghub_zhub import GitHubAPI, ZenHubAPI


EXCLUDE_REPOS = [
    'bitKlavier', 'mapping-expatriate-paris', 'davilajs',
    'bluemountainsprings', 'bluemountain-transcriptions', 'mepApp',
    'mep-beach-logbooks', 'abcbooks'
]


CSV_FIELDS = ['issue', 'project', 'url', 'estimate', 'closed',
              'labels', 'milestone']


def get_issues(all_issues=False):
    """
    Use ZenHub and GitHub API to generate a CSV of all issues in
    all repositories in this GitHub organization, excluding any in the
    EXCLUDE_REPOS list. If the CSV already exists, use the file last
    modification date and update based on issues modified since then.
    File is saved as `data/issues.csv`.
    """

    # Get APIs
    ghub = GitHubAPI(os.environ['GITHUB_USERNAME'],
                     os.environ['GITHUB_API_TOKEN'])
    zhub = ZenHubAPI(os.environ['ZENHUB_API_TOKEN'])

    # filename where data will be stored or appended
    filename = 'data/issues.csv'
    date_since = None
    issue_count = 0

    # if the file exists and not retrieving all issues,
    # determine last commit
    if os.path.exists(filename) and not all_issues:
        # get the last modification of the file in git
        last_commit_date = subprocess.check_output(
            ['git', 'log', '-1', '--date=short', '--pretty=%ad',
             filename])
        # convert bytes to string
        last_commit_date = last_commit_date.decode().strip()
        # NOTE: should add a flag or environment variable to turn this
        # off and get an updated set of all issues
        date_since = datetime.datetime.strptime(last_commit_date, '%Y-%m-%d')

    github_org = os.environ['GITHUB_REPOSITORY'].split('/')[0]
    repos = ghub.get_org_repos(github_org)

    # for reporting purposes, only include closed issues
    get_issue_params = {}
    if date_since:
        get_issue_params['since'] = date_since.isoformat()

    # open file in write mode if getting all issues; otherwise append
    write_mode = 'w' if all_issues else 'a'
    with open(filename, write_mode) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CSV_FIELDS)
        # when creating a new file, write out CSV header
        if all_issues:
            writer.writeheader()

        for repo, repo_id in repos.items():
            if repo in EXCLUDE_REPOS:
                print('Skipping %s' % repo)
                continue

            for issue in ghub.get_repo_issues(github_org, repo,
                                              params=get_issue_params):
                # github returns pull requests in issue list,
                # but we don't currently report on them
                if 'pull_request' in issue:
                    continue

                zhub_info = zhub.get_issue(repo_id, issue['number'])
                milestone = issue['milestone']

                info = {
                    'issue': issue['title'],
                    'project': repo,
                    'url': issue['url'],
                    'estimate': zhub_info.get('estimate', {}).get('value', ''),
                    'closed': issue['closed_at'],
                    'labels': ';'.join([l['name'] for l in issue['labels']]),
                    'milestone': milestone['title'] if milestone else '',
                }
                # write out to csv file
                writer.writerow(info)
                issue_count += 1

    print('Downloaded data for %d issues' % issue_count)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Gather issue information from GitHub and ZenHub.')
    parser.add_argument(
        '--all', '-a', action='store_true', default=False,
        help='Get all issues (by default only gets issues since ' +
             'data file was last changed in git)')

    args = parser.parse_args()
    get_issues(all_issues=args.all)
