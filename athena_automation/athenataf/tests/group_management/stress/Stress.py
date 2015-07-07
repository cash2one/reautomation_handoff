import logging
logger = logging.getLogger('athenataf')
import time

from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase

class Stress(AthenaGUITestCase):
	'''
	Test class for Group Management.
	'''
	
	def test_ath_11752_switching_vcs_multiple_times(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_empty_group()
		
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller5()
	
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller()
	
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller5()
	
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller()
	
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller5()
		
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller()
	
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller5()
	
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller()
	
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller5()
		
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller()
		
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller5()
		
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller()
		
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller5()
		
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller()
		
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller5()
		
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller()
		
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller5()
		
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller()
		
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller5()
		
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller()
		
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.delete_empty_group()
		self.browser.refresh()