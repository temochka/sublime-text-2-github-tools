import sublime, sublime_plugin, webbrowser
try:
    from .github import *
except ValueError:
    from github import *


class GithubOpenCommand(GithubWindowCommand):
    @require_file
    @with_repo
    def run(self, repo):
        sublime.active_window().run_command('open_url', {"url": repo.browse_file_url(self.relative_filename())})
