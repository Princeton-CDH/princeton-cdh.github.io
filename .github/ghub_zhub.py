#! /usr/bin/env python

from time import sleep

import requests
from ratelimiter import RateLimiter


class ZenHubAPI(object):
    endpoint = "https://api.zenhub.com"

    def __init__(self, token):
        self.token = token
        self.session = requests.session()
        self.session.headers.update({"X-Authentication-Token": self.token})

    @RateLimiter(max_calls=100, period=60)
    def _call(self, url):
        return self.session.get(url)

    def get_issue(self, repo_id, issue_id):
        url = "%s/p1/repositories/%s/issues/%s" % (self.endpoint, repo_id, issue_id)
        response = self._call(url)
        return response.json()


class GitHubAPI(object):
    endpoint = "https://api.github.com"

    def __init__(self, user, token):
        self.session = requests.session()
        self.session.auth = (user, token)
        # explicitly request api v3 per the documentation
        self.session.headers.update({"Accept": "application/vnd.github.v3+json"})

    def _call(self, url, params=None):
        opts = {}
        if params:
            opts["params"] = params
        return self.session.get(url, **opts)

    def get_org_repos(self, org):
        url = "%s/orgs/%s/repos" % (self.endpoint, org)
        response = self._call(url)
        repos = {}
        for repo in response.json():
            repos[repo["name"]] = repo["id"]

        while "next" in response.links:
            response = self._call(response.links["next"]["url"])
            for repo in response.json():
                repos[repo["name"]] = repo["id"]

        return repos

    def get_repo_issues(self, owner, repo, params=None):
        url = "%s/repos/%s/%s/issues" % (self.endpoint, owner, repo)
        if params is None:
            params = {}
        if "state" not in params:
            params["state"] = "all"
        response = self._call(url, params=params)
        issues = response.json()
        while "next" in response.links:
            response = self._call(response.links["next"]["url"])
            issues.extend(response.json())

        return issues

    def get_repo_commit_activity(self, owner, repo):
        url = "%s/repos/%s/%s/stats/commit_activity" % (self.endpoint, owner, repo)
        response = self._call(url)
        if response.status_code == 202:
            print("waiting for GitHub to generate statistics for %s..." % repo)
            sleep(3)
            return self.get_repo_commit_activity(owner, repo)
        elif response.status_code == 200:
            return response.json()

    def get_releases(self, owner, repo):
        url = "%s/repos/%s/%s/releases" % (self.endpoint, owner, repo)
        response = self._call(url)
        if response.status_code == requests.codes.ok:
            return response.json()

    def get_tags(self, owner, repo):
        url = "%s/repos/%s/%s/tags" % (self.endpoint, owner, repo)
        response = self._call(url)
        if response.status_code == requests.codes.ok:
            return response.json()

    def get_commit(self, owner, repo, sha):
        url = "%s/repos/%s/%s/commits/%s" % (self.endpoint, owner, repo, sha)
        response = self._call(url)
        if response.status_code == requests.codes.ok:
            return response.json()
