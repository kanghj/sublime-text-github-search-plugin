# Sublime Github Search plugin

A plugin to search github code, issues and pull requests.

# Usage

Highlight a piece of text (or multiple pieces of text) in your editor window. Then you can:

- Right click, hover "Github Search" in the context menu and select the search you want to do from the submenu
- Open the command palette, filter for "github search" and choose the search you want to do
- Use one of the key bindings below to trigger the search you want to do

## Default Key Bindings

**NB:** For all these key bindings, hold down `ctrl` + `alt` + `g` in addition to pressing the specific binding key.
ManyToMany
- code search - `c`
- issue search - `c`
- pull request search - `c`

# Default Search Options

By default the plugin adds `org:d3r` to your search. However you can change this by adding project settings under the `github_search` key. An example project settings file might look like this:

```json
{
  "folders":
  [
    <snip>
  ],
    "github_search": {
        "default_options": {
            "org": "d3r",
            "language": "php"
        }
    }
}
```

Options will be added to all search types - sometimes this may mean that they have no impact.
