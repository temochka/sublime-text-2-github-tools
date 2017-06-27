import sublime, sublime_plugin
try:
    from .github import *
except ValueError:
    from github import *


class GithubRepositoryCommand(GithubWindowCommand):
    @with_repo
    def run(self, repo):
        open_url(repo.repository_url())
