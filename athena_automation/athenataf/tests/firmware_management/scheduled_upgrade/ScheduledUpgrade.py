import logging
logger = logging.getLogger('athenataf')
import time

from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase
from athenataf.lib.functionality.common import DeviceLibrary

class ScheduledUpgrade(AthenaGUITestCase):
    '''
    Test class for Firmware Management DefaultValueCheck.
    '''
    
    def test_ath_4410_check_the_default_values_in_firmware_page(self):
        ''' manual...
            upgrade any swarm
        '''
        conf=self.config.config_vars
        inner_left_panel = self.TopPanel.click_slider_icon()
        # self.take_s1_snapshot("show_version")
        inner_left_panel.select_default_group()
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.upgrade_firmware_using_manual_option(conf.version_type_value_2,conf.version_firmware_3)
        firmware_page.click_post_firmware_upgrade()
        DeviceLibrary.connect_device_to_server('IAP_1')
        # DeviceLibrary.connect_device_to_server('IAP_2')
        time.sleep(60)
        firmware_page.assert_firmware_version('IAP_1',conf.firmware_upgrade_version)
        # firmware_page.assert_firmware_version('IAP_2',conf.firmware_upgrade_version)
        # self.take_s2_snapshot("show_version")
        # firmware_page.buy_time()
        # firmware_page.asserting_device_upgraded_successful1()
        firmware_page.select_first_vc()
        firmware_page.clicking_on_upgrade_firmware()
        firmware_page.setting_firmware_upgrade_manual_option(conf.version_type_value_2,conf.firmware_base_version)
        firmware_page.click_post_firmware_upgrade()
        time.sleep(60)
        DeviceLibrary.connect_device_to_server('IAP_1')
        # DeviceLibrary.connect_device_to_server('IAP_2')
    
        self.buy_time()
        firmware_page.assert_firmware_version('IAP_1',conf.firmware_upgrade_version)
        # firmware_page.assert_firmware_version('IAP_2',conf.firmware_upgrade_version)
        
    def test_ath_4411_upgrade_multiple_vcs_together(self):
        '''automatic '''
        conf = self.config.config_vars
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        self.take_s1_snapshot("show_version")
        firmware_page.select_first_vc()
        firmware_page.select_second_vc()
        # firmware_page.select_third_vc()
        firmware_page.clicking_on_upgrade_firmware()
        firmware_page.upgrade_firmware()
        DeviceLibrary.connect_device_to_server('IAP_1')
        DeviceLibrary.connect_device_to_server('IAP_2')
        # DeviceLibrary.connect_device_to_server('IAP_3')
        time.sleep(60)
        firmware_page.assert_firmware_version('IAP_1',conf.firmware_upgrade_version)
        firmware_page.assert_firmware_version('IAP_2',conf.firmware_upgrade_version)
        # firmware_page.assert_firmware_version('IAP_3',conf.firmware_upgrade_version)
        # self.take_s2_snapshot("show_version")
        firmware_page.select_first_vc()
        firmware_page.select_second_vc()
        # firmware_page.select_third_vc()
        firmware_page.clicking_on_upgrade_firmware()
        firmware_page.setting_firmware_upgrade_manual_option(conf.version_type_value_2,conf.firmware_base_version)
        firmware_page.click_post_firmware_upgrade()
        time.sleep(60)
        DeviceLibrary.connect_device_to_server('IAP_1')
        DeviceLibrary.connect_device_to_server('IAP_2')
        # DeviceLibrary.connect_device_to_server('IAP_3')
        self.buy_time()
        firmware_page.assert_firmware_version('IAP_1',conf.firmware_upgrade_version)
        firmware_page.assert_firmware_version('IAP_2',conf.firmware_upgrade_version)
        # firmware_page.assert_firmware_version('IAP_3',conf.firmware_upgrade_version)
        
        
    def test_ath_4413_cancel_a_scheduled_upgrade_and_reschedule_it_again(self):
        conf = self.config.config_vars
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.select_first_vc()
        firmware_page.upgrade_button.click()
        firmware_page.select_later_date_radio()
        firmware_page.set_upgrade_after_ten_mins()
        firmware_page.click_post_firmware_upgrade()
        firmware_page.cancel_upgrade.click()
        self.browser.refresh()
        firmware_page.assert_cancel_upgrade_button()
        
        
	def test_ath_9058_immediate_upgrade_beta_image(self):
		''' 
		Immediate -- manual upgrade
		'''
		conf = self.config.config_vars
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		firmware_page.select_vc_for_upgrade('IAP_1')
		firmware_page.clicking_on_upgrade_firmware()
		firmware_page.setting_firmware_upgrade_manual_option(option=conf.version_type_value_2,version=conf.firmware_upgrade_version)

		firmware_page.select_later_date_radio()
		firmware_page.set_upgrade_after_ten_mins()
		firmware_page.click_post_firmware_upgrade()

		time.sleep(1200)
		DeviceLibrary.getPrompt("IAP_1")
		DeviceLibrary.connect_device_to_server('IAP_1')
		time.sleep(60)
		firmware_page.assert_firmware_version('IAP_1',conf.firmware_upgrade_version) 

		firmware_page.select_vc_for_upgrade('IAP_1')
		firmware_page.clicking_on_upgrade_firmware()
		firmware_page.setting_firmware_upgrade_manual_option(conf.version_type_value_2,conf.firmware_base_version)
		firmware_page.click_post_firmware_upgrade()
		time.sleep(60)
		DeviceLibrary.getPrompt("IAP_1")
		DeviceLibrary.connect_device_to_server('IAP_1')
		self.buy_time()
		firmware_page.assert_firmware_version('IAP_1',conf.firmware_upgrade_version) 
        
    def test_ath_4408_scheduled_upgrade_automatic(self):
        ''' automatic upgrade '''
        conf = self.config.config_vars
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        latest_version = firmware_page.get_latest_recommended_version()
        firmware_page.select_vc_for_upgrade('IAP_1')
        # firmware_page.select_second_vc()
        firmware_page.upgrade_button.click()
        firmware_page.select_later_date_radio()
        firmware_page.set_upgrade_after_ten_mins()
        firmware_page.click_post_firmware_upgrade()
        time.sleep(600)
        DeviceLibrary.getPrompt("IAP_1")
        DeviceLibrary.connect_device_to_server('IAP_1')
        # DeviceLibrary.connect_device_to_server('IAP_2')
        self.buy_time()
        firmware_page.assert_firmware_version('IAP_1',latest_version) 
        # firmware_page.assert_firmware_version('IAP_2',conf.firmware_upgrade_version)
        # firmware_page.asserting_device_upgraded_successful1()
        firmware_page.select_vc_for_upgrade('IAP_1')
        # firmware_page.select_second_vc()
        firmware_page.clicking_on_upgrade_firmware()
        firmware_page.setting_firmware_upgrade_manual_option(conf.version_type_value_2,conf.firmware_base_version)
        firmware_page.click_post_firmware_upgrade()
        time.sleep(600)
        DeviceLibrary.getPrompt("IAP_1")
        DeviceLibrary.connect_device_to_server('IAP_1')
        # DeviceLibrary.connect_device_to_server('IAP_2')
        self.buy_time()
        firmware_page.assert_firmware_version('IAP_1',conf.firmware_upgrade_version) 
        # firmware_page.assert_firmware_version('IAP_2',conf.firmware_upgrade_version)
        
    def test_ath_4409_scheduled_upgrade_downgrade_manual(self):
        '''manual upgrade and downgrade of a swarm'''
        conf = self.config.config_vars
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        # self.take_s1_snapshot("show_version")
        firmware_page.select_vc_for_upgrade('IAP_1')
        # firmware_page.select_vc_for_upgrade('IAP_2')
        firmware_page.clicking_on_upgrade_firmware()
        firmware_page.setting_firmware_upgrade_manual_option(conf.version_type_value_2,conf.firmware_upgrade_version)
        firmware_page.select_later_date_radio()
        firmware_page.set_upgrade_after_ten_mins()
        firmware_page.click_post_firmware_upgrade()
        time.sleep(12)
        firmware_page.asser_successfully_upgrading_msg()
        time.sleep(1200)
        DeviceLibrary.getPrompt("IAP_1")
        DeviceLibrary.connect_device_to_server('IAP_1')
        # DeviceLibrary.getPrompt("IAP_1")
        # DeviceLibrary.connect_device_to_server('IAP_2')
        firmware_page.buy_time()
        firmware_page.assert_firmware_version('IAP_1',conf.firmware_upgrade_version) 
        # firmware_page.assert_firmware_version('IAP_2',conf.firmware_upgrade_version)
        ''' now downgrading'''
        firmware_page.select_vc_for_upgrade('IAP_1')
        # firmware_page.select_vc_for_upgrade('IAP_2')
        firmware_page.clicking_on_upgrade_firmware()
        firmware_page.setting_firmware_upgrade_manual_option(conf.version_type_value_2,conf.firmware_base_version)
        firmware_page.select_later_date_radio()
        firmware_page.set_upgrade_after_ten_mins()
        firmware_page.click_post_firmware_upgrade()
        time.sleep(12)
        firmware_page.asser_successfully_upgrading_msg()
        time.sleep(1200)
        DeviceLibrary.connect_device_to_server('IAP_1')
        # DeviceLibrary.connect_device_to_server('IAP_2')
        firmware_page.buy_time()
        firmware_page.assert_firmware_version('IAP_1',conf.firmware_upgrade_version) 
        # firmware_page.assert_firmware_version('IAP_2',conf.firmware_upgrade_version)
        # self.take_s2_snapshot("show_version")