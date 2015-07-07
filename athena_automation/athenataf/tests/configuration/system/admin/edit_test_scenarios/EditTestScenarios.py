import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class EditTestScenarios(ConfigurationTest):
	'''
	Test class for System Admin Non Default Value.
	'''
		
	def test_ath_11945_edit_view_only_guest_registration_only_values(self):
		conf = self.config.config_vars
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_admin_tab()
		system_page.view_only_non_default_values(conf.viewonly,conf.viewonly,conf.viewonly)
		system_page._save_settings()
		system_page.go_to_admin_tab()
		system_page.guest_registration_only_non_default_values(conf.guest_username,conf.guest_password,conf.guest_password)
		system_page._save_settings()
		system_page.go_to_admin_tab()
		system_page.view_only_non_default_values(conf.edit_viewonly_username,conf.edit_viewonly_password,conf.edit_viewonly_password)
		system_page._save_settings()
		system_page.go_to_admin_tab()
		system_page.guest_registration_only_non_default_values(conf.edit_guest_username,conf.edit_guest_password,conf.edit_guest_password)
		system_page._save_settings()
		self.take_s2_snapshot()
		system_page.go_to_admin_tab()
		system_page.restore_view_only_default_values()
		system_page.go_to_admin_tab()
		system_page.restore_guest_registration_only_default_values()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()