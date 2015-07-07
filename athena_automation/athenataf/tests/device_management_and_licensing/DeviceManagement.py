import logging
logger = logging.getLogger('athenataf')
import time

from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase

class DeviceManagement(AthenaGUITestCase):
	'''
	Test class for group management.
	'''
		
	def test_ath_7882_configure_group_with_member(self):
		device_mgmt = self.LeftPanel.go_to_device_management()
		self.browser.assert_element(device_mgmt.divice_vc,'VC s are not displayed')
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_device()
		if not self.LeftPanel.subscription_key_disabled and self.LeftPanel.device_management:
			raise AssertionError('subscription_key Link and device_management are displayed')
		self.clear()
		
	def test_ath_9172_upgrade_with_cbuild_firmware(self):
		firmware = self.LeftPanel.go_to_maintenance()
		firmware.upgrade_firmware_using_custom_build_option(self.config.config_vars.version_firmware,"IAP_1")

	def test_ath_9651_search_features(self):
		conf = self.config.config_vars
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		device_management_page = self.LeftPanel.go_to_device_management()
		device_management_page.search_device_mac_address_and_asserts()

	def test_ath_10797_assign_license_as_read_only_user_device_list_from_activate(self):
		conf = self.config.config_vars
		user_management_page=self.LeftPanel.go_to_user_management()
		user_management_page.delete_if_any_user_present()
		user_management_page.create_new_user(conf.email_read_only,conf.user_setting_group_value,conf.user_access_level_read_only)
		device_management_page = self.LeftPanel.go_to_device_management()
		device_management_page.search_device_using_mac_address()
		device_management_page.change_device1_to_unassigned()
		self.logout()
		self.login('read_only')
		device_management_page = self.LeftPanel.go_to_device_management()
		device_management_page.search_device_using_mac_address()
		device_management_page.change_device1_to_assigned()
		self.browser.assert_element(device_management_page.permission_denied_msg,'Permission Denied error message not found.')
		logger.debug("DeviceManagement Page: Cliking 'OK' button. ")
		device_management_page.ok_button.click()
		logger.debug("DeviceManagement Page: Cliking 'Close Assign PopUp'. ")
		device_management_page.close_assign_popup.click()
		
	def test_ath_10809_unassign_license_as_read_only_user_device_list_from_activate_license_and_group(self):
		conf = self.config.config_vars
		user_management_page=self.LeftPanel.go_to_user_management()
		user_management_page.delete_if_any_user_present()
		user_management_page.create_new_user(conf.email_read_only,conf.user_setting_group_value,conf.user_access_level_read_only)
		device_management_page = self.LeftPanel.go_to_device_management()
		device_management_page.search_device_using_mac_address()
		device_management_page.change_device1_to_assigned()
		self.browser.assert_element(device_management_page.unassigned_licence_text,'License is not set',False)
		if not device_management_page.group_text_group1:
			device_management_page.assign_already_created_group1()
			time.sleep(10)
		self.browser.refresh()
		device_management_page.search_device_using_mac_address()
		self.browser.assert_element(device_management_page.group_text_group1,'group1 is not assigned')
		self.logout()
		self.login('read_only')
		device_management_page = self.LeftPanel.go_to_device_management()
		device_management_page.search_device_using_mac_address()
		device_management_page.change_device1_to_unassigned()
		self.browser.assert_element(device_management_page.permission_denied_msg,'Permission Denied error message not found.')		
		logger.debug("DeviceManagement Page: Clicking 'OK' button. ")
		device_management_page.ok_button.click()
		time.sleep(4)
		
	def test_ath_10810_unassign_license_as_read_write_user_device_list_from_activate_license_and_group(self):
		conf = self.config.config_vars
		user_management_page=self.LeftPanel.go_to_user_management()
		user_management_page.delete_if_any_user_present()
		user_management_page.create_new_user(conf.email_read_write,conf.user_setting_group_value,conf.user_access_level_read_write)
		device_management_page = self.LeftPanel.go_to_device_management()
		device_management_page.search_device_using_mac_address()
		device_management_page.change_device1_to_assigned()
		self.browser.assert_element(device_management_page.unassigned_licence_text,'License is not set',False)
		if not device_management_page.group_text_group1:
			device_management_page.assign_already_created_group1()
		self.browser.assert_element(device_management_page.group_text_group1,'group1 is not assigned')
		self.logout()
		self.login('read_write')
		device_management_page = self.LeftPanel.go_to_device_management()
		device_management_page.search_device_using_mac_address()
		device_management_page.change_device1_to_unassigned()
		self.browser.assert_element(device_management_page.permission_denied_msg,'Permission Denied error message not found.')		
		logger.debug("DeviceManagement Page: Clicking 'OK' button. ")
		device_management_page.ok_button.click()
		
	def test_ath_10798_assign_license_as_read_write_user_device_list_from_activate(self):
		'''
		#bug
		'''
		conf = self.config.config_vars
		user_mgmt = self.LeftPanel.go_to_user_management()
		if not user_mgmt.assert_read_write_user():
			user_mgmt.create_new_user(conf.email_read_write, conf.user_setting_group_value, conf.access_level_read_write)
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.get_and_search_mac_address()
		device_mgmt.change_device1_to_unassigned()
		self.logout()
		self.login('read_write')
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.get_and_search_mac_address()
		device_mgmt.change_device1_to_assigned()
		device_mgmt.assert_unassigned_subscription_key()
		
		
	def test_ath_10800_assign_group_as_read_write_user_device_list_from_activate_license_assigned(self):
		'''
		#bug
		'''
		conf = self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		if not inner_left_panel.assert_group():
			group_page=inner_left_panel.add_group()
			group_page.create_multiple_empty_groups(conf.group_1)
		inner_left_panel.click_on_close_icon()
		user_mgmt = self.LeftPanel.go_to_user_management()
		if not user_mgmt.assert_read_write_user():
			user_mgmt.create_new_user(conf.email_read_write, conf.user_setting_group_value, conf.access_level_read_write)
		self.logout()
		self.login('read_write')
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.get_and_search_mac_address()
		if  device_mgmt.assert_unassigned_licence_text():
			device_mgmt.change_device1_to_assigned()
		device_mgmt.select_virtual_controller(device_mgmt.device_selector_1)
		device_mgmt.assign_group_to_device(device_mgmt.group1)
		device_mgmt.assert_group_name(conf.group_1)
	
	def test_ath_10805_add_group_as_read_write_user_from_assign_group_dialog(self):
		'''
		#bug
		'''
		conf = self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		if not inner_left_panel.assert_group():
			group_page=inner_left_panel.add_group()
			group_page.create_multiple_empty_groups(conf.group_1)
		inner_left_panel.click_on_close_icon()
		user_mgmt = self.LeftPanel.go_to_user_management()
		if not user_mgmt.assert_read_write_user():
			user_mgmt.create_new_user(conf.email_read_write, conf.user_setting_group_value, conf.access_level_read_write)
		self.logout()
		self.login('read_write')
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.get_and_search_mac_address()
		device_mgmt.select_virtual_controller(device_mgmt.device_selector_1)
		if  device_mgmt.assert_unassigned_licence_text():
			device_mgmt.change_device1_to_assigned
			device_mgmt.select_virtual_controller(device_mgmt.device_selector_1)
		device_mgmt.assign_group_to_device(device_mgmt.group1)
	
	
	def test_ath_10807_reassign_group_as_read_write_user_device_list_from_activate_license(self):
		'''
		#bug
		'''
		conf = self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		if not inner_left_panel.assert_group():
			group_page=inner_left_panel.add_group()
			group_page.create_multiple_empty_groups(conf.group_1)
		inner_left_panel.click_on_close_icon()
		user_mgmt = self.LeftPanel.go_to_user_management()
		if not user_mgmt.assert_read_write_user():
			user_mgmt.create_new_user(conf.email_read_write, conf.user_setting_group_value, conf.access_level_read_write)
		self.logout()
		self.login('read_write')
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.get_and_search_mac_address()
		device_mgmt.select_virtual_controller(device_mgmt.device_selector_1)
		if  device_mgmt.assert_unassigned_licence_text():
			device_mgmt.change_device1_to_assigned
			device_mgmt.select_virtual_controller(device_mgmt.device_selector_1)
		device_mgmt.assign_group_to_device(device_mgmt.group1)
		device_mgmt.assert_group_name(conf.group_1)
		
	def test_ath_10806_reassign_group_as_read_only_user_device_list_from_activate_license_and_group_assigned(self):
		conf = self.config.config_vars
		user_mgmt = self.LeftPanel.go_to_user_management()
		if not user_mgmt.assert_read_only_user():
			user_mgmt.create_new_user(conf.email_read_only, conf.user_setting_group_value, conf.access_level_read_only)
		self.logout()
		self.login('read_only')
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.get_and_search_mac_address()
		device_mgmt.select_virtual_controller(device_mgmt.device_selector_1)
		device_mgmt.select_assign_group()
		device_mgmt.default_group.click()
		device_mgmt.click_assign()
		device_mgmt.assert_permission_denied_message()
		device_mgmt.click_on_ok_button()
		
	def test_ath_10804_add_group_as_read_only_user_from_assign_group_dialog(self):
		conf = self.config.config_vars
		user_mgmt = self.LeftPanel.go_to_user_management()
		if not user_mgmt.assert_read_only_user():
			user_mgmt.create_new_user(conf.email_read_only, conf.user_setting_group_value, conf.access_level_read_only)
		self.logout()
		self.login('read_only')
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.get_and_search_mac_address()
		device_mgmt.select_virtual_controller(device_mgmt.device_selector_1)
		device_mgmt.select_assign_group()
		device_mgmt.create_group(conf.group_1)
		device_mgmt.assert_access_denied_message()
		device_mgmt.click_on_ok_button()
		
	def test_ath_4416_ui_check(self):
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.asserting_device_management_field()
		subscription_page = self.LeftPanel.go_to_subscription_keys()
		subscription_page.asserting_subscription_key_field()
		
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_default_group()
		firmware_page = self.LeftPanel.go_to_maintenance()
		firmware_page.asserting_device_management_and_subscription_key()
		
	def test_ath_4418_manually_add_devices_from_device_managment_page(self):
		conf = self.config.config_vars
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.adding_device(conf.activation_key,conf.device_mac_address)
		device_mgmt.asserting_device_exist_error_message()
		device_mgmt.clicking_calcel_button()
		
	def test_ath_8842_add_device_again(self):
		conf = self.config.config_vars
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.adding_device(conf.activation_key,conf.device_mac_address)
		device_mgmt.asserting_device_exist_error_message()
		device_mgmt.clicking_calcel_button()
		
	def test_ath_10812_assign_license_as_admin_user_manually_add_device(self):
		conf = self.config.config_vars
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.search_device_using_mac_address()
		device_mgmt.assert_device_as_unassisged()
		device_mgmt.assign_license_to_device()
		device_mgmt.assert_subscription_key()
		
	def test_ath_10813_assign_group_as_admin_user_manually_add_device_license_assigned(self):
		conf = self.config.config_vars
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.search_device_using_mac_address()
		device_mgmt.assert_device_as_assisged()
		device_mgmt.setting_device_as_unprovisioned()
		
		device_mgmt.select_assign_group()
		device_mgmt.set_assign_group(device_mgmt.default_group)
		device_mgmt.click_assign()
		device_mgmt.assert_group_name(device_mgmt.default_group)
		
	def test_ath_10796_assign_license_as_admin_user_device_list_from_activate(self):
		conf = self.config.config_vars
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.search_device_using_mac_address()
		device_mgmt.assert_device_as_unassisged()
		device_mgmt.assign_license_to_device()
		device_mgmt.assert_subscription_key()
		
	def test_ath_10801_assign_group_as_admin_user_device_list_from_activate_license_assigned(self):
		conf = self.config.config_vars
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.search_device_using_mac_address()
		device_mgmt.assert_device_as_assisged()
		device_mgmt.setting_device_as_unprovisioned()
		
		device_mgmt.select_assign_group()
		device_mgmt.set_assign_group(device_mgmt.default_group)
		device_mgmt.click_assign()
		device_mgmt.assert_group_name(device_mgmt.default_group)
		
	def test_ath_10803_add_group_as_admin_user_from_assign_group_dialog(self):
		conf = self.config.config_vars
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.search_device_using_mac_address()
		device_mgmt.assert_device_as_assisged()
		device_mgmt.adding_group(conf.grp_name)
		device_mgmt.assert_group_name(conf.grp_name)
		
		inner_left_panel = self.TopPanel.click_slider_icon()
		manage_group_page = inner_left_panel.manage_group()
		# manage_group_page.delete_current_working_group()
		
	def test_ath_10799_Assign_group_as_read_only_user_device_list_from_activate_license_assigned(self):
		conf = self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		if not inner_left_panel.assert_group():
			group_page=inner_left_panel.add_group()
			group_page.create_multiple_empty_groups(conf.group_1)
		inner_left_panel.click_on_close_icon()
		user_mgmt = self.LeftPanel.go_to_user_management()
		if not user_mgmt.assert_read_only_user():
			user_mgmt.create_new_user(conf.email_read_only, conf.user_setting_group_value, conf.access_level_read_only)
		self.logout()
		self.login('read_only')
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.get_and_search_mac_address()
		device_mgmt.select_virtual_controller(device_mgmt.device_selector_1)
		if  device_mgmt.assert_unassigned_licence_text():
			device_mgmt.change_device1_to_assigned()
			device_mgmt.select_virtual_controller(device_mgmt.device_selector_1)
		device_mgmt.assign_group_to_device(device_mgmt.group1)
		device_mgmt.assert_group_name(conf.group_1)
		inner_left_panel = self.TopPanel.click_slider_icon()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.delete_group1()	

	def test_ath_10808_reassign_as_admin_user_device_listfrom_activate_licence_and_group(self):
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.search_device_mac_address_and_asserts()
		device_mgmt.select_virtual_controller(device_mgmt.device_selector_1)
		device_mgmt.select_assign_group()
		device_mgmt.set_assign_group(device_mgmt.group1)
		logger.debug('DeviceManagement: Clicking on assign button')
		device_mgmt.assign.click()
		logger.debug('DeviceManagement: Clicking on ok button')
		device_mgmt.ok_button.click()
		device_mgmt.assert_group_name('group1')
		device_mgmt.select_virtual_controller(device_mgmt.device_selector_1)
		device_mgmt.select_assign_group()
		device_mgmt.set_assign_group(device_mgmt.default_group)
		logger.debug('DeviceManagement: Clicking on assign button')
		device_mgmt.assign.click()
		logger.debug('DeviceManagement: Clicking on ok button')
		device_mgmt.ok_button.click()

	def test_ath_10814_reassign_as_admin_user_device_listfrom_activate_licence_and_group(self):
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.search_device_mac_address_and_asserts()
		device_mgmt.select_virtual_controller(device_mgmt.device_selector_1)
		device_mgmt.select_assign_group()
		device_mgmt.set_assign_group(device_mgmt.group1)
		device_mgmt.click_assign()
		logger.debug('DeviceManagement: Clicking on ok button')
		device_mgmt.ok_button.click()
		device_mgmt.assert_group_name('group1')
		device_mgmt.select_virtual_controller(device_mgmt.device_selector_1)
		device_mgmt.select_assign_group()
		device_mgmt.set_assign_group(device_mgmt.default_group)
		device_mgmt.click_assign()
		logger.debug('DeviceManagement: Clicking on ok button')
		device_mgmt.ok_button.click()

	def test_ath_9738_guest_network_creation(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = vlan_obj.use_vlan_defaults()
		security.assert_default_wireless_guest_fields()
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_4419_Assign_more_devices_than_the_license_capacity(self):
		conf = self.config.config_vars
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.set_select_dropdown_value(conf.Unassigned)
		device_mgmt.click_select_button()
		device_mgmt.selec_deselect_all_devices(check=False)
		device_mgmt.assign_license_to_more_device()
		
	def test_ath_7974_add_device_from_an_existing_customer_in_same_cdp(self):
		conf = self.config.config_vars
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.adding_device(conf.activation_key_2,conf.device_mac_address_2)
		device_mgmt.search_device_using_mac_address_2(conf.device_mac_address_2)
		device_mgmt.change_device1_to_assigned()
		time.sleep(6)
		self.connect_device()
		self.browser.refresh()
		self.logout()
		self.login(email = conf.new_user_email_2,password = conf.new_user_passwd)
		time.sleep(10)
		device_mgmt.cancel_icon_2.click()
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.adding_device(conf.activation_key_2,conf.device_mac_address_2)
		device_mgmt.search_device_using_mac_address_2(conf.device_mac_address_2)
		device_mgmt.change_device1_to_assigned()
		time.sleep(6)
		self.connect_device()
		self.browser.refresh()
		
		
	def test_ath_7809_select_iap_devices_toggle_from_virtual_controller_to_switch_assign_license(self):
		conf = self.config.config_vars
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.search_device_using_mac_address_2(conf.device_mac_address_2)
		device_mgmt.change_device1_to_unassigned()
		device_mgmt.select_virtual_controller(device_mgmt.device_selector_1)
		device_mgmt.clicking_switch_tab()
		device_mgmt.assert_assign_button()
		device_mgmt.clicking_vc_tab()
		device_mgmt.change_device1_to_assigned_2()

	def test_ath_7966_order_processing_licensing_move_device_from_one_customer_to_other_without_unassigned_license(self):
		conf = self.config.config_vars
		device_mgmt = self.LeftPanel.go_to_device_management()
		# device_mgmt.adding_device(conf.activation_key_2,conf.device_mac_address_2)
		# device_mgmt.clicking_switch_tab()
		# device_mgmt.search_device_using_mac_address_2(conf.device_mac_address_2)
		# device_mgmt.change_device1_to_assigned()
		# time.sleep(6)
		# self.connect_device()
		# self.browser.refresh()
		self.logout()
		self.login(email = conf.new_user_email_3,password = conf.new_user_passwd)
		time.sleep(10)
		device_mgmt.cancel_icon_2.click()
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.adding_device(conf.activation_key_2,conf.device_mac_address_2)
		# device_mgmt.search_device_using_mac_address_2(conf.device_mac_address_2)
		# device_mgmt.change_device1_to_assigned()
		# time.sleep(6)
		# self.connect_device()
		# self.browser.refresh()

	def test_ath_7810_add_device_with_large_config_around_5300_lines_140k_bytes(self):
		conf = self.config.config_vars
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.adding_new_device()

		device_mgmt.search_device_using_mac_address_3()
		device_mgmt.assert_device_present_2()
		
	def test_ath_9438_add_slave_ap_to_the_layer_2iap_cluster(self):
		conf = self.config.config_vars
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.adding_device_to_server()
		self.connect_device()
		time.sleep(120)
		mac_ad = device_mgmt.get_mac_address_of_2device()
		self.click_on_search_icon()
		self.search_mac_address(mac_ad)
		self.click_on_search_button()
		device_mgmt.assert_device_is_present_or_not()
		monitoring_page = self.LeftPanel.go_to_monitoring_page()
		monitoring_page.navigate_to_all_ap()
		monitoring_page.asserts_aps_are_up()