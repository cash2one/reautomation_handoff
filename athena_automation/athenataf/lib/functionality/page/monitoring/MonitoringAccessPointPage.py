__author__ = 'nmehta'
from athenataf.lib.util.WebPage import WebPage
from athenataf.config import devices

#from athenataf.lib.functionality.page.common.LeftPanel import LeftPanel
#import athenataf.lib.functionality.page.common.LeftPanel
from athenataf.lib.functionality.page.monitoring.MonitoringAPDetailsPage import MonitoringAPDetailsPage
from Device_Module.ObjectModule import Device
import traceback
import logging
log = logging.getLogger('athenataf')
import time
import re

class MonitoringAccessPointPage(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "Monitoring", test, browser, config)
        self.test.assertPageLoaded(self)

    def isPageLoaded(self):
        if self.access_points_label:
            return True
        else:
            return False

    def enable_help(self):
        '''
        activate the help button
        '''
        time.sleep(2)
        if not self.help_button_enabled:
            self.help_button.click()
        else:
            self.help_button.click();self.help_button.click()
            
    def disable_help(self):
        '''
        clicks on enabled-help button
        '''
        time.sleep(2)
        if self.help_button_enabled:
            self.help_button.click()
        else:
            log.debug("Page Help button was already de-activated")

    def assert_help_option_for_access_points_flagged(self):
        '''
        asserts help text
        '''
        time.sleep(3)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.access_points_flagged).perform()
        if not self.help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(5)

    def assert_help_option_for_access_points_clients(self):
        '''
        asserts help text
        '''
        time.sleep(3)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.access_points_clients).perform()
        if not self.help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(5)

    def assert_help_option_for_access_points_throughput(self):
        '''
        asserts help text
        '''
        time.sleep(3)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.access_points_throughput).perform()
        if not self.help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(5)

    def assert_help_option_for_access_points_flagged_ap(self):
        '''
        asserts help text
        '''
        time.sleep(3)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.access_points_flagged_ap).perform()
        if not self.help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(5)

    def assert_help_option_for_access_points_flagged_util(self):
        '''
        asserts help text
        '''
        time.sleep(3)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.access_points_flagged_util).perform()
        if not self.help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(5)

    def assert_help_option_for_access_points_flagged_table_noise(self):
        '''
        asserts help text
        '''
        time.sleep(3)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.access_points_flagged_table_noise).perform()
        if not self.help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())

            time.sleep(5)


    def assert_help_option_for_access_points_flagged_table_errors(self):
        '''
        asserts help text
        '''
        time.sleep(3)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.access_points_flagged_table_errors).perform()
        if not self.help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())

            time.sleep(5)

    def assert_help_option_for_access_points_flagged_table_clients(self):
        '''
        asserts help text
        '''
        time.sleep(3)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.access_points_flagged_table_clients).perform()
        if not self.help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())

            time.sleep(5)

    def assert_help_option_for_access_points_flagged_table_memory(self):
        '''
        asserts help text
        '''
        time.sleep(3)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.access_points_flagged_table_memory).perform()
        if not self.help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())

            time.sleep(5)


    def assert_help_option_for_access_points_ap_location(self):
        '''
        asserts help text
        '''
        time.sleep(3)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.access_points_ap_location).perform()
        if not self.help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())

            time.sleep(5)

    def assert_help_option_for_access_points_ap_status(self):
        '''
        asserts help text
        '''
        time.sleep(3)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.access_points_ap_status).perform()
        if not self.help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())

            time.sleep(5)

    def assert_help_option_for_access_points_ap_clients(self):
        '''
        asserts help text
        '''
        time.sleep(3)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.access_points_ap_clients).perform()
        if not self.help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())

            time.sleep(5)
            
    def assert_help_option_for_access_points_ap_uptime(self):
        '''
        asserts help text
        '''
        time.sleep(3)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.access_points_ap_uptime).perform()
        if not self.help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())

            time.sleep(5)


    def assert_help_option_for_access_points_ap_ipadder(self):
        '''
        asserts help text
        '''
        time.sleep(3)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.access_points_ap_ipadder).perform()
        if not self.help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())

            time.sleep(5)

    def assert_help_option_for_access_points_ap_vc_name(self):
        '''
        asserts help text
        '''
        time.sleep(3)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.access_points_ap_vc_name).perform()
        if not self.help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())

            time.sleep(5)


    def assert_help_option_for_access_points_ap_vc_name(self):
        '''
        asserts help text
        '''
        time.sleep(3)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.access_points_ap_label).perform()
        if not self.help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())
            time.sleep(5)

    def check_access_page_ap_count(self):
        return self.totalAP.text

    def ap_table_empty_check(self):
        if self.access_ap_table_empty:
            return True
        else:
            raise AssertionError("AP Table is not empty. Traceback: %s" %traceback.format_exc())

            
    def assert_ap_table_empty_check_down_ap(self):
        self.access_points_totalDown.click()
        time.sleep(2)
        self.ap_table_empty_check()

    def add_label_by_variable_name_length(self, device_name, label_name, check="False"):
        ap = self.access_points_aps_table
        self.device = getattr(devices, device_name)
        lhandle = ap.find_element_by_xpath("..//td[@title='%s']" % self.device.ip)
        lhandle.find_element_by_xpath("//a[@ng-click='labelFn(row.serial_number, row.ap_labels, row.name)']").click()
        self.add_label_to_ap(label_name, check)
        self.access_points_close_add_label.click()

    def add_label_to_ap(self, label_name, check="False"):
        self.access_points_add_label_name.send_keys(label_name)
        self.access_points_add_label_button.click()
        try:
            if self.access_points_add_label_close_alert:
                self.access_points_add_label_close_alert.click()
                if check == "True":
                    return True
        except:
            pass

    def add_multiple_label_to_ap(self, device_name, count, check="False"):
        ap = self.access_points_aps_table
        self.device = getattr(devices, device_name)
        lhandle = ap.find_element_by_xpath("..//td[@title='%s']" %self.device.ip)
        log.info(self.device.ip)
        lhandle.find_element_by_xpath("//a[@ng-click='labelFn(row.serial_number, row.ap_labels, row.name)']").click()
        i = 1
        while i <= count:
            self.add_label_to_ap("LABEL%s" %i, check)
            i = i + 1
        self.access_points_close_add_label.click()

    def add_label_to_ap_with_name(self, device_name, label_name, check="False"):
        ap = self.access_points_aps_table
        self.device = getattr(devices, device_name)
        lhandle = ap.find_element_by_xpath("..//td[@title='%s']" %self.device.ip)
        lhandle.find_element_by_xpath("//a[@ng-click='labelFn(row.serial_number, row.ap_labels, row.name)']").click()
        self.add_label_to_ap(label_name, check)


    def delete_all_label_from_ap(self, device_name):
        ap = self.access_points_aps_table
        self.device = getattr(devices, device_name)
        lhandle = ap.find_element_by_xpath("..//td[@title='%s']" %self.device.ip)
        lhandle.find_element_by_xpath("//a[@ng-click='labelFn(row.serial_number, row.ap_labels, row.name)']").click()
        while len(self.access_points_check_label.find_elements_by_tag_name("a")) >= 1:
            try:
                label_disp = self.access_points_check_label
                self.browser._browser.implicitly_wait(10)
                #hov = self.browser.get_action_chain().move_to_element(label_disp.find_element_by_xpath("/html/body/div[1]/div[1]/div[6]/div/div[2]/div[2]/div/div/div[2]/div/div/display-labels/div/a[1]/span[1]"))
                try:
                    label_list = self.browser._browser.find_elements_by_xpath("//span[@ng-bind='label.name']")
                    for label in label_list:
                        hov = self.browser.get_action_chain().move_to_element(label)
                        hov.perform()
                        #elem = self.browser._browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[6]/div/div[2]/div[2]/div/div/div[2]/div/div/display-labels/div/a[1]/span[2]")
                        elem = label.find_element_by_xpath("..").find_element_by_xpath("//span[contains(@id, 'remove_label')]")
                        elem.click()
                except:
                    pass
            except Exception as err:
                log.error(err)
                time.sleep(1)
        self.access_points_close_add_label.click()

    def delete_label_from_ap(self, device_name, label_name):
        ap = self.access_points_aps_table
        self.device = getattr(devices, device_name)
        lhandle = ap.find_element_by_xpath("..//td[@title='%s']" %self.device.ip)
        lhandle.find_element_by_xpath("//a[@ng-click='labelFn(row.serial_number, row.ap_labels, row.name)']").click()
        try:
            label_disp = self.access_points_check_label
            if label_disp.find_element_by_xpath("//span[@ng-bind='label.name' and text()='%s']" %label_name):
                hov = self.browser.get_action_chain().move_to_element(label_disp.find_element_by_xpath("//span[@ng-bind='label.name' and text()='%s']" %label_name))
                hov.perform()
                self.browser._browser.implicitly_wait(10)
                elem = label_disp.find_element_by_xpath("//span[@class='icosolo icon_close']")
                elem.click()
        except Exception as err:
            log.error(err)
            pass
        try:
            ap_table_handle = lhandle.find_element_by_xpath("//tr[@ng-bind='apsTable.colIsShown('ap_labels')']")
            if not ap_table_handle.find_element_by_xpath("//span[text()='%s']" %label_name):
                self.access_points_close_add_label.click()
                return True
            else:
                self.access_points_close_add_label.click()
                return False
        except:
            self.access_points_close_add_label.click()
            return True

    def go_to_vc_page(self):
        import pdb
        #pdb.set_trace()
        vc = self.access_points_select_vc
        vc_name = vc.text
        log.info(vc_name)
        vc.click()

    def go_to_non_vc_page(self):
        slave = self.access_points_select_non_vc
        slave_name = slave.text
        log.info(slave_name)
        slave.click()
        time.sleep(5)
        self.assert_ap_page(slave_name)

    def assert_ap_page(self, ap_name):
        ap_name_str = self.access_points_verify_ap_name.text
        log.info(ap_name_str)
        if not ap_name == ap_name_str:
            raise AssertionError("Did not go into AP page i.e. Traceback: %s" %traceback.format_exc())
        else:
            return True

    def go_to_ap_page(self, ap):
        myDevice = Device.getDeviceObject(ap)
        try:
            ap_tag = self.browser._browser.find_element_by_xpath("//td[@config='apsTable' and @title='%s']//span[contains(@id,'apsTable_name_display')]" %myDevice.get("mac"))
            ap_tag.click()
            #import pdb
            #pdb.set_trace()
            self.assert_ap_page(myDevice.get("mac"))
            return MonitoringAPDetailsPage(self.test, self.browser, self.config)
        except:
            log.error("Issue while moving into AP page")

    def get_label_name_of_ap(self):
        try:
            ap_name_str = self.access_points_get_label_names_with_single_ap.text
            return ap_name_str
        except:
            ap_name_str = self.access_points_get_label_names_with_multiple_ap.text
            return ap_name_str

    def assert_verification_of_multiple_label(self, count):
        i = 1
        while i <= count:
            try:
                self.assert_verification_of_label_name("LABEL%s" %i)
            except Exception as err:
                log.error(err)
                raise AssertionError("Label Name Failed")
            i = i + 1

    def assert_verification_of_label_name(self, label_name):
        table = self.access_points_aps_table
        if not table.find_element_by_xpath("//span[contains(@title, '%s')]" %label_name):
            raise AssertionError("Label Name is not present in the AP")
        else:
            return True

    def assert_verification_of_vc_ap(self, device_name):
        self.device  = getattr(devices, device_name)
        if not self.assert_ap_page(self.device.mac):
            raise AssertionError("This device is not a VC")

    def reboot_ap(self):
        self.access_points_ap_reboot.click()
        self.access_points_ap_reboot_continue.click()

    def clear_search_values_ap(self):
        self.access_points_search_clear_values.click()

    def search_ap_with_type(self):
        self.access_points_search_ap.click()
        device_name = "IAP_1"
        self.device = getattr(devices, device_name)
        log.info(self.device.ap_type)
        self.access_points_search_ap_type.set("aa")
        self.clear_search_values_ap()
        self.access_points_search_ap_type.set(self.device.ap_type)
        self.access_points_search_submit.click()
        self.access_points_search_ap.click()
        time.sleep(5)
        for row in self.browser._browser.find_elements_by_xpath("//tr[contains(@id, 'apsTable_select_row')]"):
            if not row.find_element_by_id("apsTable_model_display_0").text == self.device.ap_type:
                raise AssertionError("Search with Type has issues %s" %traceback.format_exc())

    def search_ap_with_name(self):
        import re
        self.access_points_search_ap.click()
        device_name = "IAP_1"
        self.device = getattr(devices, device_name)
        self.access_points_search_ap_type.set("aa")
        self.clear_search_values_ap()
        self.access_points_search_ap_name.set(re.search("\w+:\w+:\w+:(\w+:\w+:\w+)", self.device.mac).group(1))
        self.access_points_search_submit.click()
        self.access_points_search_ap.click()
        time.sleep(5)
        import pdb
        #pdb.set_trace()
        for row in self.browser._browser.find_elements_by_xpath("//tr[contains(@id, 'apsTable_select_row')]"):
            if not str(row.find_element_by_id("apsTable_name_display_0").text).lower() == self.device.mac:
                raise AssertionError("Search with Name has issues %s" % traceback.format_exc())

    def search_ap_with_vc(self):
        import re
        self.access_points_search_ap.click()
        device_name = "IAP_1"
        self.device = getattr(devices, device_name)
        self.access_points_search_ap_type.set("aa")
        self.clear_search_values_ap()
        self.access_points_search_ap_vc.set(re.search("\w+:\w+:\w+:(\w+:\w+:\w+)", self.device.mac).group(1))
        self.access_points_search_submit.click()
        self.access_points_search_ap.click()
        time.sleep(5)
        for row in self.browser._browser.find_elements_by_xpath("//tr[contains(@id, 'apsTable_select_row')]"):
            if not re.search("\w+:\w+:\w+:(\w+:\w+:\w+)", self.device.mac).group(1).upper() in row.find_element_by_id("apsTable_vc_name_display_0").text:
                raise AssertionError("Search with Type has issues %s" % traceback.format_exc())

    def search_ap_with_status(self):
        self.access_points_search_ap.click()
        self.access_points_search_ap_type.set("aa")
        self.clear_search_values_ap()
        self.access_points_search_ap_status.set("Up")
        self.access_points_search_submit.click()
        self.access_points_search_ap.click()
        time.sleep(5)
        for row in self.browser._browser.find_elements_by_xpath("//tr[contains(@id, 'apsTable_select_row')]"):
            if not row.find_element_by_xpath("//span[contains(@id, 'apsTable_status_display')]").text == "Up":
                raise AssertionError("Search with Type has issues %s" % traceback.format_exc())

    def search_ap_with_location(self):
        self.access_points_search_ap.click()
        self.access_points_search_ap_type.set("aa")
        self.clear_search_values_ap()
        self.access_points_search_ap_location.set("India")
        self.access_points_search_submit.click()
        self.access_points_search_ap.click()
        time.sleep(5)

        for row in self.browser._browser.find_elements_by_xpath("//span[contains(@id, 'apsTable_loc_detail_display')]"):
            if not "India" in row.text:
                raise AssertionError("Search with Type has issues %s" % traceback.format_exc())

    def display_elem_in_ap(self, elem_name):
        self.access_points_display_option.click()
        if not getattr(self, "access_points_display_%s" %elem_name).is_selected():
            action_chain = self.browser.get_action_chain()
            action_chain.move_to_element(getattr(self, "access_points_display_%s" %elem_name)).click().perform()

    def get_ap_location(self):
        map = self.map_tag
        false = "false"
        true = "true"
        try:
            location = eval(map.get_attribute("location-markers"))
        except:
            log.error("Something wrong with the map object")
            location = []
        return location

    def check_ap_in_map(self, device_name):
        self.device = getattr(devices, device_name)
        location = self.get_ap_location()
        if location != []:
            if self.device.location == location[0]['street_address']['city']:
                return True
            else:
                raise AssertionError("ISSUE WITH LOCATION")
        else:
            raise AssertionError("AP is not present in the MAP")
    
    def get_access_point(self,index = 1):#index 1 represents the first ap
        ap_name = self.browser._browser.find_element_by_xpath("//table[@id='monitoring-accessPoints-apsTable']/tbody[1]/tr['%s']/td[1]/span[2]" %index)
        return ap_name.text
        
    def goto_ap_details_page(self,index = 1):#index 1 represents the first ap
        self.browser._browser.find_element_by_xpath("//table[@id='monitoring-accessPoints-apsTable']/tbody[1]/tr['%s']/td[1]/span[2]" %index).click()
        return MonitoringAPDetailsPage(self.test, self.browser, self.config)
        
    def go_to_ap_details_page(self,index = 1):#index 1 represents the first ap
        self.browser._browser.find_element_by_xpath("//table[@id='monitoring-accessPoints-apsTable']/tbody[1]/tr['%s']/td[1]/span[2]" %index).click()


    def expand_map(self):
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.access_points_map_overlay).click().perform()
        if not self.access_points_map_close:
            raise AssertionError("Map was not Expanded")
        else:
            self.access_points_map_close.click()

    def map_zoom(self, action):
        if action == "zoom-in":
            self.access_points_zoom_in.click()
        elif action == "zoom-out":
            self.access_points_zoom_out.click()

    def verify_flagged_ap_table(self, ap):
        from Device_Module.ObjectModule import Device
        myDevice = Device.getDeviceObject(ap)
        table = self.access_points_flagged_ap_table
        entries = table.find_elemens_by_id("flaggedAPsTable_name_display_0")
        if not myDevice.get("mac") in entries:
            raise AssertionError("AP IS NOT IN FLAGGED AP TABLE")

    def set_default_device(self, device):
        import os
        os.environ['device'] = device