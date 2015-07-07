from athenataf.lib.util.WebPage import WebPage
import traceback
import logging
logger = logging.getLogger('athenataf')

class SubscriptionKeysPage(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "SubscrptionKeys", test, browser, config)
        self.test.assertPageLoaded(self)
        
        
    def isPageLoaded(self):
        if self.subscription_keys_label:
            return True    
        else:
            return False
			
	def asserting_subscription_key_field(self):
		logger.debug("DeviceManagementPage: Asserting Name label")
		self.browser.assert_element(self.name_label,' Name is not displayed')
		logger.debug("DeviceManagementPage: Asserting Type label")
		self.browser.assert_element(self.type_label,' Type is not displayed')		
		logger.debug("DeviceManagementPage: Asserting Start Date label")
		self.browser.assert_element(self.start_date_label,' Start Date is not displayed')
		logger.debug("DeviceManagementPage: Asserting End Date label")
		self.browser.assert_element(self.end_date_label,' End Date is not displayed')
		logger.debug("DeviceManagementPage: Asserting Capacity label")
		self.browser.assert_element(self.capacity_label,' Capacity is not displayed')		
		logger.debug("DeviceManagementPage: Asserting Used label")
		self.browser.assert_element(self.used_label,' Used is not displayed')