import logging
logger = logging.getLogger('athenataf')
import time

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class InternalAuthenticated(ConfigurationTest):
	'''
		Test class for Internal Authentication of guest networks
	'''
	
	def _create_guest_network(self,wpa_wpa2=False):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.guest_network_info()
		security       = virtual_lan.use_vlan_defaults()
		if not wpa_wpa2:
			access   	   = security.configure_guest_security()
		else:
			access   	   = security.configure_guest_security(both=True)
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_591_createnetwork_guest(self):
		self._create_guest_network()
		
	def test_ath_593_createnetwork_guest_wpa_wpa2(self):
		self.NetworkPage.delete_network_if_present()
		self._delete_authenticated_server()
		network_page = self.LeftPanel.go_to_network_page()
		self.take_s1_snapshot()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.guest_network_info()
		security= virtual_lan.select_virtual_controller()
		access_page = security.create_wireless_guest_with_mac_auth_enabled()
		access_page.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self._delete_authenticated_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def _delete_authenticated_server(self):
		security_page = self.LeftPanel.go_to_security() 
		security_page.delete_authentication_server()
		security_page.delete_authentication_server2()
		security_page.delete_user_for_internal_server()
		
		
	def test_ath_592_internal_server_wpa_personal_two_external_server(self):
		self.NetworkPage.delete_network_if_present()
		self._delete_authenticated_server()
		network_page = self.LeftPanel.go_to_network_page()
		self.take_s1_snapshot()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.guest_network_info()
		security= virtual_lan.set_static_vlan()
		security.configure_wpa_personal_two_external_server()
		access_page = security.click_on_next()
		access_page.finish_network_setup()
		edit_network = self.NetworkPage.edit_network()
		edit_network.click_security_accordion()
		edit_network.set_guest_network_security_level_Splash_page_visuals_defaults()
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self._delete_authenticated_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		# self.assert_s1_s3_diff()
		# self.clear()
		
	def test_ath_596_one_external_radius_servers_wpa_2_peronsal_with_mac_auth_enabled(self):
		conf = self.config.config_vars
		network_page = self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self._delete_authenticated_server()
		network_page = self.LeftPanel.go_to_network_page()
		self.take_s1_snapshot()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.guest_network_info()
		security= virtual_lan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_Authenticated)
		security.set_mac_authentication_value('Enabled')
		security.set_delimiter()
		security.set_uppercase_support_dropdown()
		security.set_encryption('Enabled')
		security.set_security_key_management('WPA-2 Personal')
		security.set_pass_phrase_format('64 hexadecimal chars')
		security.set_passphrase_retype(conf.hexadecimal_64_char,conf.hexadecimal_64_char)
		time.sleep(5)
		security.create_external_radius_server_in_auth_server_one()
		#security.create_external_radius_server_in_auth_server_two()
		security.set_reauth_interval_options(conf.reauth_interval)
		security.create_security_internal_server_new_user()
		security.configure_blacklisting('Enable',conf.max_authentication_2)
		security.set_pass_phrase_format(conf.passphrase_frmt_8_63_char)
		security.configure_encryption('Enable',None,conf.Authentication_wpa2)
		access_page = security.move_to_next_page()
		access_page.finish_network_setup()
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self._delete_authenticated_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_598_two_external_radius_servers_both_wpa_wpa2(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self._delete_authenticated_server()
		network_page = self.LeftPanel.go_to_network_page()
		self.take_s1_snapshot()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.guest_network_info()
		security= virtual_lan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_Authenticated)
		security.create_external_radius_server_in_auth_server_one()
		security.create_external_radius_server_in_auth_server_two()
		security.set_load_balancing_field(conf.enable_option)
		security.configure_reauth_interval('2',conf.reauth_intrvl_unit_hrs)
		security.enable_accounting_interval('15')
		security.set_accounting_mode(False)
		security.configure_blacklisting('Enable',conf.max_authentication_2)
		security.set_encryption('Enabled')
		security.set_security_key_management(conf.Authentication_Wpa2_WPA_Enterprise)
		security.set_pass_phrase_format(conf.passphrase_frmt_8_63_char)
		security.set_passphrase_retype(conf.Auth_Sharedkey,conf.Auth_Sharedkey)
		access_page = security.move_to_next_page()
		access_page.finish_network_setup()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self._delete_authenticated_server()
		network_page = self.LeftPanel.go_to_network_page()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.guest_network_info()
		security= virtual_lan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_Authenticated)
		security.create_external_radius_server_in_auth_server_one()
		security.create_external_radius_server_in_auth_server_two()
		security.set_load_balancing_field(conf.enable_option)
		security.configure_reauth_interval('2',conf.reauth_intrvl_unit_hrs)
		security.enable_accounting_interval('15')
		security.set_accounting_mode(False)
		security.configure_blacklisting('Enable',conf.max_authentication_2)
		security.set_encryption('Enabled')
		security.set_security_key_management(conf.Authentication_Wpa2_WPA_Enterprise)
		security.set_pass_phrase_format(conf.pass_phrase_format_64_hexa_chars)
		security.set_passphrase_retype(conf.security_passphrase,conf.security_passphrase)
		access_page = security.move_to_next_page()
		access_page.finish_network_setup()
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self._delete_authenticated_server()		
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		# self.clear()
		
	def test_ath_590_internal_server_encryption_none(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		# self._delete_authenticated_server()
		network_page = self.LeftPanel.go_to_network_page()
		self.take_s1_snapshot()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_Authenticated)
		security.assert_none_spalsh_page_type_default_values()
		security.assert_internal_authenticated_fields()
		security.click_on_preview_splash_page()
		security.assert_splash_page_fields()
		security.click_on_preview_splash_page_close()
		access_page = security.click_on_next()
		access_page.finish_network_setup()
		self.LeftPanel.assert_delta_config_icon()
		self.take_s2_snapshot()
		self.LeftPanel.assert_delta_config_icon()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		# self._delete_authenticated_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		# self.assert_s1_s3_diff()
		# self.clear()
		
	def test_ath_594_internal_server_static_wep(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.NetworkPage.delete_custom_guest_network_if_present()
		network_page = self.LeftPanel.go_to_network_page()
		self.take_s1_snapshot()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.guest_network_info()
		virtual_lan.check_dynamic_vlan_attribute_list()
		virtual_lan.create_new_dynamic_vlan_assignment_rule(conf.Vlan_Rule_String1,conf.vlan_id_120)
		security = virtual_lan.click_on_next()
		security.setting_static_wep_with_password('128')
		security.edit_save_splash_page_details()
		access_page = security.click_on_next()
		access_page.finish_network_setup()
		network_page = self.LeftPanel.go_to_network_page()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.create_guest_network()
		virtual_lan.check_dynamic_vlan_attribute_list()
		virtual_lan.create_new_dynamic_vlan_assignment_rule(conf.Vlan_Rule_String1,conf.vlan_id_120)
		security = virtual_lan.click_on_next()
		security.setting_static_wep_with_password('64')
		security.edit_save_splash_page_details()
		access_page = security.click_on_next()
		access_page.finish_network_setup()
		self.LeftPanel.assert_delta_config_icon()
		self.take_s2_snapshot()
		self.LeftPanel.assert_delta_config_icon()
		edit_network = self.NetworkPage.edit_network()
		edit_network.click_security_accordion()
		edit_network.set_guest_network_security_level_Splash_page_visuals_defaults()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_custom_guest_network_if_present()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		# self.clear()