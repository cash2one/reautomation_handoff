import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Okc(ConfigurationTest):
	'''
	Test class for network configuration wired network.
	'''

	def _create_employee_network(self,voice=False,wpa2_wap=False):
		self.take_s1_snapshot()
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		if voice:
			virtual_lan = basic_info.voice_network_info()
		else:
			virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		if wpa2_wap:
			access = security.configure_enterprise_security(both=True)
		else:
			access = security.configure_enterprise_security()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def _check_key_management(self,voice=False):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		if voice:
			virtual_lan = basic_info.voice_network_info()
		else:
			virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		security.assert_okc_options()

	def test_ath_3949_employee_enterprise_wpa2(self):
		self._create_employee_network()

	def test_ath_3950_employee_enterprise_wpa_wpa2(self):
		self._create_employee_network(wpa2_wap=True)

	def test_ath_3951_voice_enterprise_wpa2(self):
		self._create_employee_network(voice=True)

	def test_ath_3952_voice_enterprise_wpa_wpa2(self):
		self._create_employee_network(voice=True,wpa2_wap=True)

	def test_ath_3963_employee_network_check_okc_options(self):
		self.take_s1_snapshot()
		self._check_key_management()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_3964_voice_network_check_okc_options(self):
		self.take_s1_snapshot()
		self._check_key_management(voice=True)
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
