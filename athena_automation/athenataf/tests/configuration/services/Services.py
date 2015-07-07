import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Services(ConfigurationTest):
	'''
	Test class for services test cases of configuration module.
	'''

	def test_ath_1438_airgroup_default(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.assert_airgroup_checkbox()
		services_page.assert_airgroup_checkbox_disabled()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_1439_enable_airgroup(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.enable_airgroup()
		services_page.assert_air_group_settings()
		services_page.click_all_air_group_options()
		self.take_s2_snapshot()
		services_page.air_group_restore_defaults()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(1)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_1440_airgroup_with_clearpass(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.enable_airgroup_clearpass()
		services_page.assert_new_cppm_server()
		services_page.creat_new_cppm_server()
		services_page.assert_cppm_server_feilds()
		self.take_s2_snapshot()
		services_page.restore_defaults()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_cppm_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(1)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_1441_rtls_aeroscout_default(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.assert_rtls_aeroscout_checkbox()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_1442_rtls_enable_rtls(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.enable_rtls()
		services_page.assert_rtls_enable()
		self.take_s2_snapshot()
		services_page.restore_rtls_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_6759_airgroup_nondefault_roles(self):
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security() 
		security_page.go_to_roles()
		security_page.create_new_role()
		services_page = self.LeftPanel.go_to_services()
		services_page.enable_airgroup_enable_air_print_box()
		self.take_s2_snapshot()
		services_page.restore_enable_airgroup_enable_air_print_box()
		security_page = self.LeftPanel.go_to_security() 
		# security_page.security_page()
		security_page.go_to_roles()
		security_page.delete_roles()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_1443_rtls_enable_aero_scout(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.enable_aero_scout()
		services_page.assert_rtls_3rd_party_aeroscout
		self.take_s2_snapshot()
		services_page.restore_aero_scout_defaults()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_7778_ale_cofig(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.enable_analytics_location_engine()
		self.take_s2_snapshot()
		services_page.restore_location_engine_defaults()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_7779_open_dns(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.open_dns_credentials()
		self.take_s2_snapshot()
		services_page.clear_dns_credenrials()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_7781_calea(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.conifgure_calea_settings()
		self.take_s2_snapshot()
		services_page.clear_calea_settings()  
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8254_calea_default_values(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.assert_calea_configuration_default()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_8255_network_integration_default_values(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.assert_network_integration_default()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_8256_network_integration_non_default_values(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.set_network_integration_non_default_values()
		self.take_s2_snapshot()
		services_page.reset_network_integration_fields()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_8257_open_dns_default_values(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.assert_open_dns_feilds()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_8258_rtls_analytics_and_location_engine_default_values(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.assert_rtls_analytics_and_location_engine()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_8259_rtls_analytics_and_location_engine_non_default_values(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.set_rtls_analytics_location_engine_non_default_values()
		self.take_s2_snapshot()
		services_page.disable_analytics_location_engine()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_8279_enable_guest_bojour_multicast(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.airgroup_bonjour_enable()
		self.take_s2_snapshot()
		services_page.restore_bonjour_defaults()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(3)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_9059_airgroup_settings_enable_air_print(self):
		self.take_s1_snapshot()
		services_page = self.LeftPanel.go_to_services()
		services_page.click_on_enable_air_group_checkbox()
		services_page.click_on_enable_air_print_checkbox()
		services_page.edit_air_print_disallowed_role()
		services_page.edit_air_print_disallowed_vlans_id()
		services_page.save_settings()
		self.take_s2_snapshot()
		services_page.click_on_enable_air_print_checkbox()
		services_page.click_on_enable_air_group_checkbox()
		services_page.save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
