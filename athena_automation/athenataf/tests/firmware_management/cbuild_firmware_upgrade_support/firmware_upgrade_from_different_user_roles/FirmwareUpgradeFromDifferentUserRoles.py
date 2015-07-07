import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase

class FirmwareUpgradeFromDifferentUserRoles(AthenaGUITestCase):
	'''
	Test class for UI.
	'''
	
	def test_ath_9178_verify_read_only_user_has_no_permission_to_upgrade(self):
		conf = self.config.config_vars
		user_management_page=self.LeftPanel.go_to_user_management()
		user_management_page.delete_if_any_user_present()
		user_management_page.create_new_user(conf.email_read_only,conf.user_setting_group_value,conf.user_access_level_read_only)
		device_management_page = self.LeftPanel.go_to_device_management()
		device_management_page.search_device_using_mac_address()
		device_management_page.change_device1_to_unassigned()
		self.logout()
		self.login('read_only')
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		firmware_page.upgrade_firmware_using_custom_build_option(conf.firmware_version,"IAP_1")
		firmware_page.asserting_upgrade_button()
		
	def test_ath_9177_verify_read_write_user_has_no_permission_to_upgrade(self):
		conf = self.config.config_vars
		user_management_page=self.LeftPanel.go_to_user_management()
		user_management_page.delete_if_any_user_present()
		user_management_page.create_new_user(conf.email_read_only,conf.user_setting_group_value,conf.user_access_level_read_only)
		device_management_page = self.LeftPanel.go_to_device_management()
		device_management_page.search_device_using_mac_address()
		device_management_page.change_device1_to_unassigned()
		self.logout()
		self.login('read_write')
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		firmware_page.upgrade_firmware_using_custom_build_option(conf.firmware_version,"IAP_1")
		firmware_page.asserting_upgrade_button()

	def test_ath_9176_verify_admin_user_has_permission_to_upgrade_firmware(self):
		conf = self.config.config_vars
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		firmware_page.upgrade_firmware_using_manual_option(conf.version_type_value_2,conf.version_firmware_2)
		logger.debug("FirmwarePage : Checks Firmware Upgrade button is not present or not ")
		firmware_page.browser.assert_element(firmware_page.post_upgrade, 'upgrade Button is not enable')		