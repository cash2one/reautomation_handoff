import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase
import time
from athenataf.lib.functionality.common import DeviceLibrary

class ImmediateUpgrade(AthenaGUITestCase):
	'''
	Test class for Immediate Upgrade.
	'''
	def test_ath_4415_check_upgrade_status_from_different_levels(self):
		conf = self.config.config_vars
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		# self.take_s1_snapshot("show_version")
		firmware_page.select_vc_for_upgrade('IAP_1')
		firmware_page.select_vc_for_upgrade('IAP_2')
		firmware_page.clicking_on_upgrade_firmware()
		firmware_page.upgrade_firmware()
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_default_group()
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		firmware_page.asserting_device_upgrade_progress()
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_device()
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()        
		firmware_page.asserting_device_upgrade_progress()
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.expand_group_icon1()
		inner_left_panel.select_device2()
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		firmware_page.asserting_device_upgrade_progress()
		firmware_page.buy_time()
		DeviceLibrary.getPrompt("IAP_1")    
		DeviceLibrary.connect_device_to_server("IAP_1")
		DeviceLibrary.getPrompt("IAP_2")    
		DeviceLibrary.connect_device_to_server("IAP_2")
		time.sleep(5)
		# self.take_s2_snapshot("show_version")
		'''
		downgrade back to base version
		'''
		firmware_page.select_first_vc()
		firmware_page.select_second_vc()
		firmware_page.clicking_on_upgrade_firmware()
		firmware_page.setting_firmware_upgrade_manual_option(option=conf.version_type_value_2,version=conf.firmware_base_version)
		firmware_page.click_post_firmware_upgrade()
		firmware_page.buy_time()
		DeviceLibrary.connect_device_to_server("IAP_1")
		DeviceLibrary.connect_device_to_server("IAP_2")
		time.sleep(5)


	def test_ath_4404_immediate_upgrade_downgrade_manual(self):
		conf = self.config.config_vars
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		# self.take_s1_snapshot("show_version")
		firmware_page.select_vc_for_upgrade('IAP_1')
		firmware_page.select_vc_for_upgrade('IAP_2')
		firmware_page.clicking_on_upgrade_firmware()
		firmware_page.setting_firmware_upgrade_manual_option(option=conf.version_type_value_2,version=conf.firmware_version_4122)
		firmware_page.click_post_firmware_upgrade()
		firmware_page.buy_time()
		# time.sleep(400)
		DeviceLibrary.getPrompt("IAP_1")
		DeviceLibrary.connect_device_to_server("IAP_1")
		DeviceLibrary.getPrompt("IAP_2")
		DeviceLibrary.connect_device_to_server("IAP_2")
		time.sleep(5)
		firmware_page.assert_firmware_version('IAP_1',conf.firmware_version_4122)
		firmware_page.assert_firmware_version('IAP_2',conf.firmware_version_4122)
		# self.take_s2_snapshot("show_version")
		firmware_page.select_vc_for_upgrade('IAP_1')
		firmware_page.select_vc_for_upgrade('IAP_2')
		firmware_page.clicking_on_upgrade_firmware()
		firmware_page.setting_firmware_upgrade_manual_option(option=conf.version_type_value_2,version=conf.firmware_base_version)
		firmware_page.click_post_firmware_upgrade()
		firmware_page.buy_time()
		DeviceLibrary.getPrompt("IAP_1")       
		DeviceLibrary.connect_device_to_server("IAP_1")
		DeviceLibrary.getPrompt("IAP_2")
		DeviceLibrary.connect_device_to_server("IAP_2")
		time.sleep(5)
		firmware_page.assert_firmware_version('IAP_1',conf.firmware_base_version)
		firmware_page.assert_firmware_version('IAP_2',conf.firmware_base_version)

	def test_ath_9057_Immediate_upgrade_beta_image(self):
		conf = self.config.config_vars
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		# self.take_s1_snapshot("show_version")
		firmware_page.select_vc_for_upgrade('IAP_1')
		firmware_page.clicking_on_upgrade_firmware()
		firmware_page.setting_firmware_upgrade_manual_option(option=conf.version_type_value_2,version=conf.firmware_upgrade_version)
		firmware_page.click_post_firmware_upgrade()
		firmware_page.asserting_device_upgrade_status()
		firmware_page.buy_time()
		time.sleep(5)
		DeviceLibrary.getPrompt("IAP_1")
		DeviceLibrary.connect_device_to_server("IAP_1")
		firmware_page.assert_firmware_version('IAP_1',conf.firmware_upgrade_version)
		# self.take_s2_snapshot("show_version")
		'''
		downgrade back to base version
		'''
		firmware_page.select_vc_for_upgrade('IAP_1')
		firmware_page.clicking_on_upgrade_firmware()
		firmware_page.setting_firmware_upgrade_manual_option(option=conf.version_type_value_2,version=conf.firmware_base_version)
		firmware_page.click_post_firmware_upgrade()
		firmware_page.buy_time()
		DeviceLibrary.getPrompt("IAP_1")    
		DeviceLibrary.connect_device_to_server("IAP_1")


	def test_ath_4405_immediate_upgrade_of_mixed_and_match_swarm(self):
		conf = self.config.config_vars
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		# self.take_s1_snapshot("show_version")
		firmware_page.select_vc_for_upgrade('IAP_1')
		firmware_page.select_vc_for_upgrade('IAP_2')
		firmware_page.clicking_on_upgrade_firmware()
		firmware_page.setting_firmware_upgrade_manual_option(option=conf.version_type_value_2,version=conf.firmware_upgrade_version)
		firmware_page.click_post_firmware_upgrade()
		firmware_page.buy_time()
		time.sleep(5)
		DeviceLibrary.getPrompt("IAP_1")
		DeviceLibrary.connect_device_to_server("IAP_1")
		DeviceLibrary.getPrompt("IAP_2")
		DeviceLibrary.connect_device_to_server("IAP_2")
		time.sleep(5)
		firmware_page.assert_firmware_version('IAP_1',conf.firmware_upgrade_version)
		firmware_page.assert_firmware_version('IAP_2',conf.firmware_upgrade_version)
		# self.take_s2_snapshot("show_version")
		'''
		downgrade back to base version
		'''
		firmware_page.select_vc_for_upgrade('IAP_1')
		firmware_page.select_vc_for_upgrade('IAP_2')
		firmware_page.clicking_on_upgrade_firmware()
		firmware_page.setting_firmware_upgrade_manual_option(option=conf.version_type_value_2,version=conf.firmware_base_version)
		firmware_page.click_post_firmware_upgrade()
		firmware_page.buy_time()
		DeviceLibrary.getPrompt("IAP_1")
		DeviceLibrary.connect_device_to_server("IAP_1")
		DeviceLibrary.getPrompt("IAP_2")
		DeviceLibrary.connect_device_to_server("IAP_2")


	def test_ath_4403_immediate_upgrade_automatic(self):
		conf = self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_default_group()
		time.sleep(5)
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		firmware_page.select_vc_for_upgrade('IAP_1')
		firmware_page.select_vc_for_upgrade('IAP_2')
		firmware_page.clicking_on_upgrade_firmware()
		firmware_page.upgrade_firmware()
		self.buy_time()
		time.sleep(5)
		DeviceLibrary.getPrompt("IAP_1")
		DeviceLibrary.connect_device_to_server("IAP_1")
		DeviceLibrary.getPrompt("IAP_2")
		DeviceLibrary.connect_device_to_server("IAP_2")
		time.sleep(5)
		firmware_page.select_vc_for_upgrade('IAP_1')
		firmware_page.select_vc_for_upgrade('IAP_2')
		firmware_page.clicking_on_upgrade_firmware()
		firmware_page.setting_firmware_upgrade_manual_option(option=conf.version_type_value_2,version=conf.firmware_base_version)
		firmware_page.click_post_firmware_upgrade()
		firmware_page.buy_time()
		DeviceLibrary.getPrompt("IAP_1")
		DeviceLibrary.connect_device_to_server("IAP_1")
		DeviceLibrary.getPrompt("IAP_2")
		DeviceLibrary.connect_device_to_server("IAP_2")
