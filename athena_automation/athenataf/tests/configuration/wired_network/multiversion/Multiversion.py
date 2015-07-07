import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Multiversion(ConfigurationTest):
	'''
	Test class for  wired networks > Multiversion testcases.
	'''
	
	def test_ath_11291_multi_version_flag_validation_for_spanning_tree_configuration(self):
		basic_info = self.NetworkPage.create_new_network()
		basic_info._click_on_wired()
		basic_info.check_spanning_multversion_text_availablility()
		
	def test_ath_11290_external_authentication_with_captive_portal_profile(self):
		self.take_s1_snapshot()
		conf = self.config.config_vars
		self.NetworkPage.delete_wired_network_if_present()
		basic_info= self.NetworkPage.create_new_network()
		virtual_lan= basic_info.wired_guest_network_info()
		security= virtual_lan.wired_network_vlan_defaults()
		security.set_splash_page_type_value('External')
		security.set_wired_captive_portal_value()
		security.click_on_edit_captive_portal()
		security.set_captive_ip(conf.Captive_Role_Ip)
		logger.debug("Entering the captive Auth text value. ")
		security.captive_auth_text.set(conf.auth_text_edit)
		security.save_captive_profile_button()
		security.click_on_edit_captive_portal()
		security.set_captive_type()
		security.set_use_https('check')
		security.set_captive_ip(conf.captive_portal_ip)
		security.set_captive_url(conf.captive_url)
		security.save_captive_profile_button()
		security.wired_captive_portal.set(conf.Wired_Captive_Profile_New)
		logger.debug("Entering the captive Name value. ")
		security.captive_name.set(conf.Captive_Role_Name)
		logger.debug("Setting captive portal type. ")
		security.captive_type.set(conf.Captive_Role_Text)
		security.set_captive_ip(conf.captive_portal_ip)
		security.set_captive_url(conf.captive_portal_url)
		security.set_captive_port(conf.external_captive_port)
		security.set_secuirty_auto_url_whitelisting('check')
		security.captive_auth_text.set(conf.auth_text_edit)
		security.save_captive_profile_button()
		access = security.wired_guest_security_defaults()
		network_assign_page = access.click_next()
		network_assign_page.finish_network_setup()
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_wired_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()