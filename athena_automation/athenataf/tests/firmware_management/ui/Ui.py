import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase

class Ui(AthenaGUITestCase):
	'''
	Test class for UI.
	'''
	
	def test_ath_4402_check_the_ui_element(self):
		conf=self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		self.take_s1_snapshot()
		if  inner_left_panel.assert_mygroup_without_vc_present():
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_group1()
		if inner_left_panel.assert_mygroup_with_vc_present():
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.move_virtual_controller_group1()
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_group1()
		self.take_s1_snapshot()			
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_group_with_vc1('group1')
		inner_left_panel.select_group(inner_left_panel.group_1)
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		firmware_page.check_firmware_page_default_value1()
		firmware_page.assert_aps_over_text_availability()
		logger.debug("FirmwarePage : Asserting Latest Version Number text.  ")
		self.browser.assert_element(firmware_page.latest_version_number_text, 'Latest version number text not found. ')
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_device()
		logger.debug("FirmwarePage : Asserting VC in VC level firmware page.  ")
		self.browser.assert_element(firmware_page.aps_box, 'VC in firmaware page not found. ')
		self.TopPanel.go_to_allgroups()
		logger.debug("FirmwarePage : Asserting VC in VC level firmware page.  ")
		self.browser.assert_element(firmware_page.aps_box, 'VC in firmaware page not found. ')
		self.take_s2_snapshot()
		if  inner_left_panel.assert_mygroup_without_vc_present():
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_group1()
			manage_group_page.click_manage_group_close_button()
		if inner_left_panel.assert_mygroup_with_vc_present():
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.move_virtual_controller_group1()
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_group1()
		self.TopPanel.go_to_allgroups()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()