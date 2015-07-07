import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class RfArm(ConfigurationTest):
	'''
	Test class for RF Arm.
	'''

	
	def test_ath_714_check_default_ui_and_values(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.assert_values()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_715_client_control_changes(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.set_client_control_values()
		rf_page.assert_client_control_values()
		self.take_s2_snapshot()
		rf_page.set_client_control_values_to_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_716_access_point_control_changes(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.set_access_point_control_values()
		rf_page.assert_access_point_control_values()
		self.take_s2_snapshot()
		rf_page.set_access_point_control_values_to_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_717_access_point_control_custom_channels(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.customize_channels()
		rf_page.assert_valid_channels()
		self.take_s2_snapshot()
		rf_page.customize_channels()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_6724_check_allowed_range_for_configs(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.set_out_of_range_cm_values()
		rf_page.assert_cm_error_msg()
		rf_page.set_cm_values_to_boundary()
		rf_page.assert_no_cm_error_msg()
		self.take_s2_snapshot()
		rf_page.set_cm_values_to_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8649_check_arm_client_control_band_streering_options(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.assert_band_streering_options()
		rf_page.set_different_band_streering_options()
		self.take_s2_snapshot()
		rf_page.set_band_streering_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8650_check_arm_client_control_airtime_fairness_options(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.assert_air_fairness_mode_options()
		rf_page.set_different_air_fairness_mode_options()
		self.take_s2_snapshot()
		rf_page.set_air_fairness_mode_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8651_check_arm_client_control_client_match_options(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.assert_client_match_options()
		rf_page.set_different_client_match_options()
		self.take_s2_snapshot()
		rf_page.set_client_match_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8652_check_cm_threshold_value(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.assert_cm_threshold_value()
		self.take_s2_snapshot()
		rf_page.set_cm_threshold_default_value()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8655_check_cm_client_aware_options(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.assert_client_aware_options()
		rf_page.set_different_client_aware_options()
		self.take_s2_snapshot()
		rf_page.set_client_aware_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8656_check_scanning_options(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.assert_scanning_options()
		rf_page.set_different_scanning_options()
		self.take_s2_snapshot()
		rf_page.set_scanning_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8657_check_wide_channel_bands_options(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.assert_wide_channel_bands_options()
		rf_page.set_different_wide_channel_bands_options()
		self.take_s2_snapshot()
		rf_page.set_wide_channel_bands_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8658_check_80_mhz_options(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.assert_80_mhz_options()
		rf_page.set_different_80_mhz_options()
		self.take_s2_snapshot()
		rf_page.set_80_mhz_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8189_check_help_options(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.check_rf_help()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_720_check_uncheck_regulatory_channel(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.customize_channels()
		rf_page.deselect_few_channels()
		self.take_s2_snapshot()
		rf_page.clear_channels()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	# def test_ath_6731_check_regulatory_power(self):
		# self.take_s1_snapshot()
		# rf_page = self.LeftPanel.go_to_rf_page()
		# rf_page.customize_channels()
		# rf_page.set_min_max_transmit_power()
		# self.take_s2_snapshot()
		# rf_page.customize_channels()
		# rf_page.set_default_min_max_transmit_power()
		# self.take_s3_snapshot()
		# self.assert_s1_s2_diff(None)
		# self.assert_s1_s3_diff()
		# self.clear()
		
	def test_ath_7829_check_calculation_interval(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.check_calculation_interval()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_7830_check_neighbour_interval(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.check_neighbour_interval()
		self.take_s2_snapshot()
		rf_page.set_default_neighbour_interval()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8107_change_all_default_config(self): 
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.change_config()
		self.take_s2_snapshot()
		rf_page.set_config_to_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8102_check_default_values(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.assert_rf_values()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8105_save_alert(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.modify_rf_arm_config()
		self.LeftPanel.go_to_rf_page()
		rf_page.assert_save_alert_pop_up(visible=True)
		self.LeftPanel.go_to_access_points()
		rf_page.assert_save_alert_pop_up()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

		
	def test_ath_8654_maximum_transmit_power(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.assert_transmit_power_dropdown_values(maximum=True)
		rf_page.modify_transit_power(maximum=True)
		self.take_s2_snapshot()		
		rf_page.set_access_point_control_values_to_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_8653_minimum_transmit_power(self):
		self.take_s1_snapshot()	
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.assert_transmit_power_dropdown_values()
		rf_page.modify_transit_power()
		self.take_s2_snapshot()		
		rf_page.set_access_point_control_values_to_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_11092_help_text_check(self):
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.check_rf_help()		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	
	