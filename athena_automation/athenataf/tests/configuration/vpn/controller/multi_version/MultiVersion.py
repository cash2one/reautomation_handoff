import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class MultiVersion(ConfigurationTest):
	'''
		Test class for Multi Version.
	'''
	
	def test_ath_11406_l2_specific_sublayer_multi_version(self):
		'''		
		suggested by Michael
		test case is executed on 4.1.1.7 and 4.1.2.3
		IAP_1 : 4.1.1.7
		IAP_2 : 4.1.2.3
		'''
		conf = self.config.config_vars
		import os
		os.environ['device'] = 'IAP_1'
		self.take_s1_snapshot()
		import os
		os.environ['device'] = "IAP_2"
		self.take_s1_snapshot()
		innerleftpanel = self.TopPanel.click_slider_icon()
		innerleftpanel.select_default_group()
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
		vpn_page.check_multiversion_text_availablility(False)
		vpn_page.configure_l2_specific_sublayer(True)
		vpn_page.save_session_click()
		
		import os
		os.environ['device'] = "IAP_1"
		self.take_s2_snapshot()
		
		import os
		os.environ['device'] = "IAP_2"
		self.take_s2_snapshot()
		vpn_page.delete_created_tunnel()
		vpn_page.save_settings()
		import os
		os.environ['device'] = "IAP_1"
		self.take_s3_snapshot()
		import os
		os.environ['device'] = "IAP_2"
		self.take_s3_snapshot()
		import os
		os.environ['device'] = "IAP_1"
		self.assert_s1_s2_diff(0)
		import os
		os.environ['device'] = "IAP_2"
		self.assert_s1_s2_diff(0)
		import os
		os.environ['device'] = "IAP_1"
		self.assert_s1_s3_diff()
		import os
		os.environ['device'] = "IAP_2"
		self.assert_s1_s3_diff()
		# self.clear()
		
	def test_ath_11186_aruba_gre_verify_multi_version(self):
		conf=self.config.config_vars
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_group1()
		vpn_page = self.LeftPanel.go_to_vpn()
		vpn_page.set_protocol(conf.vpn_ArubaGre_protocol)
		vpn_page.assert_multiversion_flag_availablility()