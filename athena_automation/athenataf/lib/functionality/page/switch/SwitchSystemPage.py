from athenataf.lib.util.WebPage import WebPage
import traceback
import logging
logger = logging.getLogger('athenataf')

class SwitchSystemPage(WebPage):
	def __init__(self, test, browser, config):
		WebPage.__init__(self, "SwitchConfigurationSystem", test, browser, config)
		self.test.assertPageLoaded(self)

	def isPageLoaded(self):
		if self.name_server:
			return True    
		else:
			return False

	def set_name_server(self, value=None):
		logger.debug("SystemPage: Setting the server name")
		if value:
			self.name_server.set(value)
		else:
			self.name_server.set(self.config.config_vars.name_server_default)

	def save_setting(self):
		logger.debug("SystemPage: Click save setting button")
		import time
		time.sleep(5)
		self.save_settings.click()
	
	def set_admin_password(self,value):
		'''
		sets the admin password to the given value
		'''
		logger.debug("SystemPage: Writing admin password")
		self.admin_pass.set(value)

	def set_admin_confirm_password(self,value):
		'''
		sets the admin confirm password to the given value
		'''
		logger.debug("SystemPage: Writing admin confirm password")
		self.admin_confirm_pass.set(value)

	def set_enable_password(self,value):
		'''
		sets the enable password to the given value
		'''
		logger.debug("SystemPage: Writing enable password")
		self.enable_pass.set(value)

	def set_enable_confirm_password(self,value):
		'''
		sets the enable confirm password to the given value
		'''
		logger.debug("SystemPage: Writing enable confirm password")
		self.enable_confirm_pass.set(value)
	
	def cancel_settings(self):
		'''
			clicks on cancel button
		'''
		logger.debug("SystemPage: Clicking on cancel button")
		self.cancel.click()
	
	def assert_admin_password(self, error_msg):
		'''
		asserts admin password error message
		'''
		if error_msg == 'Required field':
			if not self.admin_pass_required_field :
				raise AssertionError("SystemPage: Required field error message is not displayed")
		if error_msg == 'Mismatch':
			if not self.admin_pass_mismatch :
				raise AssertionError("SystemPage: Fields do not match error message is not displayed")
		if error_msg == 'Length error':
			if not self.admin_pass_lengtherror :
				raise AssertionError("SystemPage: Fields do not match error message is not displayed")
		if error_msg == 'pattern mismatch':
			if not self.admin_pass_pattern_mismatch :
				raise AssertionError("SystemPage: Fields do not match error message is not displayed")
				

	def assert_admin_confirm_password(self, error_msg):
		'''
		asserts admin  confirm password error message
		'''
		if error_msg == 'Required field':
			if not self.admin_confirm_required_field :
				raise AssertionError("SystemPage: Required field error message is not displayed")
		if error_msg == 'Mismatch':
			if not self.admin_confirm_mismatch :
				raise AssertionError("SystemPage: Fields do not match error message is not displayed")
		if error_msg == 'Length error':
			if not self.admin_confirm_lengtherror :
				raise AssertionError("SystemPage: Fields do not match error message is not displayed")
		if error_msg == 'pattern mismatch':
			if not self.admin_confirm_pattern_mismatch :
				raise AssertionError("SystemPage: Fields do not match error message is not displayed")

	def assert_enable_password(self, error_msg):
		'''
		asserts enable password error message
		'''
		if error_msg == 'Required field':
			if not self.enable_pass_required_field :
				raise AssertionError("SystemPage: Required field error message is not displayed")
		if error_msg == 'Mismatch':
			if not self.enable_pass_mismatch :
				raise AssertionError("SystemPage: Fields do not match error message is not displayed")
		if error_msg == 'Length error':
			if not self.enable_pass_lengtherror :
				raise AssertionError("SystemPage: Fields do not match error message is not displayed")
		if error_msg == 'pattern mismatch':
			if not self.enable_pass_pattern_mismatch :
				raise AssertionError("SystemPage: Fields do not match error message is not displayed")

	def assert_enable_confirm_password(self, error_msg):
		'''
		asserts enable confirm password error message
		'''
		if error_msg == 'Required field':
			if not self.enable_confirm_required_field :
				raise AssertionError("SystemPage: Required field error message is not displayed")
		if error_msg == 'Mismatch':
			if not self.enable_confirm_mismatch :
				raise AssertionError("SystemPage: Fields do not match error message is not displayed")
		if error_msg == 'Length error':
			if not self.enable_confirm_lengtherror :
				raise AssertionError("SystemPage: Fields do not match error message is not displayed")
		if error_msg == 'pattern mismatch':
			if not self.enable_confirm_pattern_mismatch :
				raise AssertionError("SystemPage: Fields do not match error message is not displayed")				