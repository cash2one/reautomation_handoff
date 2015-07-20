import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest
import time

class ExternalRadiusServer(ConfigurationTest):
	'''
	Test class for External Radius Server
	'''

	def test_ath_6811_two_external_auth_server_with_mac_auth(self):
		conf = self.config.config_vars
		self._delete_network_auth_server()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.set_splash_page_type_value('External')
		security.configure_encryption('Enabled','WPA 2 Personal', conf.Authentication_wpa2)
		security.creating_two_external_auth_server_with_mac_auth()
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.click_on_external_captive_protal_button()
		security_page.delete_captive_portal()
		self.LeftPanel.go_to_network_page()
		self._delete_network_auth_server()
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
		security_page.delete_internal_server()
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
		security_page.click_on_external_captive_accordion()
		security_page.delete_external_captive_role()
		time.sleep(5)	
		self.LeftPanel.go_to_network_page()
		
	def test_ath_618_mac_auth_enabled_wpa2(self):
		conf = self.config.config_vars
		self._delete_network_auth_server()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.set_splash_page_type_value('External')
		security.enable_mac_authentication()
		security.create_external_radius_server_in_auth_server_one()
		security.select_auth_server_internalserver('2')
		security.add_internal_sever_user()
		security.set_load_balancing_field(conf.enable_option)
		security.set_wispr('Enabled')
		security.set_accounting_mode(conf.accounting_mode_association)
		security.enable_accounting_interval(conf.reauth_interval10)
		security.configure_encryption('Enabled',False,conf.Authentication_wpa2)
		security.create_captive_portal_profile_with_whitelisting_enabled()
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self._delete_network_auth_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_617_static_wep(self):
		conf = self.config.config_vars
		self._delete_network_auth_server()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.set_splash_page_type_value('External')
		security.configure_encryption('Enabled','Static WEP', False)
		security.set_wep_key_size(conf.wep_key_size)
		security.set_captive_portal_profile('-- New --')
		security.set_captive_name(conf.Captive_Role_Name)
		security.set_captive_ip(conf.Captive_Role_Ip)
		security.set_use_https('uncheck')
		security.set_captive_url(conf.domain_name)
		security.set_captive_port(conf.Captive_Role_Port)
		security.set_secuirty_auto_url_whitelisting('check')
		security.set_security_captive_portal_failure(conf.external_captive_portal_failure)
		security.click_on_captive_portal_profile_save()
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self._delete_network_auth_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	
	def test_ath_616_both_wpa_and_wpa2_two_radius_servers(self):
		self._delete_network_auth_server()
		conf = self.config.config_vars
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.set_wispr('Enabled')
		security.create_external_radius_server_in_auth_server_one()
		security.set_reauth_interval_value(conf.background_wmm)
		security.set_accounting_mode()
		security.configure_blacklisting('Enable',conf.tx4)
		security.set_disable_if_uplink_type_is(True,True,True)
		security.configure_encryption('Enabled',False,conf.Authentication_Wpa2_WPA_Enterprise)
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self._delete_network_auth_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_613_encryption_none(self):
		conf = self.config.config_vars
		self._delete_network_auth_server()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_external)
		security.set_captive_portal_profile('default')
		security.add_internal_sever_user()
		access = security.use_security_default()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self._delete_network_auth_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_614_wpa_personal(self):
		conf = self.config.config_vars
		self._delete_network_auth_server()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_external)
		security.create_external_radius_server_in_auth_server_one()
		security.enable_accounting_interval('10')
		security.set_accounting_mode()
		security.set_encryption(conf.wireless_encryption)
		security.set_security_key_management(conf.Authentication_wpa2)
		security.set_passphrase_retype(conf.Auth_Sharedkey,conf.Auth_Sharedkey)
		security.create_external_captive_portal_1(whitelisting=False)
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self._delete_network_auth_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_615_external_portal_radius_authenticatoin_with_https_internalauth_none(self):
		conf = self.config.config_vars
		self._delete_network_auth_server()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.use_vlan_defaults()
		security.set_splash_page_type('External')
		security.create_external_captive_portal_1()
		security.set_wispr('Enabled')
		security.set_encryption(conf.enable_option)
		security.set_security_key_management(conf.Authentication_wpa2)
		security.set_pass_phrase_format(conf.pass_phrase_format_8_63_chars)
		security.set_passphrase_retype(conf.Auth_Sharedkey,conf.Retype_auth_shared_key)
		security.create_external_radius_server_in_auth_server_one()
		security.create_external_radius_server_in_auth_server_two()
		security.set_load_balancing_field('Enabled')
		security.set_reauth_interval_options(conf.reauth_40)
		security.enable_accounting_interval(conf.max_auth_failure_valid_num)
		security.set_accounting_mode()
		security.create_walled_garden_white_and_blacklist()
		access = security.move_to_next_page()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		self._delete_network_auth_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
		
	def _delete_captive_role_if_present(self):
		self.NetworkPage.delete_network_if_present()
		self.NetworkPage.delete_wired_network_if_present()
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
		if security_page.is_external_captive_profile_present():
			security_page.delete_external_captive_role()
		self.LeftPanel.go_to_network_page()
	
		
	def test_ath_3865_shared_password_validation(self):
		conf = self.config.config_vars
		self._delete_network_auth_server()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_Acknowledged)
		security.set_encryption('Enabled')
		# security.set_captive_portal_profile('default')
		security.set_security_key_management(conf.Authentication_wpa2)
		security.set_pass_phrase_format(conf.pass_phrase_format_8_63_chars)
		security.validate_passphrase_8_to_63_chars()
		security.set_pass_phrase_format(conf.pass_phrase_format_64_hexa_chars)
		security.validate_passphrase_64_hex_chars()		