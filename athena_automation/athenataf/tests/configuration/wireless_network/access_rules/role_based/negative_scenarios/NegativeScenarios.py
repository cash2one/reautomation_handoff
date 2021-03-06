import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class NegativeScenarios(ConfigurationTest):
	'''
	Test class for Negative Scenarios of role based module.
	'''

	def test_ath_8982_assert_no_of_characters_accepted_for_string_field(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()        
		basic_info = self.NetworkPage.create_new_network()
		vlan = basic_info.guest_network_info()
		security  = vlan.use_vlan_defaults()
		access_page = security.click_on_next()
		access_page.role_radio.click()
		access_page.no_of_characters_accepted_for_string_field()
		self.take_s2_snapshot()    
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_8983_role_string_role_options(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()    
		basic_info = self.NetworkPage.create_new_network()
		vlan = basic_info.guest_network_info()
		security  = vlan.use_vlan_defaults()
		access_page = security.click_on_next()
		access_page.role_radio.click()
		access_page.assert_string_and_role_options()
		self.take_s2_snapshot()    
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_8984_delete_newly_created_role(self):
		self.NetworkPage.delete_network_if_present()
		self.NetworkPage.delete_custom_guest_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan = basic_info.employee_network_info()
		security  = vlan.use_vlan_defaults()        
		security.enable_mac_authentication()
		access_page = security.click_on_next()
		access_page.role_radio.click()
		access_page.assert_role_delete_button()    
		access_page.finish_network_setup()
		basic_info = self.NetworkPage.create_new_network()        
		vlan = basic_info.create_guest_network()
		security  = vlan.use_vlan_defaults()        
		access_page = security.click_on_next()
		access_page.role_radio.click()
		access_page.create_employee_custom_role()          
		access_page.assert_role_delete_button(select_role=True)
		access_page.finish_network_setup()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.assert_delete_button_disabled()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_custom_guest_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_8985_assert_role_name_validation(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()            
		basic_info = self.NetworkPage.create_new_network()
		vlan = basic_info.guest_network_info()
		security  = vlan.use_vlan_defaults()
		access_page = security.click_on_next()
		access_page.role_radio.click()
		access_page.assert_role_name_validations()
		self.take_s2_snapshot()    
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_8993_assert_pre_auth_role_option(self):
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan = basic_info.guest_network_info()
		security  = vlan.use_vlan_defaults()
		security.set_splash_page_none()
		access_page = security.click_on_next()
		access_page.role_radio.click()
		access_page.assert_pre_auth_role_option() 
		self.take_s2_snapshot()    
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()