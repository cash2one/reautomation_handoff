import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class NetworkAssignedVlanDynamic(ConfigurationTest):
	'''
		Test class for test cases in Networkassigned vlan Dynamic module
	'''
	
	def test_ath_1641_check_dynamic_vlan_attribute_list(self):
		self.take_s1_snapshot()
		self.NetworkPage.delete_network_if_present()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.employee_network_info()
		virtual_lan.check_dynamic_vlan_attribute_list()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
			
	def test_ath_1642_create_vlan_assignment_rules(self):
		'''
		Create five dynamic vlan assignment rules 
		'''
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.employee_network_info()
		security	   = virtual_lan.create_vlan_assignment_rules()
		access   	   = security.set_wpa2_blacklisting_enable()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	

