import logging
logger = logging.getLogger('athenataf')


from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class EditTestScenario(ConfigurationTest):
	'''
		Test class for Default Value Check.
	'''

	def test_ath_13331_check_default_value_in_authentication_server(self):
		conf = self.config.config_vars
		security_page = self.LeftPanel.go_to_security()
		if security_page.ldapser_delete:
			logger.debug('SecurityPage : Clicking on Delete button')
			security_page.ldapser_delete.click()
		self.take_s1_snapshot()
		logger.debug('SecurityPage : Clicking on New button')
		security_page.create_auth_server.click()
		logger.debug('SecurityPage : Clicking on LDAP radio button')
		security_page.ldap_radio_button.click()
		security_page.create_new_ldap_auth_server(name = conf.server_name,ip = conf.valid_auth_server_ip,port = None,admin = conf.admin_dn_name,passphrase = conf.ldap_pass_phrase,retypepass = conf.ldap_pass_phrase,base = conf.base_dn,filter = None,key = None,timeout = None,retry = None)
		security_page.ldapser_edit.click()
		security_page.create_new_ldap_auth_server(name = None,ip = conf.auth_radius_ip1,port = conf.invalid_radius_server_acc_port_65535,admin = conf.admin_dn,passphrase = conf.ldap_pass_phrase,retypepass = conf.ldap_pass_phrase,base = conf.base_dn_name,filter = None,key = conf.key_attribute,timeout = conf.timeout,retry = conf.retry)
		self.browser.assert_element(security_page.ldapport_error,'Port validation error is not displayed')
		self.browser.assert_element(security_page.timeTxt_error,'Timeout validation error is not displayed')
		self.browser.assert_element(security_page.ldap_retry_count_error,'Retry count validation error is not displayed')
		security_page.create_new_ldap_auth_server(name = None,ip = conf.auth_radius_ip1,port = conf.auth_port_valid,admin = conf.admin_dn,passphrase = conf.ldap_pass_phrase,retypepass = conf.ldap_pass_phrase,base = conf.base_dn_name,filter = None,key = conf.key_attribute,timeout = conf.dynm_blklst_failure_time3,retry = conf.retry_count)
		self.take_s2_snapshot()
		if security_page.ldapser_delete:
			logger.debug('SecurityPage : Clicking on Delete button')
			security_page.ldapser_delete.click()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_13338_check_default_value_in_authentication_server(self):
		conf = self.config.config_vars
		security_page = self.LeftPanel.go_to_security()
		if security_page.testRole_delete:
			logger.debug('SecurityPage : Clicking on Delete button')
			security_page.testRole_delete.click()
		self.take_s1_snapshot()
		logger.debug('SecurityPage : Clicking on New button')
		security_page.create_auth_server.click()
		logger.debug('SecurityPage : Clicking on TACACS radio button')
		security_page.tacacs_radio.click()
		security_page.create_new_tacacs_auth_server(name = conf.Role_Name, key = conf.time_out_invalid, retype = conf.time_out_invalid, port = None, timeout = None, ip = conf.auth_server_ip_valid, retry = None)
		logger.debug('SecurityPage : Clicking on edit button')
		security_page.testRole_edit.click()
		security_page.create_new_tacacs_auth_server(name = None, key = None, retype = None, port = conf.invalid_radius_server_acc_port_65535, timeout = conf.timeout1, ip = None, retry = conf.retry)
		self.browser.assert_element(security_page.AuthPort_error,'Port validation error is not displayed')
		self.browser.assert_element(security_page.auth_tacacs_timeout_error,'Timeout validation error is not displayed')
		self.browser.assert_element(security_page.Auth_Retry_Count_error,'Retry count validation error is not displayed')
		security_page.create_new_tacacs_auth_server(name = None, key = None, retype = None, port = conf.auth_port_valid, timeout = conf.dynm_blklst_failure_time3, ip = None, retry = conf.retry1)
		self.take_s2_snapshot()
		if security_page.testRole_delete:
			logger.debug('SecurityPage : Clicking on Delete button')
			security_page.testRole_delete.click()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_13330_edit_coa_only_server(self):
		conf = self.config.config_vars
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security()
		security_page.create_auth_server.click()
		security_page.click_coa_only_checkbox()
		security_page.set_auth_server_name(conf.coa_name)
		security_page.set_auth_server_ip_address(conf.coa_ip_address)
		security_page.set_auth_shared_key_retype(conf.coa_shared_key,conf.coa_shared_key)
		security_page.set_air_group_coa_port()
		security_page.save_auth_server()
		security_page.click_edit_auth_server()
		security_page.set_auth_server_ip_address(conf.coa_ip_address_2)
		security_page.set_auth_shared_key_retype(conf.coa_shared_key_2,conf.coa_shared_key_2)
		security_page.set_air_group_coa_port(conf.auth_port_valid)
		security_page.save_auth_server()
		self.take_s2_snapshot()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_authentication_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_12057_edit_the_created_radius_server(self):
		conf = self.config.config_vars
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security()
		security_page.create_auth_server.click()
		security_page.set_auth_server_name(conf.auth_rad1)
		security_page.set_auth_server_ip_address(conf.auth_rad1_ip)
		security_page.set_auth_shared_key_retype(conf.shared_key_2,conf.shared_key_2)
		security_page.save_auth_server()
		security_page.click_edit_auth_server()
		security_page.editing_created_authserver_values(conf.radius_ip,conf.coa_shared_key_2,conf.time_10,conf.vlan,conf.count,conf.nas_ip_2,conf.nas_identifier,conf.port_6553,conf.port_3556,rfc=True)
		security_page.set_air_group_coa_port(conf.auth_port_valid)
		security_page.save_auth_server()
		
		security_page.create_auth_server.click()
		security_page.set_auth_server_name(conf.auth_radius_name1)
		security_page.set_auth_server_ip_address(conf.auth_radius_ip1)
		security_page.set_auth_shared_key_retype(conf.auth_radius_shared_key1,conf.auth_radius_shared_key1)
		security_page.click_rfc_3576_checkbox()
		security_page.setting_nas_ip_and_identifier(conf.nas_ip,conf.nas_identifier_2)
		security_page.save_auth_server()
		security_page.clicking_rad2_edit_button()
		security_page.set_auth_server_ip_address(conf.radius_ip_address)
		security_page.set_auth_shared_key_retype(conf.radius_shared_key,conf.radius_shared_key)
		security_page.setting_nas_ip_and_identifier(" "," ")
		security_page.click_rfc_3576_checkbox()
		security_page.save_auth_server()
		self.take_s2_snapshot()
		
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_authentication_server()
		security_page.delete_authentication_server_2()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		