import logging
logger = logging.getLogger('athenataf')
import time

from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase
from athenataf.lib.functionality.common import DeviceLibrary
from athenataf.lib.functionality.test.GroupConfigurationTest import GroupConfigurationTest

class Stress(GroupConfigurationTest):
	'''
	Test class for Group Management.
	'''
	
	def test_ath_11752_switching_vcs_multiple_times(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		# if  inner_left_panel.assert_mygroup_without_vc_present():
			# inner_left_panel.select_default_group()
			# if self.TopPanel.assert_visible_slider_icon():
				# inner_left_panel = self.TopPanel.click_slider_icon()
			# manage_group_page = inner_left_panel.manage_group()
			# manage_group_page.delete_group1()
		# if inner_left_panel.assert_mygroup_with_vc_present():
			# manage_group_page = inner_left_panel.manage_group()
			# manage_group_page.move_virtual_controller_group1()
			# inner_left_panel.select_default_group()
			# if self.TopPanel.assert_visible_slider_icon():
				# inner_left_panel = self.TopPanel.click_slider_icon()
			# manage_group_page = inner_left_panel.manage_group()
			# manage_group_page.delete_group1()
		
		# create_group_page = inner_left_panel.add_group()
		# create_group_page.create_empty_group1('group1')
		
		# manage_group_page = inner_left_panel.manage_group()
		# manage_group_page.move_virtual_controller_from_default_to_group1()
		# time.sleep(300)
		# DeviceLibrary.reconnect("IAP_1")
	
		# manage_group_page = inner_left_panel.manage_group()
		# manage_group_page.move_virtual_controller_group1()
		# time.sleep(300)
		# DeviceLibrary.reconnect("IAP_1")
	
		# manage_group_page = inner_left_panel.manage_group()
		# manage_group_page.move_virtual_controller_from_default_to_group1()
		# time.sleep(300)
		# DeviceLibrary.reconnect("IAP_1")
	
		# manage_group_page = inner_left_panel.manage_group()
		# manage_group_page.move_virtual_controller_group1()
		# time.sleep(300)
		# DeviceLibrary.reconnect("IAP_1")
	
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller_from_default_to_group1()
		time.sleep(300)
		DeviceLibrary.reconnect("IAP_1")
		
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller_group1()
		time.sleep(300)
		DeviceLibrary.reconnect("IAP_1")
	
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller_from_default_to_group1()
		time.sleep(300)
		DeviceLibrary.reconnect("IAP_1")
	
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller_group1()
		time.sleep(300)
		DeviceLibrary.reconnect("IAP_1")
	
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller_from_default_to_group1()
		
		# manage_group_page = inner_left_panel.manage_group()
		# manage_group_page.move_virtual_controller_group1()
		
		# manage_group_page = inner_left_panel.manage_group()
		# manage_group_page.move_virtual_controller_from_default_to_group1()
		
		# manage_group_page = inner_left_panel.manage_group()
		# manage_group_page.move_virtual_controller_group1()
		
		# manage_group_page = inner_left_panel.manage_group()
		# manage_group_page.move_virtual_controller_from_default_to_group1()
		
		# manage_group_page = inner_left_panel.manage_group()
		# manage_group_page.move_virtual_controller_group1()
		
		# manage_group_page = inner_left_panel.manage_group()
		# manage_group_page.move_virtual_controller_from_default_to_group1()
		
		# manage_group_page = inner_left_panel.manage_group()
		# manage_group_page.move_virtual_controller_group1()
		
		# manage_group_page = inner_left_panel.manage_group()
		# manage_group_page.move_virtual_controller_from_default_to_group1()
		
		# manage_group_page = inner_left_panel.manage_group()
		# manage_group_page.move_virtual_controller_group1()
		
		# manage_group_page = inner_left_panel.manage_group()
		# manage_group_page.move_virtual_controller_from_default_to_group1()
		
		time.sleep(300)
		DeviceLibrary.reconnect("IAP_1")
		
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller_group1()
		
		if  inner_left_panel.assert_mygroup_without_vc_present():
			inner_left_panel.select_default_group()
			if self.TopPanel.assert_visible_slider_icon():
				inner_left_panel = self.TopPanel.click_slider_icon()
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_group1()
		if inner_left_panel.assert_mygroup_with_vc_present():
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.move_virtual_controller_group1()
			inner_left_panel.select_default_group()
			if self.TopPanel.assert_visible_slider_icon():
				inner_left_panel = self.TopPanel.click_slider_icon()
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_group1()
		time.sleep(300)
		DeviceLibrary.reconnect("IAP_1")