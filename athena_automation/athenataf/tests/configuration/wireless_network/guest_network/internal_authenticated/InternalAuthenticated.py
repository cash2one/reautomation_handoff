import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class InternalAuthenticated(ConfigurationTest):
	'''
	Test class for External IAP Version 4
	'''

	def _delete_network_auth_server(self):
		'''
		Delete wireless and auth servers 
		'''
		self.NetworkPage.delete_network_if_present()
		self.NetworkPage.delete_wired_network_if_present()
		security_page = self.LeftPanel.go_to_security() 
		security_page.delete_authentication_server()
		security_page.delete_authentication_server2()
		security_page.click_walled_garden_accordion()
		security_page.click_walled_garden_link()
		if 	security_page.blacklist_delete_domain:
			security_page.blacklist_delete_domain.click()
		if security_page.whitelist_delete:
			security_page.whitelist_delete.click()
		if security_page.walled_save:
			security_page.walled_save.click()
		time.sleep(5)	
		self.LeftPanel.go_to_network_page()

	def test_ath_6814_two_auth_server_one_external_one_internal(self):
		
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.NetworkPage.delete_wired_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_Authenticated)
		security.create_external_radius_server_in_auth_server_one()
		security.set_authentication_server_2_value(conf.InternalServer)
		security.add_internal_sever_user()
		security.set_encryption('disable')
		security.configure_auth_server_settings(balancing = True)
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.NetworkPage.assert_new_network()
		self._delete_network_auth_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_6834_internal_server_one_external_one_internal(self):
		
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.NetworkPage.delete_wired_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		virtual_lan = basic_info.guest_network_info()
		security = virtual_lan.select_virtual_controller()
		security.configure_splash_page_type(conf.Splash_page_Authenticated)
		security.set_wispr(conf.Uppercase_Support_Enabled)
		security.create_external_radius_server_in_auth_server_one()
		security.create_external_radius_server_in_auth_server_two()
		security.add_internal_sever_user()
		security.set_encryption('disable')
		security.configure_auth_server_settings(balancing = True)
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.NetworkPage.assert_new_network()
		self._delete_network_auth_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()		