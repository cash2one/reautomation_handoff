from athenataf.lib.util.WebPage import WebPage  
import traceback
import logging
logger = logging.getLogger('athenataf')


class CreateGroupPage(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "CreateGroup", test, browser, config)
        self.test.assertPageLoaded(self)
        
        
    def isPageLoaded(self):
        if self.create_new_group_label:
            return True 
        else:
            return False 
            
    def create_empty_group(self):
        '''
        creates empty group 
        '''
        logger.debug('Create Group : Writing group name')
        self.group_name.set(self.config.config_vars.group_name_string)
        self.group_name.set(self.config.config_vars.group_name_string)
        if self.select_all.is_selected():
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue00d')
        logger.debug('Create Group : Clickiing next button')
        self.next.click()
        self._set_group_default_device_password()
        if self.error_message:
            logger.debug('Create Group : Writing group name')
            self.group_name.set(self.config.config_vars.group_name_string)
            logger.debug('Create Group : Clickiing next button')
            self.next.click()
            self._set_group_default_device_password()
            if self.error_message:
                pass
        
    def create_group(self):
        '''
        creates group with vc
        '''
        logger.debug('Create Group : Writing group name')
        self.group_name.set(self.config.config_vars.group_name_string)
        self.group_name.set(self.config.config_vars.group_name_string)

        if self.select_all.is_selected():
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue00d')
            # self.browser.key_press(u'\ue00d')
        # else:
            # self.browser.key_press(u'\ue004')
            # self.browser.key_press(u'\ue004')
            # self.browser.key_press(u'\ue00d')
        logger.debug('Create Group : Clickiing select all checkbox')
        self.select_all.click()
        logger.debug('Create Group : Clickiing next button')
        self.next.click()
        self._set_group_default_device_password()
        if self.error_message:
            logger.debug('Create Group : Writing group name')
            self.group_name.set(self.config.config_vars.group_name_string)
            logger.debug('Create Group : Clickiing next button')
            self.next.click()
            self._set_group_default_device_password()
            if self.error_message:
                pass
        
    def create_multiple_groups(self):
        '''
        creates multiple groups
        '''
        logger.debug('Create Group : Writing group name')
        self.group_name.set(self.config.config_vars.new_group_name)
        self.group_name.set(self.config.config_vars.new_group_name)
        if self.select_all.is_selected():
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue00d')
            # self.browser.key_press(u'\ue00d')
        # else:
            # self.browser.key_press(u'\ue004')
            # self.browser.key_press(u'\ue004')
            # self.browser.key_press(u'\ue00d')
        import time
        time.sleep(8)
        logger.debug('Create Group : Clickiing select vc checkbox')
        self.select_vc.click()
        logger.debug('Create Group : Clickiing next button')
        self.next.click()
        self._set_group_default_device_password()
        if self.error_message:
            logger.debug('Create Group : Writing group name')
            self.group_name.set(self.config.config_vars.new_group_name)
            logger.debug('Create Group : Clickiing next button')
            self.next.click()
            self._set_group_default_device_password()
            if self.error_message:
                pass
        logger.debug('Create Group : Clicking on slider icon')
        self.logo.click()
        
    def assert_duplicate_group_warning(self):
        if self.warning_box:
            logger.debug('Create Group : Clicking ok button')
            self.OK.click()
            logger.debug('Create Group : Clicking cancel button')
            self.cancel.click()
            if self.error_message:
                pass
        else:
            raise AssertionError("Duplicate Group Warning Not Found i.e. Traceback: %s" %traceback.format_exc())
    
    def create_group1(self):
        '''
            Creating new group(group1)
        '''
        logger.debug('Create Group : Writing group name')
        self.group_name.set(self.config.config_vars.group_1)
        self.group_name.set(self.config.config_vars.group_1)
        if self.select_all.is_selected():
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue00d')
        logger.debug('Create Group : Clickiing select all checkbox')
        self.select_all.click()
        # if not self.verify_switch:
            # raise AssertionError("switch not available .Traceback: %s " %(traceback.format_exc()))
        logger.debug('Create Group : Clickiing next button')
        self.next.click()
        self._set_group_default_device_password()
        if self.error_message:
            logger.debug('Create Group : Writing group name')
            self.group_name.set(self.config.config_vars.group_1)
            logger.debug('Create Group : Clickiing next button')
            self.next.click()
            self._set_group_default_device_password()
            if self.error_message:
                pass
    
    def assert_group1(self):
        if not self.group1_with_device:
            raise AssertionError("group1 has no switch attached .Traceback: %s " %(traceback.format_exc()))
        
    def expand_group1(self):
        '''
        clicks on group1 expand button
        '''
        logger.debug('Create Group : Clickiing on group1 + sign')
        self.grp1_plus_sign.click()
        
    def select_swicth(self):
        '''
        selects switch group
        '''
        logger.debug('Create Group : Selecting switch group')
        self.select_switch.click()
    
    def assert_switch_on_title_area(self):
        if not self.switch_at_title:
            raise AssertionError("switch is not display on title .Traceback: %s " %(traceback.format_exc()))
        
    def select_group1_at_title(self):
        '''
        selects group1
        '''
        logger.debug('Create Group : Selecting group1 ')
        self.switch_at_title.click()
        
    def assert_group1_with_switch_at_title(self):
        if not self.group1_with_switch_at_title:
            raise AssertionError("group1 has no switch attached at title .Traceback: %s " %(traceback.format_exc()))
    
    def refresh(self):
        logger.debug('refresh page')
        self.browser.refresh()
    
    def create_group2(self):
        '''
        creates group2
        '''
        logger.debug('Create Group : Writing group name')
        self.group_name.set(self.config.config_vars.group_2)
        self.group_name.set(self.config.config_vars.group_2)
        if self.select_all.is_selected():
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue00d')
        logger.debug('Create Group : Clicking select_all check box')
        self.select_all.click()
        # if not self.verify_switch:
            # raise AssertionError("switch not available .Traceback: %s " %(traceback.format_exc()))
        logger.debug('Create Group : Clickiing next button')
        self.next.click()
        self._set_group_default_device_password()
        if self.error_message:
            logger.debug('Create Group : Writing group name')
            self.group_name.set(self.config.config_vars.group_2)
            logger.debug('Create Group : Clickiing next button')
            self.next.click()
            self._set_group_default_device_password()
            if self.error_message:
                pass
    
    def assert_sample_group(self):
        if not self.samplegroup:
            import traceback
            raise AssertionError("samplegroup does not exist i.e. Traceback: %s" %traceback.format_exc())
    
    def create_multiple_empty_groups(self,name):
        '''
        creating group with specified name
        '''
        logger.debug('Create Group : Writing group name')
        self.group_name.set(name)
        logger.debug('Create Group : Clickiing next button')
        self.next.click()
        self._set_group_default_device_password()

    def assert_group_sorting(self):
        '''
        asserting whether the created groups are in alphabetical order or not
        '''
        self.buy_time()
        if not self.alpha_group_a:
            raise AssertionError("Created Groups are not in Alphabetical Order: %s " %traceback.format_exc())
        if not self.alpha_group_b:
            raise AssertionError("Created Groups are not in Alphabetical Order: %s " %traceback.format_exc())
        if not self.alpha_group_c:
            raise AssertionError("Created Groups are not in Alphabetical Order: %s " %traceback.format_exc())
        if not self.alpha_group_d:
            raise AssertionError("Created Groups are not in Alphabetical Order: %s " %traceback.format_exc())
        if not self.alpha_group_e:
            raise AssertionError("Created Groups are not in Alphabetical Order: %s " %traceback.format_exc())
        if not self.alpha_group_f:
            raise AssertionError("Created Groups are not in Alphabetical Order: %s " %traceback.format_exc())
        if not self.alpha_group_g:
            raise AssertionError("Created Groups are not in Alphabetical Order: %s " %traceback.format_exc())
        if not self.alpha_group_h:
            raise AssertionError("Created Groups are not in Alphabetical Order: %s " %traceback.format_exc())
        if not self.alpha_group_i:
            raise AssertionError("Created Groups are not in Alphabetical Order: %s " %traceback.format_exc())
        if not self.alpha_group_j:
            raise AssertionError("Created Groups are not in Alphabetical Order: %s " %traceback.format_exc())
    def buy_time(self):
        import time
        time.sleep(5)

    def _set_group_default_device_password(self):
        '''
        setting default device password for  group
        '''
        logger.debug("CreateGroupPage: writing password in Password textbox ")
        self.device_password.set(self.config.config_vars.device_password)
        logger.debug("CreateGroupPage: writing password to confirm password in ConfirmPassword textbox ")
        self.confirm_device_password.set(self.config.config_vars.device_password)
        logger.debug("CreateGroupPage: clicking on save button ")
        self.save.click()
        self.buy_time()
        
    def create_switch_group1(self):
        '''
            Creating new group(group1)
        '''
        logger.debug('Create Group : Writing group name')
        self.group_name.set(self.config.config_vars.group_1)
        self.group_name.set(self.config.config_vars.group_1)
        if self.select_all_switch.is_selected():
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue00d')
        logger.debug('Create Group : Clickiing select all checkbox')
        self.select_all_switch.click()
        if not self.verify_switch:
            raise AssertionError("switch not available .Traceback: %s " %(traceback.format_exc()))
        logger.debug('Create Group : Clickiing next button')
        self.next.click()
        self._set_group_default_device_password()
        if self.error_message:
            logger.debug('Create Group : Writing group name')
            self.group_name.set(self.config.config_vars.group_1)
            logger.debug('Create Group : Clickiing next button')
            self.next.click()
            self._set_group_default_device_password()
            if self.error_message:
                pass

    def create_empty_switch_group(self):
        logger.debug('Create Group : Writing group name')
        self.group_name.set(self.config.config_vars.group_name_string)
        self.group_name.set(self.config.config_vars.group_name_string)
        if self.select_all_switch.is_selected():
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue00d')
        logger.debug('Create Group : Clickiing next button')
        self.next.click()
        self._set_group_default_device_password()
        if self.error_message:
            logger.debug('Create Group : Writing group name')
            self.group_name.set(self.config.config_vars.group_name_string)
            logger.debug('Create Group : Clickiing next button')
            self.next.click()
            self._set_group_default_device_password()
            if self.error_message:
                pass

    def create_switch_group2(self):
        logger.debug('Create Group : Writing group name')
        self.group_name.set(self.config.config_vars.group_2)
        self.group_name.set(self.config.config_vars.group_2)
        if self.select_all_switch.is_selected():
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue00d')
        logger.debug('Create Group : Clickiing select all checkbox')
        self.select_all_switch.click()
        if not self.verify_switch:
            raise AssertionError("switch not available .Traceback: %s " %(traceback.format_exc()))
        logger.debug('Create Group : Clickiing next button')
        self.next.click()
        self._set_group_default_device_password()
        if self.error_message:
            logger.debug('Create Group : Writing group name')
            self.group_name.set(self.config.config_vars.group_2)
            logger.debug('Create Group : Clickiing next button')
            self.next.click()
            self._set_group_default_device_password()
            if self.error_message:
                pass

    def clicking_on_next_button(self):
        '''
        clicking on next button
        '''
        self.buy_time()
        logger.debug('Create Group : Clickiing next button')
        self.next.click()   
        self.buy_time()
    
    def assert_group_name_length_error(self):
        '''
        Asserting group name length error
        '''
        if not self.group_name_length_error:
            raise AssertionError("Group Name Accepting more than 32 characters: %s " %(traceback.format_exc()))
        
    def clicking_on_cancel_button(self):
        '''
        clicking on cancel button
        '''
        logger.debug('Create Group : Clickiing cancel button')
        self.cancel.click() 
        self.buy_time() 
        
    def Assert_valid_group_name(self):
        '''
        asserting valid group name
        '''
        if not self.device_password:
            raise AssertionError("Invalid group name %s " %(traceback.format_exc()))
            
    def create_group_for_assertion(self,name):
        '''
        creates group
        '''
        logger.debug("CreateGroupPage: writing groupname in Group name textbox ")
        self.group_name.set(name)
        logger.debug('Create Group : Clickiing next button')
        self.next.click()
        
    def set_group_password(self,password):
        '''
        set password
        '''
        logger.debug("CreateGroupPage: writing password in Password textbox ")
        self.device_password.set(password)
        
    def click_cancel_group_button(self):
        '''
        clicks on cancel button
        '''
        logger.debug("CreateGroupPage: Clicking on cancel button ")
        self.cancel_group_button.click()
        # return InnerLeftPanel(self.test, self.browser, self.config)
        
    def set_group_confirm_password(self,password):
        '''
        writes confirm password
        '''
        logger.debug("CreateGroupPage: Re- enter confirm password")
        self.confirm_device_password.set(password)
        
    def assert_password_field(self,visible = False,invisible = False):
        if visible :
            if not self.cddc_password_length_error :
                raise AssertionError("Validation error saying valid range is 6-32 is not shown.Traceback: %s " %(traceback.format_exc()))
        if invisible :
            if self.cddc_password_length_error :
                raise AssertionError("Validation error saying valid range is 6-32 is shown.Traceback: %s " %(traceback.format_exc()))
                
    def assert_confirm_password_field(self,visible = False):
        if visible :
            if not self.cddc_password_mismatch_error :
                raise AssertionError("Validation error saying password do not match is not shown.Traceback: %s " %(traceback.format_exc()))
        

        
        
        
    def assert_default_create_groups_fields(self):
        '''
        Asserts Create groups default fields
        '''
        self.buy_time()
        if not self.group_name: 
            raise AssertionError(" Group name text box is not present i.e. Traceback: %s" %traceback.format_exc())  
        if not self.group_name.get() == '': 
            raise AssertionError(" Group name text box is not Empty i.e. Traceback: %s" %traceback.format_exc())        
        if not self.select_vc:  
            raise AssertionError(" VC is not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.cancel: 
            raise AssertionError(" Create group Cancel button is not Present i.e. Traceback: %s" %traceback.format_exc())   
        if not self.next:   
            raise AssertionError(" Create group Next>> button is not Present i.e. Traceback: %s" %traceback.format_exc())   
        if not self.create_page_textbox:    
            raise AssertionError(" Create group Page text box is not Present i.e. Traceback: %s" %traceback.format_exc())   
            
    def create_group_with_vc(self,group_name):
        '''
        creates group
        '''
        logger.debug('Create Group : Writing group name')
        self.group_name.set(group_name)
        self.group_name.set(group_name)

        if self.select_all.is_selected():
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue00d')
            # self.browser.key_press(u'\ue00d')
        # else:
            # self.browser.key_press(u'\ue004')
            # self.browser.key_press(u'\ue004')
            # self.browser.key_press(u'\ue00d')
        logger.debug('Create Group : Clickiing select all checkbox')
        self.select_all.click()
        logger.debug('Create Group : Clickiing next button')
        self.next.click()
        self._set_group_default_device_password()
        if self.error_message:
            logger.debug('Create Group : Writing group name')
            self.group_name.set(self.config.config_vars.group_name_string)
            logger.debug('Create Group : Clickiing next button')
            self.next.click()
            self._set_group_default_device_password()
            if self.error_message:
                pass
                
    def create_group_with_vc1(self,group_name):
        '''
        creates group
        '''
        logger.debug('Create Group : Writing group name')
        self.group_name.set(group_name)
        self.group_name.set(group_name)

        if self.select_all.is_selected():
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue00d')
            # self.browser.key_press(u'\ue00d')
        # else:
            # self.browser.key_press(u'\ue004')
            # self.browser.key_press(u'\ue004')
            # self.browser.key_press(u'\ue00d')
        logger.debug('Create Group : Clickiing select all checkbox')
        self.select_all.click()
        logger.debug('Create Group : Clickiing next button')
        self.next1.click()
        self._set_group_default_device_password1()
        if self.error_message:
            logger.debug('Create Group : Writing group name')
            self.group_name.set(group_name)
            logger.debug('Create Group : Clickiing next button')
            self.next1.click()
            self._set_group_default_device_password1()
            if self.error_message:
                pass

    def _set_group_default_device_password1(self):
        '''
        setting default device password for  group
        '''
        logger.debug("CreateGroupPage: writing password in Password textbox ")
        self.device_password.set(self.config.config_vars.device_password)
        logger.debug("CreateGroupPage: writing password to confirm password in ConfirmPassword textbox ")
        self.confirm_device_password.set(self.config.config_vars.device_password)
        logger.debug("CreateGroupPage: clicking on save button ")
        self.buy_time()
        self.save1.click()
        self.buy_time()
        
    def create_empty_group1(self,group_name1):
        '''
        creates empty group 
        '''
        logger.debug('Create Group : Writing group name')
        self.group_name.set(group_name1)
        self.group_name.set(group_name1)
        if self.select_all.is_selected():
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue004')
            self.browser.key_press(u'\ue00d')
        logger.debug('Create Group : Clickiing next button')
        self.next.click()
        self._set_group_default_device_password()
        if self.error_message:
            logger.debug('Create Group : Writing group name')
            self.group_name.set(group_name1)
            logger.debug('Create Group : Clickiing next button')
            self.next.click()
            self._set_group_default_device_password()
            if self.error_message:
                pass

    def set_group_name(self,name):
        '''
        writes group name
        '''
        logger.debug('Create Group : Writing group name')
        self.group_name.set(name)
        
    def move_next(self):
        '''
        Clicks on Next button
        '''
        logger.debug('Create Group : Clickiing next button')
        self.next.click()

    def select_virtual_controller(self,vc):
        '''
        selects vc
        '''
        logger.debug('Create Group : Clickiing select vc checkbox')
        vc.click()
    
    def toggle_switch(self):
        '''
        clicks on switch tab
        '''
        logger.debug('Create Group : Clickiing switch tab')
        if self.switch_toggle:
            self.switch_toggle.click()

    def create_switch_group_with_unprovision_switch(self,grp_name=None):
        '''
        Creating new group
        '''
        logger.debug("CreateGroup: Clicking on Switch Tab")
        if self.switch_toggle:
            self.switch_toggle.click()
        logger.debug('Create Group : Writing group name')
        self.group_name.set(grp_name)
        self.group_name.set(grp_name)
        logger.debug('Create Group : Clickiing select all checkbox')
        if not self.unprovision_switch_checkbox.is_selected():
            self.unprovision_switch_checkbox.click()
        if not self.verify_switch:
            raise AssertionError("switch not available .Traceback: %s " %(traceback.format_exc()))
        logger.debug('Create Group : Clicking next button')
        self.next.click()
        self._set_group_default_device_password()
        if self.error_message:
            logger.debug('Create Group : Writing group name')
            self.group_name.set(self.config.config_vars.group_1)
            logger.debug('Create Group : Clickiing next button')
            self.next.click()
            self._set_group_default_device_password()
            if self.error_message:
                pass
                
    def create_unprovision_switch_group1(self,grp_name=None):
        '''
            Creating new group
        '''
        logger.debug("CreateGroup: Clickiing on Switch Tab")
        if self.switch_toggle:
            self.switch_toggle.click()
        logger.debug('Create Group : Writing group name')
        self.group_name.set(grp_name)
        self.group_name.set(grp_name)
        logger.debug('Create Group : Clickiing select all checkbox')
        if not self.switch1.is_selected():
            self.switch1.click()
        if not self.verify_switch:
            raise AssertionError("switch not available .Traceback: %s " %(traceback.format_exc()))
        logger.debug('Create Group : Clickiing next button')
        self.next.click()
        self._set_group_default_device_password()
        if self.error_message:
            logger.debug('Create Group : Writing group name')
            self.group_name.set(self.config.config_vars.group_1)
            logger.debug('Create Group : Clickiing next button')
            self.next.click()
            self._set_group_default_device_password()
            if self.error_message:
                pass
    
    def toggle_vc(self):
        '''
        clicks on switch tab
        '''
        logger.debug('Create Group : Clickiing Vc tab')
        if self.vc_toggle:
            self.vc_toggle.click()          
        
    def create_group1_with_one_switch_and_iap(self):
        '''
        Creates group1 with one iap and one switch
        '''
        conf = self.config.config_vars
        self.toggle_switch()
        self.set_group_name(conf.group_1)
        self.selects_and_delects_iap_Switch(True,self.switch1)
        self.toggle_vc()
        logger.debug('Create Group : Clickiing select vc checkbox')
        self.selects_and_delects_iap_Switch(True,self.select_vc)
        self.create_group_for_assertion(conf.group_1)
        self._set_group_default_device_password1()
        
    def create_group2_with_3_switches_and_one_iap(self):
        '''
        Creates group2 with one iap and three switches
        '''
        conf = self.config.config_vars
        self.toggle_switch()
        self.set_group_name(conf.group_2)
        logger.debug('Create Group : selecting switch1 ')
        self.selects_and_delects_iap_Switch(False,self.switch1)
        self.selects_and_delects_iap_Switch(True,self.switch2)
        self.toggle_vc()
        logger.debug('Create Group : Clickiing select vc checkbox')
        self.selects_and_delects_iap_Switch(False,self.select_vc)
        self.selects_and_delects_iap_Switch(True,self.select_vc1)
        self.create_group_for_assertion(conf.group_2)
        self._set_group_default_device_password1()
        
    def selects_and_delects_iap_Switch(self, select, check):
        '''
        Selects iaps and switches
        '''
        if select:
            logger.debug('Create Group : selecting device ')
            if not check.is_selected():
                check.click()
        else:   
            logger.debug('Create Group : deselecting device ')
            if check.is_selected():
                check.click()
    
    def create_group_with_one_switch(self,group_name,):
        '''
        Creates group1 with one iap and one switch
        '''
        conf = self.config.config_vars
        self.toggle_switch()
        self.set_group_name(group_name)
        self.selects_and_delects_iap_Switch(True,self.switch1)
        self.toggle_vc()
        self.create_group_for_assertion(group_name)
        self._set_group_default_device_password1()
            
    def create_group_with_one_switch1(self,group_name,):
        '''
        Creates group1 with one iap and one switch
        '''
        conf = self.config.config_vars
        self.toggle_switch()
        self.set_group_name(group_name)
        self.selects_and_delects_iap_Switch(False,self.switch1)
        self.selects_and_delects_iap_Switch(True,self.switch2)
        self.toggle_vc()
        self.create_group_for_assertion(group_name)
        self._set_group_default_device_password1()
        
    def create_group_with_user_groupname_password(self,groupname='',password=''):
        '''
        creates empty group 
        '''
        logger.debug('Create Group : Writing group name')
        self.group_name.set(groupname)
        self.group_name.set(groupname)
        logger.debug('Create Group : Clickiing next button')
        self.next.click()
        self.buy_time()
        logger.debug("CreateGroupPage: writing password in Password textbox ")
        self.device_password.set(password)
        logger.debug("CreateGroupPage: writing password to confirm password in ConfirmPassword textbox ")
        self.confirm_device_password.set(password)
        logger.debug("CreateGroupPage: clicking on save button ")
        self.save.click()
        import time
        time.sleep(80)
        
    def move_unprovisional_device_to_new_group(self,group_name):
        '''
        Creates new group and moves selected unprovisional device to that group.
        '''
        self.set_group_name(group_name)
        logger.debug("CreateGroupPage: Saves new group name")
        self.save_unprovisional_device.click()
        logger.debug("CreateGroupPage: writing password in Password textbox ")
        self.device_password.set(self.config.config_vars.device_password)
        logger.debug("CreateGroupPage: writing password to confirm password in ConfirmPassword textbox ")
        self.confirm_device_password.set(self.config.config_vars.device_password)
        logger.debug("CreateGroupPage: clicking on save button ")
        self.buy_time()
        self.save.click()
        self.buy_time()