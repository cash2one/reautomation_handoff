from athenataf.lib.functionality.test.SwitchConfigurationTest import SwitchConfigurationTest

class DHCPPools(SwitchConfigurationTest):
	'''
	test class for DHCP pools
	'''
	def test_ath_9695_create_dhcp_pool_with_option_type_as_ip_and_cross_verify_on_switch(self):
		dhcp_obj = self.LeftPanel.go_to_switch_configuration_dhcp_pools()
		dhcp_obj.delete_dhcp()
		self.take_s1_snapshot("show_dhcp")
		dhcp_obj.create_new_dhcp_pool('test1','10.10.10.12','255.255.255.0','IP','None','None','None','None')
		self.take_s2_snapshot("show_dhcp")
		dhcp_obj.delete_dhcp()
		self.take_s3_snapshot("show_dhcp")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_9689_add_a_new_single_dhcp_pool(self):
		dhcp_obj = self.LeftPanel.go_to_switch_configuration_dhcp_pools()
		dhcp_obj.delete_dhcp()
		self.take_s1_snapshot("show_dhcp")
		dhcp_obj.create_new_dhcp_pool('test1','10.10.10.12','255.255.255.0','IP','None','None','None','None')
		self.take_s2_snapshot("show_dhcp")
		dhcp_obj.delete_dhcp()
		self.take_s3_snapshot("show_dhcp")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_9691_add_multiple_dhcp_pools_with_different_configurations(self):
		dhcp_obj = self.LeftPanel.go_to_switch_configuration_dhcp_pools()
		dhcp_obj.delete_dhcp()
		self.take_s1_snapshot("show_dhcp")
		dhcp_obj.create_new_dhcp_pool('test1','10.10.10.12','255.255.255.0','IP','None','None','None','None')
		dhcp_obj.create_new_dhcp_pool('test2','10.10.10.13','255.255.255.0','TEXT','None','None','None','None')
		dhcp_obj.create_new_dhcp_pool('test3','10.10.10.14','255.255.255.0','IP','None','None','None','None')
		dhcp_obj.create_new_dhcp_pool('test4','10.10.10.15','255.255.255.0','TEXT','None','None','None','None')
		self.take_s2_snapshot("show_dhcp")
		dhcp_obj.delete_dhcp()
		dhcp_obj.delete_dhcp()
		dhcp_obj.delete_dhcp()
		dhcp_obj.delete_dhcp()
		self.take_s3_snapshot("show_dhcp")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_9703_verify_duplication_functionality_by_creating_two_same_pools(self):
		dhcp_obj = self.LeftPanel.go_to_switch_configuration_dhcp_pools()
		dhcp_obj.delete_dhcp()
		self.take_s1_snapshot("show_dhcp")
		dhcp_obj.create_new_dhcp_pool('test1','10.10.10.12','255.255.255.0','IP','None','None','None','None')
		dhcp_obj.assert_dhcp_duplicate_creation()
		self.take_s2_snapshot("show_dhcp")
		dhcp_obj.delete_dhcp()
		self.take_s3_snapshot("show_dhcp")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
			
	def test_ath_9707_create_two_pool_one_with_dns_server_and_other_with_wins_server(self):
		dhcp_obj = self.LeftPanel.go_to_switch_configuration_dhcp_pools()
		dhcp_obj.delete_dhcp()
		self.take_s1_snapshot("show_dhcp")
		dhcp_obj.create_new_dhcp_pool('test1','10.10.10.12','255.255.255.0','IP','1.1.1.1','None','None','None')
		dhcp_obj.create_new_dhcp_pool('test2','10.10.10.13','255.255.255.0','IP','None','1.1.1.1','None','None')
		self.take_s2_snapshot("show_dhcp")
		dhcp_obj.delete_dhcp()
		dhcp_obj.delete_dhcp()
		self.take_s3_snapshot("show_dhcp")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_9688_verify_alll_the_ui_elements_existing_on_dhcp_page(self):
		dhcp_obj = self.LeftPanel.go_to_switch_configuration_dhcp_pools()
		dhcp_obj.assert_ui_elements_existing_on_dhcp_pools_page()

	def test_ath_9713_create_a_dhcp_pool_with_exclude_ip_address_range_other_than_pool_ip_subnet(self):
		dhcp_obj = self.LeftPanel.go_to_switch_configuration_dhcp_pools()
		dhcp_obj.delete_dhcp()
		self.take_s1_snapshot("show_dhcp")
		dhcp_obj.create_new_dhcp_pool('test1','10.10.10.12','255.255.255.0','IP','None','None','10.10.10.14','10.10.10.18')
		self.take_s2_snapshot("show_dhcp")
		dhcp_obj.delete_dhcp()
		self.take_s3_snapshot("show_dhcp")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_9705_create_dhcp_pool_without_profile_name(self):
		dhcp_obj = self.LeftPanel.go_to_switch_configuration_dhcp_pools()
		dhcp_obj.create_dhcp_pool_without_profile_name()

	def test_ath_9702_add_or_delete_when_dhcp_pool_service_is_enabled_and_disabled(self):
		dhcp_obj = self.LeftPanel.go_to_switch_configuration_dhcp_pools()
		dhcp_obj.delete_dhcp()
		self.take_s1_snapshot("show_dhcp")
		dhcp_obj.set_enable_dhcp_services('enable')
		dhcp_obj.save_setting()
		dhcp_obj.create_new_dhcp_pool('test1','10.10.10.12','255.255.255.0','IP','None','None','None','None')
		# dhcp_obj.save_setting()
		self.take_s2_snapshot("show_dhcp")
		dhcp_obj.delete_dhcp()
		dhcp_obj.set_enable_dhcp_services()
		dhcp_obj.save_setting()
		self.take_s3_snapshot("show_dhcp")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_9696_create_dhcp_pool_with_option_type_as_text(self):
		dhcp_obj = self.LeftPanel.go_to_switch_configuration_dhcp_pools()
		dhcp_obj.delete_dhcp()
		self.take_s1_snapshot("show_dhcp")
		dhcp_obj.create_new_dhcp_pool('test1','10.10.10.12','255.255.255.0','TEXT','None','None','None','None')
		self.take_s2_snapshot("show_dhcp")
		dhcp_obj.delete_dhcp()
		self.take_s3_snapshot("show_dhcp")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
				
	def test_ath_9699_verify_cancel_button_functionality(self):
		dhcp_obj = self.LeftPanel.go_to_switch_configuration_dhcp_pools()
		self.take_s1_snapshot("show_dhcp")
		dhcp_obj.cancel_button_functionality()
		self.take_s2_snapshot("show_dhcp")
		self.take_s3_snapshot("show_dhcp")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_9690_create_two_pool_one_with_dns_server_and_other_with_wins_server(self):
		dhcp_obj = self.LeftPanel.go_to_switch_configuration_dhcp_pools()
		self.take_s1_snapshot("show_dhcp")
		dhcp_obj.check_test2_exist()
		dhcp_obj.select_test2_edit_icon()
		dhcp_obj.edit_dhcp_pool('10.10.10.30','255.255.0.0')
		self.take_s2_snapshot("show_dhcp")
		dhcp_obj.delete_dhcp()
		self.take_s3_snapshot("show_dhcp")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_9706_create_dhcp_pool_which_includes_ip_address_in_execlude_ip_range(self):
		self1 = self.config.config_vars
		dhcp_obj = self.LeftPanel.go_to_switch_configuration_dhcp_pools()
		self.take_s1_snapshot("show_dhcp")
		dhcp_obj.create_new_dhcp_pool(self1.dhcp_name_5,self1.dhcp_network,self1.dhcp_netmask,'IP','None','None',self1.dhcp_network,self1.address_range)
		self.take_s2_snapshot("show_dhcp")
		dhcp_obj.delete_dhcp()
		self.take_s3_snapshot("show_dhcp")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()	
		
	def test_ath_9712_create_dhcp_pool_with_multiple_exclude_ip_ranges(self):
		self1 = self.config.config_vars
		dhcp_obj = self.LeftPanel.go_to_switch_configuration_dhcp_pools()
		self.take_s1_snapshot("show_dhcp")
		dhcp_obj.create_dhcp_pool_with_multiple_exclude_ip('test2','10.10.10.11','255.255.255.0')
		self.take_s2_snapshot("show_dhcp")
		dhcp_obj.delete_dhcp()
		self.take_s3_snapshot("show_dhcp")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_9692_delete_a_dhcp_pool(self):
		dhcp_obj = self.LeftPanel.go_to_switch_configuration_dhcp_pools()
		dhcp_obj.delete_dhcp()
		self.take_s1_snapshot("show_dhcp")
		dhcp_obj.create_new_dhcp_pool('test1','10.10.10.12','255.255.255.0','IP','None','None','None','None')
		self.take_s2_snapshot("show_dhcp")
		dhcp_obj.delete_dhcp()
		self.take_s3_snapshot("show_dhcp")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_9709_create_dhcp_pool_with_nine_dns_ip_address_and_wins_server(self):
		dhcp_obj = self.LeftPanel.go_to_switch_configuration_dhcp_pools()
		dhcp_obj.delete_dhcp()
		self.take_s1_snapshot()
		dhcp_obj.create_new()
		dhcp_obj.set_profile_name('test')
		dhcp_obj.crate_dhcp_with_multiple_dns_server()
		dhcp_obj.crate_dhcp_with_multiple_wins_server()
		dhcp_obj.save_dhcp_pool()
		self.take_s2_snapshot()
		dhcp_obj.delete_dhcp()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_9708_create_dhcp_pool_with_nine_dns_server(self):
		dhcp_obj = self.LeftPanel.go_to_switch_configuration_dhcp_pools()
		dhcp_obj.delete_dhcp()
		self.take_s1_snapshot()
		dhcp_obj.create_new()
		dhcp_obj.set_profile_name('test')
		dhcp_obj.crate_dhcp_with_multiple_dns_server()
		dhcp_obj.save_dhcp_pool()
		self.take_s2_snapshot()
		dhcp_obj.delete_dhcp()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_9693_enable_and_disable_dhcp_service(self):
		dhcp_obj = self.LeftPanel.go_to_switch_configuration_dhcp_pools()
		dhcp_obj.delete_dhcp()
		self.take_s1_snapshot("show_dhcp")
		dhcp_obj.set_enable_dhcp_services('enable')
		dhcp_obj.save_setting()
		self.take_s2_snapshot("show_dhcp")
		dhcp_obj.set_enable_dhcp_services()
		dhcp_obj.save_setting()
		self.take_s3_snapshot("show_dhcp")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_9697_delete_vlan_having_NAT_enabled(self):
		self1 = self.config.config_vars
		vpn_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vpn_obj.delete_default_vlan()
		self.take_s1_snapshot("show_dhcp")		
		vpn_obj.creating_vlan()
		dhcp_obj = self.LeftPanel.go_to_switch_configuration_dhcp_pools()
		dhcp_obj.delete_dhcp()
		dhcp_obj.create_new_dhcp_pool(self1.set_description,self1.set_ip_address,self1.set_net_mask,'IP','None','None','None','None')
		dhcp_obj.create_new_dhcp_pool('test2','192.168.10.10','255.255.0.0','IP','None','None','None','None')
		self.take_s2_snapshot("show_dhcp")		
		dhcp_obj.delete_dhcp()
		dhcp_obj.delete_dhcp()
		vpn_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vpn_obj.delete_default_vlan()
		self.take_s3_snapshot("show_dhcp")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()		
		
	def test_ath_9694_validate_all_elements_existing_on_DHCP_pools_page(self):
		dhcp_obj = self.LeftPanel.go_to_switch_configuration_dhcp_pools()
		dhcp_obj.create_dhcp_pool_without_profile_name()
		dhcp_obj.cancel_button()
		dhcp_obj.validate_all_elememt_of_dhcp_page()
		dhcp_obj.asssert_all_element_of_dhcp_page()
				
		
		
		