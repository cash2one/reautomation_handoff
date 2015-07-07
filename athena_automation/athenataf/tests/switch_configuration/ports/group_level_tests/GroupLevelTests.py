import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.SwitchConfigurationTest import SwitchConfigurationTest

class GroupLevelTests(SwitchConfigurationTest):
	'''
	Test class for group level test.
	'''

	def test_ath_7816_change_Admin_status_of_port(self):
		vpn_obj = self.LeftPanel.go_to_switch_configuration_vlans()
		vpn_obj.delete_default_vlan()      
		self.take_s1_snapshot()
		vpn_obj.creating_vlan()
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		port_obj.changing_port_mode_and_native_vlan()
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


	def test_ath_7811_change_Admin_status_of_port(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		self.take_s1_snapshot()
		port_obj.change_Admin_status()
		self.take_s2_snapshot()
		port_obj.set_default_Admin_status()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_7812_change_switch_group_port_mode(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		self.take_s1_snapshot()		
		port_obj.changing_trunk_port_mode_value()
		self.take_s2_snapshot()
		port_obj.changing_access_port_mode_value()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_7813_change_switch_group_poe_state(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		self.take_s1_snapshot("show_poe")
		port_obj.changing_poe_value_disabled()
		self.take_s2_snapshot("show_poe")
		port_obj.changing_poe_value_enabled()
		self.take_s3_snapshot("show_poe")
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_7814_change_switch_group_port_speed(self):
		port_obj = self.LeftPanel.go_to_switch_configuration_ports()
		self.take_s1_snapshot()
		port_obj.selecting_checkbox_6()
		port_obj.set_speed_duplex('10 Mbps')
		port_obj.save_port_setting()
		port_obj.selecting_checkbox_6()
		port_obj.set_speed_duplex()
		port_obj.save_port_setting()
		port_obj.selecting_checkbox_6()
		port_obj.set_speed_duplex('100 Mbps')
		port_obj.save_port_setting()
		self.take_s2_snapshot()
		port_obj.selecting_checkbox_6()
		port_obj.set_speed_duplex()
		port_obj.save_port_setting()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()


	def test_ath_7815_Change_switch_group_access_vlan(self):
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

