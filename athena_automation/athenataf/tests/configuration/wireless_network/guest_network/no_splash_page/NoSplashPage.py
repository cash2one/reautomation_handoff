import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class NoSplashPage(ConfigurationTest):
	'''
	Test class for No Splash Page
	'''

	def test_ath_607_create_wireless_guest_network_profile_with_splash_type_as_none_and_encryption_none(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_none)
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.click_on_security_accordion()
		edit_network_page.assert_splash_page_option(conf.Splash_page_none)
		network_page = self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_608_create_wireless_guest_network_profile_with_splash_type_as_none_and_encryption_wpa_2_personal(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_none)
		security.configure_encryption('Enabled','none',conf.Authentication_wpa2)
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.click_on_security_accordion()
		edit_network_page.assert_splash_page_option(conf.Splash_page_none)
		edit_network_page.assert_on_security_key_management(conf.Authentication_wpa2)
		network_page = self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_609_create_wireless_guest_network_profile_with_splash_type_as_none_and_encryption_wpa_personal(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_none)
		security.configure_encryption('Enabled','none',conf.wpa_personal)
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.click_on_security_accordion()
		edit_network_page.assert_splash_page_option(conf.Splash_page_none)
		edit_network_page.assert_on_security_key_management(conf.wpa_personal)
		network_page = self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_610_create_wireless_guest_network_profile_with_splash_type_as_none_and_encryption_mixed_WPA_WPA2(self):
		self.NetworkPage.delete_network_if_present()
		conf = self.config.config_vars
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan = basic_info.guest_network_info()
		security = vlan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_none)
		security.configure_blacklisting('Enabled','10')
		security.configure_encryption('Enabled','none',conf.security_key_management)
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.click_on_security_accordion()
		edit_network_page.assert_splash_page_option('None')
		edit_network_page.assert_on_security_key_management(conf.Wpa2_WPA_Enterprise)
		network_page = self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_611_create_wireless_guest_network_profile_with_splash_type_as_none_and_encryption_static_WEP(self):
		self.NetworkPage.delete_network_if_present()
		conf = self.config.config_vars
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan = basic_info.guest_network_info()
		security = vlan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_none)
		security.configure_blacklisting('Enable','10')
		security.configure_encryption('Enabled',conf.key_mngmt_static,'none')
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.click_on_security_accordion()
		edit_network_page.assert_splash_page_option('None')
		edit_network_page.assert_on_security_key_management(conf.static_wep_value)
		network_page = self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_612_create_wireless_guest_network_profile_with_splash_type_as_none_and_encryption_mixed_WPA_WPA2(self):
		self.NetworkPage.delete_network_if_present()
		conf = self.config.config_vars
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan = basic_info.guest_network_info()
		security = vlan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_none)
		security.configure_encryption('Enabled','none',conf.security_key_management)
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.click_on_security_accordion()
		edit_network_page.assert_splash_page_option('None')
		edit_network_page.assert_on_security_key_management(conf.Wpa2_WPA_Enterprise)
		network_page = self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8373_edit_a_pre_auth_role_only_enabled_network(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.click_on_next()
		access = security.use_security_default()
		access.click_role_access()
		access.enable_pre_authentication_role1()
		access.finish_network_setup()
		self.take_s2_snapshot()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.click_vlans_accordion()
		edit_network_page.click_network_assigned()
		edit_network_page._save_settings()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		