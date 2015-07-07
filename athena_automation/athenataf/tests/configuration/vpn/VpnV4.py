import logging
logger = logging.getLogger('athenataf')


from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class VpnV4(ConfigurationTest):
	'''
		Test class for network IAP 4.0 configuration VPN.
	'''
	
	def test_ath_3989_vpn_controller_L2TPv3_default(self):
		self.take_s1_snapshot()
		vpn_obj = self.LeftPanel.go_to_vpn() 
		vpn_obj.routing.click()
		vpn_obj.controller.click()
		vpn_obj.protocol.set(self.config.config_vars.vpn_L2TPv3_protocol)
		vpn_obj.create_tunnel()
		failover_default = vpn_obj.failover_mode.get_selected()
		config_failover = self.config.config_vars.config_failover
		self.assertEquals(failover_default, config_failover)
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_3990_vpn_controller_L2TPv3_nondefault(self):
		self.take_s1_snapshot()
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.routing.click()
		vpn_obj.controller.click()		
		vpn_obj.protocol.set(self.config.config_vars.vpn_L2TPv3_protocol)
		vpn_obj.create_tunnel()
		vpn_obj.assert_tunnel_config_error()
		vpn_obj.setting_tunnel_values()
		vpn_obj.save_settings()
		vpn_obj.assert_tunnel()
		vpn_obj.create_assert_session()
		vpn_obj.save_session_click()
		self.take_s2_snapshot()
		vpn_obj.delete_session()
		vpn_obj.tunnel_created.click()
		vpn_obj.delete_tunnel.click()
		vpn_obj.save_settings()
		vpn_obj.buy_time()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_3991_vpn_controller_ArubaGre_default(self):
		self.take_s1_snapshot()
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.routing.click()
		vpn_obj.controller.click()	
		vpn_obj.protocol.set(self.config.config_vars.vpn_ArubaGre_protocol)
		vpn_obj.assert_arubaGre_default()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

		
	def test_ath_3992_vpn_controller_ArubaGre_nondefault(self):
		self.take_s1_snapshot()
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.routing.click()
		vpn_obj.controller.click()
		vpn_obj.protocol.set(self.config.config_vars.vpn_ArubaGre_protocol)
		vpn_obj.assert_IPsec_parameters_fields()
		vpn_obj.write_in_primary()
		vpn_obj.write_in_backup()
		vpn_obj.configure_IPSec_default()
		vpn_obj.enable_preup_tunnel()
		vpn_obj.save_settings()
		self.take_s2_snapshot()
		vpn_obj.revert_gre_settings()
		vpn_obj.restore_Ipsec_default()
		vpn_obj.buy_time()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		