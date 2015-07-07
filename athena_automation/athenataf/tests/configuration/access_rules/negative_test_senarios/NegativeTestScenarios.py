from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class NegativeTestScenarios(ConfigurationTest):
	'''
	Test class for Access Rule NegativeTestScenarios
	'''
	
	def test_ath_10991_check_disable_scanning_in_wired_employee_network(self): 	
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.wired_employee_network_info()
		security = vlan_obj.wired_vlan_defaults()
		security.wired_employee_security_defaults()
		access = security.return_acces_page()
		access.click_role_access()
		access.delete_default_rule_if_present()
		access._add_new_rule()
		logger('AccessPage: Checking Disable Scanning checkbox presence')
		access.browser.assert_element(access.new_disable_scaning_1, 'Disable Scanning CheckBox is present in Wired Network', False)