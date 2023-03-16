import sublime
import webbrowser
from .settings import get_setting

SUBLIME_3 = sublime.version() == '' or int(sublime.version()) > 3000

if SUBLIME_3:
    def encode(text):
        from urllib.parse import quote_plus
        return quote_plus(text)
else:
    def encode(text):
        import urllib
        return urllib.quote_plus(text)

def search_github(sel,view,search_type):
    for selection in sel:
        if selection.empty():
            continue
        open_search_tab(view.substr(selection), search_type)

def open_search_tab(text, search_type):
    qs = [
        "type=" + search_type
    ]
    search_term = [
        encode(text)
    ]
    defaults = get_setting("default_options", {})
    for key,val in defaults.items():
        search_term.append(key + ":" + val)
    url = get_setting("base_url", "https://github.com/search")
    qs.append("q=" + encode(" ".join(search_term)))
    webbrowser.open_new_tab( url + "?" + "&".join(qs) )
