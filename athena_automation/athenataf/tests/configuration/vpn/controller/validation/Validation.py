import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Validation(ConfigurationTest):
	'''
		Test class for Validation.
	'''
	
	def test_ath_8296_validate_IPSec_parameters_fields(self):
		self.take_s1_snapshot()
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.routing.click()
		vpn_obj.controller.click()
		vpn_obj.protocol.set(self.config.config_vars.vpn_def_protocol)
		protocol_default = vpn_obj.protocol.get_selected()
		config_protocol = self.config.config_vars.vpn_def_protocol
		self.assertEquals(protocol_default, config_protocol)
		vpn_obj.assert_IPsec_parameters_fields()
		vpn_obj.write_in_primary()
		vpn_obj.write_in_backup()
		vpn_obj.configure_IPSec_default()
		vpn_obj.assert_IPSec_fields()
		vpn_obj.save_settings()
		self.take_s2_snapshot()
		vpn_obj.revert_settings()
		vpn_obj.save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8297_validate_aruba_gre_parameters_fields(self):
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
		
	def test_ath_8298_validate_L2TPv3_tunnel_profile(self):
		self.take_s1_snapshot()
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.routing.click()
		vpn_obj.controller.click()		
		vpn_obj.protocol.set(self.config.config_vars.vpn_L2TPv3_protocol)
		vpn_obj.create_tunnel()
		vpn_obj.assert_tunnel_config_error()
		vpn_obj.setting_tunnel_values()
		vpn_obj.assert_tunnel()
		self.take_s2_snapshot()
		vpn_obj.tunnel_created.click()
		vpn_obj.delete_tunnel.click()
		vpn_obj.save_settings()
		# vpn_obj.restore_Ipsec_default()
		vpn_obj.buy_time()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8299_validate_manual_GRE_parameters(self):
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
	
	def test_ath_8331_validate_L2TPv3_session_profile(self):
		self.take_s1_snapshot()
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.routing.click()
		vpn_obj.controller.click()		
		vpn_obj.protocol.set(self.config.config_vars.vpn_L2TPv3_protocol)
		vpn_obj.create_tunnel()
		vpn_obj.assert_tunnel_config_error()
		vpn_obj.setting_tunnel_values()
		vpn_obj.assert_tunnel()
		vpn_obj.create_assert_session()
		self.take_s2_snapshot()
		vpn_obj.cancel_click()
		vpn_obj.buy_time()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_11187_validate_ipsec_parameter_fields(self):
		self.take_s1_snapshot()
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.write_in_primary()
		vpn_obj.assert_secs_between_test_packets()
		vpn_obj.assert_max_text_packet_loss()
		vpn_obj.set_primary_host_field(self.config.config_vars.incomplete_ip, 'true')
		vpn_obj.set_primary_host_field(self.config.config_vars.primary_add,'false')
		vpn_obj.set_primary_host_field(self.config.config_vars.invalid_hostname,'true')
		vpn_obj.set_primary_host_field(self.config.config_vars.hostname,'false')
		# vpn_obj.save_settings()
		vpn_obj.set_secs_between_test_packets('','true')
		vpn_obj.set_secs_between_test_packets(self.config.config_vars.alphanumeric,'true')
		vpn_obj.set_secs_between_test_packets(self.config.config_vars.zero_preceding_value,'true')
		vpn_obj.set_secs_between_test_packets(self.config.config_vars.invalid_interval_value,'true')
		vpn_obj.set_secs_between_test_packets(self.config.config_vars.negative_value,'true')
		vpn_obj.set_secs_between_test_packets(self.config.config_vars.interval,'false')
		# vpn_obj.save_settings()
		vpn_obj.set_max_allowed_test_packets_loss('','false')
		vpn_obj.set_max_allowed_test_packets_loss(self.config.config_vars.alphanumeric,'true')
		vpn_obj.set_max_allowed_test_packets_loss(self.config.config_vars.zero_preceding_value,'true')
		vpn_obj.set_max_allowed_test_packets_loss(self.config.config_vars.invalid_interval_value,'true')
		vpn_obj.set_max_allowed_test_packets_loss(self.config.config_vars.interval,'false')
		# vpn_obj.save_settings()
		vpn_obj.set_backup_host(self.config.config_vars.incomplete_ip,'true')
		vpn_obj.set_backup_host(self.config.config_vars.invalid_hostname,'true')
		vpn_obj.set_backup_host(self.config.config_vars.hostname,'false')
		vpn_obj.set_backup_host(self.config.config_vars.primary_add,'false')
		# vpn_obj.save_settings()
		vpn_obj.set_premption('true')
		vpn_obj.assert_hold_time_field_default_value()
		vpn_obj.set_hold_time('')
		vpn_obj.save_settings()
		vpn_obj.assert_hold_time_field('true')
		vpn_obj.set_hold_time(self.config.config_vars.alphanumeric)
		vpn_obj.save_settings()
		vpn_obj.assert_hold_time_field('true')
		vpn_obj.set_hold_time(self.config.config_vars.zero_preceding_value)
		vpn_obj.save_settings()
		vpn_obj.assert_hold_time_field('true')
		vpn_obj.set_hold_time(self.config.config_vars.gre_type)
		vpn_obj.save_settings()
		vpn_obj.assert_hold_time_field('true')
		vpn_obj.set_hold_time(self.config.config_vars.holdTime)
		vpn_obj.save_settings()
		vpn_obj.assert_hold_time_field('false')
		vpn_obj.set_reconnect_user_on_failover('true')
		vpn_obj.assert_reconnect_time_on_failover_field_default_value()
		vpn_obj.set_reconnect_time_on_failover('')
		vpn_obj.save_settings()
		vpn_obj.assert_reconnect_time_on_failover_field('true')
		vpn_obj.set_reconnect_time_on_failover(self.config.config_vars.valid_session_vlan)
		vpn_obj.save_settings()
		vpn_obj.assert_reconnect_time_on_failover_field('true')
		vpn_obj.set_reconnect_time_on_failover(self.config.config_vars.local_port)
		vpn_obj.save_settings()
		vpn_obj.assert_reconnect_time_on_failover_field('true')
		vpn_obj.set_reconnect_time_on_failover(self.config.config_vars.zero_preceding_value)
		vpn_obj.save_settings()
		vpn_obj.assert_reconnect_time_on_failover_field('true')
		vpn_obj.set_reconnect_time_on_failover(self.config.config_vars.alphanumeric)
		vpn_obj.save_settings()
		vpn_obj.assert_reconnect_time_on_failover_field('true')
		vpn_obj.set_reconnect_time_on_failover(self.config.config_vars.interval)
		vpn_obj.save_settings()
		vpn_obj.assert_reconnect_time_on_failover_field('false')
		self.take_s2_snapshot()
		vpn_obj.set_backup_host('','false')
		vpn_obj.set_primary_host_field('','false')
		vpn_obj.buy_time()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_11190_validate_manual_gre_parameter_fields(self):
		self.take_s1_snapshot()
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.set_protocol(self.config.config_vars.vpn_gre_protocol)
		vpn_obj.set_manual_gre_host(self.config.config_vars.incomplete_ip)
		vpn_obj.save_settings()
		vpn_obj.assert_manual_gre_host('true')
		vpn_obj.set_manual_gre_host(self.config.config_vars.primary_add)
		vpn_obj.save_settings()
		vpn_obj.assert_manual_gre_host('false')
		vpn_obj.set_manual_gre_host(self.config.config_vars.invalid_hostname)
		vpn_obj.save_settings()
		vpn_obj.assert_manual_gre_host('true')
		vpn_obj.set_manual_gre_host(self.config.config_vars.hostname)
		vpn_obj.save_settings()
		vpn_obj.assert_manual_gre_host('false')
		vpn_obj.set_gre_type('')
		vpn_obj.save_settings()
		vpn_obj.assert_gre_type_field('true')
		vpn_obj.set_gre_type(self.config.config_vars.valid_session_vlan)
		vpn_obj.save_settings()
		vpn_obj.assert_gre_type_field('false')
		vpn_obj.assert_per_ap_tunnel('false')
		vpn_obj.set_per_ap_tunnel('true')
		vpn_obj.save_settings()
		self.take_s2_snapshot()
		vpn_obj.set_protocol(self.config.config_vars.vpn_def_protocol)	
		vpn_obj.save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_11398_validate_aruba_gre_parameter_fields(self):
		self.take_s1_snapshot()
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.set_protocol(self.config.config_vars.vpn_ArubaGre_protocol)
		vpn_obj.write_in_primary()
		vpn_obj.assert_secs_between_test_packets()
		vpn_obj.assert_max_text_packet_loss()
		vpn_obj.set_primary_host_field(self.config.config_vars.incomplete_ip, 'true')
		vpn_obj.set_primary_host_field(self.config.config_vars.primary_add,'false')
		vpn_obj.set_primary_host_field(self.config.config_vars.invalid_hostname,'true')
		vpn_obj.set_primary_host_field(self.config.config_vars.hostname,'false')
		# vpn_obj.save_settings()
		vpn_obj.set_secs_between_test_packets('','true')
		vpn_obj.set_secs_between_test_packets(self.config.config_vars.alphanumeric,'true')
		vpn_obj.set_secs_between_test_packets(self.config.config_vars.zero_preceding_value,'true')
		vpn_obj.set_secs_between_test_packets(self.config.config_vars.invalid_interval_value,'true')
		vpn_obj.set_secs_between_test_packets(self.config.config_vars.negative_value,'true')
		vpn_obj.set_secs_between_test_packets(self.config.config_vars.interval,'false')
		# vpn_obj.save_settings()
		vpn_obj.set_max_allowed_test_packets_loss('','false')
		vpn_obj.set_max_allowed_test_packets_loss(self.config.config_vars.alphanumeric,'true')
		vpn_obj.set_max_allowed_test_packets_loss(self.config.config_vars.zero_preceding_value,'true')
		vpn_obj.set_max_allowed_test_packets_loss(self.config.config_vars.invalid_interval_value,'true')
		vpn_obj.set_max_allowed_test_packets_loss(self.config.config_vars.interval,'false')
		# vpn_obj.save_settings()
		vpn_obj.set_backup_host(self.config.config_vars.incomplete_ip,'true')
		vpn_obj.set_backup_host(self.config.config_vars.invalid_hostname,'true')
		vpn_obj.set_backup_host(self.config.config_vars.hostname,'false')
		vpn_obj.set_backup_host(self.config.config_vars.primary_add,'false')
		# vpn_obj.save_settings()
		vpn_obj.set_premption('true')
		vpn_obj.assert_hold_time_field_default_value()
		vpn_obj.set_hold_time('')
		vpn_obj.save_settings()
		vpn_obj.assert_hold_time_field('true')
		vpn_obj.set_hold_time(self.config.config_vars.alphanumeric)
		vpn_obj.save_settings()
		vpn_obj.assert_hold_time_field('true')
		vpn_obj.set_hold_time(self.config.config_vars.zero_preceding_value)
		vpn_obj.save_settings()
		vpn_obj.assert_hold_time_field('true')
		vpn_obj.set_hold_time(self.config.config_vars.gre_type)
		vpn_obj.save_settings()
		vpn_obj.assert_hold_time_field('true')
		vpn_obj.set_hold_time(self.config.config_vars.holdTime)
		vpn_obj.save_settings()
		vpn_obj.assert_hold_time_field('false')
		vpn_obj.set_reconnect_user_on_failover('true')
		vpn_obj.assert_reconnect_time_on_failover_field_default_value()
		vpn_obj.set_reconnect_time_on_failover('')
		vpn_obj.save_settings()
		vpn_obj.assert_reconnect_time_on_failover_field('true')
		vpn_obj.set_reconnect_time_on_failover(self.config.config_vars.valid_session_vlan)
		vpn_obj.save_settings()
		vpn_obj.assert_reconnect_time_on_failover_field('true')
		vpn_obj.set_reconnect_time_on_failover(self.config.config_vars.local_port)
		vpn_obj.save_settings()
		vpn_obj.assert_reconnect_time_on_failover_field('true')
		vpn_obj.set_reconnect_time_on_failover(self.config.config_vars.zero_preceding_value)
		vpn_obj.save_settings()
		vpn_obj.assert_reconnect_time_on_failover_field('true')
		vpn_obj.set_reconnect_time_on_failover(self.config.config_vars.alphanumeric)
		vpn_obj.save_settings()
		vpn_obj.assert_reconnect_time_on_failover_field('true')
		vpn_obj.set_reconnect_time_on_failover(self.config.config_vars.interval)
		vpn_obj.save_settings()
		vpn_obj.assert_reconnect_time_on_failover_field('false')
		vpn_obj.assert_per_ap_tunnel('false')
		vpn_obj.set_per_ap_tunnel('true')
		vpn_obj.save_settings()
		self.take_s2_snapshot()
		vpn_obj.set_per_ap_tunnel('false')
		vpn_obj.set_backup_host('','false')
		vpn_obj.set_primary_host_field('','true')
		vpn_obj.buy_time()
		vpn_obj.set_protocol(self.config.config_vars.vpn_def_protocol)
		vpn_obj.buy_time()
		vpn_obj.save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11189_validate_L2TPv3_tunnel_profile(self):
		conf = self.config.config_vars
		self.take_s1_snapshot()
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.controller.click()		
		vpn_obj.protocol.set(self.config.config_vars.vpn_L2TPv3_protocol)
		vpn_obj.create_tunnel()
		vpn_obj.save_tunnel_settings()
		vpn_obj.assert_required_fields_of_tunnel()
		vpn_obj.set_tunnel_profile_name(conf.tunnel_name)
		vpn_obj.set_tunnel_primary_adress(conf.incomplete_ip)
		vpn_obj.save_tunnel_settings()
		vpn_obj.assert_primary_peer_validation_error_message('invalid')
		vpn_obj.set_tunnel_primary_adress(conf.backup_text)
		vpn_obj.save_tunnel_settings()
		vpn_obj.assert_primary_peer_validation_error_message('valid')
		vpn_obj.set_backup_address(conf.incomplete_ip)
		vpn_obj.save_tunnel_settings()
		vpn_obj.assert_invalid_backup_peer_ip_address_message('invalid')
		vpn_obj.set_backup_address(conf.primary_text)
		vpn_obj.save_tunnel_settings()
		vpn_obj.assert_invalid_backup_peer_ip_address_message('valid')
		#bug #27386
		vpn_obj.set_peer_udp_port('')
		vpn_obj.set_local_udp_port('')
		vpn_obj.save_tunnel_settings()
		vpn_obj.assert_invalid_peer_udp_message('invalid')
		vpn_obj.assert_invalid_local_udp_message('invalid')
		vpn_obj.set_peer_udp_port(conf.invalid_zero_input)
		vpn_obj.set_local_udp_port(conf.invalid_zero_input)
		vpn_obj.save_tunnel_settings()
		vpn_obj.assert_invalid_peer_udp_message('invalid')
		vpn_obj.assert_invalid_local_udp_message('invalid')
		vpn_obj.set_peer_udp_port(conf.invalid_coa_port)
		vpn_obj.set_local_udp_port(conf.invalid_coa_port)
		vpn_obj.save_tunnel_settings()
		vpn_obj.assert_invalid_peer_udp_message('invalid')
		vpn_obj.assert_invalid_local_udp_message('invalid')
		vpn_obj.set_peer_udp_port(conf.valid_session_vlan)
		vpn_obj.set_local_udp_port(conf.valid_session_vlan)
		vpn_obj.save_tunnel_settings()
		vpn_obj.assert_invalid_peer_udp_message('valid')
		vpn_obj.assert_invalid_local_udp_message('valid')
		vpn_obj.set_hello_interval('')	
		vpn_obj.save_tunnel_settings()
		vpn_obj.validate_hello_interval_field()	
		vpn_obj.set_message_digest_type(conf.msg_type)
		vpn_obj.save_tunnel_settings()
		vpn_obj.assert_shared_key_validation_error_message('invalid')
		vpn_obj.set_message_digest_type(conf.none_default_value)
		vpn_obj.save_tunnel_settings()
		vpn_obj.assert_shared_key_field('False')
		vpn_obj.set_message_digest_type(conf.msg_type)
		vpn_obj.save_tunnel_settings()
		vpn_obj.assert_shared_key_field('True')
		vpn_obj.assert_checksum_default_value()
		vpn_obj.assert_failover_mode_default_value()
		vpn_obj.validate_fail_over_retry_interval()
		vpn_obj.validate_fail_over_retry_count()
		vpn_obj.set_backup_address('')
		vpn_obj.set_failover_retry(conf.zero_cookie_length)
		vpn_obj.save_tunnel_settings()
		vpn_obj.validate_mtu_field()
		vpn_obj.save_tunnel_settings()
		
	def test_ath_11191_validate_L2TPv3_session_proifile(self):
		conf=self.config.config_vars
		vpn_obj = self.LeftPanel.go_to_vpn()
		vpn_obj.assert_create_new_session_button()
		vpn_obj.create_new_session()
		
		vpn_obj.session_save_button()
		vpn_obj.assert_session_profile_name_error()
		# vpn_obj.assert_session_profile_tunnel_ip_error(True)
		# vpn_obj.assert_session_profile_tunnel_netmask_error(True)
		vpn_obj.set_profile_name(conf.session_name)
		vpn_obj.session_save_button()
		
		# vpn_obj.get_session_tunnel_name(conf."give tunnel name name ")
		vpn_obj.set_tunnel_ip_address(conf.incomplete_ip)
		vpn_obj.set_tunnel_netmask(conf.invalid_session_netmask)
		vpn_obj.session_save_button()
		# vpn_obj.assert_session_profile_tunnel_ip_error(True)
		# vpn_obj.assert_session_profile_tunnel_netmask_error(True)
		
		vpn_obj.set_tunnel_ip_address(conf.valid_ip)
		vpn_obj.set_tunnel_netmask(conf.route_mask)
		vpn_obj.session_save_button()
		vpn_obj.assert_session_profile_tunnel_ip_error(False)
		vpn_obj.assert_session_profile_tunnel_netmask_error(False)
		
		vpn_obj.validate_session_tunnel_vlan_id(conf.default_gre_type,True)
		vpn_obj.validate_session_tunnel_vlan_id(conf.session_tunnel_vlan_id,True)
		vpn_obj.validate_session_tunnel_vlan_id(conf.invalid_session_tunnel_vlan_id,True)
		vpn_obj.validate_session_tunnel_vlan_id(conf.zero_preceding_value,True)
		vpn_obj.validate_session_tunnel_vlan_id(conf.valid_session_vlan,False)
		
		vpn_obj.get_session_cookie_length(conf.zero_cookie_length)
		vpn_obj.set_cookie_length('4')
		vpn_obj.set_cookie(conf.cookie_field_8)
		vpn_obj.session_save_button()
		vpn_obj.assert_session_cookie_error_8x()
		vpn_obj.set_cookie_length('8')
		vpn_obj.set_cookie(conf.cookie_field_4)
		vpn_obj.session_save_button()
		vpn_obj.assert_session_cookie_error_16x()
		
		vpn_obj.validate_session_remote_end_id(conf.session_name,True)
		vpn_obj.validate_session_remote_end_id(conf.alphanumeric,True)
		vpn_obj.validate_session_remote_end_id(conf.valid_session_remote_end_id,False)
		vpn_obj.cancel_click()