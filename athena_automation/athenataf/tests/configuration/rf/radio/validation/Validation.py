import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Validation(ConfigurationTest):
	'''
		Test class for Validation.
	'''
	def test_ath_8644_edit_rf_radio_check(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.check_all_values()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11104_picklist_validation(self):
		conf = self.config.config_vars
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.check_all_values()
		rf_page.set_beacon_interval_24ghz(conf.beacon_interval_value_outside_range )
		rf_page.set_beacon_interval_5ghz(conf.beacon_interval_value_outside_range )
		rf_page.save_changes()
		rf_page.assert_beacon_interval_error_msg()
		rf_page.set_beacon_interval_24ghz(conf.beacon_interval_value_outside_range_600 )
		rf_page.set_beacon_interval_5ghz(conf.beacon_interval_value_outside_range_600 )
		rf_page.save_changes()
		rf_page.assert_beacon_interval_error_msg()
		rf_page.set_beacon_interval_24ghz(conf.beacon_interval_value_preceding_zero )
		rf_page.set_beacon_interval_5ghz(conf.beacon_interval_value_preceding_zero )
		rf_page.save_changes()
		rf_page.assert_beacon_interval_error_msg()
		rf_page.set_beacon_interval_24ghz(conf.beacon_interval_value_alpa_spl_char )
		rf_page.set_beacon_interval_5ghz(conf.beacon_interval_value_alpa_spl_char )
		rf_page.save_changes()
		rf_page.assert_beacon_interval_error_msg()
		rf_page.set_beacon_interval_to_dafault()		