import logging
from __main__ import time
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.SwitchConfigurationTest import SwitchConfigurationTest

class VLANS(SwitchConfigurationTest):
	'''
	Test class for VLANS.
	'''

	def test_ath_6413_edit_an_existing_vlan(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot("show_vlan")		
		vlan_obj.creating_vlan()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.changing_access_vlan_value()
		vpn_obj1 = self.LeftPanel.go_to_switch_configuration_vlans()
		vpn_obj1.change_default_vlan_value()
		self.take_s2_snapshot("show_vlan")
 
		vlan_obj.delete_default_vlan()
		port_obj1 = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj1.set_default_access_vlan_value()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_6412_create_new_vlan_and_cross_verify(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot("show_vlan")	
		vlan_obj.creating_vlan()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.changing_access_vlan_value()
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		self.take_s2_snapshot("show_vlan")
		vlan_obj.delete_default_vlan()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.set_default_access_vlan_value()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()


	def test_ath_6414_delete_existing_vlan_and_cross_verify(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot("show_vlan")
		vlan_obj.creating_vlan()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.changing_access_vlan_value()
		self.take_s2_snapshot("show_vlan")	
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.set_default_access_vlan_value()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()


	def test_ath_6415_add_long_description_to_existing_VLAN_and_verify(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot("show_vlan")
		vlan_obj.creating_vlan()
		vlan_obj.verify_existing_vlan_description(self.config.config_vars.description_32_char)
		vlan_obj.verify_existing_vlan_description(self.config.config_vars.description_digit)
		vlan_obj.verify_existing_vlan_description(self.config.config_vars.description_spl_char)
		vlan_obj.verify_existing_vlan_description(self.config.config_vars.description_char_combination)
		self.take_s2_snapshot("show_vlan")
		vlan_obj._delete_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()


	def test_ath_6417_vlan_description_field_allows_maximum_32_characters(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		vlan_obj.creating_vlan_for_description_field_validation(self.config.config_vars.description_33_char)
		vlan_obj.assert_error_msg_for_description_field_with_33_char()	
		vlan_obj.delete_default_vlan()



	def test_ath_6421_verify_clicking_cancel_button_discards_the_config_changes(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot("show_vlan")
		vlan_obj.creating_vlan()
		vlan_obj.editing_vlan_2()
		vlan_obj.vlan_2_cancel_button()
		vlan_obj.vlan_1_edit_button()
		vlan_obj.editing_vlan_1()
		vlan_obj.vlan_1_cancel_button()
		self.take_s2_snapshot("show_vlan")
		vlan_obj.delete_default_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()


	def test_ath_6422_verify_sorting_VLAN_table_with_each_table_header(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot("show_vlan")		
		vlan_obj.creating_vlan()
		vlan_obj.creating_vlan_2()
		vlan_obj.creating_vlan_3()
		vlan_obj.creating_vlan_4()
		self.take_s2_snapshot("show_vlan")
		vlan_obj.clicking_id_label()
		vlan_obj.clicking_id_label()
		vlan_obj.delete_default_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()


	def test_ath_8369_verify_error_message_thrown_when_adding_vlan_with_invalid_host(self):
		conf=self.config.config_vars
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		vlan_obj.creating_new_vlan(conf.set_id,conf.set_description,conf.ip_address,conf.inproper_netmask)	
		vlan_obj.assert_netmask_message()

	def test_ath_9654_enable_disable_NAT_single_vlan_without_assigning_ip(self):
		conf=self.config.config_vars
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot("show_vlan")
		vlan_obj.creating_new_vlan(conf.set_id,conf.set_description,"","")
		vlan_obj.selcet_source_nat()
		vlan_obj.click_save_button()
		vlan_obj.selcet_source_nat()
		vlan_obj.click_save_button()
		self.take_s2_snapshot("show_vlan")
 
		vlan_obj.delete_default_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()


	def test_ath_9655_enable_disable_NAT_without_assigning_ip_for_multiple_vlans(self):
		conf=self.config.config_vars
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot("show_vlan")
		vlan_obj.creating_new_vlan(conf.set_id,conf.set_description,"","")
		vlan_obj.creating_new_vlan_2(conf.set_id_2,conf.set_description_2,"","")
		vlan_obj.creating_new_vlan_3(conf.set_id_3,conf.set_description_3,"","")
		vlan_obj.selcet_source_nat()
		vlan_obj.selcet_source_nat_2()
		vlan_obj.selcet_source_nat_3()
		vlan_obj.click_save_button()
		vlan_obj.selcet_source_nat()
		vlan_obj.selcet_source_nat_2()
		vlan_obj.selcet_source_nat_3()
		vlan_obj.click_save_button()
		self.take_s2_snapshot("show_vlan")
		vlan_obj.delete_default_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()


	def test_ath_9684_enable_disable_NAT_single_vlan_with_assigning_ip(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		#self.take_s1_snapshot("show_run_vlan_nat")
		vlan_obj.creating_vlan()
		vlan_obj.selcet_source_nat()
		vlan_obj.click_save_button()
		self.take_s1_snapshot("show_run_vlan_nat")
		vlan_obj.selcet_source_nat()
		vlan_obj.click_save_button()
		self.take_s2_snapshot("show_run_vlan_nat")
		vlan_obj.delete_default_vlan()
		#self.take_s3_snapshot("show_run_vlan_nat")
		self.assert_s1_s2_diff(0)
		#self.assert_s1_s3_diff()
		self.clear()
		

	def test_ath_9685_enable_disable_NAT_having_ip_for_multiple_vlans(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot("show_vlan")
		vlan_obj.creating_vlan()
		vlan_obj.creating_vlan_2()
		vlan_obj.creating_vlan_3()
		vlan_obj.selcet_source_nat()
		vlan_obj.selcet_source_nat_2()
		vlan_obj.selcet_source_nat_3()
		vlan_obj.click_save_button()
		vlan_obj.selcet_source_nat()
		vlan_obj.selcet_source_nat_2()
		vlan_obj.selcet_source_nat_3()
		vlan_obj.click_save_button()
		self.take_s2_snapshot("show_vlan")
		vlan_obj.delete_default_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()


	def test_ath_9686_delete_vlan_having_NAT_enabled(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan() 
		self.take_s1_snapshot("show_vlan")		
		vlan_obj.creating_vlan()
		vlan_obj.selcet_source_nat()
		vlan_obj.click_save_button()
		self.take_s2_snapshot("show_vlan")
 
		vlan_obj.delete_default_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()


	def test_ath_9687_delete_vlan_having_NAT_enabled(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot("show_vlan")		
		vlan_obj.creating_vlan()
		vlan_obj.selcet_source_nat()
		vlan_obj.click_save_button()
		vlan_obj.change_default_vlan_value()
		vlan_obj.selcet_source_nat()
		vlan_obj.click_save_button()
		self.take_s2_snapshot("show_vlan")		
 
		vlan_obj.delete_default_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_6411_web_ui_Elements_verification(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_default_group()
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.assert_vlan_label_fields()

	def test_ath_6444_verify_creating_new_vlan_with_existing_vlan_ip_throws_proper_error_message(self):
		conf=self.config.config_vars
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot("show_vlan")
		vlan_obj.creating_vlan()
		vlan_obj.creating_duplicate_ip_vlan(conf.set_id_2,conf.set_description_2,conf.set_ip_address,conf.set_net_mask1)
		vlan_obj.asssert_duplicate_ip_address()
		self.take_s2_snapshot("show_vlan")
		vlan_obj.delete_default_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()		
	
	def test_ath_6420_verify_creating_new_vlan_with_existing_vlan_id_throws_proper_error_message(self):
		conf=self.config.config_vars
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot("show_vlan")
		vlan_obj.creating_vlan()
		vlan_obj.creating_duplicate_ip_vlan(conf.set_id,conf.set_description_2,conf.set_ip_address1,conf.set_net_mask1)
		vlan_obj.asssert_duplicate_vlan_id()
		self.take_s2_snapshot("show_vlan")
		vlan_obj.delete_default_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_6419_specify_invalid_subnet_mask_while_creating_new_vlan_and_verify_proper_error_message_thrown(self):
		conf=self.config.config_vars
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot("show_vlan")
		vlan_obj.creating_vlan()
		vlan_obj.creating_duplicate_ip_vlan(conf.set_id_2,conf.set_description_2,conf.set_ip_address1,conf.invalid_subnet_mask_1)
		vlan_obj.asssert_invalid_netmask('2')
		vlan_obj.creating_duplicate_ip_vlan(conf.set_id_2,conf.set_description_2,conf.set_ip_address1,conf.invalid_subnet_mask_2)
		vlan_obj.asssert_invalid_netmask('2')
		vlan_obj.creating_duplicate_ip_vlan(conf.set_id_2,conf.set_description_2,conf.set_ip_address1,conf.invalid_subnet_mask_3)
		vlan_obj.asssert_invalid_netmask('2')
		self.take_s2_snapshot("show_vlan")
		vlan_obj.delete_default_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_6418_specify_invalid_ip_while_creating_new_vlan_and_verify_proper_error_message_thrown(self):
		conf=self.config.config_vars
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot("show_vlan")
		vlan_obj.creating_vlan()
		vlan_obj.creating_duplicate_ip_vlan(conf.set_id_2,conf.set_description_2,conf.invalid_ip_1,conf.set_net_mask1)
		vlan_obj.click_save_button()
		vlan_obj.assert_invalid_ip_netmask()
		vlan_obj.click_edit_vlan2()
		vlan_obj.creating_duplicate_ip_vlan(conf.set_id_2,conf.set_description_2,conf.invalid_ip_2,conf.set_net_mask1)
		vlan_obj.assert_invalid_ip()
		vlan_obj.click_edit_vlan2()
		vlan_obj.creating_duplicate_ip_vlan("",conf.set_description_2,conf.invalid_ip_3,conf.set_net_mask1)
		vlan_obj.click_save_button()
		vlan_obj.assert_invalid_ip_netmask()
		self.take_s2_snapshot("show_vlan")
		vlan_obj.delete_vlan_2()
		vlan_obj.delete_default_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_6430_create_multiple_vlans_with_valid_ip_address_and_masks(self):
		conf=self.config.config_vars
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot("GET_RUN_CONFIG")
		vlan_obj.creating_new_vlan("2","test2","2.2.2.2","255.0.0.0")
		vlan_obj.creating_new_vlan_2("3","test2","175.16.1.1","255.255.240.0")
		vlan_obj.creating_new_vlan_3("4","test2","172.16.1.1","255.255.240.0")
		vlan_obj.creating_new_vlan_4("5","test2","10.10.1.1","255.240.0.0")
		vlan_obj.creating_new_vlan_5("6","test2","175.190.1.1","255.255.192.0")
		vlan_obj.creating_new_vlan_6("7","test2","180.180.1.1","255.255.224.0")
		# vlan_obj.creating_new_vlan_7("8","test2","20.20.20.20","255.255.224.0")
		# vlan_obj.creating_new_vlan_8("9","test2","20.20.20.30","255.255.240.0")
		# vlan_obj.creating_new_vlan_9("10","test2","20.20.20.40","255.255.248.0")
		# vlan_obj.creating_new_vlan_10("11","test2","20.20.20.50","255.255.252.0")
		# vlan_obj.creating_new_vlan_11("12","test2","30.30.30.10","255.255.254.0")
		# vlan_obj.creating_new_vlan_12("13","test2","30.30.30.20","255.255.255.0")
		# vlan_obj.creating_new_vlan_13("14","test2","30.30.30.30","255.255.255.128")
		# vlan_obj.creating_new_vlan_14("15","test2","30.30.30.40","255.255.255.192")
		# vlan_obj.creating_new_vlan_15("16","test2","30.30.30.50","255.255.255.224")
		# vlan_obj.creating_new_vlan_16("17","test2","30.30.30.60","255.255.255.240")
		# vlan_obj.creating_new_vlan_17("18","test2","40.40.40.10","255.255.255.248")
		# vlan_obj.creating_new_vlan_18("19","test2","40.40.40.2","255.255.255.252")
		# vlan_obj.creating_new_vlan_19("20","test2","40.40.40.30","255.128.0.0")
		self.take_s2_snapshot("GET_RUN_CONFIG")
		vlan_obj.deleting_multiple_vlans()
		self.take_s3_snapshot("GET_RUN_CONFIG")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	
	
	###################################################     NEW TESTCASES     ##################################################
	
	
	
	def test_ath_11713_verify_add_new_vlan_without_source_nat(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot("show_vlan")
		vlan_obj.creating_new_vlan("2","test2")
		vlan_obj.assert_source_nat("checked")
		self.take_s2_snapshot("show_vlan")
		vlan_obj.delete_default_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11714_verify_add_new_vlan_with_source_nat(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot("show_vlan")
		vlan_obj.creating_new_vlan("2","test2")
		vlan_obj.selcet_source_nat()
		vlan_obj.click_save_button()		
		vlan_obj.assert_source_nat("unchecked")
		self.take_s2_snapshot("show_vlan")
		vlan_obj.delete_default_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_11700_verify_ip_address_inputs_octect_greater_than_255(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		vlan_obj.creating_new_vlan("2","test1","192.168.256.2","255.255.255.0",False)
		vlan_obj.assert_invalid_ip(True)
		vlan_obj.delete_default_vlan()
		
	def test_ath_11701_verify_subnet_mask_inputs_octet_greater_than_255(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		vlan_obj.creating_new_vlan("2","test1","192.168.2.2","255.256.255.0",False)
		vlan_obj.asssert_invalid_netmask('1')
		vlan_obj.delete_default_vlan()
		
	def test_ath_11691_verify_vlan_description_inputs_ascii_characters(self):
		conf = self.config.config_vars
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj._delete_vlan()
		self.take_s1_snapshot("show_vlan")
		vlan_obj.creating_vlan_for_description_field_validation(conf.description_ascii)
		vlan_obj.click_save_settings()
		vlan_obj.assert_vlan_description(conf.description_ascii)
		self.take_s2_snapshot("show_vlan")			
		vlan_obj._delete_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
		
	def test_ath_11692_verify_vlan_description_inputs_unicode_characters(self):
		conf = self.config.config_vars
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj._delete_vlan()
		self.take_s1_snapshot("show_vlan")
		vlan_obj.creating_vlan_for_description_field_validation(conf.description_unicode.decode('utf-8'))
		vlan_obj.click_save_settings()
		vlan_obj.assert_vlan_description(conf.description_unicode.decode('utf-8'))
		self.take_s2_snapshot("show_vlan")			
		vlan_obj._delete_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11693_verify_vlan_description_inputs_special_characters(self):
		conf = self.config.config_vars
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj._delete_vlan()
		self.take_s1_snapshot("show_vlan")
		vlan_obj.creating_vlan_for_description_field_validation(conf.description_special_char)
		vlan_obj.click_save_settings()
		vlan_obj.assert_vlan_description(conf.description_special_char)
		self.take_s2_snapshot("show_vlan")			
		vlan_obj._delete_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11717_verify_delete_vlan(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		vlan_obj.creating_vlan()
		vlan_obj.delete_default_vlan()
		vlan_obj.assert_vlan_test1('Not Exist')
		vlan_obj.delete_default_vlan()

	def test_ath_11696_verify_ip_address_inputs_default_network(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		vlan_obj.creating_new_vlan("2","test1","0.0.0.0","255.0.0.0")
		vlan_obj.assert_netmask_message()
		vlan_obj.delete_default_vlan()
		
	def test_ath_11698_verify_ip_address_inputs_network_broadcast_ip(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		vlan_obj.creating_new_vlan("2","test1","192.168.2.255","255.255.255.0")
		vlan_obj.assert_netmask_message()
		vlan_obj.delete_default_vlan()

	def test_ath_11699_verify_ip_address_inputs_all_octet_255(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		vlan_obj.creating_new_vlan("2","test1","255.255.255.0","255.255.255.0")
		vlan_obj.assert_netmask_message()
		vlan_obj.delete_default_vlan()
	
	def test_ath_11686_verify_vlan_id_max_malue(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.assert_vlan_id_max_and_min_value(self.config.config_vars.set_id_max)
		
	def test_ath_11687_verify_vlan_id_max_malue(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.assert_vlan_id_max_and_min_value(self.config.config_vars.set_id_min)
		
	def test_ath_11688_verify_vlan_description_inputs_33_characters(self):
		conf = self.config.config_vars
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj._delete_vlan()
		vlan_obj.creating_vlan_for_description_field_validation(conf.description_33_char)
		vlan_obj.assert_error_msg_for_description_field_with_33_char()	
		vlan_obj._delete_vlan()
		
	def test_ath_11689_verify_vlan_description_inputs_null_characters(self):
		conf = self.config.config_vars
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj._delete_vlan()
		self.take_s1_snapshot("show_vlan")
		vlan_obj.creating_vlan_for_description_field_validation('')
		vlan_obj.click_save_settings()
		vlan_obj.assert_vlan_description('')
		self.take_s2_snapshot("show_vlan")			
		vlan_obj._delete_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11690_verify_vlan_description_inputs_string_with_spaces(self):
		conf = self.config.config_vars
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj._delete_vlan()
		self.take_s1_snapshot("show_vlan")
		vlan_obj.creating_vlan_for_description_field_validation(conf.description_string_with_spaces)
		vlan_obj.click_save_settings()
		vlan_obj.assert_vlan_description(conf.description_string_with_spaces)
		self.take_s2_snapshot("show_vlan")			
		vlan_obj._delete_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	# def test_ath_22234_Verify_Add_New_VLAN_with_Existing_IP_Address_on_Switch(self):
		# conf = self.config.config_vars
		# vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		# vlan_obj.delete_default_vlan()
		# self.take_s1_snapshot()
		# vlan_obj.creating_new_vlan("45","test1","3.3.3.3","255.255.255.0")
		# vlan_obj.creating_new_vlan_2("45")
		# vlan_obj.asssert_duplicate_vlan_id()
		# self.take_s2_snapshot()			
		# vlan_obj.delete_default_vlan()
		# self.take_s3_snapshot()
		# self.assert_s1_s2_diff(None)
		# self.assert_s1_s3_diff()
		# self.clear()
		
	def test_ath_11694_verify_vlan_description_japanese_characters(self):
		conf=self.config.config_vars
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot("show_vlan")
		vlan_obj.creating_new_vlan(conf.set_id,conf.set_japanese_char.decode('utf-8'),"","")
		vlan_obj.assert_vlan_description(conf.set_japanese_char.decode('utf-8'))
		self.take_s2_snapshot("show_vlan")
		vlan_obj.change_default_vlan_value()
		vlan_obj.delete_default_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11695_verify_vlan_description_german_characters(self):
		conf=self.config.config_vars
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot("show_vlan")
		vlan_obj.creating_new_vlan(conf.set_id,conf.set_german_char.decode('utf-8'),"","")
		vlan_obj.assert_vlan_description(conf.set_german_char.decode('utf-8'))
		self.take_s2_snapshot("show_vlan")
		vlan_obj.change_default_vlan_value()
		vlan_obj.delete_default_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11715_Verify_Add_new_vlan_with_existing_ip_address_on_switch(self):
		conf=self.config.config_vars
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		vlan_obj.creating_new_vlan(conf.set_id_45,conf.set_description,conf.set_ip_address_5,conf.set_net_mask)
		vlan_obj.creating_duplicate_ip_vlan(conf.set_id_50,conf.set_description1,conf.set_ip_address_5,conf.set_net_mask)
		vlan_obj.asssert_duplicate_ip_address()
		vlan_obj.delete_default_vlan()		
		
	def test_ath_11702_verify_no_of_vlans_field(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot("show_vlan")		
		vlan_obj.creating_vlan()
		vlan_obj.creating_vlan_2()
		vlan_obj.creating_vlan_3()
		vlan_obj.creating_vlan_4()
		vlan_obj.asserting_no_of_vlans()
		self.take_s2_snapshot("show_vlan")
		vlan_obj.delete_default_vlan()
		self.take_s3_snapshot("show_vlan")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	