import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest
from athenataf.lib.functionality.page.configuration.network.AccessPage import AccessPage
# access1 = AccessPage(test, browser, config)

class MixedGroup(ConfigurationTest):
	'''
	Test class for Mixed Group of APP RF
	'''
	
	def _asserting_access_page_option(self):
		access.delete_default_rule_if_present()
		access.click_on_role_based_add_rule()
		access.assert_service()
	
	def test_ath_6126_check_the_multiversion_control_tooltip(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.configure_employee_security()
		access.click_role_access()
		access.delete_default_rule_if_present()
		access.click_on_role_based_add_rule()
		access.assert_service()
		access.asserting_rule_type_options()
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.click_on_role_based_add_rule()
		access.assert_service()
		access.asserting_rule_type_options(bandwidth = False)
		access.click_on_cancel_button()
		
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.wired_employee_network_info()
		security = vlan_obj.wired_vlan_defaults()
		access = security.wired_security_defaults()
		access.click_role_access()
		access.delete_default_rule_if_present()
		access.click_on_role_based_add_rule()
		access.assert_service()
		access.asserting_rule_type_options()
		access.click_network_access()
		access.delete_default_rule_if_present()
		access.click_on_role_based_add_rule()
		access.assert_service()
		access.asserting_rule_type_options(bandwidth = False)
		access.click_on_cancel_button()
		
		security = self.LeftPanel.go_to_security()
		security.clicking_on_role_accordion()
		security.delete_default_rule_if_present()
		security.clicking_on_add_rule()
		security.assert_service()
		security.asserting_rule_type_options()
		security.click_on_cancel_button()
		
	def test_ath_6128_check_the_multiversion_control_tooltip(self):
		conf = self.config.config_vars
		self.take_s1_snapshot()
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		firmware_page.upgrade_firmware_using_custom_build_option(conf.version_firmware_2,"IAP_1")
		firmware_page.upgrade_firmware()
		firmware_page.asserting_device_upgrade_status()
		# self.connect_device()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()		

	def test_ath_6129_check_the_multiversion_control_tooltip(self):
		conf = self.config.config_vars
		self.take_s1_snapshot()
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		firmware_page.upgrade_firmware_using_custom_build_option(conf.version_firmware,"IAP_1")
		firmware_page.upgrade_firmware()
		firmware_page.asserting_device_upgrade_status()
		# self.connect_device()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_6127_access_rule_configuration(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		access = security.configure_employee_security()
		access.click_role_access()
		access.delete_default_rule_if_present()
		access.create_allow_any_to_all_rule()
		access.create_vlan_rule_assignment()
		access.click_on_role_based_add_rule()
		access.creating_captive_portal_rule()
		access.click_on_role_based_add_rule()
		access.creating_calea_rule()
		access.click_on_role_based_add_rule()
		access.creating_bandwidth_contract_rule()
		access.creating_service_application_rule()
		access.create_rule_with_webtegory_travel_deny()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()