import logging
logger = logging.getLogger('athenataf')


from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DeleteTestScenario(ConfigurationTest):
	'''
	Test class for network configuration Security Authentication Server DeleteTestScenario.
	'''

	def test_ath_13337_delete_the_created_coa_only_server(self):
		conf = self.config.config_vars
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_coa_servers()
		self.take_s1_snapshot()
		security_page.create_coa_servers(conf.CoAServer, conf.coa_server_ip, conf.alpha_numeric)
		security_page.create_coa_servers(conf.CoAServer1, conf.coa_server_ip1, conf.alpha_numeric, conf.auth_port_valid)
		self.take_s2_snapshot()
		security_page.delete_coa_servers()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_13335_delete_the_created_ldap_server(self):
		conf = self.config.config_vars
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_ldap_servers()
		self.take_s1_snapshot()
		security_page= self.LeftPanel.go_to_security()
		security_page.create_new_server()
		security_page.ldap_radio_button.click()
		security_page.create_new_ldap_auth_server(name = conf.server_name,ip = conf.valid_auth_server_ip,port = None,admin = conf.admin_dn_name,passphrase = conf.ldap_pass_phrase,retypepass = conf.ldap_pass_phrase,base = conf.base_dn,filter = None,key = None,timeout = None,retry = None)
		security_page.ldap_radio_button.click()
		security_page.create_new_ldap_auth_server(name = conf.server_name1,ip = conf.auth_radius_ip1,port = conf.invalid_radius_server_acc_port_65535,admin = conf.admin_dn,passphrase = conf.ldap_pass_phrase,retypepass = conf.ldap_pass_phrase,base = conf.base_dn_name,filter = None,key = conf.key_attribute,timeout = conf.timeout,retry = conf.retry)
		self.take_s2_snapshot()
		security_page.delete_ldap_servers()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_13336_check_default_value_in_authentication_server(self):
		conf = self.config.config_vars
		security_page = self.LeftPanel.go_to_security()
		if security_page.testRole_delete:
			logger.debug('SecurityPage : Clicking on Delete button')
			security_page.testRole_delete.click()
		if security_page.tac123_delete:
			logger.debug('SecurityPage : Clicking on Delete button')
			security_page.tac123_delete.click()
		self.take_s1_snapshot()
		logger.debug('SecurityPage : Clicking on New button')
		security_page.create_auth_server.click()
		logger.debug('SecurityPage : Clicking on TACACS radio button')
		security_page.tacacs_radio.click()
		security_page.create_new_tacacs_auth_server(name = conf.Role_Name, key = conf.time_out_invalid, retype = conf.time_out_invalid, port = None, timeout = None, ip = conf.auth_server_ip_valid, retry = None)
		security_page.create_auth_server.click()
		logger.debug('SecurityPage : Clicking on TACACS radio button')
		security_page.tacacs_radio.click()
		security_page.create_new_tacacs_auth_server(name = conf.tacacs_name, key = conf.time_out_invalid, retype = conf.time_out_invalid, port = None, timeout = None, ip = conf.auth_server_ip_valid, retry = None)
		logger.debug('SecurityPage : Clicking on edit button')
		security_page.tac123_edit.click()
		security_page.create_new_tacacs_auth_server(name = None, key = None, retype = None, port = conf.auth_port_valid, timeout = conf.dynm_blklst_failure_time3, ip = None, retry = conf.count1)
		self.take_s2_snapshot()
		if security_page.testRole_delete:
			logger.debug('SecurityPage : Clicking on Delete button')
			security_page.testRole_delete.click()
		if security_page.tac123_delete:
			logger.debug('SecurityPage : Clicking on Delete button')
			security_page.tac123_delete.click()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
				