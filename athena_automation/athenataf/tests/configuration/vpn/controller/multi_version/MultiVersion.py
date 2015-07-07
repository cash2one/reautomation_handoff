import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class MultiVersion(ConfigurationTest):
	'''
		Test class for Multi Version.
	'''
	
	def test_ath_11406_l2_specific_sublayer_multi_version(self):
		conf=self.config.config_vars
		self.take_s1_snapshot()
		conf = self.config.config_vars
		vpn_page = self.LeftPanel.go_to_vpn()
		vpn_page.set_protocol(conf.vpn_L2TPv3_protocol)
		vpn_page.create_tunnel()
		vpn_page.set_tunnel_profile_name(conf.tunnel_name)
		vpn_page.set_tunnel_primary_adress(conf.primary_text)
		vpn_page.set_message_digest_type(conf.msg_type_none)
		vpn_page.save_tunnel_settings()
		vpn_page.create_new_session()
		vpn_page.set_profile_name(conf.session_name)
		vpn_page.set_tunnel_ip_address(conf.valid_session_ip_adress)
		vpn_page.set_tunnel_netmask(conf.valid_session_netmask)
		vpn_page.set_tunnel_vlan(conf.valid_gre_type)
		vpn_page.set_cookie_length('4')
		vpn_page.set_cookie(conf.cookie_field_4)
		vpn_page.set_session_remote_end_id(conf.valid_session_remote_end_id)
		vpn_page.check_multiversion_text_availablility()
		vpn_page.configure_l2_specific_sublayer(True)
		vpn_page.save_session_click()
		
		
		inner_left_panel = self.TopPanel.click_slider_icon()
		if inner_left_panel.assert_group1_and_group2():
			if inner_left_panel.assert_sample_group_with_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.move_virtual_controller_from_Mygroup(group1=True)
				inner_left_panel.manage_group()
				manage_group_page.delete_specific_group(group1=True)
				
		create_group_page = inner_left_panel.add_group()
		create_group_page.set_group_name(conf.group_1)
		create_group_page.select_virtual_controller(create_group_page.select_vc)
		create_group_page.move_next()
		create_group_page._set_group_default_device_password1()
		
		inner_left_panel.select_default_with_one_vc()
		
		vpn_page = self.LeftPanel.go_to_vpn()
		vpn_page.set_protocol(conf.vpn_L2TPv3_protocol)
		vpn_page.assert_tunnel()
		vpn_page.assert_session()
		vpn_page.select_session()
		vpn_page.assert_multiversion_flag_unavailablility()
		
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_group1_with_one_vc()
		
		vpn_page = self.LeftPanel.go_to_vpn()
		vpn_page.set_protocol(conf.vpn_L2TPv3_protocol)
		vpn_page.create_tunnel()
		vpn_page.set_tunnel_profile_name(conf.tunnel_name)
		vpn_page.set_tunnel_primary_adress(conf.primary_text)
		vpn_page.set_message_digest_type(conf.msg_type_none)
		vpn_page.save_tunnel_settings()
		vpn_page.create_new_session()
		vpn_page.assert_disabled_l2_sublayer()
		
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.default_group.click()
		
		inner_left_panel = self.TopPanel.click_slider_icon()
		if inner_left_panel.assert_group1_and_group2():
			if inner_left_panel.assert_sample_group_with_vc_present():
				manage_group_page = inner_left_panel.manage_group()
				manage_group_page.move_virtual_controller_from_Mygroup(group1=True)
				inner_left_panel.manage_group()
				manage_group_page.delete_specific_group(group1=True)
				
		self.take_s2_snapshot()
		vpn_page = self.LeftPanel.go_to_vpn()
		vpn_page.delete_created_tunnel()
		vpn_page.save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11186_aruba_gre_verify_multi_version(self):
		conf=self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_group1()
		vpn_page = self.LeftPanel.go_to_vpn()
		vpn_page.set_protocol(conf.vpn_ArubaGre_protocol)
		vpn_page.assert_multiversion_flag_availablility()