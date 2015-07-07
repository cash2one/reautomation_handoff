import logging
logger = logging.getLogger('athenataf')


from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DefaultValueCheck(ConfigurationTest):
	'''
		Test class for Default Value Check.
	'''

	def test_ath_11962_check_default_value_in_authentication_server(self):
		security_page = self.LeftPanel.go_to_security()
		self.browser.assert_element(security_page.no_data_msg, "No Data msg not visible ")
		self.browser.assert_element(security_page.name_col, "Name coloumn not present")
		self.browser.assert_element(security_page.type_col, "Type coloumn not present")
		security_page.create_auth_server.click()
		security_page.assert_radius_radio('true')
		security_page.assert_ldpa_radio('false')
		security_page.assert_tacacs_radio('false')
		security_page.assert_coa_only_checkbox('false')
		security_page.assert_auth_server_name()
		security_page.assert_auth_ipaddr()
		security_page.assert_auth_sharedkey()
		security_page.assert_retype_auth_shared_key()
		security_page.assert_rfc_3576('false')
		security_page.assert_dead_time()
		security_page.assert_timeout()
		security_page.assert_retry_count()
		security_page.assert_auth_port()
		security_page.assert_optional_feilds()
		
		
	def test_ath_13332_check_radius_ldpa_default_values(self):
		security_page = self.LeftPanel.go_to_security()
		security_page.create_auth_server.click()
		security_page.assert_radius_radio('true')
		security_page.assert_auth_server_name()
		security_page.assert_auth_ipaddr()
		security_page.assert_auth_sharedkey()
		security_page.assert_retype_auth_shared_key()
		security_page.assert_rfc_3576('false')
		security_page.assert_dead_time()
		security_page.assert_timeout()
		security_page.assert_retry_count()
		security_page.assert_auth_port()
		security_page.assert_optional_feilds()
		security_page.ldap_radio_button.click()
		security_page.assert_ldpa_name()
		security_page.assert_ldpa_ipaddr()
		security_page.assert_ldpa_admin_pass()
		security_page.assert_ldpa_admin_retype_pass()
		security_page.assert_admin_dn()
		security_page.assert_base_dn()
		security_page.assert_ldap_Port()
		security_page.assert_ldpa_Filter()
		security_page.assert_ldpa_KeyAttribute()
		security_page.assert_ldpa_timeout()
		security_page.assert_ldpa_retry_count()
		
		
	def test_ath_13333_check_tacacs_coa_default_values(self):
		security_page = self.LeftPanel.go_to_security()
		security_page.create_auth_server.click()	
		security_page.tacacs_radio.click()
		security_page.assert_auth_server_tacacs_name()
		security_page.assert_auth_tacacs_ipaddr()
		security_page.assert_auth_tacacs_sharedkey()
		security_page.assert_retype_auth_tacacs_shared_key()
		security_page.assert_Auth_Tacacs_Port()
		security_page.assert_auth_tacacs_timeout()
		security_page.assert_auth_tacacs_retry_count()
		security_page.coa_only_checkbox.click()
		security_page.assert_auth_server_name()
		security_page.assert_auth_ipaddr()
		security_page.assert_auth_sharedkey()
		security_page.assert_retype_auth_shared_key()
		security_page.assert_airGroup_port()