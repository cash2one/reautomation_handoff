import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class NegativeScenarios(ConfigurationTest):
	'''
	Test class for Employee Security Level Personal testcases.
	'''

	def test_ath_9034_upload_captive_portal_image_file_which_contains_space_in_the_filename(self):
		conf = self.config.config_vars
		innerleftpanel = self.TopPanel.click_slider_icon()
		innerleftpanel.select_device()
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.click_on_next()
		security.set_splash_page_type_value(conf.Splash_page_Acknowledged)
		logger.debug('SecurityPage : Clicking on upload button')
		fu = self.get_file_uploader(conf.logo_file_name_with_space)
		fu.start()
		security.logo_upload.click()
		fu.join()
		logger.debug('SecurityPage : Asserting logo preview image')
		self.browser.assert_element(security.logo_preview,'Logo preview image is not displayed')
		logger.debug('SecurityPage : Asserting logo change button')
		self.browser.assert_element(security.change_logo,'Logo change button is not displayed')
		logger.debug('SecurityPage : Asserting logo delete button')
		self.browser.assert_element(security.delete_logo,'Logo delete button is not displayed')
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8879_verify_an_iap_configured_with_captive_portal_logo_disconnects_from_athena(self):
		conf=self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		if inner_left_panel.assert_group1_and_group2():
			if inner_left_panel.assert_sample_group_with_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.move_virtual_controller_from_Mygroup(group1=True)
				inner_left_panel.manage_group()
				manage_group_page.delete_specific_group(group1=True)
				
			if inner_left_panel.assert_sample_group_with_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.move_virtual_controller_from_Mygroup(group2=True)
				inner_left_panel.manage_group()
				manage_group_page.delete_specific_group(group2=True)
				
		# self.take_s1_snapshot()
		# inner_left_panel = self.TopPanel.click_slider_icon()
		create_group_page = inner_left_panel.add_group()
		create_group_page.set_group_name(conf.group_1)
		create_group_page.select_virtual_controller(create_group_page.select_vc)
		create_group_page.move_next()
		create_group_page._set_group_default_device_password1()
		inner_left_panel.select_group(inner_left_panel.group_1)
		inner_left_panel.select_group1()
		network_page = self.LeftPanel.go_to_network_page()
		basic_info = network_page.create_new_network()
		virtual_lan = basic_info.guest_network_info_with_specific_name(conf.guest_network_1)
		security = virtual_lan.use_vlan_defaults()
		# fu = self.get_file_uploader(conf.logo_path)
		# fu.start()
		# security.logo_upload.click()
		# fu.join()
		access = security.click_on_next()
		access.finish_network_setup()
		
		inner_left_panel = self.TopPanel.click_slider_icon()
		create_group_page = inner_left_panel.add_group()
		create_group_page.set_group_name(conf.group_2)
		create_group_page.select_virtual_controller(create_group_page.select_vc1)
		create_group_page.move_next()
		create_group_page._set_group_default_device_password1()
		inner_left_panel.select_group(inner_left_panel.group_2)
		inner_left_panel.select_group2()
		network_page = self.LeftPanel.go_to_network_page()
		basic_info = network_page.create_new_network()
		virtual_lan = basic_info.guest_network_info_with_specific_name(conf.guest_network_2)
		security = virtual_lan.use_vlan_defaults()
		# fu = self.get_file_uploader(conf.logo_path)
		# fu.start()
		# security.logo_upload.click()
		# fu.join()
		access = security.click_on_next()
		access.finish_network_setup
		
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.default_group.click()
		
		inner_left_panel = self.TopPanel.click_slider_icon()
		if inner_left_panel.assert_group1_and_group2():
			if inner_left_panel.assert_sample_group_with_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.move_virtual_controller_from_Mygroup(group1=True)
				inner_left_panel.manage_group()
				manage_group_page.delete_specific_group(group1=True)
				
			if inner_left_panel.assert_sample_group_with_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.move_virtual_controller_from_Mygroup(group2=True)
				inner_left_panel.manage_group()
				manage_group_page.delete_specific_group(group2=True)
		self.take_s2_snapshot()        
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8878_verify_an_iap_configured_with_captive_portal_logo_disconnects_from_athena_and_reconnects_to_same_group(self):
		conf = self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		if inner_left_panel.assert_group():
			if inner_left_panel.assert_mygroup_with_vc_present():
				inner_left_panel.select_group1()
				self._delete_guest_nw()
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.move_virtual_controller_group1()
				inner_left_panel.manage_group()	
				manage_group_page.delete_group1()
			elif inner_left_panel.assert_sample_group_without_vc_present():
				inner_left_panel.select_group1()
				self._delete_guest_nw()
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.delete_group1()
		if inner_left_panel.assert_group_2():
			inner_left_panel.select_group2()
			self._delete_guest_nw()
			manage_group_page = inner_left_panel.manage_group()
			manage_group_page.delete_empty_group2()
		self.take_s1_snapshot()
		'''
		Creates Guest-Nw1 in Group1 and uploading logo in SecurityPage
		'''
		group_page=inner_left_panel.add_group()
		group_page.create_group_with_vc1(conf.group_1)
		inner_left_panel.select_group1()
		self.LeftPanel.go_to_network_page()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info_with_specific_name(conf.guest_nw1)
		security = vlan_obj.use_vlan_defaults()
		security.set_splash_page_type_value(conf.Splash_page_Acknowledged)
		logger.debug('SecurityPage : Clicking on upload button')
		fu = self.get_file_uploader(conf.logo1)
		fu.start()
		security.logo_upload.click()
		fu.join()
		logger.debug('SecurityPage : Clicking on save button')
		security.save_button.click()
		access = security.click_on_next()
		access.finish_network_setup()
		'''
		Creates Guest-Nw2 in Group2 and uploading logo in SecurityPage
		'''
		inner_left_panel = self.TopPanel.click_slider_icon()
		group_page=inner_left_panel.add_group()
		group_page.create_multiple_empty_groups(conf.group_2)
		inner_left_panel.select_group2()
		self.LeftPanel.go_to_network_page()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info_with_specific_name(conf.guest_nw2)
		security = vlan_obj.use_vlan_defaults()
		security.set_splash_page_type_value(conf.Splash_page_Acknowledged)
		logger.debug('SecurityPage : Clicking on upload button')
		fu = self.get_file_uploader(conf.logo1)
		fu.start()
		security.logo_upload.click()
		fu.join()
		logger.debug('SecurityPage : Clicking on save button')
		security.save_button.click()
		access = security.click_on_next()
		access.finish_network_setup()
		self.connect_device()
		self.take_s2_snapshot()
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_group1()
		self._delete_guest_nw()
		inner_left_panel.select_group2()
		self._delete_guest_nw()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.move_virtual_controller_group1()
		inner_left_panel.manage_group()	
		manage_group_page.delete_group1()
		manage_group_page = inner_left_panel.manage_group()
		manage_group_page.delete_empty_group2()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def _delete_guest_nw(self):
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_guest_nw1_if_present()
		network_page.delete_guest_nw2_if_present()
		self.TopPanel.go_to_allgroups()
		inner_left_panel = self.TopPanel.click_slider_icon()