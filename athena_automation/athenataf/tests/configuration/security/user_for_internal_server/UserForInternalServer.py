import logging
logger = logging.getLogger('athenataf')


from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class UserForInternalServer(ConfigurationTest):
	'''
		Test class for User For Internal Server.
	'''

	def test_ath_13339_check_tacacs_coa_default_values(self):
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_user_for_internal_server()	
		security_page.click_on_ok_button()
		self.browser.assert_element(security_page.user_name,'Username field is not found')
		self.browser.assert_element(security_page.pswd_txt,'Password field is not found')
		self.browser.assert_element(security_page.retype_pswd,'Retype field is not found')
		self.browser.assert_element(security_page.user_type,'Type field is not found')
		self.browser.assert_drop_down_value(security_page.user_type,'-Select-','Type dropdown not set to -Select- ')
		security_page.assert_internal_server_user_type_dropdown_values()		