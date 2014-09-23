import sublime, sublime_plugin, webbrowser
try:
    from .github import *
except ValueError:
    from github import *


class GithubCreatePrCommand(GithubWindowCommand):
    @with_repo
    def run(self, repo):
        self.remotes      = repo.remotes
        self.remote_names = list(self.remotes.keys())
        self.repo         = repo
        self.window.show_quick_panel(self.remote_names, self.remote_selected)

    def remote_selected(self, index):
        url = self.remotes[self.remote_names[index]]
        remote = re.search(":(\w+)\/", url).group(1)
        webbrowser.open_new_tab(self.generate_url(remote))

    def generate_url(self, remote):
        branch = self.repo.branch
        interpolations = (self.repo.info['web_uri'], remote, branch, branch)
        return "https://%s/compare/%s:%s...%s" % interpolations
