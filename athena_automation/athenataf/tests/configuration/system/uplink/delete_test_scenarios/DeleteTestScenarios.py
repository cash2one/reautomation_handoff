import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DeleteTestScenarios(ConfigurationTest):
	'''
		Test class for Delete Test Scenarios under System module.
	'''
	
	def test_ath_11351_delete_the_created_uplink_parameters(self):
		conf = self.config.config_vars
		system_page = self.LeftPanel.go_to_system_page()
		system_page.click_uplink()
		self.take_s1_snapshot()
		system_page.checking_non_default_value_for_3g_4g(conf.Modem_Country,conf.modem_isp_value,None,None,None,None,None,None,None,None,None,None)
		system_page.checking_non_default_value_for_wifi_field(conf.wifi_name1,conf.preferred_band_new_value,None,None,conf.area_code_2)
		system_page.checking_non_default_values_for_management(conf.enforce_uplink1,conf.pre_emption1,conf.timeout_value,conf.manage_internet_failover_value)
		system_page.checking_non_default_values_for_pppoe(conf.pppoe_service_name,conf.re_chap_secret,conf.re_chap_secret,conf.user_name_value,conf.password_value,conf.password_value)
		system_page._save_settings()
		system_page.click_uplink()
		system_page.set_default_uplink_3g_4g_setting()
		system_page.set_default_uplink_wi_fi_setting()
		system_page.set_default_uplink_management_settings()
		system_page.set_default_uplink_pppoe_setting()
		system_page._save_settings()
		system_page.click_uplink()
		system_page.checking_non_default_value_for_3g_4g(None,None,"abc","def","ghi","jkl","mno","pqrs","tuv","CHAP","wxyz","abcde")
		system_page.checking_non_default_value_for_wifi_field(conf.wifi_name1,conf.prefered_band_2_4ghz,conf.wifi_management1,conf.wifi_passphrase_format2,conf.hexadecimal_64_char)
		system_page.checking_non_default_values_for_management(conf.enforce_uplink2,conf.pre_emption,conf.timeout_3600,conf.internet_failover)
		system_page._save_settings()
		self.take_s2_snapshot()		
		system_page.click_uplink()
		system_page.set_default_uplink_3g_4g_setting()
		system_page.set_default_uplink_wi_fi_setting()
		system_page.set_default_uplink_management_settings()
		system_page.set_default_uplink_pppoe_setting()
		system_page._save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()