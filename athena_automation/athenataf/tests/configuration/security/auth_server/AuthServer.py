import logging
logger = logging.getLogger('athenataf')


from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class AuthServer(ConfigurationTest):
	'''
		Test class for network configuration Security.
	'''

	def test_ath_6700_create_coa_server(self):
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_coa_server() 
		security_page.create_coa_server()
		self.take_s2_snapshot()
		security_page.delete_coa_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1645_create_LDAP_server(self):
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_ldap_server() 
		security_page.create_ldap_server()
		self.take_s2_snapshot()
		security_page.delete_ldap_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_12061_edit_the_created_radius_server_drp_values(self):
		conf = self.config.config_vars
		system_page = self.LeftPanel.go_to_system_page()
		system_page.set_general_dynamic_proxy('enabled')
		system_page._save_settings()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_authentication_server()
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security()
		security_page.create_new_server()
		security_page.create_authentication_server(name=conf.auth_radius_name, ip=conf.auth_radius_ip, sharedkey=conf.auth_radius_shared_key, retypekey=conf.auth_radius_shared_key,  mask=conf.network_mask ,dip=conf.drp_ip, gateway=conf.drp_gateway, vlan=conf.vlan)
		security_page.save_auth_server()
		security_page.click_edit_auth_server()
		security_page.create_authentication_server(dip=conf.drp_ip1, mask=conf.valid_netmask, gateway=conf.drp_gateway1, vlan=conf.vlan_id_4093)
		security_page.save_auth_server()
		self.take_s2_snapshot()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_authentication_server()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.set_general_dynamic_proxy('disabled')
		system_page._save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_12062_delete_delete_radius_which_is_mapped_to_network(self):
		conf = self.config.config_vars
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_authentication_server()
		self.take_s1_snapshot()
		self.LeftPanel.go_to_network_page()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.create_external_radius_server_in_auth_server_one()
		access = security.click_on_next()
		access.finish_network_setup()
		security_page = self.LeftPanel.go_to_security()
		security_page.assert_auth_server()
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_authentication_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11963_create_radius_server(self):
		conf = self.config.config_vars
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_authentication_server()
		security_page.delete_authentication_server()
		self.take_s1_snapshot()
		security_page.create_new_server()
		security_page.create_authentication_server(name=conf.auth_rad1, ip=conf.auth_rad1_ip, sharedkey=conf.alpha_numeric, retypekey=conf.alpha_numeric)
		security_page.save_auth_server()
		security_page.create_new_server()
		security_page.create_authentication_server(name=conf.auth_radius_name1, ip=conf.auth_radius_ip1, sharedkey=conf.auth_radius_shared_key1, retypekey=conf.auth_radius_shared_key1, rfc=True)
		security_page.NAS_ip.set(conf.nas_ip)
		security_page.nas_identifier.set(conf.abc)
		security_page.save_auth_server()
		self.take_s2_snapshot()
		security_page.delete_authentication_server()
		security_page.delete_authentication_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_12064_create_ldap_and_tacacs_server(self):
		config1 = self.config.config_vars
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_authentication_server()
		security_page.delete_authentication_server()
		self.take_s1_snapshot()
		security_page.create_ldap_server()
		security_page.create_new_server()
		security_page.tacacs_radio.click()
		security_page.set_new_server_tacacs_name(config1.User_Name_1)
		security_page.set_new_server_tacacs_shared_key(config1.auth_sharedkey_value)
		security_page.set_new_server_tacacs_retype_shared_key(config1.auth_sharedkey_value)
		security_page.set_new_server_tacacs_ip(config1.cppm_server_ip)
		security_page.save_auth_server()
		self.take_s2_snapshot()
		security_page.delete_authentication_server()
		security_page.delete_authentication_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8852_verify_captive_portal_logo_upload_feature_enabled_on_iap_41(self):
		self.LeftPanel.go_to_network_page()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.assert_splas_page_visuals_fields()
		
	def test_ath_12063_create_coa_only_server(self):
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_coa_server() 
		security_page.create_coa_server()
		self.take_s2_snapshot()
		security_page.delete_coa_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8853_verify_captive_portal_logo_feature_on_iap_with_below_41_versions(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.configure_splash_page_type(self.config.config_vars.Splash_page_Authenticated)
		security.assert_upload_logo_button()
		
	def test_ath_8856_verify_captive_portal_logo_image_size(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.configure_splash_page_type(self.config.config_vars.Splash_page_Authenticated)
		fu = self.get_file_uploader(self.config.config_vars.logo_5_kb)
		fu.start()
		security.logo_upload.click()
		fu.join()
		logger.debug("SecurityPage: Asserting logo preview ")
		if not security.logo_preview:
			raise AssertionError("Captive Portal Logo is not displayed")
		fu = self.get_file_uploader(self.config.config_vars.logo_16_kb)
		fu.start()
		security.change_logo.click()
		fu.join()
		logger.debug("SecurityPage: Asserting logo preview ")
		if not security.logo_preview:
			raise AssertionError("Captive Portal Logo is not displayed")
		fu = self.get_file_uploader(self.config.config_vars.logo_20_kb)
		fu.start()
		security.change_logo.click()
		fu.join()
		logger.debug("SecurityPage: Asserting logo size error message ")
		if not security.logo_size_error:
			raise AssertionError("Captive Portal Logo is not displayed")		
		
	def test_ath_8874_verify_user_with_admin_permission_can_upload_captive_portal_logo_on_iap_41(self):
		'''
		user with admin permission is not implemented
		'''
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.configure_splash_page_type(self.config.config_vars.Splash_page_Authenticated)
		security.assert_splas_page_visuals_fields()
		
		fu = self.get_file_uploader(self.config.config_vars.logo_5_kb)
		fu.start()
		security.logo_upload.click()
		fu.join()
		if not security.logo_preview:
			raise AssertionError("Captive Portal Logo is not displayed")
		security.check_captive_portal_logo_text_availablility()
		if not security.change_logo:
			raise AssertionError("Captive Portal Logo 'Change' button is not Visible")
		if not security.delete_logo:
			raise AssertionError("Captive Portal Logo 'Delete' button is not Enable")