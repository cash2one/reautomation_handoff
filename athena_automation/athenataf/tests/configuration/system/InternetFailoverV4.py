import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class InternetFailoverV4(ConfigurationTest):
	'''
	Test class for System UsbAuthTypeV4 module.
	'''

	def test_ath_4573_feild_value_configuration(self):
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.click_uplink()
		system_page.assert_internet_failover_default_values()
		system_page.configure_internet_failover()
		self.take_s2_snapshot()
		system_page.click_uplink()
		system_page.restore_internet_failover_default_values()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		