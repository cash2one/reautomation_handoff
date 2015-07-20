import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class SecurityLevelOpen(ConfigurationTest):
	'''
		Test class for services test cases of SecurityLevelOpen.
	'''

	def test_ath_9428_field_validation(self):

		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.voice_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.set_roaming_to_enable()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_network_changes()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_9436_create_network_with_blacklisting_max_auth_failure(self):
		self.take_s1_snapshot()
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.voice_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.set_blacklisting_and_max_authentication_failure()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_network_blacklist_max_auth_changes()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
			
	def test_ath_9429_edit_open_employee_network_with_802r_roaming_mac_authentication_reauth_interv(self):
		self.take_s1_snapshot()
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.voice_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.set_802_roaming_dropdown()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.change_roaming_mac_authentication_settings()		
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_roaming_mac_authentication_changes()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
				
	def test_ath_9430_edit_open_employee_network_with_authentication_server_1(self):

		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.voice_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.set_mac_authentication_dropdown()
		access.finish_network_setup()
		self.take_s2_snapshot()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.change_to_external_server()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_authentication_server_changes()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_external_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_9431_edit_open_employee_network_with_authentication_server_2(self):
		self.take_s1_snapshot()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_2_external_servers()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.voice_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.set_mac_authentication_dropdown()
		access.finish_network_setup()
		self.take_s2_snapshot()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.change_auth_server_2_to_external_server()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.change_delimiter_uppercase_rauth()
		edit_network_page = self.NetworkPage.edit_network()		
		edit_network_page.assert_authentication_server_delimeter_uppercase_reauth_changes()
		self.NetworkPage.delete_network_if_present()						
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_2_external_servers()		
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_9432_edit_open_voice_network_with_accounting_interval_accounting_load_balancing_delimiter_character_uppercase_support(self):
		self.take_s1_snapshot()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_2_external_servers()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.voice_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.set_mac_authentication_auth_server_delimeter_uppercase_options()
		access.finish_network_setup()
		self.take_s2_snapshot()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.set_accounting_delimeter_loadbalance_uppercase()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.verify_accounting_delimeter_loadbalance_uppercase_changes()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_2_external_servers()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_9433_edit_open_voice_network_with_accounting_interval_uppercase_support_accounting_authentication_server(self):
		self.take_s1_snapshot()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_2_external_servers()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.voice_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.set_mac_authentication_auth_server_accounting_options()
		access.finish_network_setup()
		self.take_s2_snapshot()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.set_accounting_uppercase_auth_server()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.verify_accounting_uppercase_auth_server()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_2_external_servers()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_9434_edit_open_voice_network_with_accounting_interval_uppercase_supported(self):
		
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_2_external_servers()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.voice_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.set_mac_authentication_auth_server_accounting_options()
		access.finish_network_setup()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.set_accounting_uppercase_auth_server()
		self.LeftPanel.assert_delta_config_icon()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.verify_accounting_uppercase_auth_server()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_2_external_servers()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_9437_edit_open_voice_network_with_blacklisting_max_authentication_failure(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		conf = self.config.config_vars
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.voice_network_info()
		security = virtual_lan.use_vlan_defaults()
		security._set_phrase()
		security.configure_blacklisting(conf.blacklisting_option,conf.max_authentication_failure)
		access = security.click_on_next()
		access.finish_network_setup()
		edit_network = self.NetworkPage.edit_network()
		edit_network.click_security_accordion()
		edit_network.set_blacklisting_option()
		edit_network._save_settings()
		self.LeftPanel.assert_delta_config_icon()
		edit_network = self.NetworkPage.edit_network()
		edit_network.click_security_accordion()
		edit_network.assert_auth_server_settings(blacklisting_disable=True)
		edit_network.networks.click()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_9435_edit_open_voice_network_with_mac_authentication_accounting_accounting_interval_a(self):
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_2_external_servers()
		conf = self.config.config_vars
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.voice_network_info()
		security = virtual_lan.use_vlan_defaults()
		security.edit_network_with_mac_authentication_accounting_accounting_interval(open=True)
		access = security.click_on_next()        
		access.finish_network_setup()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.open_security_accordion()
		edit_network_page.mac_authentication.set(conf.blacklisting_disabled)
		edit_network_page.save_configuration()
		self.take_s2_snapshot()
		self.LeftPanel.assert_delta_config_icon()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_2_external_servers()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_12047_field_validation(self):
		self.take_s1_snapshot()
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.voice_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.set_roaming_to_enable()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_network_changes()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_12048_edit_open_employee_network_with_802r_roaming_mac_authentication_reauth_interv(self):
		self.take_s1_snapshot()
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.voice_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.set_802_roaming_dropdown()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.change_roaming_mac_authentication_settings()		
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_roaming_mac_authentication_changes()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
				
	def test_ath_12049_edit_open_employee_network_with_authentication_server_1(self):
		self.take_s1_snapshot()
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.voice_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.set_mac_authentication_dropdown()
		access.finish_network_setup()
		self.take_s2_snapshot()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.change_to_external_server()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_authentication_server_changes()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_external_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_12050_edit_open_employee_network_with_authentication_server_2(self):
		self.take_s1_snapshot()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_2_external_servers()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.voice_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.set_mac_authentication_dropdown()
		access.finish_network_setup()
		self.take_s2_snapshot()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.change_auth_server_2_to_external_server()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.change_delimiter_uppercase_rauth()
		edit_network_page = self.NetworkPage.edit_network()		
		edit_network_page.assert_authentication_server_delimeter_uppercase_reauth_changes()
		self.NetworkPage.delete_network_if_present()						
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_2_external_servers()		
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_12051_edit_open_voice_network_with_accounting_interval_accounting_load_balancing_delimiter_character_uppercase_support(self):
		self.take_s1_snapshot()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_2_external_servers()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.voice_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.set_mac_authentication_auth_server_delimeter_uppercase_options()
		access.finish_network_setup()
		self.take_s2_snapshot()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.set_accounting_delimeter_loadbalance_uppercase()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.verify_accounting_delimeter_loadbalance_uppercase_changes()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_2_external_servers()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_12052_edit_open_voice_network_with_blacklisting_uppercase_support_accounting_authentication_server(self):

		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_2_external_servers()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.voice_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.set_mac_authentication_auth_server_accounting_options()
		access.finish_network_setup()

		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.set_accounting_uppercase_auth_server()
		edit_network_page = self.NetworkPage.edit_network()
		self.take_s2_snapshot()
		edit_network_page.verify_accounting_uppercase_auth_server()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_2_external_servers()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_12053_edit_open_voice_network_with_accounting_interval_uppercase_supported(self):

		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_2_external_servers()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.voice_network_info()
		security = virtual_lan.use_vlan_defaults()
		security.open_voice_network_with_accounting_interval_uppercase_supported(open=True)
		access = security.click_on_next()
		access.finish_network_setup()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.open_security_accordion()
		edit_network_page.edit_open_voice_network_with_accounting_interval_uppercase_supported()
		self.LeftPanel.assert_delta_config_icon()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_open_voice_network_with_accounting_interval_uppercase_supported()
		edit_network_page.click_on_network()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_2_external_servers()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_12054_edit_open_voice_network_with_mac_authentication_accounting_accounting_interval_a(self):
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_2_external_servers()
		conf = self.config.config_vars
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.voice_network_info()
		security = virtual_lan.use_vlan_defaults()
		security.edit_network_with_mac_authentication_accounting_accounting_interval(open=True)
		access = security.click_on_next()        
		access.finish_network_setup()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.open_security_accordion()
		edit_network_page.mac_authentication.set(conf.blacklisting_disabled)
		edit_network_page.save_configuration()
		self.take_s2_snapshot()
		self.LeftPanel.assert_delta_config_icon()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_2_external_servers()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_12055_create_network_with_blacklisting_max_auth_failure(self):
		self.take_s1_snapshot()
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.voice_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.set_blacklisting_and_max_authentication_failure()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		self.take_s2_snapshot()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_network_blacklist_max_auth_changes()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_12056_edit_open_voice_network_with_blacklisting_max_authentication_failure(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.voice_network_info()
		security = virtual_lan.use_vlan_defaults()
		security._set_phrase()
		security.configure_blacklisting(conf.blacklisting_option,conf.max_authentication_failure)
		access = security.click_on_next()
		access.finish_network_setup()
		edit_network = self.NetworkPage.edit_network()
		edit_network.click_security_accordion()
		edit_network.set_blacklisting_option()
		edit_network._save_settings()
		self.LeftPanel.assert_delta_config_icon()
		edit_network = self.NetworkPage.edit_network()
		edit_network.click_security_accordion()
		edit_network.assert_auth_server_settings(blacklisting_disable=True)
		edit_network.networks.click()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()