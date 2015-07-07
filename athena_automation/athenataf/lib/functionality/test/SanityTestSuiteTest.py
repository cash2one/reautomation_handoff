from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase
from athenataf.lib.functionality.page.configuration.network.NetworkPage import NetworkPage
from athenataf.lib.functionality.page.common.LogoutPage import LogoutPage
from athenataf.lib.functionality.page.common.LoginPage import LoginPage
from athenataf.lib.functionality.page.common.LeftPanel import LeftPanel
from athenataf.lib.functionality.page.common.TopPanel import TopPanel
import logging
logger = logging.getLogger('athenataf')    

class SanityTestSuiteTest(AthenaGUITestCase):

    def __init__(self, config):
        super(SanityTestSuiteTest, self).__init__(config)
        self.NetworkPage = None
        self.config = config

    def setUpTestClass(self):
        logger.debug("ConfigurationTest: setUpTestClass")    
        AthenaGUITestCase.setUpTestClass(self)
        logger.debug("ConfigurationTest: Go To Configuration.")
        all_group_page = self.LeftPanel.go_to_configuration()
        logger.debug("ConfigurationTest: Go To Network.")
        self.NetworkPage = all_group_page.go_to_networks()

    def assertPageLoaded(self, page_name, msg=None):
        msg = msg or ""
        if page_name.isPageLoaded():
            logger.debug("Page Loaded Successfully")
        else:
            raise AssertionError("%s.\n%s Page does not get loaded" % (msg, page_name))

    def tearDown(self):
        if self.LeftPanel.save_pop_up:
            self.LeftPanel.save_pop_up.click()
            import time
            time.sleep(15)
        self.LeftPanel.configuration.click()
        logoutScreen = LogoutPage(self, self.browser, self.config)
        logoutScreen.logout()        
#         import time 
#         time.sleep(10)
#         self.stop_browser()
#         time.sleep(10)
#         self.start_browser()
#         logger.debug("AthenaGUITestCase: Open URL as per Global config.")                        
#         self.browser.go_to(self.config.global_vars.url)
        logger.debug("AthenaGUITestCase: Login")                                
        loginScreen = LoginPage(self, self.browser, self.config)    
        self.Dashboard = loginScreen.login_sso()
        #logger.debug("ConfigurationTest: Go To Configuration.")
        #self.LeftPanel.go_to_network_page()
#         logger.debug("ConfigurationTest: Go To Network.")
#         self.NetworkPage = all_group_page.go_to_networks()