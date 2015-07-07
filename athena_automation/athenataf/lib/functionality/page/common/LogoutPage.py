from athenataf.lib.util.WebPage import WebPage	
import logging
logger = logging.getLogger('athenataf')

class LogoutPage(WebPage):
	def __init__(self, test, browser, config, IAP=False):
		WebPage.__init__(self, "Logout", test, browser, config)
		self.test.assertPageLoaded(self)
		
	def logout(self):
		import time
		time.sleep(5)
		self.browser.key_press(u'\ue00e')
		self.user.click()
		self.logout_button.click()
		if self.logged_out_sso:
			logger.debug("Logout page : Logged out ")
			import time
			time.sleep(10)
		elif self.logged_out_devel:
			logger.debug("Logout page : Logged out ")

	def isPageLoaded(self):
		if self.user:
			return True
		else:
			return False 


class LogoutIAP(WebPage):
	def __init__(self, test, browser, config):
		WebPage.__init__(self, "Logout", test, browser, config)
		self.test.assertPageLoaded(self)			
	
	def isPageLoaded(self):
		if self.iap_logout:
			return True
		else:
			return False 
	
	def logout_IAP(self):
		'''
		Logout from IAP Ui
		'''
		self.iap_logout.click()
		time.sleep(5)