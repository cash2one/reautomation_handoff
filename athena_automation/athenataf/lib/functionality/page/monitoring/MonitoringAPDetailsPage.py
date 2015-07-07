__author__ = 'aarunakirisamy'
from athenataf.lib.util.WebPage import WebPage
#from athenataf.lib.functionality.page.common.LeftPanel import LeftPanel
#import athenataf.lib.functionality.page.common.LeftPanel
import traceback
import logging
log = logging.getLogger('athenataf')
from Device_Module.ObjectModule import Device
import time
import re

class MonitoringAPDetailsPage(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "Monitoring", test, browser, config)
        self.test.assertPageLoaded(self)

    def isPageLoaded(self):
        if self.ap_details_page:
            return True
        else:
            return False

    def verify_ap_details_page(self, expected_ap_name):
        '''
        verify AP DETAILS page
        '''
        log.info("Expected: It should take us to the corresponding AP DETAILS page")
        time.sleep(10)
        if self.ap_details_page:
            log.info("PASS: Successfully it took us to the AP DETAILS page")
            existing_ap_name = self.ap_details_ap_name.text
            if expected_ap_name == existing_ap_name:
                log.info("PASS: Successfully it took us to the corresponding AP DETAILS page")
            else:
                log.info("FAIL: it didn't take us to the corresponding AP DETAILS page.\nExisting AP: %s,\tExpected AP: %s" %(existing_ap_name,expected_ap_name))
                raise AssertionError("Traceback: %s " %traceback.format_exc())
        else:
            log.info("FAIL: it didn't take us to the AP DETAILS page")
            raise AssertionError("Traceback: %s " %traceback.format_exc())
            
    def verify_wired_interface_table(self):
        '''
        verify wired interface table in AP DETAILS Page
        '''
        expected_fields_list = ["WIRED INTERFACE","MAC ADDRESS","IP ADDRESS","STATUS","LINK TYPE","DUPLEX MODE"]
        log.info("Expected: Wired interface table should have the following fields: %s" %expected_fields_list)
        table = self.ap_details_wired_interface_table
        existing_fields_list = []
        all_fields_existing = True
        for field in table.find_elements_by_tag_name("th"):
            existing_fields_list.append(field.text)            
        
        for expected_field in expected_fields_list:
            if expected_field in existing_fields_list:
                log.info("PASS: Field \"%s\" is existing in wired interface table" %expected_field)
            else:
                log.info("FAIL: Field \"%s\" is not existing in wired interface table" %expected_field)
                all_fields_existing = False
                
        if not all_fields_existing:
            raise AssertionError("Expected fields missing in wired interface table.")
            
    def verify_wireless_interface_table(self):
        '''
        verify wireless interface table in AP DETAILS Page
        '''
        expected_fields_list = ["MAC ADDRESS","RADIO TYPE","STATUS","CLIENTS","SSIDS","CHANNEL","TX POWER","ANTENNA TYPE","ROLE"]
        log.info("Expected: Wireless interface table should have the following fields: %s" %expected_fields_list)
        table = self.ap_details_wireless_interface_table
        existing_fields_list = []
        all_fields_existing = True
        for field in table.find_elements_by_tag_name("th"):
            existing_fields_list.append(field.text)            
        
        for expected_field in expected_fields_list:
            if expected_field in existing_fields_list:
                log.info("PASS: Field \"%s\" is existing in wireless interface table" %expected_field)
            else:
                log.info("FAIL: Field \"%s\" is not existing in wireless interface table" %expected_field)
                all_fields_existing = False
                
        if not all_fields_existing:
            raise AssertionError("Expected fields missing in wireless interface table.")
            
    def get_ssids_count_from_ap_details_wireless_interface_table(self, ssid_index=5):
        '''
        return the number of ssids from wireless interface table in AP DETAILS Page
        '''


        table = self.ap_details_wireless_interface_table
        existing_fields_list = [" "]
        for field in table.find_elements_by_tag_name("th"):
            existing_fields_list.append(field.text)

        if existing_fields_list[ssid_index] == "SSIDS":
            count = table.find_element_by_xpath("//table[@id='monitoring-apDetails-wirelessIntTable']/tbody/tr[1]/td[%d]/span[2]" %ssid_index).text
        else:
            raise AssertionError("SSIDS is not at expected index - %d in wireless interface table." %ssid_index)      
            
        return int(count)


    def verify_clients_table(self, client):
        myDevice = Device.getDeviceObject(client)
        #import pdb
        #pdb.set_trace()
        table = self.access_points_detail_client_table
        ip = myDevice.get("ip")
        mac = myDevice.get("mac")
        if myDevice.get("os") == "Win8":
            #os = "Windows"
            os = "Unknown"
        else:
            os = "Windows"
        mac_list = table.find_elements_by_xpath("//span[contains(@id, 'clientsInterfaceTable_macaddr_display')]")
        #ip_list = table.find_elements_by_xpath("//span[contains(@id, 'clientsInterfaceTable_ipaddress_display')]")
        #log.info(ip_list)
        i = 0
        try:
            #for ip_obj in ip_list:
            for mac_obj in mac_list:
                #if ip_obj.text == ip:
                if mac_obj.text == mac:
                    index = i
                    break
                i = i + 1
            log.info("#" * 100)
            log.info(index)
        except:
            raise AssertionError("The client requested is not in the table")
        if not table.find_elements_by_xpath("//span[contains(@id, 'clientsInterfaceTable_username_display')]")[index].text == "Admin":
            raise AssertionError("Client Name doesnt match")
        if not table.find_elements_by_xpath("//span[contains(@id, 'clientsInterfaceTable_ipaddress_display')]")[index].text == ip:
        #if not table.find_elements_by_xpath("//span[contains(@id, 'clientsInterfaceTable_macaddr_display')]")[index].text == mac:
            raise AssertionError("Client IP doesnt match")
        if not table.find_elements_by_xpath("//span[contains(@id, 'clientsInterfaceTable_devicetype_display')]")[index].text == os:
            raise AssertionError("Client OS doesnt match")
        if not table.find_elements_by_xpath("//span[contains(@id, 'clientsInterfaceTable_ssid_display')]")[index].text == "TEST_Monitoring":
            raise AssertionError("Client NETWORK doesnt match")
        if not table.find_elements_by_xpath("//span[contains(@id, 'clientsInterfaceTable_channel_display')]")[index].text:
            raise AssertionError("Client CHANNEL doesnt match")
        if not table.find_elements_by_xpath("//span[contains(@id, 'clientsInterfaceTable_connection_display')]")[index].text == "802.11AN":
            raise AssertionError("Client TYPE doesnt match")
        if not table.find_elements_by_xpath("//span[contains(@id, 'clientsInterfaceTable_role_display')]")[index].text == "TEST_Monitoring":
            raise AssertionError("Client ROLE doesnt match")


    def assert_latest_alert(self, ap, action):
        myDevice = Device.getDeviceObject(ap)
        mac = myDevice.get("mac")
        for i in range(0, 5):
            #table = self.access_points_alert_table
            #alert = table.find_element_by_id("alertsTable_select_row_0").text
            alert = self.first_alert.text
            if alert == "Access point %s is %s" % (mac, action):
                break
            time.sleep(50)
            #self.browser.refresh()
        if not alert == "Access point %s is %s" %(mac, action):
            log.error("Expected alert is not seen : %s" %alert)
            raise AssertionError("Expected alert is not seen")

    def assert_empty_event_log(self):
        table = self.access_points_detail_event_log_table
        if not len(table.find_elements_by_xpath("//tr[contains(@id, 'eventLogTable_select_row')]")) > 0:
            raise AssertionError("EVENT LOG IS EMPTY")

    def assert_tooltip_event_log(self):
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.access_points_detail_event_log_help).perform()
        if not self.help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" % traceback.format_exc())
            time.sleep(5)

    def assert_client_present_in_ap(self, client):
        myDevice = Device.getDeviceObject(client)

        table = self.access_points_details_client_table
        ip = myDevice.get("ip")
        ip_list = table.find_elements_by_xpath("//span[contains(@id, 'clientsInterfaceTable_ipaddress_display')]")
        try:
            index = ip_list.index(ip)
        except:
            raise AssertionError("The client requested is not in the table")

    def get_tx_power_from_wireless_interface_table(self, tx_power_index=7):
        '''
        return the tx power from wireless interface table in AP DETAILS Page
        '''
        table = self.ap_details_wireless_interface_table
        existing_fields_list = [" "]
        for field in table.find_elements_by_tag_name("th"):
            existing_fields_list.append(field.text)
        if existing_fields_list[tx_power_index] == "TX POWER":
            tx_power = table.find_element_by_xpath("//table[@id='monitoring-apDetails-wirelessIntTable']/tbody/tr[1]/td[%d]/span[2]" %tx_power_index).text
        else:
            raise AssertionError("TX Power is not at expected index - %d in wireless interface table." %tx_power_index)
        return int(tx_power)
        
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
            ele_object = eval("self.ap_details_%s" %element)
            action_chain.move_to_element(ele_object).perform()
            if re.search('\S+',self.help_content.text):
                log.info("PASS: Help text for \"%s\" is existing." %element)
            else:
                log.info("FAIL: Help text for \"%s\" is not existing/Empty." %element)
                raise AssertionError("Help content is not opened/Empty i.e. Traceback: %s" %traceback.format_exc())
            self.help_content.click()
            time.sleep(3)
    def get_ap_location(self):
        map = self.map_tag
        try:
            location = eval(map.get_attribute("location-markers"))
        except:
            log.error("Something wrong with the map object")
            location = []
        return location

    def assert_edit_location_changed(self):
        log.info("Clicking on map")
        self.ap_details_page_map.click()
        location = self.get_ap_location()
        self.ap_details_page_map_edit_loc.click()
        time.sleep(2)

        current_city = location[0]["street_address"]["city"]
        if current_city == "Chennai":
            current_city = "Bengaluru"
            state = "Karnataka"
        else:
            current_city = "Chennai"
            state = "Tamil Nadu"
        self.ap_details_edit_map_address.clear()
        self.ap_details_edit_loc_city.clear()
        self.ap_details_edit_loc_city.send_keys(current_city)
        self.ap_details_edit_ap_map_state.clear()
        self.ap_details_edit_ap_map_state.send_keys(state)
        self.ap_details_edit_zip.clear()
        self.ap_details_edit_loc_save.click()

        log.info("Assert if location changed")
        self.ap_details_page_map.click()
        log.info("Retrieve changed city information")
        changed_loc =  self.get_ap_location()
        changed_city = changed_loc[0]["street_address"]["city"]
        if current_city == changed_city:
            raise AssertionError("Change of location not successful from %s, to the new city %s" %current_city %changed_city)
        time.sleep(2)