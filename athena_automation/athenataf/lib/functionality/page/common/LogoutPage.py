from athenataf.lib.util.WebPage import WebPage  
import logging
logger = logging.getLogger('athenataf')

class LogoutPage(WebPage):
    def __init__(self, test, browser, config, IAP=False):
        WebPage.__init__(self, "Logout", test, browser, config)
        self.test.assertPageLoaded(self)
        
    def logout(self):
        self.browser.refresh()
        try:
            if self.manage_license:
                self.manage_license.click()

        except:
            pass
        import time
        time.sleep(5)
        self.browser.key_press(u'\ue00e')
        if self.logout_user_link:
            self.logout_user_link.click()
            time.sleep(5)
            if self.account_settings_hidden:
                self.logout_user_link.click()
                time.sleep(5)
        else:
            self.user.click()
            time.sleep(5)
        self.logout_button.click()
        if self.browser._browser.find_element_by_id("username"):
            self.browser.go_to(self.config.global_vars.url)
			
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