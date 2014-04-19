import sublime, sublime_plugin
from github import copy_and_open_default_settings


class GithubPluginSettings(sublime_plugin.WindowCommand):
    def run(self):
        copy_and_open_default_settings()
