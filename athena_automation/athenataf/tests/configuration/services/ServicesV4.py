import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class ServicesV4(ConfigurationTest):
	'''
	Test class for services test cases of IAP 4.0
	'''
	def test_ath_3979_field_value_validation(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.assert_calea_support_settings()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_3980_calea_configuration(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.conifgure_calea_settings()
		self.take_s2_snapshot()
		services_page.reset_calea_fields()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_4567_field_value_validation(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.assert_rtls_analytics_location_engine()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_4568_change_ale_configuration(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.assert_rtls_analytics_location_engine()
		self.take_s2_snapshot()
		services_page.disable_analytics_location_engine()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()               