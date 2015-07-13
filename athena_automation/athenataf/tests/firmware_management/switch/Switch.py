import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.SwitchConfigurationTest import SwitchConfigurationTest
import time
from athenataf.lib.functionality.common import DeviceLibrary

class Switch(SwitchConfigurationTest):
    '''
    Test class for switch configuration->ports.
    '''

    def test_ath_9082_verify_the_switch_connectivity_with_athena_and_after_manually_upgrading_the_switch(self):
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.upgrade_firmware_switch()
    
    def test_ath_6490_verify_all_ui_elements_on_the_upgrade_firmware_page(self):
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.click_switches()
        firmware_page.verify__ui_elements_on_the_upgrade_firmware_page()
        
    def test_ath_6518_Parallel_upgrade_of_switches_and_iaps(self):
        conf = self.config.config_vars
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.click_switches()
        firmware_page.firmware_upgrade( switch_vc='switch', Manual=True, option=conf.version_type_value_2,version=conf.version_firmware_2)
        firmware_page.assert_upgrading_status()
        firmware_page.click_on_virtual_controller_tab()
        firmware_page.firmware_upgrade( switch_vc='vc', automatic=True, option=conf.version_type_value_2,version=conf.version_firmware_2)
        firmware_page.click_switches()
        firmware_page.asserting_device_upgraded_successful()
        
    def test_ath_6519_Parallel_upgrading_firmware_on_a_switch_in_upgrading_state_fails(self):
        conf = self.config.config_vars
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.click_switches()
        firmware_page.firmware_upgrade( switch_vc='switch', Manual=True, option=conf.version_type_value_2,version=conf.version_firmware_2)
        '''
        While Switch is upgrading we can't select the switch
        '''
        firmware_page.firmware_upgrade( switch_vc='switch', Manual=True, option=conf.version_type_value_2,version=conf.version_firmware_2)
        
    def test_ath_6494_verify_the_switch_connectivity_with_athena_and_after_manually_upgrading_the_switch(self):
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        self.take_s1_snapshot('show_switchinfo')
        firmware_page.click_switches()
        firmware_page.select_all_switches()
        firmware_page.clicking_on_upgrade_firmware()
        firmware_page.upgrade_firmware()
        firmware_page.asserting_device_upgrade_progress()
        self.take_s2_snapshot('show_switchinfo')
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(None)
        self.assert_s1_s3_diff()
        self.clear()

    def test_ath_6492_manual_upgrade_of_single_switch(self):
        conf = self.config.config_vars
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.click_switches()
        firmware_page.upgrade_firmware_using_manual_option(conf.version_type_value,conf.version_firmware)
        firmware_page.click_post_firmware_upgrade()
        firmware_page.asserting_device_upgrade_progress()
        
    def test_ath_6493_manual_upgrade_of_multiple_switches_attempt_different_build_types_builds(self):
        conf = self.config.config_vars
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.click_switches()
        firmware_page.upgrade_all_switches_using_manual_option(conf.version_type_value,conf.version_firmware)
        firmware_page.click_post_firmware_upgrade()
        firmware_page.asserting_device_upgrade_progress()
        import time
        time.sleep(600)
        firmware_page.upgrade_all_switches_using_manual_option(conf.version_type_value_2,conf.version_firmware_2)
        firmware_page.click_post_firmware_upgrade()
        firmware_page.asserting_device_upgrade_progress()
        
    def test_ath_9458_verify_scheduled_upgrade_automatic(self):
        conf = self.config.config_vars
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.click_switch_tab()
        firmware_page.select_first_switch()
        firmware_page.clicking_on_upgrade_firmware()
        firmware_page.upgrade_firmware()
        time.sleep(600)
        # self.connect_device()
        # self.browser.refresh()
        firmware_page.asserting_device_upgrade_status()
        
    def test_ath_9459_verify_scheduled_upgrade_manual(self):
        conf = self.config.config_vars
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.click_switch_tab()
        firmware_page.select_first_switch()
        firmware_page.clicking_on_upgrade_firmware()
        firmware_page.setting_firmware_upgrade_manual_option(conf.version_type_value_2,conf.switch_version)
        firmware_page.upgrade_firmware()
        time.sleep(600)
        # self.connect_device()
        # self.browser.refresh()
        firmware_page.asserting_device_upgrade_status()
        
    def test_ath_6498_verify_no_action_on_selecting_cancel_button_or_close_icon_in_upgrade_pop_up(self):
        conf = self.config.config_vars
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.click_switch_tab()
        firmware_page.select_first_switch()
        firmware_page.clicking_on_upgrade_firmware()
        firmware_page.click_cancel_icon()
        
        # firmware_page.click_switch_tab()
        # firmware_page.select_first_switch()
        firmware_page.clicking_on_upgrade_firmware()
        firmware_page.upgrade_firmware()
        time.sleep(600)
        # self.connect_device()
        # self.browser.refresh()
        firmware_page.asserting_device_upgrade_status()
        
        # firmware_page.click_switch_tab()
        # firmware_page.select_first_switch()
        firmware_page.clicking_on_upgrade_firmware()
        firmware_page.click_cancel_icon()
        
    def test_ath_9083_upgrade_default_configuration_switch_from_athena(self):
        conf = self.config.config_vars
        inner_left_panel = self.TopPanel.click_slider_icon()
        # self.take_s1_snapshot()
        group_page=inner_left_panel.add_group()
        group_page.create_unprovision_switch_group1(conf.group_1)
        self.browser.refresh()
        time.sleep(5)
        inner_left_panel = self.TopPanel.click_slider_icon()
        inner_left_panel.select_group1()
        time.sleep(5)
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.click_switch_tab()
        firmware_page.select_first_switch()
        firmware_page.clicking_on_upgrade_firmware()
        firmware_page.upgrade_firmware()
        time.sleep(600)
        # self.connect_device()
        # self.browser.refresh()
        firmware_page.click_reboot_button()
        time.sleep(5)
        inner_left_panel = self.TopPanel.click_slider_icon()
        inner_left_panel.select_default_switch()
        time.sleep(5)
        self.TopPanel.click_slider_icon()
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.move_switch_to_default_switch_group()
        inner_left_panel.manage_group() 
        manage_group_page.delete_group1()
        
    def test_ath_6491_disconnect_switch_from_athena_and_verify_the_switch_is_not_shown_in_firmware_upgrade_page(self):
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.click_switches()
        DeviceLibrary.disconnect_device_from_server('Switch_1')     
        firmware_page.assert_switch()
        device_management_page = self.LeftPanel.go_to_device_management()
        device_management_page.add_switch_and_assign_license("Switch_1")
        DeviceLibrary.getPrompt("Switch_1")
        DeviceLibrary.connect_device_to_server('Switch_1')
