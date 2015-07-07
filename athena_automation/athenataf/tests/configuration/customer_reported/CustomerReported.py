import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest
import time

class CustomerReported(ConfigurationTest):
	'''
	Test class for Customer Reported
	'''
	
	def test_ath_10998_edit_a_created_network_using_firefox(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		security.security_level_enterprise()
		access = security.click_on_next()
		access.finish_network_setup()
		edit_network = self.NetworkPage.edit_network()
		edit_network.select_group_user()
		edit_network._save_settings()
		self.take_s2_snapshot()
		edit_network = self.NetworkPage.edit_network()
		edit_network.assert_guest_user()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
		
	def test_ath_11011_scroll_bar_in_edit_vc_name(self):
		conf=self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_all_virtual_controller_to_default_group()
		import time
		time.sleep(5)
		# inner_left_panel.select_group(inner_left_panel.default_group_click)
		inner_left_panel.click_on_close_icon()
		time.sleep(5)
		# network_page = self.LeftPanel.go_to_network_page()
		# inner_left_panel.select_wireless_configuration_module()
		system_page = self.LeftPanel.go_to_system_page()
		logger.debug('System Page : clicking on edit vc name')
		system_page.edit_values_name.click()
		logger.debug('System Page : Asserting scroll bar')
		system_page.browser.assert_element(system_page.scroll_bar,'Scroll Bar is not visible')
		

	def test_ath_10997_check_list_of_groups_under_wireless_configuration(self):
		conf = self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		group_page=inner_left_panel.add_group()
		group_page.create_multiple_empty_groups(conf.group_1)
		group_page=inner_left_panel.add_group()
		group_page.create_multiple_empty_groups(conf.group_2)
		group_page=inner_left_panel.add_group()
		group_page.create_multiple_empty_groups(conf.my_group_2)
		self.browser.refresh()
		time.sleep(5)

		self.LeftPanel.go_to_network_page()

		self.logout()

		self.login()

		self.browser.go_to(self.config.global_vars.url_group)
		self.browser.key_press(u'\ue007')

		self.TopPanel.click_slider_icon()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.delete_group1()

		inner_left_panel.manage_group()
		manage_group_page.delete_group2()

		inner_left_panel.manage_group()
		manage_group_page.delete_empty_Mygroup2()