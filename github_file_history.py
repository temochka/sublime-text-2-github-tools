import sublime, sublime_plugin, webbrowser
try:
    from .github import *
except ValueError:
    from github import *


class GithubFileHistoryCommand(GithubWindowCommand):
    @require_file
    @with_repo
    def run(self, repo):
        webbrowser.open_new_tab(repo.file_history_url(self.relative_filename()))
