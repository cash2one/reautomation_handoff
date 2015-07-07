import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class NegativeTestCases(ConfigurationTest):
	'''
	Test class for test cases in Wireless Network.
	'''

	def test_ath_7064_not_allow_to_create_a_Duplicate_ssid(self):
		self.NetworkPage.delete_new_test_network_if_present()
		self.take_s1_snapshot()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.employee_network_info_with_specific_name('XXXX',True)
		security       = virtual_lan.use_vlan_defaults()
		access         = security.set_wpa2_blacklisting_enable()
		access.finish_network_setup()
		self.NetworkPage.assert_new_test_network()
		basic_info     = self.NetworkPage.create_new_network()
		basic_info.employee_network_info_with_specific_name('XXXX',False)
		basic_info.assert_duplicate_network_error_message()
		self.take_s2_snapshot()
		self.NetworkPage.delete_new_test_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_7066_wireless_dynamic_vlan_network_cannot_be_created_without_default_vlan(self):
		self.NetworkPage.delete_new_test_network_if_present()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.employee_network_info_with_specific_name('XXXX',True)		
		condition      = virtual_lan.check_dynamic_vlan_attribute_list()

		
	def test_ath_7067_wireless_static_vlan_network_cannot_be_created_without_entering_any_value_in_the_vlan_id_field(self):
		self.NetworkPage.delete_new_test_network_if_present()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.employee_network_info_with_specific_name('XXXX',True)
		virtual_lan.assert_static_vlan_required_message()

		
	def test_ath_7070_checking_movement_default_vlan(self):
		self.take_s1_snapshot()
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		virtual_lan.check_dynamic_vlan_attribute_list()
		virtual_lan.create_dynamic_vlan_assignment_rule()
		self.take_s2_snapshot()
		virtual_lan.assert_up_down()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_7074_checking_invalid_passphrase(self):
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		security.assert_invalid_passphrase()
		
	def test_ath_7072_checking_authentication_server_value_next(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		security.set_authentication_server_next()
		
	def test_ath_7073_checking_duplicate_user_name(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		security = virtual_lan.use_vlan_defaults()
		security.assert_exist_name_error()
		
	def test_ath_7068_checking_mac_address_attribute(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.employee_network_info()
		virtual_lan.assert_operator()
		
		
	def test_ath_7071_can_not_delete_the_role_if_it_is_used_by_others_networks(self):
		self.NetworkPage.delete_new_test_network_if_present()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_newly_created_role()
		security_page.back_to_network_page()
		self.take_s1_snapshot()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.employee_network_info_with_specific_name('XXXX',True)
		security       = virtual_lan.use_vlan_defaults()
		access         = security.set_wpa2_blacklisting_enable()
		access.click_role_access()
		access.create_role()
		access.assign_created_role()
		access.finish_network_setup()
		self.take_s2_snapshot()		
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.employee_network_info_with_specific_name('test2',True)
		security       = virtual_lan.use_vlan_defaults()
		access         = security.set_wpa2_blacklisting_enable()
		access.click_role_access()
		access.assert_delete_button_for_assigned_role()
		access.click_on_cancel_button()
		self.NetworkPage.delete_new_test_network_if_present()		
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_newly_created_role()
		security_page.back_to_network_page()	
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_7069_do_not_allow_to_create_a_duplicate_roles(self):
		self.NetworkPage.delete_new_test_network_if_present()		
		self.take_s1_snapshot()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.employee_network_info_with_specific_name('XXXX',True)
		security       = virtual_lan.use_vlan_defaults()
		access         = security.set_wpa2_blacklisting_enable()
		access.click_role_access()
		access.assert_duplicate_role_error_msg()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()		