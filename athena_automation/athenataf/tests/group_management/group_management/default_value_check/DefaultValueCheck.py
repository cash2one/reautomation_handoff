import logging
logger = logging.getLogger('athenataf')
import time

from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase
from athenataf.lib.functionality.common import DeviceLibrary
from athenataf.lib.functionality.test.GroupConfigurationTest import GroupConfigurationTest

class DefaultValueCheck(GroupConfigurationTest):
	'''
	Test class for DefaultValueCheck.
	'''
	def test_ath_11524_check_default_values_of_group_management(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.assert_default_manage_groups_fields()
		create_group_page=manage_group_page.create_new_group_from_manage()
		create_group_page.assert_default_create_groups_fields()
		create_group_page.click_create_page_cancel_button()
		manage_group_page=inner_left_panel.manage_group()
		manage_group_page.assert_delete_and_clone_disabled_for_all_group()
		manage_group_page.assert_delete_and_clone_disabled_for_all_group()
		
	def test_ath_11527_check_clone(self):
		conf=self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		if inner_left_panel.assert_Mygroups():
			if inner_left_panel.assert_mygroup_0_with_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.move_virtual_controller_from_Mygroup(mygroup=True)
				inner_left_panel.select_default_group()
				inner_left_panel = self.TopPanel.click_slider_icon()
				inner_left_panel.manage_group()
				manage_group_page.delete_empty_Mygroup1()
			if inner_left_panel.assert_mygroup_0_without_vc_present():
				inner_left_panel.select_default_group()
				inner_left_panel = self.TopPanel.click_slider_icon()
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.delete_empty_Mygroup1()
		if inner_left_panel.assert_Mygroups():
			if inner_left_panel.assert_mygroup_2_with_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.move_virtual_controller_from_Mygroup(mygroup2=True)
				inner_left_panel.select_default_group()
				if self.TopPanel.assert_visible_slider_icon():
					inner_left_panel = self.TopPanel.click_slider_icon()
				inner_left_panel.manage_group()
				manage_group_page.delete_empty_Mygroup2()
			if inner_left_panel.assert_mygroup_2_without_vc_present():
				inner_left_panel.select_default_group()
				if self.TopPanel.assert_visible_slider_icon():
					inner_left_panel = self.TopPanel.click_slider_icon()
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.delete_empty_Mygroup2()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_group_with_vc(conf.my_group)
		time.sleep(300)
		DeviceLibrary.reconnect("IAP_1")
		manage_group_page1 = inner_left_panel.manage_group()
		manage_group_page1.cloning_mygroup2()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.assert_delete_and_clone_disabled_for_all_group()
		manage_group_page.assert_delete_and_clone_enabled_for_other_groups()
		manage_group_page.assert_delete_and_clone_disabled_for_all_group()
		manage_group_page.close_icon.click()
		if inner_left_panel.assert_Mygroups():
			if inner_left_panel.assert_mygroup_0_with_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.move_virtual_controller_from_Mygroup(mygroup=True)
				inner_left_panel.select_default_group()
				if self.TopPanel.assert_visible_slider_icon():
					inner_left_panel = self.TopPanel.click_slider_icon()
				inner_left_panel.manage_group()
				manage_group_page.delete_empty_Mygroup1()
			if inner_left_panel.assert_mygroup_0_without_vc_present():
				inner_left_panel.select_default_group()
				if self.TopPanel.assert_visible_slider_icon():
					inner_left_panel = self.TopPanel.click_slider_icon()
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.delete_empty_Mygroup1()
		if inner_left_panel.assert_Mygroups():
			if inner_left_panel.assert_mygroup_2_with_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.move_virtual_controller_from_Mygroup(mygroup2=True)
				inner_left_panel.select_default_group()
				if self.TopPanel.assert_visible_slider_icon():
					inner_left_panel = self.TopPanel.click_slider_icon()
				inner_left_panel.manage_group()
				manage_group_page.delete_empty_Mygroup2()
			if inner_left_panel.assert_mygroup_2_without_vc_present():
				inner_left_panel.select_default_group()
				if self.TopPanel.assert_visible_slider_icon():
					inner_left_panel = self.TopPanel.click_slider_icon()
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.delete_empty_Mygroup2()
		time.sleep(300)
		DeviceLibrary.reconnect("IAP_1")