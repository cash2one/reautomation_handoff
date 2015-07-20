import time 

from athenataf.lib.util.WebPage import WebPage	
from athenataf.lib.functionality.page.common.Dashboard import Dashboard
from athenataf.lib.functionality.page.common.LeftPanel import LeftPanel
from athenataf.lib.functionality.page.common.TopPanel import TopPanel

class LoginPage(WebPage):
    def __init__(self, test, browser, config, IAP=False):
        WebPage.__init__(self, "Login", test, browser, config)
        self.test.assertPageLoaded(self)
        
    def isPageLoaded(self):
        if self.username:
            return True
        else:
            return False
            
    def _handle_manage_license(self):
        '''
        Click on manage license
        '''
        try:
            if self.manage_license:
                self.manage_license.click()
                import time
                time.sleep(10)
                self.monitoring.click()
        except:
            pass
        
    def login(self):
        self.username.set(self.config.global_vars.email)
        self.password.set(self.config.global_vars.password)
        self.submit.click()
        self._handle_manage_license()
        return Dashboard(self.test, self.browser, self.config)
        
    def login_sso(self):    
        self.username.set(self.config.global_vars.email)
        self.password.set(self.config.global_vars.password)
        self.submit.click()
        self._handle_manage_license()       
        
    def login_read_write(self, access_level):
        if access_level == 'read_only':
            self.username.set(self.config.global_vars.email_read_only)
        elif access_level == 'read_write':
            self.username.set(self.config.global_vars.email_read_write)
        elif access_level == 'default':
            self.username.set(self.config.global_vars.email)
        else :
            self.username.set(self.config.global_vars.email_administrator)
        self.password.set(self.config.global_vars.password)
        self.submit.click()
        self._handle_manage_license()
        return Dashboard(self.test, self.browser, self.config)
        
    def login_dynamic(self,email=None,passwd=None):
        '''
        Login using user name and password 
        '''
        self.username.set(email)
        self.password.set(passwd)
        self.submit.click()
        self._handle_manage_license()
        return Dashboard(self.test, self.browser, self.config)

    def login_ui(self):
        self.username.set(self.config.global_vars.email)
        self.password.set(self.config.global_vars.password)
        self.submit.click()
        self._handle_manage_license()
        return self.isPageLoaded()
        
class LoginIAP(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "Login", test, browser, config)
        self.test.assertPageLoaded(self)
    
    def isPageLoaded(self):
        if self.iap_username:
            return True
        else:
            return False 
    
    def login_IAP(self):
        '''
        Login to IAP using ip address and credentials
        '''
        self.iap_username.set(self.config.global_vars.iap_username)
        self.iap_password.set(self.config.global_vars.iap_password)
        self.iap_submit.click()
        time.sleep(2)