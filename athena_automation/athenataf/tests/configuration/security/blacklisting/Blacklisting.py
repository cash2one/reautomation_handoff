import logging
logger = logging.getLogger('athenataf')


from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Blacklisting(ConfigurationTest):
	'''
		Test class for network configuration Security.
	'''

	def test_ath_1651_add_clients_to_manual_blacklisting(self):
		security_page = self.LeftPanel.go_to_security()
		security_page.go_to_blacklisting()
		security_page.delete_blacklisting_if_present()
		self.take_s1_snapshot()
		security_page.create_manual_blacklisting()
		security_page.go_to_blacklisting()
		security_page.assert_manual_blacklisting_present()
		self.take_s2_snapshot()
		security_page.delete_manual_blacklisting()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1652_dynamic_blacklisting(self):
		conf = self.config.config_vars
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security()
		security_page.go_to_blacklisting()
		security_page.create_dynamic_blacklisting(conf.dynm_blklst_failure_time1, conf.dynm_blklst_time_unit1)
		security_page.go_to_blacklisting()
		security_page.create_dynamic_blacklisting(conf.dynm_blklst_failure_time2, conf.dynm_blklst_time_unit2)
		security_page.go_to_blacklisting()
		security_page.create_dynamic_blacklisting(conf.dynm_blklst_failure_time3, conf.dynm_blklst_time_unit3)
		self.take_s2_snapshot()
		security_page.go_to_blacklisting()
		security_page.set_dynamic_blacklisting_to_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(1)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1654_delete_blacklisting(self):
		security_page = self.LeftPanel.go_to_security()
		security_page.go_to_blacklisting()
		security_page.delete_blacklisting_if_present()
		security_page.create_manual_blacklisting()
		security_page.go_to_blacklisting()
		security_page.assert_manual_blacklisting_present()
		self.take_s1_snapshot()
		security_page.delete_manual_blacklisting()
		security_page.go_to_blacklisting()
		security_page.assert_manual_blacklisting_not_present()
		self.take_s2_snapshot()
		security_page.create_manual_blacklisting()
		security_page.go_to_blacklisting()
		self.take_s3_snapshot()
		security_page.delete_manual_blacklisting()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()