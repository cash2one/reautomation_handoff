import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class EditTestScenarios(ConfigurationTest):
	'''
	Test class for System EditTestScenarios module.
	'''

	def test_ath_11948_edit_the_createduplink_parameters_management(self):
		conf=self.config.config_vars
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.click_uplink()
		system_page.set_management_enforce_uplink(conf.enforce_uplink2)
		system_page.set_management_Pre_emption(False)
		system_page.set_management_vpn_failover_timeout(conf.management_failover_value)
		system_page.set_management_internet_failover(False)
		system_page._save_settings()
		system_page.click_uplink()
		system_page.pppoe_service_name(conf.pppoe_service_name)
		system_page.set_pp_chap_secret1(conf.chap_secret)
		system_page.set_pp_chap_secret2(conf.chap_secret)
		system_page.set_pp_user(conf.Cell_Usb_User)
		system_page.set_pp_password(conf.chap_secret)
		system_page.set_pp_retype_password(conf.chap_secret)
		system_page._save_settings()

		system_page.click_uplink()
		system_page.set_management_enforce_uplink(conf.enforce_uplink3)
		system_page.set_management_vpn_failover_timeout(conf.management_failover_value1)
		system_page.set_uplink_priority_list_wifi_first()
		system_page.set_uplink_priority_list_Eth0_second()
		system_page._save_settings()

		system_page.click_uplink()
		system_page.pppoe_service_name(conf.pppoe_service_new_name)
		system_page.set_pp_chap_secret1(conf.chap_secret_passwrd)
		system_page.set_pp_chap_secret2(conf.chap_secret_passwrd)
		system_page.set_pp_user(conf.Cell_Usb_User)
		system_page.set_pp_password(conf.chap_secret)
		system_page.set_pp_retype_password(conf.chap_secret)
		system_page._save_settings()

		self.take_s2_snapshot()
		system_page.click_uplink()
		system_page.set_management_enforce_uplink(False)
		system_page.set_management_Pre_emption(False)
		system_page.set_management_vpn_failover_timeout(None)
		system_page.set_management_internet_failover(False)
		system_page.pppoe_service_name(None)
		system_page.set_pp_chap_secret1(None)
		system_page.set_pp_chap_secret2(None)
		system_page.set_pp_password(None)
		system_page.set_pp_retype_password(None)
		system_page.set_default_uplink_priority_list()
		system_page._save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_11947_edit_the_created_uplink_parameters_3G_4G_and_wifi(self):
		conf = self.config.config_vars
		system_page = self.LeftPanel.go_to_system_page()
		system_page.click_uplink()
		self.take_s1_snapshot()
		system_page.checking_non_default_value_for_3g_4g(None,None,"abc","def","ghi","jkl","mno","pqrs","tuv","CHAP","wxyz","abcde")
		system_page._save_settings()
		system_page.click_uplink()		
		system_page.checking_non_default_value_for_wifi_field(conf.wifi_name1,conf.prefered_band_2_4ghz,conf.wifi_management1,conf.wifi_passphrase_format2,conf.hexadecimal_64_char)
		system_page._save_settings()
		system_page.click_uplink()
		system_page.checking_non_default_value_for_3g_4g(None,None,"abcdef","defghi","ghijkl","jklmon","mnopqrs","pqrstuv","tuvwxyz","CHAP","wxyzabc","defghijkl")
		system_page.checking_non_default_value_for_wifi_field("Myguest123",conf.preferred_band_new_value,conf.wifi_management1,conf.wifi_passphrase_format1,"1234567890")
		system_page._save_settings()
		self.take_s2_snapshot()
		system_page.click_uplink()
		system_page.set_default_uplink_3g_4g_setting()
		system_page.set_default_uplink_wi_fi_setting()
		system_page._save_settings()		
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()