import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class NonDefaultValue(ConfigurationTest):
	'''
	Test class for System General->NonDeafault value .
	'''
	
	def test_ath_11302_check_non_default_values_cpu_util(self):
		network_page = self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		conf = self.config.config_vars
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.configure_employee_security()
		access.click_network_access()
		access.finish_network_setup()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.set_non_default_values_cpu_util()
		system_page._save_settings()
		self.take_s2_snapshot()
		network_page = self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.set_cpu_util_default_values()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()