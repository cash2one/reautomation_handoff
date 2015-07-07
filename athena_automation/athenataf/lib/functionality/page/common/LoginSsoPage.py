from athenataf.lib.util.WebPage import WebPage    
from athenataf.lib.functionality.page.common.Dashboard import Dashboard

class LoginSsoPage(WebPage):
    def __init__(self, test, browser, config, IAP=False):
        WebPage.__init__(self, "LoginSSO", test, browser, config)
        self.test.assertPageLoaded(self)
        
    def isPageLoaded(self):
        if self.username_sso:
            return True        
        else:
            return False 
    
    def login_sso(self): 
        if self.username_sso:   
            self.username_sso.set(self.config.global_vars.username_sso)
            self.password_sso.set(self.config.global_vars.password_sso)
            self.sign_in.click()
        else:
            pass
        return Dashboard(self.test, self.browser, self.config)

