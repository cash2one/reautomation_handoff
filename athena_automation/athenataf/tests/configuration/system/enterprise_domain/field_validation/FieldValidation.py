import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class FieldValidation(ConfigurationTest):
	'''
	Test class for System Enterprise_Domain.
	'''
	def test_ath_11955_enterprise_domain_field_validation(self):
		# TestCase_11955 is parked due to bug
		path = self.config.config_vars
		system_page = self.LeftPanel.go_to_system_page()
		system_page.click_enterprise_domain()
		system_page.create_new_domain()
		
		#--------Waiting to correct the function according to assertion message-----------------------------------------------
		
		# system_page.assert_invalid_enterprise_domain_name_and_ip(path.domain_name_invalid)
		# system_page.assert_invalid_enterprise_domain_name_and_ip(path.domain_ip_invalid)		