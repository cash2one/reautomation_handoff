import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class GuestNetwork(ConfigurationTest):
	'''
	Test class for GuestNetwork
	'''

		
	def test_ath_6840_group_with_mixed_version_iaps(self):
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.assert_splash_page_type_disabled_option()
		
	def test_ath_6790_default_wireless_guest_profile_configuration(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.assert_default_wireless_guest_fields()
		logger.debug('Network :SecurityPage : capitive Redirect Url textbox : Empty')	
		self.browser.assert_text(security.Secuirty_redirect_url, '', "capitive Redirect Url textbox not Empty by default", "value")
		security.assert_splas_page_visuals_fields()