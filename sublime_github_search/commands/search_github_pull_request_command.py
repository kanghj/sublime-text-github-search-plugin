import sublime_plugin
from ..utils import search_github

class SearchGithubPullRequestCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        search_github(self.view.sel(), self.view, "pullrequests")
