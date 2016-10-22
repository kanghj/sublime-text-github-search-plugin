import sublime, sublime_plugin
import webbrowser
import json

SUBLIME_3 = sublime.version() == '' or int(sublime.version()) > 3000
PHANTOM_SUPPORT = int(sublime.version()) >= 3118

if SUBLIME_3:
    def encode(text):
        from urllib.parse import quote_plus
        return quote_plus(text)
else:
    def encode(text):
        import urllib
        return urllib.quote_plus(text)

try:
    from urllib.request import Request, urlopen
    from urllib.error import URLError
except ImportError:
    from urllib2 import Request, urlopen, URLError


def open_search_tab(text, search_type):
    
    webbrowser.open_new_tab( 'https://github.com/search?q=%s&ref=simplesearch&type=%s' % (encode(text), search_type) )

def github_token():
    try:
        plugin_settings = sublime.load_settings("GithubSearch.sublime-settings")
        return plugin_settings.get('api_tokens')['github.com']
    except:
        return ''

def current_language(view):
    import os
    syntax = os.path.basename(view.settings().get('syntax'))
    return os.path.splitext(syntax)[0]


class SearchGithubIssueCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            if selection.empty():
                continue
                
            open_search_tab(self.view.substr(selection), 'Issues')

class SearchGithubCodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        pset = sublime.PhantomSet(self.view)
        token = github_token()

        for selection in self.view.sel():
            if selection.empty():
                continue
            

            selected = self.view.substr(selection)
            
            req = Request('https://api.github.com/search/code?q=' + 
                encode(selected) + '&language=' + current_language(self.view))
            req.add_header('Authorization', 'token ' + token)
            req.add_header('Accept', 'application/vnd.github.v3.text-match+json')
            resp = urlopen(req).read()

            github_data = json.loads(resp.decode('utf8', 'ignore'))
            
            first_result = github_data['items'][0]['text_matches'][0]
            first_fragment = first_result['fragment']
            fragment_url = first_result['object_url']

            self.view.show_popup(
                '<div style="background-color:rgba(123,123,123);"> ' + 
                first_fragment.replace('\n', '<br>') +
                '<br>' + '<a href="' + fragment_url + '"> View </a>'
                 '</div>', sublime.HIDE_ON_MOUSE_MOVE_AWAY, -1, 480, 700
            )
