import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DefaultValueCheck(ConfigurationTest):
	'''
	Test class for System DefaultValueCheck.
	'''
	def test_ath_11380_check_default_value_of_proxy(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_proxy_tab()
		system_page.assert_default_proxy_value()
		system_page.click_on_proxy_exception_cancel()