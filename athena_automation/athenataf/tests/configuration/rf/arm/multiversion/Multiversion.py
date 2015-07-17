import logging
logger = logging.getLogger('athenataf')
import time
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Multiversion(ConfigurationTest):
	'''
	Test class for Multiversion.
	'''

	def test_ath_11080_slb_mode(self):
		'''
		test case is executed on 4.1.1.7 and 4.1.2.3
		IAP_1 : 4.1.1.7
		IAP_2 : 4.1.2.3
		suggested by Michael
		'''
		innerleftpanel = self.TopPanel.click_slider_icon()
		innerleftpanel.click_on_expand_group_icon(innerleftpanel.expand_group_icon)
		innerleftpanel.select_vc('IAP_1')
		time.sleep(3)
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.assert_slb_mode_value1()
		rf_page.assert_slb_mode_multiversion()
		innerleftpanel = self.TopPanel.click_slider_icon()
		innerleftpanel.select_default_group()
		rf_page.assert_slb_mode_value1()
		rf_page.assert_slb_mode_multiversion()
		rf_page.set_rf_arm_client_control_slb_mode(self.config.config_vars.slb_mode_value_3rd)
		time.sleep(5)
		logger.debug('RfPage : Clicking on save settings')
		rf_page.save_settings.click()
		time.sleep(80)
		rf_page.assert_arm_configuration('IAP_1','channel+radio based')
		time.sleep(10)
		rf_page.assert_arm_configuration('IAP_2','channel+radio based')
		rf_page.set_rf_arm_client_control_slb_mode(None)
		logger.debug('RfPage : Clicking on save settings')
		rf_page.save_settings.click()
		
		
		
	def test_ath_11081_mhz_support(self):
		'''
		test case is executed on 4.1.1.7 and 4.1.2.3
		IAP_1 : 4.1.1.7
		IAP_2 : 4.1.2.3
		suggested by Michael
		'''
		innerleftpanel = self.TopPanel.click_slider_icon()
		innerleftpanel.click_on_expand_group_icon(innerleftpanel.expand_group_icon)
		innerleftpanel.select_vc('IAP_1')
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.check_multiversion_text_availablility(rf_page.eightysupport_multiversion,False)
		innerleftpanel = self.TopPanel.click_slider_icon()
		innerleftpanel.select_default_group()
		rf_page.check_multiversion_text_availablility(rf_page.eightysupport_multiversion,False)
		rf_page.set_rf_arm_access_point_control_mhz_support(self.config.config_vars.new_mhz_support_value)
		time.sleep(5)
		logger.debug('RfPage : Clicking on save settings')
		rf_page.save_settings.click()
		time.sleep(90)
		rf_page.assert_arm_configuration('IAP_1','80Mhz Support            :enable')
		time.sleep(10)
		rf_page.assert_arm_configuration('IAP_2','80Mhz Support            :enable')
		rf_page.set_rf_arm_access_point_control_mhz_support(None)
		logger.debug('RfPage : Clicking on save settings')
		time.sleep(5)
		rf_page.save_settings.click()
		
		
	def test_ath_11082_client_match(self):
		'''
		test case is executed on 4.1.1.7 and 4.1.2.3
		IAP_1 : 4.1.1.7
		IAP_2 : 4.1.2.3
		suggested by Michael
		'''
		innerleftpanel = self.TopPanel.click_slider_icon()
		innerleftpanel.click_on_expand_group_icon(innerleftpanel.expand_group_icon)
		innerleftpanel.select_vc('IAP_1')
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.check_multiversion_text_availablility(rf_page.eightysupport_multiversion,False)
		innerleftpanel = self.TopPanel.click_slider_icon()
		innerleftpanel.select_default_group()
		rf_page.assert_client_aware_options()
		rf_page.set_rf_arm_client_control_client_match(self.config.config_vars.client_match_enabled)
		logger.debug('RfPage : Clicking on save settings')
		time.sleep(5)
		rf_page.save_settings.click()
		time.sleep(100)
		rf_page.assert_arm_configuration('IAP_2','Client Match             :enable')
		time.sleep(20)
		rf_page.assert_arm_configuration('IAP_1','Client Match             :enable')
		rf_page.set_rf_arm_client_control_slb_mode(None)
		logger.debug('RfPage : Clicking on save settings')
		rf_page.save_settings.click()
