import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class FieldValidation(ConfigurationTest):
	'''
	Test class for FieldValidation test cases of configuration module.
	'''
	
	def test_ath_11314_rtls_configuration(self):
		services_page = self.LeftPanel.go_to_services()
		services_page.rtls_field_validation()
		
	def test_ath_11313_cppm_serverfor_airgroup(self):
		conf=self.config.config_vars
		system_page = self.LeftPanel.go_to_system_page()
		system_page.set_general_dynamic_proxy('enabled')
		system_page._save_settings()
		services_page = self.LeftPanel.go_to_services()
		services_page.click_on_enable_air_group_checkbox()
		services_page.set_cppm_server1(conf.new_cppm_server_name)
		services_page.assert_radius_radio('true')
		services_page.validate_server_radio_fields()
		services_page.validate_server_tacacs_radio_fields()
		services_page.validate_server_coa_only_fields()	
		
	def test_ath_11317_network_integration_field_validation(self):
		conf=self.config.config_vars
		system_page = self.LeftPanel.go_to_services()
		system_page.click_on_network_integration_accordion()
		system_page.validate_network_integration_fields()
		system_page.click_on_cancel()
		
	def test_ath_11316_calea(self):
		services_page = self.LeftPanel.go_to_services()
		services_page.assert_calea_support_settings()

	def test_ath_11315_opendns(self):
		conf=self.config.config_vars
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		logger.debug("ServicesPage : Clicking on Open dns Accordion. ")
		services_page.open_dns_accordion.click()
		services_page.assert_open_dns_empty_password()
		services_page.assert_open_dns_passwrd_with_blanks_inbetween()
		services_page.set_opendns_username_password(conf.invalid_dns_username,conf.User_Name1)
		if not services_page.save_setting :
			raise AssertionError('open dns is accepting invalid user name and password')
		services_page.set_opendns_username_password('','')
		if services_page.save_setting :
			raise AssertionError('open dns is not accepting valid user name and password')
		self.take_s2_snapshot()
		services_page.set_opendns_username_password('','')
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
					