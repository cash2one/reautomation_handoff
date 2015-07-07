import os
from athenataf.lib.util.webdrivertest import WebDriverTestCase
from athenataf.lib.functionality.page.common.LoginSsoPage import LoginSsoPage
from athenataf.lib.functionality.page.common.LogoutPage import LogoutPage
from athenataf.lib.functionality.page.common.TopPanel import TopPanel
from athenataf.lib.functionality.page.common.LeftPanel import LeftPanel
from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase
from athenataf.lib.util.Browser import *

import logging
logger = logging.getLogger('athenataf')    

class MaintenanceTestSso(AthenaGUITestCase):
    
    def __init__(self, config):
        super(MaintenanceTest, self).__init__(config)

    def setUpTestClass(self):
        WebDriverTestCase.setUpTestClass(self)
        self.start_browser()
        self.browser.go_to(self.config.global_vars.url)
        loginScreen = LoginSsoPage(self, self.browser, self.config)    
        self.Dashboard = loginScreen.login_sso()
        self.Dashboard.close_welcome_message()
        self.TopPanel = TopPanel(self, self.browser, self.config)
        self.LeftPanel = LeftPanel(self, self.browser, self.config)
        
    def _loginSso(self):
        self.start_browser()
        self.browser.go_to(self.config.global_vars.url)
        loginScreen = LoginSsoPage(self, self.browser, self.config)    
        self.Dashboard = loginScreen.login_sso()
        self.Dashboard.close_welcome_message()
        self.TopPanel = TopPanel(self, self.browser, self.config)
        self.LeftPanel = LeftPanel(self, self.browser, self.config)
        
    def _logoutSso(self):
        logoutScreen = LogoutPage(self, self.browser, self.config)
        logoutScreen.logout()
        import time 
        time.sleep(10)
        self.stop_browser()        
        
    def assertPageLoaded(self, page_name, msg=None):
        msg = msg or ""
        if page_name.isPageLoaded():
            logger.debug("Page Loaded Successfully")
        else:
            raise AssertionError("%s.\n%s Page does not get loaded" % (msg, page_name))
        
    def tearDown(self):
        pass