import logging
logger = logging.getLogger('athenataf')


from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Vpn(ConfigurationTest):
	'''
		Test class for network configuration VPN.
	'''
	
	def test_ath_1955_vpn_controller_Ipsec_default(self):
		self.take_s1_snapshot()
		vpn_obj = self.LeftPanel.go_to_vpn() 
		vpn_obj.routing.click()
		vpn_obj.controller.click()
		vpn_obj.protocol.set(self.config.config_vars.vpn_def_protocol)
		protocol_default = vpn_obj.protocol.get_selected()
		config_protocol = self.config.config_vars.vpn_def_protocol
		self.assertEquals(protocol_default, config_protocol)
		vpn_obj.write_in_primary()
		vpn_obj.assert_default_fields()
		vpn_obj.write_in_backup()
		vpn_obj.assert_fields()
		vpn_obj.set_primary_backup_host_default_values()
		vpn_obj.save_settings()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

		
	def test_ath_1956_vpn_controller_Ipsec_nondefault(self):
		self.take_s1_snapshot()
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.routing.click()
		vpn_obj.controller.click()
		vpn_obj.protocol.set(self.config.config_vars.vpn_def_protocol)
		protocol_default = vpn_obj.protocol.get_selected()
		config_protocol = self.config.config_vars.vpn_def_protocol
		self.assertEquals(protocol_default, config_protocol)
		# vpn_obj.assert_IPsec_parameters_fields()
		vpn_obj.write_in_primary()
		vpn_obj.write_in_backup()
		vpn_obj.setting_nondefault_values()
		vpn_obj.save_settings()
		self.take_s2_snapshot()
		vpn_obj.revert_settings()
		vpn_obj.save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1957_vpn_controller_gre_default(self):
		self.take_s1_snapshot()
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.routing.click()
		vpn_obj.controller.click()
		vpn_obj.protocol.set(self.config.config_vars.vpn_gre_protocol)
		vpn_obj.assert_gre_default()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
		
	def test_ath_1958_vpn_controller_gre_nondefault(self):
		self.take_s1_snapshot()
		vpn_obj = self.LeftPanel.go_to_vpn() 
		vpn_obj.routing.click()
		vpn_obj.controller.click()
		vpn_obj.protocol.set(self.config.config_vars.vpn_gre_protocol)
		vpn_obj.assert_manual_gre_parameters_fields()
		vpn_obj.setting_gre_values()
		vpn_obj.save_settings()
		self.take_s2_snapshot()
		vpn_obj.restore_manual_GRE_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1959_vpn_add_route(self):
		self.take_s1_snapshot()
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.got_to_vpn_routing()
		vpn_obj.click_new_route()
		vpn_obj.add_route()
		vpn_obj.save_settings()
		vpn_obj.assert_route()
		vpn_obj.buy_time()
		self.take_s2_snapshot()
		vpn_obj.delete_route()
		vpn_obj.save_settings()
		vpn_obj.buy_time()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1960_vpn_edit_route(self):
		self.take_s1_snapshot()
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.got_to_vpn_routing()
		# vpn_obj.assert_edit_field_error()
		vpn_obj.click_new_route()
		vpn_obj.add_route()
		vpn_obj.assert_route()
		vpn_obj.clicking_edit_route()
		vpn_obj.assert_edit_route_fields()
		# vpn_obj.assert_edit_field_error()
		vpn_obj.edit_route()
		vpn_obj.assert_edited_route()
		vpn_obj.buy_time()
		self.take_s2_snapshot()
		vpn_obj.delete_route()
		vpn_obj.save_settings()
		vpn_obj.buy_time()	
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_1961_vpn_delete_route(self):
		self.take_s1_snapshot()
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.got_to_vpn_routing()
		vpn_obj.click_new_route()
		vpn_obj.add_route()
		vpn_obj.assert_route()
		vpn_obj.buy_time()
		self.take_s2_snapshot()
		vpn_obj.delete_route()
		vpn_obj.save_settings()
		vpn_obj.buy_time()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
		
		