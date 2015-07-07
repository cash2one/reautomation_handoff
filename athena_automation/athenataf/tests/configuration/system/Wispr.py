import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Wispr(ConfigurationTest):
	'''
	Test class for System WISPR module.
	'''

	def test_ath_11369_check_default_values_of_wispr(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.wispr_accordion()
		system_page.assert_wispr_default_values()
		
	def test_ath_11377_check_non_default_values_of_wispr(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.wispr_accordion()
		self.take_s1_snapshot()
		system_page.set_iso_country_code(self.config.config_vars.iso_country_code)
		system_page.set_operator_name(self.config.config_vars.operator_name)
		system_page.set_ssid_zone(self.config.config_vars.ssid)
		system_page.set_location_name(self.config.config_vars.location_name)
		system_page._save_settings()
		system_page.wispr_accordion()
		system_page.set_ssid_zone(self.config.config_vars.ssid_2)
		system_page.set_operator_name(self.config.config_vars.operator_name_2)
		system_page.set_164_area_code(self.config.config_vars.area_code)
		system_page._save_settings()
		self.take_s2_snapshot()
		system_page.wispr_accordion()
		system_page.set_wispr_default_value()
		system_page._save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11379_field_validation_in_wispr(self):
		'''
			Not added in excel waiting to fix error(BUG)
		'''
		system_page = self.LeftPanel.go_to_system_page()
		system_page.wispr_accordion()
		system_page.set_iso_country_code(self.config.config_vars.iso_country_code_2)
		system_page.set_164_area_code(self.config.config_vars.area_code_2)
		system_page.set_164_country_code(self.config.config_vars.e164_country_code)
		system_page.set_location_name(self.config.config_vars.location_name_2)		
		system_page._save_settings()
		#         For Assertion Message
		system_page.set_iso_country_code(self.config.config_vars.iso_country_code)	
		system_page._save_settings()
		#         For Assertion Message
		system_page.set_operator_name(self.config.config_vars.operator_name)
		system_page.set_ssid_zone(self.config.config_vars.ssid)
		system_page._save_settings()		
		#         For Assertion Message		
		
	def test_ath_11959_edit_created_wispr_values(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.wispr_accordion()
		self.take_s1_snapshot()	
		system_page.set_iso_country_code(self.config.config_vars.iso_country_code)
		system_page.set_operator_name(self.config.config_vars.operator_name)
		system_page.set_ssid_zone(self.config.config_vars.wifi_name1)
		system_page.set_location_name(self.config.config_vars.location_name)
		system_page._save_settings()
		system_page.wispr_accordion()
		system_page.set_iso_country_code(self.config.config_vars.iso_country_code1)
		system_page.set_operator_name(self.config.config_vars.operator_name1)
		system_page.set_ssid_zone(self.config.config_vars.ssid_value)
		system_page.set_location_name(self.config.config_vars.location_name3)
		system_page._save_settings()
		self.take_s2_snapshot()
		system_page.wispr_accordion()
		system_page.set_wispr_default_value()
		system_page._save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11378_delete_created_wispr(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.wispr_accordion()
		self.take_s1_snapshot()
		system_page.set_iso_country_code(self.config.config_vars.iso_country_code)
		system_page.set_ssid_zone(self.config.config_vars.wifi_name1)
		system_page.set_operator_name(self.config.config_vars.operator_name)
		system_page.set_location_name(self.config.config_vars.location_name)
		system_page._save_settings()
		self.take_s2_snapshot()
		system_page.wispr_accordion()
		system_page.set_wispr_default_value()
		system_page._save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		