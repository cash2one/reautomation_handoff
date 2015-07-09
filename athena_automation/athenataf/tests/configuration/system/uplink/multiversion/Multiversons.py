import logging
logger = logging.getLogger('athenataf')
import time

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest
import os
import pdb

class Multiversons(ConfigurationTest):
	'''
	Test class for System EditTestScenarios module.
	'''

	def test_ath_11356_multiversion_check_for_uplink_parameters(self):
		'''
			Snapshot command is remaining for multiple devices
		'''
		conf=self.config.config_vars
		system_page = self.LeftPanel.go_to_system_page()
		os.environ['device'] = "IAP_1"
		self.take_s1_snapshot()
		os.environ['device'] = "IAP_2"
		self.take_s1_snapshot()
		system_page.click_uplink()
		system_page.checking_non_default_value_for_3g_4g(u_type="abc",c_4g_type="def",u_dev="ghi",u_tty="jkl",u_init="mno",u_dial="pqrs",switch="tuv",auth="CHAP",user="wxyz",pwd="abcde")
		system_page._save_settings()
		time.sleep(5)
		system_page.click_uplink()
		system_page.pppoe_service_name(conf.pppoe_service_name)
		system_page.set_pp_chap_secret1(conf.re_chap_secret)
		system_page.set_pp_chap_secret2(conf.re_chap_secret)
		system_page.set_pp_user(conf.Cell_Usb_User)
		system_page.set_pp_password(conf.chap_secret)
		system_page.page_down()
		self.browser.key_press(u'\ue00f')
		system_page.set_pp_retype_password(conf.chap_secret)
		system_page.pp_local_interafce.set('None')
		system_page._save_settings()
		os.environ['device'] = "IAP_1"
		self.take_s2_snapshot()
		os.environ['device'] = "IAP_2"
		self.take_s2_snapshot()
		time.sleep(5)
		system_page.click_uplink()
		system_page.set_default_uplink_3g_4g_setting()
		system_page.set_default_uplink_pppoe_setting()
		system_page._save_settings()
		os.environ['device'] = "IAP_1"
		self.take_s3_snapshot()
		os.environ['device'] = "IAP_2"
		self.take_s3_snapshot()
		os.environ['device'] = "IAP_1"
		self.assert_s1_s2_diff(0)
		os.environ['device'] = "IAP_2"
		self.assert_s1_s2_diff(0)
		os.environ['device'] = "IAP_1"
		self.assert_s1_s3_diff()
		os.environ['device'] = "IAP_2"
		self.assert_s1_s3_diff()