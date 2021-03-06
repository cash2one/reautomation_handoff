import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class LocalDhcp(ConfigurationTest):
	'''
	Test class for DHCP --> Centralized dhcp scopes.
	'''
	def test_ath_11256_local_l3_scope(self):
		# test case contains BUG #27637,#27644
		path = self.config.config_vars
		dhcp_page = self.LeftPanel.go_to_dhcp_page()
		self.take_s1_snapshot()
		dhcp_page.go_to_local_dhcp_scopes_accordion()
		dhcp_page.create_new_local_dhcp()
		dhcp_page.set_local_dhcp_name(path.centralized_dhcp_name)
		dhcp_page.set_local_dhcp_type(path.local_dhcp_type_local_l3)

		dhcp_page.set_local_dhcp_vlan(path.vlan_id_3333)
		dhcp_page.set_local_dhcp_network(path.local_dhcp_network)
		dhcp_page.set_local_dhcp_netmask(path.local_dhcp_netmask)
		dhcp_page.set_local_dhcp_excluded_address(path.local_dhcp_excluded_addr_invalid)
		dhcp_page.set_local_dhcp_dns_server(path.local_dhcp_dns_server_invalid_3)
		dhcp_page.set_local_dhcp_domain_name(path.Dhcp_Domain_Name_invalid)
		dhcp_page.set_local_dhcp_lease_time(path.dhcp_lease_time_spl_char)
		dhcp_page.set_local_dhcp_option_type_and_value(path.local_dhcp_option_type, path.local_dhcp_option_value)
		dhcp_page.save_local_dhcp_settings()
		dhcp_page.assert_local_dhcp_vlan_error_message('invalid')
		dhcp_page.assert_local_dhcp_excluded_error_message()
		dhcp_page.assert_local_dhcp_dns_server_error_message()
		dhcp_page.assert_local_dhcp_domain_error_message()
		dhcp_page.assert_local_dhcp_lease_time_error_message()
		
		dhcp_page.set_local_dhcp_vlan(path.vlan_id_invalid)
		dhcp_page.save_local_dhcp_settings()
		dhcp_page.assert_local_dhcp_vlan_error_message('invalid')
		
		#not accepting comma separated multiple domain names
		dhcp_page.set_local_dhcp_domain_name(path.dhcp_domain_names)
		dhcp_page.save_local_dhcp_settings()
		dhcp_page.assert_local_dhcp_domain_error_message()
		
		dhcp_page.set_local_dhcp_name(path.centralized_dhcp_name)
		dhcp_page.set_local_dhcp_type(path.local_dhcp_type_local_l3)
		dhcp_page.set_local_dhcp_vlan(path.vlan_id)
		dhcp_page.set_local_dhcp_network(path.local_dhcp_network)
		dhcp_page.set_local_dhcp_netmask(path.local_dhcp_netmask)
		dhcp_page.set_local_dhcp_excluded_address(path.local_dhcp_excluded_addr_valid)
		dhcp_page.set_local_dhcp_dns_server(path.local_dhcp_excluded_addr_valid)
		#not taking two domain server ip's separated by camma(,)
		dhcp_page.set_local_dhcp_domain_name(path.edit_Dhcp_Domain_Name)
		dhcp_page.set_local_dhcp_lease_time(path.local_dhcp_lease_time)
		dhcp_page.set_local_dhcp_option_type_and_value(path.local_dhcp_option_type,path.local_dhcp_option_value)
		dhcp_page.save_local_dhcp_settings()
		#dhcp_page.assert_local_dhcp_dns_server_error_message()
		#dhcp_page.set_local_dhcp_dns_server(path.local_dhcp_excluded_addr_valid)
		#dhcp_page.save_local_dhcp_settings()
		self.take_s2_snapshot()
		dhcp_page.delete_and_accept_alert()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
		
	def test_ath_11488_dhcp_scope_with_same_vlan_id(self):
		conf=self.config.config_vars
		dhcp_page = self.LeftPanel.go_to_dhcp_page()
		dhcp_page.delete_distributed_dhcp_scope_if_present()
		self.take_s1_snapshot()
		dhcp_page.click_on_distributed_dhcp_scopes_new()
		dhcp_page.set_distributed_dhcp_usrname(conf.distributed_dhcp_name_profile)
		dhcp_page.set_distributed_dhcp_vlan(conf.distributed_dhcp_vlan_120)
		dhcp_page.set_distributed_dhcp_netmask(conf.Dhcp_Netmask)
		dhcp_page.set_distributed_dhcp_default_router(conf.distributed_dhcp_default_router)
		dhcp_page.set_distributed_dhcp_dns_server(conf.distributed_dhcp_dns_server)
		dhcp_page.set_distributed_dhcp_domain_name(conf.distributed_dhcp_domain_name)
		dhcp_page.set_distributed_dhcp_ipaddress_range_start(conf.distributed_dhcp_ipaddress_range_start)
		dhcp_page.set_distributed_dhcp_ipaddress_range_end(conf.distributed_dhcp_ipaddress_range_end)
		dhcp_page.click_on_dhcp_distributed_add_new_ip_range()
		dhcp_page.set_distributed_dhcp_ipaddress_range_start_one(conf.distributed_dhcp_ipaddress_range_start1)
		dhcp_page.set_distributed_dhcp_ipaddress_range_end_one(conf.distributed_dhcp_ipaddress_range_end1)
		dhcp_page.set_distributed_dhcp_option_type(conf.Distributed_Option_Type)
		dhcp_page.set_distributed_dhcp_option_value(conf.Distributed_Option_Value)
		dhcp_page.click_on_next_button()
		dhcp_page.set_distributed_dhcp_client_per_branch(conf.Client_Per_Branch)
		dhcp_page.click_on_next_button()
		dhcp_page.set_distributed_dhcp_reserve_first(conf.Reserve_Last)
		dhcp_page.set_distributed_dhcp_reserve_last(conf.Reserve_First)
		dhcp_page.click_on_distributed_dhcp_finish_button()
		
		dhcp_page.click_on_distributed_dhcp_scopes_new()
		dhcp_page.set_distributed_dhcp_usrname(conf.distributed_dhcp_name_profile)
		dhcp_page.set_distributed_dhcp_vlan(conf.distributed_dhcp_vlan)
		dhcp_page.set_distributed_dhcp_netmask(conf.Dhcp_Netmask)
		dhcp_page.set_distributed_dhcp_default_router(conf.distributed_dhcp_default_router)
		dhcp_page.set_distributed_dhcp_dns_server(conf.distributed_dhcp_dns_server)
		dhcp_page.set_distributed_dhcp_domain_name(conf.distributed_dhcp_domain_name)
		dhcp_page.set_distributed_dhcp_ipaddress_range_start(conf.distributed_dhcp_ipaddress_range_start)
		dhcp_page.set_distributed_dhcp_ipaddress_range_end(conf.distributed_dhcp_ipaddress_range_end)
		dhcp_page.click_on_dhcp_distributed_add_new_ip_range()
		dhcp_page.set_distributed_dhcp_ipaddress_range_start_one(conf.distributed_dhcp_ipaddress_range_start1)
		dhcp_page.set_distributed_dhcp_ipaddress_range_end_one(conf.distributed_dhcp_ipaddress_range_end1)
		dhcp_page.set_distributed_dhcp_option_type(conf.Distributed_Option_Type)
		dhcp_page.set_distributed_dhcp_option_value(conf.Distributed_Option_Value)
		dhcp_page.click_on_next_button()
		dhcp_page.set_distributed_dhcp_client_per_branch(conf.Client_Per_Branch)
		dhcp_page.click_on_next_button()
		dhcp_page.set_distributed_dhcp_reserve_first(conf.Reserve_Last)
		dhcp_page.set_distributed_dhcp_reserve_last(conf.Reserve_First)
		dhcp_page.click_on_distributed_dhcp_finish_button()
		#bug 27631
		dhcp_page.click_on_distributed_dhcp_scopes_new()
		dhcp_page.set_distributed_dhcp_usrname(conf.distributed_dhcp_name_profile)
		dhcp_page.set_distributed_dhcp_vlan(conf.distributed_dhcp_vlan)
		dhcp_page.set_distributed_dhcp_netmask(conf.Dhcp_Netmask)
		dhcp_page.set_distributed_dhcp_default_router(conf.distributed_dhcp_default_router)
		dhcp_page.set_distributed_dhcp_dns_server(conf.distributed_dhcp_dns_server)
		dhcp_page.set_distributed_dhcp_domain_name(conf.distributed_dhcp_domain_name)
		dhcp_page.set_distributed_dhcp_ipaddress_range_start(conf.distributed_dhcp_ipaddress_range_start)
		dhcp_page.set_distributed_dhcp_ipaddress_range_end(conf.distributed_dhcp_ipaddress_range_end)
		dhcp_page.click_on_dhcp_distributed_add_new_ip_range()
		dhcp_page.set_distributed_dhcp_ipaddress_range_start_one(conf.distributed_dhcp_ipaddress_range_start1)
		dhcp_page.set_distributed_dhcp_ipaddress_range_end_one(conf.distributed_dhcp_ipaddress_range_end1)
		dhcp_page.set_distributed_dhcp_option_type(conf.Distributed_Option_Type)
		dhcp_page.set_distributed_dhcp_option_value(conf.Distributed_Option_Value)
		dhcp_page.click_on_next_button()
		dhcp_page.set_distributed_dhcp_client_per_branch(conf.Client_Per_Branch)
		dhcp_page.click_on_next_button()
		dhcp_page.set_distributed_dhcp_reserve_first(conf.Reserve_Last)
		dhcp_page.set_distributed_dhcp_reserve_last(conf.Reserve_First)
		dhcp_page.click_on_distributed_dhcp_finish_button()
		#bug 27643
		self.take_s2_snapshot()
		dhcp_page.delete_distributed_dhcp_scope_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
		
	def test_ath_11255_edit_local_dhcp_scope(self):
		dhcp_page = self.LeftPanel.go_to_dhcp_page()
		conf = self.config.config_vars
		self.take_s1_snapshot()
		dhcp_page.go_to_local_dhcp_scopes_accordion()
		dhcp_page.delete_and_accept_alert()
		dhcp_page.create_new_local_dhcp()
		dhcp_page.set_local_dhcp_name(conf.dhcp_name_new)
		dhcp_page.set_local_dhcp_type(conf.dhcp_type_local)
		dhcp_page.set_local_dhcp_vlan(conf.Dhcp_Vlan)
		dhcp_page.set_local_dhcp_network(conf.dhcp_network_address)
		dhcp_page.set_local_dhcp_netmask(conf.Dhcp_Netmask)
		dhcp_page.set_local_dhcp_excluded_address(conf.dhcp_excluded_address)
		dhcp_page.set_local_dhcp_dns_server(conf.Dhcp_Dns_Server)
		dhcp_page.set_local_dhcp_domain_name(conf.Dhcp_Domain_Name)
		dhcp_page.local_dhcp_lease_time.set(conf.lease_time_value)
		dhcp_page.local_dhcp_option_type.set(conf.dhcp_option_type)
		dhcp_page.local_dhcp_option_value.set(conf.dhcp_option_value)
		dhcp_page.save_local_dhcp_settings()
		#edit
		dhcp_page.assert_edit_button_and_click()
		dhcp_page.assert_default_local_dhcp_type()
		dhcp_page.set_local_dhcp_name(conf.edit_dhcp_name_new)
		dhcp_page.set_local_dhcp_vlan(conf.edit_Dhcp_Vlan)
		dhcp_page.set_local_dhcp_network(conf.edit_dhcp_network_address)
		dhcp_page.set_local_dhcp_netmask(conf.edit_Dhcp_Netmask)
		dhcp_page.set_local_dhcp_excluded_address(conf.edit_dhcp_excluded_address)
		dhcp_page.set_local_dhcp_dns_server(conf.Edit_Dhcp_Dns_Server)
		dhcp_page.set_local_dhcp_domain_name(conf.edit_Dhcp_Domain_Name)
		dhcp_page.local_dhcp_lease_time.set(conf.edit_lease_time_value)
		dhcp_page.local_dhcp_option_type.set(conf.edit_dhcp_option_type)
		dhcp_page.local_dhcp_option_value.set(conf.edit_dhcp_option_value)
		dhcp_page.save_local_dhcp_settings()
		self.take_s2_snapshot()
		dhcp_page.delete_and_accept_alert()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
		
	def test_ath_11258_edit_local_dhcp_scope_to_local_l3_scope(self):
		dhcp_page = self.LeftPanel.go_to_dhcp_page()
		conf = self.config.config_vars
		self.take_s1_snapshot()
		dhcp_page.go_to_local_dhcp_scopes_accordion()
		dhcp_page.delete_and_accept_alert()
		dhcp_page.create_new_local_dhcp()
		dhcp_page.set_local_dhcp_name(conf.dhcp_name_new)
		dhcp_page.set_local_dhcp_type(conf.dhcp_type_local)
		dhcp_page.set_local_dhcp_vlan(conf.Dhcp_Vlan)
		dhcp_page.set_local_dhcp_network(conf.dhcp_network_address)
		dhcp_page.set_local_dhcp_netmask(conf.Dhcp_Netmask)
		dhcp_page.set_local_dhcp_excluded_address(conf.dhcp_excluded_address)
		dhcp_page.set_local_dhcp_dns_server(conf.Dhcp_Dns_Server)
		dhcp_page.set_local_dhcp_domain_name(conf.Dhcp_Domain_Name)
		dhcp_page.local_dhcp_lease_time.set(conf.lease_time_value)
		dhcp_page.local_dhcp_option_type.set(conf.dhcp_option_type)
		dhcp_page.local_dhcp_option_value.set(conf.dhcp_option_value)
		dhcp_page.save_local_dhcp_settings()
		dhcp_page.assert_edit_button_and_click()
		dhcp_page.set_local_dhcp_type(conf.local_l3)
		dhcp_page.save_local_dhcp_settings()
		self.take_s2_snapshot()
		dhcp_page.delete_and_accept_alert()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11259_delete_local_dhcp_scope(self):
		dhcp_page = self.LeftPanel.go_to_dhcp_page()
		conf = self.config.config_vars
		dhcp_page.go_to_local_dhcp_scopes_accordion()
		dhcp_page.delete_and_accept_alert()
		self.take_s1_snapshot()
		dhcp_page.create_new_local_dhcp()
		dhcp_page.set_local_dhcp_name(conf.dhcp_name_new)
		dhcp_page.set_local_dhcp_type(conf.dhcp_type_local)
		dhcp_page.set_local_dhcp_vlan(conf.Dhcp_Vlan)
		dhcp_page.set_local_dhcp_network(conf.dhcp_network_address)
		dhcp_page.set_local_dhcp_netmask(conf.Dhcp_Netmask)
		dhcp_page.set_local_dhcp_excluded_address(conf.dhcp_excluded_address)
		dhcp_page.set_local_dhcp_dns_server(conf.Dhcp_Dns_Server)
		dhcp_page.set_local_dhcp_domain_name(conf.Dhcp_Domain_Name)
		dhcp_page.local_dhcp_lease_time.set(conf.lease_time_value)
		dhcp_page.local_dhcp_option_type.set(conf.dhcp_option_type)
		dhcp_page.local_dhcp_option_value.set(conf.dhcp_option_value)
		dhcp_page.save_local_dhcp_settings()
		dhcp_page.delete_and_accept_alert()
		self.take_s2_snapshot()
		dhcp_page.create_new_local_dhcp()
		dhcp_page.set_local_dhcp_name(conf.special_chars)
		dhcp_page.set_local_dhcp_type(conf.dhcp_type_local)
		dhcp_page.set_local_dhcp_vlan(conf.Dhcp_Vlan)
		dhcp_page.set_local_dhcp_network(conf.dhcp_network_address)
		dhcp_page.set_local_dhcp_netmask(conf.Dhcp_Netmask)
		dhcp_page.set_local_dhcp_excluded_address(conf.dhcp_excluded_address)
		dhcp_page.set_local_dhcp_dns_server(conf.Dhcp_Dns_Server)
		dhcp_page.set_local_dhcp_domain_name(conf.Dhcp_Domain_Name)
		dhcp_page.local_dhcp_lease_time.set(conf.lease_time_value)
		dhcp_page.local_dhcp_option_type.set(conf.dhcp_option_type)
		dhcp_page.local_dhcp_option_value.set(conf.dhcp_option_value)
		dhcp_page.save_local_dhcp_settings()
		dhcp_page.delete_and_accept_alert()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11254_create_local_dhcp_scope(self):
		dhcp_page = self.LeftPanel.go_to_dhcp_page()
		conf = self.config.config_vars
		dhcp_page.go_to_local_dhcp_scopes_accordion()
		dhcp_page.create_new_local_dhcp()
		dhcp_page.save_local_dhcp_settings()
		dhcp_page.local_dhcp_name_req_field_error.assert_element()
		dhcp_page.local_dhcp_vlan_range_error.assert_element()
		dhcp_page.local_dhcp_network_invalid_error.assert_element()
		dhcp_page.local_dhcp_netmask_req_error.assert_element()
		dhcp_page.set_local_dhcp_name(conf.special_chars)
		dhcp_page.save_local_dhcp_settings()
		dhcp_page.name_max_length_error.assert_element()

		dhcp_page.set_local_dhcp_name(conf.double_quotes)
		dhcp_page.save_local_dhcp_settings()
		dhcp_page.assert_local_dhcp_name_error_message('invalid')
		#bug make changes

		dhcp_page.set_local_dhcp_name(conf.alpha_numeric)
		dhcp_page.save_local_dhcp_settings()
		dhcp_page.local_dhcp_name_req_field_error.assert_element()
		dhcp_page.set_local_dhcp_name(conf.admin_invalid_u_name)
		dhcp_page.save_local_dhcp_settings()
		dhcp_page.name_max_length_error.assert_element()

		dhcp_page.set_local_dhcp_type()
		dhcp_page.set_local_dhcp_vlan(conf.Dhcp_Vlan_Error)
		dhcp_page.save_local_dhcp_settings()
		dhcp_page.name_max_length_error.assert_element()
		dhcp_page.set_local_dhcp_vlan(conf.dhcp_vlan_error_3333)
		dhcp_page.save_local_dhcp_settings()
		dhcp_page.local_dhcp_vlan_3333.assert_element()
		dhcp_page.set_local_dhcp_network(conf.Dhcp_Default_Router_Error)
		dhcp_page.set_local_dhcp_netmask(conf.invalid_netmask)
		dhcp_page.save_local_dhcp_settings()
		dhcp_page.assert_local_dhcp_network_error_message('invalid')
		dhcp_page.set_local_dhcp_network(conf.edit_dhcp_network_address)
		dhcp_page.set_local_dhcp_netmask(conf.edit_Dhcp_Netmask)
		dhcp_page.save_local_dhcp_settings()
		dhcp_page.assert_local_dhcp_network_error_message('valid')
		dhcp_page.set_local_dhcp_excluded_address(conf.distributed_dhcp_ipaddress_range_end2)
		dhcp_page.save_local_dhcp_settings()
		dhcp_page.assert_local_dhcp_excluded_error_message()
		dhcp_page.set_local_dhcp_excluded_address('')
		dhcp_page.set_local_dhcp_dns_server(conf.local_dhcp_dns_server_valid_2)
		dhcp_page.save_local_dhcp_settings()
		#due to bug test case is parked 
		
	def test_ath_11257_edit_local_l3_dhcp_scope(self):
		#TestCase contains Bug #27646
		path = self.config.config_vars
		dhcp_page = self.LeftPanel.go_to_dhcp_page()
		dhcp_page.go_to_local_dhcp_scopes_accordion()
		self.take_s1_snapshot()
		dhcp_page.create_local_dhcp_scope()
		#Scope is not highlighted when click on 'Local,L3'
		dhcp_page.edit_created_local_dhcp_scope()
		self.take_s2_snapshot()
		dhcp_page.delete_local_scope_and_accept_alert()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_11260_define_dhcp_scope_override_ap(self):
		conf = self.config.config_vars
		self.take_s1_snapshot()
		innerleftpanel = self.TopPanel.click_slider_icon()
		innerleftpanel.select_device()
		dhcp_page = self.LeftPanel.go_to_dhcp_page()
		dhcp_page.go_to_local_dhcp_scopes_accordion()
		dhcp_page.create_local_dhcp_scope()
		innerleftpanel = self.TopPanel.click_slider_icon()
		innerleftpanel.select_default_group()
		dhcp_page = self.LeftPanel.go_to_dhcp_page()
		dhcp_page.go_to_local_dhcp_scopes_accordion()
		logger.debug('DHCP : Asserting newly created local dhcp scope on group level')
		self.browser.assert_element(dhcp_page.dhcp_local_edit_icon,'newly created local dhcp scope is visible on group level',False)
		self.take_s2_snapshot()
		dhcp_page.delete_local_scope_and_accept_alert()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		