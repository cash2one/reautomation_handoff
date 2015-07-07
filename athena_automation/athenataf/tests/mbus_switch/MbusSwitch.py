from athenataf.lib.functionality.test.SwitchConfigurationTest import SwitchConfigurationTest

class MbusSwitch(SwitchConfigurationTest):
	'''
	Test class for MBUS_Switch 
	'''
	def test_ath_9568_verify_static_ip_assignment_functionality_on_switches_page(self):
		self1 = self.config.config_vars
		self.take_s1_snapshot()
		self.SwitchesPage.edit_switch()
		self.SwitchesPage.set_ip_assignment('Static')
		self.SwitchesPage.set_static_ipaddress_netmask_gateway(self1.switch_ip_address,self1.netmask,self1.gateway)
		self.take_s2_snapshot()
		self.SwitchesPage.edit_switch()
		self.SwitchesPage.set_ip_assignment('DHCP')
		self.SwitchesPage.save_switch_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_9577_configure_access_vlan_for_port_in_access_mode_and_verify(self):
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s1_snapshot()
		vlan_obj.creating_vlan()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.changing_access_vlan_value(assert_fields=True)
		self.take_s2_snapshot()		
		port_obj.set_default_access_vlan_value()
		vlan_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vlan_obj.delete_default_vlan()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_9578_configure_native_vlan_allowed_vlans_for_port_in_trunk_mode_and_verify(self):
		vpn_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		self.take_s1_snapshot()
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
		
	def test_ath_9576_change_admin_status_of_port_and_verify(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		self.take_s1_snapshot()
		port_obj.change_Admin_status()
		self.take_s2_snapshot()
		port_obj.set_default_Admin_status()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()