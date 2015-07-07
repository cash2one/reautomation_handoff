import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase

class NegativeScenarios(AthenaGUITestCase):
	'''
	Test class for NegativeScenarios.
	'''
	def test_ath_11526_delete_default_group(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.delete_default_group()
		manage_group_page.assert_default_group_does_not_delete()
		manage_group_page.assert_group_has_swarm()
		manage_group_page.click_manage_group_close_button()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_empty_group()
		inner_left_panel.select_sample_group()
		self.TopPanel.click_slider_icon()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.delete_current_working_group()
		manage_group_page.assert_current_working_group_does_not_delete()
		manage_group_page.assert_group_has_swarm()
		manage_group_page.click_manage_group_close_button()
		manage_group_page.click_all_group_button()
		self.take_s2_snapshot()
		self.browser.refresh()
		inner_left_panel = self.TopPanel.click_slider_icon()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.delete_current_working_group()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()