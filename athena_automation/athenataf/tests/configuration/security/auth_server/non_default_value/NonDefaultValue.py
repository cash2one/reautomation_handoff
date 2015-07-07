import logging
logger = logging.getLogger('athenataf')


from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class NonDefaultValue(ConfigurationTest):
	'''
		Test class for network configuration Security.
	'''

	def test_ath_12060_create_radius_with_drp_enabled(self):
		self.take_s1_snapshot()
		conf = self.config.config_vars
		system = self.LeftPanel.go_to_system_page()
		system.set_general_dynamic_proxy(conf.manage_internet_failover_value)
		system._save_settings()
		security_page = self.LeftPanel.go_to_security()
		security_page.create_new_server()
		security_page.create_authentication_server('Myradius','10.23.24.25','Aruba#123','Aruba#123',mask = '255.255.255.0',dip='10.23.24.26',gateway = '10.23.24.1',vlan='15')
		logger.debug('SecurityPage : Clicking save button')
		security_page.auth_server_save.click()
		self.take_s2_snapshot()
		security_page.delete_authentication_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()