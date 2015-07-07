import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class EditAndDelete(ConfigurationTest):
	'''
	Test class for EditAndDelete testcases.
	'''

	def test_ath_6958_currently_created_network_ssid_can_not_be_deleted_in_role_based_wirless_network(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		security = vlan_obj.use_vlan_defaults()
		access = security.set_key_management_wpa_personal()
		access.click_role_access()
		access.assert_role_delete_button(select_role=False)



	def test_ath_6959_vlan_assignment_rule_with_ap_group_attribute_should_be_deleteable(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		vlan_obj.create_dynamic_vlan_assignment_rule_with_differnt_attribute('AP-Group')
		vlan_obj.delete_dynamic_vlan_assignment_rule_with_differnt_attribute()

	def test_ath_6974_vlan_assignment_rule_with_acct_input_gigawords_attribute_should_be_deleteable(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		vlan_obj.create_dynamic_vlan_assignment_rule_with_differnt_attribute('Acct-Input-Gigawords')
		vlan_obj.delete_dynamic_vlan_assignment_rule_with_differnt_attribute()


	def test_ath_6975_vlan_assignment_rule_with_mac_address_and_dhcp_options_attribute_should_be_deleteable(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		vlan_obj.create_dynamic_vlan_assignment_rule_with_differnt_attribute('mac-address-and-dhcp-options')
		vlan_obj.delete_dynamic_vlan_assignment_rule_with_differnt_attribute()


	def test_ath_6969_vlan_assignment_rule_with_acct_interim_interval_attribute_should_be_deleteable(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		vlan_obj.create_dynamic_vlan_assignment_rule_with_differnt_attribute('Acct-Interim-Interval')
		vlan_obj.delete_dynamic_vlan_assignment_rule_with_differnt_attribute()


	def test_ath_6970_vlan_assignment_rule_with_acct_link_count_attribute_should_be_deleteable(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		vlan_obj.create_dynamic_vlan_assignment_rule_with_differnt_attribute('Acct-Link-Count')
		vlan_obj.delete_dynamic_vlan_assignment_rule_with_differnt_attribute()


	def test_ath_6967_vlan_assignment_rule_with_acct_input_octets_attribute_should_be_deleteable(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		vlan_obj.create_dynamic_vlan_assignment_rule_with_differnt_attribute('Acct-Input-Octets')
		vlan_obj.delete_dynamic_vlan_assignment_rule_with_differnt_attribute()


	def test_ath_6968_vlan_assignment_rule_with_acct_input_packets_attribute_should_be_deleteable(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		vlan_obj.create_dynamic_vlan_assignment_rule_with_differnt_attribute('Acct-Input-Packets')
		vlan_obj.delete_dynamic_vlan_assignment_rule_with_differnt_attribute()


	def test_ath_6973_vlan_assignment_rule_with_acct_output_gigawords_attribute_should_be_deleteable(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		vlan_obj.create_dynamic_vlan_assignment_rule_with_differnt_attribute('Acct-Output-Gigawords')
		vlan_obj.delete_dynamic_vlan_assignment_rule_with_differnt_attribute()


	def test_ath_6972_vlan_assignment_rule_with_acct_multi_session_id_attribute_should_be_deleteable(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		vlan_obj.create_dynamic_vlan_assignment_rule_with_differnt_attribute('Acct-Multi-Session-Id')
		vlan_obj.delete_dynamic_vlan_assignment_rule_with_differnt_attribute()


	def test_ath_6960_vlan_assignment_rule_with_arap_features_attribute_should_be_deleteable(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.employee_network_info()
		vlan_obj.create_dynamic_vlan_assignment_rule_with_differnt_attribute('ARAP-Features')
		vlan_obj.delete_dynamic_vlan_assignment_rule_with_differnt_attribute()


	def test_ath_6966_validate_vlan_assignment_with_acct_input_gigawords(self):
		self.NetworkPage.delete_network_if_present()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.employee_network_info()
		virtual_lan.validate_acct_input_gigawords()

	def test_ath_6963_validate_vlan_assignment_with_ARAP_zone_access(self):
		self.NetworkPage.delete_network_if_present()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.employee_network_info()
		virtual_lan.validate_ARAP_zone_access()

	def test_ath_6957_validate_delete_default_value(self):
		self.NetworkPage.delete_network_if_present()
		basic_info     = self.NetworkPage.create_new_network()
		virtual_lan    = basic_info.employee_network_info()
		virtual_lan.validate_delete_default_value()

	def test_ath_7003_default_role_for_the_role_assignment_rules_should_not_be_editable(self):
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		basic_info = network_page.create_new_network()
		vlan_page = basic_info.employee_network_info()
		security_page = vlan_page.use_vlan_defaults()
		access_page = security_page.set_default_settings()
		access_page.click_role_radio_and_click_finish_button()
		network_page = self.LeftPanel.go_to_network_page()
		edit_network_page = network_page.edit_network()
		edit_network_page._click_access_accordion()
		edit_network_page.assert_role_radio_role_assignment_rules_default_role_edit_disable()       

	def test_ath_7004_default_role_for_the_role_assignment_rules_should_not_be_deleteable(self):
		network_page = self.LeftPanel.go_to_network_page()
		network_page.delete_network_if_present()
		basic_info = network_page.create_new_network()
		vlan_page = basic_info.employee_network_info()
		security_page = vlan_page.use_vlan_defaults()
		access_page = security_page.set_default_settings()
		access_page.click_role_radio_and_click_finish_button()
		network_page = self.LeftPanel.go_to_network_page()
		edit_network_page = network_page.edit_network()
		edit_network_page._click_access_accordion()
		edit_network_page.assert_role_radio_role_assignment_rules_default_role_delete_disable()

	def test_ath_6946_the_field_name_in_basic_info_option_should_have_proper_validation_check(self):
		self.NetworkPage.delete_network_if_present()
		basic_info = self.NetworkPage.create_new_network()
		basic_info.name_field_validation('1234567assssssddddddddddddddddddddd','invalid','max_length')
		basic_info.name_field_validation('"dd','invalid','spcl_char')		