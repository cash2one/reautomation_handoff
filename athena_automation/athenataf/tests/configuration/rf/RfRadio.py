import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class RfRadio(ConfigurationTest):
	'''
	Test class for RF Radio.
	'''

	
	def test_ath_719_2ghz_band_check_default_values(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.assert_radio_values_24_ghz()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_721_5ghz_band_check_default_values(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.assert_radio_values_5_ghz()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_718_2ghz_band_change_default(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.set_2ghz_band_values()
		rf_page.assert_new_2ghz_band_values()
		self.take_s2_snapshot()
		rf_page.set_2ghz_band_values_to_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_722_5ghz_band_change_default(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.set_5ghz_band_values()
		rf_page.assert_new_5ghz_band_values()
		self.take_s2_snapshot()
		rf_page.set_5ghz_band_values_to_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_6752_beacon_interval_range_validation(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.set_beacon_interval_outside_range()
		rf_page.assert_beacon_interval_error_msg()
		rf_page.assert_string_beacon_interval()
		self.take_s2_snapshot()
		rf_page.set_beacon_interval_to_dafault()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8185_edit_rf_options(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.assert_beacon_error_msg()
		rf_page.set_2ghz_band_field()
		rf_page.set_5ghz_band_field()
		self.take_s2_snapshot()
		rf_page.set_2ghz_band_values_to_default()
		rf_page.set_5ghz_band_values_to_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8184_check_radio_default_values(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.open_radio_accordion()
		rf_page.assert_radio_default_values()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8190_enable_help_button(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.enable_help()
		rf_page.assert_help_option()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_11105_radio_help_text(self):
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.enable_help()
		rf_page.assert_help_option()				
		
		
		
		
		
		
		
		
		
		
		