import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class NonDefaultValue(ConfigurationTest):
	'''
	Test class for System Admin Non Default Value.
	'''
		
	def test_ath_11325_view_only_guest_registration_only_non_default_values(self):
		conf = self.config.config_vars
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_admin_tab()
		system_page.view_only_non_default_values(conf.viewonly,conf.viewonly,conf.viewonly)
		system_page._save_settings()
		system_page.go_to_admin_tab()
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
		
	def test_ath_11320_internal_server_nondefault_values(self):
		conf = self.config.config_vars
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_admin_tab()
		system_page.set_admin_authentication_value(conf.authentication_value)
		system_page.set_username_and_password_field(conf.user_name_2,conf.password_2)
		system_page._save_settings()
		system_page.go_to_admin_tab()
		system_page.set_admin_authentication_value(conf.authentication_value_2)
		system_page._assert_admin_local_auth_server_fields()
		system_page.create_new_radius_server_one(conf.authserver_name_1,conf.subnet_ip1,conf.password_2)
		system_page.create_new_tacacs_server(conf.authserver_name_2,conf.subnet_ip1,conf.password_2)
		system_page.assert_auth_server_1_value(conf.authserver_name_1)
		system_page.assert_auth_server_2_value(conf.authserver_name_2)
		system_page._save_settings()
		system_page.go_to_admin_tab()
		system_page.set_admin_authentication_value(conf.authentication_value_3)
		system_page._assert_admin_local_radius_server_fallback_fields()
		system_page.create_new_radius_server_one(conf.authserver_name_3,conf.ntp_server,conf.chap_secret)
		system_page.assert_auth_server_1_value(conf.authserver_name_3)
		system_page._save_settings()
		system_page.go_to_admin_tab()
		system_page.set_admin_authentication_value(conf.authentication_value_3)
		system_page._assert_admin_local_radius_server_fallback_fields()
		system_page.create_new_tacacs_server(conf.authserver_name_4,conf.authserver_ip,conf.auth_shared_key_2)
		system_page.assert_auth_server_2_value(conf.authserver_name_4)
		system_page._save_settings()
		self.take_s2_snapshot()
		system_page.go_to_admin_tab()
		system_page.set_admin_authentication_default_value()
		
		self.LeftPanel.go_to_network_page()
		self._delete_network_auth_server()
		security_page = self.LeftPanel.go_to_security() 
		security_page.delete_authentication_server_3()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def _delete_network_auth_server(self):
		'''
		Delete wireless and auth servers 
		'''
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security() 
		security_page.delete_authentication_server()
		security_page.delete_authentication_server2()
		self.LeftPanel.go_to_network_page()	
	
	
	
	
	