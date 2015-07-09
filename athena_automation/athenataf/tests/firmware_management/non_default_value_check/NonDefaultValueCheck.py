import logging
logger = logging.getLogger('athenataf')
import time

from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase
from athenataf.lib.functionality.common import DeviceLibrary

class NonDefaultValueCheck(AthenaGUITestCase):
    '''
    Test class for Firmware Management Non DefaultValueCheck.
    '''
    
    def test_ath_11846_firmware_upgrade_in_vc_automatic(self):
        conf = self.config.config_vars
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        latest_version = firmware_page.get_latest_recommended_version()
        firmware_page.select_vc_for_upgrade('IAP_1')
        firmware_page.upgrade_button.click()
        # firmware_page.select_later_date_radio()
        # firmware_page.set_upgrade_after_ten_mins()
        firmware_page.click_post_firmware_upgrade()
        time.sleep(1000)
        # self.buy_time()
        DeviceLibrary.getPrompt("IAP_1")
        DeviceLibrary.connect_device_to_server('IAP_1')
        # self.buy_time()
        firmware_page.assert_firmware_version('IAP_1',latest_version)
        
    def test_ath_11941_firmware_upgrade_in_vc_manual(self):
        conf = self.config.config_vars
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.select_vc_for_upgrade('IAP_1')
        firmware_page.clicking_on_upgrade_firmware()
        firmware_page.setting_firmware_upgrade_manual_option(conf.version_type_value_2,conf.firmware_upgrade_version)
        firmware_page.click_post_firmware_upgrade()
        time.sleep(1000)
        # self.buy_time()
        DeviceLibrary.getPrompt("IAP_1")
        DeviceLibrary.connect_device_to_server('IAP_1')
        # self.buy_time()
        firmware_page.assert_firmware_version('IAP_1',conf.firmware_upgrade_version)