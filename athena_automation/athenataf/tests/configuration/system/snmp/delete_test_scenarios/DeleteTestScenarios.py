import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DeleteTestScenarios(ConfigurationTest):
	'''
	Test class for System--->SNMP.
	'''
	def test_ath_11367_delete_the_created_snmp_values(self):
		path = self.config.config_vars
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_snmp_tab()
		self.take_s1_snapshot()
		system_page.click_new_snmp_button()
		system_page.set_snmp_value(path.snmp_name)
		system_page.click_new_snmpv3_button()
		system_page.set_snmpv3_user_value(path.snmpv3_user_name)
		system_page.set_snmp_user_password(path.snmp_user_auth_password1,path.snmp_user_auth_password1)
		system_page.set_snmp_user_privacy_password(path.snmp_user_privacy_password1,path.snmp_user_privacy_password1)
		system_page.click_save_snmpv3_user()
		system_page._save_settings()
		system_page.go_to_snmp_tab()
		system_page.click_new_snmp_trap_button()
		system_page.set_snmp_trap_ip_address(path.snmp_trap_valid_ip_address)
		system_page.set_snmp_trap_community_name(path.community_name)
		system_page.click_save_traps()
		system_page._save_settings()
		self.take_s2_snapshot()
		system_page.go_to_snmp_tab()
		system_page.delete_snmp_community_string_settings()
		system_page.delete_snmpv3_user_settings()
		system_page.delete_snmp_trap_settings()
		system_page._save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()