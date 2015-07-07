import os
from athenataf.lib.util.webdrivertest import WebDriverTestCase
from athenataf.lib.functionality.page.common.LoginPage import LoginPage
from athenataf.lib.functionality.page.common.LoginPage import LoginIAP
from athenataf.lib.functionality.page.common.LogoutPage import LogoutIAP
from athenataf.lib.functionality.page.common.LogoutPage import LogoutPage
from athenataf.lib.functionality.page.common.TopPanel import TopPanel
from athenataf.lib.functionality.page.common.LeftPanel import LeftPanel
from athenataf.lib.functionality.common.deviceverifier import DeviceVerifier
from athenataf.lib.util.nativewindows import WinFileUploader


import logging
logger = logging.getLogger('athenataf')    

class AthenaGUITestCase(WebDriverTestCase):

    def __init__(self, config):
        logger.debug("Initializing Test Case:: %s" % self.__class__.__name__)
        super(AthenaGUITestCase, self).__init__(config)
        self.TopPanel = None
        self.LeftPanel = None
        self.Dashboard = None
        self.device_verifier = DeviceVerifier(self.config, self)
        self.all_config_vars = {}
        self.loginPageObj = None
        self.only_close_browser = None
        
    def get_all_config_dict(self):
        import copy
        return_dict = copy.deepcopy(self.all_config_vars)
        for k,v in self.record.items():
            return_dict[k] = v
        return return_dict
    
    def get_file_uploader(self, file_path):
        in_file_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..","..","..")),"test_data","in_data")
        path = os.path.join(in_file_path,file_path)
        return WinFileUploader(path)
    
    def setUpTestClass(self, IAP=False):
        logger.debug("Setting up the current test for Global config vars object")
        self.config.global_vars.set_current_test(self)
        logger.debug("Setting up the current test for config vars object")
        self.config.config_vars.set_current_test(self)
        self.all_config_vars = self.config.global_vars._dict
        for k,v in self.config.config_vars._dict.items():
            self.all_config_vars[k] = v
        logger.debug("AthenaGUITestCase: setUpTestClass")       
        WebDriverTestCase.setUpTestClass(self)
        logger.debug("AthenaGUITestCase: Start Browser")                
        self.start_browser()
        logger.debug("AthenaGUITestCase: Open URL as per Global config.")                       
        if not IAP:
            self.browser.go_to(self.config.global_vars.url)
            logger.debug("AthenaGUITestCase: Login SSO")
            self.login()
    def tearDownTestClass(self):
        try:
            if not self.only_close_browser:
                logoutScreen = LogoutPage(self, self.browser, self.config)
                logoutScreen.logout()
            WebDriverTestCase.tearDownTestClass(self)
            self.stop_browser()
        except:
            self.stop_browser()
            raise

    def assert_s1_s2_diff(self, num_of_context_lines):
        if not self.device_verifier.check_s1_s2_diff(0):
            raise AssertionError("The actual and expected running config didn't match")
            
    def assert_s1_s3_diff(self):
        if not self.device_verifier.check_s1_s3_diff():
            raise AssertionError("Post clean-up the device did not return to original state.")          

    def take_s1_snapshot(self, extra_command=None):
        self.device_verifier.take_s1_snapshot(extra_command)

    def take_s2_snapshot(self, extra_command=None):
        self.device_verifier.take_s2_snapshot(extra_command)
        
    def take_s3_snapshot(self, extra_command=None):
        self.device_verifier.take_s3_snapshot(extra_command)        

    def clear(self):
        self.device_verifier.clear()
        
    def connect_device(self):
        self.device_verifier.connect_device()
        
    def logout(self):
        logoutScreen = LogoutPage(self, self.browser, self.config)
        logoutScreen.logout()
        
    def login(self, access_level=None,email=None,password=None,login_form_submit=None):
        
        loginScreen = LoginPage(self, self.browser, self.config)
        print "I am in sso page"
        if access_level:
            self.Dashboard = loginScreen.login_read_write(access_level)
        elif email:
            self.Dashboard = loginScreen.login_dynamic(email,password)
        elif login_form_submit:
            return loginScreen.login_ui()
        else:
            self.Dashboard = loginScreen.login()
        # logger.debug("AthenaGUITestCase: Close Welcome message.")                                     
        # self.Dashboard.close_welcome_message()
        logger.debug("AthenaGUITestCase: Creating panels")                                              
        self.TopPanel = TopPanel(self, self.browser, self.config)
        self.LeftPanel = LeftPanel(self, self.browser, self.config)
        
    def logout_and_login_back(self):
        logoutScreen = LogoutPage(self, self.browser, self.config)
        logoutScreen.logout()
        logger.debug("AthenaGUITestCase: Login SSO")
        loginScreen = LoginPage(self, self.browser, self.config)    
        self.Dashboard = loginScreen.login()
        
    def login_to_athena_page(self):
        logger.debug("AthenaGUITestCase: Open URL as per Global config.")
        self.browser.go_to(self.config.global_vars.url)
        self.login()
        
    def login_to_athena_IAP(self):
        logger.debug("AthenaGUITestCase: Open IAP URL as per Global config.")
        self.browser.go_to(self.config.global_vars.url_iap)
        logger.debug("AthenaGUITestCase: Login to the Athena IAP")
        loginScreen = LoginIAP(self, self.browser, self.config)
        loginScreen.login_IAP()
    
    def logout_from_athena_IAP(self):
        logger.debug("AthenaGUITestCase: log out IAP ")
        logoutScreen = LogoutIAP(self, self.browser, self.config)
        logoutScreen.logout_IAP()
        
    def factory_reset(self):
        self.device_verifier.get_config.factory_reset()
        