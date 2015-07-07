import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class MultiVersion(ConfigurationTest):
	'''
	Test class for services test cases of configuration module.
	'''

	def test_ath_11318_calea(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.conifgure_calea_settings()
		self.take_s2_snapshot()
		services_page.reset_calea_fields()  
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11328_airgroup_fields_in_multiversion(self):
		services_page = self.LeftPanel.go_to_services()
		services_page.assert_airgroup_checkbox_disabled()
		services_page.enable_airgroup()
		services_page.assert_air_group_fields()
		
	def test_ath_11327_analytics_and_location_engine(self):
		self.take_s1_snapshot()
		conf = self.config.config_vars
		services_page = self.LeftPanel.go_to_services()
		services_page.rtls_click()
		services_page.click_analytics_location_engine_checkbox()
		services_page.assert_analytics_and_location_engine_fields()
		services_page.set_rtls_analytics_location_engine_fields(conf.service_server,conf.report_interval_location)
		services_page.save_settings()
		self.take_s2_snapshot()
		services_page.set_rtls_analytics_location_engine_fields(conf.empty,conf.report_interval_location)
		services_page.save_settings()
		services_page.click_analytics_location_engine_checkbox()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
	
	def test_ath_11319_network_integration(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.click_on_network_integration_accordion()
		services_page.edit_network_integration()
		services_page.assert_override_flag_button('False')
		self.take_s2_snapshot()
		services_page.reset_network_integration_fields()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()