import datetime
import os
import subprocess

import pandas as pd

from ghub_zhub import GitHubAPI, ZenHubAPI

EXCLUDE_REPOS = [
    'bitKlavier', 'mapping-expatriate-paris', 'davilajs',
    'bluemountainsprings', 'bluemountain-transcriptions', 'mepApp',
    'mep-beach-logbooks', 'abcbooks'
]


def get_issues():
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

    # Read existing CSV
    filename = 'data/issues.csv'
    date_since = None
    data_dict = []

    if os.path.exists(filename):
        # get the last modification of the file in git
        last_commit_date = subprocess.check_output(
            ['git', 'log', '--date=short', '--pretty=%ad', 'data/issues.csv'])
        # convert bytes to string
        last_commit_date = last_commit_date.strip().decode()
        date_since = datetime.datetime.strptime(last_commit_date, '%Y-%m-%d')
        df = pd.read_csv(filename, parse_dates=['closed'])
        data_dict = df.to_dict('records')

    github_org = os.environ['GITHUB_REPOSITORY'].split('/')[0]
    repos = ghub.get_org_repos(github_org)

    get_issue_params = {}
    if date_since:
        get_issue_params['since'] = date_since.isoformat()

    for repo, repo_id in repos.items():
        if repo in EXCLUDE_REPOS:
            print('Skipping %s' % repo)
            continue

        for issue in ghub.get_repo_issues(github_org, repo,
                                          params=get_issue_params):
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
            data_dict.append(info)

    pd.DataFrame(data_dict).to_csv(filename, index=False)


if __name__ == '__main__':
    get_issues()
