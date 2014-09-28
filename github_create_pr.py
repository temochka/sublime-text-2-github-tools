import sublime, sublime_plugin, webbrowser
try:
    from .github import *
except ValueError:
    from github import *


class GithubCreatePrCommand(GithubWindowCommand):
    @with_repo
    def run(self, repo):
        webbrowser.open_new_tab(self.generate_url(repo))

    def generate_url(self, repo):
        interpolations = (repo.info['web_uri'], repo.branch)
        return "https://%s/compare/%s?expand=1" % interpolations
