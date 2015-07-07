from athenataf.lib.functionality.test.SwitchConfigurationTest import SwitchConfigurationTest

class SwitchPage(SwitchConfigurationTest):
	'''
	Test class for switch configuration.
	'''
	def test_ath_7208_change_host_name_and_verify_config_push(self):
		'''
			This test case will not pass if we don't give the time.sleep()
		'''
		self.take_s1_snapshot()
		self.SwitchesPage.edit_switch()
		self.SwitchesPage.set_host_name(self.config.config_vars.host_name)
		self.SwitchesPage.save_switch_settings()
		self.SwitchesPage.edit_switch()
		self.SwitchesPage.set_host_name(self.config.config_vars.host_name1)
		self.SwitchesPage.save_switch_settings()
		self.take_s2_snapshot()
		self.SwitchesPage.edit_switch()
		self.SwitchesPage.set_host_name()
		self.SwitchesPage.save_switch_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	
	
		###################################################     NEW TESTCASES     ##################################################
	
	
	
	
	def test_ath_11558_verify_default_switch_configuration(self):
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		switch_page.assert_default_switch_configuration()
		
	def test_ath_11571_verify_ip_address_inputs_default_network(self):
		self1 = self.config.config_vars
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		switch_page.edit_switch()
		switch_page.set_ip_assignment('Static')
		switch_page.set_static_ipaddress_netmask_gateway(self1.ip_2,self1.netmask_2,self1.gateway_2)
		switch_page.assert_ip_netmask()
		
	def test_ath_11572_verify_ip_address_Inputs_loopback_ip(self):
		self1 = self.config.config_vars
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		switch_page.edit_switch()
		switch_page.set_ip_assignment('Static')
		switch_page.set_static_ipaddress_netmask_gateway(self1.ip_3,self1.netmask_2,self1.gateway_2)
		switch_page.assert_ip_netmask()
		
	def test_ath_11573_verify_ip_address_inputs_network_broadcast_ip(self):
		self1 = self.config.config_vars
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		switch_page.edit_switch()
		switch_page.set_ip_assignment('Static')
		switch_page.set_static_ipaddress_netmask_gateway(self1.ip_4,self1.netmask,self1.gateway_3)
		switch_page.assert_ip_netmask()
		
	def test_ath_11574_verify_ip_address_inputs_multicast_ip(self):
		self1 = self.config.config_vars
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		switch_page.edit_switch()
		switch_page.set_ip_assignment('Static')
		switch_page.set_static_ipaddress_netmask_gateway(self1.ip_5,self1.netmask,self1.gateway_3)
		switch_page.assert_ip_netmask()
		
	def test_ath_11568_verify_hostname_special_charecters(self):
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		self.take_s1_snapshot()
		switch_page.edit_switch()
		switch_page.set_host_name('@#$@')
		switch_page.save_switch_settings()
		switch_page.assert_hostname()
		self.take_s2_snapshot()
		switch_page.edit_switch()
		switch_page.set_host_name()
		switch_page.save_switch_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11575_verify_ip_address_inputs_all_octet_255(self):
		self1 = self.config.config_vars
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		switch_page.edit_switch()
		switch_page.set_ip_assignment('Static')
		switch_page.set_static_ipaddress_netmask_gateway(self1.netmask,self1.netmask,self1.gateway_3)
		switch_page.assert_ip_netmask()

	def test_ath_11576_verify_ip_address_inputs_octect_greater_than_255(self):
		self1 = self.config.config_vars
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		switch_page.edit_switch()
		switch_page.set_ip_assignment('Static')
		switch_page.set_static_ipaddress_netmask_gateway(self1.ip_6,self1.netmask,self1.gateway_3)
		switch_page.assert_ip_or_netmask('ip')
		
	def test_ath_11577_verify_subnet_mask_inputs_octet_greater_than_255(self):
		self1 = self.config.config_vars
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		switch_page.edit_switch()
		switch_page.set_ip_assignment('Static')
		switch_page.set_static_ipaddress_netmask_gateway(self1.ip_7,self1.netmask_1,self1.gateway_3)
		switch_page.assert_ip_or_netmask('netmask')

	def test_ath_11559_Verify_Switch_Configuration_with_DHCP_Enable(self):
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		switch_page.edit_switch()
		switch_page.set_ip_assignment('DHCP')
		switch_page.save_switch_settings()
		switch_page.assert_default_switch_configuration()
	
	def test_ath_11561_verify_hostname_inputs_string_max_length_63(self):
		self1 = self.config.config_vars
		self.take_s1_snapshot()
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		switch_page.edit_switch()
		switch_page.set_host_name(self1.host_name_2)
		switch_page.save_switch_settings()
		switch_page.edit_switch()
		switch_page.assert_max_string_hostname(self.config.config_vars.host_name_2)
		switch_page.save_switch_settings()
		self.take_s2_snapshot()
		switch_page.edit_switch()
		switch_page.set_host_name()
		switch_page.save_switch_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11562_verify_hostname_inputs_one_character_less_than_max_length(self):
		self1 = self.config.config_vars
		self.take_s1_snapshot()
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		switch_page.edit_switch()
		switch_page.set_host_name(self1.host_name_3)
		switch_page.save_switch_settings()
		switch_page.edit_switch()
		switch_page.assert_max_string_hostname(self.config.config_vars.host_name_3)
		switch_page.save_switch_settings()
		self.take_s2_snapshot()
		switch_page.edit_switch()
		switch_page.set_host_name()
		switch_page.save_switch_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11565_verify_hostname_inputs_spaces_in_text(self):
		self1 = self.config.config_vars
		self.take_s1_snapshot()
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		switch_page.edit_switch()
		switch_page.set_host_name(self1.host_name_4)
		switch_page.save_switch_settings()
		switch_page.edit_switch()
		switch_page.assert_max_string_hostname(self.config.config_vars.host_name_4)
		switch_page.save_switch_settings()
		self.take_s2_snapshot()
		switch_page.edit_switch()
		switch_page.set_host_name()
		switch_page.save_switch_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_11563_verify_hostname_inputs_one_character_greater_than_max_length(self):
		self1 = self.config.config_vars
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		switch_page.edit_switch()
		switch_page.set_host_name(self1.host_name_64)
		switch_page.save_switch_settings()
		switch_page.assert_invalid_hostname('maxlength')

		
	def test_ath_11564_verify_hostname_inputs_blank_or_null_string(self):
		self1 = self.config.config_vars
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		switch_page.edit_switch()
		switch_page.set_host_name(" ")
		switch_page.save_switch_settings()
		switch_page.assert_hostname('blank')
		
	def test_ath_11566_verify_hostname_input_ascii_charecters(self):
		'''
			Not present in excel waiting for clarification from switch team
		'''
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		self.take_s1_snapshot()
		switch_page.edit_switch()
		switch_page.set_host_name(self.config.config_vars.host_name_ascii.decode('utf-8'))
		switch_page.save_switch_settings()
		switch_page.edit_switch()
		switch_page.assert_max_string_hostname(self.config.config_vars.host_name_ascii.decode('utf-8'))
		switch_page.save_switch_settings()
		self.take_s2_snapshot()
		switch_page.edit_switch()
		switch_page.set_host_name()
		switch_page.save_switch_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11567_verify_hostname_unicode_charecters(self):
		'''
			Not present in excel waiting for clarification from switch team
		'''
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		self.take_s1_snapshot()
		switch_page.edit_switch()
		switch_page.set_host_name(self.config.config_vars.host_name_unicode.decode('utf-8'))
		switch_page.save_switch_settings()
		switch_page.edit_switch()
		switch_page.assert_max_string_hostname(self.config.config_vars.host_name_unicode.decode('utf-8'))
		switch_page.save_switch_settings()
		self.take_s2_snapshot()
		switch_page.edit_switch()
		switch_page.set_host_name()
		switch_page.save_switch_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11545_group_level_verify_modify_hostname(self):
		self1 = self.config.config_vars
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		self.take_s1_snapshot()
		switch_page.edit_switch()
		switch_page.set_host_name(self1.host_name_new)
		switch_page.save_switch_settings()
		switch_page.edit_switch()
		switch_page.assert_max_string_hostname(self1.host_name_new)
		switch_page.save_switch_settings()
		self.take_s2_snapshot()
		switch_page.edit_switch()
		switch_page.set_host_name()
		switch_page.save_switch_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11569_verify_hostname_japanese_characters(self):
		self1 = self.config.config_vars
		self.take_s1_snapshot()
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		switch_page.edit_switch()
		switch_page.set_host_name(self1.set_japanese_char.decode('utf-8'))
		switch_page.save_switch_settings()
		switch_page.edit_switch()
		switch_page.assert_max_string_hostname(self.config.config_vars.set_japanese_char.decode('utf-8'))
		switch_page.save_switch_settings()
		self.take_s2_snapshot()
		switch_page.edit_switch()
		switch_page.set_host_name()
		switch_page.save_switch_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11570_verify_hostname_german_characters(self):
		self1 = self.config.config_vars
		self.take_s1_snapshot()
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		switch_page.edit_switch()
		switch_page.set_host_name(self1.set_german_char.decode('utf-8'))
		switch_page.save_switch_settings()
		switch_page.edit_switch()
		switch_page.assert_max_string_hostname(self.config.config_vars.set_german_char.decode('utf-8'))
		switch_page.save_switch_settings()
		self.take_s2_snapshot()
		switch_page.edit_switch()
		switch_page.set_host_name()
		switch_page.save_switch_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11541_group_level_verify_mac_address_interface(self):
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		switch_page.verify_mac_address(self.config.config_vars.mac_address)
		
	def test_ath_11543_group_level_verify_hostname(self):
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		switch_page.edit_switch()
		switch_page.assert_max_string_hostname(self.config.config_vars.host_name)
		
	def test_ath_11550_device_level_verify_mac_address_interface(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_switch_device()
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		switch_page.verify_mac_address(self.config.config_vars.mac_address)
		
	def test_ath_11552_device_level_verify_hostname(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_switch_device()
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		switch_page.edit_switch()
		switch_page.assert_max_string_hostname(self.config.config_vars.host_name)	
		
	def test_ath_11554_device_level_verify_modify_hostname(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_switch_device()
		self1 = self.config.config_vars
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		self.take_s1_snapshot()
		switch_page.edit_switch()
		switch_page.set_host_name(self1.host_name_new)
		switch_page.save_switch_settings()
		switch_page.edit_switch()
		switch_page.assert_max_string_hostname(self1.host_name_new)
		switch_page.save_switch_settings()
		self.take_s2_snapshot()
		switch_page.edit_switch()
		switch_page.set_host_name()
		switch_page.save_switch_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_11578_verify_invalid_ip_subnet_mask_and_gateway_combination(self):
		'''
			Testcase not including in Excel sheet waiting to fix error
			Assert function is still remaining to call depending upon the error
		'''
		self1 = self.config.config_vars
		switch_page = self.LeftPanel.go_to_switch_configuration_switch()
		switch_page.edit_switch()
		switch_page.set_ip_assignment('Static')
		switch_page.set_static_ipaddress_netmask_gateway(self1.ip_8,self1.netmask_3,self1.gateway_4)
		# switch_page.assert_ip_netmask()
	
	
	
	
	
	