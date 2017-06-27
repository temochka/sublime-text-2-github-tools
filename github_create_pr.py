import sublime, sublime_plugin
try:
    from .github import *
except ValueError:
    from github import *


class GithubCreatePrCommand(GithubWindowCommand):
    @with_repo
    def run(self, repo):
        open_url(git_compare_url(repo.info['web_uri'], repo.branch))
