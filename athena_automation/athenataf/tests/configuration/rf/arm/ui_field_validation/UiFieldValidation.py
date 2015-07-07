import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class UiFieldValidation(ConfigurationTest):
	'''
		Test class for UiFieldValidation.
	'''
	def test_ath_8659_custom_channels(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.custom_channel_defaults()
		self.take_s2_snapshot()
		rf_page.revert_custom_channel_values()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11300_arm_section_field_validation(self):
		conf = self.config.config_vars
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.assert_band_streering_options()
		rf_page.assert_air_fairness_mode_options()
		rf_page.assert_client_match_options()
		rf_page.assert_rf_values()
		rf_page.assert_cm_calculating_interval_seconds_label()
		rf_page.validating_cm_calculating_interval()
		rf_page.assert_cm_neighbour_matching_style()
		rf_page.validating_client_control_cm_neighbor_matching()
		rf_page.validating_client_control_cm_threshold()
		rf_page.assert_slb_mode_value1()
		rf_page.set_rf_arm_access_point_control_customized_valid_channel('true')
		rf_page.assert_access_point_control_customized_valid_channels()
		rf_page.click_on_edit_24_ghz()
		rf_page.assert_24ghz_checkbox_values()
		rf_page.click_on_close_24_ghz()
		rf_page.click_on_edit_5_ghz()
		rf_page.assert_5ghz_checkbox_values1()
		rf_page.click_on_close_5_ghz()
		rf_page.assert_min_transmit_power_dropdown_values()
		rf_page.assert_max_transmit_power_dropdown_values()
		rf_page.assert_min_transmit_power_dropdown_values(True)
		rf_page.assert_max_transmit_power_dropdown_values(True)
		rf_page.assert_client_aware_options()
		rf_page.assert_scanning_options()
		rf_page.assert_wide_channel_bands_options()
		rf_page.assert_80_mhz_options()
		rf_page.click_on_rf_cancel_button()