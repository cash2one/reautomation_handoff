import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class FieldValidation(ConfigurationTest):
	'''
	Test class for System Admin Field Validation.
	'''
		
	def test_ath_11944_system_help_text(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_admin_tab()
		system_page.enable_help()
		system_page.assert_help_option()
		
	def test_ath_11321_username_password_field_validation(self):
		conf = self.config.config_vars
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_admin_tab()
		system_page.validate_local_uname_passwd_field()
		system_page.validate_admin_viewonly_fields()
		system_page.guest_registration_only_non_default_values(conf.admin_invalid_u_name,conf.admin_password,conf.admin_unmatch_p_word)
		system_page._save_settings()
		system_page.assert_admin_guest_pasword_error_msg(assert_msg=True)
		system_page.set_admin_local_uname_and_pswrd(conf.uname, conf.admin_paswd, conf.admin_paswd)
		system_page.view_only_non_default_values(conf.viewonly,conf.viewonly,conf.viewonly)
		system_page.guest_registration_only_non_default_values(conf.guest_username,conf.guest_password,conf.guest_password)
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
	
	
	
	
	
	
	
	