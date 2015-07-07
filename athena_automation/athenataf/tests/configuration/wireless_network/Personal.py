import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Personal(ConfigurationTest):
	'''
	Test class for test cases in Voice network.
	'''

	def test_ath_16_create_network_voice_wpa2_personal(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.voice_network_info()
		security       = virtual_lan.use_vlan_defaults()
		access          = security.set_wpa2_blacklisting_enable()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()