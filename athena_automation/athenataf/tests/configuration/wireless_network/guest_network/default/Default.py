import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Default(ConfigurationTest):
	'''
	Test class for Guest Network -> Default
	'''
	
	def test_ath_12103_default_value_vlan(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		virtual_lan.assert_vlan_page()
		
	def test_ath_12161_default_value_vlan_default(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		virtual_lan.select_network_assigned()
		virtual_lan.assert_default_value_vlan()

	def test_ath_12100_default_value_vlan_static(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_new_network_info()
		vlan_obj.asserting_vlan_network_assigned_static_value()
		
	def test_ath_12101_default_value_vlan_dynamic(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_new_network_info()
		vlan_obj.asserting_vlan_network_assigned_dynamic_value()
	
	def test_ath_12234_security_sp_external(self):
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.set_splash_page_type_value("External")
		security.assert_external_spalsh_page_type_default_values()

	def test_ath_12235_security_sp_none(self):
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.set_splash_page_type_value("None")
		security.assert_none_spalsh_page_type_default_values()
		
	def test_ath_12102_default_value_security(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.assert_default_wireless_guest_fields()

	def test_ath_12233_default_value_security_sp_internal_auth(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.splash_page_type.set(conf.Splash_page_Authenticated)
		security.assert_splash_page_internal_auth_fields()

	def test_ath_12236_default_value_security_sp_internal_auth(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.splash_page_type.set(conf.Splash_page_Acknowledged)
		security.set_mac_authentication_value('Enabled')
		security.assert_splash_page_internal_acknowledged_mac_enabled_field()
		
	def test_ath_12098_voice_default_value_advanced_settings(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		basic_info.wired_network_guest.click()
		basic_info.click_advanced_settings()
		basic_info.assert_dropdown_default_values(broadcasefiltering=True,dtiminterval=True,multicastratetransmission=True,dynamicmulticast=True,content_filtering=True,band=True)
		basic_info.assert_broadcasefiltering_dropdown_values()
		basic_info.assert_dtiminterval_dropdown_options()
		basic_info.assert_multicastratetransmission_dropdown_values()
		basic_info.assert_dynamicmulticast_dropdown_values()
		basic_info.assert_content_filtering_dropdown()
		basic_info.assert_band_dropdown()
		basic_info.assert_transmit_rates_dropdown_default_values(ghz24_min=True,ghz24_max=True,ghz5_min=True,ghz5_max=True)
		basic_info.assert_2_Ghz_dropdown_options('min')
		basic_info.assert_2_Ghz_dropdown_options('max')
		basic_info.assert_5_Ghz_dropdown_options('min')
		basic_info.assert_5_Ghz_dropdown_options('max')
		basic_info.assert_local_probe_request_threshold()
		basic_info.assert_max_client_threshold()
		basic_info.assert_can_be_used_without_uplink()
		basic_info.assert_disable_ssid()
		basic_info.assert_hide_ssid()
		basic_info.assert_inactivity_timeout()
		basic_info.assert_dmo_channel_utilization_threshold()
		basic_info.assert_wmm_share_value()
		basic_info.assert_bandwidth_limits_airtime_checkbox()
		# basic_info.assert_bandwidth_limits_each_radio_checkbox()
		basic_info.click_airtime_checkbox()
		basic_info.assert_airtime_textbox_empty()
		# basic_info.click_each_radio_checkbox()
		# basic_info.assert_each_radio_textbox_empty()
		
	def test_ath_12237_default_value_security_sp_internal_ack_mac_authserver1_external(self):
		self.take_s1_snapshot()
		conf = self.config.config_vars
		self._delete_network_auth_server()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.splash_page_type.set(conf.Splash_page_Acknowledged)
		security.enable_mac_authentication1()
		security.create_external_radius_server_in_auth_server_one()
		security.assert_auth_server2_and_accounting()
		access=security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self._delete_network_auth_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_12238_default_value_security_sp_internal_ack_mac_authserver1and_authserver2_external(self): 
		self.take_s1_snapshot()
		conf = self.config.config_vars
		self._delete_network_auth_server()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.splash_page_type.set(conf.Splash_page_Acknowledged)
		security.enable_mac_authentication1()
		security.create_external_radius_server_in_auth_server_one()	
		security.create_external_radius_server_in_auth_server_two()	
		security.assert_load_balancing()
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
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
		security_page = self.LeftPanel.go_to_security() 
		security_page.delete_2_external_servers()
		self.LeftPanel.go_to_network_page()
		
	def test_ath_12425_default_value_security_sp_internal_auth_mac_enabled(self):
		conf = self.config.config_vars
		self.take_s1_snapshot()
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.select_virtual_controller()
		security.set_splash_page_type_value(conf.Splash_page_Authenticated)
		security.set_mac_authentication_value('Enabled')
		security.assert_splash_page_internal_authenticated_mac_enabled_field()
		
	def test_ath_12426_default_value_security_sp_internal_auth_auth_server_1_external(self):
		conf = self.config.config_vars
		self.take_s1_snapshot()
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.select_virtual_controller()
		security.set_splash_page_type_value(conf.Splash_page_Authenticated)
		security.create_external_radius_server_in_auth_server_one()
		security.assert_authentication_server2('Select')
		security_page = self.LeftPanel.go_to_security() 
		security_page.delete_authentication_server()
	
	def test_ath_12241_default_value_security_sp_internal_auth_wispr_enabled(self):
		self._delete_network_auth_server()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.set_splash_page_type_value()
		security.set_wispr('Enabled')
		security.assert_security_sp_internal_auth_wispr_enabled_fields(captive=False)
		security.network_create_cancel.click()
		self._delete_network_auth_server()
		
	def test_ath_12239_default_value_security_sp_internal_ack_mac_as1_external_as2_internal(self):
		conf = self.config.config_vars
		self._delete_network_auth_server()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.set_splash_page_type_value("Internal - Acknowledged")
		security.enable_mac_authentication()
		security.create_external_radius_server_in_auth_server_one()
		security.set_authentication_server_2_value(self.config.config_vars.edit_Authentication_server)
		security.assert_accounting_and_user_link()
		security.network_create_cancel.click()
		self._delete_network_auth_server()
		
		
	def test_ath_12240_default_value_security_sp_internal_ack_mac_as1_external_as2_external_accounting_enabled(self):
		conf = self.config.config_vars
		self._delete_network_auth_server()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.set_splash_page_type_value("Internal - Acknowledged")
		security.enable_mac_authentication()
		security.create_external_radius_server_in_auth_server_one()
		security.create_external_radius_server_in_auth_server_two()
		security.configure_auth_server_settings(accounting_enable= True)
		security.assert_accounting_mode_and_interval()
		security.network_create_cancel.click()
		self._delete_network_auth_server()
		
	def test_ath_12242_default_value_security_sp_internal_auth_wispr_enabled_as1_as2_external(self):
		self.take_s1_snapshot()
		conf = self.config.config_vars
		self._delete_network_auth_server()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.splash_page_type.set(conf.Splash_page_Authenticated)
		security.set_wispr(conf.blacklisting_enabled)
		security.create_external_radius_server_in_auth_server_one()	
		security.create_external_radius_server_in_auth_server_two()
		security.assert_load_balancing()
		security.assert_internal_server_link(False)
		self.take_s2_snapshot()
		self._delete_network_auth_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		# self.clear('IAP_1')
		
	def test_ath_12428_default_value_security_sp_iternal_auth_as_1_external_as2_external(self):
		conf = self.config.config_vars
		self._delete_network_auth_server()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.set_splash_page_type_value("Internal - Acknowledged")
		security.enable_mac_authentication()
		security.create_external_radiuds_server('1')
		security.create_external_radiuds_server('2')
		logger.debug('Network :SecurityPage : asserting for accounting field')
		if security.show_users_link:
			raise AssertionError("Network : SecurityPage :zero show users link visible for user  . i.e . Traceback: %s" % traceback.format_exc())
		logger.debug('Network : SecurityPage : asserting show user link')	
		self.browser.assert_drop_down_value(security.accounting,conf.open_roaming_value,'accounting field is not set to disabled')
		logger.debug('Network :SecurityPage : asserting load balancing : disabled')	
		self.browser.assert_drop_down_value(security.load_balancing,conf.open_roaming_value,'load balancing field is not set to disabled')
		security.network_create_cancel.click()
		self._delete_network_auth_server()
		
	def test_ath_12427_default_value_security_sp_iternal_auth_as_1_external_as2_internal(self):
		conf = self.config.config_vars
		self._delete_network_auth_server()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.set_splash_page_type_value("Internal - Acknowledged")
		security.enable_mac_authentication()
		security.create_external_radiuds_server('1')
		security.set_authentication_server_2_value(self.config.config_vars.edit_Authentication_server)
		security.assert_default_value_security_sp_iternal_auth_as_1_external_as2_internal()
		security.network_create_cancel.click()
		self._delete_network_auth_server()
		
	def test_ath_12507_default_value_security_sp_external_wispr_enabled(self):
		self._delete_network_auth_server()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.set_splash_page_type_value("External")
		security.set_wispr('Enabled')
		security.assert_security_sp_internal_auth_wispr_enabled_fields(captive=True)
		security.network_create_cancel.click()
		self._delete_network_auth_server()
		
	def test_ath_8371_verify_splash_page_preview(self):
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.preview_splash_page.click()
		security.assert_splash_page_fields()
	
	def test_ath_6838_group_with_iap_version_4(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		if inner_left_panel.assert_group():
			if inner_left_panel.assert_sample_group_with_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.move_virtual_controller()
				inner_left_panel.manage_group()
				manage_group_page.delete_empty_group()
			elif inner_left_panel.assert_sample_group_without_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.delete_empty_group()
		self.take_s1_snapshot()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_group()
		inner_left_panel.select_sample_group()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.assert_splash_page_type_disabled_option()
		self.take_s2_snapshot()
		inner_left_panel = self.TopPanel.click_slider_icon()
		manage_group_page1 = inner_left_panel.manage_group()
		manage_group_page1.move_virtual_controller()
		inner_left_panel.manage_group()
		manage_group_page1.delete_empty_group()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

		
	def test_ath_601_wpa_personal(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.click_on_external_captive_protal_button()
		security_page.delete_captive_portal()
		security_page.delete_user_for_internal_server()
		self.LeftPanel.go_to_network_page()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.set_splash_page_type_value('External')
		security.create_captive_portal_profile_with_whitelisting_enabled()
		security.configure_encryption('Enabled',False,conf.Authentication_wpa2)
		security.enable_mac_authentication()
		security.select_auth_server_internalserver('1')
		security.add_internal_sever_user()
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.click_on_external_captive_protal_button()
		security_page.delete_captive_portal()
		security_page.delete_user_for_internal_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_8370_default_value_vlan(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_authentication_server()
		self.LeftPanel.go_to_network_page()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		virtual_lan.assert_default_vlan_value()
		security = virtual_lan.click_on_next()
		access = security.use_security_default()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_authentication_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	