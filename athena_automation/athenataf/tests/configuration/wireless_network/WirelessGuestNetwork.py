import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class WirelessGuestNetwork(ConfigurationTest):
	'''
		Test class for network configuration wireless network.
	'''

	def _create_text_captive_role(self,delete=False):

		if delete:
			self._delete_captive_role_if_present()
		# self.LeftPanel.go_to_network_page()
		# self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.guest_network_info()
		security= virtual_lan.use_vlan_defaults()
		access = security.create_wireless_guest_captive_portal_profile(text=True)
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		self._delete_captive_role_if_present()
		# self.LeftPanel.go_to_network_page()
		# self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def _create_text_captive_role_network(self,delete=False):
		self.take_s1_snapshot()
		if delete:
			self._delete_captive_role_if_present()
		# self.LeftPanel.go_to_network_page()
		# self.NetworkPage.delete_network_if_present()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.guest_network_info()
		security= virtual_lan.use_vlan_defaults()
		access = security.create_wireless_guest_captive_portal_profile(text=True)
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		self._delete_captive_role_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()


	def _create_external_auth_captive_portal(self):
		self.take_s1_snapshot()
		self._delete_captive_role_if_present()
		# self.LeftPanel.go_to_network_page()
		# self.NetworkPage.delete_network_if_present()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.guest_network_info()
		security= virtual_lan.use_vlan_defaults()
		access = security.create_wireless_guest_captive_portal_profile()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		self._delete_captive_role_if_present()
		# self.LeftPanel.go_to_network_page()		
		# self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def _create_wireless_guest_network_default_captive_portal(self):
		self.take_s1_snapshot()
		self.NetworkPage.delete_network_if_present()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.guest_network_info()
		security= virtual_lan.use_vlan_defaults()
		access = security.set_default_captive_role(wireless=True)
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def _delete_captive_role_if_present(self):
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security() 
		security_page = self.LeftPanel.go_to_security() 
		if security_page.is_external_captive_profile_present():
			security_page.delete_external_captive_role()
		self.LeftPanel.go_to_network_page()
			
	def _create_external_captive_portal(self):
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security()
		security_page.click_on_external_captive_accordion()
		security_page.delete_captive_portal()
		security_page.click_on_external_captive_accordion()
		security_page.create_new_captive_portal()
		security_page.click_on_external_captive_accordion()
		security_page.assert_new_captive_portal()
		self.take_s2_snapshot()
		security_page.delete_captive_portal()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_4006_check_splash_page_options(self):
		self.take_s1_snapshot()
		self.NetworkPage.delete_network_if_present()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.guest_network_info()
		security= virtual_lan.use_vlan_defaults()
		security.check_splash_page_options(wireless=True)
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(4)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_4007_create_wireless_guest_network_default_captive_portal(self):
		self._create_wireless_guest_network_default_captive_portal()
		
	def test_ath_4008_create_external_auth_text_captive_portal(self):
		self._create_text_captive_role(delete=True)
		
	def test_ath_4009_create_external_auth_captive_portal(self):
		self._create_external_auth_captive_portal()
		
	def test_ath_4010_delete_external_captive_role(self):
		security_page = self.LeftPanel.go_to_security() 
		security_page.click_on_external_captive_accordion()
		security_page.delete_captive_portal()
		security_page.click_on_external_captive_accordion()
		security_page.create_new_captive_portal()
		security_page.click_on_external_captive_accordion()
		import time
		security_page.assert_new_captive_portal()
		time.sleep(2)
		security_page.delete_captive_portal()		
		self._create_text_captive_role_network(delete=True)
			
	def test_ath_4011_create_multiple_guest_networks_captive_portal(self):
		# self.take_s1_snapshot()
		# self.NetworkPage.delete_network_if_present()
		# basic_info= self.NetworkPage.create_new_network()
		# virtual_lan= basic_info.guest_network_info()
		# security= virtual_lan.use_vlan_defaults()
		# access = security.set_default_captive_role(wireless=True)
		# access.finish_network_setup()
		# self.NetworkPage.assert_new_network()
		# self.NetworkPage.delete_network_if_present()
		
		# self._create_text_captive_role(delete=True)
		
		# self._delete_captive_role_if_present()
		# self.LeftPanel.go_to_network_page()
		# self.NetworkPage.delete_network_if_present()
		# basic_info= self.NetworkPage.create_new_network()
		# virtual_lan= basic_info.guest_network_info()
		# security= virtual_lan.use_vlan_defaults()
		# access = security.create_wireless_guest_captive_portal_profile(text=True)
		# access.finish_network_setup()
		# self.NetworkPage.assert_new_network()
		# self.take_s2_snapshot()
		# self.NetworkPage.delete_network_if_present()
		# self.take_s3_snapshot()
		# self.assert_s1_s2_diff(0)
		# self.assert_s1_s3_diff()
		# self.clear()
		
		self._create_external_captive_portal()
		


				