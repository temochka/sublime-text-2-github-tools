import sublime, sublime_plugin
try:
    from .github import *
except ValueError:
    from github import *


class GithubFileHistoryCommand(GithubWindowCommand):
    @require_file
    @with_repo
    def run(self, repo):
        open_url(repo.file_history_url(self.relative_filename()))
