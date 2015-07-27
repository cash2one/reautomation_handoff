import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase
from athenataf.lib.functionality.common.deviceverifier import DeviceVerifier
import time

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
        #device_management_page.search_device_using_mac_address()
        #device_management_page.change_device1_to_unassigned()
        self.logout()
        self.login(access_level = 'read_only')
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        #firmware_page.upgrade_firmware_using_custom_build_option(conf.version_type_value_2)
        firmware_page.upgrade_firmware_using_custom_build_option(conf.cbuild_version)
        firmware_page.asserting_upgrade_failure_error()
        
    def test_ath_9177_verify_read_write_user_has_no_permission_to_upgrade(self):
        conf = self.config.config_vars

        user_management_page=self.LeftPanel.go_to_user_management()
        user_management_page.delete_if_any_user_present()
        user_management_page.create_new_user(conf.email_read_write,conf.user_setting_group_value,conf.user_access_level_read_write)
        device_management_page = self.LeftPanel.go_to_device_management()
        #device_management_page.search_device_using_mac_laddress()
        #device_management_page.change_device1_to_unassigned()
        self.logout()
        self.login(access_level = 'read_write')
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.upgrade_firmware_using_custom_build_option(conf.version_firmware_3)
        firmware_page.asserting_upgrade_button()
        firmware_page.asserting_upgrade_button_disabled()

    def test_ath_9176_verify_admin_user_has_permission_to_upgrade_firmware(self):
        conf = self.config.config_vars
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        logger.debug("FirmwarePage : Clicking on device ")
        firmware_page.select_device.click()
        logger.debug("FirmwarePage : Clicking on Upgrade Firmware ")
        firmware_page.upgrade_button.click()
        logger.debug("FirmwarePage : Clicking on Manual option ")
        firmware_page.manual_upgrade.click()
        logger.debug("FirmwarePage : Selecting Type ")
        firmware_page.version_type.set(conf.version_type_value)
        time.sleep(5)
        firmware_page.firmware_version_text.set(conf.c_builb_image_version)
        time.sleep(5)
        logger.debug("FirmwarePage : Checks Firmware Upgrade button is not present or not ")
        firmware_page.browser.assert_element(firmware_page.post_upgrade, 'upgrade Button is not enable')        
        firmware_page.cancel_firmware.click()        