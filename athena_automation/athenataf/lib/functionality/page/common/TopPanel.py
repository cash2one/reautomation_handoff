from athenataf.lib.util.WebPage import WebPage
from athenataf.lib.functionality.page.group.InnerLeftPanel import InnerLeftPanel
import logging
logger = logging.getLogger('athenataf')
import time
import traceback

class TopPanel(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "DashboardTopPanel", test, browser, config)
        self.test.assertPageLoaded(self)

    def isPageLoaded(self):
        if self.slider_icon:
            return True    
        else:
            return False 
            
    def go_to_allgroups(self):
        self.all_groups.click()
        # self.all_groups.click()
        # self.all_groups.click()
        try:
            self.default_group
        except:
            self.all_groups.click()
            
    def click_slider_icon(self):
        time.sleep(5)
        self.innerleft_panel_icon.click()
        return InnerLeftPanel(self.test, self.browser, self.config)


    def get_inner_left_panel(self):
        time.sleep(5)
        return InnerLeftPanel(self.test, self.browser, self.config)

    def validate_user_interface(self):
        '''
            Validate User Interface
        '''
        logger.debug("Clicking on user icon")
        self.user_setting.click()
        logger.debug("Checking the user name")
        if not self.user_name:
            raise AssertionError("Display user name is not correct Traceback: %s " %traceback.format_exc())
        logger.debug("Checking the account setting option")
        if not self.account_settings:
            raise AssertionError("Account setting option is not present Traceback: %s " %traceback.format_exc())
        logger.debug("Checking the change password option")
        if not self.change_password:
            raise AssertionError("Change password option is not present Traceback: %s " %traceback.format_exc())
        logger.debug("checking the logout option")
        if not self.logout:
            raise AssertionError("Logout option is not present Traceback: %s " %traceback.format_exc())
        logger.debug("Clicking on the account setting button")
        self.account_settings.click()
        logger.debug("Checking the default group field")
        if not self.user_setting_group:
            raise AssertionError("Default group option is not present Traceback: %s " %traceback.format_exc())
        logger.debug("Checking the Time zone field")
        if not self.user_setting_timeZone:
            raise AssertionError("Time zone option is not present Traceback: %s " %traceback.format_exc())
        logger.debug("Checking the idle time out field")
        if not self.user_setting_idel_time:
            raise AssertionError("Idle timeout option is not present Traceback: %s " %traceback.format_exc())
        logger.debug("Ckeckinh the default idle time out value")
        if not self.user_setting_idel_time.get() == self.config.config_vars.user_idel_time_default:
            raise AssertionError("Default value of idle timeout is not set to default Traceback: %s " %traceback.format_exc())
        logger.debug("Setting the incorrect value in idle time out")
        self.set_idel_time_value(self.config.config_vars.user_idel_time_error)
        time.sleep(3)
#         self.user_setting_idel_time.set(self.config.config_vars.user_idel_time_error)
        
        if not self.idel_timeout_error:
            raise AssertionError("Must be number in range 5-10080 Traceback: %s " %traceback.format_exc())
        
        self.set_idel_time_value()
        if not self.idle_timeout_error_2:
            raise AssertionError("Error while taking valid value because valid range is 5-10080 Traceback: %s " %traceback.format_exc())        
        
        logger.debug("Clicking on save button")
        self.save_button.click()
    
    
    def validate_time_zone(self):
        '''
            Validating the time zone field
        '''
        time.sleep(4)
        logger.debug("Clicking on user icon")
        self.user_setting.click()
        time.sleep(4)
        logger.debug("Clicking on the account setting button")
        self.account_settings.click()
        logger.debug("Checking the time zone field")
        if not self.user_setting_timeZone:
            raise AssertionError("Time zone option is not present Traceback: %s " %traceback.format_exc())
        logger.debug("Clicking on cancel button")
        self.cancel_button.click()
        
    
    def validate_idle_timeout(self):
        '''
            Validating the idle time out field
        '''
        logger.debug("Clicking on user icon")
        self.user_setting.click()
        logger.debug("Clicking on the account setting button")
        self.account_settings.click()
        logger.debug("Empty the idle time out field")
        self.user_setting_idel_time.set("")
        logger.debug("Setting value to the idle time out field")
        self.set_idel_time_value(self.config.config_vars.user_idel_time_value)
#         self.user_setting_idel_time.set(self.config.config_vars.user_idel_time_value)
        logger.debug("Clicking on save button")
        self.save_button.click()
        time.sleep(260)
        
        logger.debug("Clicking the session time out cancel button")
        self.cancel_session_timeout.click()
        
    
    def setting_default_value(self):
        '''
            Setting the default value to the idle time out field
        '''
        if self.close_user_setting_pop_up:
            self.close_user_setting_pop_up.click()
            import time
            time.sleep(5)
        logger.debug("Clicking on user icon")
        self.user_setting.click()
        logger.debug("Clicking on the account setting button")
        self.account_settings.click()
        logger.debug("Empty the idle time out field")
        self.user_setting_idel_time.set("")
        logger.debug("Setting default value to the idle time out field")
        self.set_idel_time_value(self.config.config_vars.user_idel_time_default)
        #         self.user_setting_idel_time.set(self.config.config_vars.user_idel_time_default)
        logger.debug("Clicking on save button")
        self.save_button.click()
    
    
    
    def set_idel_time_value(self,value=None):
        logger.debug("Setting value to the idle timeout field")
        if value:
            self.user_setting_idel_time.set(value)
        else:
            self.user_setting_idel_time.set(self.config.config_vars.user_idel_time_default)
            
    def assert_user_profile_name(self,name):
        '''
        asserts profile name with the param name
        '''
        logger.debug("Clicking on user icon")
        self.user_setting.click()
        logger.debug("Asserting profile name")
        if not self.user_profile_name.get_attribute_value('text') == name:
            raise AssertionError("User name is not set to given name %s",name)        
        