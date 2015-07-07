from athenataf.lib.util.WebPage import WebPage
from athenataf.lib.functionality.page.group.CreateGroupPage import CreateGroupPage
import traceback
import time
import logging
logger = logging.getLogger('athenataf')
from Device_Module.ObjectModule import Device
class ManageGroupsPage(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "ManageGroup", test, browser, config)
        self.test.assertPageLoaded(self)
        
    def isPageLoaded(self):
        if self.manage_group_label:
            return True    
        else:
            return False


    def delete_group(self, group):
        logger.debug("ManageGroupPage: Clicking on 'Group %s' group " %group)
        self.browser._browser.find_element_by_xpath("//span[@data-ng-bind='grpObj.group.name' and text()='%s'" %group).click()
        self.delete_group.click()
        logger.debug("ManageGroupPage: Clicking on 'Close' icon ")
        self.close_icon.click()
        if not self.browser._browser.find_element_by_xpath("//span[@data-ng-bind='grpObj.group.name' and text()='%s'" %group):
            #self.logo.click()
            self.browser.refresh()

    def move_all_ap_to_group(self, group):
        logger.debug("ManageGroupPage: Clicking on 'All Group' group ")
        self.all_group.click()
        time.sleep(5)
        if not self.select_all.is_selected():
            self.select_all.click()
        logger.debug("ManageGroupPage: Clicking on 'Move' button ")
        self.move.click()
        self.buy_time()
        logger.debug("ManageGroupPage: Clicking on required 'group' ")
        group_obj = self.browser._browser.find_element_by_xpath("//span[contains(@id,'group_table_name') and contains(text(), '%s')]" %group)
        logger.info(group_obj)
        group_obj.click()
        logger.debug("ManageGroupPage: Clicking on 'Save' button ")
        self.save.click()
        if not self.virtual_controller:
            self.logo.click()
        time.sleep(6)
        self.all_groups_button.click()

    def move_vc_to_group(self, group, vc):
        myDevice = Device.getDeviceObject(vc)
        mac = myDevice.get("mac")
        vc_name = mac.split(":")
        vc_name = "instant-%s:%s:%s" %(vc_name[-3].upper(), vc_name[-2].upper(), vc_name[-1].upper())
        logger.debug("ManageGroupPage: Clicking on 'All Group' group ")
        self.all_group.click()
        time.sleep(5)
        if self.select_all.is_selected():
            self.select_all.click()
        logger.debug("ManageGroupPage: Clicking on vc checkbox ")
        vc_list = self.browser._browser.find_elements_by_xpath("//table[@id='manageGroupSwarms']//tr//*[contains(@id, 'manageVCListTable_name_display')]")
        for vc in vc_list:
            if vc.text == vc_name:
                #vc.click()
                index = vc_list.index(vc)
        sel_list = self.browser._browser.find_elements_by_xpath("//table[@id='manageGroupSwarms']//tr//*[contains(@id, 'manageVCListTable_row_selector')]//input")
        sel_list[index].click()
                #tr = vc.find_element_by_xpath("..")
                #tr.find_element_by_xpath("//td[contains(@id, 'manageVCListTable_row_selector')]//input").click()
        #table = self.browser._browser.find_element_by_xpath("//table[@id='manageGroupSwarms']")
        #for tr in table.find_elements_by_tag_name("tr"):
        #    if tr.find_element_by_xpath("//*[contains(@id, 'manageVCListTable_name_display')]").text == vc_name:
        #        tr.find_element_by_xpath("//*[contains(@id, 'manageVCListTable_row_selector')]//input").click()
        #self.virtual_controller.click()
        logger.debug("ManageGroupPage: Clicking on 'Move' button ")
        self.move.click()
        self.buy_time()
        logger.debug("ManageGroupPage: Clicking on required 'group' ")
        group_obj = self.browser._browser.find_element_by_xpath("//span[contains(@id,'group_table_name') and contains(text(), '%s')]" % group)
        logger.info(group_obj)
        group_obj.click()
        logger.debug("ManageGroupPage: Clicking on 'Save' button ")
        self.save.click()
        if not self.virtual_controller:
            self.logo.click()
        time.sleep(6)
        # self.all_groups_button.click()



    def move_one_vc_to_group(self, group):
        logger.debug("ManageGroupPage: Clicking on 'All Group' group ")
        self.all_group.click()
        time.sleep(5)
        if self.select_all.is_selected():
            self.select_all.click()
        logger.debug("ManageGroupPage: Clicking on vc checkbox ")
        self.virtual_controller.click()
        logger.debug("ManageGroupPage: Clicking on 'Move' button ")
        self.move.click()
        self.buy_time()
        logger.debug("ManageGroupPage: Clicking on required 'group' ")
        group_obj = self.browser._browser.find_element_by_xpath("//span[contains(@id,'group_table_name') and contains(text(), '%s')]" % group)
        logger.info(group_obj)
        group_obj.click()
        logger.debug("ManageGroupPage: Clicking on 'Save' button ")
        self.save.click()
        if not self.virtual_controller:
            self.logo.click()
        time.sleep(6)
        self.all_groups_button.click()
    
    
    def move_virtual_controller(self):
        logger.debug("ManageGroupPage: Clicking on 'samplegroup' group ")
        self.sample_group.click()
        time.sleep(5)
        if self.select_all.is_selected():
            self.select_all.click()
        logger.debug("ManageGroupPage: Clicking on vc checkbox ")
        self.virtual_controller.click()
        logger.debug("ManageGroupPage: Clicking on 'Move' button ")
        self.move.click()
        self.buy_time()
        logger.debug("ManageGroupPage: Clicking on default 'group' ")
        self.default_group1.click()
        logger.debug("ManageGroupPage: Clicking on 'Save' button ")
        self.save.click()
        if not self.virtual_controller:
            self.logo.click()
        time.sleep(6)
            
    def move_virtual_controller1(self):
        logger.debug("ManageGroupPage: Clicking on 'newgroup' group ")
        self.new_group.click()
        if self.select_all.is_selected():
            self.select_all.click()
        logger.debug("ManageGroupPage: Clicking on vc checkbox ")
        self.virtual_controller.click()
        logger.debug("ManageGroupPage: Clicking on 'Move' button ")
        self.move.click()
        logger.debug("ManageGroupPage: Clicking on default 'group' ")
        self.default_group1.click()
        logger.debug("ManageGroupPage: Clicking on 'Save' button ")
        self.save.click()
        if not self.virtual_controller:
            self.logo.click()
            
    def move_virtual_controller2(self):
        logger.debug("ManageGroupPage: Clicking on 'newgroup' group ")
        self.new_group.click()
        if self.select_all.is_selected():
            self.select_all.click()
        logger.debug("ManageGroupPage: Clicking on vc checkbox ")
        self.virtual_controller.click()
        logger.debug("ManageGroupPage: Clicking on 'Move' button ")
        self.move.click()
        logger.debug("ManageGroupPage: Clicking on 'samplegroup' group ")
        self.sample_group1.click()
        logger.debug("ManageGroupPage: Clicking on 'Save' button ")
        self.save.click()
        if not self.virtual_controller:
            self.logo.click()
            
    def delete_empty_group(self):
        logger.debug("ManageGroupPage: Clicking on 'samplegroup' group ")
        self.sample_group.click()
        time.sleep(5)
        logger.debug("ManageGroupPage: Clicking on 'Delete' button ")
        self.delete.click()
        for i in range (100):
            if self.sample_group:
                self.group_list.click()
            else:
                break
        logger.debug("ManageGroupPage: Clicking on 'Close' icon ")
        self.close_icon.click()
        if not self.sample_group:
            self.logo.click()
            
    def delete_empty_group1(self):
        logger.debug("ManageGroupPage: Clicking on 'newgroup' group ")
        self.new_group.click()
        logger.debug("ManageGroupPage: Clicking on 'Delete' button ")
        self.delete.click()
        for i in range (100):
            if self.new_group:
                self.group_list.click()
            else:
                break
        logger.debug("ManageGroupPage: Clicking on 'Close' icon ")
        self.close_icon.click()
        if not self.new_group:
            self.logo.click()
        
    def create_new_group_from_manage(self):
        logger.debug("ManageGroupPage: Clicking on 'Create New Group' Tab ")
        self.create_new_group.click()
        return CreateGroupPage(self.test, self.browser, self.config)
    
    def assert_group_has_swarm(self):
        if not self.alert_msg:
            raise AssertionError("group has not swarm can be deleted i.e. Traceback: %s" %traceback.format_exc())
        self.alert_ok.click()
    
    def move_virtual_controller3(self):
        '''
        Move switch to default group(Switch)
        '''
        logger.debug("ManageGroupPage: Clicking on 'group1' group ")
        self.group1.click()
        if self.select_vc.is_selected():
            self.select_vc.click()
        logger.debug("ManageGroupPage: Clicking on vc checkbox ")
        self.select_vc.click()
        logger.debug("ManageGroupPage: Clicking on 'Move' button ")
        self.move.click()
        logger.debug("ManageGroupPage: Clicking on 'switch' group") 
        self.switch_group.click()
        logger.debug("ManageGroupPage: Clicking on 'Save' button ")
        self.save.click()
        if not self.select_vc:
            self.logo.click()    
    
    def delete_group1(self):
        '''
            Delete newly created group
        '''
        logger.debug("ManageGroupPage: Clicking on 'group1' group ")
        self.buy_time()
        self.group1.click()
        self.buy_time()
        logger.debug("ManageGroupPage: Clicking on 'Delete' button ")
        self.delete.click()
        self.buy_time()
        for i in range (100):
            if self.new_group:
                self.group_list.click()
            else:
                break
        logger.debug("ManageGroupPage: Clicking on 'Close' icon ")
        self.close_icon.click()
        if not self.new_group:
            self.logo.click()    
    
    def move_virtual_controller4(self):
        logger.debug("ManageGroupPage: Clicking on 'group2' group ")
        self.group2.click()
        if self.select_vc.is_selected():
            self.select_vc.click()
        logger.debug("ManageGroupPage: Clicking on VC checkbox ")
        self.select_vc.click()
        logger.debug("ManageGroupPage: Clicking on 'Move' button ")
        self.move.click()
        logger.debug("ManageGroupPage: Clicking on 'switch' group") 
        self.switch_group.click()
        logger.debug("ManageGroupPage: Clicking on 'Save' button ")
        self.save.click()
        if not self.select_vc:
            self.logo.click()    
    
    def delete_group2(self):
        logger.debug("ManageGroupPage: Clicking on 'group2' group")
        self.group2.click()
        logger.debug("ManageGroupPage: Clicking on 'Delete' button ")
        self.delete.click()
        for i in range (100):
            if self.new_group:
                self.group_list.click()
            else:
                break
        logger.debug("ManageGroupPage: Clicking on 'Close' icon ")
        self.close_icon.click()
        if not self.new_group:
            self.logo.click()    
    
    def assert_sample_group_witn_no_vc(self):
        self.sample_group.click()
        if not self.no_data_message:
            raise AssertionError("samplegroup have the vc i.e. Traceback: %s" %traceback.format_exc())
            
    def delete_default_group(self):
        '''
            Delete default group
        '''
        logger.debug("ManageGroupPage: Clicking on default 'group'")
        self.default_group.click()
        logger.debug("ManageGroupPage: Clicking on 'Delete' button ")
        self.delete.click()
        
    def assert_default_group_does_not_delete(self):
        if not self.alert_msg :
            raise AssertionError("default group has deleted !!! i.e. Traceback: %s" %traceback.format_exc())

    def assert_current_working_group_does_not_delete(self):
        if not self.alert_msg_for_current_working_group :
            import traceback
            raise AssertionError("Current working group has deleted !!! i.e. Traceback: %s" %traceback.format_exc())
            
    def delete_current_working_group(self):
        logger.debug("ManageGroupPage: Clicking on 'samplegroup' group")
        self.sample_group.click()
        logger.debug("ManageGroupPage: Clicking on 'Delete' button ")
        self.delete.click()
        
    def cloning_samplegroup2(self):
        logger.debug("ManageGroupPage: Clicking on 'samplegroup' group")
        self.sample_group.click()
        logger.debug("ManageGroupPage: Clicking on 'Clone' button ")
        self.clone.click()
        logger.debug("ManageGroupPage: setting the group name")
        self.group_name.set(self.config.config_vars.group_samplegroup2)
        logger.debug("ManageGroupPage: Clicking on 'Save' button ")
        self.save_group.click()
        
    def delete_empty_group_samplegroup2(self):
        logger.debug("ManageGroupPage: Clicking on 'samplegroup2' group")
        self.samplegroup2.click()
        time.sleep(5)
        logger.debug("ManageGroupPage: Clicking on 'Delete' button ")
        self.delete.click()
        for i in range (100):
            if self.sample_group:
                self.group_list.click()
            else:
                break
        logger.debug("ManageGroupPage: Clicking on Close icon ")
        self.close_icon.click()
        if not self.sample_group:
            self.logo.click()        
    def move_group_wihtout_selecting_vc(self):
        logger.debug("ManageGroupPage: Clicking on 'samplegroup' group")
        self.sample_group.click()
        logger.debug("ManageGroupPage: Clicking on 'Move' button ")
        self.move.click()

    def assert_move_group_wihtout_selecting_vc(self):
        if not self.alert_msg_for_moving_group_without_selecting_vc :
            raise AssertionError("Group has moved without selecting vc !!! i.e. Traceback: %s" %traceback.format_exc())

    def assert_delete_and_clone_disabled_for_all_group(self):
        self.all_group.click()
        if not self.disabled_delete and self.disabled_clone :
            raise AssertionError("Delete and clone buttons are not disabled for all group i.e. Traceback: %s" %traceback.format_exc())    
    
    def delete_empty_groups(self):
        logger.debug("ManageGroupPage: Deleting the groups")
        if self.manage_alpha_group_a:
            self.manage_alpha_group_a.click()
            self.click_on_delete_button()
        if self.manage_alpha_group_b:
            self.manage_alpha_group_b.click()
            self.click_on_delete_button()
        if self.manage_alpha_group_c:
            self.manage_alpha_group_c.click()
            self.click_on_delete_button()
        if self.manage_alpha_group_d:
            self.manage_alpha_group_d.click()
            self.click_on_delete_button()
        if self.manage_alpha_group_e:
            self.manage_alpha_group_e.click()
            self.click_on_delete_button()
        if self.manage_alpha_group_f:
            self.manage_alpha_group_f.click()
            self.click_on_delete_button()
        if self.manage_alpha_group_g:
            self.manage_alpha_group_g.click()
            self.click_on_delete_button()
        if self.manage_alpha_group_h:
            self.manage_alpha_group_h.click()
            self.click_on_delete_button()
        if self.manage_alpha_group_i:
            self.manage_alpha_group_i.click()
            self.click_on_delete_button()
        if self.manage_alpha_group_j:
            self.manage_alpha_group_j.click()
            self.click_on_delete_button()

    def buy_time(self):
        time.sleep(5)

    def click_on_delete_button(self):
        logger.debug('ManageGroupPage: Clicking on "Delete" button ')
        self.buy_time()
        self.delete.click()
        self.buy_time()
    
    def delete_four_empty_groups(self):
        logger.debug("ManageGroupPage: Deleting the groups")
        if self.group_name_a:
            self.group_name_a.click()
            logger.debug('ManageGroupPage: Clicking on "Delete" button ')
            self.click_on_delete_button()
        if self.group_name_spcl_char:
            self.group_name_spcl_char.click()
            logger.debug('ManageGroupPage: Clicking on "Delete" button ')
            self.click_on_delete_button()
        if self.group_name_8:
            self.group_name_8.click()
            logger.debug('ManageGroupPage: Clicking on "Delete" button ')
            self.click_on_delete_button()
        if self.group_name_1group:
            self.group_name_1group.click()
            logger.debug('ManageGroupPage: Clicking on "Delete" button ')
            self.click_on_delete_button()
            
    def assert_default_manage_groups_fields(self):
        '''
        Asserts Manage  groups default fields
        '''
        self.buy_time()
        if not self.manage_groups_button:    
            raise AssertionError("Manage Group tab is not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.create_groups_button:    
            raise AssertionError("Create Group tab is not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.all_group:
            raise AssertionError("by deafault Manage Groups fields are not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.default_group:    
            raise AssertionError(" Default Group  is not Present  i.e. Traceback: %s" %traceback.format_exc())
        if not self.disabled_delete:    
            raise AssertionError(" Manage Group Delete button is not Present  i.e. Traceback: %s" %traceback.format_exc())    
        self.buy_time()
        if not self.disabled_clone:    
            raise AssertionError(" Manage Group Clone button is not Present  i.e. Traceback: %s" %traceback.format_exc())
        if not self.move:    
            raise AssertionError("Manage Group Move button is not Present  i.e. Traceback: %s" %traceback.format_exc())
        if not self.manage_group_close:    
            raise AssertionError(" manage group close button is not Present  i.e. Traceback: %s" %traceback.format_exc())
            
    
    def click_manage_group_close_button(self):
        '''
        Clicking on Manage Group Close button
        '''
        self.buy_time()
        logger.debug("ManageGroupPage: Clicking on cancel button ")
        self.manage_group_close.click()
        
    def click_all_group_button(self):
        '''
        Clicking on All Groups  button
        '''
        self.buy_time()
        logger.debug("ManageGroupPage: Clicking on All Group  button ")
        self.all_groups_button.click()
    
    def click_move_button(self):
        '''
        Clicking on Move button
        '''
        self.buy_time()
        logger.debug("ManageGroupPage: Clicking on Move  button ")
        self.move.click()
    
    def click_alert_ok_button(self):
        '''
        Clicking on OK button
        '''
        self.buy_time()
        logger.debug("ManageGroupPage: Clicking on OK  button ")
        self.alert_ok.click()
    
    def assert_mygroup_and_mynew(self):
        '''
        Asserts newly created Groups Mygroup and Mynew
        '''
        logger.debug('LeftPanel: Checking Mygroup is present or not')
        self.browser.assert_element(self.Mygroup,'Mygroup is  not Present')
        logger.debug('LeftPanel: Checking Mynew group is present or not')
        self.browser.assert_element(self.Mynew,'Mynew group is  not Present')
    
    def move_virtual_controller5(self):
        logger.debug("ManageGroupPage: Clicking on 'Mygroup' group ")
        if self.Mygroup:
            self.Mygroup.click()
            time.sleep(5)
            if self.select_all.is_selected():
                self.select_all.click()
            logger.debug("ManageGroupPage: Clicking on vc checkbox ")
            self.virtual_controller.click()
            logger.debug("ManageGroupPage: Clicking on 'Move' button ")
            self.move.click()
            self.buy_time()
            logger.debug("ManageGroupPage: Clicking on default 'group' ")
            self.default_group1.click()
            logger.debug("ManageGroupPage: Clicking on 'Save' button ")
            self.save.click()
            if not self.virtual_controller:
                self.logo.click()
            time.sleep(6)
            
    def delete_empty_mygroup(self):
        logger.debug("ManageGroupPage: Deleting the groups")
        if self.Mygroup:
            self.Mygroup.click()
            self.click_on_delete_button()

    def delete_empty_mynew_group(self):
        logger.debug("ManageGroupPage: Deleting the groups")
        if self.Mynew:
            self.Mynew.click()
            self.click_on_delete_button()
            
    def cloning_mygroup2(self):
        self.Mygroup.click()
        self.clone.click()
        self.group_name.set(self.config.config_vars.my_group_2)
        self.save_group.click()
        
    def assert_delete_and_clone_enabled_for_other_groups(self):
        self.default_group.click()
        if self.disabled_delete and self.disabled_clone :
            raise AssertionError("Delete and clone buttons are not enabled for other group i.e. Traceback: %s" %traceback.format_exc())
            
        self.Mygroup.click()
        if self.disabled_delete and self.disabled_clone :
            raise AssertionError("Delete and clone buttons are not enabled for other group i.e. Traceback: %s" %traceback.format_exc())
            
        self.Mygroup2.click()
        if self.disabled_delete and self.disabled_clone :
            raise AssertionError("Delete and clone buttons are not enabled for other group i.e. Traceback: %s" %traceback.format_exc())
            
    def move_virtual_controller_from_Mygroup(self,mygroup=False,mygroup2=False,group1=False,group2=False):
        logger.debug("ManageGroupPage: Clicking on 'Mygroup' group ")
        if mygroup:
            self.Mygroup.click()
        if mygroup2:
            self.Mygroup2.click()
        if group1:
            self.group1.click()
        if group2:
            self.group2.click()
        time.sleep(5)
        if self.select_all.is_selected():
            self.select_all.click()
        logger.debug("ManageGroupPage: Clicking on vc checkbox ")
        self.virtual_controller.click()
        logger.debug("ManageGroupPage: Clicking on 'Move' button ")
        self.move.click()
        self.buy_time()
        logger.debug("ManageGroupPage: Clicking on default 'group' ")
        self.default_group1.click()
        logger.debug("ManageGroupPage: Clicking on 'Save' button ")
        self.save.click()
        if not self.virtual_controller:
            self.logo.click()
        time.sleep(6)
        
    def delete_empty_Mygroup1(self):
        logger.debug("ManageGroupPage: Clicking on 'Mygroup' group ")
        self.Mygroup.click()
        time.sleep(5)
        logger.debug("ManageGroupPage: Clicking on 'Delete' button ")
        self.delete.click()
        for i in range (100):
            if self.Mygroup:
                self.group_list.click()
            else:
                break
        logger.debug("ManageGroupPage: Clicking on 'Close' icon ")
        self.close_icon.click()
        if not self.Mygroup :
            self.logo.click()
            
    def delete_empty_Mygroup2(self):
        logger.debug("ManageGroupPage: Clicking on 'Mygroup2' group ")
        self.Mygroup2.click()
        time.sleep(5)
        logger.debug("ManageGroupPage: Clicking on 'Delete' button ")
        self.delete.click()
        for i in range (100):
            if self.Mygroup2:
                self.group_list.click()
            else:
                break
        logger.debug("ManageGroupPage: Clicking on 'Close' icon ")
        self.close_icon.click()
        if not self.Mygroup2 :
            self.logo.click()
            
    def move_virtual_controller5(self):
        logger.debug("ManageGroupPage: Clicking on 'default' group ")
        self.default_group.click()
        if self.select_all.is_selected():
            self.select_all.click()
        logger.debug("ManageGroupPage: Clicking on vc checkbox ")
        self.virtual_controller.click()
        logger.debug("ManageGroupPage: Clicking on 'Move' button ")
        self.move.click()
        logger.debug("ManageGroupPage: Clicking on 'samplegroup' group ")
        self.sample_group.click()
        logger.debug("ManageGroupPage: Clicking on 'Save' button ")
        self.save.click()
        if not self.virtual_controller:
            self.logo.click()
            
    def move_virtual_controller_group1(self):
        logger.debug("ManageGroupPage: Clicking on 'Mygroup' group ")
        if self.group1:
            self.group1.click()
            time.sleep(5)
            if self.select_all.is_selected():
                self.select_all.click()
            logger.debug("ManageGroupPage: Clicking on vc checkbox ")
            self.virtual_controller.click()
            logger.debug("ManageGroupPage: Clicking on 'Move' button ")
            self.move.click()
            self.buy_time()
            logger.debug("ManageGroupPage: Clicking on default 'group' ")
            self.default_group1.click()
            logger.debug("ManageGroupPage: Clicking on 'Save' button ")
            self.save.click()
            if not self.virtual_controller:
                self.logo.click()
            time.sleep(6)

    def delete_specific_group(self,group1=False,group2=False):
        '''
        Delete newly created group
        '''
        logger.debug("ManageGroupPage: Clicking on group which has to be deleted ")
        self.buy_time()
        if group1:
            self.group1.click()
        if group2:
            self.group2.click()
        time.sleep(5)
        logger.debug("ManageGroupPage: Clicking on 'Delete' button ")
        self.delete.click()
        self.buy_time()
        logger.debug("ManageGroupPage: Clicking on 'Close' icon ")
        self.close_icon.click()
        if not self.new_group:
            self.logo.click()

    def move_virtual_controller_between_two_groups(self,group1,group2):
        logger.debug("ManageGroupPage: Moving VC from one group to another group")
        if group1:
            group1.click()
            time.sleep(5)
            if self.select_all.is_selected():
                self.select_all.click()
            logger.debug("ManageGroupPage: Clicking on vc checkbox ")
            self.virtual_controller.click()
            logger.debug("ManageGroupPage: Clicking on 'Move' button ")
            self.move.click()
            self.buy_time()
            group2.click()
            # self.move_to_group1.click()
            logger.debug("ManageGroupPage: Clicking on 'Save' button ")
            self.save.click()
            if not self.virtual_controller:
                self.logo.click()
            time.sleep(6)            
            
    def delete_empty_group2(self):
        if self.group2:
            logger.debug("ManageGroupPage: Clicking on 'group2' group")
            self.group2.click()
            logger.debug("ManageGroupPage: Clicking on 'Delete' button ")
            self.delete.click()
            
    def select_group(self,group):
        '''
        selects a group to move
        '''
        logger.debug('ManageGroupPage : Clicking on group')
        group.click()
        
    def save_move_vc(self):
        '''
        clicks on save button
        '''
        logger.debug('ManageGroupPage : Clicking on save button')
        self.save.click()
        
        
    def move_all_switch_from_anygroup_to_default(self,mygroup=False,mygroup2=False,group1=False,group2=False):
        logger.debug("ManageGroupPage: Clicking on 'Mygroup' group ")
        if mygroup:
            self.Mygroup.click()
        if mygroup2:
            self.Mygroup2.click()
        if group1:
            self.group1.click()
        if group2:
            self.group2.click()
        time.sleep(5)
        
        logger.debug("ManageGroupPage: Click on 'Switch' Tab ")
        self.clicking_switch_tab()
        
        logger.debug("ManageGroupPage: Clicking on select all switch checkbox ")
        self.select_vc.click()
    
        logger.debug("ManageGroupPage: Clicking on 'Move' button ")
        self.move.click()
        self.buy_time()
        logger.debug("ManageGroupPage: Clicking on default 'group' ")
        self.default_group1.click()
        logger.debug("ManageGroupPage: Clicking on 'Save' button ")
        self.save.click()
        
        
    def select_group1_to_move_device(self):
        logger.debug("ManageGroupPage: Clicking on 'group1' ")
        self.select_group_1.click()
        logger.debug("ManageGroupPage: Clicking on 'Save' button ")
        self.save.click()
        
    def move_switch_to_default_switch_group(self):
        '''
        Move switch to default group(Switch)
        '''
        logger.debug("ManageGroupPage: Clicking on 'group1' group ")
        self.group1.click()
        logger.debug("ManageGroupPage: Click on 'Switch' Tab ")
        self.clicking_switch_tab()
        logger.debug("ManageGroupPage: Clicking on switch checkbox ")
        if not self.group1_switch.is_selected():
            self.group1_switch.click()
        logger.debug("ManageGroupPage: Clicking on 'Move' button ")
        self.move.click()
        logger.debug("ManageGroupPage: Clicking on 'switch' group") 
        self.switch_group.click()
        logger.debug("ManageGroupPage: Clicking on 'Save' button ")
        self.save.click()
        if not self.select_vc:
            self.logo.click()
            
    def click_configuration_page_new_group_button(self):
        logger.debug("ManageGroupPage: Click on New Group")
        time.sleep(5)
        self.new_group_button.click()
        return CreateGroupPage(self.test, self.browser, self.config)
        
    def click_switches_toggle(self):
        logger.debug("ManageGroupPage: Click on switches toggle")
        self.switches_toggle.click()
        
    def clone_group1(self):
        logger.debug("ManageGroupPage: Clicking on 'group1' group ")
        self.group1.click()
        self.click_switches_toggle()
        self.clone.click()
        self.group_name.set(self.config.config_vars.group_2)
        self.save_group.click()
        
        
    # def click_configuration_page_new_group_button(self):
        # logger.debug("ManageGroupPage: Click on New Group")
        # self.new_group_button.click()
        # time.sleep(4)    
        
    def clicking_switch_tab(self):
        logger.debug("ManageGroupPage: Click on 'Switch' Tab ")
        self.switches_toggle .click()
        
    def click_on_switch_tab(self):
        '''
        clicks on switch tab
        '''
        logger.debug('ManageGroupPage : Clickiing Switch tab')
        if self.toggle_switch:
            self.toggle_switch.click()    
    
    def selects_and_delects_iap_Switch(self, select, check):
        '''
        Selects iaps and switches
        '''
        if select:
            logger.debug('ManageGroupPage : selecting device ')
            if not check.is_selected():
                check.click()
        else:    
            logger.debug('ManageGroupPage : deselecting device ')
            if check.is_selected():
                check.click()
    
    def click_on_vc_tab(self):
        '''
        clicks on vc tab
        '''
        logger.debug('ManageGroupPage : Clickiing vc tab')
        if self.switches_toggle :
            self.switches_toggle .click()
                
    def move_switches_to_group2(self,from_grop, to_group,vc):
        '''
        moving switches to group2
        '''
        self.select_group(from_grop)
        self.selects_and_delects_iap_Switch(True,vc)
        self.click_move_button()
        self.select_group(to_group)
        self.save_move_vc()
        
        
    def move_all_virtual_controller_to_default_group(self):
        logger.debug("ManageGroupPage: Clicking on 'Mygroup' group ")
        self.select_all.click()
        logger.debug("ManageGroupPage: Clicking on 'Move' button ")
        self.move.click()
        self.buy_time()
        logger.debug("ManageGroupPage: Clicking on default 'group' ")
        self.default_group1.click()
        logger.debug("ManageGroupPage: Clicking on 'Save' button ")
        self.save.click()
        
    def move_unprovisioned_device(self,device,group=None,group_name=''):
        '''
        Moves a unprovioned switch or IAP to new group or overwrite config to existing group.
        '''
        myDevice = Device.getDeviceObject(device)
        if "IAP" in device:
            device_name=myDevice.get("vc_name")
        else:
            device_name=myDevice.get("switch_name")
        # self.TopPanel.click_slider_icon()
        # self.slider_icon.click()
        logger.debug("ManageGroupPage: Select device ")
        raw_input('check1')
        print self.browser._browser.find_element_by_xpath("//span[contains(.,'%s')]" %device_name)
        self.browser._browser.find_element_by_xpath("//span[contains(.,'%s')]" %device_name).click()
        import time
        time.sleep(5)
        # self.browser._browser.find_element_by_xpath("//span[contains(.,'%s')]" %device_name)
        self.browser._browser.find_element_by_xpath("//span[contains(.,'%s')]" %device_name).click()
        # self.browser._browser.find_element_by_xpath("//span[contains(.,'ArubaS2500')]").click()
        # self.browser._browser.find_element_by_xpath("//span[contains(.,'ArubaS2500')]").click()
        time.sleep(10)
        if group == 'New Group':
            logger.debug("ManageGroupPage: Click on new group.")
            self.unprovisioned_new_group.click()
            logger.debug("ManageGroupPage: set group name.")
            self.group_name.set(group_name)
            logger.debug("ManageGroupPage: Click on save")
            self.creategroup_btn.click()
            logger.debug("ManageGroupPage: set password.")
            self.password_text.set('test123')           
            logger.debug("ManageGroupPage: set password again.")
            self.confirm_password_text.set('test123')
            logger.debug("ManageGroupPage: Click on save.")
            self.browser._browser.find_element_by_xpath("//button[contains(@id,'group_sidebar_cddc_creategrpddc') and text()='Save']").click()
        else:
            logger.debug("ManageGroupPage: Click on existing group")
            self.existing_group.click()
            logger.debug("ManageGroupPage: select group")           
            self.browser._browser.find_element_by_xpath("//span[contains(@id,'group_table_name') and text()='%s']" %group_name).click()
            # print self.browser._browser.find_element_by_xpath("//span[contains(@id,'group_sidebar_save') and text()='Save']")
            # raw_input('save')
            logger.debug("ManageGroupPage: Click save")         
            self.browser._browser.find_element_by_xpath("//span[contains(@id,'group_sidebar_save') and text()='Save']").click()

            
    def move_device_to_group(self,group,device):
        '''
        Move device from one one group to other .
        '''
        myDevice = Device.getDeviceObject(device)
        if not "IAP" in device:
            logger.debug("ManageGroupPage: Click on switches_toggle")
            self.switches_toggle.click()
            self.switches_toggle.click()
            device_name=myDevice.get("switch_name")
        else:
            self.browser._browser.find_element_by_xpath("//a[@id='toggle_vc']").click()
            device_name=myDevice.get("vc_name")
        logger.debug("ManageGroupPage: Select device")      
        self.browser._browser.find_element_by_xpath("//span[contains(.,'%s')]/../preceding-sibling::td[1]/input" %device_name).click()
        logger.debug("ManageGroupPage: Clicking on 'Move' button ")
        self.move.click()
        self.buy_time()
        logger.debug("ManageGroupPage: Clicking on required 'group' ")
        group_obj = self.browser._browser.find_element_by_xpath("//span[contains(@id,'group_table_name') and contains(text(), '%s')]" % group)
        logger.info(group_obj)
        group_obj.click()
        logger.debug("ManageGroupPage: Clicking on 'Save' button ")
        self.save.click()
        
    def clone_group(self,source='',destination=''):
        '''
        Clone group 
        '''
        logger.debug("ManageGroupPage: Clicking on 'samplegroup' group")
        self.browser._browser.find_element_by_xpath("//span[contains(@id,'group_sidebar_group_name') and text()='%s']" % source).click()
        logger.debug("ManageGroupPage: Clicking on 'Clone' button ")
        self.clone.click()
        logger.debug("ManageGroupPage: setting the group name")
        self.group_name.set(destination)
        logger.debug("ManageGroupPage: Clicking on 'Save' button ")
        self.save_group.click()
