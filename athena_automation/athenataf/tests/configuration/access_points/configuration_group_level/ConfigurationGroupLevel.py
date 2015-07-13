import logging
logger = logging.getLogger('athenataf')
import traceback
import time

from athenataf.lib.functionality.test.AccessPointsTest import AccessPointsTest

class ConfigurationGroupLevel(AccessPointsTest):
	'''
	Test class  for ConfigurationGroupLevel.
	'''
	def test_ath_8888_set_access_point_name(self):
		self.take_s1_snapshot()
		access_point = self.LeftPanel.go_to_access_points()
		default_name = access_point.get_ap_default_name()
		access_point.assert_name_error()
		access_point.set_access_point_name(self.config.config_vars.new_access_point_name)
		access_point.assert_new_access_name()
		self.take_s2_snapshot()
		access_point.set_access_point_name(default_name)		
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8969_radio_custom_channel_and_power(self):
		self.take_s1_snapshot()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_radio_custom_channel_and_power()
		self.take_s2_snapshot()
		access_point.set_radio_defaults()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8968_validate_access_points_radio_custom_channel_and_power(self):
		access_point = self.LeftPanel.go_to_access_points()
		access_point.validate_access_points_radio_custom_channel_and_power()
		
	def test_ath_11229_radio_custom_channel_and_power(self):
		self.take_s1_snapshot()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_radio_custom_channel_and_power()
		self.take_s2_snapshot()
		access_point.set_radio_defaults()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11230_radio_custom_channel_and_power(self):
		self.take_s1_snapshot()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.click_uplink_accordion()
		access_point.set_nondefault_values_of_uplink()
		access_point.reboot_ok_button.click()
		self.take_s2_snapshot()
		access_point.edit_access_point()
		access_point.click_uplink_accordion()
		access_point.assert_nondefault_values_of_uplink()
		access_point.set_default_value_of_uplink_management_vlan()
		access_point.set_default_value_of_etho_bridging()
		access_point.reboot_ok_button.click()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_11221_edit_static_ip(self):
		conf = self.config.config_vars
		self.take_s1_snapshot()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.select_static_radio_button()
		access_point.assert_basic_info_ip_address_static_fields()
		access_point.get_current_server_ip_and_set()
		access_point.set_netmask_value(conf.netmask_address)
		access_point.set_gateway_value(conf.valid_default_gateway)
		access_point.set_dns_server_value(conf.dns_server1)
		access_point.set_domain_name_value(conf.domain_name_valid1)
		access_point.save_settings()
		access_point.reboot_ok_button.click()
		self.LeftPanel.go_to_monitoring_page()
		access=self.LeftPanel.go_to_monitoring_access_points()
		access.iap.click()
		access.get_eth_ip_and_compare()
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.get_ip_from_dhcp.click()
		access_point.save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11226_radio_mode_monitor_to_access(self):
		conf = self.config.config_vars
		self.take_s1_snapshot()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.click_radio_accordion()
		access_point.set_radio_mode(conf.monitor_wifi_mode)
		access_point.set_radio_mode(conf.access_wifi_mode)
		access_point.save_setting_button()
		access_point.reboot_ok_button.click()
		self.LeftPanel.go_to_monitoring_page()
		access=self.LeftPanel.go_to_monitoring_access_points()
		access.iap.click()
		access.get_wireless_interface_role_and_compare()
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.click_radio_accordion()
		access_point.set_mode_to_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11227_radio_mode_aceess_to_spectrum(self):
		conf = self.config.config_vars
		self.take_s1_snapshot()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.click_radio_accordion()
		access_point.set_mode_to_spectrum()
		access_point.reboot_ok_button.click()
		self.LeftPanel.go_to_monitoring_page()
		self.LeftPanel.go_to_monitoring_page()
		access=self.LeftPanel.go_to_monitoring_access_points()
		access.iap.click()
		access.get_wireless_interface_role_and_compare1()
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.click_radio_accordion()
		access_point.set_mode_to_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11228_radio_mode_spectrum_to_access(self):
		self.take_s1_snapshot()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.click_radio()
		access_point.set_mode_to_spectrum()
		access_point.reboot_ok_button.click()
		access_point.edit_access_point()
		access_point.click_radio()
		access_point.set_mode_to_access()
		access_point.reboot_ok_button.click()
		self.LeftPanel.go_to_monitoring_page()
		access = self.LeftPanel.go_to_monitoring_access_points()
		logger.debug('AccessPointsPage : Selecting iap')
		access.iap.click()
		logger.debug('AccessPointsPage : Checking Mode')
		if not access.access_mode :
			raise AssertionError('Mode is not set to access')
		logger.debug('AccessPointsPage : Checking 2.4GHZ Role')
		if not access.wireless_role_0.get_attribute_value('title') == 'access':
			raise AssertionError('Mode is not set to access')
		logger.debug('AccessPointsPage :  Checking 5GHZ Role')
		if not access.wireless_role_1.get_attribute_value('title') == 'access':
			raise AssertionError('Mode is not set to access')			
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11224_radio_mode_monitor_to_spectrum(self):
		import os
		os.environ['device'] = "IAP_1"
		self.take_s1_snapshot('AP_ENV')
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.click_radio()
		access_point.set_mode_to_monitor()
		# access_point.reboot_ok_button.click()	
		access_point.edit_access_point()
		access_point.click_radio()
		access_point.set_mode_to_spectrum()
		# access_point.reboot_ok_button.click()
		self.LeftPanel.go_to_monitoring_page()
		access = self.LeftPanel.go_to_monitoring_access_points()
		time.sleep(60)
		# raw_input('se')
		logger.debug('AccessPointsPage : Selecting iap')
		access.iap.click()
		time.sleep(30)
		logger.debug('AccessPointsPage : Checking Mode')
		if not access.spectrum_mode :
			raise AssertionError('Mode is not set to spectrum')
		logger.debug('AccessPointsPage : Checking 2.4GHZ Role')
		if not access.wireless_role_0.get_attribute_value('title') == 'spectrum':
			raise AssertionError('Mode is not set to spectrum')
		logger.debug('AccessPointsPage :  Checking 5GHZ Role')
		if not access.wireless_role_1.get_attribute_value('title') == 'spectrum':
			raise AssertionError('Mode is not set to spectrum')		
		import os
		os.environ['device'] = "IAP_1"
		self.take_s2_snapshot('AP_ENV')
		self.LeftPanel.go_to_network_page()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.click_radio()
		access_point.set_mode_to_default()
		# access_point.reboot_ok_button.click()
		import os
		os.environ['device'] = "IAP_1"
		self.take_s3_snapshot('AP_ENV')
		import os
		os.environ['device'] = "IAP_1"
		self.assert_s1_s2_diff(0)
		import os
		os.environ['device'] = "IAP_1"
		self.assert_s1_s3_diff()
		# self.clear()
		
		
	def test_ath_11220_basic_info_edit_name(self):
		self.take_s1_snapshot()
		access_point = self.LeftPanel.go_to_access_points()
		default_name = access_point.get_ap_default_name()
		access_point.assert_name_error()
		access_point.set_access_point_name(self.config.config_vars.new_access_point_name)
		access_point.assert_new_access_name()
		access_point.configure_preffered_master(enable=True)
		self.take_s2_snapshot()
		access_point.set_access_point_name(default_name)
		access_point.configure_preffered_master(enable=False)		
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11223_radio_mode_access_to_monitor(self):
		'''
		reboot steps are remaining
		'''
		self.take_s1_snapshot()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.click_radio()
		access_point.set_mode_to_monitor()
		logger.debug('Clicking on OK button')
		access_point.ok.click()
		self.LeftPanel.go_to_monitoring_page()
		access = self.LeftPanel.go_to_monitoring_access_points()
		logger.debug('AccessPointsPage : Selecting iap')
		access.iap.click()
		logger.debug('AccessPointsPage : Checking Mode')
		if not access.monitor_mode :
			raise AssertionError('Mode is not set to Monitoring')
		logger.debug('AccessPointsPage : Checking 2.4GHZ Role')
		if not access.wireless_role_0.get_attribute_value('title') == 'monitor' :
			raise AssertionError('2.4GHZ Role is not set to Monitoring')
		logger.debug('AccessPointsPage :  Checking 5GHZ Role')
		if not access.wireless_role_1.get_attribute_value('title') == 'monitor' :
			raise AssertionError('5GHZ is not set to Monitoring')
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.click_radio()
		access_point.set_mode_to_access()
		logger.debug('Clicking on OK button')
		access_point.ok.click()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11222_edit_dhcp_ip(self):
		'''
		reboot steps are remaining
		'''
		self.take_s1_snapshot()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.select_static_radio_button()
		access_point.set_ip_address_value(conf.ip_address_value)
		access_point.set_netmask_value(conf.netmask_address)
		access_point.set_gateway_value(conf.default_gateway)
		access_point.save_settings()
		logger.debug('Clicking on OK button')
		access_point.ok.click()
		access_point.edit_access_point()
		logger.debug('Selecting DHCP')
		access_point.get_ip_from_dhcp.click()
		access_point.save_settings()
		logger.debug('Clicking on OK button')
		access_point.ok.click()
		self.LeftPanel.go_to_monitoring_page()
		access = self.LeftPanel.go_to_monitoring_access_points()
		logger.debug('AccessPointsPage : Selecting iap')
		access.iap.click()
		logger.debug('AccessPointsPage : Checking IP Address')
		access.get_eth_ip_and_compare()
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.click_radio()
		access_point.set_mode_to_access()
		logger.debug('Clicking on OK button')
		access_point.ok.click()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()		
		
	def test_ath_11225_radio_mode_spectrum_to_monitor(self):
		import os
		os.environ['device'] = "IAP_1"
		self.take_s1_snapshot('AP_ENV')
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.click_radio()
		access_point.set_mode_to_monitor()
		# access_point.ok.click()
		self.LeftPanel.go_to_monitoring_page()
		access = self.LeftPanel.go_to_monitoring_access_points()
		time.sleep(60)
		# raw_input('se')
		logger.debug('AccessPointsPage : Selecting iap')
		access.iap.click()
		time.sleep(30)
		logger.debug('AccessPointsPage : Checking Mode')
		if not access.monitor_mode :
			raise AssertionError('Mode is not set to Monitoring')
		logger.debug('AccessPointsPage : Checking 2.4GHZ Role')
		if not access.wireless_role_0.get_attribute_value('title') == 'monitor' :
			raise AssertionError('2.4GHZ Role is not set to Monitoring')
		logger.debug('AccessPointsPage :  Checking 5GHZ Role')
		if not access.wireless_role_1.get_attribute_value('title') == 'monitor' :
			raise AssertionError('5GHZ is not set to Monitoring')
		import os
		os.environ['device'] = "IAP_1"
		self.take_s2_snapshot('AP_ENV')
		self.LeftPanel.go_to_network_page()
		access_point = self.LeftPanel.go_to_access_points()
		access_point.edit_access_point()
		access_point.click_radio()
		access_point.set_mode_to_access()
		# access_point.ok.click()
		import os
		os.environ['device'] = "IAP_1"
		self.take_s3_snapshot('AP_ENV')
		import os
		os.environ['device'] = "IAP_1"
		self.assert_s1_s2_diff(0)
		import os
		os.environ['device'] = "IAP_1"
		self.assert_s1_s3_diff()
		# self.clear()

		
		
	def test_ath_11231_edit_default_external_antenna(self):
		conf = self.config.config_vars
		self.take_s1_snapshot('AP_ENV')
		access_point = self.LeftPanel.go_to_access_points()
		access_point.click_134_edit_iap()
		access_point.click_external_antenna_accordion()
		access_point.set_24_ghz_antenna_gain(conf.channel_24g_value)
		access_point.set_5_ghz_antenna_gain(conf.transmit_power_24g_value2)
		access_point.save_setting_button()
		time.sleep(10)
		self.take_s2_snapshot('AP_ENV')
		access_point.click_134_edit_iap()
		access_point.click_external_antenna_accordion()
		access_point.set_24_ghz_antenna_gain(value=None)
		access_point.set_5_ghz_antenna_gain(value=None)
		access_point.save_setting_button()
		time.sleep(10)
		self.take_s3_snapshot('AP_ENV')
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()