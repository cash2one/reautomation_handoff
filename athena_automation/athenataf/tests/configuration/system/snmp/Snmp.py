import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Snmp(ConfigurationTest):
	'''
	Test class for System Snmp.
	'''
	
	def test_ath_8376_snmp_community_string_validation(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_snmp_tab()
		system_page.snmp_community_string_validation()