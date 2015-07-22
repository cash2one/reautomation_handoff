import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase

class CBuildAttributesOfCustomBuildTextbox(AthenaGUITestCase):
	'''
	Test class for UI.
	'''

	def test_ath_9179_verify_attributes_of_textbox_which_is_used_to_enter_custom_build_number(self):
		conf = self.config.config_vars

		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		firmware_page.upgrade_firmware_using_custom_build_option(conf.special_char_version)

		firmware_page.asserting_version_error_message()
		# firmware_page.cancel_firmware_upgrade()
		firmware_page.upgrade_firmware_using_custom_build_option(conf.hrs8)
		firmware_page.asserting_version_error_message()
		#firmware_page.click_cancel_icon()
		
	def test_ath_9173_cbuild_images_sync_with_athena(self):
		'''
			Required Firmware version for custom build option
		'''
		conf = self.config.config_vars
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		firmware_page.upgrade_firmware_using_custom_build_option(conf.c_builb_image_version,"IAP_1")
		firmware_page.asserting_upgrade_button()
		
		firmware_page.click_switch_tab()
		firmware_page.select_switch_for_upgrade("Switch_1")
		firmware_page.clicking_on_upgrade_firmware()
		firmware_page.upgrade_firmware_using_custom_build_option_for_switch(conf.switch_version_2,"Switch_1")
		firmware_page.asserting_upgrade_button()