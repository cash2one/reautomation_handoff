# Developed by : Ishan Anand
# On date : 30th Jun 2014

import logging
logger = logging.getLogger('athenataf')


from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase

class AccessPoints(AthenaGUITestCase):
	'''
	Test class for network configuration Access Points.
	'''

	def test_ath_4571_access_point_configuration(self):
		self.take_s1_snapshot()
		access_point = self.LeftPanel.go_to_access_points() 
		access_point.edit_access_point()		
		access_point.configure_preffered_master(enable=True)
		self.take_s2_snapshot()		
		access_point.edit_access_point()		
		access_point.configure_preffered_master(enable=False)	
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_1679_access_point_edit(self):
		self.take_s1_snapshot()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.click_access_point()
		access_point.assert_edit_button()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_1683_change_from_access_to_monitor(self):
		self.take_s1_snapshot()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.click_radio()
		access_point.set_mode_to_monitor()
		self.take_s2_snapshot()
		access_point.edit_access_point()
		access_point.click_radio()
		access_point.set_mode_to_access()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()


	def test_ath_1685_change_from_spectrum_to_monitor(self):
		self.take_s1_snapshot()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.click_radio()
		access_point.set_mode_to_spectrum()
		access_point.edit_access_point()
		access_point.click_radio()
		access_point.set_mode_to_monitor()
		self.take_s2_snapshot()
		access_point.edit_access_point()
		access_point.click_radio()
		access_point.set_mode_to_access()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_1686_change_from_monitor_to_access(self):
		self.take_s1_snapshot()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.click_radio()
		access_point.set_mode_to_monitor()
		access_point.edit_access_point()
		access_point.click_radio()
		access_point.set_mode_to_access()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_1687_radio_manual_assignment(self):
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.click_radio()
		access_point.assert_arm_assigned()
		access_point.set_radio_Administrator_assigned()
		access_point.edit_access_point()
		access_point.click_radio()
		access_point.set_radio_adaptive_assigned()

	def test_ath_1688_default_uplink_values(self):
		self.take_s1_snapshot()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.go_to_uplink()
		access_point.assert_default_values_of_uplink()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_1689_nondefault_uplink_values(self):
		self.take_s1_snapshot()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.go_to_uplink()
		access_point.set_nondefault_values_of_uplink()
		self.take_s2_snapshot()
		access_point.edit_access_point()
		access_point.go_to_uplink()
		access_point.set_default_value_of_etho_bridging()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_1681_change_name_validation(self):
		self.take_s1_snapshot()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.assert_name_error()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_9648_uplink_vlan_validation(self):
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.go_to_uplink()
		access_point.assert_uplink_management_vlan()

	def test_ath_11236_uplink_vlan_validation(self):
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.go_to_uplink()
		access_point.assert_uplink_management_vlan()
	
	def test_ath_11234_radio_validation(self):
		conf=self.config.config_vars
		self.take_s1_snapshot()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.click_access_point_edit_go_to_radio()
		access_point.set_24ghz_radio_Administrator_assigned()
		access_point.assert_radio_administrator_assigned_fields()
		access_point.set_radio_24ghz_band_admn_assgnd_channel(conf.channel_24g_value)
		access_point.save_settings()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.click_access_point_edit_go_to_radio()
		access_point.set_24ghz_radio_Administrator_assigned()
		access_point.assert_radio_administrator_assigned_fields()
		access_point.validating_radio_24ghz_transmit_power()
		access_point.page_down()
		access_point.set_5ghz_radio_Administrator_assigned()
		access_point.assert_5ghz_band_channel_drop_down()
		access_point.validating_radio_5ghz_transmit_power()
		access_point.click_on_cancel()
		self.take_s2_snapshot()
		access_point.set_radio_defaults()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_11233_basic_info_validation(self):
		conf = self.config.config_vars
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		# access_point.assert_name_error()  // waiting to fix error
		access_point.set_access_point_name("")
		
		access_point.edit_access_point()
		access_point.select_static_radio_button()
		access_point.assert_ip_netmask_gateway(conf.default_value)
		access_point.set_ip_address_value(conf.ip_address_value)
		access_point.set_netmask_value("")
		access_point.save_setting_button()
		access_point.assert_reboot_ap_warning()
		access_point.asserting_ip_netmask_gateway_dns_domain_error(False,True,False,False,False,False)
		access_point.set_netmask_value(conf.netmask_address)
		access_point.set_gateway_value()
		access_point.save_setting_button()
		access_point.asserting_ip_netmask_gateway_dns_domain_error(False,False,True,False,False,False)
		access_point.set_gateway_value(conf.gateway_error)
		access_point.save_setting_button()
		access_point.asserting_ip_netmask_gateway_dns_domain_error(False,False,False,True,False,False)
		access_point.set_gateway_value(conf.default_gateway)
		access_point.clicking_reboot_ap_warning()
		access_point.asserting_ip_netmask_gateway_dns_domain()
		access_point.set_ip_address_value()
		access_point.set_netmask_value()
		access_point.set_gateway_value()
		access_point.save_setting_button()
		access_point.asserting_ip_netmask_gateway_dns_domain_error(True,True,True,False,False,False)
		access_point.set_dns_server_value(conf.invalid_address)
		access_point.save_setting_button()
		access_point.asserting_ip_netmask_gateway_dns_domain_error(False,False,False,False,True,False)
		access_point.set_domain_name_value(conf.invalid_domain)
		access_point.save_setting_button()
		access_point.asserting_ip_netmask_gateway_dns_domain_error(False,False,False,False,False,True)
		access_point.set_domain_name_value(conf.valid_domain)
		access_point.save_setting_button()
		access_point.asserting_ip_netmask_gateway_dns_domain(False,False,False,False,False,True)