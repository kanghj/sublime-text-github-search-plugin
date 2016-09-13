import sublime, sublime_plugin
import webbrowser

SUBLIME_3 = sublime.version() == '' or int(sublime.version()) > 3000

if SUBLIME_3:
    def encode(text):
        from urllib.parse import quote_plus
        return quote_plus(text)
else:
    def encode(text):
        import urllib
        return urllib.quote_plus(text)


class SearchGithubCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            if selection.empty():
                continue

            text = self.view.substr(selection)

            webbrowser.open_new_tab( 'https://github.com/search?q=%s&ref=simplesearch&type=Issues' % (encode(text), ) )
