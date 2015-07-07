import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class FieldValidation(ConfigurationTest):
	'''
	Test class for System Logging Field Validation
	'''
		
	def test_ath_11951_syslog_server_help_content(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.click_logging()
		system_page.enable_help()
		system_page.assert_help_option_for_logging()
		
	def test_ath_11362_check_syslog_server_fields(self):
		conf = self.config.config_vars
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.click_logging()
		system_page.set_syslog_server(conf.invalid_syslog_server)
		system_page._save_settings()
		system_page.assert_syslog_server_ip()
		system_page.set_syslog_server(conf.sys_log_ip)
		system_page._save_settings()
		self.take_s2_snapshot()
		system_page.click_logging()
		system_page.set_syslog_server('')
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()