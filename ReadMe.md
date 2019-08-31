# LogAnalyzer

This is a Sublime Text 3 plugin. This plugin is intended to assist in analyzing logs. 
## Features

* Log colouring based on log level.
    * Errors – Red, Warnings – Yellow, Info – Blue and Debug – Grey. 
* Highlighting lines with particular patterns with different colours.
    * This can be used to mark important logs. Eg: “StartPreview called” “OnPeerListChanged event generated” etc.
* Filtering out patterns which we are not interested, in the logs.
    * This can be used to hide unnecessary logs from the view. Eg: Hide all ME logs while debugging peer related issue.
    * <mark>**Multiple pattern filtering is now supported.**</mark>

## Plan
* Auto reload from disk and scroll to end of file.
* <del>Multiple pattern filtering.</del> Done.

## Compatibility
Currently tested only with Sublime Text 3. May not work with Sublime Text 2. Please get the latest build of Sublime Text 3 before installation.

## Installation

1. Clone the repository in your Sublime Text *Packages* directory. Please note that the destination directory must be `LogAnalyzer`.
2. Open terminal in this folder and clone the repository.
3. Clone command `git clone https://gitlab.com/grhegde09/LogAnalyzer.git`   

The *Packages* directory locations are listed below. Alternatively, selecting `Preferences->Browse Packages` from Sublime Text menu will get you to the *Packages* directory.

| OS            | Packages location                                         |
| ------------- | --------------------------------------------------------- |
| OS X          | `~/Library/Application Support/Sublime Text 3/Packages/`  |
| Linux         | `~/.config/sublime-text-3/Packages/`                      |
| Windows       | `%APPDATA%\Sublime Text 3\Packages\`                      |


## Help on how to use this plugin can be found here: [LogAnalyzer:Help](https://gitlab.com/grhegde09/LogAnalyzer/tree/master/help)
You can also opn `Help` -> `LogAnalyzer - Help` to view help from within Sublime Text 3.
