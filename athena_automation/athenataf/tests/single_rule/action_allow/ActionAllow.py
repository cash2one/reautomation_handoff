import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class ActionAllow(ConfigurationTest):
	'''
	Test class for action allow of single rule.
	'''
	def test_ath_8632_allow_any_to_all(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.assert_roaming_defaults(True, False)
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.create_allow_any_to_all_rule()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created('Any', 'To all destinations')
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8564_allow_adp_to_all(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.assert_roaming_defaults(True, False)
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.create_allow_adp_to_all_rule()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created('adp', 'To all destinations')
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8565_allow_bootp_to_a_particular_server(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.assert_roaming_defaults(True, False)
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.create_allow_bootp_to_a_particular_server_rule()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created('bootp', 'To a particular server')
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8566_allow_cfgm_tcp_except_a_particular_server(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.assert_roaming_defaults(True, False)
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.create_allow_cfgm_tcp_except_a_particular_server()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created('cfgm-tcp', 'Except to a particular server')
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8570_allow_custom_other_to_a_network(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.assert_roaming_defaults(True, False)
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.create_allow_custom_other_to_a_network_rule()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created('CUSTOM', 'To a network')
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8633_allow_http_proxy_except_to_a_network(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.assert_roaming_defaults(True, False)
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.create_allow_http_proxy_except_to_a_network_rule()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created('http-proxy2', 'Except to a network')
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8634_allow_custom_udp_to_a_domain_name(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.assert_roaming_defaults(True, False)
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.create_allow_custom_udp_to_a_domain_name_rule()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created('CUSTOM', 'To a Domain Name')
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8581_allow_https_to_all_destinations(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.assert_roaming_defaults(True, False)
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.create_allow_http_to_all_destinations_rule()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created('http', 'To all destinations')
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8587_allow_ldp_udp_to_a_particular_server(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.assert_roaming_defaults(True, False)
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.create_allow_ldp_udp_to_a_particular_server_rule()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created('lpd-udp', 'To a particular server')
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8635_allow_netbios_ns_except_to_a_particular_server(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.assert_roaming_defaults(True, False)
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.create_allow_netbios_ns_except_to_a_particular_server_rule()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created('netbios-ns', 'Except to a particular server')
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8636_allow_nterm_to_a_network(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.assert_roaming_defaults(True, False)
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.create_allow_nterm_to_a_network_rule()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created('nterm', 'To a network')
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8600_allow_pptp_except_to_a_network(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.assert_roaming_defaults(True, False)
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.create_allow_pptp_except_to_a_network_rule()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created('pptp', 'Except to a network')
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8637_allow_sip_tcp_to_a_domain_name(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.assert_roaming_defaults(True, False)
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.create_allow_sip_tcp_to_a_domain_name_rule()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created('sip-tcp', 'To a Domain Name')
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8589_allow_msrps_udp_to_a_particular_server(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.assert_roaming_defaults(True, False)
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.create_allow_msrpc_udp_except_to_a_server_rule()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created('msrpc-udp', 'Except to a particular server')
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8613_allow_syslog_to_a_network(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.assert_roaming_defaults(True, False)
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.create_allow_syslog_to_a_network()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created('syslog', 'To a network')
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8609_allow_snmp_to_a_domain_name(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.assert_roaming_defaults(True, False)
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.create_allow_snmp_to_a_domain_name()
		access.finish_network_setup()
		self.NetworkPage.assert_new_network()
		edit_network_page = self.NetworkPage.edit_network()
		edit_network_page.assert_new_rule_created('snmp', 'To a Domain Name')
		self.take_s2_snapshot()
		edit_network_page.delete_access_rule()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()