import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DefaultValueCheck(ConfigurationTest):
	'''
		Test class for Default Value Check under System module.
	'''

	def test_ath_11341_check_uplink_default_values(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.click_uplink()
		system_page.assert_3g_4g_default_value()
		system_page.assert_wi_fi_default_value()
		system_page.assert_management_default_value()
		system_page.assert_pppoe_default_value()
		
