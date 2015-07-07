import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class System(ConfigurationTest):
	'''
	Test class for System .
	'''
	def test_ath_11009_configure_vc_name_on_iap_level(self):
		
		#Test Case contains override issue
		
		inner_left_panel = self.TopPanel.click_slider_icon()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_group()
		inner_left_panel.select_sample_group()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.edit_vc_name_values()
		vc_default_value = system_page.vc_name_textbox1.get_attribute_value('title')
		system_page.edit_vc_name_icon1()
		system_page.set_vc_name(self.config.config_vars.vcip)
		system_page.save_int_vc_name()
		system_page.save_vc_name()
		system_page.edit_vc_name_values()
		system_page.set_vc_name(vc_default_value)
		system_page.save_int_vc_name()
		system_page.save_vc_name()
		
		inner_left_panel1 = self.TopPanel.click_slider_icon()
		manage_group_page = inner_left_panel1.manage_group()
		manage_group_page.move_virtual_controller()
		self.TopPanel.go_to_allgroups()
		inner_left_panel2 = self.TopPanel.click_slider_icon()
		manage_group_page1 = inner_left_panel2.manage_group()
		manage_group_page1.delete_empty_group()
		self.browser.refresh()
		
		inner_left_panel = self.TopPanel.click_slider_icon()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_group()
		inner_left_panel.select_sample_group()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.edit_vc_name_values()
		vc_default_value = system_page.vc_name_textbox1.get_attribute_value('title')
		system_page.edit_vc_name_icon1()
		system_page.set_vc_name(self.config.config_vars.vcip)
		system_page.save_int_vc_name()
		system_page.save_vc_name()
		
		#test case is parked due to override issue
		
		
		
		