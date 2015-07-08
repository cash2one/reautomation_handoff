from athenataf.lib.util.WebPage import WebPage
import traceback
import logging
import time
logger = logging.getLogger('athenataf')
from athenataf.config import devices
from Device_Module.ObjectModule import Device
class DeviceManagementPage(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "DeviceManagement", test, browser, config)
        self.test.assertPageLoaded(self)


    def isPageLoaded(self):
        if self.device_management:
            return True    
        else:
            return False

    def buy_time(self):
        time.sleep(12)

    def set_select_dropdown_value(self,select_value):
        '''
        Sets value of 'SELECT' drop down value.
        '''
        if self.select:
            logger.debug("DeviceManagement Page : Setting 'SELECT' dropdown to '%s'..."%select_value)
            self.select.set(select_value)
            self.buy_time()

    def click_select_button(self):
        '''
        Clicks on 'SELECT' button
        '''
        logger.debug("DeviceManagement Page : Clicking on 'SELECT' button")
        self.select_button.click()
        self.buy_time()

    def click_unassign_button(self):
        '''
        Clicks on 'Unassign' button.
        '''
        logger.debug("DeviceManagement Page : Clicking on 'Unassign' button")
        self.unassign_button.click()
        self.buy_time()

    def select_assigned_devices(self):
        '''
        Selects assigned devices.
        '''
        self.set_select_dropdown_value(self.config.config_vars.assigned)
        self.click_select_button()

    def assert_device_unassigned(self):
        '''
        Asserts whether the Device is unassigned. 
        '''
        logger.debug("DeviceManagement Page : Asserting whether the device is unassigned. ")
        if not self.unassigned_licence_text:
            raise AssertionError("Unassigned licence text not found i.e. Traceback: %s" %traceback.format_exc())

    def change_device1_to_assigned(self):
        '''
        Changes the devices to assigned.
        '''
        logger.debug("DeviceManagement Page : Changing device to assigned. ")
        if self.unassigned_licence_text:        
            self.device_selector_1.click()
            self.click_assign_license_button()
            self.click_assign_button()
            self.buy_time()

    def change_device1_to_unassigned(self):
        '''
        Changes the devices to unassigned.
        '''
        logger.debug("DeviceManagement Page : Changing device to unassigned. ")
        if not self.unassigned_licence_text:        
            self.device_selector_1.click()
            self.click_unassign_button()
            self.buy_time()

    def click_assign_license_button(self):
        '''
        Clicks on 'Assign License(s)' button.
        '''
        logger.debug("DeviceManagement Page : Clicking on 'Assign License(s)' button.. ")
        if self.assigned_licence_button:
            self.assigned_licence_button.click()
            self.buy_time()

    def click_assign_button(self):
        '''
        Clicks on 'Assign' button.
        '''
        logger.debug("DeviceManagement Page : Clicking on 'Assign' button.. ")
        if self.assign_button:
            self.assign_button.click()
            self.buy_time()
            
    def click_on_search_icon(self):
        '''
        Clicks on Search 
        '''
        logger.debug("DeviceManagement Page: Clicking on Search Icon ")
        self.search_icon.click()

    def search_mac_address(self, mac):
        '''
        Writes Mac Adress in Mac search textbox
        '''
        logger.debug("DeviceManagement Page: Writing mac address ")
        self.mac_search_field.set(mac)

    def click_on_search_button(self):
        '''
        Clicks on Search 
        '''
        logger.debug("DeviceManagement Page: Clicking on Search Button ")
        self.search_button.click()

    def search_device_mac_address_and_asserts(self):
        '''
        search Mac Address
        '''
        mac_ad = devices.IAP_1.mac_address
        type = devices.IAP_1.iap_type
        serial_num = devices.IAP_1.serial_no
        self.click_on_search_icon()
        self.search_mac_address(mac_ad)
        self.click_on_search_button()
        logger.debug("DeviceManagement Page: Checking Device Serial Number ")
        if not self.divice_vc.get_attribute_value('text') == serial_num :
            raise AssertionError('serial number is not displayed')
        logger.debug("DeviceManagement Page: Checking Device Mac Address ")
        if not self.mac_display.get_attribute_value('text') == mac_ad :
            raise AssertionError('Mac Address is not displayed')
        logger.debug("DeviceManagement Page: Checking Device Type ")
        if not self.type_display.get_attribute_value('text') == type :
            raise AssertionError('device Model is not displayed')
    
    def asserting_device_management_field(self):
        logger.debug("DeviceManagementPage: Asserting Serial Number label")
        self.browser.assert_element(self.serial_number_label,'Serial Number is not displayed')
        logger.debug("DeviceManagementPage: Asserting MAC Address label")
        self.browser.assert_element(self.mac_address_label,'MAC Address is not displayed')      
        logger.debug("DeviceManagementPage: Asserting Type label")
        self.browser.assert_element(self.type_label,'Type is not displayed')

    def adding_device(self,key=None,mac=None):
        logger.debug("DeviceManagementPage: Clicking on 'Add Device' button")
        self.add_device.click()
        logger.debug("DeviceManagementPage: Setting Cloud Activation Key")
        if key:
            self.activation_key.set(key)
        logger.debug("DeviceManagementPage: Setting Cloud Activation Key")
        if mac:
            self.device_mac_address.set(mac)
        logger.debug("DeviceManagementPage: Clicking on 'Add' button")
        self.add_button.click()

    def asserting_device_exist_error_message(self):
        logger.debug("DeviceManagementPage: Asserting error message")
        if not self.permission_denied_label:
            raise AssertionError('DeviceManagementPage: Device exist error is not displayed')       
        logger.debug("DeviceManagementPage: Clicking on 'Ok' button")
        self.ok_button.click()

    def clicking_calcel_button(self):
        logger.debug("DeviceManagementPage: Clicking on 'Cancel' button")
        self.cancel_button.click()

    def search_device_using_mac_address(self):
        '''
        search device
        '''
        mac_ad = devices.IAP_1.mac_address
        self.click_on_search_icon()
        self.search_mac_address(mac_ad)
        self.click_on_search_button()
        
    # def select_virtual_controller(self,vc):
        # '''
        # clicks on virtual controller checkbox
        # '''
        # logger.debug("DeviceManagement Page: Clicks on vc checkbox")
        # vc.click()
        
    def assert_device_as_unassisged(self):
        logger.debug("DeviceManagement Page: Asserting 'Subscription Key' as unassigned ")
        if not self.unassign_key:
            self.setting_device_as_unassigned()
        
    def setting_device_as_unassigned(self):
        logger.debug("DeviceManagement Page: Clicks on vc checkbox")
        self.device_selector_1.click()
        logger.debug("DeviceManagement Page: Clicking on Unassign Button")
        self.unassign_button.click()
        
    def assign_license_to_device(self):
        logger.debug("DeviceManagement Page: Clicks on vc checkbox")
        self.device_selector_1.click()
        logger.debug("DeviceManagement Page: Clicking on 'Assign License' Button")
        self.assign_license.click()
        logger.debug("DeviceManagement Page: Clicking on 'Assign' Button")
        self.assign_button_0.click()
        
    def assert_subscription_key(self):
        logger.debug("DeviceManagement Page: Asserting 'Subscription key'")
        print self.license_key
        print self.subscription_key
        # raw_input("000000")
        if not self.license_key == self.subscription_key:
            raise AssertionError("DeviceManagement Page: 'Subscription key' is not matching with assign key")
        
    def assert_device_as_assisged(self):
        logger.debug("DeviceManagement Page: Asserting 'Subscription Key' as unassigned ")
        if self.unassign_key:
            self.assign_license_to_device()
        
        
    def setting_device_as_unprovisioned(self):
        logger.debug("DeviceManagement Page: Setting the device as 'Unprovisioned' ")
        if not self.unprovisioned_label:
            self.select_assign_group()
            self.set_assign_group(self.all_group)
            self.click_assign()

    def select_assign_group(self):
        '''
        clicks on assign group
        '''
        logger.debug("DeviceManagement Page: Clicks on assign group")
        self.assign_group.click()


    def set_assign_group(self,group):
        '''
        clicks on group name
        '''
        time.sleep(5)
        logger.debug("DeviceManagement Page: Clicks on vc checkbox")
        group.click()

    def click_assign(self):
        '''
        clicks on assign button
        '''
        logger.debug('DeviceManagement: Clicking on assign button')
        self.assign.click()
        
    def assert_group_name(self,group_name):
        '''
        asserts group name of vc with passed param
        '''
        if not self.group_name.get_attribute_value('text') == group_name :
            raise AssertionError('Group name is not set to')
            
    def assign_already_created_group1(self):
        '''
        Assign group if present else create new group and assign. 
        '''
        logger.debug("DeviceManagement Page : Checking for group if present. ")     
        self.device_selector_1.click()
        self.select_assign_group()
        logger.debug("DeviceManagement Page : Clicking on 'group1'. ")
        self.created_group1.click()
        self.click_assign()
        logger.debug("DeviceManagement Page : Clicking on 'OK' button. ")
        self.ok_button.click()
        self.buy_time()
        
    def adding_group(self,name=None):
        logger.debug("DeviceManagement Page: Clicks on vc checkbox")
        self.device_selector_1.click()
        logger.debug("DeviceManagement Page: Clicks on assign group")
        self.select_assign_group()
        logger.debug("DeviceManagement Page: Setting Group name")
        self.new_group_name.set(name)
        logger.debug("DeviceManagement Page: Click on add button")
        self.add_group_button.click()
        logger.debug("DeviceManagement Page: Click on 'Assign' button")
        self.click_assign()
        
        
        
        
        
    def get_device_mac_address(self):
        '''
        Gives Device Mac Address
        '''
        mac_ad = devices.IAP_1.mac_address
        return mac_ad
        
    def get_and_search_mac_address(self):
        '''
        Gets Mac Address and Search it
        '''
        mac_ad = self.get_device_mac_address()
        self.click_on_search_icon()
        self.search_mac_address(mac_ad)
        self.click_on_search_button()
        
    def assert_unassigned_licence_text(self):
        '''
        '''
        logger.debug("DeviceManagement Page : checking licence Assigned or not ")
        if self.unassigned_licence_text:    
            return True
        else:
            return False
            
    def select_virtual_controller(self,vc):
        '''
        clicks on virtual controller checkbox
        '''
        logger.debug("DeviceManagement Page: Clicks on vc checkbox")
        if not vc.is_selected():
            vc.click()

    def click_on_ok_button(self):
        '''
        Clicks on Ok button
        '''
        logger.debug('DeviceManagement: Clicking on ok button')
        self.ok_button.click()
    
    def assign_group_to_device(self):
        self.select_assign_group()
        self.group1.click()
        self.click_assign()
        self.click_on_ok_button()
    
    def assert_unassigned_subscription_key(self):
        '''
        Asserts SubscriptionKey
        '''
        logger.debug("DeviceManagement Page : checking licence Assigned or not ")
        self.browser.assert_element(self.unassigned_licence_text, 'License is not assigned',False)
    
    def assert_permission_denied_message(self):
        '''
        Asserts Permission Denied Message
        ''' 
        logger.debug("DeviceManagement Page : checking Permission denied message ")
        self.browser.assert_element(self.device_exist_error, 'License is not assigned')
    
    def create_group(self, group_name):
        '''
        creates group
        '''
        self.new_group_name.set(group_name)
        self.plus_button.click()
    
    def assert_access_denied_message(self):
        '''
        Asserts Access Denied Message
        ''' 
        logger.debug("DeviceManagement Page : Access Denied message is not present ")
        self.browser.assert_element(self.access_denied, 'Access Denied message is not present')
        
    def assert_non_preconfigured_group(self):
        logger.debug("DeviceManagement Page: Asserting Non Preconfigured Group ")
        if not self.non_preconfigured_group:
            raise AssertionError("DeviceManagement Page: Non Preconfigured Group is not Present")
            
            
    def assert_assigned_group1(self):
        logger.debug("DeviceManagement Page: Asserting Newly assigned Group ")
        if not self.group_text_group1:
            raise AssertionError("DeviceManagement Page: Group is not Present..Device management is not updated")
    
    def assert_device_present(self):
        '''
        Checks Device is present or not
        '''
        mac_ad = devices.IAP_1.mac_address  
        if self.mac_display.get_attribute_value('text') == mac_ad :
            return True
        else:
            return False
            
            
    def assign_default_group(self):
        '''
        Assign Default group . 
        '''
        logger.debug("DeviceManagement Page : Checking for group if present. ")  
        self.device_selector_1.click()
        self.select_assign_group()
        logger.debug("DeviceManagement Page : Clicking on 'group1'. ")
        self.default_group.click()
        self.click_assign()
        logger.debug("DeviceManagement Page : Clicking on 'OK' button. ")
        self.ok_button.click()
        self.buy_time()
        
    def search_device_using_mac_address_2(self,mac_ad = None):
        '''
        search device
        '''
        self.click_on_search_icon()
        self.search_mac_address(mac_ad)
        self.click_on_search_button()
        
    def selec_deselect_all_devices(self, check):
        '''
        Checks and Unchecks the devices
        '''
        if check:
            if not self.select_all.is_selected():
                self.select_all.click()
        if check==False:
            if self.select_all.is_selected():
                self.select_all.click()
            
    def assign_license_to_more_device(self):
        '''
        Assign the devices to assigned.
        '''
        logger.debug("DeviceManagement Page : Changing device to assigned. ")
        if self.unassigned_licence_text:        
            self.device_selector_1.click()
            self.click_assign_license_button()
            if self.device_with_capacity1:
                self.device_with_capacity1_assign.click()
            self.click_assign_button()
            self.buy_time()
        if self.unassigned_licence_text1:
            self.device_selector_2.click()
            self.click_assign_license_button()
            if self.device_with_capacity1:
                self.browser.assert_element(self.disabled_assign_button, 'Allowing to Assign more devices than the license capacity')
                
                
    def assert_assign_button(self):
        logger.debug("DeviceManagementPage: ")
        if self.assign_license:
            raise AssertionError("DeviceManagementPage: 'Assign' button is displayed")

    def clicking_switch_tab(self):
        logger.debug("DeviceManagementPage : Clicking on Switch Tab")
        self.switch_tab.click()

    def clicking_vc_tab(self):
        logger.debug("DeviceManagementPage : Clicking on Switch Tab")
        self.vc_tab.click()

    def click_assign_button_2(self):
        '''
        Clicks on 'Assign' button.
        '''
        logger.debug("DeviceManagement Page : Clicking on 'Assign' button.. ")
        if self.assign_button_2:
            self.assign_button_2.click()
            self.buy_time()

    def change_device1_to_assigned_2(self):
        '''
        Changes the devices to assigned.
        '''
        logger.debug("DeviceManagement Page : Changing device to assigned. ")
        if self.unassigned_licence_text:  
            self.device_selector_1.click()
            self.click_assign_license_button()
            self.click_assign_button_2()
            self.buy_time()

    def assign_already_created_group2(self):
        '''
        Assign group2 to Device .
        '''
        logger.debug("DeviceManagement Page : Checking for group if present. ")  
        self.device_selector_1.click()
        self.select_assign_group()
        logger.debug("DeviceManagement Page : Clicking on 'group2'. ")
        self.created_group2.click()
        self.click_assign()
        logger.debug("DeviceManagement Page : Clicking on 'OK' button. ")
        self.ok_button.click()
        self.buy_time()

    def search_device_and_add_if_not_exist(self,mac_ad = None,key=None):
        '''
        Adding device if not found
        '''
        self.click_on_search_icon()
        self.search_mac_address(mac_ad)
        self.click_on_search_button()
        if self.no_device_found_msg:
            self.adding_device(key,mac)

    def adding_new_device(self):
        '''
        search Mac Address
        '''
        mac_ad = devices.IAP_1.mac_address_2
        key = devices.IAP_1.activation_id
        self.adding_device(key,mac_ad)

    def search_device_using_mac_address_3(self):
        '''
        search device
        '''
        mac_ad = devices.IAP_1.mac_address_2
        self.click_on_search_icon()
        self.search_mac_address(mac_ad)
        self.click_on_search_button()

    def assert_device_present_2(self):
        '''
        Checks Device is present or not
        '''
        mac_ad = devices.IAP_1.mac_address_2 
        if self.mac_display.get_attribute_value('text') == mac_ad :
            return True
        else:
            return False
            
    def adding_device_to_server(self):
        logger.debug("DeviceManagementPage: Clicking on 'Add Device' button")
        self.add_device.click()
        logger.debug("DeviceManagementPage: Setting Cloud Activation Key")
        if key:
            actvatn_id = devices.IAP_1.activation_id
            self.activation_key.set(actvatn_id)
        logger.debug("DeviceManagementPage: Setting Cloud Activation Key")
        if mac:
            mac_ad = devices.IAP_1.mac_address
            self.device_mac_address.set(mac_ad)
        logger.debug("DeviceManagementPage: Clicking on 'Add' button")
        self.add_button.click()
        
    def assert_device_is_present_or_not(self):
        '''
        Asserts attached device is present or not
        '''
        logger.debug("DeviceManagementPage: checking attached device is present or not")
        self.browser.assert_element(self.device_selector_1, 'device is not present')
        
    def get_mac_address_of_2device(self):
        '''
        gives mac address of second device
        '''
        mac_ad = devices.IAP_2.mac_address
        return mac_ad
            
    def unassign_switch_license(self,switch):
        self.clicking_switch_tab()
        self.click_on_search_icon()
        myDevice = Device.getDeviceObject(switch)
        serial = myDevice.get("serial")
        mac_address = myDevice.get("mac")
        self.mac_search_field.set(mac_address)
        self.click_on_search_button()
        self.browser._browser.find_element_by_xpath("//span[contains(.,'%s')]/../preceding-sibling::td[1]/input" %serial).click()
        try:
            if self.unassign_button :
                self.unassign_button.click()
        except:
            pass

    def add_switch_and_assign_license(self,switch):
        myDevice = Device.getDeviceObject(switch)
        mac_address = myDevice.get("mac")
        activation_key = myDevice.get("activation_id")
        serial = myDevice.get("serial")
        self.clicking_switch_tab()
        device = self.browser._browser.find_element_by_xpath("//span[contains(.,'%s')]/../preceding-sibling::td[1]/input" %serial)
        if not device :
            logger.debug("DeviceManagementPage: Clicking on 'Add Device' button")
            self.add_device.click()
            logger.debug("DeviceManagementPage: Setting Cloud Activation Key")
            self.activation_key.set(activation_key)
            logger.debug("DeviceManagementPage: Setting Cloud Activation Key")
            self.device_mac_address.set(mac_address)
            logger.debug("DeviceManagementPage: Clicking on 'Add' button")
            self.add_button.click()
            self.browser.key_press(u'\ue00c')
        device.click()
        try:
            self.assigned_licence_button.click()
            assign = self.browser._browser.find_element_by_xpath("//a[@id='assign_0' and text()='Assign']")
            print assign
            raw_input('assign license')
            # assign.click()
        except:
            pass