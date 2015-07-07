import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class NonDefaultValueCheck(ConfigurationTest):
    '''
    Test class for System NonDefaultValueCheck module.
    '''
    
    def test_ath_11358_enterprise_domain_non_default_value(self):
		conf=self.config.config_vars
		system_page = self.LeftPanel.go_to_system_page()
		self.take_s1_snapshot()
		system_page.click_enterprise_domain()
		system_page.set_enterprise_domain_non_default_values(conf.valid_Proxy_exception_value6)
		system_page._save_settings()
		system_page.click_enterprise_domain()
		system_page.set_enterprise_domain_non_default_values(conf.valid_Proxy_exception_value5)
		system_page.set_enterprise_domain_non_default_values(conf.enterprise_domain_value)
		system_page.set_enterprise_domain_non_default_values(conf.enterprise_domain_value1)
		system_page.set_enterprise_domain_non_default_values(conf.enterprise_domain_value2)
		system_page.set_enterprise_domain_non_default_values(conf.enterprise_domain_value3)
		system_page.set_enterprise_domain_non_default_values(conf.enterprise_domain_value4)
		system_page.set_enterprise_domain_non_default_values(conf.enterprise_domain_value5)
		system_page._save_settings()
		self.take_s2_snapshot()
		system_page.click_enterprise_domain()
		system_page.delete_created_domains()
		system_page._save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()