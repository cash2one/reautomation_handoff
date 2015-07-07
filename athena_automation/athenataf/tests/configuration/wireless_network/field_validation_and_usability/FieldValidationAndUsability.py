import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class FieldValidationAndUsability(ConfigurationTest):
	'''
	Test class for Field Validation And Usability testcases.
	'''

	def test_ath_7041_creating_editing_the_authentication_server_in_network_security(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.configure_auth_server_settings(mac_authentication = True)
		security.validate_authentication_server_feilds()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_7047_required_fields_to_create_authentication_server(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.configure_auth_server_settings(mac_authentication = True)
		security.validate_authentication_server_required_feilds()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_7048_can_not_navigate_to_access_page_with_select_option_in_authentication_server(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.configure_auth_server_settings(mac_authentication = True)
		security.authentication_feild_with_select()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_7049_mac_authentication_and_checking_for_authentication_servers_visibility(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.configure_auth_server_settings(mac_authentication = True)
		security.checking_for_authentication_servers_visibility()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_7050_mac_authentication_and_checking_for_authentication_servers_visibility(self):
		self._delete_external_radius_servers()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.configure_auth_server_settings(mac_authentication = True)
		security.create_external_radiuds_server('1')
		security.checking_for_authentication_server2_visibility()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_7055_role_assignment_rule_string_field_is_a_required_field(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		security = vlan_obj.use_vlan_defaults()
		access = security.set_key_management_wpa_personal()
		access.click_role_access()
		access.assert_string_field_compulsion()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_7056_role_assignment_rule_string_field_should_have_validation_check_for_the_character_length(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		security = vlan_obj.use_vlan_defaults()
		access = security.set_key_management_wpa_personal()
		access.click_role_access()
		access.assert_string_field_check_for_the_character_length()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def _delete_external_radius_servers(self):
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security() 
		security_page.delete_authentication_server()
		security_page.delete_authentication_server2()
		self.LeftPanel.go_to_network_page()
		
	def test_ath_7051_reauth_interval_should_accept_a_valid_range(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.validate_reauth_interval('personal','min.')
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
		
	def test_ath_7116_by_default_employee_option_selected_for_primary_usage(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		basic_info.assert_employee_radio_button()

		
	def test_ath_7117_by_default_disabled_option_selected_for_broadcasefiltering_field(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		basic_info.employee_network_info_with_advanced_settings()
		basic_info.assert_broadcasefiltering('Disabled')

		
	def test_ath_7118_by_default_1_beacon_option_selected_for_dtim_interval_field(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		basic_info.employee_network_info_with_advanced_settings()
		basic_info.assert_dtiminterval('1 beacon')

	def test_ath_7119_by_default_disabled_option_selected_for_multicasttransmission_optimization_field(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		basic_info.employee_network_info_with_advanced_settings()
		basic_info.assert_multicastratetransmissionl('Disabled')

		
	def test_ath_7120_by_default_disabled_option_selected_for_dynamicmulticast_optimization_field(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		basic_info.employee_network_info_with_advanced_settings()
		basic_info.assert_dynamicmulticast('Disabled')


	def test_ath_7036_validate_port_number(self):
		self.NetworkPage.delete_network_if_present()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.guest_network_info()
		security       = virtual_lan.use_vlan_defaults()
		security.validate_splash_page()


	def test_ath_7037_validate_backlist_field(self):
		self.NetworkPage.delete_network_if_present()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.guest_network_info()
		security_page  = virtual_lan.use_vlan_defaults()
		security_page.validate_backlist_field()

	def test_ath_7038_validate_whitelist_field(self):
		self.NetworkPage.delete_network_if_present()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.guest_network_info()
		security_page  = virtual_lan.use_vlan_defaults()
		security_page.validate_whitelist_field()

	def test_ath_7121_valid_transmit_rates_2_Ghz(self):
		self.NetworkPage.delete_network_if_present()
		basic_info     = self.NetworkPage.create_new_network()
		basic_info.assert_transmit_rates_2_Ghz_defaults()


	def test_ath_7122_valid_transmit_rates_5_Ghz(self):
		self.NetworkPage.delete_network_if_present()
		basic_info     = self.NetworkPage.create_new_network()
		basic_info.assert_transmit_rates_5_Ghz_defaults()

	def test_ath_7123_validate_content_filtering(self):
		self.NetworkPage.delete_network_if_present()
		basic_info     = self.NetworkPage.create_new_network()
		basic_info.assert_content_filtering_defaults()

	def test_ath_7124_validate_band_field(self):
		self.NetworkPage.delete_network_if_present()
		basic_info     = self.NetworkPage.create_new_network()
		basic_info.assert_band_field_defaults()

	def test_ath_7125_validate_inactivity_timeout_field(self):
		self.NetworkPage.delete_network_if_present()
		basic_info     = self.NetworkPage.create_new_network()
		basic_info.assert_inactivity_timeout_defaults()        

	def test_ath_8840_check_wireless_network(self,wpa_wpa2=False):
		self.NetworkPage.delete_network_if_present()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.employee_network_info()
		security       = virtual_lan.use_vlan_defaults()
		if not wpa_wpa2:
			access          = security.configure_employee_security()
		else:
			access          = security.configure_employee_security(both=True)
		access.finish_network_setup()        
		self.NetworkPage.assert_wireless_network_overview()
		self.NetworkPage.delete_network_if_present()


	def test_ath_9650_network_name_validation(self):
		network_page = self.LeftPanel.go_to_network_page()
		basic_info = network_page.create_new_network()
		basic_info.validate_network_name()

	def test_ath_7142_validate_default_radius_option(self):
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		basic_info = network_page.create_new_network()
		vlan_page = basic_info.employee_network_info()
		security_page=vlan_page.use_vlan_defaults()
		security_page.click_on_enterprise_radio_button()
		security_page.setting_termination_option(1)
		security_page.set_authentication_server1('New')
		security_page.assert_radius_radio_button()

	def test_ath_7143_validate_radius_default_auth_port(self):
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		basic_info = network_page.create_new_network()
		vlan_page = basic_info.employee_network_info()
		security_page=vlan_page.use_vlan_defaults()
		security_page.click_on_enterprise_radio_button()
		security_page.setting_termination_option(1)
		security_page.set_authentication_server1('New')
		security_page.assert_auth_port()

	def test_ath_7144_validate_radius_default_accounting_port_field(self):
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		basic_info = network_page.create_new_network()
		vlan_page = basic_info.employee_network_info()
		security_page=vlan_page.use_vlan_defaults()
		security_page.click_on_enterprise_radio_button()
		security_page.setting_termination_option(1)
		security_page.set_authentication_server1('New')
		security_page.assert_auth_account_port()

	def test_ath_7145_validate_radius_default_dead_time(self):
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		basic_info = network_page.create_new_network()
		vlan_page = basic_info.employee_network_info()
		security_page=vlan_page.use_vlan_defaults()
		security_page.click_on_enterprise_radio_button()
		security_page.setting_termination_option(1)
		security_page.set_authentication_server1('New')
		security_page.assert_dead_time()


	def test_ath_7147_validate_ldap_default_auth_port(self):
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		basic_info = network_page.create_new_network()
		vlan_page = basic_info.employee_network_info()
		security_page=vlan_page.use_vlan_defaults()
		security_page.click_on_enterprise_radio_button()
		security_page.setting_termination_option(1)
		security_page.set_authentication_server1('New')
		security_page.set_ldap_radio_button()
		security_page.assert_ldap_auth_port()


	def test_ath_7149_validate_default_access_rules_field(self):
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		basic_info = network_page.create_new_network()
		vlan_page = basic_info.employee_network_info()
		security_page=vlan_page.use_vlan_defaults()
		access_page=security_page.set_wireless_security_defaults()
		access_page.assert_access_rule_unrestricted() 


	def test_ath_7150_validate_access_new_rules_allow_any_to_all_destination(self):
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		basic_info = network_page.create_new_network()
		vlan_page = basic_info.employee_network_info()
		security_page = vlan_page.use_vlan_defaults()
		access_page = security_page.set_wireless_security_defaults()
		access_page.click_role_access()
		access_page.create_role()
		access_page.assert_allow_any_to_all_destination_msg()
		
	def test_ath_7131_vlan_assignment_rules_default_operator(self):
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		basic_info = network_page.create_new_network()
		vlan_page = basic_info.employee_network_info()
		vlan_page.assert_dynamic_operator_default_value()

	def test_ath_7132_by_default_personal_option_selected_for_security_level_field(self):
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		basic_info = network_page.create_new_network()
		vlan_page = basic_info.employee_network_info()
		security_page = vlan_page.use_vlan_defaults()
		security_page.assert_security_level_default()

	def test_ath_7133_default_security_personal_key_management(self):
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		basic_info = network_page.create_new_network()
		vlan_page = basic_info.employee_network_info()
		security_page = vlan_page.use_vlan_defaults()
		security_page.assert_personal_key_management_default_value()

	def test_ath_7134_default_security_personal_dot11r_roaming(self):
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		basic_info = network_page.create_new_network()
		vlan_page = basic_info.employee_network_info()
		security_page = vlan_page.use_vlan_defaults()
		security_page.assert_personal_security_dot11r_roaming_default()

	def test_ath_7135_default_security_personal_passphrase_format(self):
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		basic_info = network_page.create_new_network()
		vlan_page = basic_info.employee_network_info()
		security_page = vlan_page.use_vlan_defaults()
		security_page.assert_personal_passphrase_format_default()

	def test_ath_7136_default_security_personal_mac_authentication(self):
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		basic_info = network_page.create_new_network()
		vlan_page = basic_info.employee_network_info()
		security_page = vlan_page.use_vlan_defaults()
		security_page.assert_personal_mac_authentication_default()

	def test_ath_7137_default_security_personal_blacklisting(self):
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		basic_info = network_page.create_new_network()
		vlan_page = basic_info.employee_network_info()
		security_page = vlan_page.use_vlan_defaults()
		security_page.assert_personal_blacklisting_default()

	def test_ath_7139_default_security_enterprise_termination(self):
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		basic_info = network_page.create_new_network()
		vlan_page = basic_info.employee_network_info()
		security_page = vlan_page.use_vlan_defaults()
		security_page.assert_enterprise_termination_default()

	def test_ath_7140_default_security_enterprise_authentication_server1(self):
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		basic_info = network_page.create_new_network()
		vlan_page = basic_info.employee_network_info()
		security_page = vlan_page.use_vlan_defaults()
		security_page.assert_enterprise_authentication_server1_default()

	def test_ath_7141_default_security_enterprise_mac_authentication(self):
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		basic_info = network_page.create_new_network()
		vlan_page = basic_info.employee_network_info()
		security_page = vlan_page.use_vlan_defaults()
		security_page.assert_enterprise_perform_mac_authentication_uppercase()

	def test_ath_7146_default_5_displayed_for_timeout_field_while_creating_new_radius_server(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.click_on_enterprise_radio_button()
		security.setting_termination_option(1)
		security.set_authentication_server('new')
		security.assert_timeout()

	def test_ath_7035_external_splash_page_visuals_should_be_validated_for_required_fields(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.assert_splash_page_required_fields()


	def test_ath_7034_redirect_url_field_in_internal_splash_page_visuals_and_external_splash_page_visuals_is_an_optional(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security=vlan_obj.use_vlan_defaults()
		security.assert_splash_page_visuals()

	def test_ath_7126_by_default_network_assigned_option_selected_for_client_ip_assignment_field(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		vlan_obj.assert_default_client_ip_assignment()

	def test_ath_7127_by_default_default_option_itself_is_selcted_for_client_vlan_assignment_field(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		vlan_obj.assert_default_client_vlan_assignmenet()

	def test_ath_7128_by_default_1_displayed_for_vlan_id_field(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		vlan_obj.assert_default_value_vlan_static()


	def test_ath_7129_by_default_default_vlan_1_displayed_for_vlan_assignment_rules_table_in_first_row(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		vlan_obj.assert_default_value_vlan_dyanamic()

	def test_ath_7130_by_default_AG_Group_option_selected_for_attribute_field(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		vlan_obj.assert_new_vlan_assignment_rule_attribute()

