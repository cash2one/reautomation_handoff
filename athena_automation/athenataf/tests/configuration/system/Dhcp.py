import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Dhcp(ConfigurationTest):
	'''
	Test class for System DHCP.
	'''
	
	def test_ath_1428_dhcp_non_default_values(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_dhcp_tab()
		system_page.set_dhcp_values()
	
	def test_ath_8326_assert_dhcp_default_values(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_dhcp_tab()
		system_page.assert_dhcp_default_values()
	
	def test_ath_11338_check_dhcp_default_values(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_dhcp_tab()
		system_page.assert_dhcp_default_values()