import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class WiredGuestNetwork(ConfigurationTest):
	'''
	Test class for network configuration wired network.
	'''

	def _create_text_captive_role(self,delete=False):
		self.take_s1_snapshot()
		if delete: 
			self._delete_captive_role_if_present()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_wired_network_if_present()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.wired_guest_network_info()
		security= virtual_lan.wired_network_vlan_defaults()
		access = security.create_captive_portal_profile(text=True)
		network_assignment=access.use_access_defaults()
		network_assignment.finish_network_setup()
		self.NetworkPage.assert_wired_network()
		self.take_s2_snapshot()
		self._delete_captive_role_if_present()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_wired_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def _create_external_auth_captive_portal(self):
		self.take_s1_snapshot()
		self._delete_captive_role_if_present()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_wired_network_if_present()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.wired_guest_network_info()
		security= virtual_lan.wired_network_vlan_defaults()
		access = security.create_captive_portal_profile()
		network_assignment=access.use_access_defaults()
		network_assignment.finish_network_setup()
		self.NetworkPage.assert_wired_network()
		self.take_s2_snapshot()
		self.NetworkPage.delete_wired_network_if_present()
		self._delete_captive_role_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def _create_wired_guest_network_default_captive_portal(self):
		self.take_s1_snapshot()
		self.NetworkPage.delete_wired_network_if_present()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.wired_guest_network_info()
		security= virtual_lan.wired_network_vlan_defaults()
		access = security.set_default_captive_role()
		network_assignment=access.use_access_defaults()
		network_assignment.finish_network_setup()
		self.NetworkPage.assert_wired_network()
		self.take_s2_snapshot()
		self.NetworkPage.delete_wired_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()


	def _delete_captive_role_if_present(self):
		security_page = self.LeftPanel.go_to_security()
		if security_page.is_external_captive_profile_present():
			security_page.delete_external_captive_role()
			
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

	def test_ath_4012_assert_check_splash_page_options(self):
		self.take_s1_snapshot()
		self.NetworkPage.delete_wired_network_if_present()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.wired_guest_network_info()
		security= virtual_lan.wired_network_vlan_defaults()
		security.check_splash_page_options()
		access_page = security.click_on_next()
		network_assignment_page = access_page.click_on_next()
		network_assignment_page.finish_network_setup()
		self.take_s2_snapshot()
		self.NetworkPage.delete_wired_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_4013_create_wired_guest_network_default_captive_portal(self):
		self._create_wired_guest_network_default_captive_portal()

	def test_ath_4014_create_external_auth_text_captive_portal(self):
		self._create_external_captive_portal()

	def test_ath_4015_create_external_auth_captive_portal(self):
		self._create_external_auth_captive_portal()

	def test_ath_4016_create_multiple_guest_networks_captive_portal(self):
		self.take_s1_snapshot()
		self.NetworkPage.delete_wired_network_if_present()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.wired_guest_network_info()
		security= virtual_lan.wired_network_vlan_defaults()
		access = security.set_default_captive_role()
		network_assignment=access.use_access_defaults()
		network_assignment.finish_network_setup()
		self.NetworkPage.assert_wired_network()
		self.NetworkPage.delete_wired_network_if_present()
		self._delete_captive_role_if_present()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_wired_network_if_present()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.wired_guest_network_info()
		security= virtual_lan.wired_network_vlan_defaults()
		access = security.create_captive_portal_profile(text=True)
		network_assignment=access.use_access_defaults()
		network_assignment.finish_network_setup()
		self.NetworkPage.assert_wired_network()
		self.take_s2_snapshot()
		self._delete_captive_role_if_present()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_wired_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()


	def test_ath_4017_delete_external_captive_role(self):
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security() 
		if security_page.is_external_captive_profile_present():
			security_page.delete_external_captive_role()
			self.take_s2_snapshot()
			self.take_s3_snapshot()
			self.assert_s1_s2_diff(0)
			self.assert_s1_s3_diff()
			self.clear()
		else:
			self._create_text_captive_role()
			self.LeftPanel.go_to_network_page()
			security_page = self.LeftPanel.go_to_security()
			self.take_s2_snapshot()
			security_page.delete_external_captive_role()
			security_page.assert_captive_role_deleted()
			self.take_s3_snapshot()
			self.assert_s1_s2_diff(0)
			self.assert_s1_s3_diff()
			self.clear()

	def test_ath_6855_security_splash_type_internal_ack(self):
		self.NetworkPage.delete_wired_network_if_present()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.wired_guest_network_info()
		security= virtual_lan.wired_network_vlan_defaults()
		security.set_splash_page_type_value('Internal - Acknowledged')
		security.enable_mac_authentication1()
		security.create_security_internal_server_new_user()
		security.set_splash_page_visuals_field_values()
		security.preview_splash_page.click()
		import time
		time.sleep(5)
		security.preview_splash_page_close.click()
		access_page = security.click_on_next()
		network_assnmnt_page = access_page.use_access_defaults()
		network_assnmnt_page.finish_network_setup()
		self.NetworkPage.delete_wired_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.go_to_user_for_internal_server()
		security_page.delete_user_for_internal_server()

