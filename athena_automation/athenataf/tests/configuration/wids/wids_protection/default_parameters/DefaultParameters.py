import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DefaultParameters(ConfigurationTest):
	'''
		Test class for Default Parameters.
	'''
	
	def test_ath_8170_default_wids_protection_settings(self):
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.assert_infrastructure_clients_protection()
		
	def test_ath_8638_check_wired_wireless_containment(self):
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.assert_wired_wireless_containment()
		
	def test_ath_11162_default_wids_protection_settings(self):
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.assert_infrastructure_clients_protection()
		