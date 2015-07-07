import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class RfV4(ConfigurationTest):
	'''
	Test class for RF Arm.
	'''
	
	def test_ath_3974_slb_mode(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.assert_slb_mode_value()
		rf_page.set_slb_mode_value()
		self.take_s2_snapshot()
		rf_page.set_slb_mode_value_to_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_3976_slb_parameters_renamed_to_cm(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.assert_client_match_parameters()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_3978_80_mhz_support(self):
		self.take_s1_snapshot()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.assert_80_mhz_support_field_and_default_value()
		rf_page.set_80_mhz_support_value('enable')
		self.take_s2_snapshot()
		rf_page.set_80_mhz_support_value('disable')
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
		
		