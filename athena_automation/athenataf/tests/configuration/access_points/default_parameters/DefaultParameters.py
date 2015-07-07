import logging
logger = logging.getLogger('athenataf')


from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase

class DefaultParameters(AthenaGUITestCase):
	'''
	Test class  for DefaultParameters.
	'''

	def test_ath_8849_access_point_page_navigation(self):
		self.take_s1_snapshot()
		access_point_page = self.LeftPanel.go_to_access_points()
		access_point_page.assert_table_headers()
		access_point_page.assert_edit_button()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_8850_basic_info_default(self):
		self.take_s1_snapshot()
		access_point_page = self.LeftPanel.go_to_access_points()
		access_point_page.click_edit_iap()
		access_point_page.assert_basic_info_accordion_open()
		access_point_page.assert_basic_info_fields()
		access_point_page.assert_basic_info_default_values()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_8882_radio_default(self):
		self.take_s1_snapshot()
		access_point_page = self.LeftPanel.go_to_access_points()
		access_point_page.click_edit_iap()
		access_point_page.click_radio_accordion()
		access_point_page.assert_radio_default_values()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_8885_uplink_default(self):
		self.take_s1_snapshot()
		access_point_page = self.LeftPanel.go_to_access_points()
		access_point_page.click_edit_iap()
		access_point_page.click_uplink_accordion()
		access_point_page.assert_uplink_default_values()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11215_access_point_page_navigation(self):
		access_point_page = self.LeftPanel.go_to_access_points()
		access_point_page.assert_table_headers()
		access_point_page.assert_edit_button()
		access_point_page.assert_pagination_option()
		
	def test_ath_11216_basic_info_default(self):
		access_point_page = self.LeftPanel.go_to_access_points()
		access_point_page.click_edit_iap()
		access_point_page.assert_basic_info_accordion_open()
		access_point_page.assert_basic_info_fields()
		access_point_page.assert_basic_info_default_values()

	def test_ath_11217_radio_default(self):
		access_point_page = self.LeftPanel.go_to_access_points()
		access_point_page.click_edit_iap()
		access_point_page.click_radio_accordion()
		access_point_page.assert_radio_default_values()

	def test_ath_11218_uplink_default(self):
		access_point_page = self.LeftPanel.go_to_access_points()
		access_point_page.click_edit_iap()
		access_point_page.click_uplink_accordion()
		access_point_page.assert_uplink_default_values()
		
	def test_ath_11219_external_antenna_default(self):
		'''
		External Antenna  Supported IAPs ( IAP-92 / IAP-104 /  IAP-134 / IAP-224 ) 
		AP which not support External Antenna ( IAP-93 / IAP-105 / IAP-135 / IAP-225 )
		'''
		access_point_page = self.LeftPanel.go_to_access_points()
		access_point_page.select_particular_iap_type('IAP_1')
		access_point_page.click_external_antenna_accordion()
		access_point_page.assert_24ghz_and_5ghz_antenna_gain()
		access_point_page = self.LeftPanel.go_to_access_points()
		access_point_page.select_particular_iap_type('IAP_2')
		access_point_page.asserting_external_antenna_accordion()
		
		
	def test_ath_11239_configure_swarm_different_hardware_in_a_cluster(self):
		'''
		Configure cluster with AP135 as a Master and AP134 as a slave 
		slave details must be in IAP_2
		'''
		# remove snapshots and check the configured values in IAP-2 i.e slave
		
		conf=self.config.config_vars
		import os
		os.environ['device'] = "IAP_2"
		# self.take_s1_snapshot('AP_ENV')
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_master_slave_group()
		self.LeftPanel.go_to_network_page()
		access_point = self.LeftPanel.go_to_access_points()
		logger.debug('Clicking on edit button')
		access_point_page.select_particular_iap_type('IAP_2')
		access_point_page.click_external_antenna_accordion()
		access_point_page.set_24_ghz_antenna_gain(conf.channel_24g_value)
		access_point_page.set_5_ghz_antenna_gain(conf.transmit_power_24g_value2)
		access_point_page.save_settings()
		import os
		os.environ['device'] = "IAP_2"
		access_point.assert_backend('IAP_2','show ap-env',conf.channel_24g_value)
		access_point.assert_backend('IAP_2','show ap-env',conf.transmit_power_24g_value2)
		# self.take_s2_snapshot('AP_ENV')
		access_point_page.select_particular_iap_type('IAP_2')
		access_point_page.click_external_antenna_accordion()
		access_point_page.set_24_ghz_antenna_gain(None)
		access_point_page.set_5_ghz_antenna_gain(None)
		access_point_page.save_settings()
		
		
		