import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Dhcp(ConfigurationTest):
	'''
		Test class for Dhcp module.
	'''

	def test_ath_4548_field_validation(self):
		self.take_s1_snapshot()
		dhcp_page = self.LeftPanel.go_to_dhcp_page()
		dhcp_page.delete_dhcp_if_present()
		dhcp_page.dhcp_field_validation()
		dhcp_page.assert_mandatory_fields()
		dhcp_page.assert_client_per_branch()
		dhcp_page.assert_reserve_first_ip_range()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_4545_create_new_dhcp(self):
		self.take_s1_snapshot()
		dhcp_page = self.LeftPanel.go_to_dhcp_page()
		dhcp_page.delete_dhcp_if_present()
		dhcp_page.create_new_dhcp()
		self.take_s2_snapshot()
		dhcp_page.delete_dhcp_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_4547_delete_dhcp_scope(self):
		self.take_s1_snapshot()
		dhcp_page = self.LeftPanel.go_to_dhcp_page()
		if not dhcp_page.is_dhcp_present():
			dhcp_page.create_new_dhcp()
		self.take_s2_snapshot()
		dhcp_page.delete_dhcp_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_4546_edit_dhcp_scope(self):
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
	
	def test_ath_11261_define_dhcp_scope_unprovisoned_ap(self):
		conf = self.config.config_vars
		
		dhcp_page = self.LeftPanel.go_to_dhcp_page()
		dhcp_page.delete_dhcp_scope()
		self.take_s1_snapshot()
		dhcp_page.click_on_distributed_dhcp_scopes_new()
		dhcp_page.create_distributed_dhcp(name =conf.distributed_dhcp_name1,type = conf.Dhcp_Network_Type,vlan = conf.dhcp_option_value,nmask = conf.local_dhcp_netmask,router = conf.local_dhcp_netmask,startip = conf.local_dhcp_netmask,endip = conf.end_ip,clients = conf.Edit_Client_Per_Branch,first = conf.Reserve_First,last = conf.Reserve_First)
		dhcp_page.click_on_distributed_dhcp_scopes_new()
		dhcp_page.create_distributed_dhcp(name =conf.distributed_dhcp_name2,type = conf.Dhcp_Network_Type2,vlan = conf.dhcp_option_value,server = conf.distributed_dhcp_dns_server,domain = conf.distributed_dhcp_domain_name,startip = conf.distributed_dhcp_ipaddress_range_start,endip = conf.distributed_dhcp_ipaddress_range_end,clients = conf.Edit_Client_Per_Branch,first = conf.Reserve_First,last = conf.Reserve_First)
		dhcp_page.click_centralize_accordion()
		dhcp_page.create_new_centralized_dhcp()
		dhcp_page.create_centralized_dhcp_scope(name = conf.centralized_dhcp_name1,vlan = conf.local_dhcp_option_type, relay = False,option82 = None,helper = None,ip = None, mask = None)
		dhcp_page.create_new_centralized_dhcp()
		dhcp_page.create_centralized_dhcp_scope(name = conf.centralized_dhcp_name2,vlan = conf.Edit_Client_Per_Branch, relay = True,option82 = 'None',helper = None,ip = conf.local_dhcp_network, mask = conf.local_dhcp_netmask)
		dhcp_page.go_to_local_dhcp_scopes_accordion()
		dhcp_page.create_new_local_dhcp()
		dhcp_page.create_local_new_dhcp_scope(name = conf.local_dhcp_name1, type = conf.dhcp_type_local, vlan = conf.edit_dhcp_option_value,network= conf.dhcp_network_address, netmask = conf.edit_Dhcp_Netmask,exaddress = conf.edit_dhcp_excluded_address, server = None,domain = None,time = None,optype = None, value = None)
		dhcp_page.create_new_local_dhcp()
		dhcp_page.create_local_new_dhcp_scope(name = conf.local_dhcp_name2, type = conf.local_l3, vlan = conf.dhcp_option_type,network= conf.subnet_address, netmask = conf.edit_Dhcp_Netmask,exaddress = conf.distributed_dhcp_ipaddress_range_start, server = None,domain = None,time = None,optype = None, value = None)
		self.take_s2_snapshot()
		dhcp_page.delete_dhcp_scope()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	