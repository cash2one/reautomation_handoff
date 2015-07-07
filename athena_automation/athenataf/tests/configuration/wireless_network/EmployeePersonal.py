import logging
logger = logging.getLogger('athenataf')


from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class EmployeePersonal(ConfigurationTest):
	'''
		Test class for network configuration wireless network.
	'''
	
	def _create_employee_network(self,wpa_wpa2=False):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.employee_network_info()
		security       = virtual_lan.use_vlan_defaults()
		if not wpa_wpa2:
			access   	   = security.configure_employee_security()
		else:
			access   	   = security.configure_employee_security(both=True)
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_2_createnetwork_employee(self,wpa_wpa2=False):
		self._create_employee_network()
		
	def test_ath_4_createnetwork_employee_wpa_wpa2(self):
		self._create_employee_network(wpa_wpa2=True)
		
		
		

