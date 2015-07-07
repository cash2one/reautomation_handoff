import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class NonDefaultValueCheck(ConfigurationTest):
	'''
	Test class for System NonDefaultValueCheck.
	'''
	def test_ath_11381_check_non_default_values_for_proxy(self):
		conf=self.config.config_vars
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_proxy_tab()
		system_page.set_proxy_server_value(conf.valid_Proxy_Server_value)
		system_page.set_proxy_port_value(conf.valid_Proxy_Port_value)
		system_page.click_on_proxy_new_exception()
		system_page.set_proxy_exception_value(conf.valid_Proxy_exception_value)
		system_page.click_on_proxy_exception_ok()
		system_page._save_settings()
		system_page.go_to_proxy_tab()
		system_page.click_on_proxy_new_exception()
		system_page.non_default_values_for_proxy_exception()
		system_page._save_settings()
		self.take_s2_snapshot()
		system_page.go_to_proxy_tab()
		system_page.set_proxy_server_value(None)
		system_page.set_proxy_port_value(None)
		system_page.delete_proxy_multiple_exceptions(7)
		system_page._save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
		
		
		