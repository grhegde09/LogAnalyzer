from collections import OrderedDict
import sublime, sublime_plugin,json,os,webbrowser

masterEraseDictionary = OrderedDict()
config = None

def plugin_loaded():
	settings = sublime.load_settings('LogAnalyzer.sublime-settings')
	global config
	config  = settings.get('config','{"config":{"highlighterPreferences":{"highlightPatterns":[{"searchRegex":"DefaultHighlightPattern1","style":1},{"searchRegex":"DefaultHighlightPattern2","style":2}]},"filterPreferences":{"isFilteringEnabled":true,"filterPatterns":["DefaultFilterPattern1","DefaultFilterPattern2"]}}}' )

class HighlightLinesCommand(sublime_plugin.TextCommand):

	def HighlightLines(self,edit,searchString,style):
		allOccurances = self.view.find_all(searchString)
		for occurance in allOccurances:
			rowNum,colNum = self.view.rowcol(occurance.begin())
			self.view.add_regions(str(rowNum),self.view.lines(occurance),"studiolog.style"+str(style),"bookmark")

	def run(self, edit):
		plugin_loaded()
		for pattern in config['highlighterPreferences']['highlightPatterns']:
			self.HighlightLines(edit,pattern['searchRegex'],pattern['style'])

class UndoHighlightLinesCommand(sublime_plugin.TextCommand):

	def UndoHilightLines(self,edit,searchString):
		allOccurances = self.view.find_all(searchString)
		rowNum = 0
		for occurance in allOccurances:
			rowNum,colNum = self.view.rowcol(occurance.begin())
			self.view.erase_regions(str(rowNum))
		pass

	def run(self,edit):
		print ("Highlight Clear called")
		plugin_loaded()
		for pattern in config['highlighterPreferences']['highlightPatterns']:
			self.UndoHilightLines(edit,pattern['searchRegex'])


class EraseLinesCommand(sublime_plugin.TextCommand):

	def EraseLines(self,edit,stringToErase):
		lastEraseLineRegion = None
		eraseDictionary =  OrderedDict()
		allOccurances = self.view.find_all(stringToErase)
		# A little too complicated. Let us not get into how it is done. Will clean it up when possible. Promise.
		for occurance in reversed(allOccurances):
			if lastEraseLineRegion:
				doesLastEraseCoverThisRegion = lastEraseLineRegion.contains(occurance)
				if doesLastEraseCoverThisRegion:
					continue
			eraseLineRegion = self.view.full_line(occurance)	
			lastEraseLineRegion = eraseLineRegion
			stringToBeErased = self.view.substr(eraseLineRegion)
			eraseBeginPoint = eraseLineRegion.begin()
			eraseDictionary[eraseBeginPoint] = stringToBeErased;
			self.view.erase(edit,eraseLineRegion)
		return eraseDictionary

	def run(self, edit):
		print ("erase called")
		plugin_loaded()
		if len(masterEraseDictionary) > 0:
			pass
		else:
			if config['filterPreferences']['isFilteringEnabled'] is True:
				for pattern in config['filterPreferences']['filterPatterns']:
					masterEraseDictionary[pattern]= self.EraseLines(edit,pattern)
			else:
				sublime.message_dialog("Filtering is disabled. You can change it in LogAnalyzer settings.")
			# Timeout for save! Why God ? Why !?
			sublime.set_timeout(lambda: self.view.run_command("save"), 10)

class UndoEraseLinesCommand(sublime_plugin.TextCommand):

	def UndoEraseLines(self,edit,eraseDictionary):
		orderedEraseDictionary = OrderedDict(sorted(eraseDictionary.items(), key=lambda t: t[0]))
		for point,textToInsert in orderedEraseDictionary.items():
			self.view.insert(edit,point,textToInsert)
		eraseDictionary.clear()	

	def run(self, edit):
		print ("undo erase called")
		plugin_loaded()
		if config['filterPreferences']['isFilteringEnabled'] is True:
			if len(masterEraseDictionary) == 0:
				pass
			else:
				#orderedMasterEraseDictionary! TODO: Come up with a better name later.
				orderedMasterEraseDictionary = OrderedDict(sorted(masterEraseDictionary.items(),  reverse=True))
				for pattern in orderedMasterEraseDictionary:
					print(pattern)
					self.UndoEraseLines(edit,orderedMasterEraseDictionary[pattern])
				masterEraseDictionary.clear()
				sublime.message_dialog("All filtered lines have been restored. Please save the file.")
		else:
			sublime.message_dialog("Filtering is disabled. You can change it in LogAnalyzer settings.")
		sublime.set_timeout(lambda: self.view.run_command("save"), 0)

class OpenLogAnalyzerHelpInBrowserCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		webbrowser.open('https://gitlab.com/grhegde09/LogAnalyzer/tree/master/help', new=2, autoraise=True)