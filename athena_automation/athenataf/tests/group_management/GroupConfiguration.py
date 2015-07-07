import logging
logger = logging.getLogger('athenataf')
import time

from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase

class GroupConfiguration(AthenaGUITestCase):
	'''
	Test class for group management.
	'''
	def _create_network(self , network_page):
		time.sleep(4)
		basic_info_page = network_page.create_new_network()
		virtual_lan_page = basic_info_page.employee_network_info()
		security_page = virtual_lan_page.select_virtual_controller()
		access_page = security_page.configure_employee_security()
		access_page.finish_network_setup()
		
	def test_ath_880_configure_group_with_member(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		if inner_left_panel.assert_group():
			if inner_left_panel.assert_sample_group_with_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.move_virtual_controller()
				inner_left_panel.manage_group()
				manage_group_page.delete_empty_group()
			elif inner_left_panel.assert_sample_group_without_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.delete_empty_group()
		self.take_s1_snapshot()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_group()
		inner_left_panel.assert_group_exist()
		inner_left_panel.select_sample_group()
		network_page = self.LeftPanel.go_to_network_page()
		self._create_network(network_page)
		network_page.assert_new_network()
		network_page.delete_network_if_present()
		self.TopPanel.click_slider_icon()
		inner_left_panel.select_default_group()
		self.TopPanel.click_slider_icon()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller()
		inner_left_panel.manage_group()
		manage_group_page.delete_empty_group()
		inner_left_panel.assert_group_not_exist()
		self.connect_device()
		self.take_s2_snapshot()
		self.TopPanel.innerleft_panel_icon.click()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_882_delete_configuration(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		if inner_left_panel.assert_group():
			if inner_left_panel.assert_sample_group_with_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.move_virtual_controller()
				inner_left_panel.manage_group()
				manage_group_page.delete_empty_group()
			elif inner_left_panel.assert_sample_group_without_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.delete_empty_group()
		self.take_s1_snapshot()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_group()
		inner_left_panel.assert_group_exist()
		inner_left_panel.select_sample_group()
		network_page = self.LeftPanel.go_to_network_page()
		self._create_network(network_page)
		network_page.assert_new_network()
		network_page.delete_network_if_present()
		network_page.assert_network_not_exist()
		self.TopPanel.click_slider_icon()
		inner_left_panel.select_default_group()
		self.TopPanel.click_slider_icon()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller()
		inner_left_panel.manage_group()
		manage_group_page.delete_empty_group()
		inner_left_panel.assert_group_not_exist()
		self.connect_device()
		self.take_s2_snapshot()
		self.TopPanel.innerleft_panel_icon.click()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_881_move_vcs_between_the_group(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		if inner_left_panel.assert_group():
			if inner_left_panel.assert_sample_group_with_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.move_virtual_controller()
				inner_left_panel.manage_group()
				manage_group_page.delete_empty_group()
			elif inner_left_panel.assert_sample_group_without_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.delete_empty_group()
		self.take_s1_snapshot()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_empty_group()
		inner_left_panel.assert_group_exist()
		inner_left_panel.select_sample_group()
		network_page = self.LeftPanel.go_to_network_page()
		self._create_network(network_page)
		network_page.assert_new_network()
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.add_group()
		create_group_page.create_multiple_groups()
		inner_left_panel.select_new_group()
		self.LeftPanel.go_to_network_page()
		self._create_network(network_page)
		network_page.assert_new_network()
		self.TopPanel.click_slider_icon()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller2()
		inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller()
		inner_left_panel.select_sample_group()
		self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		network_page.assert_network_not_exist()
		self.TopPanel.click_slider_icon()
		inner_left_panel.select_new_group()
		self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		network_page.assert_network_not_exist()
		self.TopPanel.click_slider_icon()
		inner_left_panel.select_default_group()
		self.TopPanel.click_slider_icon()
		inner_left_panel.manage_group()
		manage_group_page.delete_empty_group()
		manage_group_page=inner_left_panel.manage_group()
		manage_group_page.delete_empty_group1()
		self.connect_device()
		self.take_s2_snapshot()
		self.TopPanel.innerleft_panel_icon.click()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()