import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Logging(ConfigurationTest):
	'''
	Test class for System General.
	'''
	
	def test_ath_1436_logging_non_default_server(self):

		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.click_logging()
		system_page.assert_logging_page()
		system_page.add_syslog_server()
		import time
		time.sleep(10)
		self.take_s2_snapshot()
		system_page.click_logging()
		system_page.revert_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		# system_page.assert_add_syslog_server()
		
	def test_ath_1437_syslog_non_default_values(self):
		self.take_s1_snapshot()
		conf = self.config.config_vars
		system_page = self.LeftPanel.go_to_system_page()
		system_page.click_logging()
		system_page.set_non_default_values(conf.Emergency,conf.Alert,conf.Critical,conf.Error,conf.Warning,conf.Notice,conf.Information,conf.Debug)
		self.take_s2_snapshot()
		system_page.click_logging()
		system_page.assert_syslog_facility_levels()
		system_page.restore_default_values()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	