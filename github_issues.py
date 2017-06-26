import sublime, sublime_plugin
try:
    from .github import *
except ValueError:
    from github import *


class GithubIssuesCommand(GithubWindowCommand):
    @with_repo
    def run(self, repo):
        open_url(repo.issues_url())
