import logging
logger = logging.getLogger('athenataf')
import time

from athenataf.lib.functionality.test.DeviceManagementTest import DeviceManagementTest
from athenataf.lib.functionality.common import DeviceLibrary

class EnhancedZtp(DeviceManagementTest):
	'''
	Test class for group management Enhanced Ztp.
	'''		
		
	def test_ath_10822_device_move_from_default_group_to_another_group(self):
		conf = self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		if inner_left_panel.assert_group_is_present_or_not(inner_left_panel.group1_with_vc):
			manage_group = inner_left_panel.manage_group()
			manage_group.move_virtual_controller_from_Mygroup(group1=True)
			manage_group = inner_left_panel.manage_group()
			manage_group.delete_group1()
		elif inner_left_panel.assert_group_is_present_or_not(inner_left_panel.group1_without_vc):
			manage_group = inner_left_panel.manage_group()
			manage_group.delete_group1()
		elif inner_left_panel.assert_group_2():
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_empty_group2()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_group1()
		inner_left_panel.click_on_close_icon()
		# device_management_page = self.LeftPanel.go_to_device_management()
		# device_management_page.search_device_mac_address_and_asserts()
		# device_management_page.assert_assigned_group1()
		import time
		time.sleep(20)
		inner_left_panel = self.TopPanel.click_slider_icon()
		if inner_left_panel.assert_group_is_present_or_not(inner_left_panel.group1_with_vc):
			manage_group = inner_left_panel.manage_group()
			manage_group.move_virtual_controller_from_Mygroup(group1=True)
			manage_group = inner_left_panel.manage_group()
			manage_group.delete_group1()
		elif inner_left_panel.assert_group_is_present_or_not(inner_left_panel.group1_without_vc):
			manage_group = inner_left_panel.manage_group()
			manage_group.delete_group1()
		elif inner_left_panel.assert_group_2():
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_empty_group2()
				
				
	def test_ath_10815_unassign_license_as_admin_user_manually_add_device_license_and_group_assigned(self):
		conf = self.config.config_vars
		device_management_page = self.LeftPanel.go_to_device_management()
		device_management_page.get_and_search_mac_address()
		device_management_page.change_device1_to_unassigned()
		device_management_page.assert_device_unassigned()
		# device_management_page.assert_group_name('')
		
	def test_ath_10802_assign_group_as_admin_user_device_list_from_activate_license_not_assigned(self):
		conf = self.config.config_vars
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.get_and_search_mac_address()
		device_mgmt.change_device1_to_unassigned()
		device_mgmt.assert_device_as_unassisged()
		device_mgmt.assign_already_created_group1()
		
	def test_ath_10816_unassign_license_as_admin_user_manually_add_device_license_and_group_assigned(self):
		conf = self.config.config_vars
		# inner_left_panel = self.TopPanel.click_slider_icon()
		# if inner_left_panel.assert_group_is_present_or_not(inner_left_panel.group1_with_vc):
			# manage_group = inner_left_panel.manage_group()
			# manage_group.move_virtual_controller_from_Mygroup(group1=True)
			# manage_group = inner_left_panel.manage_group()
			# manage_group.delete_group1()
		# elif inner_left_panel.assert_group_is_present_or_not(inner_left_panel.group1_without_vc):
			# manage_group = inner_left_panel.manage_group()
			# manage_group.delete_group1()
		# elif inner_left_panel.assert_group_2():
			# manage_group_page = inner_left_panel.manage_group()
			# manage_group_page.delete_empty_group2()
		# create_group_page = inner_left_panel.add_group()
		# create_group_page.create_group1()
		# inner_left_panel.click_on_close_icon()
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.get_and_search_mac_address()
		device_mgmt.change_device1_to_assigned()
		# if device_mgmt.assert_assigned_group1_label:
			# device_mgmt.assign_default_group()	
		# else:
		device_mgmt.assign_already_created_group1()
		device_mgmt.change_device1_to_unassigned()
		device_mgmt.assert_device_unassigned()
		
	def test_ath_10811_unassign_license_as_admin_user_device_license_and_group_assigned(self):
		conf = self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		if inner_left_panel.assert_group_is_present_or_not(inner_left_panel.group1_with_vc):
			manage_group = inner_left_panel.manage_group()
			manage_group.move_virtual_controller_from_Mygroup(group1=True)
			manage_group = inner_left_panel.manage_group()
			manage_group.delete_group1()
		elif inner_left_panel.assert_group_is_present_or_not(inner_left_panel.group1_without_vc):
			manage_group = inner_left_panel.manage_group()
			manage_group.delete_group1()
		elif inner_left_panel.assert_group_2():
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_empty_group2()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_group1()
		inner_left_panel.click_on_close_icon()
		device_mgmt = self.LeftPanel.go_to_device_management()
		device_mgmt.get_and_search_mac_address()
		device_mgmt.change_device1_to_assigned()
		# if device_mgmt.assert_assigned_group1_label:
			# device_mgmt.assign_default_group()	
		# else:
		device_mgmt.assign_already_created_group1()
		device_mgmt.change_device1_to_unassigned()
		device_mgmt.assert_device_unassigned()
		device_mgmt.get_and_search_mac_address()
		device_mgmt.change_device1_to_assigned()
		
	def test_ath_10821_device_move_from_preconfigured_group_to_another_group(self):
		conf = self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		if inner_left_panel.assert_group_is_present_or_not(inner_left_panel.group1_with_vc):
			manage_group = inner_left_panel.manage_group()
			manage_group.move_virtual_controller_from_Mygroup(group1=True)
			manage_group = inner_left_panel.manage_group()
			manage_group.delete_group1()
		elif inner_left_panel.assert_group_is_present_or_not(inner_left_panel.group1_without_vc):
			manage_group = inner_left_panel.manage_group()
			manage_group.delete_group1()
		elif inner_left_panel.assert_group_2():
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_empty_group2()
		create_group_page = inner_left_panel.add_group()
		create_group_page.create_group1()
		inner_left_panel.click_on_close_icon()
		# device_management_page = self.LeftPanel.go_to_device_management()
		# device_management_page.search_device_mac_address_and_asserts()
		# device_management_page.assert_assigned_group1()
		inner_left_panel = self.TopPanel.click_slider_icon()
		if inner_left_panel.assert_group_is_present_or_not(inner_left_panel.group1_with_vc):
			manage_group = inner_left_panel.manage_group()
			manage_group.move_virtual_controller_from_Mygroup(group1=True)
			manage_group = inner_left_panel.manage_group()
			manage_group.delete_group1()
		elif inner_left_panel.assert_group_is_present_or_not(inner_left_panel.group1_without_vc):
			manage_group = inner_left_panel.manage_group()
			manage_group.delete_group1()
		elif inner_left_panel.assert_group_2():
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_empty_group2()
		inner_left_panel.click_on_close_icon()
	
	def test_ath_10825_swarm_login_master_and_slave_preconfigured_in_same_group(self):
		device_management_page = self.LeftPanel.go_to_device_management()
		device_management_page.get_and_search_mac_address()
		if not device_management_page.assert_device_present():
			device_mgmt.adding_device(conf.activation_key,conf.device_mac_address)
			device_management_page.get_and_search_mac_address()
		device_management_page.change_device1_to_assigned()
		self.connect_device()
		self.browser.refresh()
		inner_left_panel = self.TopPanel.click_slider_icon()
		logger.debug('InnerLeftPanel: Clicking on expand button')
		inner_left_panel.expand_group_icon.click()
		logger.debug('InnerLeftPanel: Asserting swarm displayed in group as single single virtual controller')
		if not inner_left_panel.virtual_controller_with_one_vc:
			raise AssertionError('The swarm is not displayed in the group as single virtual controller.')

	def test_ath_10818_device_login_licensed_Preconfigured_no_group_assigned(self):
		device_management_page = self.LeftPanel.go_to_device_management()
		DeviceLibrary.disconnect_device_from_server("IAP_1")
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_all_group()
		device_management_page.get_and_search_mac_address()
		if not device_management_page.assert_device_present():
			device_mgmt.adding_device(conf.activation_key,conf.device_mac_address)
			device_management_page.get_and_search_mac_address()
		device_management_page.change_device1_to_assigned()
		DeviceLibrary.connect_device_to_server("IAP_1")
	
	def test_ath_10820_device_login_licensed_preconfigured_group_preconfigured(self):
		device_management_page = self.LeftPanel.go_to_device_management()
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_all_group()
		device_management_page.get_and_search_mac_address()
		if not device_management_page.assert_device_present():
			device_mgmt.adding_device(conf.activation_key,conf.device_mac_address)
			device_management_page.get_and_search_mac_address()
		device_management_page.change_device1_to_assigned()
		device_management_page.assign_default_group()
		
		
	def test_ath_10817_device_login_licensed_factory_defaulted_no_group_assigned(self):
		conf = self.config.config_vars
		device_management_page = self.LeftPanel.go_to_device_management()
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_all_group()
		device_management_page.get_and_search_mac_address()
		if not device_management_page.assert_device_present():
			device_management_page.adding_device(devices.IAP_1.activation_id,devices.IAP_1.mac_address)
			import time
			time.sleep(10)
			device_management_page.get_and_search_mac_address()
		device_management_page.change_device1_to_assigned()
		# if not device_management_page.non_preconfigured_group:
			# device_management_page.assign_default_group()
		self.factory_reset()
		self.connect_device()
		self.browser.refresh()
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.assert_device_present_in_default_group()
		
	def test_ath_10819_Device_login_licensed_factory_defaulted_group_preconfigured(self):
		device_management_page = self.LeftPanel.go_to_device_management()
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_all_group()
		device_management_page.get_and_search_mac_address()
		if not device_management_page.assert_device_present():
			device_management_page.adding_device(devices.IAP_1.activation_id,devices.IAP_1.mac_address)
			import time
			time.sleep(10)
			device_management_page.get_and_search_mac_address()
		device_management_page.change_device1_to_assigned()
		if not device_management_page.non_preconfigured_group:
			device_management_page.assign_default_group()
		self.factory_reset()
		self.connect_device()
		self.browser.refresh()
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.assert_device_present_in_default_group()
	
	def test_ath_10823_device_move_from_unprovisioned_group_to_preconfigured_group(self):
		conf = self.config.config_vars
		# self.factory_reset()
		inner_left_panel = self.TopPanel.click_slider_icon()
		if inner_left_panel.assert_group_is_present_or_not(inner_left_panel.group1_with_vc):
			manage_group = inner_left_panel.manage_group()
			manage_group.move_virtual_controller_between_two_groups(manage_group.group1, manage_group.move_to_group1)
			manage_group = inner_left_panel.manage_group()
			manage_group.delete_group1()
		if  inner_left_panel.assert_group_is_present_or_not(inner_left_panel.group1_without_vc):
			manage_group = inner_left_panel.manage_group()
			manage_group.delete_group1()
		if inner_left_panel.assert_group_2():
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_empty_group2()
		inner_left_panel.select_unprovision_iap()
		create_group_page = inner_left_panel.click_configuration_page_new_group_button()
		create_group_page.create_unprovision_iap_group1(conf.group_1)
		device_management_page = self.LeftPanel.go_to_device_management()
		device_management_page.get_and_search_mac_address()
		if not device_management_page.assert_device_present():
			raise AssertionError('Mac address is not present')
		self.connect_device()
		self.browser.refresh()
		if not device_management_page.group_text_group1:
			raise AssertionError('Device Management : IAP is not moved to group1 successfully')
		if inner_left_panel.assert_group_is_present_or_not(inner_left_panel.group1_with_vc):
			manage_group = inner_left_panel.manage_group()
			manage_group.move_virtual_controller_between_two_groups(manage_group.group1, manage_group.move_to_group1)
			manage_group = inner_left_panel.manage_group()
			manage_group.delete_group1()
		if  inner_left_panel.assert_group_is_present_or_not(inner_left_panel.group1_without_vc):
			manage_group = inner_left_panel.manage_group()
			manage_group.delete_group1()
		if inner_left_panel.assert_group_2():
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_empty_group2()
			
	def test_ath_10824_device_move_from_unprovisioned_group_to_other_than_opreconfigured_group(self):
		conf = self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		create_group_page = inner_left_panel.add_group()
		create_group_page.set_group_name(conf.group_1)
		create_group_page.move_next()
		create_group_page._set_group_default_device_password1()
		create_group_page = inner_left_panel.add_group()
		create_group_page.set_group_name(conf.group_2)
		create_group_page.move_next()
		create_group_page._set_group_default_device_password1()
		
		device_management_page = self.LeftPanel.go_to_device_management()
		device_management_page.get_and_search_mac_address()
		if not device_management_page.assert_device_present():
			raise AssertionError('Mac address is not present')
		device_management_page.select_virtual_controller(device_management_page.device_selector_1)	
		device_management_page.select_assign_group()
		device_management_page.set_assign_group(device_management_page.group1)
		device_management_page.click_assign()
		self.connect_device()
		self.browser.refresh()
		device_management_page.select_virtual_controller(device_management_page.device_selector_1)	
		device_management_page.select_assign_group()
		device_management_page.set_assign_group(device_management_page.group2)
		device_management_page.click_assign()
		self.connect_device()
		
		self.browser.refresh()
		inner_left_panel = self.TopPanel.click_slider_icon()
		logger.debug('Expanding group1')
		inner_left_panel.group2_expand_icon.click()
		if not inner_left_panel.mac_24_de_c6_cb_7c_80:
			raise AssertionError('Moving of device from unprovisioned group to preconfigured group is not successful')	
	
	def test_ath_10826_Swarm_Login_Master_and_slave_preconfigured_in_different_groups(self):
		conf = self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.delete_group1()

		inner_left_panel.manage_group()
		manage_group_page.delete_group2()
		create_group_page = inner_left_panel.add_group()
		create_group_page.set_group_name(conf.group_1)
		create_group_page.move_next()
		create_group_page._set_group_default_device_password1()
		create_group_page = inner_left_panel.add_group()
		create_group_page.set_group_name(conf.group_2)
		create_group_page.move_next()
		create_group_page._set_group_default_device_password1()
		'''
		search master slave assign groups
		'''
		device_management_page = self.LeftPanel.go_to_device_management()
		device_management_page.search_device_and_add_if_not_exist(conf.master_mac,conf.master_activation_key)
		device_management_page.change_device1_to_assigned()
		device_management_page.assign_already_created_group1()
		device_management_page.search_device_and_add_if_not_exist(conf.slave_mac,conf.slave_activation_key)
		device_management_page.change_device1_to_assigned_2()
		device_management_page.assign_already_created_group2()
		self.connect_device()
		self.browser.refresh()
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_group1()
		access_point = self.LeftPanel.go_to_monitoring_access_points()
		access_point.assert_mac_address(access_point.master_vc)
		access_point.assert_mac_address(access_point.slave_vc)