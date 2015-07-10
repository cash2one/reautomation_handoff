import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase

class NegativeTesting(AthenaGUITestCase):
    '''
    Test class for Negative Testing.
    '''
    
    def test_ath_4414_cant_initiate_another_upgrade_when_upgrading(self):
        conf=self.config.config_vars
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.select_vc_for_upgrade("IAP_1")
        firmware_page.clicking_on_upgrade_firmware()
        firmware_page.setting_firmware_upgrade_manual_option(conf.version_type_value_2,conf.firmware_upgrade_version)
        firmware_page.click_post_firmware_upgrade()
        import time
        time.sleep(5)
        firmware_page.select_vc_for_upgrade("IAP_1")
        firmware_page.assert_device_selector_disabled()

        firmware_page.buy_time()
        DeviceLibrary.getPrompt("IAP_1")
        DeviceLibrary.connect_device_to_server("IAP_1")
        firmware_page.select_vc_for_upgrade("IAP_1")
        firmware_page.clicking_on_upgrade_firmware()
        firmware_page.setting_firmware_upgrade_manual_option(option=conf.version_type_value_2,version=conf.firmware_base_version)
        firmware_page.click_post_firmware_upgrade()
        firmware_page.buy_time()
        DeviceLibrary.getPrompt("IAP_1")
        DeviceLibrary.connect_device_to_server("IAP_1")
        
        
    def test_ath_6758_upgrade_firmware_without_selecting_vc(self):
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.upgrade_button.click()
        firmware_page.assert_no_vc_error_message()
        firmware_page.ok_button.click()
        
    def _view_monitoring_pages(self):
        self.LeftPanel.go_to_monitoring_page()
        self.LeftPanel.go_to_monitoring_access_points()
        self.LeftPanel.go_to_monitoring_clients()
        self.LeftPanel.go_to_monitoring_wids()
        self.LeftPanel.go_to_monitoring_event_log()
        self.LeftPanel. go_to_monitoring_notifications()

    def test_ath_6836_check_ui_stability_after_page_reload(self):
        self._view_monitoring_pages()
        self.browser.refresh()
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.isPageLoaded()    
        self.logout_and_login_back()
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.isPageLoaded()  
    
    def test_ath_8343_downgrade_iap_224_225_to_34_and_blow(self):
        conf = self.config.config_vars
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.upgrade_firmware_using_custom_build_option(conf.version_firmware,"IAP_1")
        firmware_page.asserting_version_unavailable_img()
    
    def test_ath_4426_downgrade_iap_224_225_to_34_and_blow(self):
        conf = self.config.config_vars
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.upgrade_firmware_using_custom_build_option(conf.invalid_version_firmware,"IAP_1")
        firmware_page.asserting_version_unavailable_img()
    
    def test_ath_8344_downgrade_iap_224_225_to_34_and_blow(self):
        conf = self.config.config_vars
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.upgrade_firmware_using_custom_build_option(conf.version_firmware,"IAP_1")
        firmware_page.asserting_version_unavailable_img()
        