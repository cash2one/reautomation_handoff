import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest
import time

class ExternalIAPVersion4(ConfigurationTest):
	'''
	Test class for External IAP Version 4
	'''

	def test_ath_7182_multiple_captive_portal_page(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security() 
		security_page.click_on_external_captive_protal_button()
		security_page.create_new_captive_portal_1(conf.captive_text_1,conf.captive_role_type,conf.Captive_Role_Ip,conf.redirect_url,conf.Captive_Role_Port,auth_text=None,http1=True)
		security_page.create_new_captive_portal_1(conf.captive_text_2,conf.captive_role_type,conf.Captive_Role_Ip,conf.redirect_url,conf.Captive_Role_Port,auth_text=None,http1=False)
		security_page.create_new_captive_portal_1(conf.auth_server_name_value,conf.Captive_Role_Text,conf.Captive_Role_Ip,conf.redirect_url,conf.Captive_Role_Port,conf.Captive_Role_Text,http1=False)
		security_page.create_new_captive_portal_1(conf.captive_text_3,conf.Captive_Role_Text,conf.Captive_Role_Ip,conf.redirect_url,conf.Captive_Role_Port,conf.Captive_Role_Text,http1=False)
		security_page.save_settings()
		self.LeftPanel.go_to_network_page()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_external)
		security.edit_captive_portal_profile()
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		security_page = self.LeftPanel.go_to_security() 
		security_page.click_on_external_captive_protal_button()
		security_page.asserting_captive_portal()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security() 
		security_page.click_on_external_captive_protal_button()
		security_page.delete_external_captive_portal_2()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_7171_auth_text_portal_profile_user_radius_failover_with_wpa2_encryption(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.create_security_captive_portal_profile()
		security.create_external_radius_server_in_auth_server_one()
		security.create_external_radius_server_in_auth_server_two()
		security.configure_blacklisting("Enable",conf.max_authentication_failure)
		security.configure_auth_server_settings(accounting_enable=True,balancing=True)
		security.set_reauth_interval_options(conf.reauth_interval_145)
		security.set_encryption("Enabled")
		security.set_security_key_management("WPA-2 Personal")
		security.set_pass_phrase_format('64 hexadecimal chars')
		security.set_passphrase_retype(conf.hexadecimal_64_char,conf.hexadecimal_64_char)
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		self._delete_network_auth_server()
		security_page = self.LeftPanel.go_to_security()
		security_page.click_on_external_captive_protal_button()
		security_page.delete_captive_portal()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
		
	def test_ath_7168_external_auth_type_profile_internal_user_auth_with_mac(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.click_on_external_captive_protal_button()
		security_page.delete_captive_portal()
		self.LeftPanel.go_to_network_page()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.set_encryption('Disabled')
		security.create_security_captive_portal_profile()
		security.add_internal_sever_user()
		security.set_auth_interval_time('10')
		security.set_mac_authentication_value('Enabled')
		security.set_delimiter()
		security.set_uppercase_support_dropdown()
		security.configure_blacklisting('Enable',conf.max_authentication_failure)
		security.create_walled_garden_white_and_blacklist()
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		self._delete_network_auth_server()
		security_page = self.LeftPanel.go_to_security()
		security_page.click_on_external_captive_protal_button()
		security_page.delete_captive_portal()
		
		security_page = self.LeftPanel.go_to_security() 
		security_page.click_walled_garden_accordion()
		
		security_page.click_walled_garden_link()
		security_page.delete_edited_blacklist_domain()
		security_page.delete_edited_whitelist_domain()
		
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
		import time
		time.sleep(5)
		self.LeftPanel.go_to_network_page()

	def test_ath_7174_external_wipsr_enabled_auth_text_captive_portal_profile_user_auth_two_radius_server(self):
		conf = self.config.config_vars
		self._delete_network_auth_server()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_external)
		security.set_wired_captive_portal_value()
		security.set_wispr('Enabled')
		security.create_external_radius_server_in_auth_server_one()
		security.create_external_radius_server_in_auth_server_two()
		security.configure_blacklisting('Disabled','')
		logger.debug('Network : SecurityPage : Configuring Accounting mode as Association ')
		security.accounting_mode.set(conf.acct_mode_association)
		logger.debug('EditNetworkPage :Set Accouting Interval :5 mins')
		security.accounting_interval.set(conf.max_auth_failure_valid_num)
		logger.debug("SecurityPage : Writing valid numbers in reauth interval text-box...")
		security.reauth_interval.set(self.config.config_vars.reauth_intrvl_num_valid)
		security.create_blacklist_whitelist_walled_garden()		
		security.configure_encryption('Enabled','none',conf.Authentication_wpa_wpa2)
		access = security.click_on_next()
		access.finish_network_setup()
		self.LeftPanel.assert_delta_config_icon()
		self.take_s2_snapshot()
		self.NetworkPage.assert_new_network()
		self._delete_network_auth_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_7173_external_wipsr_enabled_auth_text_captive_portal_profile(self):
		conf = self.config.config_vars
		self._delete_network_auth_server()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_external)
		security.set_wired_captive_portal_value()
		security.set_wispr('Enabled')
		security.create_external_radius_server_in_auth_server_one()
		security.configure_blacklisting('Enable','5')
		logger.debug('Network : SecurityPage : Configuring Accounting mode as Association ')
		security.accounting_mode.set(conf.acct_mode_association)
		logger.debug('Network : SecurityPage : Set Accouting Interval :30 mins')
		security.accounting_interval.set(conf.thirty)
		logger.debug("SecurityPage : Writing valid numbers in reauth interval text-box...")
		security.reauth_interval.set(self.config.config_vars.fifteen)
		security.create_blacklist_whitelist_walled_garden()		
		security.configure_encryption('Enabled','none',conf.Authentication_wpa2)
		access = security.click_on_next()
		access.finish_network_setup()
		self.LeftPanel.assert_delta_config_icon()
		self.take_s2_snapshot()
		self.NetworkPage.assert_new_network()
		self._delete_network_auth_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_7172_external_wipsr_enabled_auth_text_captive_portal_profile(self):
		conf = self.config.config_vars
		self._delete_network_auth_server()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_external)
		security.create_captive_portal_profile(text = True,ret = False)
		security.create_external_radius_server_in_auth_server_one()
		security.configure_auth_server_settings(accounting_enable = True,mac_authentication = True)
		logger.debug("SecurityPage : Set delimiter to  : /")
		security.personal_delimeter.set(conf.external_captive_url)
		security.configure_blacklisting('Enable','10')
		security.configure_reauth_interval(conf.wep_key_index,conf.reauth_intrvl_unit_hrs)
		logger.debug('Security :Set Accouting Interval :30 mins')
		security.accounting_interval.set(conf.thirty)
		logger.debug("SecurityPage : Writing valid numbers in reauth interval text-box...")
		security.reauth_interval.set(self.config.config_vars.fifteen)
		security.configure_encryption('Enabled','none',conf.security_key_management)
		security.set_pass_phrase_format('64 hexadecimal chars')
		security.set_passphrase_retype(conf.security_passphrase,conf.security_passphrase)
		access = security.click_on_next()
		access.finish_network_setup()
		self.LeftPanel.assert_delta_config_icon()
		self.take_s2_snapshot()
		self.NetworkPage.assert_new_network()
		self._delete_network_auth_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_7167_edit_external_splash_default_profile(self):
		conf = self.config.config_vars
		self._delete_network_auth_server()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_external)
		access = security.create_captive_portal_profile(text = False)
		access.finish_network_setup()
		self.LeftPanel.assert_delta_config_icon()
		self.take_s2_snapshot()
		self.NetworkPage.assert_new_network()
		self._delete_network_auth_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()


	def test_ath_7169_create_auth_text_portal_auth_text_captive_portal_profile(self):
		conf = self.config.config_vars
		self._delete_network_auth_server()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_external)
		security.create_captive_portal_profile(text = True,ret = False)
		security.set_authentication_server_1_value(conf.InternalServer)
		logger.debug("SecurityPage : Disable mac authentication.")
		security.set_mac_authentication_value('Disabled')
		security.configure_blacklisting('Enable','0')
		security.configure_reauth_interval(conf.two,conf.reauth_intrvl_unit_hrs)
		# logger.debug('SecurityPage :Set Accouting Interval :30 mins')
		# security.accounting_interval.set(conf.thirty)
		logger.debug("SecurityPage : Writing valid numbers in reauth interval text-box...")
		security.reauth_interval.set(self.config.config_vars.fifteen)
		security.configure_encryption('Enabled',conf.key_mngmt_static,'none')
		security.set_wep_key_size('64-bit')
		security.set_wep_passphrase(conf.ten_hexa_decimal_chars,conf.ten_hexa_decimal_chars)
		access = security.click_on_next()
		access.finish_network_setup()
		self.LeftPanel.assert_delta_config_icon()
		self.take_s2_snapshot()
		self.NetworkPage.assert_new_network()
		self._delete_network_auth_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_6839_group_with_iap_version_3_4_and_below(self):
		conf = self.config.config_vars
		self._delete_network_auth_server()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.select_virtual_controller()
		logger.debug('Security: Checking for External option in security splash page type')
		if not security.splash_page_type_external :
			raise AssertionError('External option is not present')
		logger.debug('Security: Checking for external radius server disabled option in security splash page type')
		if not security.external_radius_server_disabled :
			raise AssertionError('external_radius_server_disabled option is not present')
		logger.debug('Security: Checking for external auth text disabled option in security splash page type')
		if not security.external_auth_text :
			raise AssertionError('external_auth_text option is not present')
			
			
	def test_ath_7170_external_create_auth_text_portal_profile_user_two_radius_auth_with_wpa_encryption(self):
		conf = self.config.config_vars
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_authentication_server()
		security_page.delete_authentication_server2()
		if security_page.is_external_captive_profile_present():
			security_page.delete_external_captive_role()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.use_vlan_defaults()
		security.set_splash_page_type('External')
		security.create_external_captive_portal_1()
		security.configure_auth_server_settings(mac_authentication=True,uppercase_support=True)
		security.configure_reauth_interval(conf.reauth_2,conf.reauth_intrvl_unit_hrs)
		security.set_delimiter()
		security.create_external_radius_server_in_auth_server_one()
		security.create_external_radius_server_in_auth_server_two()
		security.set_load_balancing_field(conf.enable_option)
		security.enable_accounting_interval('')
		security.configure_blacklisting('disable','')
		security.set_encryption(conf.enable_option)
		security.set_security_key_management(conf.Authentication_wpa2)
		security.set_pass_phrase_format(conf.pass_phrase_format_64_hexa_chars)
		security.set_passphrase_retype(conf.passphrase_hex_num_valid,conf.passphrase_hex_num_valid)
		access = security.move_to_next_page()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_authentication_server()
		security_page.delete_authentication_server2()
		if security_page.is_external_captive_profile_present():
			security_page.delete_external_captive_role()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_6841_iap4_splash_page_type_external_default(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_external)
		security.click_on_next_button()
		security.assert_default_captive_portal_profile_error()
		security.set_captive_portal_profile('default')
		security.click_on_edit_captive_portal()
		security.assert_default_captive_portal_type()
		security.assert_default_captive_portal_auth_text()
		security.click_captive_profile_cancel_button()
		security.assert_default_users()
		security.assert_internal_authenticated_fields()
		security.add_internal_sever_user()
		access = security.use_security_default()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_11014_verify_walled_garden_ui_screen_alignment(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.LeftPanel.go_to_network_page()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.configure_employee_security()
		access.finish_network_setup()
		security_page = self.LeftPanel.go_to_security()
		security_page.click_walled_garden_accordion()
		security_page.click_walled_garden_link()
		security_page.assert_walled_garden_ui()
		security_page.click_walled_garden_link()
		security_page.create_blacklist_new_domain()
		security_page.edit_blacklist_domain()
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		self._delete_network_auth_server()
		security_page = self.LeftPanel.go_to_security()
		security_page.click_walled_garden_accordion()
		security_page.click_walled_garden_link()
		security_page.delete_edited_blacklist_domain()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11034_check_for_security_eridien_display_2(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.configure_employee_security()
		access.finish_network_setup()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.set_general_dynamic_proxy('enabled')
		system_page._save_settings()
		security_page = self.LeftPanel.go_to_security()
		security_page.assert_security_page()
		self.take_s2_snapshot()
		network_page = self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11015_validating_walled_garden_with_single_quotes(self):
		'''
			The AssertionError should not thrown for the URL in Single Quote.
			If it throw the AssertionError then, Assertion message will Raise
		'''
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.LeftPanel.go_to_network_page()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.configure_employee_security()
		access.finish_network_setup()
		security_page = self.LeftPanel.go_to_security()
		security_page.click_walled_garden_accordion()
		security_page.click_walled_garden_link()
		security_page.create_blacklist_new_domain_with_single_qoutes()
		# security_page.edit_blacklist_domain()
		self.take_s2_snapshot()
		
		self.LeftPanel.go_to_network_page()
		self._delete_network_auth_server()
		security_page = self.LeftPanel.go_to_security()
		security_page.click_walled_garden_accordion()
		security_page.click_walled_garden_link()
		security_page.delete_edited_blacklist_domain()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()