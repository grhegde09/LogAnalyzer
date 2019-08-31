# LogAnalyzer: Help
This is the help page for LogAnalyzer.

## How to use LogAnalyzer?
* Log colouring feature is enabled by default. Just open studioLog.log file in Sublime Text 3 and you will see the colouring. (Note: Extension has to be ‘.log’)
* To use highlight or filtering, you need to update the LogAnalyzer config. 
* To edit LogAnalyzer config, go to `Preferences` -> `LogAnalyzer` -> `Configuration` 
* After updating the configuration you can invoke LogAnalyzer commands.
* All LogAnalyzer commands can be accessed with both Keyboard shortcuts and Command palette.

</br></br>

#### Sample Configuration File   
Here is a sample configuration file. Please read the notes before editing the configuration file.

```javascript
{
  "config": {
    "highlighterPreferences": {
      "highlightPatterns": [
        {
          "searchRegex": "DefaultHighlightPattern1",
          "style": 1
        },
        {
          "searchRegex": "DefaultHighlightPattern2",
          "style": 2
        }
      ]
    },
    "filterPreferences": {
      "isFilteringEnabled": false,
      "filterPatterns": [
        "DefaultFilterPattern1",
        "DefaultFilterPattern2"
      ]
    }
  }
}
```
</br>

#### Important notes
* All lines matching patterns specified under `highlightPatterns` will be highlighted.
* Styles 1 - 8 are supported for highlighting.
* If `isFilteringEnabled` is `true`, then all lines matching regex specified under  `filterPatterns` will be removed from the file.
* `searchRegex ` and each regex pattern mentioned in `filterPatterns` should be provided so that, it matches a part of a line and never more than a line. If it matches more than a line, then the behaviour is undefined.


## Default Keyboard Shortcuts:
### Linux
* To highlight patterns – <kbd>Super</kbd>+<kbd>CTRL</kbd>+<kbd>h</kbd>
* To clear highlights – <kbd>Super</kbd>+<kbd>CTRL</kbd>+<kbd>Shift</kbd>+<kbd>h</kbd>
* To filter pattern – <kbd>Super</kbd>+<kbd>CTRL</kbd>+<kbd>e</kbd>
* To restore filtered pattern – <kbd>Super</kbd>+<kbd>CTRL</kbd>+<kbd>Shift</kbd>+<kbd>h</kbd>
* To launch 'Command Palette' - <kbd>CTRL</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd> (All LogAnalyzer commands start with ‘LogAnalyzer:’ in command palette e.g.: `LogAnalyzer: Highlight Lines`)

### OS X
* To highlight patterns – <kbd>CMD</kbd>+<kbd>CTRL</kbd>+<kbd>h</kbd>
* To clear highlights – <kbd>CMD</kbd>+<kbd>CTRL</kbd>+<kbd>Shift</kbd>+<kbd>h</kbd>
* To filter pattern – <kbd>CMD</kbd>+<kbd>CTRL</kbd>+<kbd>e</kbd>
* To restore filtered pattern – <kbd>CMD</kbd>+<kbd>CTRL</kbd>+<kbd>Shift</kbd>+<kbd>h</kbd>
* To launch 'Command Palette' - <kbd>CMD</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd> (All LogAnalyzer commands start with ‘LogAnalyzer:’ in command palette e.g.: `LogAnalyzer: Highlight Lines`)

These key bindings can be changed by going to  `Preferences` -> `LogAnalyzer` ->  `Key Bindings`

