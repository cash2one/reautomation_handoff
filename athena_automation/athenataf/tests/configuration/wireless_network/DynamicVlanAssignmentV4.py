import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DynamicVlanAssignmentV4(ConfigurationTest):
	'''
	Test class for network configuration wireless network.
	'''
	
	def test_ath_3994_mac_dscp_address_attribute(self):
		basic_info = self.NetworkPage.create_new_network()
		self.take_s1_snapshot()
		vlan = basic_info.employee_network_info()
		vlan.create_dynamic_vlan_assignment_rule()
		security = vlan.click_on_next()
		access = security.configure_employee_security()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()