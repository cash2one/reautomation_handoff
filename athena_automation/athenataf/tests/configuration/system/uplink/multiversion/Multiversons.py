import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Multiversons(ConfigurationTest):
	'''
	Test class for System EditTestScenarios module.
	'''

	def test_ath_11356_multiversion_check_for_uplink_parameters(self):
		conf=self.config.config_vars
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.click_uplink()
		system_page.checking_non_default_value_for_3g_4g('None','None',"abc","def","ghi","jkl","mno","pqrs","tuv","CHAP","wxyz","abcde")
		system_page._save_settings()
		system_page.click_uplink()
		system_page.pppoe_service_name(conf.pppoe_service_name)
		system_page.set_pp_chap_secret1(conf.re_chap_secret)
		system_page.set_pp_chap_secret2(conf.re_chap_secret)
		system_page.set_pp_user(conf.Cell_Usb_User)
		system_page.set_pp_password(conf.chap_secret)
		system_page.set_pp_retype_password(conf.chap_secret)
		system_page.pp_local_interafce.set('None')
		system_page._save_settings()
		self.take_s2_snapshot()
		system_page.click_uplink()
		system_page.set_default_uplink_3g_4g_setting()
		system_page.set_default_uplink_pppoe_setting()
		system_page._save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()