import sublime, sublime_plugin
import webbrowser

class SearchGithubCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            if selection.empty():
                continue

            text = self.view.substr(selection)

            webbrowser.open_new_tab( 'https://github.com/search?q=%s&ref=simplesearch' % (text, ) )
