import logging
logger = logging.getLogger('athenataf')
import time

from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase

class NonDefaultValueCheck(AthenaGUITestCase):
	'''
	Test class for Firmware Management NonDefaultValueCheck.
	'''
	
	def test_ath_11845_firmware_check_with_vcs_attached(self):
		'''
		Assuming that 2 devices in "default" group and master slave in second group named "master_slave"
		'''
		conf = self.config.config_vars
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_default_group()
		# firmware_page.asserts_IAP1_details_in_firmware_vc_table('IAP_1')
		firmware_page.asserts_IAP1_details_in_firmware_vc_table('IAP_2')
		firmware_page.asserts_IAP1_details_in_firmware_vc_table('IAP_3')
		time.sleep(2)
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_device()
		firmware_page.asserts_IAP1_details_in_firmware_vc_table('IAP_2')
		# firmware_page.assert_master_slave_details('master')
		
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_all_group()
		firmware_page.asserts_IAP1_details_in_firmware_vc_table('IAP_1')
		firmware_page.asserts_IAP1_details_in_firmware_vc_table('IAP_2')
		firmware_page.asserts_IAP1_details_in_firmware_vc_table('IAP_3')
		
		inner_left_panel.select_master_slave_group()
		firmware_page.asserts_IAP1_details_in_firmware_vc_table('IAP_1')
		# firmware_page.assert_master_slave_details('slave')
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_all_group()
		firmware_page.asserts_IAP1_details_in_firmware_vc_table('IAP_1')
		# firmware_page.assert_master_slave_details('slave')
		

 
