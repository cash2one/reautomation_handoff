import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DefaultValues(ConfigurationTest):
	'''
	Test class for Default Values test cases 
	'''
			
	def test_ath_11049_rtls(self):
		services_page = self.LeftPanel.go_to_services()
		services_page.assert_entire_rtls_fields()
		
	def test_ath_11051_open_dns(self):
		services_page = self.LeftPanel.go_to_services()
		services_page.assert_open_dns_feilds()
		
	def test_ath_11052_calea(self):
		services_page = self.LeftPanel.go_to_services()
		services_page.assert_calea_configuration_default()
		

	def test_ath_11053_network_integration(self):
		services_page = self.LeftPanel.go_to_services()
		services_page.assert_network_integration_default()
		
	def test_ath_11048_airgroup(self):
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security() 
		security_page.go_to_roles()
		security_page.create_new_role()
		services_page = self.LeftPanel.go_to_services()
		services_page.assert_airgroup_checkbox_disabled()
		services_page.enable_airgroup()
		services_page.assert_air_group_settings()
		services_page.enable_airgroup_clearpass()
		services_page.assert_airprint_disallowed_roles_and_vlans()
		services_page.assert_air_play_disallowed_roles_and_vlans()
		services_page.assert_itunes_disallowed_roles_and_vlans()
		services_page.assert_remote_management_disallowed_roles_and_vlans()
		services_page.assert_sharing_disallowed_roles_and_vlans()
		services_page.assert_chat_disallowed_roles_and_vlans()
		services_page.assert_allow_all_disallowed_roles_and_vlans()
		self.take_s2_snapshot()
		security_page = self.LeftPanel.go_to_security()
		security_page.go_to_roles()
		security_page.delete_roles()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11054_app_rf(self):
		services_page = self.LeftPanel.go_to_services()
		services_page.click_on_app_rf_accordion()
		services_page.assert_enable_dpi('false')
		
	def test_ath_11059_cppm_server_for_airgroup(self):
		conf = self.config.config_vars
		services_page = self.LeftPanel.go_to_services()
		services_page.enable_air_group.click()
		services_page.buy_time()
		services_page.set_cppm_server1(conf.new_cppm_server_name)
		services_page.assert_radius_radio('true')
		services_page.assert_auth_server_name()
		services_page.assert_auth_ipaddr()
		services_page.assert_auth_sharedkey()
		services_page.assert_retype_auth_shared_key()
		services_page.assert_rfc_3576('false')
		services_page.set_rfc_3576('enable')
		services_page.assert_airGroup_port()
		services_page.assert_auth_account_port()
		services_page.assert_dead_time()
		services_page.assert_timeout()
		services_page.assert_retry_count()
		services_page.assert_auth_port()
		services_page.tacacs_radio.click()
		services_page.assert_auth_server_tacacs_name()
		services_page.assert_auth_tacacs_ipaddr()
		services_page.assert_auth_tacacs_sharedkey()
		services_page.assert_retype_auth_tacacs_shared_key()
		services_page.assert_Auth_Tacacs_Port()
		services_page.assert_auth_tacacs_timeout()
		services_page.assert_auth_tacacs_retry_count()
		services_page.auth_coa_only.click()
		services_page.assert_radius_radio('true')
		services_page.assert_auth_server_name()
		services_page.assert_auth_ipaddr()
		services_page.assert_auth_sharedkey()
		services_page.assert_retype_auth_shared_key()
		services_page.assert_airGroup_port()
		services_page.cppm_cancel_button.click()
		services_page.click_on_enable_air_group()
		services_page.save_settings()		