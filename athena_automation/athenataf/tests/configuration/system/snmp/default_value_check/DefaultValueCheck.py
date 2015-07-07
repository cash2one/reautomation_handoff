import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DefaultValueCheck(ConfigurationTest):
	'''
	Test class for System Snmp.
	'''
	sys_pg_obj = None
	def tearDown(self):
		'''
		Overrided method
		'''
		# raw_input('inside teardown')
		self.browser.refresh()
		DefaultValueCheck.sys_pg_obj.go_to_snmp_tab()
		DefaultValueCheck.sys_pg_obj.delete_snmpv3_user_settings()
		DefaultValueCheck.sys_pg_obj.delete_snmp_trap_settings()
		DefaultValueCheck.sys_pg_obj.delete_snmp_community_string_settings()
		# clean up code
		super(DefaultValueCheck, self).tearDown()
	
	def test_ath_11364_check_default_values_of_snmp(self):
		system_page = self.LeftPanel.go_to_system_page()
		DefaultValueCheck.sys_pg_obj = system_page
		system_page.go_to_snmp_tab()
		system_page.assert_empty_snmp_community_string_table()
		system_page.click_new_snmp_button()
		system_page.assert_empty_snmp_community_string()
		system_page.click_snmp_cancel_button()
		system_page.assert_empty_user_for_snmpv3_table()
		system_page.click_new_snmpv3_button()
		system_page.assert_snmpv3_deafault_name()
		system_page.assert_snmpv3_default_auth_protocol()
		system_page.assert_snmpv3_default_privacy_protocol()
		system_page.assert_snmpv3_default_password_values()
		system_page.click_snmpv3_cancel_button()
		system_page.assert_empty_snmp_traps_table()
		system_page.click_new_snmp_trap_button()
		system_page.assert_default_snmp_trap_ip_address()
		system_page.assert_default_version()
		system_page.assert_default_port()
		system_page.assert_default_snmp_inform()
		system_page.cancel_trap_settings()