import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class CustomerReported(ConfigurationTest):
	'''
	Test class for CustomerReported 
	'''
	
	def test_ath_11312_scroll_bar_in_edit_vc_name(self):
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
		
		
		
		
		
		