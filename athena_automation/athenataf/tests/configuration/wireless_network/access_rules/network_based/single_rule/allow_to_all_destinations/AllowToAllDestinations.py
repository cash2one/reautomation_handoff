from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class AllowToAllDestinations(ConfigurationTest):
	'''
	Test class for Allow To All Destinations
	'''
	def test_ath_1564_allow_any_to_all_destinations(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.configure_employee_security()
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.set_rule_service_action_and_destination(conf.Service_Role1_any, conf.action_default_value, conf.destination_default_value)
		access._save_rule()
		access.finish_network_setup()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created(conf.Service_Role1_any, conf.destination_default_value)
		edit_network_page.assert_on_action(conf.action_default_value)
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1565_allow_adp_to_all_destinations(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.configure_employee_security()
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.set_rule_service_action_and_destination(conf.service_adp, conf.action_default_value, conf.destination_default_value)
		access._save_rule()
		access.finish_network_setup()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created(conf.service_adp, conf.destination_default_value)
		edit_network_page.assert_on_action(conf.action_default_value)
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
		
	def test_ath_1566_allow_bootp_to_all_destinations(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.configure_employee_security()
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.set_rule_service_action_and_destination(conf.service_bootp, conf.action_default_value, conf.destination_default_value)
		access._save_rule()
		access.finish_network_setup()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created(conf.service_bootp, conf.destination_default_value)
		edit_network_page.assert_on_action(conf.action_default_value)
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1567_allow_cfgm_tcp_to_all_destinations(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.configure_employee_security()
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.set_rule_service_action_and_destination(conf.service_cfgm, conf.action_default_value, conf.destination_default_value)
		access._save_rule()
		access.finish_network_setup()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created(conf.service_cfgm, conf.destination_default_value)
		edit_network_page.assert_on_action(conf.action_default_value)
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1568_allow_cups_to_all_destinations(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.configure_employee_security()
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.set_rule_service_action_and_destination(conf.Service_Role1_cups, conf.action_default_value, conf.destination_default_value)
		access._save_rule()
		access.finish_network_setup()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created(conf.Service_Role1_cups, conf.destination_default_value)
		edit_network_page.assert_on_action(conf.action_default_value)
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1569_allow_dhcp_to_all_destinations(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.configure_employee_security()
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.set_rule_service_action_and_destination(conf.service_dhcp_value, conf.action_default_value, conf.destination_default_value)
		access._save_rule()
		access.finish_network_setup()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created(conf.service_dhcp_value, conf.destination_default_value)
		edit_network_page.assert_on_action(conf.action_default_value)
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1570_allow_dns_to_all_destinations(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.configure_employee_security()
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.set_rule_service_action_and_destination(conf.service_role_dns, conf.action_default_value, conf.destination_default_value)
		access._save_rule()
		access.finish_network_setup()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created(conf.service_role_dns, conf.destination_default_value)
		edit_network_page.assert_on_action(conf.action_default_value)
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1571_allow_custom_to_all_destinations(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.configure_employee_security()
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.set_rule_service_action_and_destination(conf.Service_Role1_custom, conf.action_default_value, conf.destination_default_value)
		access.set_port(conf.Port_26)
		access._save_rule()
		access.finish_network_setup()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created(conf.Service_Role1_custom, conf.destination_default_value)
		edit_network_page.assert_on_action(conf.action_default_value)
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1572_allow_esp_to_all_destinations(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.configure_employee_security()
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.set_rule_service_action_and_destination(conf.Service_Role1_esp, conf.action_default_value, conf.destination_default_value)
		access._save_rule()
		access.finish_network_setup()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created(conf.Service_Role1_esp, conf.destination_default_value)
		edit_network_page.assert_on_action(conf.action_default_value)
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1573_allow_ftp_to_all_destinations(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.configure_employee_security()
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.set_rule_service_action_and_destination(conf.service_role_ftp, conf.action_default_value, conf.destination_default_value)
		access._save_rule()
		access.finish_network_setup()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created(conf.service_role_ftp, conf.destination_default_value)
		edit_network_page.assert_on_action(conf.action_default_value)
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1646_allow_mspsc_udp_to_all_destinations(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.configure_employee_security()
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.set_rule_service_action_and_destination(conf.service_mspsc_udp, conf.action_default_value, conf.destination_default_value)
		access._save_rule()
		access.finish_network_setup()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created(conf.service_mspsc_udp, conf.destination_default_value)
		edit_network_page.assert_on_action(conf.action_default_value)
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.LeftPanel.assert_delta_config_icon()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_7975_allow_custom_to_all_destinations(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.configure_employee_security()
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.set_rule_service_action_and_destination(conf.Service_Role1_custom, conf.action_default_value, conf.destination_default_value)
		access.check_custom_options_validity()	
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()