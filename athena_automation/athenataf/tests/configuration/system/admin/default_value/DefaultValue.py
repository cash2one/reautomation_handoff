import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DefaultValue(ConfigurationTest):
	'''
	Test class for System Admin DefaultValue.
	'''
	
		
	def test_ath_11324_local_sever_default_values(self):
		''' Assertion'''
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_admin_tab()
		system_page.assert_local_server_default_values()
		system_page.assert_view_only_default_values()
		system_page.assert_guest_registration_only_default_values()
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	