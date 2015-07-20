import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase
from athenataf.lib.functionality.test.GroupConfigurationTest import GroupConfigurationTest

class FieldValidation(GroupConfigurationTest):
	'''
	Test class for FieldValidation.
	'''
	def test_ath_11529_check_help_text(self):
		self.Dashboard.enable_help()
		self.Dashboard.assert_help_option_for_all_groups_label()

			
	def test_ath_11528_group_name_validation(self):
		conf=self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_multiple_empty_groups(conf.group_name_with_spcl_char)
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_group_for_assertion(conf.invalid_group_name)
		create_group_page.assert_group_name_length_error()
		create_group_page.clicking_on_cancel_button()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_multiple_empty_groups(conf.group_name_starts_with_num)
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_multiple_empty_groups(conf.group_name_single_digit)
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_multiple_empty_groups(conf.group_name_single_alphabet)
		inner_left_panel.assert_valid_group_names()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_multiple_empty_groups(conf.group_name_starts_with_num)
		create_group_page.assert_duplicate_group_warning()
		manage_group_page=inner_left_panel.manage_group()
		manage_group_page.delete_four_empty_groups()
		
		
	def test_ath_11522_password_validation(self):
		conf=self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_group_for_assertion(conf.mynew)
		create_group_page.set_group_password(conf.abc)
		create_group_page.assert_password_field(visible = True,invisible = False)
		create_group_page.set_group_password(conf.char_33)
		create_group_page.assert_password_field(visible = True,invisible = False)
		create_group_page.set_group_password(conf.group_valid_password)
		create_group_page.assert_password_field(visible = False,invisible = True)
		create_group_page.click_cancel_group_button()
		inner_left_panel.add_group()
		create_group_page.create_group_for_assertion(conf.mynew)
		create_group_page.set_group_password(conf.group_valid_password)
		create_group_page.set_group_confirm_password(conf.confirm_invalid)
		create_group_page.assert_confirm_password_field(visible = False)
		self.browser.refresh()