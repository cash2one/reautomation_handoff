from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase
from athenataf.lib.functionality.page.configuration.network.NetworkPage import NetworkPage

import logging
logger = logging.getLogger('athenataf')    

class ConfigurationTest(AthenaGUITestCase):

	def __init__(self, config):
		super(ConfigurationTest, self).__init__(config)
		self.NetworkPage = None
		self.config = config

	def setUpTestClass(self, IAP=False):
		logger.debug("ConfigurationTest: setUpTestClass")	
		AthenaGUITestCase.setUpTestClass(self, IAP)
		if not IAP:
			logger.debug("ConfigurationTest: Go To Configuration.")
			all_group_page = self.LeftPanel.go_to_configuration()
			logger.debug("ConfigurationTest: Go To Network.")
			self.NetworkPage = all_group_page.go_to_networks()

	def assertPageLoaded(self, page_name, msg=None):
		msg = msg or ""
		if page_name.isPageLoaded():
			logger.debug("Page Loaded Successfully")
		else:
			raise AssertionError("%s.\n%s Page does not get loaded" % (msg, page_name))

	def tearDown(self):
		self.browser.refresh()
		if self.LeftPanel.save_pop_up:
			self.LeftPanel.save_pop_up.click()
			import time
			time.sleep(15)
		# self.LeftPanel.assert_delta_config_icon()
		self.LeftPanel.configuration.click()