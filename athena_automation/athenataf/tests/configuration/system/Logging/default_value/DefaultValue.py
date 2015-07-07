import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DefaultValue(ConfigurationTest):
	'''
	Test class for System Logging DefaultValue.
	'''
		
	def test_ath_11360_syslog_server_default_values(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.click_logging()
		system_page.assert_syslog_server()
		system_page.assert_tftp_dump_server()
		system_page.assert_syslog_facility_levels_default_values()
		
	