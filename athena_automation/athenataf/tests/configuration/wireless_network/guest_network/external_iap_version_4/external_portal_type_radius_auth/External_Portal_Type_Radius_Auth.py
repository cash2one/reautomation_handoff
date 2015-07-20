import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest
import time

class External_Portal_Type_Radius_Auth(ConfigurationTest):
	'''
	Test class for Guest Network -> External_Iap_Version_4
	'''
	
	def test_ath_7192_external_portal_radius_authenticatoin_with_https_internalauth_none(self):
		self._delete_captive_role_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.use_vlan_defaults()
		security.set_splash_page_type('External')
		security.create_external_captive_portal_1()
		security.assert_captive_external_splash_page_type_fields()
		security.add_internal_sever_user()
		access = security.move_to_next_page()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self._delete_captive_role_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def _delete_captive_role_if_present(self):
		self.NetworkPage.delete_network_if_present()
		self.NetworkPage.delete_wired_network_if_present()
		self.NetworkPage.delete_custom_guest_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_authentication_server()
		security_page.delete_authentication_server2()
		security_page.delete_internal_server()
		security_page.click_walled_garden_accordion()
		security_page.click_walled_garden_link()
		if 	security_page.blacklist_delete_domain:
			security_page.blacklist_delete_domain.click()
		if security_page.whitelist_delete:
			security_page.whitelist_delete.click()
		if security_page.walled_save:
			security_page.walled_save.click()	
		security_page.click_on_external_captive_accordion()
		security_page.delete_external_captive_portal_2()
		security_page.delete_captive_portal()
		time.sleep(5)	
		self.LeftPanel.go_to_network_page()
		
		
	def test_ath_7193_external_portal_radius_authenticatoin_internal_auth_with_mac_none(self):
		conf = self.config.config_vars
		self._delete_captive_role_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.use_vlan_defaults()
		security.set_splash_page_type('External')
		security.create_external_captive_portal_1(https=False)
		security.configure_auth_server_settings(mac_authentication=True,uppercase_support=True,blacklisting=True)
		security.set_max_auth_failures_value(conf.max_authentication_failure)
		security.set_delimiter()
		security.assert_auth_server1_selected_option(conf.InternalServer)
		security.add_internal_sever_user()
		security.create_walled_garden_white_and_blacklist()
		access = security.move_to_next_page()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self._delete_captive_role_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_7194_external_portal_radius_authenticatoin_single_external_auth_server_with_mac_wpa2(self):
		conf = self.config.config_vars
		self._delete_captive_role_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.use_vlan_defaults()
		security.set_splash_page_type('External')
		security.create_external_captive_portal_1(https=False)
		security.configure_auth_server_settings(mac_authentication=True)
		security.set_delimiter_characrter(conf.hyphen)
		security.create_external_radius_server_in_auth_server_one()
		security.assert_authentication_server2('Select')
		security.set_reauth_interval_options(conf.reauth_30)
		self.browser.assert_element(security.blacklist_whitelist, "blacklisting not set to default value")
		security.set_encryption(conf.enable_option)
		security.set_security_key_management(conf.Authentication_wpa2)
		security.set_pass_phrase_format(conf.pass_phrase_format_64_hexa_chars)
		security.set_passphrase_retype(conf.passphrase_hex_num_valid,conf.passphrase_hex_num_valid)
		access = security.move_to_next_page()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self._delete_captive_role_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	
		
	def test_ath_8375_edit_a_profile_type_of_a_external_captive_portal(self):
		conf = self.config.config_vars
		self._delete_captive_role_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.click_on_next()
		security.assert_splash_page_required_fields()
		access = security.create_captive_portal_profile(True,True)
		access.finish_network_setup()
		self.take_s2_snapshot()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.click_security_accordion()
		edit_network_page.click_captive_portal_edit_link()
		edit_network_page.set_auth_text('')
		edit_network_page.set_cative_portal_type()
		edit_network_page.save_captive_profile_button()
		edit_network_page._save_settings()
		self.LeftPanel.go_to_network_page()
		self._delete_captive_role_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def _delete_network_auth_server(self):
		'''
		Delete wireless and auth servers 
		'''
		self.NetworkPage.delete_network_if_present()
		self.NetworkPage.delete_wired_network_if_present()
		self.NetworkPage.delete_custom_guest_network_if_present()
		security_page = self.LeftPanel.go_to_security() 
		security_page.delete_authentication_server()
		security_page.delete_authentication_server2()
		security_page.click_walled_garden_accordion()
		security_page.click_walled_garden_link()
		if 	security_page.blacklist_delete_domain:
			security_page.blacklist_delete_domain.click()
		if security_page.whitelist_delete:
			security_page.whitelist_delete.click()
		if security_page.walled_save:
			security_page.walled_save.click()
		time.sleep(5)	
		security_page.click_on_external_captive_accordion()
		security_page.delete_external_captive_portal_2()
		security_page.delete_captive_portal()
		time.sleep(5)	
		self.LeftPanel.go_to_network_page()		
		
	def test_ath_7197_Portal_radius_authenticatoin_with_https_single_external_auth_server_with_mac_static_wep(self):
		conf = self.config.config_vars
		self._delete_captive_role_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.create_security_captive_portal_profile()
		security.enable_mac_authentication1()
		security.configure_auth_server_settings(uppercase_support = True)
		security.configure_reauth_interval(conf.cache_timeout_default, conf.reauth_intrvl_unit_hrs)
		security.configure_blacklisting(False,False)
		security.set_external_radius_server_1()
		security.create_blacklist_whitelist_walled_garden()
		security.configure_encryption('Enabled','Static WEP', False)
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self._delete_captive_role_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def _delete_network_auth_servers_blacklist_whitelist(self):
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security() 
		security_page.delete_authentication_server()
		security_page.delete_2_external_servers()
		security_page = self.LeftPanel.go_to_security() 
		security_page.click_walled_garden_accordion()
		security_page.click_walled_garden_link()
		security_page.delete_blacklist_domain()
		security_page.click_walled_garden_link()
		security_page.delete_whitelist_domain()
		security_page.click_on_external_captive_protal_button()
		security_page.delete_captive_portal()
		self.LeftPanel.go_to_network_page()

	