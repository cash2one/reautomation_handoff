import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class FieldValidation(ConfigurationTest):
	'''
	Test class for System FieldValidation.
	'''
	def test_ath_11383_validate_proxy_fields(self):
		conf=self.config.config_vars
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_proxy_tab()
		system_page.set_proxy_server_value(conf.invalid_Proxy_Server_value)
		system_page.set_proxy_port_value(conf.invalid_Proxy_Port_value)
		system_page._save_settings()
		system_page.assert_proxy_server_error('true')
		system_page.assert_proxy_port_error('true')
		system_page.click_on_proxy_new_exception()
		system_page.set_proxy_exception_value(conf.invalid_Proxy_exception_value)
		system_page.click_on_proxy_exception_ok()
		system_page.assert_proxy_exception_error('true')
		system_page.click_on_proxy_exception_cancel()
		system_page.click_on_cancel_settings()
		
		