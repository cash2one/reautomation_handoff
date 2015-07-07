__author__ = 'rrkrishnan'
from athenataf.lib.util.WebPage import WebPage
from athenataf.config import devices
from Device_Module.ObjectModule import Device
import os
import traceback
import logging
log = logging.getLogger('athenataf')
import time
import re

class MonitoringClientPage(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "Monitoring", test, browser, config)
        self.test.assertPageLoaded(self)

    def isPageLoaded(self):
        if self.client_label:
            return True
        else:
            return False

    def select_timeline(self, timeline):
        if timeline == '1H':
            if not self._timeline_1H:
                raise AssertionError("1 YEAR LINK IS NOT WORKING")
            self._timeline_1H.click()
        elif timeline == '3H':
            if not self._timeline_3H:
                raise AssertionError("1 YEAR LINK IS NOT WORKING")
            self._timeline_3H.click()
        elif timeline == '1D':
            if not self._timeline_1D:
                raise AssertionError("1 YEAR LINK IS NOT WORKING")
            self._timeline_1D.click()
        elif timeline == '1W':
            if not self._timeline_1W:
                raise AssertionError("1 YEAR LINK IS NOT WORKING")
            self._timeline_1W.click()
        elif timeline == '1Y':
            try:
                if not self._timeline_1Y:
                    raise AssertionError("1 YEAR LINK IS NOT WORKING")
                self._timeline_1Y.click()
            except:
                pass


    def graph_stream(self, direction):
        self.client_details_throughput_graph.click()
        if direction.lower() == "inbound":
            self.client_details_inbound_graph.click()
        else:
            try:
                self.client_details_outbound_graph.click()
            except:
                pass

    def graph_stream_overview_page(self, direction):
        self.clients_page_throughput_graph.click()
        if direction.lower() == "upstream":
            self._upstream_graph.click()
        else:
            try:
                self._downstream_graph.click()
            except:
                pass

    def assert_client_type(self, client):
        myDevice = Device.getDeviceObject(client)
        if not self.client_device_type == myDevice.get("os"):
            #raise AssertionError("Client Type does not match")
            log.error("Clent Type Does Not Match")

    def go_to_client_details_page(self, client):
        import pdb
        #pdb.set_trace()
        myDevice = Device.getDeviceObject(client)
        table = self.client_monitoring_table
        entries = table.find_elements_by_xpath("//span[contains(@id,'clientsTable_macaddr_display_')]")
        for entry in entries:
            if entry.text == myDevice.get("mac"):
                entry.click()
        time.sleep(5)
        for i in range(1, 5):
            try:
                log.info("Checking Client Label in Clients Detail Page : %s" %self.client_details_page_label.text)
                if self.client_details_page_label.text == myDevice.get("mac"):
                    break
                else:
                    time.sleep(5)
                    self.browser.refresh()
            except:
                time.sleep(5)
                self.browser.refresh()
        if not self.client_details_page_label.text == myDevice.get("mac"):
            raise AssertionError("NOT IN THE EXPECTED CLIENT PAGE")

    def get_client_location(self):
        map = self.map_tag
        false = "false"
        true = "true"
        try:
            location = eval(map.get_attribute("location-markers"))
        except:
            log.error("Something wrong with the map object")
            location = []
        return location
    
    def get_client_ip(self):
        return self.clients_ip_address.text

    def check_client_in_map(self, device_name):
        self.device = getattr(devices, device_name)
        location = self.get_client_location()
        if location != []:
            if self.device.location == location[0]['street_address']['city']:
                return True
            else:
                raise AssertionError("ISSUE WITH LOCATION")
        else:
            raise AssertionError("AP is not present in the MAP")


    def expand_map(self):
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.client_map_overlay).click().perform()
        if not self.client_map_close:
            raise AssertionError("Map was not Expanded")
        else:
            self.client_map_close.click()

    def map_zoom(self, action):
        if action == "zoom-in":
            self.client_map_zoom_in.click()
        elif action == "zoom-out":
            self.client_map_zoom_in.click()

        
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
            ele_object = eval("self.clients_%s" %element)
            action_chain.move_to_element(ele_object).perform()
            time.sleep(2)
            if re.search('\S+',self.help_content.text):
                log.info("PASS: Help text for \"%s\" is existing." %element)
            else:
                log.info("FAIL: Help text for \"%s\" is not existing/Empty." %element)
                raise AssertionError("Help content is not opened/Empty i.e. Traceback: %s" %traceback.format_exc())
            self.help_content.click()
            time.sleep(3)


    def assert_help_options_client_details(self,elements):
        '''
        asserts help text
        '''

        for element in elements:
            action_chain = self.browser.get_action_chain()
            ele_object = eval("self.client_details_%s" %element)
            action_chain.move_to_element(ele_object).perform()
            if re.search('\S+',self.help_content.text):
                log.info("PASS: Help text for \"%s\" is existing." %element)
            else:
                log.info("FAIL: Help text for \"%s\" is not existing/Empty." %element)
                raise AssertionError("Help content is not opened/Empty i.e. Traceback: %s" %traceback.format_exc())
            self.help_content.click()
            time.sleep(3)