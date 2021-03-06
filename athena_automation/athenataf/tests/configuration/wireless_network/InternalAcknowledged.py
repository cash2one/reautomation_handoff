import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class InternalAcknowledged(ConfigurationTest):
	'''
		Test class for Internal Acknowledge of guest networks.
	'''
	
	def test_ath_585_createnetwork_guest_internal_acknowledge_encryption_none(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.guest_network_info()
		security       = virtual_lan.use_vlan_defaults()
		access   	   = security.configure_guest_security(acknowledged=True)
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_587_internal_server_static_wep(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		network_page = self.LeftPanel.go_to_network_page()
		self.take_s1_snapshot()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.setting_wpa_personal_internal_server('8-63')
		access_page = security.click_on_next()
		access_page.finish_network_setup()
		network_page = self.LeftPanel.go_to_network_page()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.wired_guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.setting_wpa_personal_internal_server('64')
		access_page = security.click_on_next()
		access_page.finish_network_setup()
		self.LeftPanel.assert_delta_config_icon()
		self.take_s2_snapshot()
		self.LeftPanel.assert_delta_config_icon()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_wired_network_if_present()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_589_static_wep(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		network_page = self.LeftPanel.go_to_network_page()
		self.take_s1_snapshot()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.setting_static_wep_with_password('128')
		access_page = security.click_on_next()
		access_page.finish_network_setup()
		network_page = self.LeftPanel.go_to_network_page()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.wired_guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.setting_static_wep_with_password('64')
		access_page = security.click_on_next()
		access_page.finish_network_setup()
		self.LeftPanel.assert_delta_config_icon()
		self.take_s2_snapshot()
		self.LeftPanel.assert_delta_config_icon()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_wired_network_if_present()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_586_wpa_2_personal_two_authserver_internal_and_external(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		network_page = self.LeftPanel.go_to_network_page()
		self.take_s1_snapshot()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.setting_wpa_2_personal_two_authserver_internal_and_external('8-63',authserver=True)
		access_page = security.click_on_next()
		access_page.finish_network_setup()
		network_page = self.LeftPanel.go_to_network_page()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.wired_guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.setting_wpa_2_personal_two_authserver_internal_and_external('64',authserver=False)
		access_page = security.click_on_next()
		access_page.finish_network_setup()
		self.LeftPanel.assert_delta_config_icon()
		self.take_s2_snapshot()
		self.LeftPanel.assert_delta_config_icon()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_wired_network_if_present()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security() 
		security_page.delete_authentication_server()
		security_page.delete_authentication_server2()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()