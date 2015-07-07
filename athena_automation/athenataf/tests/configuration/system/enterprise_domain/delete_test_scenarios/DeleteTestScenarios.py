import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DeleteTestScenarios(ConfigurationTest):
	'''
	Test class for System Enterprise_Domain.
	'''
	def test_ath_11359_delete_the_created_domains(self):
		path = self.config.config_vars
		system_page = self.LeftPanel.go_to_system_page()
		self.take_s1_snapshot()
		system_page.click_enterprise_domain()
		system_page.create_new_domain()
		system_page.set_domain_name_value(path.domain_name_valid1)
		system_page._save_domain()
		system_page.create_new_domain()
		system_page.set_domain_name_value(path.domain_name_valid2)
		system_page._save_domain()
		system_page.create_new_domain()
		system_page.set_domain_name_value(path.domain_name_valid3)
		system_page._save_domain()
		system_page.create_new_domain()
		system_page.set_domain_name_value(path.domain_name_valid4)
		system_page._save_domain()
		system_page.create_new_domain()
		system_page.set_domain_name_value(path.domain_name_valid5)
		system_page._save_domain()
		system_page._save_settings()
		self.take_s2_snapshot()
		system_page.click_enterprise_domain()
		system_page.delete_domain_name(system_page.gmail_delete_icon)
		system_page.delete_domain_name(system_page.yahoo_co_in_delete_icon)
		system_page.delete_domain_name(system_page.arubathena_com_delete_icon)
		system_page._save_settings()
		system_page.click_enterprise_domain()
		system_page.assert_domain_name(system_page.gmail_delete_icon)
		system_page.assert_domain_name(system_page.yahoo_co_in_delete_icon)
		system_page.assert_domain_name(system_page.arubathena_com_delete_icon)
		system_page.delete_domain_name(system_page.google_delete_icon)
		system_page.delete_domain_name(system_page.yahoo_com_delete_icon)
		system_page._save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		