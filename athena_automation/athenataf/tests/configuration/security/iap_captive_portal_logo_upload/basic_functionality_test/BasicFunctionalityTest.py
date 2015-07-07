import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class BasicFunctionalityTest(ConfigurationTest):
	'''
	Test class for IAP Captive Portal Logo Upload.
	'''
	
	def test_ath_8861_verify_captive_portal_logo_save_on_group_with_mix_iap_versions(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.click_on_next()
		security.set_splash_page_type_value(conf.Splash_page_Acknowledged)
		if not security.logo_upload:
			raise AssertionError("Captive Portal 'Upload' button is not displayed")
		logger.debug('SecurityPage : Clicking on upload button')
		fu = self.get_file_uploader(self.config.config_vars.logo_5_kb)
		fu.start()
		security.logo_upload.click()
		fu.join()
		logger.debug('SecurityPage : Clicking on save button')
		security.save_button.click()
		
		security.check_captive_portal_logo_text_availablility()
		security.assert_splash_logo_preview_change_delete_options()
		security.click_on_preview_splash_page()
		if not security.splash_banner_logo:
			raise AssertionError("Splash banner logo is not Present")
		security.click_on_preview_splash_page_close()
		
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8862_verify_captive_portal_logo_save_on_iap_41(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.click_on_next()
		security.set_splash_page_type_value(conf.Splash_page_Acknowledged)
		if not security.logo_upload:
			raise AssertionError("Captive Portal 'Upload' button is not displayed")
		logger.debug('SecurityPage : Clicking on upload button')
		fu = self.get_file_uploader(self.config.config_vars.logo_5_kb)
		fu.start()
		security.logo_upload.click()
		fu.join()
		logger.debug('SecurityPage : Clicking on save button')
		security.save_button.click()
		
		security.check_captive_portal_logo_text_availablility()
		security.assert_splash_logo_preview_change_delete_options()
		security.click_on_preview_splash_page()
		if not security.splash_banner_logo:
			raise AssertionError("Splash banner logo is not Present")
		security.click_on_preview_splash_page_close()
		
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()