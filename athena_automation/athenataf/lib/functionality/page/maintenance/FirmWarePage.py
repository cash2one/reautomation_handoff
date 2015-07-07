from athenataf.lib.util.WebPage import WebPage
import traceback
import logging
logger = logging.getLogger('athenataf')
import time
from athenataf.config import devices
from athenataf.lib.util.dateandtime import *
from Device_Module.ObjectModule import Device
class FirmWarePage(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "FirmWare", test, browser, config)
        self.test.assertPageLoaded(self)


    def isPageLoaded(self):
        if self.firmware_label:
            return True    
        else:
            return False

    def upgrade_firmware_switch(self):
        logger.debug('Selecting Switch tab')
        self.switch_tab.click
        self.switch_tab.click
        logger.debug('Clicking on switch checkbox')
        self.switch_checkbox.click()
        logger.debug('Clicking on upgrade button')
        self.upgrade_button.click()
        self.final_upgrade_button.click()

    def assert_no_data_message(self):
        if not self.switch_no_data_message:
            import traceback
            raise AssertionError("switch is available in group i.e. Traceback: %s" %traceback.format_exc())

    def click_switches(self):
        logger.debug('Selecting Switch tab')
        self.switch_tab.click()

    def verify__ui_elements_on_the_upgrade_firmware_page(self):
        if not self.hostname :
            raise AssertionError("FirmwarePage : Firmware hostname is not visible")
        if not self.macaddress :
            raise AssertionError("FirmwarePage : Firmware mac address is not visible")
        if not self.location :
            raise AssertionError("FirmwarePage : Firmware location is not visible")
        if not self.status :
            raise AssertionError("FirmwarePage : Firmware status is not visible")
        if not self.version :
            raise AssertionError("FirmwarePage : Firmware version is not visible")
            
    
    def check_firmware_page_default_value(self):
        '''
        Check Default values in Firmware Page
        '''
        logger.debug("FirmwarePage : Asserting Recommended FirmWare Version Label  ")
        self.browser.assert_element(self.firmware_version_label,'Recommended FirmWare Version Label is not present')
        logger.debug("FirmwarePage : Asserting No Data Display Label  ")
        self.browser.assert_element(self.no_data_msg,' No Data Display Label is not present')
        logger.debug("FirmwarePage : Asserting VC NAME Label  ")
        self.browser.assert_element(self.vc_name,' VC NAME Label is not present')
        logger.debug("FirmwarePage : Asserting APS Label  ")
        self.browser.assert_element(self.aps,' APS Label is not present')
        logger.debug("FirmwarePage : Asserting LOCATION Label  ")
        self.browser.assert_element(self.location_label,' LOCATION Label is not present')
        logger.debug("FirmwarePage : Asserting FirmWare Version Label  ")
        self.browser.assert_element(self.firmware_version,' FirmWare Version Label is not present')
        logger.debug("FirmwarePage : Asserting Status Label  ")
        self.browser.assert_element(self.status_label,' Status Label is not present')
        logger.debug("FirmwarePage : Asserting Upgrade Version button  ")
        self.browser.assert_element(self.upgrade_button,'Upgrade Version button is not present')
        
    def assert_no_vc_error_message(self):
        '''
        Asserts no vc selected to upgrade version Error Message
        '''
        self.browser.assert_element(self.no_vc_error_message, 'no vc selected to upgrade version Error Message is not present ')
        
    def upgrade_firmware(self):
        '''
        clicks on firmware button
        '''
        logger.debug("FirmwarePage : Clicks on Firmware Upgrade button  ")
        self.post_upgrade.click()
    
    
    def verify_custom_build_drop_down_menu(self,iap=None):
        logger.debug("FirmwarePage : Clicking on device ")
        self.select_vc_for_upgrade(iap)
        logger.debug("FirmwarePage : Clicking on Upgrade Firmware ")
        self.upgrade_button.click()
        logger.debug("FirmwarePage : Clicking on Manual option ")
        self.manual_upgrade.click()
        logger.debug("FirmwarePage : Asserting Custom build drop down ")
        if not self.version_type:
            raise AssertionError("FirmWarePage : Custom build drop down does not appear ")
        logger.debug("FirmwarePage : Selecting Custom build option ")
        self.version_type.set(self.config.config_vars.version_type_value)
        logger.debug("FirmwarePage : Asserting version list textbox  ")
        if not self.firmware_version_text:
            raise AssertionError("FirmWarePage : version list textbox does not appear ")

    def upgrade_firmware_using_custom_build_option(self,version=None,iap=None):
        import time
        logger.debug("FirmwarePage : Clicking on device ")
        self.select_vc_for_upgrade(iap)
        logger.debug("FirmwarePage : Clicking on Upgrade Firmware ")
        self.upgrade_button.click()
        logger.debug("FirmwarePage : Clicking on Manual option ")
        self.manual_upgrade.click()
        logger.debug("FirmwarePage : Selecting Custom build option ")
        self.version_type.set(self.config.config_vars.version_type_value)
        if version:
            self.firmware_version_text.set(version) 
        self.browser.key_press( u'\ue007')
        time.sleep(5)
    
    def assert_aps_over_text_availability(self):
        '''
        Asserts text that displays when over on AP.
        '''
        logger.debug("FirmwarePage : Asserting AP's detailed table.  ")
        actions = self.browser.get_action_chain()
        if self.ap_row_checkbox:
            if self.aps_box:
                actions.move_to_element(self.aps_box).perform()
                time.sleep(5)
                if not self.ap_over_details_table:
                    raise AssertionError(" AP details table is not visible. i.e. Traceback: %s" %traceback.format_exc())
                    time.sleep(5)
                    
    def check_firmware_page_default_value1(self):
        '''
        Check Default values in Firmware Page
        '''
        logger.debug("FirmwarePage : Asserting Recommended FirmWare Version Label  ")
        self.browser.assert_element(self.firmware_version_label,'Recommended FirmWare Version Label is not present')
        logger.debug("FirmwarePage : Asserting VC NAME Label  ")
        self.browser.assert_element(self.vc_name,' VC NAME Label is not present')
        logger.debug("FirmwarePage : Asserting APS Label  ")
        self.browser.assert_element(self.aps,' APS Label is not present')
        logger.debug("FirmwarePage : Asserting LOCATION Label  ")
        self.browser.assert_element(self.location_label,' LOCATION Label is not present')
        logger.debug("FirmwarePage : Asserting FirmWare Version Label  ")
        self.browser.assert_element(self.firmware_version,' FirmWare Version Label is not present')
        logger.debug("FirmwarePage : Asserting Status Label  ")
        self.browser.assert_element(self.status_label,' Status Label is not present')       
        
    def assert_device_selector_disabled(self):
        '''
        Asserts device selector is disabled.
        '''
        logger.debug("FirmwarePage : Asserting device selector is disabled. ")
        self.browser.assert_element(self.select_device_disabled,'Device selector is not disabled.') 
        
        
    def assert_cancel_upgrade_button(self):
        '''
        Asserts  upgrade cancel button
        '''
        logger.debug("FirmwarePage : Upgrade cancel button  ")
        if self.cancel_upgrade :
            raise AssertionError("FirmwarePage : upgrade cancel button is  visible")
            
    def select_first_vc(self):
        '''
        Selecting first vc
        '''
        logger.debug("FirmwarePage : Selecting first vc  ")
        self.select_device.click()
        
    def select_later_date_radio(self):
        '''
        Select later date radio
        '''
        logger.debug("FirmwarePage : Select later date radio  ")
        self.later_date_radio.click()
        
    def schedule_time(self):
        '''
        Schedules a time
        '''
        conf = self.config.config_vars
        logger.debug("FirmwarePage : Schedule time  ")
        t = get_current_hour_minute_second()
        hour = int(t[0])
        if ((hour>=0) and (hour<=11)):
            self.SessionList.set(conf.session_PM)
            self.TimeList.set(conf.hrs8)
        elif ((hour>=13) and (hour<=23)):
            hour1 = (hour-12)+1
            string_hour = str(hour1)
            if len(string_hour) == 1:
                final_string = '0'+string_hour
                self.TimeList.set(final_string)
            self.TimeList.set(string_hour)
            self.SessionList.set(conf.session_PM)
        
    def click_post_firmware_upgrade(self):
        '''
        Click Post Upgrade button
        '''
        logger.debug("FirmwarePage : Click Post Upgrade button  ")
        self.post_firmware_upgrade.click()  
        
    def set_time_zone(self,value):
        '''
        Sets time zone
        '''
        logger.debug("FirmwarePage : set time zone  ")
        self.Firmware_modem_country.set(value)
        time.sleep(5)
        
    def set_time(self,hrs,min,session):
        '''
        Sets hours , mins , session
        '''
        logger.debug("FirmwarePage : set hours  ")
        self.TimeList.set(hrs)
        logger.debug("FirmwarePage : set mins  ")
        self.TimeMinList.set(min)
        logger.debug("FirmwarePage : set session  ")
        self.SessionList.set(session)
        time.sleep(5)
        
    def asserting_device_management_and_subscription_key(self):
        logger.debug("FirmwarePage : Asserting Subscription key ")
        self.browser.assert_element(self.disable_subscription,' Subscription key is not disabled')      
        logger.debug("FirmwarePage : Asserting Device management ")
        self.browser.assert_element(self.disable_device_management,' Device management is not disabled')        
        
    def asserting_upgrade_button(self):
        logger.debug("FirmwarePage : Asserting 'Upgrade' button ")
        if self.disable_upgrade_button:
            raise AssertionError("FirmWarePage : 'Upgrade' button does not enabled ")
            
    def clicking_on_upgrade_firmware(self):
        logger.debug("FirmwarePage : Clicking on Upgrade Firmware ")
        self.upgrade_button.click()
        
    def asserting_device_upgrade_status(self):
        logger.debug("FirmWarePage: Asserting Device upgrade Status")
        if not self.upgrade_status:
            raise AssertionError("Device Upgradation failed")
        
    def upgrade_firmware_using_manual_option(self,option=None,version=None):
        logger.debug("FirmwarePage : Clicking on device ")
        self.select_device.click()
        logger.debug("FirmwarePage : Clicking on Upgrade Firmware ")
        self.upgrade_button.click()
        logger.debug("FirmwarePage : Clicking on Manual option ")
        self.manual_upgrade.click()
        logger.debug("FirmwarePage : Selecting Type ")
        self.version_type.set(option)
        self.version_list.set(version)
        time.sleep(5)
    
    def asserts_vc_details_in_firmware_vc_table(self):
        '''
        asserts Firmware vc table Fields
        '''
        vc_name = devices.IAP_1.vc_name
        location = devices.IAP_1.location
        firmware_version = devices.IAP_1.firmware_version
        logger.debug("FirmwarePage Page: Checking vc name ")
        if not self.firm_vc_name.get_attribute_value('text') == vc_name :
            raise AssertionError('vc name is not displayed')
        logger.debug("FirmwarePage Page: Checking vc location ")
        if not self.firm_vc_location.get_attribute_value('title') == location :
            raise AssertionError('vc location is not displayed')
        logger.debug("FirmwarePage Page: Checking firmware version ")
        if not self.firm_vc_version.get_attribute_value('text') == firmware_version :
            raise AssertionError('firmware version is not displayed')
    
    def asserts_vc_details_in_firmware_vc_table2(self):
        '''
        asserts Firmware vc table Fields
        '''
        vc_name = devices.IAP_2.vc_name
        location = devices.IAP_2.location
        firmware_version = devices.IAP_2.firmware_version
        logger.debug("FirmwarePage Page: Checking vc name ")
        if not self.firm_vc_name2.get_attribute_value('text') == vc_name :
            raise AssertionError('vc name is not displayed')
        logger.debug("FirmwarePage Page: Checking vc location ")
        if not self.firm_vc_location2.get_attribute_value('title') == location :
            raise AssertionError('vc location is not displayed')
        logger.debug("FirmwarePage Page: Checking firmware version ")
        if not self.firm_vc_version2.get_attribute_value('text') == firmware_version :
            raise AssertionError('firmware version is not displayed')
            
    def asserting_device_upgrade_progress(self):
        logger.debug("FirmWarePage: Asserting Device upgrade Progress")
        if not self.upgrading_label:
            raise AssertionError("Device Upgradation icon is not showing")
        
    def asserting_version_error_message(self):
        logger.debug("FirmWarePage: Asserting version textbox")
        self.browser.assert_element(self.version_error_message, "versionerror message not displayed")
        
    def select_second_vc(self):
        '''
        Selecting second vc
        '''
        logger.debug("FirmwarePage : Selecting second vc  ")
        self.select_device_2.click()
        
    def select_third_vc(self):
        '''
        Selecting third vc
        '''
        logger.debug("FirmwarePage : Selecting third vc  ")
        self.select_device_3.click()
        
    def assert_subscription_device_management_link(self):
        '''
        Checks Subscription Key and Device Management Link
        '''
        self.browser.assert_element(self.subscptions_key_link_disabled, 'Subscription Key Link is not diasabled')
        self.browser.assert_element(self.device_management_link_disabled, 'Device Management Link is not diasabled')
        
    def select_all_switches(self):
        '''
        clicks on select all checkbox 
        '''
        logger.debug('FirmwarePage: Clicking on the select all checkbox')
        selff.select_all_switch.click()
        
    def firmware_upgrade(self,switch_vc=None,Manual=False,automatic=False, option=None,version=None):
        if switch_vc == 'switch':
            logger.debug("FirmwarePage : selecting all Switches ")
            self.select_all_switch.click()
        if switch_vc == 'vc':
            logger.debug("FirmwarePage : selecting all device ")
            self.vc_check.click()
        logger.debug("FirmwarePage : Clicking on Upgrade Firmware ")
        self.upgrade_button.click()
        if manual:
            logger.debug("FirmwarePage : Clicking on Manual option ")
            self.manual_upgrade.click()
        if automatic:
            logger.debug("FirmwarePage : Clicking on Automatic option ")
            self.auto_upgrade.click()
        logger.debug("FirmwarePage : Selecting Type ")
        self.version_type.set(option)
        logger.debug("FirmwarePage : Selecting Version ")
        self.version_list.set(version)
        self.upgrade_firmware()
        time.sleep(600)
        
    def assert_upgrading_status(self):
        '''
        Checks Upgrading is in progress
        '''
        logger.debug("FirmwarePage : Checking Upgrading Status ")
        self.browser.assert_element(self.upgrading, 'Status is not changed to  Upgrading')
        
    def click_on_virtual_controller_tab(self):
        '''
        Clicks on Virtual Controller Tab
        '''
        logger.debug("FirmwarePage : Clicking on Virtual Controller ")
        self.virtual_controller.click()
        
    def asserting_device_upgraded_successful(self):
        '''
        Asserts Upgraded Successful Label
        '''
        logger.debug("FirmWarePage: Asserting Device upgrade Status")
        self.browser.assert_element(self.upgraded_successful, 'Device Upgradation failed')
        
    def click_on_manual_upgrade(self):
        '''
        Select on 'Manual' radio button.
        '''
        if self.manual_upgrade:
            logger.debug("FirmwarePage : Clicking on Manual option ")
            self.manual_upgrade.click()
            
    def upgrade_all_switches_using_manual_option(self,option=None,version=None):
        logger.debug("FirmwarePage : selecting all Switches ")
        self.select_all_switch.click()
        logger.debug("FirmwarePage : Clicking on Upgrade Firmware ")
        self.upgrade_button.click()
        logger.debug("FirmwarePage : Clicking on Manual option ")
        self.manual_upgrade.click()
        logger.debug("FirmwarePage : Selecting Type ")
        self.version_type.set(option)
        self.version_list.set(version)
        time.sleep(5)
        
    def select_version_type(self,type=None):
        logger.debug("FirmwarePage : Selecting Type ")
        self.version_type.set(type)
        logger.debug("FirmwarePage : Selecting Version ")
        options = self.version_list.get_options()
        self.version_list.set(options[1])
        
        
    def set_upgrade_after_ten_mins(self):
        conf = self.config.config_vars
        logger.debug("FirmwarePage : Schedule time  ")
        t = get_current_hour_minute_second()
        hour = int(t[0])
        min = int(t[1])
        
        logger.debug("FirmwarePage : Setting Session..  ")
        if ((hour>=0) and (hour<=11)):
            logger.debug("FirmwarePage : Setting Session 'AM'..  ")
            self.SessionList.set(conf.session_AM)
            # raw_input('session AM')
        elif ((hour>=12) and (hour<=23)):
            logger.debug("FirmwarePage : Setting Session 'AM'..  ")
            self.SessionList.set(conf.session_PM)
            # raw_input('session PM')
            
        logger.debug("FirmwarePage : Setting Minute..  ")       
        if min<10:
            logger.debug("FirmwarePage : Setting '10' Minute..  ")
            self.TimeMinList.set('10')
            # raw_input('Set 10 minutes')
        elif min>49 and min<60:
            logger.debug("FirmwarePage : Setting '00' Minute..  ")
            self.TimeMinList.set('00')
            # raw_input('set 00 minutes')
        else:
            set_minute = str(((min/10)*10)+10)
            self.TimeMinList.set(set_minute)
            # raw_input('set minutes accordingly')
            
        logger.debug("FirmwarePage : Setting Hour..  ")
        if min>49:
            next_hour = hour+1
            if next_hour>11:
                set_hour = next_hour-12
                if set_hour ==0:
                    logger.debug("FirmwarePage : Setting '12' Hour..  ")
                    self.TimeList.set('12')
                    # raw_input('Set 12 hours')
                elif set_hour==10 or set_hour==11:
                    self.TimeList.set(str(set_hour))
                    # logger.debug("FirmwarePage : Setting next Hour..  ")
                    # if set_hour==10 or set_hour==11:
                        # self.TimeList.set(str(set_hour))
                else:
                    self.TimeList.set('0'+str(set_hour))
            elif next_hour==10 or next_hour==11:
                self.TimeList.set(str(next_hour))
            else:
                self.TimeList.set('0'+str(next_hour))
        else:
            if hour==00 and hour==12:
                self.TimeList.set('12')
            elif hour>12 and hour<=21:
                current_hour = hour-12
                self.TimeList.set('0'+str(current_hour))
            elif hour==22 and hour ==23 :
                current_hour = hour-12
                self.TimeList.set(str(current_hour))
            else:
                self.TimeList.set(str(hour))
                    
                    
    def asser_successfully_upgrading_msg(self):
        logger.debug("FirmwarePage : Asserting whether the upgrade has stared ")
        if self.upgrading_status:
            logger.debug("FirmwarePage :the upgrade has stared ")
        else :
            raise AssertionError("FirmwarePage : the upgrade has not stared")
            
            
    def buy_time(self):
        import time
        time.sleep(1000)
                
    def click_switch_tab(self):
        '''
        Click Switch Tab
        '''
        logger.debug('Selecting Switch tab')
        self.switch_tab.click()
        self.switch_tab.click()

    def select_first_switch(self):
        '''
        Selecting first vc
        '''
        logger.debug("FirmwarePage : Selecting first switch ")
        self.select_switch.click()
        
    def setting_firmware_upgrade_manual_option(self,option=None,version=None):
        logger.debug("FirmwarePage : Clicking on Manual option ")
        self.manual_upgrade.click()
        logger.debug("FirmwarePage : Selecting Type ")
        self.version_type.set(option)
        self.version_list.set(version)
        # time.sleep(5)
        
    def click_cancel_icon(self):
        logger.debug("FirmwarePage : Clicking Cancel icon ")
        self.cancel_icon.click()
        
    def click_reboot_button(self):
        logger.debug("FirmwarePage : Clicking Reboot button ")
        self.reboot.click()
        
    def asserting_version_unavailable_img(self):
        '''
        Asserting version unavailable img
        '''
        logger.debug("FirmWarePage: Asserting version unavailable img")
        self.browser.assert_element(self.version_unavailable_img, 'version unavailable img is not present')
        
    def select_first_switch(self):
        '''
        Selects first switch...
        '''
        logger.debug('Clicking on switch checkbox')
        self.switch_checkbox.click()
        
    def degrade_switch_select_version_type(self,type=None):
        logger.debug("FirmwarePage : Selecting Type ")
        self.version_type.set(type)
        logger.debug("FirmwarePage : Selecting Version ")
        options = self.version_list.get_options()
        self.version_list.set(options[3])
        
    def assert_ugrade_button_is_disabled_for_readwrite_and_readonly_user(self):
        logger.debug("FirmwarePage : Clicking on device ")
        if not self.select_device.is_selected():
            self.select_device.click()
        logger.debug("FirmwarePage : Clicking on Upgrade Firmware ")
        self.upgrade_button.click()
        logger.debug("FirmwarePage : Clicking on Manual option ")
        self.manual_upgrade.click()
        logger.debug("FirmwarePage : Selecting Custom build option ")
        self.version_type.set(self.config.config_vars.version_type_value)
        if not self.disable_upgrade_button:
            raise AssertionError("FirmWarePage : 'Upgrade' button is enabled ")
        self.click_cancel_icon()
    
    def assert_firmware_version(self, ap, firmware_version):
        logger.debug("FirmwarePage : creating object of Device")
        myDevice = Device.getDeviceObject(ap)
        logger.debug("FirmwarePage : splitting the firmware version")
        version = firmware_version.split('_')[0]
        logger.debug("FirmwarePage : waiting to receive prompt")
        myDevice.receive("#")
        logger.debug("FirmwarePage : passing command 'show version' ")
        myDevice.transmit("show version")
        logger.debug("FirmwarePage : waiting to receive prompt")
        output = myDevice.receive("#")
        if not version in output:
            raise AssertionError("%s Device is not upgraded to firmware version" %version)  
            
    def select_vc_for_upgrade(self,iap):
        myDevice = Device.getDeviceObject(iap)
        vcname = myDevice.get("vc_name")
        self.browser._browser.find_element_by_xpath("//td[@title='%s']/preceding-sibling::td/input" %vcname).click()

    def get_latest_recommended_version(self):
        return self.latest_version_number_text.get_label_text()
        
    def select_switch_for_upgrade(self,switch):
        myDevice = Device.getDeviceObject(switch)
        mac_addr = myDevice.get("mac")
        self.browser._browser.find_element_by_xpath("//td[@title='%s']/preceding-sibling::td/input" %mac_addr).click()
        
    def upgrade_firmware_using_custom_build_option_for_switch(self,version=None,switch=None):
        import time
        logger.debug("FirmwarePage : Clicking on device ")
        self.select_switch_for_upgrade(switch)
        logger.debug("FirmwarePage : Clicking on Upgrade Firmware ")
        self.upgrade_button.click()
        logger.debug("FirmwarePage : Clicking on Manual option ")
        self.manual_upgrade.click()
        logger.debug("FirmwarePage : Selecting Custom build option ")
        self.version_type.set(self.config.config_vars.version_type_value)
        if version:
            self.firmware_version_text.set(version) 
        self.browser.key_press( u'\ue007')
        time.sleep(5)
        
    def assert_switch(self):
        '''
        Asserts Switch is down or not
        '''
        logger.debug("FirmWarePage:Asserting Switch showin up on ui")
        # print self.browser._browser.find_element_by_xpath("//span[contains(.,'%s')]" %devices.Switch_1.mac).is_displayed()
        try:
            if self.browser._browser.find_element_by_xpath("//span[contains(.,'%s')]" %devices.Switch_1.mac).is_displayed():
                raise AssertionError('Switch is still showing up on UI firmware')
        except:
            pass
            
    def asserts_IAP1_details_in_firmware_vc_table(self, IAP):
        myDevice = Device.getDeviceObject(IAP)
        vc_name = myDevice.get("vc_name")
        location = myDevice.get("location")
        firmware_version = myDevice.get("firmware_version")
        if not self.browser._browser.find_element_by_xpath("//td[@title='%s']" %vc_name):
            raise AssertionError('vc name is not displayed')
        if not self.browser._browser.find_element_by_xpath("//td[@title='%s']/following-sibling::td[2]/span[2][@title='%s']" %(vc_name,location)):
            raise AssertionError('vc location is not displayed')
        if not self.browser._browser.find_element_by_xpath("//td[@title='%s']/following-sibling::td[3][@title='%s']" %(vc_name,firmware_version)):   
            raise AssertionError('firmware version is not displayed')
            
    def assert_slave_details(self):
        if self.firm_second_vc:
             raise AssertionError('slave vc  is  displayed')