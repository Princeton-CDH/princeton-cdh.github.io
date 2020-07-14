#!/usr/bin/env python
"""
# INTEGRATION NOTES
- "since" functionality dropped for now

"""
import csv
from datetime import date
import json
import os

from storypoints import GitHubAPI


DEVTEAM_PROJECTS = [
    'cdh-web', 'winthrop-django', 'django-pucas', 'djiffy', 'django-annotator-store',
    'derrida-django', 'mep-django', 'viapy',
    'ppa-django', 'piffle', 'parasolr', 'pemm-scripts', 'startwords'
]

def get_repo_releases(since=date(2020, 6, 22)):
    ghub = GitHubAPI(os.environ['GITHUB_USERNAME'], os.environ['GITHUB_API_TOKEN'])

    tag_data = []
    for repo in DEVTEAM_PROJECTS:
        print(repo)
        tags = ghub.get_tags('Princeton-CDH', repo)
        repo_data = {}
        for tag in tags:
            commit_info = ghub.get_commit('Princeton-CDH', repo, tag['commit']['sha'])
            if commit_info:
                date_parts = commit_info['commit']['author']['date'].split('T')[0].split('-')
                release_date = date(*(int(part) for part in date_parts))
                # if release_date >= since:
                    # print('%s %s' % (tag['name'], commit_info['commit']['author']['date']))

                repo_data[tag['name']] = commit_info['commit']['author']['date']

        tag_data.append({'repo': repo, 'tags': repo_data})


    with open(f'data/releases-{date.today()}.json', 'w') as outfile:
        json.dump(tag_data, outfile, indent=4)


if __name__ == '__main__':
    get_repo_releases()
