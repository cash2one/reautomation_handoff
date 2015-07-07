import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.SwitchConfigurationTest import SwitchConfigurationTest

class System(SwitchConfigurationTest):
	'''
	Test class for switch configuration->System.
	'''

	def test_ath_9652_configure_and_verifydns_ip_at_group_level_and_switch_level(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		group_page=inner_left_panel.add_group()
		group_page.create_switch_group1()
		group_page.refresh()
		self.TopPanel.click_slider_icon()
		inner_left_panel.select_group1()
		self.take_s1_snapshot("show_dom")
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		system_page = self.LeftPanel.go_to_switch_configuration_system()	
		system_page.set_name_server(self.config.config_vars.name_server_1)
		system_page.save_setting()
		self.TopPanel.click_slider_icon()
		inner_left_panel.select_aruba_switch()
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		system_page = self.LeftPanel.go_to_switch_configuration_system()
		system_page.set_name_server(self.config.config_vars.name_server_2)
		system_page.save_setting()
		self.take_s2_snapshot("show_dom")
		group_page.refresh()
		self.TopPanel.click_slider_icon()	
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller3()
		inner_left_panel.select_all_group()
		self.TopPanel.click_slider_icon()
		manage_group_page = inner_left_panel.manage_group()	
		manage_group_page.delete_group1()
		self.take_s3_snapshot("show_dom")
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_6426_validate_admin_and_enable_fields_with_invalid_nputs(self):
		system_page = self.LeftPanel.go_to_switch_configuration_system()	
		system_page.set_admin_password(self.config.config_vars.admin)
		system_page.set_admin_confirm_password(self.config.config_vars.admin)	
		system_page.save_setting()
		system_page.assert_admin_password('Length error')
		system_page.assert_admin_confirm_password('Length error')
		system_page.cancel_settings()
		system_page.set_admin_password(self.config.config_vars.thirtythree_chars)
		system_page.set_admin_confirm_password(self.config.config_vars.thirtythree_chars)	
		system_page.save_setting()
		system_page.assert_admin_password('Length error')
		system_page.assert_admin_confirm_password('Length error')
		system_page.cancel_settings()
		system_page.set_enable_password(self.config.config_vars.thirtythree_chars)
		system_page.set_enable_confirm_password(self.config.config_vars.thirtythree_chars)	
		system_page.save_setting()
		system_page.assert_enable_password('Length error')
		system_page.assert_enable_confirm_password('Length error')
		system_page.cancel_settings()
		system_page.set_admin_password(self.config.config_vars.admin)
		system_page.set_admin_confirm_password(self.config.config_vars.admin)	
		system_page.set_enable_password(self.config.config_vars.admin)
		system_page.set_enable_confirm_password(self.config.config_vars.admin)	
		system_page.save_setting()
		system_page.assert_admin_password('Length error')
		system_page.assert_admin_confirm_password('Length error')
		system_page.cancel_settings()
		system_page.set_admin_password(self.config.config_vars.admin)
		system_page.save_setting()
		system_page.assert_admin_password('Mismatch')
		system_page.cancel_settings()
		system_page.set_admin_password(self.config.config_vars.admin)
		system_page.set_admin_confirm_password(self.config.config_vars.admin)	
		system_page.set_enable_password(self.config.config_vars.admin)
		system_page.set_enable_confirm_password(self.config.config_vars.admin)	
		system_page.cancel_settings()
		system_page.set_admin_password(self.config.config_vars.admin_space)
		system_page.set_admin_confirm_password(self.config.config_vars.admin_space)	
		system_page.save_setting()
		system_page.assert_admin_password('pattern mismatch')
		system_page.assert_admin_confirm_password('pattern mismatch')
		system_page.cancel_settings()
		system_page.set_admin_password(self.config.config_vars.admin_special_char)
		system_page.set_admin_confirm_password(self.config.config_vars.admin_special_char)	
		system_page.save_setting()
		system_page.assert_admin_password('pattern mismatch')
		system_page.assert_admin_confirm_password('pattern mismatch')
		system_page.cancel_settings()
		system_page.set_enable_password(self.config.config_vars.admin_special_char)
		system_page.set_enable_confirm_password(self.config.config_vars.admin_special_char)	
		system_page.save_setting()
		system_page.assert_enable_password('pattern mismatch')
		system_page.assert_enable_confirm_password('pattern mismatch')
		system_page.cancel_settings()
		