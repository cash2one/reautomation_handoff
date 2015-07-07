import logging
logger = logging.getLogger('athenataf')
import time

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class SecurityTestingEnhancement(ConfigurationTest):
	'''
	Test class for network configuration SecurityTestingEnhancement.
	'''
	
	def test_ath_10865_default_wireless_guest_profile_configuration(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.click_on_next()
		security.assert_wired_guest_network_security_level_defaults()
		security.assert_splash_page_visuals_disabled()
		access = security.return_acces_page()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()