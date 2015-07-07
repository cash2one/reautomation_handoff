import logging
logger = logging.getLogger('athenataf')


from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class ExternalCaptivePortal(ConfigurationTest):
	'''
		Test class for External Captive Portal.
	'''

	def test_ath_11042_non_default_radius_authentication(self):
		conf = self.config.config_vars
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_captive_portal_testradius1()
		security_page.click_on_external_captive_accordion()
		security_page.create_new_captive_portal_1(name=conf.captive_text_1,type=conf.captive_role_type,ip=conf.auth_radius_ip1,url=conf.url_22,port=conf.auth_port_valid,http1=False,captive_portal=conf.deny_internet1,whitelisting=None,redirect_url_text=conf.redirect_url_new)
		security_page.edit_captive_portal(type=conf.captive_role_type,ip=conf.ip_address_new,port=conf.auth_port_valid,captive_portal=conf.deny_internet1,whitelisting=True)
		self.take_s2_snapshot()
		security_page.delete_captive_portal_testradius1()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_11043_non_default_authentication_text(self):
		conf = self.config.config_vars
		self.take_s1_snapshot()
		security_page = self.LeftPanel.go_to_security()
		security_page.delete_captive_portal_testradius1()
		security_page.click_on_external_captive_accordion()
		security_page.create_new_captive_portal_1(name=conf.captive_text_1,type=conf.Captive_Role_Text,ip=conf.ip_address1,url=conf.url1,port=conf.port_new,captive_portal=conf.allow_internet1,whitelisting=None,redirect_url_text=conf.redirect_url1,auth_text=conf.ldap_pass_phrase,http1=False)		
		self.take_s2_snapshot()
		security_page.delete_captive_portal_testradius1()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()	

	def test_ath_13754_create_new_external_captive_portal(self):
		conf = self.config.config_vars
		security_page = self.LeftPanel.go_to_security() 
		security_page.click_on_external_captive_accordion()
		security_page.deleting_cp1()
		self.take_s1_snapshot()
		security_page.create_new_captive_portal_1(conf.cp_name,conf.captive_role_type,conf.cp_ip,conf.cp_url,conf.cp_port,auth_text=None,http1=False)
		logger.debug('SecurityPage : Editing Cp1 ...Clicking on Edit button')
		security_page.edit_external_captive.click()
		security_page.edit_cp1(conf.Captive_Role_Text,conf.Captive_Role_Text)
		security_page.save_settings()
		self.take_s2_snapshot()
		security_page.click_on_external_captive_accordion()
		security_page.deleting_cp1()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11039_field_validation_radius_authentication(self):
		security_page = self.LeftPanel.go_to_security()
		security_page.click_on_external_captive_accordion()
		security_page.create_new_captive_portal_1(name=conf.Role_Name,type=conf.captive_role_type,ip=conf.dynm_blklst_default_time,url='',port=conf.invalid_radius_server_retry_count_0,auth_text=None,http1=False)
		logger.debug('SecurityPage : Asserting Validation error messages')
		if not security_page.captive_ip_error and security_page.captive_url_req_error and security_page.captive_port_error :
			raise AssertionError('SecurityPage : Validation error message not displayed for invalid ip, invalid port and url')
		logger.debug('SecurityPage: Clicking on cancel button')
		security_page.cancel.click()

	def test_ath_11040_default_value_radius_authentication(self):
		security_page = self.LeftPanel.go_to_security()
		security_page.click_on_external_captive_accordion()
		logger.debug('SecurityPage: Clicking on edit button')
		security_page.edit_captive_portal.click()
		security_page.assert_captive_portal_type_and_options()
		logger.debug('SecurityPage: Asserting default captive portal name')
		self.browser.assert_element(security_page.default_captive_name_disabled,'Default name is editable')
		security_page.assert_default_captive_portal_values()
		security_page.set_captive_portal_type(self.config.config_vars.Captive_Role_Radius_Authentication)
		logger.debug('Asserting use https')
		if not security_page.security_use_https:
			raise AssertionError('use https is not visible')
		logger.debug('SecurityPage: Clicking on cancel button')
		security_page.cancel.click()					
