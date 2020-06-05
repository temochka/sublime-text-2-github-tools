import sublime, sublime_plugin
try:
    from .github import *
except ValueError:
    from github import *


class GithubOpenCommand(GithubWindowCommand):
    @require_file
    @with_repo
    def run(self, repo):
        open_url(
            repo.browse_file_url(
                self.relative_filename(),
                self.current_line_number(),
            )
        )
