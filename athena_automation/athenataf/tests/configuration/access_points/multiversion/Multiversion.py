import logging
logger = logging.getLogger('athenataf')


from athenataf.lib.functionality.test.AccessPointsTest import AccessPointsTest

class Multiversion(AccessPointsTest):
	'''
	Test class  for Multiversion.
	'''

	def test_ath_11232_multi_version_check_basic_info_preferred_master(self):
		'''
		3.4 iap is no more supported so step 1 and 2 is skipped
		'''
		conf = self.config.config_vars
		self.take_s1_snapshot()
		access_point = self.LeftPanel.go_to_access_points() 
		access_point.edit_access_point()		
		access_point.configure_preffered_master(enable=True)	
		access_point.edit_access_point()
		self.browser.assert_drop_down_value(access_point.prefered_master,conf.preffered_master_enable, "Prefered master field is not set to 'Enable'")
		self.take_s2_snapshot()
		access_point.configure_preffered_master(enable=False)	
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()