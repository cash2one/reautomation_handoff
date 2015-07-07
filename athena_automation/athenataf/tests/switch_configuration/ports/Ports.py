import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.SwitchConfigurationTest import SwitchConfigurationTest

class Ports(SwitchConfigurationTest):
	'''
	Test class for switch configuration->ports.
	'''

	def test_ath_6401_configure_access_vlan_for_a_port_in_access_mode_and_verify(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot()
		vlan_obj.creating_vlan()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.changing_access_vlan_value(assert_fields=True)
		port_obj.set_default_access_vlan_value()
		self.take_s2_snapshot()
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()


	def test_ath_6397_change_Admin_status_of_port(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		self.take_s1_snapshot()
		port_obj.change_Admin_status()
		self.take_s2_snapshot()
		port_obj.set_default_Admin_status()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

		
	def test_ath_6382_verify_switch_configuration_ports_Page(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.verify_port_page_field()
		
	def test_ath_6398_change_the_port_mode_of_port_and_verify(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		self.take_s1_snapshot("show_port")
		port_obj.selecting_checkbox_6()
		port_obj.set_port_mode('Trunk')
		port_obj.save_port_setting()
		self.take_s2_snapshot("show_port")
		port_obj.selecting_checkbox_6()
		port_obj.set_port_mode()
		port_obj.save_port_setting()
		self.take_s3_snapshot("show_port")
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

		
	def test_ath_6399_change_the_poe_state_of_port_and_verify(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		self.take_s1_snapshot("show_poe")
		port_obj.selecting_checkbox_6()
		port_obj.set_poe('Disabled')
		port_obj.save_port_setting()
		self.take_s2_snapshot("show_poe")
		port_obj.selecting_checkbox_6()
		port_obj.set_poe()
		port_obj.save_port_setting()
		self.take_s3_snapshot("show_poe")
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_6400_change_the_port_speed_of_port_and_verify(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		self.take_s1_snapshot()
		port_obj.selecting_checkbox_6()
		port_obj.set_speed_duplex('10 Mbps')
		self.take_s2_snapshot()
		port_obj.save_port_setting()
		port_obj.selecting_checkbox_6()
		port_obj.set_speed_duplex()
		port_obj.save_port_setting()
		port_obj.selecting_checkbox_6()
		port_obj.set_speed_duplex('100 Mbps')
		port_obj.save_port_setting()
		port_obj.selecting_checkbox_6()
		port_obj.set_speed_duplex('1 Gbps')
		port_obj.save_port_setting()
		port_obj.selecting_checkbox_6()
		port_obj.set_speed_duplex()
		port_obj.save_port_setting()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_6402_configure_native_vlan_allowed_vlans_for_port_in_trunk_mode_and_verify(self):
		vpn_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		self.take_s1_snapshot()
		vpn_obj.delete_default_vlan()
		vpn_obj.creating_vlan()
		vpn_obj.creating_vlan_2()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.selecting_checkbox_6()
		port_obj.set_port_mode('Trunk')
		port_obj.set_native_vlan(self.config.config_vars.set_id)
		port_obj.set_allowed_vlan(self.config.config_vars.set_id_2)
		port_obj.save_port_setting()
		self.take_s2_snapshot()
		vpn_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vpn_obj.delete_default_vlan()
		vpn_obj.delete_default_vlan()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.setting_port_trunk_default()
		port_obj.setting_port_access_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_6405_configure_native_vlan_multiple_allowed_vlans_range_for_port(self):
		vpn_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vpn_obj.delete_default_vlan()
		self.take_s1_snapshot()
		vpn_obj.creating_vlan()
		vpn_obj.creating_vlan_2()
		vpn_obj.creating_vlan_3()
		vpn_obj.creating_vlan_4()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.selecting_checkbox_6()
		port_obj.set_port_mode('Trunk')
		port_obj.set_native_vlan(self.config.config_vars.set_id)
		port_obj.set_allowed_vlan('4-6')
		port_obj.save_port_setting()
		self.take_s2_snapshot()
		vpn_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vpn_obj.delete_default_vlan()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.setting_port_trunk_default()
		port_obj.setting_port_access_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_6408_configure_native_vlan_multiple_allowed_vlans_range_for_port(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		# self.take_s1_snapshot()
		port_obj.selecting_checkbox_3(refresh1=False)
		port_obj.selecting_checkbox_4(refresh1=False)
		port_obj.selecting_checkbox_5(refresh1=False)
		port_obj.selecting_checkbox_6(refresh1=False)
		port_obj.set_port_mode()
		port_obj.set_access_vlan('5')
		port_obj.set_poe('Disabled')
		port_obj.set_speed_duplex('1 Gbps')
		port_obj.set_admin_status('Down')
		port_obj.set_port_mode('Trunk')
		port_obj.cancel_port_setting()
		# self.take_s2_snapshot()
		# self.take_s3_snapshot()
		# self.assert_s1_s2_diff(None)
		# self.assert_s1_s3_diff()
		# self.clear()
		
	def test_ath_6403_Configure_invalid_vlan_for_a_port_in_access_or_trunk_mode_and_verify(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		# self.take_s1_snapshot()
		port_obj.selecting_checkbox_6()
		port_obj.set_port_mode('Access')
		port_obj.assert_access_vlan()
		port_obj.set_port_mode('Trunk')
		port_obj.assert_allow_vlan()
		
	def test_ath_6409_verify_clicking_close_icon_in_edit_pop_up_post_config_changes(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.selecting_checkbox_3(refresh1=False)
		port_obj.selecting_checkbox_4(refresh1=False)
		port_obj.selecting_checkbox_5(refresh1=False)
		port_obj.selecting_checkbox_6(refresh1=False)
		port_obj.set_access_vlan('5')
		port_obj.set_poe('Disabled')
		port_obj.set_speed_duplex('1 Gbps')
		port_obj.set_admin_status('Down')
		port_obj.set_port_mode('Trunk')
		port_obj.cancel_port_setting()
		
	def test_ath_6384_verify_ui_elements_on_switch_configuration_ports_page_for_S1500_24P_switch(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.verify_port_page_field()
		port_obj.assert_ports_number_and_format()
		
	def test_ath_6385_verify_ui_elements_on_switch_configuration_ports_page_for_S1500_12P_switch(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_switch_device()
		self.SwitchesPage.assert_switch_1()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.verify_port_page_field()
		port_obj.assert_edit_disable_button()
		
	
	
	
	###################################################     NEW TESTCASES     ##################################################
	
	
	
		
	def test_ath_11639_verify_edit_port_mode_access_with_existing_access_vlan(self):
		self1=self.config.config_vars
		vpn_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vpn_obj.delete_default_vlan()
		self.take_s1_snapshot()
		vpn_obj.creating_new_vlan(self1.set_id_10,self1.set_description,self1.set_ip_address,self1.set_net_mask)
		vpn_obj.creating_new_vlan_2(self1.set_id_20,self1.set_description_2,self1.set_ip_address_2,self1.set_net_mask_2)
		vpn_obj.creating_new_vlan_3(self1.set_id_30,self1.set_description_3,self1.set_ip_address_3,self1.set_net_mask_3)
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()		
		port_obj.selecting_checkbox_3(refresh1=False)
		port_obj.click_edit_button()
		port_obj.set_port_mode()
		port_obj.set_access_vlan(self1.set_id_20)
		port_obj.save_port_setting()
		port_obj.assert_access_vlan_value(self1.set_id_20)
		self.take_s2_snapshot()
		port_obj.selecting_checkbox_3(refresh1=True)
		port_obj.click_edit_button()
		port_obj.setting_port_access_default_value()
		vpn_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vpn_obj.delete_default_vlan()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()		
		
	def test_ath_11640_verify_edit_port_mode_access_with_non_existing_access_vlan(self):
		self1=self.config.config_vars
		vpn_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vpn_obj.delete_default_vlan()
		self.take_s1_snapshot()
		vpn_obj.creating_new_vlan(self1.set_id_10,self1.set_description,self1.set_ip_address,self1.set_net_mask)
		vpn_obj.creating_new_vlan_2(self1.set_id_20,self1.set_description_2,self1.set_ip_address_2,self1.set_net_mask_2)
		vpn_obj.creating_new_vlan_3(self1.set_id_30,self1.set_description_3,self1.set_ip_address_3,self1.set_net_mask_3)
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()		
		port_obj.selecting_checkbox_3(refresh1=False)
		port_obj.click_edit_button()
		port_obj.set_port_mode()
		port_obj.set_access_vlan(self1.set_id_50)
		port_obj.save_port_setting()
		port_obj.assert_access_vlan_value(self1.set_id_50)		
		self.take_s2_snapshot()		
		
		port_obj.selecting_checkbox_3(refresh1=True)
		port_obj.click_edit_button()
		port_obj.setting_port_access_default_value()
		vpn_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vpn_obj.delete_default_vlan()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11641_verify_edit_port_mode_trunk(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		self.take_s1_snapshot()		
		port_obj.selecting_checkbox_3(refresh1=False)
		port_obj.click_edit_button()
		port_obj.set_port_mode(self.config.config_vars.portmode_trunk)
		port_obj.save_port_setting()
		port_obj.assert_trunk_mode(self.config.config_vars.portmode_trunk)
		self.take_s2_snapshot()		
		
		port_obj.selecting_checkbox_3(refresh1=True)
		port_obj.click_edit_button()
		port_obj.setting_port_access_default_value()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11642_verify_edit_port_mode_trunk_allowed_vlans(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		self.take_s1_snapshot()		
		port_obj.selecting_checkbox_3(refresh1=False)
		port_obj.click_edit_button()
		port_obj.set_port_mode(self.config.config_vars.portmode_trunk)
		port_obj.set_allowed_vlan(self.config.config_vars.allowed_vlan_1)
		port_obj.save_port_setting()
		port_obj.assert_trunk_mode_allowed_vlan(self.config.config_vars.portmode_trunk,self.config.config_vars.allowed_vlan_1)
		self.take_s2_snapshot()		
		
		port_obj.selecting_checkbox_3(refresh1=True)
		port_obj.click_edit_button()
		port_obj.setting_port_trunk_default_value()
		port_obj.selecting_checkbox_3(refresh1=True)
		port_obj.click_edit_button()		
		port_obj.setting_port_access_default_value()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11643_verify_edit_port_mode_trunk_native_vlans(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		self.take_s1_snapshot()		
		port_obj.selecting_checkbox_3(refresh1=False)
		port_obj.click_edit_button()
		port_obj.set_port_mode(self.config.config_vars.portmode_trunk)
		port_obj.set_native_vlan(self.config.config_vars.native_vlan_1)
		port_obj.save_port_setting()
		port_obj.assert_trunk_mode_native_and_allowed_vlan(True,self.config.config_vars.portmode_trunk,self.config.config_vars.native_vlan_1,'')
		port_obj.cancel_port_setting()
		port_obj.selecting_checkbox_3(refresh1=True)
		port_obj.click_edit_button()
		self.take_s2_snapshot()		
		port_obj.setting_port_trunk_default_value()
		port_obj.selecting_checkbox_3(refresh1=True)
		port_obj.click_edit_button()		
		port_obj.setting_port_access_default_value()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11644_verify_edit_poe_disable(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		self.take_s1_snapshot()		
		port_obj.selecting_checkbox_3(refresh1=False)
		port_obj.click_edit_button()
		port_obj.set_poe(self.config.config_vars.poe1_disabled)
		port_obj.save_port_setting()
		port_obj.assert_poe_field(self.config.config_vars.poe1_disabled)
		self.take_s2_snapshot()		
		
		port_obj.selecting_checkbox_3(refresh1=True)
		port_obj.click_edit_button()		
		port_obj.setting_port_access_default_value()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_11648_Verify_Edit_Speed_Setting_1_Gbps(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		self.take_s1_snapshot()		
		port_obj.selecting_checkbox_3(refresh1=False)
		port_obj.click_edit_button()
		port_obj.set_speed_duplex(self.config.config_vars.speed_1gbps)
		port_obj.save_port_setting()
		port_obj.selecting_checkbox_3(refresh1=True)
		port_obj.click_edit_button()		
		port_obj.assert_speed_duplex_value(self.config.config_vars.speed_1gbps)
		self.take_s2_snapshot()		
		port_obj.selecting_checkbox_3(refresh1=True)
		port_obj.click_edit_button()		
		port_obj.setting_port_access_default_value()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()		
		
	def test_ath_11651_verify_modify_settings_for_few_ports(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		self.take_s1_snapshot()		
		port_obj.selecting_checkbox_4(refresh1=False)
		port_obj.selecting_checkbox_5(refresh1=False)
		port_obj.selecting_checkbox_6(refresh1=False)
		# port_obj.click_edit_button()
		port_obj.set_speed_duplex(self.config.config_vars.speed_1gbps)
		port_obj.set_port_mode(self.config.config_vars.portmode_trunk)
		port_obj.set_native_vlan(self.config.config_vars.native_vlan_1)
		port_obj.set_allowed_vlan(self.config.config_vars.allowed_vlan_2)
		port_obj.save_port_setting()
		self.take_s2_snapshot()
		port_obj.selecting_checkbox_4(refresh1=True)
		port_obj.selecting_checkbox_5(refresh1=False)
		port_obj.selecting_checkbox_6(refresh1=False)
		port_obj.assert_trunk_mode_native_and_allowed_vlan(False,self.config.config_vars.portmode_trunk,self.config.config_vars.native_vlan_1,self.config.config_vars.allowed_vlan_2,False)
		port_obj.assert_speed_duplex_value(self.config.config_vars.speed_1gbps)
		port_obj.cancel_port_setting()
		port_obj.selecting_checkbox_4(refresh1=True)
		port_obj.selecting_checkbox_5(refresh1=False)
		port_obj.selecting_checkbox_6(refresh1=False)
		port_obj.setting_port_trunk_default_value()
		port_obj.selecting_checkbox_4(refresh1=True)
		port_obj.selecting_checkbox_5(refresh1=False)
		port_obj.selecting_checkbox_6(refresh1=False)
		# port_obj.click_edit_button()
		port_obj.setting_port_access_default_value()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()		

	def test_ath_11647_verify_edit_speed_setting_100_mbps(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		self.take_s1_snapshot()		
		port_obj.selecting_checkbox_3(refresh1=False)
		port_obj.click_edit_button()
		port_obj.set_speed_duplex(self.config.config_vars.speed_100mbps)
		port_obj.save_port_setting()
		port_obj.selecting_checkbox_3(refresh1=True)
		port_obj.click_edit_button()		
		port_obj.assert_speed_duplex_value(self.config.config_vars.speed_100mbps)
		self.take_s2_snapshot()		
		port_obj.selecting_checkbox_3(refresh1=True)
		port_obj.click_edit_button()		
		port_obj.setting_port_access_default_value()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11645_verify_edit_poe_enable(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		self.take_s1_snapshot()		
		port_obj.selecting_checkbox_3(refresh1=False)
		port_obj.click_edit_button()
		port_obj.set_poe(self.config.config_vars.poe1_enabled)
		port_obj.save_port_setting()
		port_obj.assert_poe_field(self.config.config_vars.poe1_enabled)
		self.take_s2_snapshot()		
		
		port_obj.selecting_checkbox_3(refresh1=True)
		port_obj.click_edit_button()		
		port_obj.setting_port_access_default_value()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_11646_verify_edit_speed_setting_10_mbps(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		self.take_s1_snapshot()		
		port_obj.selecting_checkbox_3(refresh1=False)
		port_obj.click_edit_button()
		port_obj.set_speed_duplex(self.config.config_vars.speed_10mbps)
		port_obj.save_port_setting()
		port_obj.selecting_checkbox_3(refresh1=True)
		port_obj.click_edit_button()		
		port_obj.assert_speed_duplex_value(self.config.config_vars.speed_10mbps)
		self.take_s2_snapshot()		
		port_obj.selecting_checkbox_3(refresh1=True)
		port_obj.click_edit_button()		
		port_obj.setting_port_access_default_value()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_11649_verify_edit_admin_status_down(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		self.take_s1_snapshot()		
		port_obj.selecting_checkbox_3(refresh1=False)
		port_obj.click_edit_button()
		port_obj.set_admin_status(self.config.config_vars.admin_down)
		port_obj.save_port_setting()
		port_obj.selecting_checkbox_3(refresh1=True)
		port_obj.click_edit_button()		
		port_obj.assert_admin_status(self.config.config_vars.admin_down)
		self.take_s2_snapshot()		
		port_obj.selecting_checkbox_3(refresh1=True)
		port_obj.click_edit_button()		
		port_obj.setting_port_access_default_value()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_11650_verify_edit_admin_status_up(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		self.take_s1_snapshot()		
		port_obj.selecting_checkbox_3(refresh1=False)
		port_obj.click_edit_button()
		port_obj.set_admin_status(self.config.config_vars.admin_up)
		port_obj.save_port_setting()
		port_obj.selecting_checkbox_3(refresh1=True)
		port_obj.click_edit_button()		
		port_obj.assert_admin_status(self.config.config_vars.admin_up)
		self.take_s2_snapshot()		
		port_obj.selecting_checkbox_3(refresh1=True)
		port_obj.click_edit_button()		
		port_obj.setting_port_access_default_value()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_11628_verify_access_vlan_port_mode_access(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.selecting_checkbox_3(refresh1=False)
		port_obj.click_edit_button()
		port_obj.set_port_mode()
		port_obj.assert_access_vlan_mode('enabled')
		port_obj.assert_native_vlan_mode('disabled')
		port_obj.assert_allowed_vlan_mode('disabled')
		port_obj.cancel_port_setting()
		
	def test_ath_11629_verify_access_vlan_port_mode_trunk(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.selecting_checkbox_3(refresh1=False)
		port_obj.click_edit_button()
		port_obj.set_port_mode('Trunk')
		port_obj.assert_access_vlan_mode('disabled')
		port_obj.assert_native_vlan_mode('enabled')
		port_obj.assert_allowed_vlan_mode('enabled')
		port_obj.cancel_port_setting()
		
	def test_ath_11598_group_12Port_switch_verify_default_ports_configuration_admin_status(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_group_12Port_admin_status()	

	def test_ath_11599_group_12Port_switch_verify_default_ports_configuration_port_mode(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_group_12Port_port_mode()		
		
		
	def test_ath_11600_group_12Port_switch_verify_default_ports_configuration_vlan(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_group_12Port_vlan()
		
	def test_ath_11601_group_12Port_switch_verify_default_ports_configuration_poe(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_group_12Port_poe()			
		
	def test_ath_11602_group_12Port_switch_verify_default_ports_configuration_speed_duplex(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_group_12Port_speed_duplex()			
	
	def test_ath_11613_switch_12Port_switch_verify_default_ports_configuration_admin_status(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_switch_device()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_switch_12Port_admin_status()

	def test_ath_11614_switch_12Port_switch_verify_default_ports_configuration_port_mode(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_switch_device()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_switch_12Port_port_mode()
		
	def test_ath_11615_switch_12Port_switch_verify_default_ports_configuration_vlan(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_switch_device()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_switch_12Port_vlan()
		
	def test_ath_11616_switch_12Port_switch_verify_default_ports_configuration_poe(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_switch_device()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_switch_12Port_poe()				
		
	def test_ath_11617_switch_12Port_switch_verify_default_ports_configuration_speed_duplex(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_switch_device()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_switch_12Port_speed_duplex()
	
	def test_ath_11603_group_24Port_switch_verify_default_ports_configuration_admin_status(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_group_24Port_admin_status()

	def test_ath_11604_group_24Port_switch_verify_default_ports_configuration_port_mode(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_group_24Port_port_mode()
		
	def test_ath_11605_group_24Port_switch_verify_default_ports_configuration_vlan(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_group_24Port_vlan()
		
	def test_ath_11606_group_24Port_switch_verify_default_ports_configuration_poe(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_group_24Port_poe()
		
	def test_ath_11607_group_24Port_switch_verify_default_ports_configuration_speed_duplex(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_group_24Port_speed_duplex()	
	
	def test_ath_11618_switch_24Port_switch_verify_default_ports_configuration_admin_status(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_switch_device()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_switch_24Port_admin_status()

	def test_ath_11619_switch_24Port_switch_verify_default_ports_configuration_port_mode(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_switch_device()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_switch_24Port_port_mode()
		
	def test_ath_11620_switch_24Port_switch_verify_default_ports_configuration_vlan(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_switch_device()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_switch_24Port_vlan()
		
	def test_ath_11621_switch_24Port_switch_verify_default_ports_configuration_poe(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_switch_device()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_switch_24Port_poe()
		
	def test_ath_11622_switch_24Port_switch_verify_default_ports_configuration_speed_duplex(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_switch_device()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_switch_24Port_speed_duplex()	
	
	
	
	def test_ath_11608_group_48Port_switch_verify_default_ports_configuration_admin_status(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_group_48Port_admin_status()		
		

	def test_ath_11609_group_48Port_switch_verify_default_ports_configuration_port_mode(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_group_48Port_port_mode()
		
	def test_ath_11610_group_48Port_switch_verify_default_ports_configuration_vlan(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_group_48Port_vlan()	
		
		
	def test_ath_11611_group_48Port_switch_verify_default_ports_configuration_poe(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_group_48Port_poe()		
		
	def test_ath_11612_group_48Port_switch_verify_default_ports_configuration_speed_duplex(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_group_48Port_speed_duplex()	
	
	def test_ath_11623_switch_48Port_switch_verify_default_ports_configuration_admin_status(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_switch_device()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_switch_48Port_admin_status()


	def test_ath_11624_switch_48Port_switch_verify_default_ports_configuration_port_mode(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_switch_device()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_switch_48Port_port_mode()
		
	def test_ath_11625_switch_48Port_switch_verify_default_ports_configuration_vlan(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_switch_device()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_switch_48Port_vlan()
		
	def test_ath_11626_switch_48Port_switch_verify_default_ports_configuration_poe(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_switch_device()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_switch_48Port_poe()
		
	def test_ath_11627_switch_48Port_switch_verify_default_ports_configuration_speed_duplex(self):
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_switch_device()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.assert_switch_48Port_speed_duplex()
	
	
	
	
	
	
	
	
	