from athenataf.lib.util.WebPage import WebPage
from athenataf.lib.functionality.page.group.CreateGroupPage import CreateGroupPage
from athenataf.lib.functionality.page.group.ManageGroupsPage import ManageGroupsPage
from athenataf.lib.functionality.page.common.AllGroupPage import AllGroupPage
import logging
logger = logging.getLogger('athenataf')
import time
import traceback
from Device_Module.ObjectModule import Device
class InnerLeftPanel(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "DashboardInnerLeftpanel", test, browser, config)
        self.test.assertPageLoaded(self)

    def isPageLoaded(self):
        if self.all_group_lebel:
            return True 
        else:
            return False 
            
    def add_group(self):
        logger.debug('InnerLeftPanel: Clicking on Add icon')
        time.sleep(4)
        self.add_button.click()
        # if self.all_group1:
            # pass
        return CreateGroupPage(self.test, self.browser, self.config)
        
    def manage_group(self):
        logger.debug('InnerLeftPanel: Clicking on "Manage" icon')
        time.sleep(4)
        self.manage.click()
        # if self.all_group1:
            # pass
        return ManageGroupsPage(self.test, self.browser, self.config)
        
    def assert_group(self):
        logger.debug('InnerLeftPanel: Asserting the group name')
        if self.group_1 or self.group_name:
            return True
        else:
            return False
            
    def assert_group_not_exist(self):
        logger.debug('InnerLeftPanel: Asserting the group name')
        if not self.group_name:
            return True
        else:
            raise AssertionError("%s Group not deleted i.e. Traceback: %s" % (self.config.config_vars.group_name_string,traceback.format_exc()))
            
    def assert_group_exist(self):
        logger.debug('InnerLeftPanel: Asserting the group name')
        if self.group_name:
            return True
        else:
            raise AssertionError("%s Group not created i.e. Traceback: %s" % (self.config.config_vars.group_name_string,traceback.format_exc()))
            
    def assert_virtual_controller(self):
        logger.debug('InnerLeftPanel: Asserting the virtual controller')
        if not self.default_group1:
            return True
        else:
            raise AssertionError("virtual controller not moved to default group i.e. Traceback: %s" %traceback.format_exc())
            
    def select_sample_group(self):
        logger.debug('InnerLeftPanel: Clicking on "SampleGroup" ')
        self.group_name.click()
        if self.all_group1:
            pass
            
    def select_new_group(self):
        logger.debug('InnerLeftPanel: Clicking on "NewGroup" ')
        self.new_group.click()
        if self.all_group1:
            pass
            
    def select_default_group(self):
        logger.debug('InnerLeftPanel: Clicking on default "Group" ')
        self.default_group.click()
        if self.all_group1:
            pass
        
    def assert_sample_group_with_vc_present(self):
        if self.group_name_with_vc:
            return True
        else :
            return False
            
    def assert_sample_group_without_vc_present(self):
        if self.group_name_without_vc:
            return True
        else :
            return False    
        
    def assert_group_with_selected_vc_present(self):
        if not self.group_name_with_vc:
            raise AssertionError("group does not contains virtual controller i.e. Traceback: %s" %traceback.format_exc())
    
    def assert_group_with_no_vc(self):
        if not self.group_name_without_vc:
            raise AssertionError("group does contains virtual controller i.e. Traceback: %s" %traceback.format_exc())
    
    def select_device(self):
        logger.debug('InnerLeftPanel: Clicking on plus(+) icon to expand the group')
        self.expand_group_icon.click()
        time.sleep(4)
        logger.debug('InnerLeftPanel: Clicking on virtual controller ')
        self.device.click()
        
    def select_default_switch(self):
        time.sleep(4)
        logger.debug('InnerLeftPanel: Clicking on "Switch" group ')
        self.switch.click()
        time.sleep(4)
        
    def select_all_group(self):
        '''
            Selecting all_group option 
        '''
        self.all_group_lebel.click()
        
    def assert_group1(self):
        if self.group1:
            raise AssertionError("group1  exist i.e. Traceback: %s" %traceback.format_exc())
        
    def assert_group2(self):
        if self.group2:
            raise AssertionError("group2 exist i.e. Traceback: %s" %traceback.format_exc())
    
    def select_aruba_switch(self):
        logger.debug('InnerLeftPanel: Clicking on plus(+) icon to expand the group')
        self.expand_switch_icon.click()
        import time
        time.sleep(4)
        logger.debug('InnerLeftPanel: Clicking on virtual controller ')
        self.aruba_switch.click()
        
    def select_group1(self):
        logger.debug("InnerLeftPanel: selecting group1 ")
        self.group_1.click()
        
    def manage_groups(self):
        time.sleep(4)
        logger.debug('InnerLeftPanel: Clicking on "ManageGroup" Tab')
        self.manage_groups_button.click()
        return ManageGroupsPage(self.test, self.browser, self.config)
        
    def select_samplegroup(self):
        logger.debug("InnerLeftPanel: selecting samplegroup ")
        self.samplegroup.click()
        
    def select_samplegroup2(self):
        logger.debug("InnerLeftPanel: selecting samplegroup ")
        self.samplegroup2.click()   
        
    def select_switch_device(self):
        logger.debug('InnerLeftPanel: Clicking on plus(+) icon to expand the group')
        self.expand_switch_icon_2.click()
        import time
        time.sleep(4)
        logger.debug('InnerLeftPanel: Clicking on virtual controller ')
        self.aruba_switch.click()
        
    def click_all_groups_label(self):
        self.all_groups_label.click()
        return AllGroupPage(self.test, self.browser, self.config)
      
    def select_wireless_configuration_module(self):
        logger.debug('LeftPanel: Clicking on Wireless Configuration Option')
        self.wireless_configuration_module.click()  

    def assert_valid_group_names(self):
        '''
        Asserting valid group name
        '''
        if not self.group_name_1group:
            raise AssertionError("Group Name text box is not accepting the name starts with number i.e. Traceback: %s" %traceback.format_exc())
        if not self.group_name_8:
            raise AssertionError("Group Name text box is not accepting single digit as group name  i.e. Traceback: %s" %traceback.format_exc())
        if not self.group_name_a:
            raise AssertionError("Group Name text box is not accepting single alphabet as group name  i.e. Traceback: %s" %traceback.format_exc())
        if not self.group_name_spcl_char:
            raise AssertionError("Group Name text box is not accepting special characters i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_mygroup_with_vc_present(self):
        if self.mygroup_name_with_vc:
            return True
        else :
            return False
    
    def assert_mygroup_without_vc_present(self):
        if self.mygroup_name_without_vc:
            return True
        else :
            return False
            
    def assert_mynew_group(self):
        logger.debug('InnerLeftPanel: Asserting the group name')
        if self.Mynew_group:
            return True
        else:
            return False        
    
    def assert_mygroup(self):
        logger.debug('InnerLeftPanel: Asserting the group name')
        if self.Mygroup_name:
            return True
        else:
            return False
            
    def assert_Mygroups(self):
        logger.debug('InnerLeftPanel: Asserting the group name')
        if self.Mygroup_name or self.Mygroup_name_2:
            return True
        else:
            return False

    def select_group(self,group):       
        '''
        Selects a group
        '''
        logger.debug("InnerLeftPanel: selecting group1 ")
        group.click()

    def assert_group1_and_group2(self):
        logger.debug('InnerLeftPanel: Asserting the group name')
        if self.group_1 or self.group_two:
            return True
        else:
            return False

    def select_group2(self):
        logger.debug("InnerLeftPanel: selecting group2 ")
        self.group_two.click()
        
    def click_on_close_icon(self):
        '''
        Clicks on Close Icon
        '''
        self.group_close_icon.click()
        
        
    def select_default_with_one_vc(self):
        logger.debug("InnerLeftPanel: selecting default with one vc ")
        self.default_with_vc.click()
        
    def select_group1_with_one_vc(self):
        logger.debug("InnerLeftPanel: selecting default with one vc ")
        self.group1_with_vc.click()
        
    def select_device1(self):
        logger.debug('InnerLeftPanel: Clicking on plus(+) icon to expand the group')
        self.expand_group_icon1.click()
        time.sleep(4)
        logger.debug('InnerLeftPanel: Clicking on virtual controller ')
        self.device.click()
    
    def select_group2(self):
        logger.debug("InnerLeftPanel: selecting group2 ")
        self.group_two.click()
    
    def assert_group_2(self):
        logger.debug('InnerLeftPanel: Asserting the group name')
        if self.group_two:
            return True
        else:
            return False
            
    def assert_switch_context_changes(self):
        if self.all_groups_label and self.group1_label and self.switch_label :
            return True
        else:
            raise AssertionError("All groups/group/[device] is not present i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_vc_context_changes(self):
        if self.all_groups_label and self.group1_label and self.vc_label :
            return True
        else:
            raise AssertionError("All groups/group/[device] is not present i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_open_wireless_configuration_module(self):
        if self.createnetwork:
            raise AssertionError("wireless configuration has not expand i.e. Traceback: %s" %traceback.format_exc())
            
            
    def asserting_unprovisioned_switch_list(self): 
        logger.debug("Asserting Unprovisioned Switch list")
        if not self.verify_unprovision_switch and verify_unprovision_switch_1:
            raise AssertionError("InnerLeftPanel: Multiple Switches are not displayed under 'Unprovisioned Group'")
            
    
    def click_configuration_page_existing_group_button(self):
        logger.debug("ManageGroupPage: Click on New Group")
        time.sleep()
        self.existing_group.click()
        return ManageGroupsPage(self.test, self.browser, self.config)

    def asserting_switch_as_unprovisioned_devices(self):
        logger.debug("Asswerting the Switch as Unprovisioned Switch")
        if not self.verify_unprovision_switch:
            raise AssertionError("InnerLeftPanel: Switch is not displayed under 'Unprovision Group'")

    def select_unprovision_switch(self):
        time.sleep(4)
        logger.debug('InnerLeftPanel: Clicking on "Unprovision Switch" ')
        self.swarm_1.click()
        # return CreateGroupPage(self.test, self.browser, self.config)
        
    def click_expand_group1_icon(self):
        logger.debug('InnerLeftPanel: Clicking on plus(+) icon to expand the group')
        self.expand_group_icon1.click()
        
    def select_first_swarm_in_group1(self):
        logger.debug('InnerLeftPanel: Selecting first swarm in group1')
        if self.swarm_1_group1:
            self.swarm_1_group1.click()
            
    def asserting_switch_inside_group2(self):
        import time
        time.sleep(4)
        logger.debug('InnerLeftPanel: Asserting switch in group2 ')
        if self.group2_without_switch:
            raise AssertionError("InnerLeftPanel: Switch found under 'group2'")
        
    def click_configuration_page_new_group_button(self):
        logger.debug("ManageGroupPage: Click on New Group")
        time.sleep(6)
        self.new_group_button.click()
        return CreateGroupPage(self.test, self.browser, self.config)
        
    def asserting_switch_inside_group(self):
        import time
        time.sleep(4)
        logger.debug('InnerLeftPanel: Clicking on virtual controller ')
        self.aruba_switch.click()
        
    def expand_switch_group_icon(self):
        logger.debug('InnerLeftPanel: Clicking on plus(+) icon to expand the group')
        self.expand_switch_icon_2.click()
    
    def asserting_switch_inside_default_group(self):
        logger.debug('InnerLeftPanel: Asserting switch ')
        if not self.aruba_switch:
            raise AssertionError("InnerLeftPanel : Switch is not displayed under Defaut Group")
    
    def assert_group1_group2_with_switch_and_vc(self):
        '''
        Asserts group1 and group2 with switch and vc
        '''
        logger.debug('InnerLeftPanel: Asserting the group1 with one switch and one iap')
        self.browser.assert_element(self.group1_with_switch_and_vc, 'group1 is not created')
        logger.debug('InnerLeftPanel: Asserting the group2 with one switch and one iap')
        self.browser.assert_element(self.group2_with_switch_and_vc, 'group2 is not created')
        self.click_on_expand_group_icon(self.expand_group_icon1)
        logger.debug('InnerLeftPanel: Asserting the group1 with one iap')
        self.browser.assert_element(self.vc_1, 'group1 iap is not present')
        logger.debug('InnerLeftPanel: Asserting the group1 with one Switch')
        self.browser.assert_element(self.switch_1, 'group1 Switch is not present')
        self.click_on_expand_group_icon(self.expand_group_icon2)
        logger.debug('InnerLeftPanel: Asserting the group2 with one iap')
        self.browser.assert_element(self.vc_2, 'group2 iap is not present')
        logger.debug('InnerLeftPanel: Asserting the group2 with one iap')
        self.browser.assert_element(self.switch_2, 'group2 one Switch is not present')
            
    def click_on_expand_group_icon(self, group_expand_icon):
        '''
        Clicks on expand group icon
        '''
        logger.debug('InnerLeftPanel: Clicking on plus(+) icon to expand the group')
        group_expand_icon.click()
        
    def assert_group_with_swithes_iaps(self, switch):
        '''
        asserts group2 with three switches
        '''
        logger.debug('InnerLeftPanel: Asserting the group with  Switches iap')
        self.browser.assert_element(switch, 'group Switch is not present')
    
    def assert_group_is_present_or_not(self,group):
        if group:
            return True
        else :
            return False
            
            
    def asserting_iap_as_unprovisioned_devices(self):
        logger.debug("Asserting the Iap as Unprovisioned IAP")
        if not self.verify_unprovision_iap:
            raise AssertionError("InnerLeftPanel: IAP is not displayed under 'Unprovision Group'")
            
    def select_unprovision_iap(self):
        time.sleep(4)
        logger.debug('InnerLeftPanel: Clicking on "Unprovision IAP" ')
        self.verify_unprovision_iap.click()
        
    def assert_unprovisioned_alert_popup(self):
        time.sleep(4)
        logger.debug('Asserting Unprovision Alert" ')
        if not self.existing_group and self.new_group_button:
            raise AssertionError("InnerLeftPanel: Unprovision Alert pop up did not appear")
        logger.debug('InnerLeftPanel: Clicking on close icon')
        self.close_hide_popup.click()
        
    def select_device2(self):
        logger.debug('InnerLeftPanel: Clicking on virtual controller ')
        self.device_2.click()
    
    def select_master_slave_group(self):
        logger.debug("InnerLeftPanel: selecting Master Slave Group ")
        self.master_slave_group.click()
        
        
        
    def assert_device_in_group(self,device,group=''):
        '''
        Verify if device is there in group or provisioned group
        '''
        myDevice = Device.getDeviceObject(device)
        if "IAP" in device:
            device_name=myDevice.get("vc_name")
        else:
            device_name=myDevice.get("switch_name")     
        if 'IAP' in device:
            logger.debug('InnerLeftPanel: Search IAP in group ')
            if not group == 'Unprovisioned':

                try:
                    logger.debug('InnerLeftPanel:Click on + button ')
                    print self.browser._browser.find_element_by_xpath("//span[contains(.,'%s')]/../preceding-sibling::span[contains(@id,'show_swarms')]"%group)
                    self.browser._browser.find_element_by_xpath("//span[contains(.,'%s')]/../preceding-sibling::span[contains(@id,'show_swarms')]"%group).click()
                except:
                    pass
                if not self.browser._browser.find_element_by_xpath("//span[@id='group_sidebar_groupname' and contains(.,'%s')]/../../following-sibling::ul[*]/li/a/span[contains(.,'%s')]" %(group,device_name)):
                    raise AssertionError("InnerLeftPanel: Device %s is not present in %s"%(device_name,group))
            else:
                logger.debug('InnerLeftPanel: Search device in unprovisioned group ')
                if not self.browser._browser.find_element_by_xpath("//span[contains(.,'Unprovisioned ')]/../following-sibling::ul[2]/li/a//span/span[contains(.,'%s')]" %device_name):
                        raise AssertionError("InnerLeftPanel: Device %s is not present in unprovisioned group"%device_name)
        else:
            logger.debug('InnerLeftPanel:Search switch in group ')
            if not group == 'Unprovisioned':
                try:
                    logger.debug('InnerLeftPanel:Click on + button ')
                    self.browser._browser.find_element_by_xpath("//span[contains(.,'%s')]/../preceding-sibling::span[contains(@id,'show_swarms')]"%group).click()
                except:
                    pass
                if not self.browser._browser.find_element_by_xpath("//span[@id='group_sidebar_groupname' and contains(.,'%s')]/../../following-sibling::ul[*]/li/a/span[contains(.,'%s')]" %(group,device_name)):
                    raise AssertionError("InnerLeftPanel: Device %s is not present in %s"%(device_name,group))
            else:
                logger.debug('InnerLeftPanel: Search switch in unprovisioned group ')
                if not self.browser._browser.find_element_by_xpath("//span[contains(.,'Unprovisioned')]/../following-sibling::ul[2]/li/a//span/span[contains(.,'%s')]" %device_name):
                        raise AssertionError("InnerLeftPanel: Device %s is not present in unprovisioned group"%device_name)
        
    def click_expand_default_group_icon(self):
        logger.debug('InnerLeftPanel: Clicking on plus(+) icon to expand the default group')
        self.expand_group_icon.click()
        
    def select_vc(self,iap):
        myDevice = Device.getDeviceObject(iap)
        vcname = myDevice.get("vc_name")
        time.sleep(10)
        self.browser._browser.find_element_by_xpath("//span[@class='swarm-name ng-binding swarm-with-alert' and contains(.,'%s')]" %vcname).click()
        
    def select_country_code(self,country_code = None):
        if self.select_country:
            logger.debug("Selecting the Country Code")
            self.select_country.set(country_code)
            logger.debug("Clicking on Save button")
            time.sleep(5)
            self.country_code_save.click()
            logger.debug("Clicking on OK button")
            self.ok_alert_button.click()
    
    def select_master_slave_master_vc(self,iap):
        myDevice = Device.getDeviceObject(iap)
        vcname = myDevice.get("vc_name")
        time.sleep(10)
        self.browser._browser.find_element_by_xpath("//span[ contains(.,'%s') and @id='swarm_name_1']" %vcname).click()    
        
    def click_on_default_group_expand_plus_icon(self):
        logger.debug('InnerLeftPanel: Clicking on plus(+) icon to expand the group')
        self.expand_group_icon.click()
        time.sleep(4)