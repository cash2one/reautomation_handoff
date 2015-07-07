import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class NetworkAssignedVlanStatic(ConfigurationTest):
	'''
		Test class for test cases in Networkassigned vlan static module
	'''

	def test_ath_58_create_network_employee_vlan_static(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.employee_network_info()
		security       = virtual_lan.set_static_vlan()
		access   	   = security.set_wpa2_blacklisting_enable()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_3356_edit_network_vlan_dynamic(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.employee_network_info()
		security       = virtual_lan.set_static_vlan()
		access   	   = security.set_wpa2_blacklisting_enable()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		edit_network = self.NetworkPage.edit_network()
		edit_network.edit_vlan_settings()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
		