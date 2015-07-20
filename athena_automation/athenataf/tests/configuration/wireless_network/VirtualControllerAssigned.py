import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class VirtualControllerAssigned(ConfigurationTest):
	'''
		Test class for test cases in Network assigned module
	'''


	def test_ath_1633_create_network_employee_virtual_controller_assigned(self):
		'''
		create a Employee network with VirtualControllerAssigned WPA2-Personal Security
		'''
		self.take_s1_snapshot()
		self.NetworkPage.delete_network_if_present()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.employee_network_info()
		security       = virtual_lan.select_virtual_controller()
		access   	   = security.set_wpa2_blacklisting_enable()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_3357_edit_network_vlan_network_assigned(self):

		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.employee_network_info()
		security       = virtual_lan.select_virtual_controller()
		access   	   = security.set_wpa2_blacklisting_enable()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		time.sleep(5)
		edit_network = self.NetworkPage.edit_network()
		time.sleep(5)
		edit_network.edit_vlan_settings(network_assigned=True)
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		