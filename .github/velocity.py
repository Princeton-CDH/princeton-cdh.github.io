#!/usr/bin/env python

from datetime import date, datetime
import csv
import os

import pandas as pd

from storypoints import ZenHubAPI, GitHubAPI

DEVTEAM_PROJECTS = [
    'cdh-web', 'winthrop-django', 'django-pucas', 'djiffy', 'django-annotator-store',
    'derrida-django', 'mep-django', 'viapy',
    'ppa-django', 'parasolr', 'pemm-scripts', 'startwords'
]

def get_closed_issues():
    # Get APIs
    ghub = GitHubAPI(os.environ['GH_USERNAME'], os.environ['GH_API_TOKEN'])
    zhub = ZenHubAPI(os.environ['ZENHUB_API_TOKEN'])

    # Read existing CSV
    filename = 'data/issues.csv'
    if os.path.exists(filename):
        df = pd.read_csv(filename, parse_dates=['closed'])
        # find the latest date already read
        date_since = df['closed'].max()
        data_dict = df.to_dict('records')
    else:
        date_since = date(2020, 4, 1) # HELP: How far back do we want to look?
        data_dict = []

    # get dict of repo by name -> id
    repos = ghub.get_org_repos('Princeton-CDH')

    for repo, repo_id in repos.items():
        if repo not in DEVTEAM_PROJECTS:
            continue

        for issue in ghub.get_repo_issues('Princeton-CDH', repo,
                                          params={'since': date_since.isoformat()}):
            
            zhub_info = zhub.get_issue(repo_id, issue['number'])
            
            info = {
                'issue': issue['title'],
                'project': repo,
                'url': issue['url'],
                'estimate': zhub_info.get('estimate', {}).get('value', ''),
                'closed': issue['closed_at'],
                'labels': ';'.join([label['name'] for label in issue['labels']])
            }

            data_dict.append(info)

    pd.DataFrame(data_dict).to_csv(filename, index=False)


if __name__ == '__main__':
    get_closed_issues()
