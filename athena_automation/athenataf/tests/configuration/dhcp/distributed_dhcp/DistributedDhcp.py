import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DistributedDhcp(ConfigurationTest):
	'''
		Test class for DistributedDhcp 
	'''
	def test_ath_11243_edit_distributed_scope_values(self):
		conf=self.config.config_vars
		dhcp_page = self.LeftPanel.go_to_dhcp_page()
		dhcp_page.delete_dhcp_if_present()
		self.take_s1_snapshot()
		if not dhcp_page.is_dhcp_present():
			dhcp_page.create_new_dhcp()
		dhcp_page.edit_network()
		self.take_s2_snapshot()
		dhcp_page.delete_dhcp_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11242_create_distributed_scope_values(self):
		conf=self.config.config_vars
		dhcp_page = self.LeftPanel.go_to_dhcp_page()
		dhcp_page.delete_distributed_dhcp_scope_if_present()
		self.take_s1_snapshot()
		dhcp_page.click_on_distributed_dhcp_scopes_new()
		dhcp_page.set_distributed_dhcp_usrname(conf.distributed_dhcp_name)
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
		self.take_s2_snapshot()
		dhcp_page.delete_distributed_dhcp_scope_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11244_delete_dhcp_scope(self):
		conf=self.config.config_vars
		self.take_s1_snapshot()
		dhcp_page = self.LeftPanel.go_to_dhcp_page()
		dhcp_page.delete_distributed_dhcp_scope_if_present()
		dhcp_page.click_on_distributed_dhcp_scopes_new()
		dhcp_page.set_distributed_dhcp_usrname(conf.distributed_dhcp_name)
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
		dhcp_page.delete_distributed_dhcp_scope_if_present()
		if not dhcp_page.is_dhcp_present():
			dhcp_page.create_new_dhcp()
		self.take_s2_snapshot()
		dhcp_page.delete_dhcp_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_11245_create_distributed_l3_scope(self):
		conf=self.config.config_vars
		dhcp_page = self.LeftPanel.go_to_dhcp_page()
		dhcp_page.delete_distributed_dhcp_scope_if_present()
		self.take_s1_snapshot()
		dhcp_page.click_on_distributed_dhcp_scopes_new()
		dhcp_page.assert_distributed_dhcp_scopes_network_label()
		dhcp_page.set_distributed_dhcp_usrname(conf.distributed_dhcp_name)
		dhcp_page.select_distributed_dhcp_network_type('l3')
		dhcp_page.assert_distributed_dhcp_netmask_and_default_router()
		dhcp_page.validate_distributed_dhcp_vlan_dns_domain_lease_fields()
		dhcp_page.validate_distributed_dhcp_ip_range_and_lease_time()
		dhcp_page.set_distributed_dhcp_option_type(conf.Dhcp_Domain_Name_invalid)
		dhcp_page.set_distributed_dhcp_option_value(conf.invalid_Distributed_Option_Value)
		dhcp_page.click_on_next_button()
		dhcp_page.assert_distributed_dhcp_option_type_error(True)
		dhcp_page.set_distributed_dhcp_option_type(conf.centralized_dhcp_name_special_char)
		dhcp_page.click_on_next_button()
		dhcp_page.assert_distributed_dhcp_option_type_error(True)
		dhcp_page.set_distributed_dhcp_option_value(conf.Distributed_Option_Value)
		dhcp_page.click_on_next_button()
		dhcp_page.assert_distributed_dhcp_option_type_error(True)
		dhcp_page.set_distributed_dhcp_option_type(conf.Distributed_Option_Type)
		dhcp_page.click_on_next_button()
		dhcp_page.validating_branch_size_and_static_ip()
		dhcp_page.click_on_distributed_dhcp_finish_button()
		self.take_s2_snapshot()
		dhcp_page.delete_dhcp_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11246_create_distributed_l3_scope(self):
		conf=self.config.config_vars
		dhcp_page = self.LeftPanel.go_to_dhcp_page()
		dhcp_page.delete_distributed_dhcp_scope_if_present()
		self.take_s1_snapshot()
		dhcp_page.create_distributed_dhcp_with_type_l2_and_l3('l2')
		dhcp_page.click_on_distributed_edit_dhcp_button()
		dhcp_page.select_distributed_dhcp_network_type('l3')
		dhcp_page.click_on_next_button()
		dhcp_page.click_on_next_button()
		dhcp_page.click_on_distributed_dhcp_finish_button()
		dhcp_page.create_distributed_dhcp_with_type_l2_and_l3('l3')
		dhcp_page.click_on_distributed_edit_dhcp_button()
		dhcp_page.select_distributed_dhcp_network_type('l2')
		dhcp_page.set_distributed_dhcp_netmask(conf.Dhcp_Netmask)
		dhcp_page.set_distributed_dhcp_default_router(conf.distributed_dhcp_default_router)
		dhcp_page.click_on_next_button()
		dhcp_page.click_on_next_button()
		dhcp_page.click_on_distributed_dhcp_finish_button()
		self.take_s2_snapshot()
		dhcp_page.delete_dhcp_if_present()
		dhcp_page.delete_dhcp_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11247_create_l2_scope_multi_version_iaps_in_group(self):
		conf=self.config.config_vars
		dhcp_page = self.LeftPanel.go_to_dhcp_page()
		dhcp_page.delete_distributed_dhcp_scope_if_present()
		self.take_s1_snapshot()
		dhcp_page.create_distributed_l2_scope()
		dhcp_page.create_distributed_l3_scope()
		self.take_s2_snapshot()
		dhcp_page.delete_distributed_dhcp_scope_if_present()
		dhcp_page.delete_distributed_dhcp_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11241_field_validation(self):
		conf=self.config.config_vars
		dhcp_page = self.LeftPanel.go_to_dhcp_page()
		dhcp_page.delete_distributed_dhcp_scope_if_present()
		self.take_s1_snapshot()
		
		dhcp_page.asserting_new_button()
		dhcp_page.assert_mandatory_fields()
		dhcp_page.dhcp_field_validation()
		dhcp_page.distributed_dhcp_field_validation()
		dhcp_page.edit_distributed_dhcp()
		
		self.take_s2_snapshot()
		dhcp_page.delete_distributed_dhcp_scope_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
		
		
		
		
		
		