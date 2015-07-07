from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Edit(ConfigurationTest):
	'''
	Test class for System Snmp.
	'''
	sys_pg_obj = None
	
	def tearDown(self):
		'''
		Overrided method
		'''
		self.browser.refresh()
		Edit.sys_pg_obj.go_to_snmp_tab()
		Edit.sys_pg_obj.delete_snmpv3_user_settings()
		Edit.sys_pg_obj.delete_snmp_trap_settings()
		Edit.sys_pg_obj.delete_snmp_community_string_settings()
		Edit.sys_pg_obj._save_settings()
		# clean up code
		super(Edit,self).tearDown()
	
	def test_ath_11958_check_default_values_of_snmp(self):
		system_page = self.LeftPanel.go_to_system_page()
		Edit.sys_pg_obj = system_page
		system_page.go_to_snmp_tab()
		system_page.delete_snmpv3_user_settings()
		system_page.delete_snmp_trap_settings()
		system_page.delete_snmp_community_string_settings()
		system_page._save_settings()
		conf = self.config.config_vars
		self.take_s1_snapshot()
		# system_page.go_to_snmp_tab()
		system_page.click_new_snmp_button()
		system_page.set_snmp_value(conf.snmp_name)
		system_page.click_new_snmpv3_button()
		system_page.set_snmpv3_user_value(conf.community_name)
		system_page.set_snmp_user_password(conf.snmp_user_auth_password1,conf.snmp_user_auth_password1)
		system_page.set_snmp_user_privacy_password(conf.snmp_user_auth_password1,conf.snmp_user_auth_password1)
		system_page.set_auth_protocol(conf.default_smpv3_auth_protocol)
		system_page.click_save_snmpv3_user()		
		system_page._save_settings()
		system_page.go_to_snmp_tab()
		system_page.edit_community_string()
		system_page.set_snmp_value(conf.edit_snmp_name)
		system_page.edit_snmpv3_user_settings()
		system_page.set_snmpv3_user_value(conf.community_name)
		system_page.set_snmp_user_password(conf.snmp_user_auth_re_password1,conf.snmp_user_auth_re_password1)
		system_page.set_snmp_user_privacy_password(conf.snmp_user_auth_re_password1,conf.snmp_user_auth_re_password1)
		system_page.set_auth_protocol(conf.auth_protocol_MD5)
		system_page.click_save_snmpv3_user()		
		system_page._save_settings()
		system_page.go_to_snmp_tab()
		system_page.click_new_snmp_trap_button()
		system_page.set_snmp_trap_ip_address(conf.valid_Proxy_exception_value2)
		system_page.set_snmp_trap_community_name(conf.community_name)
		system_page.click_save_traps()
		system_page._save_settings()
		system_page.go_to_snmp_tab()
		system_page.edit_snmpv_traps_settings()
		system_page.click_new_snmp_trap_button()
		system_page.set_snmp_trap_ip_address(conf.trap_ip)
		system_page.set_snmp_trap_community_name(conf.comm_name)
		system_page.set_version(conf.version_v1)
		system_page.set_snmp_trap_port_value(conf.port_65534)
		# system_page.set_inform(conf.inform_no)
		system_page.click_save_traps()
		system_page._save_settings()
		self.take_s2_snapshot()
		system_page.go_to_snmp_tab()
		system_page.delete_snmpv3_user_settings()
		system_page.delete_snmp_trap_settings()
		system_page.delete_snmp_community_string_settings()
		system_page._save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()				