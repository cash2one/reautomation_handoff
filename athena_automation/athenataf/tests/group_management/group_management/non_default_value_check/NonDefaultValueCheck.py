import logging
logger = logging.getLogger('athenataf')
import time
from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase

class NonDefaultValueCheck(AthenaGUITestCase):
	'''
	Test class for NonDefaultValueCheck.
	'''
	def _create_network(self , network_page):
		time.sleep(10)
		network_page.delete_network_if_present()
		network_page.delete_wired_network_if_present()
		basic_info = network_page.create_new_network()
		vlan_page = basic_info.employee_network_info()
		security_page = vlan_page.use_vlan_defaults()
		access_page = security_page.set_default_settings()
		access_page.click_role_radio_and_click_finish_button()
		
		basic_info = network_page.create_new_network()
		vlan_obj = basic_info.wired_employee_network_info()
		security = vlan_obj.wired_vlan_defaults()
		security.wired_employee_security_defaults()
		access = security.wired_security_defaults()
		network_assign = access.use_access_defaults()
		network_assign.finish_network_setup()	
		
	def test_ath_11748_group_configuration(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		self.take_s1_snapshot()
		if inner_left_panel.assert_group():
			if inner_left_panel.assert_sample_group_with_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.move_virtual_controller()
				inner_left_panel.manage_group()
				manage_group_page.delete_empty_group()
			elif inner_left_panel.assert_sample_group_without_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.delete_empty_group()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_multiple_groups()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_empty_group()
		inner_left_panel.select_samplegroup()
		network_page = self.LeftPanel.go_to_network_page()
		self._create_network(network_page)
		inner_left_panel.click_all_groups_label()
		inner_left_panel = self.TopPanel.click_slider_icon()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller2()
		inner_left_panel.select_samplegroup()
		network_page = self.LeftPanel.go_to_network_page()
		self._create_network(network_page)
		self.take_s2_snapshot()
		network_page.delete_network_if_present()
		network_page.delete_wired_network_if_present()
		inner_left_panel.click_all_groups_label()
		inner_left_panel = self.TopPanel.click_slider_icon()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.delete_empty_group1()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.delete_empty_group()
		self.browser.refresh()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()	
		
	def test_ath_11521_create_group(self):
		conf=self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		self.take_s1_snapshot()
		if inner_left_panel.assert_mygroup():
			if inner_left_panel.assert_mygroup_with_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.move_virtual_controller5()
				inner_left_panel.manage_group()
				manage_group_page.delete_empty_mygroup()
			elif inner_left_panel.assert_mygroup_without_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.delete_empty_mygroup()
		if  inner_left_panel.assert_mynew_group():
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_empty_mynew_group()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_multiple_empty_groups(conf.mynew)
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_group_with_vc(conf.Mygroup)
		create_group_page = inner_left_panel.add_group()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.assert_mygroup_and_mynew()
		manage_group_page.click_manage_group_close_button()
		self.take_s2_snapshot()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller5()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.delete_empty_mygroup()
		manage_group_page.delete_empty_mynew_group()
		self.browser.refresh()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11523_delete_group(self):
		conf=self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		self.take_s1_snapshot()
		if inner_left_panel.assert_mygroup():
			if inner_left_panel.assert_mygroup_with_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.move_virtual_controller5()
				inner_left_panel.manage_group()
				manage_group_page.delete_empty_mygroup()
			elif inner_left_panel.assert_mygroup_without_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.delete_empty_mygroup()
		if  inner_left_panel.assert_mynew_group():
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_empty_mynew_group()
			manage_group_page.click_manage_group_close_button()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_multiple_empty_groups(conf.mynew)
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_group_with_vc(conf.Mygroup)
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.delete_empty_mynew_group()
		manage_group_page.delete_empty_mygroup()
		manage_group_page.assert_group_has_swarm()
		self.take_s2_snapshot()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller5()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.delete_empty_mygroup()
		self.browser.refresh()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()