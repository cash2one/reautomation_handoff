from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class AccessRule(ConfigurationTest):
	'''
	Test class for Access Rule
	'''
	
	def test_ath_10992_tcp_port_range_validation(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.configure_employee_security()
		access.tcp_port_range_validation()
		
	def test_ath_10993_mac_address_and_dhcp_options_attribute_to_be_disabled_in_wired_networks(self):
		'''
		bug
		'''
		self.NetworkPage.delete_wired_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.wired_employee_network_info()
		security = vlan_obj.wired_network_vlan_defaults()
		access = security.wired_security_defaults()
		access.click_role_access()
		access.check_mac_address_and_dhcp_option_in_wired_network()
		
	def test_ath_10986_role_with_mac_address_and_dhcp_options_matches_regular_expression(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.NetworkPage.delete_custom_guest_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		access = security.use_security_default()
		access.click_role_access()
		access.create_access_role_assignment_rule(str=conf.max_client_threshold, attribute=conf.dropdown_mac_address_and_dhcp_options)
		access.finish_network_setup()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info_with_specific_name(conf.guest_network_name, True)
		security = vlan_obj.use_vlan_defaults()
		security._set_phrase()
		access = security.move_to_next_page()
		access.click_role_access()
		access.create_access_role_assignment_rule(str=conf.max_client_threshold, attribute=conf.dropdown_mac_address_and_dhcp_options)
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.NetworkPage.delete_custom_guest_network_if_present()
		self._delete_network_auth_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	