try:
    from .github import *
except ValueError:
    from github import *


class GithubPullsCommand(GithubWindowCommand):
    @with_repo
    def run(self, repo):
        open_url(repo.pulls_url())
