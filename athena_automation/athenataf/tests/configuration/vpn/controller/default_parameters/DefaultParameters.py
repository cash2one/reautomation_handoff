import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DefaultParameters(ConfigurationTest):
	'''
		Test class for Default Parameters.
	'''
	
	def test_ath_8285_Ipsec_default(self):
		self.take_s1_snapshot()
		vpn_obj = self.LeftPanel.go_to_vpn() 
		vpn_obj.routing.click()
		vpn_obj.controller.click()
		vpn_obj.assert_Ipsec_default()
		self.take_s2_snapshot()
		self.assert_s1_s2_diff(0)
		self.clear()
		
	def test_ath_8286_default_aruba_gre(self):
		self.take_s1_snapshot()
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.routing.click()
		vpn_obj.controller.click()
		vpn_obj.protocol.set(self.config.config_vars.vpn_ArubaGre_protocol)
		vpn_obj.assert_aruba_gre_default()
		self.take_s2_snapshot()
		vpn_obj.restore_Ipsec_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	
	def test_ath_8287_default_L2TPv3(self):
		self.take_s1_snapshot()
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.routing.click()
		vpn_obj.controller.click()
		vpn_obj.protocol.set(self.config.config_vars.vpn_L2TPv3_protocol)
		vpn_obj.assert_L2TPv3_default()
		self.take_s2_snapshot()
		vpn_obj.restore_Ipsec_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_8288_manual_gre(self):
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.controller.click()
		vpn_obj.assert_default_manual_gre()
		
	def test_ath_11182_Ipsec_default(self):
		vpn_obj = self.LeftPanel.go_to_vpn() 
		vpn_obj.routing.click()
		vpn_obj.controller.click()
		vpn_obj.assert_Ipsec_default()

	def test_ath_11183_default_aruba_gre(self):
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.routing.click()
		vpn_obj.controller.click()
		vpn_obj.protocol.set(self.config.config_vars.vpn_ArubaGre_protocol)
		vpn_obj.assert_aruba_gre_default()
		vpn_obj.restore_Ipsec_default()

	def test_ath_11184_default_L2TPv3(self):
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.routing.click()
		vpn_obj.controller.click()
		vpn_obj.protocol.set(self.config.config_vars.vpn_L2TPv3_protocol)
		vpn_obj.assert_L2TPv3_default()
		vpn_obj.restore_Ipsec_default()
		
	def test_ath_11185_manual_gre(self):
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.controller.click()
		vpn_obj.assert_default_manual_gre()
		