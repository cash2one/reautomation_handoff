import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Multiversion(ConfigurationTest):
	'''
	Test class for Multiversion.
	'''

	def test_ath_11080_slb_mode(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_group1()
		rf_page.check_multiversion_text_availablility(rf_page.slb_mode_multiversion)
		inner_left_panel.select_group2()
		rf_page.assert_slb_mode_value1()
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_all_group()
		rf_page.assert_slb_mode_value1()
		rf_page.set_rf_arm_client_control_slb_mode(self.config.config_vars.slb_mode_value_3rd)
		logger.debug('RfPage : Clicking on save settings')
		rf_page.save_settings.click()
		self.take_s2_snapshot()
		rf_page.set_rf_arm_client_control_slb_mode(None)
		logger.debug('RfPage : Clicking on save settings')
		rf_page.save_settings.click()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
		
		
	def test_ath_11081_mhz_support(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_group1()
		rf_page.check_multiversion_text_availablility(rf_page.eightysupport_multiversion)
		inner_left_panel.select_group2()
		rf_page.assert_80_mhz_options()
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_all_group()
		rf_page.assert_80_mhz_options()
		rf_page.set_rf_arm_access_point_control_mhz_support(conf.new_mhz_support_value)
		logger.debug('RfPage : Clicking on save settings')
		rf_page.save_settings.click()
		self.take_s2_snapshot()
		rf_page.set_rf_arm_access_point_control_mhz_support(None)
		logger.debug('RfPage : Clicking on save settings')
		rf_page.save_settings.click()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
		
	def test_ath_11082_client_match(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_group1()
		rf_page.check_multiversion_text_availablility(rf_page.client_match_multiversion)
		inner_left_panel.select_group2()
		rf_page.assert_client_aware_options()
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_all_group()
		rf_page.assert_client_aware_options()
		rf_page.set_rf_arm_client_control_client_match(self.config.config_vars.client_match_enabled)
		logger.debug('RfPage : Clicking on save settings')
		rf_page.save_settings.click()
		self.take_s2_snapshot()
		rf_page.set_rf_arm_client_control_slb_mode(None)
		logger.debug('RfPage : Clicking on save settings')
		rf_page.save_settings.click()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		