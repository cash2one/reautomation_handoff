import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class NegativeTestScenarios(ConfigurationTest):
	'''
	Test class for NegativeTestScenarios test cases of configuration module.
	'''
	
	def test_ath_10988_empty_password_for_open_dns(self):
		services_page = self.LeftPanel.go_to_services()
		services_page.assert_open_dns_empty_password()
		services_page.assert_open_dns_passwrd_with_blanks_inbetween()
		
	def test_ath_11019_calea_ip_addr_with_preceding_zeros(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.conifgure_calea_ip_address_with_preceding_zeros()
		services_page.assert_calea_ip_address_with_preceding_zeros()
		self.take_s2_snapshot()
		services_page.clear_calea_ip_address()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()