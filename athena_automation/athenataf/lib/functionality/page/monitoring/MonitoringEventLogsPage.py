__author__ = 'rrkrishnan'
from athenataf.lib.util.WebPage import WebPage
from athenataf.lib.functionality.page.monitoring.MonitoringAPDetailsPage import MonitoringAPDetailsPage
from athenataf.config import devices
from Device_Module.ObjectModule import Device
import os
import traceback
import logging
log = logging.getLogger('athenataf')
import time
import re


class MonitoringEventLogsPage(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "Monitoring", test, browser, config)
        self.test.assertPageLoaded(self)

    def isPageLoaded(self):
        if self.event_log_label:
            return True
        else:
            return False

    def scroll_to_last_event_log(self):
        if not self.browser._browser.find_elements_by_xpath("//tr[contains(@id, 'EVENT_LOG_TABLE_select_row')]")[-1]:
            raise

    def display_mac_addr(self):
        self.event_log_display_dropDown.click()
        if not self.event_log_display_select_mac.is_selected():
            self.event_log_display_select_mac.click()

    def assert_ap_event_log(self, ap_list):
        if not isinstance(ap_list, list):
            ap_list = ap_list.split(" ")
        ap_mac_list = []
        for ap in ap_list:
            ap_mac_list.append(Device.getDeviceObject(ap).get("mac"))
        table = self.event_log_table
        mac_list = table.find_elements_by_xpath("//span[contains(@id, 'EVENT_LOG_TABLE_mac_addr_display')]")
        for mac in mac_list:
            log.info(mac.text)
            if mac.text not in ap_mac_list and mac.text != "":
                raise AssertionError("Mac address that are not part of AP List is present")
            #elif mac.text != '':
            #    raise AssertionError("Mac address that are not part of AP List is present")


    def assert_swarm_event_log(self, swarm):
        table = self.event_log_table
        swarm_list = table.find_elements_by_xpath("//span[contains(@id, 'EVENT_LOG_TABLE_hostname_display')]")
        for _swarm in swarm_list:
            if not _swarm.text == swarm and _swarm.text != "":
                raise AssertionError("Swarm other than expected is present")
                
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



    def assert_help_options(self,elements):
        '''
        asserts help text
        '''

        for element in elements:
            action_chain = self.browser.get_action_chain()
            ele_object = eval("self.monitoring_event_log_%s" %element)
            action_chain.move_to_element(ele_object).perform()
            time.sleep(2)
            if re.search('\S+',self.help_content.text):
                log.info("PASS: Help text for \"%s\" is existing." %element)
            else:
                log.info("FAIL: Help text for \"%s\" is not existing/Empty." %element)
                raise AssertionError("Help content is not opened/Empty i.e. Traceback: %s" %traceback.format_exc())
            self.help_content.click()
            time.sleep(3)
