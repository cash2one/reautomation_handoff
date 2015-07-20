import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase
from athenataf.lib.functionality.common import DeviceLibrary
from athenataf.lib.functionality.test.GroupConfigurationTest import GroupConfigurationTest
import time

class EditTestScenarios(GroupConfigurationTest):
	'''
	Test class for EditTestScenarios.
	'''
	def test_ath_11530_move_vcs(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.click_move_button()
		manage_group_page.assert_move_group_wihtout_selecting_vc()
		manage_group_page.click_alert_ok_button()
		manage_group_page.click_manage_group_close_button()

	def test_ath_11750_modify_the_created_network(self):
		conf=self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		if  inner_left_panel.assert_mygroup_without_vc_present():
			inner_left_panel.select_default_group()
			inner_left_panel = self.TopPanel.click_slider_icon()
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_group1()
		if inner_left_panel.assert_mygroup_with_vc_present():
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.move_virtual_controller_group1()
			inner_left_panel.select_default_group()
			inner_left_panel = self.TopPanel.click_slider_icon()
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_group1()
		self.take_s1_snapshot()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_group_with_vc1('group1')
		inner_left_panel.select_group(inner_left_panel.group_1)
		time.sleep(300)
		DeviceLibrary.reconnect("IAP_1")
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		basic_info = network_page.create_new_network()
		basic_info.employee_network_info_with_advanced_settings()
		basic_info.set_inactivity_timeout_value(self.config.config_vars.valid_inactivity_timeout)
		vlan = basic_info.click_on_next()
		security_page = vlan.select_virtual_controller()
		security_page.security_level_enterprise()
		security_page.configure_80211r_romaing()
		access = security_page.click_on_next()
		access.finish_network_setup()
		network_page.assert_new_network()
		self.LeftPanel.assert_delta_config_icon()
		edit_network_page = network_page.edit_network()
		edit_network_page.basic_info_accordion.click()
		edit_network_page.select_group_user()
		edit_network_page.page_down()
		edit_network_page.setting_splash_page_type_internal_acknowledge(self.config.config_vars.internal_acknowledge)
		edit_network_page.setting_password(conf.edit_Retype_auth_shared_key)
		edit_network_page.click_vc_assigned()
		edit_network_page._save_settings()
		edit_network_page = network_page.edit_network()
		edit_network_page.asserting_modified_created_network()
		self.take_s2_snapshot()
		self.LeftPanel.assert_delta_config_icon()
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		self.TopPanel.go_to_allgroups()
		inner_left_panel = self.TopPanel.click_slider_icon()
		if  inner_left_panel.assert_mygroup_without_vc_present():
			inner_left_panel.select_default_group()
			inner_left_panel = self.TopPanel.click_slider_icon()
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_group1()
		if inner_left_panel.assert_mygroup_with_vc_present():
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.move_virtual_controller_group1()
			inner_left_panel.select_default_group()
			inner_left_panel = self.TopPanel.click_slider_icon()
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_group1()
		time.sleep(300)
		DeviceLibrary.reconnect("IAP_1")
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_11749_delete_configuration(self):
		conf=self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		if  inner_left_panel.assert_mygroup_without_vc_present():
			inner_left_panel.select_default_group()
			inner_left_panel = self.TopPanel.click_slider_icon()
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_group1()
		if inner_left_panel.assert_mygroup_with_vc_present():
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.move_virtual_controller_group1()
			inner_left_panel.select_default_group()
			inner_left_panel = self.TopPanel.click_slider_icon()
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_group1()
		self.take_s1_snapshot()			
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_empty_group1('group1')
		inner_left_panel.select_group(inner_left_panel.group_1)
		network_page = self.LeftPanel.go_to_network_page()
		# network_page.delete_specific_network_if_present(conf.network_name1)
		# network_page.delete_specific_network_if_present(conf.network_name2)
		# network_page.delete_network_if_present()	
		basic_info = network_page.create_new_network()
		vlan_obj = basic_info.create_new_network(basic_info.wireless,conf.network_name1,basic_info.employee)
		security = vlan_obj.use_vlan_defaults()
		access = security.set_default_settings()
		access.finish_network_setup()
		basic_info = network_page.create_new_network()
		vlan_obj = basic_info.create_new_network(basic_info.wireless,conf.network_name2,basic_info.voice)
		security = vlan_obj.use_vlan_defaults()
		access = security.set_default_settings()
		access.finish_network_setup()
		basic_info = network_page.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.click_on_next()
		access = security.move_to_next_page()
		access.finish_network_setup()
		inner_left_panel = self.TopPanel.click_slider_icon()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller_from_default_to_group1()
		inner_left_panel.select_group(inner_left_panel.group_1)
		time.sleep(300)
		DeviceLibrary.reconnect("IAP_1")
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_specific_network_if_present(conf.network_name1)
		network_page.delete_specific_network_if_present(conf.network_name2)
		network_page.delete_network_if_present()
		time.sleep(100)
		basic_info = network_page.create_new_network()
		vlan_obj = basic_info.create_new_network(basic_info.wireless,conf.network_name1,basic_info.employee)
		security = vlan_obj.use_vlan_defaults()
		access = security.set_default_settings()
		access.finish_network_setup()
		basic_info = network_page.create_new_network()
		vlan_obj = basic_info.create_new_network(basic_info.wireless,conf.network_name2,basic_info.voice)
		security = vlan_obj.use_vlan_defaults()
		access = security.set_default_settings()
		access.finish_network_setup()
		basic_info = network_page.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.click_on_next()
		access = security.use_security_default()
		access.finish_network_setup()
		self.take_s2_snapshot()
		network_page = self.LeftPanel.go_to_network_page()		
		network_page.delete_specific_network_if_present(conf.network_name1)
		network_page.delete_specific_network_if_present(conf.network_name2)
		network_page.delete_network_if_present()
		self.TopPanel.go_to_allgroups()
		inner_left_panel = self.TopPanel.click_slider_icon()
		if  inner_left_panel.assert_mygroup_without_vc_present():
			inner_left_panel.select_default_group()
			inner_left_panel = self.TopPanel.click_slider_icon()
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_group1()
		if inner_left_panel.assert_mygroup_with_vc_present():
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.move_virtual_controller_group1()
			inner_left_panel.select_default_group()
			inner_left_panel = self.TopPanel.click_slider_icon()
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_group1()
		time.sleep(300)
		DeviceLibrary.reconnect("IAP_1")
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
