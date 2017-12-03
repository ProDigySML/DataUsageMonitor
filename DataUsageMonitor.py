"""
Description: Data usage monitor for Burp
Author: Sajeeb Lohani (sml555)
"""

from burp import IBurpExtender
from burp import ITab
from burp import IHttpListener
from burp import IBurpExtenderCallbacks
from javax.swing import JPanel;
from javax.swing import JLabel;
from javax.swing import JButton;

class BurpExtender(IBurpExtender, ITab, IHttpListener):
	
	def registerExtenderCallbacks(self, callbacks):
		'''
		Description: Required for implementing Burp Extender.
		Param: callbacks: Burp callbacks within Extender
		'''
		# keep a reference to our callbacks object
		self._callbacks = callbacks
		
		# obtain an extension helpers object
		self._helpers = callbacks.getHelpers()
		
		# set our extension name
		callbacks.setExtensionName("Data Usage Monitor")
		
		self._init_gui()

		# register ourselves as an HTTP listener
		callbacks.registerHttpListener(self)
		
		# add the custom tab to Burp's UI
		callbacks.addSuiteTab(self)
		
		# the actual data usage monitor counter
		self.counter = 0
		
		return
		
	def _init_gui(self):
		'''
		Description: Initialises the GUI for the application
		'''
		self.tab = JPanel()
		
		self.label = JLabel("Data Usage: 0B")
		
		self.reset = JButton("Reset Counter", actionPerformed=self._reset_counter)
		
		self.tab.add(self.label)
		
		self.tab.add(self.reset)
		
		return
	
	def getTabCaption(self):
		'''
		Description: Gets the caption within the tab
		'''
		return "Data Usage"
	
	def getUiComponent(self):
		'''
		Description: Gets the tab set up in the UI initialisation component
		'''
		return self.tab
		
	def _reset_counter(self, e=None):
		'''
		Description: Resets the counter and updates the UI to replicate the reset
		Param: e: Event object
		'''
		self.counter = 0
		self._update_gui()
		
	def _update_gui(self):
		'''
		Description: Calculates the amount of usage based on the counter and allots into their respective category of size
		'''
		if self.counter < 1024:
			self.label.text = "Data Usage: " + str(self.counter) + "B"
		elif self.counter < (1024 ** 2):
			self.label.text = "Data Usage: " + str(self.counter / 1024) + "KB"
		elif self.counter < (1024 ** 3):
			self.label.text = "Data Usage: " + str(self.counter / (1024 ** 2)) + "MB"
		elif self.counter < (1024 ** 4):
			self.label.text = "Data Usage: " + str(self.counter / (1024 ** 3)) + "GB"
		elif self.counter < (1024 ** 5):
			self.label.text = "Data Usage: " + str(self.counter / (1024 ** 4)) + "TB"
		
		return 0
	
	def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
		'''
		Description: Processes all messages that are sent through Burp. We use it to get the length of both the request and the response
		Param: toolFlag: Enum: Tells which part of burp the request came from
		Param: messageIsRequest: Boolean: Lets you know if the message is a request or a response
		Param: messageInfo: RequestResponse Object: Holds both the request and the response
		'''
		
		if messageIsRequest:
			return
		
		self.counter += len(messageInfo.getRequest())

		self.counter += len(messageInfo.getResponse())
		
		self._update_gui()
