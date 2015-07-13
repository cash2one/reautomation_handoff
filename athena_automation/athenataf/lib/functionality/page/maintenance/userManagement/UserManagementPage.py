import traceback
from athenataf.lib.util.WebPage import WebPage
import traceback
import logging
logger = logging.getLogger('athenataf')

class UserManagementPage(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "UserManagement", test, browser, config)
        self.test.assertPageLoaded(self)


    def isPageLoaded(self):
        if self.add_user:
            return True    
        else:
            return False
            
    def buy_time(self):
        import time
        time.sleep(8)

    def assert_user_present(self):
        import traceback
        if not self.customer_id:
            raise AssertionError("Admin user lot listed i.e. Traceback: %s" %traceback.format_exc())
        if not self.read_only_user:
            raise AssertionError("Read only user not listed i.e. Traceback: %s" %traceback.format_exc())
        if not self.read_write_user:
            raise AssertionError("Read write user not listed i.e. Traceback: %s" %traceback.format_exc())        

    def open_new_tab(self):
        action_chain = self.browser.get_action_chain()
        self.browser.open_new_tab()
        action_chain.key_down(u'\ue009').send_keys(u'\ue004').key_up(u'\ue009').perform()
        action_chain.key_down(u'\ue009').send_keys(u'\ue004').key_up(u'\ue009').perform()
        action_chain.key_down(u'\ue009').send_keys('w').key_up(u'\ue009').perform()
        self.browser.go_to(self.config.global_vars.url)
        import time
        time.sleep(10)
        if self.cancel:
            self.cancel.click()

    def assert_user_management_page(self):
        if not self.username:
            raise AssertionError("the page does not displaying USERNAME i.e. Traceback: %s" %traceback.format_exc())
        if not self.userscope:
            raise AssertionError("the page does not displaying USER_SCOPE i.e. Traceback: %s" %traceback.format_exc())
        if not self.accesslevel:
            raise AssertionError("the page does not displaying ACCESS LEVEL i.e. Traceback: %s" %traceback.format_exc())
        if not self.actions:
            raise AssertionError("the page does not displaying ACTIONS (EDIT / DELETE)i.e. Traceback: %s" %traceback.format_exc())
        if not self.add_user:
            raise AssertionError("the page does not displaying add_user button i.e. Traceback: %s" %traceback.format_exc())
        if not self.support_access:
            raise AssertionError("the page does not displaying SUPPORT ACCESS button i.e. Traceback: %s" %traceback.format_exc())

    def create_adminstrator_user(self):
        logger.debug("UserManagement: Clicking on 'Add User' Button ")
        self.add_user.click()
        logger.debug("UserManagement: Setting the user email ")
        self.user_email.set(self.config.config_vars.valid_user_email)
        logger.debug("UserManagement: Setting the access level ")
        self.access_level.set(self.config.config_vars.access_level_adminstrator)
        logger.debug("UserManagement: Clicking on 'Save' button")
        self.save_button.click()
        self.buy_time()

    def delete_current_adminstrator_user(self):
        if self.current_admin:
            if self.delete_user:
                raise AssertionError("the current administrator user can be deletable i.e. Traceback: %s" %traceback.format_exc())

    def delete_new_administrator_user_if_present(self): 
        if self.new_admin:  
            self.buy_time()
            logger.debug("UserManagement: Clicking on delete button")
            self.delete_new_user.click() 
            self.delete_alert.click()
            if self.close_delete_user_pop_up:
                self.close_delete_user_pop_up.click()
            import time
            time.sleep(5) 

    def change_access_level_read_write(self):
        if self.new_admin:
            self.buy_time()
            logger.debug("UserManagement: Clicking on created user")
            self.new_admin.click()
            logger.debug("UserManagement: Clicking on edit")
            self.edit_new_user.click()
            self.buy_time()
            logger.debug("UserManagement: Setting the access level ")
            self.access_level.set(self.config.config_vars.access_level_read_write)
            logger.debug("UserManagement: Clicking on 'Save' button")
            self.save_button.click()
            if self.user_scope_error:
                self.user_scope.set(self.config.config_vars.default_user_scope)
            logger.debug("UserManagement: Clicking on 'Save' button")
            self.save_button.click()

    def change_access_level_read_only(self):
        if self.new_admin:
            self.buy_time()
            logger.debug("UserManagement: Clicking on created user")
            self.new_admin.click()
            logger.debug("UserManagement: Clicking on edit")
            self.edit_new_user.click()
            logger.debug("UserManagement: Setting the access level ")
            self.access_level.set(self.config.config_vars.access_level_read_only)
            if self.user_scope_error:
                self.user_scope.set(self.config.config_vars.default_user_scope)
            logger.debug("UserManagement: Clicking on 'Save' button")
            self.save_button.click()

    def create_new_user(self,umail,uscope,access_level):
        '''
        Creates new user in UserManagement page.
        '''
        logger.debug("UserManagement: Clicking on 'Add User' Button ")
        self.add_user.click()
        logger.debug("UserManagement: Setting the user email ")
        self.user_email.set(umail)
        logger.debug("UserManagement: Setting the user scope ")
        self.browser.key_press(u'\ue004')
        self.user_scope_text_box.set(uscope)
        self.browser.key_press(u'\ue007')
        logger.debug("UserManagement: Setting the access level ")
        self.access_level.set(access_level)
        logger.debug("UserManagement: Clicking on 'Save' button")
        self.save_button.click()
        self.buy_time()

    def delete_if_any_user_present(self):
        '''
        Deletes Read Only User.
        '''
        logger.debug("UserManagement: Clicking on 'Read Only User' delete Button ")
        if self.delete_read_only_user:
            self.delete_read_only_user.click()
            self.confirm_save_button.click()
            self.buy_time()
        logger.debug("UserManagement: Clicking on 'Read Write User' delete Button ")
        if self.delete_read_write_user:
            self.delete_read_write_user.click()
            self.confirm_save_button.click()
            self.buy_time()
        logger.debug("UserManagement: Clicking on 'administrator' delete Button ")
        if self.delete_administrator:
            self.delete_administrator.click()
            self.confirm_save_button.click()
            self.buy_time()
            
    def assert_read_write_user(self):
        '''
        Delete Read Write User 
        '''
        if self.read_write_user1:
            return True
        else:
            return False
            
    def assert_read_only_user(self):
        '''
        Delete Read Write User 
        '''
        if self.read_only_user1_delete:
            return True
        else:
            return False
            
    def edit_read_only_user(self):      
        '''
        clicks on read only user edit button
        '''
        logger.debug('User Management : CLicking on read only user edit button')
        self.read_only_user_edit.click()
        
    def edit_user_scope(self,scope):
        '''
        sets group for user
        '''
        logger.debug('UserManagement :setting user scope')
        self.user_scope_second.set(scope)
        
    def save_user_configuration(self):
        '''
        clicks on save button 
        '''
        logger.debug('User Management : CLicking on save button')
        self.save_button.click()

    def edit_access_level(self,access):
            logger.debug("UserManagement: Setting the access level ")
            self.access_level.set(access)
        
    def edit_user_settings(self,user_scope = False,scope = None , access_level = False, access = None):
        '''
        edit user scope, access level 
        '''
        if user_scope :
            self.edit_user_scope(scope)
        if access_level:
            self.edit_access_level(access)
        self.save_user_configuration()

    def edit_read_write_user(self):     
        '''
        clicks on read write user edit button
        '''
        logger.debug('User Management : CLicking on read write user edit button')
        self.read_write_user_edit.click()
        
    def click_support_access_on(self):
        logger.debug("UserManagement: Clicking on 'Support Access'")
        if not self.support_access_on:
            self.support_access_on.click()
        
    def assert_support_access_button(self):
        logger.debug("UserManagement: Asserting 'Support Access' button")
        if not self.support_access_on:
            raise AssertionError("UserManagement : Support Access Button is not 'ON'")
            
    def set_support_access_on(self,flag=True):
        '''
        Setting 'Support Access' to 'ON' or 'OFF'
        '''
        if flag:
            if not self.support_access_on:
                logger.debug("UserManagement: Clicking on 'Support Access' to 'ON' ")
                self.support_access.click()
        else:
            if self.support_access_on:
                logger.debug("UserManagement: Clicking on 'Support Access' to 'OFF' ")
                self.support_access.click()

    def assert_new_administrator_user(self):
        '''
        Delete Read Write User 
        '''
        if self.administrator_user_created:
            return True
        else:
            return False
                