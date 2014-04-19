import sublime, sublime_plugin, webbrowser
try:
    from .github import *
except ValueError:
    from github import *


class GithubBlameCommand(GithubWindowCommand):
    @with_repo
    def run(self, repo):
        webbrowser.open_new_tab(repo.blame_file_url(self.relative_filename()))
