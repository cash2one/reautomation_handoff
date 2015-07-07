import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest
import time
class DifferentUserRoles(ConfigurationTest):
	'''
	Test class for Different User Roles.
	'''

	def test_ath_8872_verify_user_with_read_write_permission_can_upload_captive_portal_logo_on_iap_4_1(self):
		'''
		User with read/write permission has to be created.
		Logout and login as new user(read/write permission)
		'''
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		self.take_s1_snapshot()
		basic_info = self.NetworkPage.create_new_network()
		vlan_obj = basic_info.guest_network_info()
		security = vlan_obj.click_on_next()
		security.set_splash_page_type_value(conf.Splash_page_Acknowledged)
		self.browser.assert_element(security.no_logo_image,'No_logo_image is not found.')
		self.browser.assert_element(security.logo_upload,'Enabled Upload button not found.')
		self.browser.assert_element(security.logo_disabled_delete_button,'Disabled Delete button not found.')
		logger.debug('SecurityPage : Clicking on upload button')
		fu = self.get_file_uploader(conf.logo1)
		fu.start()
		security.logo_upload.click()
		fu.join()
		time.sleep(5)
		self.browser.assert_element(security.logo_preview,'Preview logo_image is not found.')
		self.browser.assert_element(security.logo_preview,'logo_image_preview is not found.')
		self.browser.assert_element(security.change_logo,'Enabled Change button not found.')
		self.browser.assert_element(security.delete_logo,'Enabled Delete button not found.')
		access = security.click_on_next()
		access.finish_network_setup()
		self.take_s2_snapshot()
		self.NetworkPage.delete_network_if_present()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()