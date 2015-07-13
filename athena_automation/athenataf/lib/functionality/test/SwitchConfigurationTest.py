from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase
import logging
logger = logging.getLogger('athenataf')

class SwitchConfigurationTest(AthenaGUITestCase):

	def __init__(self, config):
		super(SwitchConfigurationTest, self).__init__(config)
		self.SwitchesPage = None
		self.config = config

	def setUpTestClass(self):
		logger.debug("SwitchConfigurationTest: setUpTestClass")    
		AthenaGUITestCase.setUpTestClass(self)
		# logger.debug("SwitchConfigurationTest: Go To SwitchConfiguration.")
		# switch_page = self.LeftPanel.go_to_switch_configuration()
		# logger.debug("ConfigurationTest: Go To Network.")
		# self.SwitchesPage = switch_page.go_to_switches()

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
			time.sleep(10)
		self.LeftPanel.switch_configuration.click()