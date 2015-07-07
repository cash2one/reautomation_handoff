import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DefaultValueCheck(ConfigurationTest):
	'''
	Test class for System .
	'''
		
	def test_ath_11357_enterprise_domain_default_values(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.click_enterprise_domain()
		system_page.assert_enterprise_domain_names_empty()
		system_page.create_new_domain()
		system_page.assert_enter_new_domain_name_popup_textbox_empty()
					