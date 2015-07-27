import logging
logger = logging.getLogger('athenataf')
import time

from athenataf.lib.functionality.test.MaintenanceTest import MaintenanceTest

class UserManagement(MaintenanceTest):
    '''
    Test class for UserManagement.
    '''

    def _view_monitoring_pages(self):
        self.LeftPanel.go_to_monitoring_page()
        self.LeftPanel.go_to_monitoring_access_points()
        self.LeftPanel.go_to_monitoring_clients()
        self.LeftPanel.go_to_monitoring_wids()
        self.LeftPanel.go_to_monitoring_event_log()
        self.LeftPanel. go_to_monitoring_notifications()

    def test_ath_23566_assert_customer(self):
        self._view_monitoring_pages()
        user_management = self.LeftPanel.go_to_user_management()
        user_management.assert_user_present()
        user_management.open_new_tab()            
        self._view_monitoring_pages()
        user_management = self.LeftPanel.go_to_user_management()
        user_management.assert_user_present()
        self._logoutSso()
        self._loginSso()
        user_management = self.LeftPanel.go_to_user_management()
        user_management.assert_user_present()

    def test_ath_8208_check_user_management_page(self):
        user_management_page=self.LeftPanel.go_to_user_management()
        user_management_page.assert_user_management_page()


    def test_ath_1928_delete_existing_user(self):
        conf = self.config.config_vars
        user_management_page=self.LeftPanel.go_to_user_management()
        user_management_page.delete_current_adminstrator_user()
        
        # if user_management_page.assert_new_administrator_user():
            # user_management_page.delete_if_any_user_present()

        user_management_page.create_new_user(conf.administrator_user,conf.user_setting_group_value,conf.administrator_access_level)
        if not user_management_page.assert_new_administrator_user():
            raise AssertionError('Newly created user is not displayed in the list')
            
        if user_management_page.assert_new_administrator_user():
            user_management_page.delete_if_any_user_present()
            
    def test_ath_8207_edit_existing_user(self):
        conf = self.config.config_vars
        user_management_page=self.LeftPanel.go_to_user_management()
        if user_management_page.assert_new_administrator_user():
            user_management_page.delete_if_any_user_present()
        user_management_page.create_new_user(conf.administrator_user,conf.user_setting_group_value,conf.administrator_access_level)
        if not user_management_page.assert_new_administrator_user():
            raise AssertionError('Newly created user is not displayed in the list')

        user_management_page.change_access_level_read_write()
        if user_management_page.user_create_success_ok_button:
            user_management_page.user_create_success_ok_button.click()
        user_management_page.change_access_level_read_only()
        if user_management_page.user_create_success_ok_button:
            user_management_page.user_create_success_ok_button.click()
        if user_management_page.assert_new_administrator_user():
            user_management_page.delete_if_any_user_present()

    def test_ath_8211_edit_a_read_only_user(self):
        conf = self.config.config_vars
        user_mgmt = self.LeftPanel.go_to_user_management()

        if not user_mgmt.assert_read_only_user() :
            user_mgmt.create_new_user(conf.email_read_only, conf.user_setting_group_value, conf.access_level_read_only)
        user_mgmt.edit_read_only_user()
        user_mgmt.edit_user_settings(user_scope = True,scope = conf.group_one, access_level = False, access = None)
        self.logout()
        self.login(access_level = 'default')
        user_mgmt = self.LeftPanel.go_to_user_management()
        logger.debug('UserManagement: asserting user scope')
        if not user_mgmt.default_group1:
            raise AssertionError('user scope is not set to default and group1')
        user_mgmt.edit_read_only_user()
        user_mgmt.edit_user_settings(user_scope = False,scope = None, access_level = True, access = conf.access_level_read_write)
        if not user_mgmt.read_write_user2:
            raise AssertionError('Access level is not set to default and group1')
        user_mgmt.edit_read_only_user()
        user_mgmt.edit_user_settings(user_scope = False,scope = None, access_level = True, access = conf.access_level_adminstrator)
        if not user_mgmt.read_only_admistrator:
            raise AssertionError('Access level is not set to administrator')    
        user_mgmt.delete_if_any_user_present()  

    def test_ath_8210_edit_a_read_write_user(self):
        conf = self.config.config_vars
        user_mgmt = self.LeftPanel.go_to_user_management()
        user_mgmt.delete_any_user()

        if not user_mgmt.assert_read_write_user() :
            user_mgmt.create_new_user(conf.email_read_write, conf.user_setting_group_value, conf.user_access_level_read_write)
        user_mgmt.edit_read_write_user()
        user_mgmt.edit_user_settings(user_scope = True,scope = conf.group_one, access_level = False, access = None)
        self.logout()
        self.login(access_level = 'default')
        user_mgmt = self.LeftPanel.go_to_user_management()
        logger.debug('UserManagement: asserting user scope')
        if not user_mgmt.default_group1:
            raise AssertionError('user scope is not set to default and group1')
        user_mgmt.edit_read_write_user()
        user_mgmt.edit_user_settings(user_scope = False,scope = None, access_level = True, access = conf.access_level_read_only)
        if not user_mgmt.read_only_user1:
            raise AssertionError('Access level is not set to default and group1')       
        user_mgmt.edit_read_write_user()
        user_mgmt.edit_user_settings(user_scope = False,scope = None, access_level = True, access = conf.access_level_adminstrator)
        if not user_mgmt.read_write_admistrator:
            raise AssertionError('Access level is not set to administrator')    
        user_mgmt.delete_if_any_user_present()  
        
    def test_ath_8212_turn_on_support_access(self):
        conf = self.config.config_vars
        user_mgmt = self.LeftPanel.go_to_user_management()
        user_mgmt.click_support_access_on()
        self.logout()
        time.sleep(240)
        self.login(access_level = 'default')
        user_mgmt = self.LeftPanel.go_to_user_management()
        user_mgmt.assert_support_access_button()
        
    def test_ath_8213_turn_off_support_access(self):
        self.only_close_browser = True
        conf = self.config.config_vars
        user_mgmt = self.LeftPanel.go_to_user_management();
        user_mgmt.set_support_access_on(False)
        self.logout()
        if self.login(login_form_submit = True):
            pass
        else:
            # fail
            raise AssertionError('User is logged in..')

            
    def test_ath_8830_add_deleted_user(self):
        conf = self.config.config_vars
        user_management_page = self.LeftPanel.go_to_user_management()
        user_management_page.delete_if_any_user_present()
        user_management_page.create_new_user(conf.email_read_write, conf.user_setting_group_value, conf.user_access_level_read_write)
        user_management_page.delete_if_any_user_present()
        user_management_page.create_new_user(conf.email_read_write, conf.user_setting_group_value, conf.user_access_level_read_write)
        user_management_page.delete_if_any_user_present()

    def test_ath_7992_create_an_administrator_user(self):
        conf = self.config.config_vars
        user_mgmt = self.LeftPanel.go_to_user_management()
        if user_mgmt.assert_new_administrator_user():
            user_mgmt.delete_if_any_user_present()
        user_mgmt.create_new_user(conf.administrator_user,conf.user_setting_group_value,conf.administrator_access_level)
        if not user_mgmt.assert_new_administrator_user():
            raise AssertionError('Newly created user is not displayed in the list')
        self.logout()
        self.login(access_level = 'admin')
        self.TopPanel.assert_user_profile_name(conf.administrator_user)
        self.logout()
        self.login(access_level = None)

    def test_ath_1893_create_a_read_and_write_user(self):
        conf = self.config.config_vars
        user_mgmt = self.LeftPanel.go_to_user_management()
        if user_mgmt.assert_read_write_user():
            user_mgmt.delete_if_any_user_present()
        user_mgmt.create_new_user(conf.email_read_write,conf.user_setting_group_value,conf.user_access_level_read_write)
        if not user_mgmt.assert_read_write_user():
            raise AssertionError('Newly created user is not displayed in the list')
        self.logout()
        self.login(access_level = 'read_write')
        self.TopPanel.assert_user_profile_name(conf.email_read_write)
        user_mgmt = self.LeftPanel.go_to_user_management()
        logger.debug('Asserting group name')
        logger.debug('Asserting access level')
        if not user_mgmt.read_write_user1:
            raise AssertionError('For newly created user access level is not set to read/write ')
        self.logout()
        self.login(access_level = None)

    def test_ath_1892_create_a_read_only_user(self):
        conf = self.config.config_vars
        user_mgmt = self.LeftPanel.go_to_user_management()
        if user_mgmt.assert_read_only_user():
            user_mgmt.delete_if_any_user_present()
        user_mgmt.create_new_user(conf.email_read_only,conf.user_setting_group_value,conf.user_access_level_read_only)
        if not user_mgmt.only_read:
            raise AssertionError('Newly created user is not displayed in the list')
        self.logout()
        self.login(access_level = 'read_only')
        self.TopPanel.assert_user_profile_name(conf.email_read_only)
        user_mgmt = self.LeftPanel.go_to_user_management()
        logger.debug('Asserting group name')
        logger.debug('Asserting access level')
        if not user_mgmt.only_read:
            raise AssertionError('For newly created user access level is not set to readonly ')
        self.logout()
        self.login(access_level = None)     