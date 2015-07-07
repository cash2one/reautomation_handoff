import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase

class UserAccountSettings(AthenaGUITestCase):
	'''
	Test class to validate the user maintenance info
	'''

	def test_ath_8214_validate_user_interface(self):
		self.TopPanel.validate_user_interface()
		self.TopPanel.setting_default_value()

	def test_ath_8219_validate_time_zone(self):
		self.TopPanel.validate_time_zone()

	def test_ath_8220_validate_idle_timeout(self):
		self.TopPanel.validate_idle_timeout()
		self.TopPanel.setting_default_value()

	def test_ath_8217_login_Logout(self):
		self.logout()
		self.login('default')
		
	def test_ath_8218_login_Logout(self):
		conf = self.config.config_vars
		user_management_page=self.LeftPanel.go_to_user_management()
		user_management_page.delete_if_any_user_present()
		user_management_page.create_new_user(conf.email_read_write,conf.user_setting_group_value,conf.user_access_level_read_write)
		self.logout()
		self.login('read_write')
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.assert_virtual_controller()
		inner_left_panel.click_on_close_icon()
