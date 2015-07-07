import os
from athenataf.lib.test.TestCase import TestCase
from athenataf.lib.functionality.page.common.LoginPage import LoginPage
from athenataf.lib.functionality.page.common.LogoutPage import LogoutPage
from athenataf.lib.util.WebPage import WebPage
from athenataf.lib.functionality.page.common.TopPanel import TopPanel
from athenataf.lib.functionality.page.common.LeftPanel import LeftPanel
from athenataf.lib.util.Browser import *

import logging
logger = logging.getLogger('athenataf')    

class WebDriverTestCase(TestCase,WebPage):
    
	def __init__(self, config):
		logger.debug("Initializing Test Case:: %s" % self.__class__.__name__)
		super(WebDriverTestCase, self).__init__(config)
		self.browser = None
		self.current_test_method = None
		self.current_test_id = None
		self.current_screen_shots = {}

	def start_browser(self):
		self.browser = Browser(self.config.options.browser.lower())		

	def take_screenshot(self):
		try:
			if self.browser is not None:
				logger.debug("Taking snapshot")
				counter = 1
				if self.current_screen_shots.has_key(self.current_test_method):
					counter = len(self.current_screen_shots[self.current_test_method]) + 1				
				file_name = "%s_%s_%s_%d.png" % (self.current_test_id,self.__class__.__name__, self.current_test_method, counter)
				screenshot_file = os.path.join(self.config.screenshots_dir, file_name)
				logger.debug("Snapshot file: %s" % screenshot_file)			
				self.browser.get_screenshot_as_file(screenshot_file)	
				logger.debug("Snapshot taken")
				if not self.current_screen_shots.has_key(self.current_test_method):
					self.current_screen_shots[self.current_test_method] = [file_name]
				else:
					self.current_screen_shots[self.current_test_method].append(file_name)				
			else:
				logger.debug("Browser is not set. No screenshot would be taken.")
		except Exception, e:
			logger.error("Error while taking snapshot: %s" % str(e))
			import traceback
			logger.debug(traceback.format_exc())
        
	def on_fail(self):
		self.take_screenshot()
		self.current_test_method = None
		self.current_test_id = None		
		
	def on_error(self):
		self.take_screenshot()
		self.current_test_method = None
		self.current_test_id = None		

	def setUpTestClass(self):
		self.current_screen_shots = {}	

	def tearDownTestClass(self):
		pass

	def assertPageLoaded(self, page_name, msg=None):
		msg = msg or ""
		if page_name.isPageLoaded():
			logger.debug("Page Loaded Successfully")
		else:
			raise AssertionError("%s.\n%s Page does not get loaded" % (msg, page_name))

	def assertElementNotNone(self, element, msg=None):
		msg = msg or ""
		if element is None:
			raise AssertionError("%s.\nElement is None.")

	def assertTextInPage(self, text, msg=None):
		msg = msg or ""
		if self.browser.getPageSource().find(text) == -1:
			raise AssertionError("%s.\nText not found in HTML source: %s" % (msg,text))

	def stop_browser(self):
		if self.browser is not None:
			logger.debug("Closing browser")
			self.browser.close()
		else:
			logger.debug("Browser is None.")