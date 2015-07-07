import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class MacFormat(ConfigurationTest):
	'''
	Test class for Mac format module of wireless networks.
	'''

	def _create_employee_wireless_network(self,enterprise=False,open_security=False):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		if enterprise:
			access = security.create_network_mac_authentication_enabled(enterprise=True)
		elif open_security :
			access = security.create_network_mac_authentication_enabled(open_security=True)
		else:
			access = security.create_network_mac_authentication_enabled()
		access.finish_network_setup()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.set_uppercase_delimiter_option()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()


	def test_ath_3967_create_network_employee_personal_mac_authentication(self):
		self._create_employee_wireless_network()

	def test_ath_3968_create_network_employee_enterprise_mac_authentication(self):
		self._create_employee_wireless_network(enterprise=True)

	def test_ath_3969_create_network_employee_open_mac_authentication(self):
		self._create_employee_wireless_network(open_security=True)
        
        
    