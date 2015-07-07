import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class CaleaV4(ConfigurationTest):
	'''
	Test class for Iap wired networks testcases.
	'''

	def test_ath_4003_network_based_network(self):
		self.take_s1_snapshot()
		self.NetworkPage.delete_wired_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.wired_employee_network_info()
		security = vlan_obj.wired_vlan_defaults()
		access = security.wired_security_defaults()
		access.click_network_access()
		access.access_rule_type_calea()
		access.assert_calea()
		network_assign = access.click_next()
		network_assign.finish_network_setup()
		self.NetworkPage.assert_wired_network()
		self.take_s2_snapshot()
		self.NetworkPage.delete_wired_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_4004_role_based_network(self):
		self.take_s1_snapshot()
		self.NetworkPage.delete_wired_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.wired_employee_network_info()
		security = vlan_obj.wired_vlan_defaults()
		access = security.wired_security_defaults()
		access.click_role_access()
		access.access_rule_type_calea()
		access.assert_calea()
		network_assign = access.click_next()
		network_assign.finish_network_setup()
		self.NetworkPage.assert_wired_network()
		self.take_s2_snapshot()
		self.NetworkPage.delete_wired_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
