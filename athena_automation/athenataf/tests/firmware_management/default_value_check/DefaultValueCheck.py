import logging
logger = logging.getLogger('athenataf')
import time

from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase

class DefaultValueCheck(AthenaGUITestCase):
	'''
	Test class for Firmware Management DefaultValueCheck.
	'''
	
	def test_ath_11844_check_the_default_values_in_firmware_page(self):
		conf=self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		self.take_s1_snapshot()
		if	inner_left_panel.assert_mynew_group():
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_empty_mynew_group()
			manage_group_page.click_manage_group_close_button()
		inner_left_panel.group_close_icon.click()
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		firmware_page.check_firmware_page_default_value()
		inner_left_panel = self.TopPanel.click_slider_icon()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_multiple_empty_groups(conf.mynew)
		inner_left_panel.group_close_icon.click()
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		firmware_page.check_firmware_page_default_value()
		firmware_page.upgrade_button.click()
		firmware_page.assert_no_vc_error_message()
		firmware_page.ok_button.click()
		self.take_s2_snapshot()
		inner_left_panel = self.TopPanel.click_slider_icon()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.delete_empty_mynew_group()
		self.browser.refresh()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_9170_verify_customer_build_drop_menu_under_tracks(self):
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		firmware_page.verify_custom_build_drop_down_menu("IAP_1")
		
	def test_ath_9171_verification_of_cbuild_image(self):
		'''
			Required Firmware version for custom build option 
		'''
		conf = self.config.config_vars
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		firmware_page.verify_custom_build_drop_down_menu("IAP_1")
		firmware_page.cancel_firmware.click()
		self.browser.refresh()
		firmware_page.upgrade_firmware_using_custom_build_option(conf.c_builb_image_version,"IAP_1")
		firmware_page.asserting_upgrade_button()
		
		firmware_page.click_switch_tab()
		firmware_page.select_switch_for_upgrade("Switch_1")
		firmware_page.clicking_on_upgrade_firmware()
		firmware_page.upgrade_firmware_using_custom_build_option_for_switch(conf.switch_version_2,"Switch_1")
		firmware_page.asserting_upgrade_button()
	
	def test_ath_11846_firmware_upgrade_in_vc_automatic(self):
		conf = self.config.config_vars
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		firmware_page.select_first_vc()
		firmware_page.clicking_on_upgrade_firmware()
		firmware_page.upgrade_firmware()
		time.sleep(600)
		self.connect_device()
		self.browser.refresh()
		firmware_page.asserting_device_upgrade_status()
		
	def test_ath_11941_firmware_upgrade_in_vc_manual(self):
		conf = self.config.config_vars
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		firmware_page.upgrade_firmware_using_manual_option(conf.version_type_value_2,conf.version_firmware_2)
		firmware_page.upgrade_firmware()
		time.sleep(600)
		self.connect_device()
		self.browser.refresh()
		firmware_page.asserting_device_upgrade_status()
		
