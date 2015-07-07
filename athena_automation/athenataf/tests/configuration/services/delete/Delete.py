import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Delete(ConfigurationTest):
	'''
	Test class for Delete test cases of configuration module.
	'''
	
	def test_ath_11337_airgroup(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.enable_airgroup_options()
		self.take_s2_snapshot()
		services_page.restore_defaults()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11345_rtls_configuration(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.enable_rtls()
		services_page.enable_analytics_location_engine()
		services_page.enable_aero_scout()
		self.take_s2_snapshot()
		services_page.restore_rtls_default()
		services_page.restore_location_engine_defaults()
		services_page.restore_aero_scout_defaults()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11347_app_rf(self):
		services_page = self.LeftPanel.go_to_services()
		services_page.click_on_app_rf_accordion()
		services_page.assert_enable_dpi('false')
		self.take_s1_snapshot()
		services_page.set_enable_dpi('true')
		services_page.save_settings()
		services_page.set_enable_dpi('false')
		services_page.save_settings()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11346_network_integration(self):
		services_page = self.LeftPanel.go_to_services()
		services_page.click_on_network_integration_accordion()
		self.take_s1_snapshot()
		services_page.edit_network_integration()
		self.take_s2_snapshot()
		services_page.reset_network_integration_fields()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()		
		
		
		
		