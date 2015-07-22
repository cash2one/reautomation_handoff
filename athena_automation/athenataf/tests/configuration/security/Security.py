import logging
logger = logging.getLogger('athenataf')
import time

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Security(ConfigurationTest):
	'''
		Test class for network configuration Security.
	'''

	def test_ath_3988_security_UI_check(self):
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security() 
		security_page.click_firewall()
		security_page.assert_management_subnet()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_3997_create_subnet(self):
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security()
		security_page.click_firewall()
		security_page.assert_management_subnet()
		security_page.create_new_subnet()
		security_page.assert_subnet()
		self.take_s2_snapshot()
		security_page.delete_subnet()
		security_page.save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_3998_delete_subnet(self):
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security() 
		security_page.click_firewall()
		security_page.create_new_subnet()
		security_page.assert_subnet()
		security_page.delete_subnet()
		security_page.create_new_subnet()
		self.take_s2_snapshot()
		security_page.assert_subnet()
		security_page.delete_all_subnet()
		security_page.save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1699_check_all_options(self):
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security() 
		security_page.click_firewall()
		security_page.assert_firewall_default_options()
		self.take_s2_snapshot()		
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1701_enable_all_options(self):
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security() 
		security_page.click_firewall()
		security_page.enable_all_protection_attacks_options()
		self.take_s2_snapshot()	
		security_page.restore_firewall_settings_defaults()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
		
	def test_ath_1700_disable_all_options(self):
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security() 
		security_page.click_firewall()
		security_page.disable_application_layer_gateway()
		self.take_s2_snapshot()	
		security_page.restore_firewall_settings_defaults()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1647_create_user_for_internal_server_employee(self):
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security()
		security_page.go_to_user_for_internal_server()
		if security_page.if_internal_server_guest_present():  
			security_page.delete_internal_server()
		security_page.create_user_for_internal_server_employee()
		self.take_s2_snapshot()
		security_page.delete_internal_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1648_create_user_for_internal_server_guest(self):
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security()
		security_page.go_to_user_for_internal_server()
		if security_page.if_internal_server_guest_present():
			security_page.delete_internal_server()
		security_page.create_user_for_internal_server_guest()
		self.take_s2_snapshot()
		security_page.delete_internal_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

		
	def test_ath_1649_delete_user_for_internal_server(self):
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security()
		security_page.go_to_user_for_internal_server()
		if not security_page.if_internal_server_guest_present():
			security_page.create_user_for_internal_server_guest()
			self.take_s2_snapshot()
		security_page.delete_internal_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_3376_assert_create_user_for_internal_server_guest(self):
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security()
		security_page.go_to_user_for_internal_server()
		if security_page.if_internal_server_guest_present():
			security_page.delete_internal_server()
		security_page.assert_user_for_internal_server()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_6701_edit_user_for_internal_server_guest(self):
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security()
		security_page.go_to_user_for_internal_server()
		if not security_page.if_internal_server_guest_present():
			security_page.create_user_for_internal_server_guest()
		security_page.edit_user_for_internal_server_employee()
		self.take_s2_snapshot()
		security_page.delete_internal_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_1643_create_authentication_server(self):
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security()
		time.sleep(10)
		if security_page.if_authentication_server_radius_present():
			security_page.delete_authentication_server_radius()
		security_page.assert_authentication_server_radius()
		security_page.clear_all_auth_server_fields()
		security_page.create_authentication_server_radius()
		self.take_s2_snapshot()
		security_page.delete_authentication_server_radius()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1644_delete_authentication_server(self):
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security()
		time.sleep(10)
		if not security_page.if_authentication_server_radius_present():
			security_page.create_authentication_server_radius()
		self.take_s2_snapshot()		
		security_page.delete_authentication_server_radius()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_11035_try_editing_radius_erver_onfiguration(self):
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
		access = security.click_on_next()
		access.finish_network_setup()
		security_page = self.LeftPanel.go_to_security()
		security_page.create_new_server()
		security_page.create_authentication_server(name=conf.auth_rad1, ip=conf.auth_rad1_ip, sharedkey=conf.alpha_numeric, retypekey=conf.alpha_numeric)
		security_page.save_auth_server()
		security_page.click_edit_auth_server()
		security_page.create_authentication_server(actport=conf.auth_acct_port,time=conf.timeout1,timeout=conf.time_10)
		security_page.save_auth_server()
		time.sleep(60)
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_authentication_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		# self.clear()
		
	def test_ath_11033_check_for_security_meridien_display(self):
		conf = self.config.config_vars
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		self.LeftPanel.go_to_network_page()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		security._set_phrase()
		access = security.click_on_next()
		access.finish_network_setup()
		edit_network = self.NetworkPage.edit_network()
		edit_network.click_on_security_accordion()
		edit_network.configure_blacklisting(blacklisting_enable=True)
		edit_network.save_configuration()
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		# self.clear()
		
		
	def test_ath_11016_verify_external_captive_portal_page(self):
		conf = self.config.config_vars
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.click_on_next()
		security.set_splash_page_type('External')
		security.set_captive_portal_profile('default')
		security.click_on_edit_captive_portal()
		security.set_captive_ip(conf.external_captive_ip)
		security.save_captive_profile_button()
		access = security.click_on_next()
		access.finish_network_setup()
		security_page = self.LeftPanel.go_to_security()
		security_page.click_on_external_captive_accordion()
		security_page.edit_created_captive_portal()
		security_page.assert_external_captive_portal_default()
		security_page.click_captive_cancel_button()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		
		
		
	def test_ath_11030_verify_security_firewall_configuration(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		security = vlan_obj.use_vlan_defaults()
		access = security.assert_roaming_defaults(True,False)
		access.finish_network_setup()
		security_page = self.LeftPanel.go_to_security()
		security_page.click_firewall()
		security_page.create_new_subnet()
		security_page.assert_subnet()
		security_page.save_settings()
		security_page.click_firewall()
		security_page.delete_subnet()
		security_page.save_settings()
		self.take_s2_snapshot()
		network_page = self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8857_verify_captive_portal_logo_delete_without_save_on_41_or_a_group(self):	
		conf = self.config.config_vars
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.click_on_next()
		security.set_splash_page_type_value(conf.Splash_page_Acknowledged)
		logger.debug('SecurityPage : Clicking on upload button')
		fu = self.get_file_uploader(conf.logo1)
		fu.start()
		security.logo_upload.click()
		fu.join()
		security.click_on_delete_logo()
		logger.debug('SecurityPage : Asserting logo preview image')
		self.browser.assert_element(security.logo_preview,'Logo preview image is not displayed',False)	
		security.assert_splas_page_visuals_fields()
		security.click_on_preview_splash_page()
		security.assert_splash_banner_logo()
		security.click_on_preview_splash_page_close()
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11008_blacklisting_mac_validation(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		security = self.LeftPanel.go_to_security()
		security.delete_authentication_server()
		security.go_to_blacklisting()
		security.delete_blacklisting_if_present()
		self.take_s1_snapshot()
		self.LeftPanel.go_to_network_page()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		security._set_phrase()
		access = security.use_security_default()
		access.finish_network_setup()
		security = self.LeftPanel.go_to_security()
		security.go_to_blacklisting()
		security.create_manual_blacklisting()
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		security = self.LeftPanel.go_to_security()
		security.delete_authentication_server()
		security.go_to_blacklisting()
		security.delete_blacklisting_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_11012_validating_authentication_server(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		security = self.LeftPanel.go_to_security()
		security.delete_authentication_server()
		self.take_s1_snapshot()
		self.LeftPanel.go_to_network_page()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		security.enable_mac_authentication()
		security.set_authentication_server_next()
		security.assert_authentication_server1_error()
		security.create_external_radius_server_in_auth_server_one()
		security.select_auth_server_internalserver('1')
		security.use_security_default()
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		security = self.LeftPanel.go_to_security()
		security.delete_authentication_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11013_validating_authentication_servers_1_and_2(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		security = self.LeftPanel.go_to_security()
		security.delete_authentication_server()
		self.take_s1_snapshot()
		self.LeftPanel.go_to_network_page()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		security.enable_mac_authentication()
		security.set_authentication_server1('New')
		security.set_auth_server_name(conf.auth_server_name_new)
		security.set_auth_server_ip_address(conf.valid_auth_server_ip)
		security.set_auth_shared_key_retype(conf.wep_key_64_num_valid,conf.wep_key_64_num_valid)
		security.set_drp_vlan_value(conf.thirty)
		security.click_save_server()
		security.assert_authentication_server_1_and_2_dropdown_values('1',conf.auth_server_name_new)
		security.create_external_radius_server_in_auth_server_one()
		security.set_authentication_server_2_value(conf.new_server)
		security.set_auth_server_name(conf.auth_server_name_new)
		security.set_auth_server_ip_address(conf.valid_auth_server_ip)
		security.set_auth_shared_key_retype(conf.wep_key_64_num_valid,conf.wep_key_64_num_valid)
		security.set_drp_vlan_value(conf.thirty)
		security.click_save_server()
		security.assert_authentication_server_1_and_2_dropdown_values('2',conf.auth_server_name_new)
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		security = self.LeftPanel.go_to_security()
		security.delete_authentication_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_11031_verify_captive_portal_names_with_quotes(self):
		self.NetworkPage.delete_network_if_present()
		security = self.LeftPanel.go_to_security()
		security.delete_authentication_server()
		self.take_s1_snapshot()
		self.LeftPanel.go_to_network_page()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		security = vlan_obj.use_vlan_defaults()
		security._set_phrase()
		access = security.click_on_next()
		access.finish_network_setup()
		security_page = self.LeftPanel.go_to_security()
		security_page.external_captive_profile.click()
		security_page.create_new_captive_portal_1(name = "'testradius'",http1=False)
		security_page.asserting_captive_portal_name()
		security_page.click_captive_cancel_button()
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11044_authentication_text_field_validation(self):
		conf = self.config.config_vars
		security_page = self.LeftPanel.go_to_security()
		security_page.page_down()
		security_page.click_on_external_captive_accordion()
		logger.debug('SecurityPage: Clicking new ')
		security_page.create_external_captive.click()
		logger.debug('SecurityPage: Selecting the captive portal Type')
		security_page.captive_portal_type.set(conf.Captive_Role_Text)
		logger.debug('SecurityPage: Setting the captive portal IP or HostName')
		security_page.captive_portal_ip.set(conf.dynm_blklst_default_time)
		logger.debug('SecurityPage: Setting the captive portal URL')
		security_page.captive_portal_url.set('')
		logger.debug('SecurityPage: Setting the captive portal Port')
		security_page.captive_portal_port.set(conf.captive_portal_port)
		security_page.captive_portal_save_button.click()
		security_page.assert_captive_ip_error('True')
		security_page.assert_captive_url_req_error('True')
		security_page.assert_captive_port_error('True')
		security_page.assert_captive_auth_text_req_error('True')
		
		
	def test_ath_10996_check_for_possible_sql_injection(self):
		conf = self.config.config_vars
		security_page = self.LeftPanel.go_to_security() 
		security_page.check_global_search(conf.search1)
		security_page.check_global_search(conf.search2)
		security_page.check_global_search(conf.search3)
		security_page.check_global_search(conf.search4)