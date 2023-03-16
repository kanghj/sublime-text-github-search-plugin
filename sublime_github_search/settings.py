import sublime

def filename():
    return 'Github Search.sublime-settings'

def get_setting(name, default=None):
    v = sublime.active_window().project_data().get("github_search", {}).get(name, None)
    if v != None:
        return v
    else:
        return sublime.load_settings(filename()).get(name, default)
