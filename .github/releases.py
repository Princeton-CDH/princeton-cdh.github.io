#!/usr/bin/env python

import json
import os

from storypoints import GitHubAPI


def get_repo_releases():
    """Use the GitHub API to collect all tags from all repositories
    in the GitHub organization.
    Create a JSON of all releases and output as `data/releases.json`
    """
    ghub = GitHubAPI(os.environ['GITHUB_USERNAME'],
                     os.environ['GITHUB_API_TOKEN'])

    github_org = os.environ['GITHUB_REPOSITORY'].split('/')[0]

    tag_data = []
    for repo in ghub.get_org_repos(github_org):
        tags = ghub.get_tags(github_org, repo)
        repo_data = {}
        for tag in tags:
            commit_info = ghub.get_commit(ghub_org, repo, tag['commit']['sha'])
            repo_data[tag['name']] = commit_info['commit']['author']['date']

        # skip if no tags
        if repo_data:
            tag_data.append({'repo': repo, 'tags': repo_data})

    with open('data/releases.json', 'w') as outfile:
        json.dump(tag_data, outfile, indent=4)


if __name__ == '__main__':
    get_repo_releases()
