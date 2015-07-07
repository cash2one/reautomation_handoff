import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Admin(ConfigurationTest):
	'''
	Test class for System Admin.
	'''
	
	def test_ath_1425_internal_server_nondefault_values(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_admin_tab()
		system_page.set_username_and_password('invalid' , None)
		system_page.assert_error_message_present()
		system_page.set_username_and_password('valid' , None)
		system_page.go_to_admin_tab()
		system_page.set_username_and_password(None , 'mismatch')
		system_page.assert_error_message_present()
		system_page.set_username_and_password(None , 'match')
	
	def test_ath_1426_radius_server_new(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_admin_tab()
		system_page.create_new_radius_server('without fallback')
		system_page.go_to_admin_tab()
		system_page.assert_new_auth_server_present()
		system_page.set_admin_authentication_default_value()
	
	def test_ath_1427_radius_server_fallback_to_internal(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_admin_tab()
		system_page.create_new_radius_server('with fallback')
		system_page.go_to_admin_tab()
		system_page.set_username_and_password('valid' , 'match')
		system_page.go_to_admin_tab()
		system_page.assert_new_auth_server_present()
		system_page.set_admin_authentication_default_value()
	
	def test_ath_8309_local_sever_default_values(self):
		''' Assertion'''
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_admin_tab()
		system_page.assert_local_server_default_values()
		
	def test_ath_8311_view_only_default_values(self):
		''' Assertion'''
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_admin_tab()
		system_page.assert_view_only_default_values()
		
	def test_ath_8321_guest_registration_only_default_values(self):
		''' Assertion'''
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_admin_tab()
		system_page.assert_guest_registration_only_default_values()
		
	def test_ath_8323_guest_registration_only_non_default_values(self):
		conf = self.config.config_vars
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_admin_tab()
		system_page.guest_registration_only_non_default_values(conf.guest,conf.guest,conf.guest)
		system_page._save_settings()
		self.take_s2_snapshot()
		system_page.go_to_admin_tab()
		system_page.restore_guest_registration_only_default_values()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()