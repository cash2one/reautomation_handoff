import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DefaultParameters(ConfigurationTest):
	'''
		Test class for Default Parameters.
	'''
	
	def test_ath_8151_check_default_WIDS_settings(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.assert_detection_level_defaults()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11128_check_default_WIDS_settings(self):
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.assert_detection_level_defaults()
