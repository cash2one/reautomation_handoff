import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class FieldValidation(ConfigurationTest):
	'''
	Test class for System--->SNMP.
	'''
	sys_pg_obj = None
	def tearDown(self):
		'''
		Overrided method
		'''
		self.browser.refresh()
		# raw_input('inside teardown')
		FieldValidation.sys_pg_obj.go_to_snmp_tab()
		FieldValidation.sys_pg_obj.delete_snmpv3_user_settings()
		FieldValidation.sys_pg_obj.delete_snmp_trap_settings()
		FieldValidation.sys_pg_obj.delete_snmp_community_string_settings()
		# clean up code
		super(FieldValidation, self).tearDown()

	def test_ath_11368_field_validation_in_SNMP(self):
		
		#TestCase contains bug
		
		path = self.config.config_vars
		system_page = self.LeftPanel.go_to_system_page()
		FieldValidation.sys_pg_obj = system_page
		system_page.go_to_snmp_tab()
		system_page.click_new_snmp_button()
		system_page.set_snmp_value(path.invalid_snmp_string_33)
		
		#make changes after the resolving the bug
		
		system_page.assert_invalid_snmp_string_error()
		system_page.click_snmp_cancel_button()
		system_page.click_new_snmpv3_button()
		system_page.set_snmpv3_user_value(path.snmpv3_user_name)
		system_page.click_save_snmpv3_user()
		system_page.set_snmp_user_password(path.snmp_user_auth_password_empty,path.snmp_user_auth_password_empty)
		system_page.set_snmp_user_privacy_password(path.snmp_user_auth_password_empty,path.snmp_user_auth_password_empty)
		system_page.click_save_snmpv3_user()
		system_page.assert_snmpv3_empty_password_error()
		system_page.set_snmp_user_password(path.snmp_user_auth_password1,path.snmp_user_auth_re_password1)
		system_page.set_snmp_user_privacy_password(path.snmp_user_privacy_password1,path.snmp_user_privacy_re_password1)
		system_page.click_save_snmpv3_user()
		system_page.assert_snmpv3_password_mismatch_error()
		system_page.click_snmpv3_cancel_button()
		system_page.click_new_snmp_trap_button()
		system_page.assert_snmp_trap_invalid_ip()
		system_page.set_snmp_trap_ip_address(path.snmp_trap_valid_ip_address)
		system_page.set_snmp_trap_community_name(path.community_name)
		
		#make changes after the resolving the bug
		system_page.assert_snmp_trap_invalid_port_value()
		
		
		