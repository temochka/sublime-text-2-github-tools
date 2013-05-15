import sublime, sublime_plugin, webbrowser
from .github import *

class GithubOpenCommand(GithubWindowCommand):
  @with_repo
  def run(self, repo):
    webbrowser.open_new_tab(repo.browse_file_url(self.relative_filename()))
