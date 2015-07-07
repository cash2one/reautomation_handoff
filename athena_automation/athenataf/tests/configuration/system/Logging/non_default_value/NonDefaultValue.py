import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class NonDefaultValue(ConfigurationTest):
	'''
	Test class for System Logging Non Default Value.
	'''
		
	def test_ath_11361_syslog_server_non_default_values(self):
		conf = self.config.config_vars
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.click_logging()
		system_page.set_syslog_server(conf.sys_log_ip)
		system_page.set_tftp_dump_server(conf.tftp_dump_server_ip) 
		system_page.set_non_default_values(conf.Emergency,conf.Alert,conf.Critical,conf.Error,conf.Warning,conf.Notice,conf.Information,conf.Debug)
		self.take_s2_snapshot()
		system_page.click_logging()
		system_page.set_syslog_server('')
		system_page.set_tftp_dump_server('')
		system_page.restore_default_values()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	