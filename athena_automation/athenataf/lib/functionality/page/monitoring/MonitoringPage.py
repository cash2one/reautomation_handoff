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

class MonitoringPage(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "Monitoring", test, browser, config)
        self.test.assertPageLoaded(self)

    def isPageLoaded(self):
        if self.overview_label:
            return True
        else:
            return False

    def access_points(self):
        self.access_point.click()

    def wlan_table_enable_check(self, nw='test1'):
        self.browser.refresh()
        try:
            wlan_ssid_list = self.browser._browser.find_elements_by_xpath("//span[contains(@id, 'overview_wlans_ssid_display')]")
            for ssid in wlan_ssid_list:
                if ssid.text == nw:
                    return True
        except:
            log.error("Wlan Table Not Enabled")
            return False
        return False

    def assert_network_in_ap(self, ap, nw):
        myDevice = Device.getDeviceObject(ap)
        myDevice.receive("#")
        myDevice.transmit("show network")
        output = myDevice.receive("#")
        log.info(output)
        if not nw in output:
            raise AssertionError("%s is not present in the network" %nw)

    def assert_network_not_in_ap(self, ap, nw):
        myDevice = Device.getDeviceObject(ap)
        for i in range(0, 10):
            myDevice.receive("#")
            myDevice.transmit("show network")
            output = myDevice.receive("#")
            log.info(output)
            if not nw in output:
                break
            time.sleep(5)
        if nw in output:
            raise AssertionError("Network still exists in the configuration")

    def wlan_table_disable_check(self):
        self.browser.refresh()
        table = self.wlan_table
        try:
            for td in table.find_elements_by_tag_name("td"):
                if td.text == "test1":
                    return False
        except:
            pass
        return True


    def verify_tool_tip(self):
        toolTip = self.toolTip
        if "test1" in toolTip.text:
            log.info("ToolTip exists")
            return True
        else:
            log.error("ToolTip Does not exist")
            return False


    def check_ap_count(self):
        return self.nav_all_ap.text

    def go_to_all_ap(self):
        self.nav_all_ap.click()
        time.sleep(2)
        ap_page = self.verify_ap_page
        if ap_page:
            return True
        else:
            return False

    def go_to_up_ap(self):
        self.up_ap.click()
        time.sleep(2)
        ap_page = self.verify_ap_page
        if ap_page:
            return True
        else:
            return False

    def go_to_down_ap(self):
        self.down_ap.click()
        time.sleep(2)
        ap_page = self.verify_ap_page
        if ap_page:
            return True
        else:
            return False

    def check_monitoring_page_ap_down_count(self):
        return self.down_ap.text


    def go_to_wifi_clients(self):
        self.wifi_client.click()
        time.sleep(2)
        client_page = self.verify_client_page
        log.info(client_page)
        if client_page:
            return True
        else:
            return False


    def go_to_wired_clients(self):
        self.wired_client.click()
        time.sleep(2)
        client_page = self.verify_client_page
        if client_page:
            return True
        else:
            return False

    def wait_for(self, retries, diff, func):
        i = 0
        func_call = getattr(self, func)
        while i < retries:
            if func_call():
                log.info("Values exist in WLAN Table")
                return True
                break
            else:
                log.error("WLAN TABLE IS NOT ENABLED")
                time.sleep(diff)
                i = i + 1
        return False

    def get_ap_location(self):
        map = self.map_tag
        false="false"
        true="true"
        try:
            location = eval(map.get_attribute("location-markers"))
        except:
            log.error("Something wrong with the map object")
            location = []
        return location

    def check_no_ap_in_map(self):
        location = self.get_ap_location()
        if location == []:
            return True
        else:
            raise AssertionError("AP is present in the MAP")

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

    def go_to_all_groups_page(self):
        try:
            self.all_groups_tag.click()
            time.sleep(2)
        except:
            pass

    def create_new_network_quicklink(self, single_group=False):
        self.create_new_network_quicklink_tag.click()

        if not single_group:
            log.info("Expected result: It should take us to the groups under wireless configuration")

            if self.verify_all_groups_network:
                log.info("PASS: Successfully it took us to the groups under wireless configuration")
            else:
                import traceback
                log.info("FAIL: it didn't take us to the groups under wireless configuration")
                raise AssertionError("Traceback: %s " %traceback.format_exc())

        else:
            log.info("Expected result: It should take us to create new network page ")

            if self.create_network_page:
                log.info("PASS: Successfully it took us to create new network page")
            else:
                import traceback
                log.info("FAIL: it didn't take us to create new network page")
                raise AssertionError("Traceback: %s " %traceback.format_exc())

    def create_report_quicklink(self):
        self.create_report_quicklink_tag.click()
        log.info("Expected result: It should take us to Reports -> network summary report page")
        if self.verify_report:
            log.info("PASS: Successfully it took us to Reports -> network summary report page")
        else:
            import traceback
            log.info("FAIL: it didn't take us to Reports -> network summary report page")
            raise AssertionError("Traceback: %s " %traceback.format_exc())

    def manage_groups_quicklink(self):
        self.manage_groups_quicklink_tag.click()
        log.info("Expected result: It should open the manage groups page")

        if self.verify_manage_groups_quicklink:
            log.info("PASS: Successfully it opened the manage groups page")
            self.close_manage_groups.click()

        else:
            import traceback
            log.info("FAIL: it didn't open the manage groups page")
            raise AssertionError("Traceback: %s " %traceback.format_exc())

    def update_device_firmware_quicklink(self):
        self.update_device_firmware_quicklink_tag.click()
        log.info("Expected result: It should take us to Firmware page")

        if self.verify_update_device_firmware_quicklink:
            log.info("PASS: Successfully it took us to Firmware page")
        else:
            import traceback
            log.info("FAIL: it didn't take us to Firmware page")
            raise AssertionError("Traceback: %s " %traceback.format_exc())

    def set_security_quicklink(self, single_group=False):
        self.set_security_quicklink_tag.click()

        if not single_group:
            log.info("Expected result: It should take us to the groups under wireless configuration")
            if self.verify_all_groups_network:
                log.info("PASS: Successfully it took us to the groups under wireless configuration")
            else:
                import traceback
                log.info("FAIL: it didn't take us to the groups under wireless configuration")
                raise AssertionError("Traceback: %s " %traceback.format_exc())
        else:
            log.info("Expected result: It should take us to the configuration ->Security page")
            if self.configuration_security_page:
                log.info("PASS: Successfully it took us to the configuration ->Security page")
            else:
                import traceback
                log.info("FAIL: it didn't take us to the configuration ->Security page")
                raise AssertionError("Traceback: %s " %traceback.format_exc())

    def manage_devices_quicklink(self, single_group=False):
        self.manage_devices_quicklink_tag.click()

        if not single_group:
            log.info("Expected result: It should take us to the device management page")

            if self.verify_manage_devices_quicklink:
                log.info("PASS: Successfully it took us to the device management page")
            else:
                import traceback
                log.info("FAIL: it didn't take us to the device management page")
                raise AssertionError("Traceback: %s " %traceback.format_exc())
        else:
            log.info("Expected result: It should throw an alert \"manage device option available on all group level\"")

            if self.group_manage_devices_alert:
                log.info("PASS: Successfully it threw an alert \"manage device option available on all group level\"")
                self.group_manage_devices_alert_confirm.click()
            else:
                import traceback
                log.info("FAIL: it didn't throw an alert \"manage device option available on all group level\"")
                raise AssertionError("Traceback: %s " %traceback.format_exc())

    def go_to_default_group(self):
        self.select_group_icon.click()
        self.select_default_group.click()
        if not self.default_group_label:
            raise AssertionError("Unable to navigate to the default group page : %s" % traceback.format_exc())

    def go_to_group_page(self, group):
        self.select_group_icon.click()
        group_obj = self.browser._browser.find_element_by_xpath("//span[contains(@id,'group_name')]//span[text()='%s']" %group)
        group_obj.click()
        if not self.browser._browser.find_element_by_xpath("//label[text()='%s']" %group):
            raise AssertionError("Unable to navigate to the group page : %s" %traceback.format_exc())

    def go_to_swarm_in_group(self, group):
        self.select_group_icon.click()
        group_obj_list = self.browser._browser.find_elements_by_xpath("//span[contains(@id,'group_name')]//span")
        for group_obj in group_obj_list:
            try:
                if group_obj.text == group:
                    ind = group_obj_list.index(group_obj)
                    break
            except:
                pass
        ind = ind / 2
        self.browser._browser.find_element_by_xpath("//a[contains(@id,'group_list')]//span[@id='show_swarms_%s']" % ind).click()
        swarm_name = self.browser._browser.find_element_by_xpath("//span[@id='swarm_name_0']").text
        self.browser._browser.find_element_by_xpath("//span[@id='swarm_name_0']").click()
        return swarm_name

    def delete_group(self, groupName):
        log.debug("ManageGroupPage: Clicking on 'samplegroup' group ")
        self.browser._browser.find_element_by_xpath("//span[@id='group_sidebar_group_name_spn' and text()=%s]").click()
        # self.sample_group.click()
        time.sleep(5)
        log.debug("ManageGroupPage: Clicking on 'Delete' button ")
        self.delete.click()
        time.sleep(6)

    def create_new_group(self, group, pwd):
        from selenium.common.exceptions import NoSuchElementException
        self.select_group_icon.click()
        try:
            self.manage_group.click()
            self.delete_group(group)
        except:
            pass
        self.add_new_group.click()
        self.new_group_text_box.send_keys(group)
        self.new_group_next_button.click()
        self.new_group_password.send_keys(pwd)
        self.new_group_password_confirm.send_keys(pwd)
        try:
            self.new_group_save_button.click()
        except:
            pass
        #if self.browser._browser.find_element_by_xpath("//div[@id='warnigBox_common_Alert']"):
        #if self.group_manage_devices_alert:
        try:
            self.group_manage_devices_alert_confirm.click()
            log.info("Received Alert : %s" % self.group_manage_devices_alert.text)
        except:
            log.info("Alert Element is not seen")
        try:
            self.manage_group_close.click()
        except:
            pass


   # def move_all_ap_to_group(self):
    #    self.select_group_icon.click()


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

    def assert_help_option_for_access_points(self):
        '''
        asserts help text
        '''
        time.sleep(3)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.overview_access).perform()
        if not re.search('\S+',self.help_content.text):
            raise AssertionError("Help content is not opened/Empty i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(1)

    def assert_help_option_for_clients(self):
        '''
        asserts help text
        '''
        time.sleep(3)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.overview_clients).perform()
        if not re.search('\S+',self.help_content.text):
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(5)

    def assert_help_option_for_alerts(self):
        '''
        asserts help text
        '''
        time.sleep(3)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.overview_alerts).perform()
        if not re.search('\S+',self.help_content.text):
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(5)

    def assert_help_option_for_access_throughput(self):
        '''
        asserts help text
        '''
        time.sleep(3)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.overview_throughput).perform()
        if not re.search('\S+',self.help_content.text):
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(5)

    def assert_help_option_for_clients_type(self):
        '''
        asserts help text
        '''
        time.sleep(3)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.overview_clients_type).perform()
        if not re.search('\S+',self.help_content.text):
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(5)

    def get_number_of_input_devices(self, device_type="all"):
        from inspect import isclass
        device_list = [x for x in dir(devices) if isclass(getattr(devices, x))]
        dev = {}
        dev["iap"] = []
        dev["client"] = []
        dev["switch"] = []
        for devic in device_list:
            type = getattr(getattr(devices, devic), "type")
            if type.lower() == "client":
                dev["client"].append(devic)
            elif type.lower() == "iap":
                dev["iap"].append(devic)
            elif type.lower() == "switch":
                dev["switch"].append(devic)
        if device_type == "all":
            return len(dev["iap"]) + len(dev["client"]) + len(dev["switch"])
        else:
            return len(dev[device_type])

    def assert_ap_count_in_overview_page(self, value):
        for i in range(0, 10):
            try:
                if int(self.check_ap_count()) == int(value):
                    break
            except:
                time.sleep(10)
                self.browser.refresh()
                pass
        if not int(self.check_ap_count()) == int(value):
            raise AssertionError("Number of IAP in overview page %s does not match with Expected %s" %(self.check_ap_count(), value))

    def verify_global_search(self, input, field, expected_result):
        '''
        verify the expected result is part of the result from Global search
        '''
        self.global_search_input.clear()
        self.global_search_input.send_keys("%s\r" %input)
        result_table_fields = ["AP", "SWITCHES", "CLIENTS", "EVENTS", "NETWORKS", "LABELS"]
        field_index = result_table_fields.index(field) + 1
        time.sleep(5)
        existing_result = self.browser._browser.find_element_by_xpath("//table[@cellpadding='']/tbody/tr[%d]/td[2]" %field_index).text
        if re.search(expected_result,existing_result):
            log.info("PASS: For Input string \"%s\", Expected string \"%s\" is matching with Global search result in %s ." %(input, expected_result, field))
        else:
            log.info("FAIL: For Input string \"%s\", Expected string \"%s\" is not matching with Global search result in %s ." %(input, expected_result, field))
            raise AssertionError("Global search result is not matching with expected.")

    def set_default_device(self, device):
        os.environ['device'] = device

    def connect_device_to_server(self, device):
        myDevice = Device.getDeviceObject(device)
        try:
            myDevice.connect_device_to_server()
        except:
            myDevice.disconnect()
            time.sleep(100)
            myDevice.connect()
            myDevice.connect_device_to_server()
        i = 1
        while i < 10:
            if myDevice.get_device_status():
                break
            else:
                time.sleep(10)
            i = i+1
        if not myDevice.get_device_status():
            raise AssertionError("Device is not attached to Athena Yet")

    def disconnect_device_from_server(self, device):

        myDevice = Device.getDeviceObject(device)
        try:
            myDevice.connect_device_to_server("1.1.1.1")
        except:
            myDevice.disconnect()
            time.sleep(100)
            myDevice.connect()
            myDevice.connect_device_to_server("1.1.1.1")
        time.sleep(10)
        i = 1
        while i < 10:
            if not myDevice.get_device_status():
                break
            else:
                time.sleep(5)
            i = i + 1
        if myDevice.get_device_status():
            raise AssertionError("Device is attached to Athena Yet")

    def assert_up_ap_count_in_overview_page(self, value):
        i = 1
        while i < 10:
            if int(self.up_ap.text) == value:
                break
            else:
                self.browser.refresh()
                time.sleep(18)
            i = i + 1
        if not int(self.up_ap.text) == value:
            raise AssertionError("Number of IAP in overview page does not match with given number of IAPs")

    def assert_down_ap_count_in_overview_page(self, value):
        i = 1
        while i < 10:
            if int(self.down_ap.text) == value:
                break
            else:
                self.browser.refresh()
                time.sleep(18)
            i = i + 1
        if not  int(self.down_ap.text) == value:
            raise AssertionError("Number of IAP in overview page does not match")

    def disconnect_client_from_ap(self, device):
        myDevice = Device.getDeviceObject(device)
        try:
            myDevice.disconnect_client_from_ap()
        except:
            myDevice.connect()
            myDevice.disconnect_client_from_ap()

    def connect_client_to_ap(self, device, SSID=None):
        myDevice = Device.getDeviceObject(device)
        try:

            myDevice.connect_client_to_ap(SSID=SSID)
        except:
            myDevice.connect()
            myDevice.connect_client_to_ap(SSID=SSID)

    def assert_wifi_client_count(self, value):
        i = 0
        while i < 10:
            if int(self.wifi_client.text) == value:
                break
            else:
                self.browser.refresh()
                time.sleep(150)
            i = i + 1
        if not int(self.wifi_client.text) == value:
            raise AssertionError("Number of Clients in overview page does not match with the expected number")

    def get_number_of_groups(self):
        grp_cntner = self.browser._browser.find_element_by_xpath("//div[@class='group-container group-list-container']")
        return len(grp_cntner.find_elements_by_xpath("//span[contains(@class, 'group_name_')]"))

    def go_to_second_group(self):
        self.select_group_icon.click()
        self.select_next_group.click()
        group_name = self.select_next_group.text
        if self.browser._browser.find_element_by_xpath("//label[text()='%s']" %group_name):
            return True
        else:
            return False

    def add_network_to_client(self, device, nw, pw):
        myDevice = Device.getDeviceObject(device)
        myDevice.execute("netsh wlan set hostednetwork mode=allow ssid=%s key=\"%s\"" %(nw, pw))

    def go_to_ap_details_page(self):
        self.overview_map_ap.click()
        time.sleep(2)
        ap_details_page = self.ap_details_page
        if ap_details_page:
            return MonitoringAPDetailsPage(self.test, self.browser, self.config)
        else:
            return False


    def go_to_ssid_network_page(self):
        self.overview_wlan_ssid.click()
        time.sleep(2)
        ssid_network_page = self.create_network_page
        if ssid_network_page:
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
        time.sleep(2)
        self.access_points_throughput_graph.click()
        time.sleep(2)
        if direction == "upstream":
            self._upstream_graph.click()
        else:
            try:
                self._downstream_graph.click()
            except:
                pass

    def get_alert_count(self):
        return self.overview_alert_count.text

    def assert_alert_count(self, count):
        for i in range(0, 15):
            if int(re.sub(",", "", self.overview_alert_count.text)) - 1 == int(count):
                break
            else:
                #self.browser.refresh()
                time.sleep(20)
        log.info("Comparing Alerts Count %s and %s" %(self.overview_alert_count.text, count))
        if not int(re.sub(",", "", self.overview_alert_count.text)) - 1 == int(count):
            raise AssertionError("Alert was not generated")

    def assert_click_ap_on_map(self):
        ap_count= self.check_ap_count()
        log.info("AP COUNT      %s" %ap_count)
        if ap_count:
            ap_count = int(self.check_ap_count())

        else:
            raise AssertionError("No AP's")
        self.overview_map_ap.click()
        if ap_count >= 2:
            if not self.access_points_label:
                raise AssertionError("Map was not clicked")
        elif ap_count == 1:
            log.info("Clicking on Single AP, will navigate to AP Device page")
            if not self.ap_details_page:
                raise AssertionError("Map was not clicked")

    def map_zoom(self, action):
        if action == "zoom-in":
            self.overview_map_points_zoom_in.click()
        elif action == "zoom-out":
            self.overview_map_points_zoom_out.click()


    def assert_new_network_in_monitoring(self,ssid="test1"):
        '''
        Verify the new ssid updated in monitoring page.
        '''
        max_wait_time = int(self.config.config_vars.ssid_updation_max_time)
        total_wait_time_elapsed = 0
        time_slots = max_wait_time / 60
        time_interval = max_wait_time / time_slots
        log.info("Verify the ssid : '%s' updated in monitoring page. Max wait time: %s" %(ssid, max_wait_time))
        ssid_updation_flag = self.wlan_table_enable_check(ssid)

        for slot in range(time_slots):
            if ssid_updation_flag:
                break
            log.debug("Max wait time: %s s,Total Time elapsed: %s s" %(max_wait_time,total_wait_time_elapsed))
            time.sleep(time_interval)
            total_wait_time_elapsed = total_wait_time_elapsed + time_interval
            ssid_updation_flag = self.wlan_table_enable_check(ssid)
            self.browser._browser.refresh()
        if ssid_updation_flag:
            log.info("PASS: SSID: '%s' is updated in monitoring page which came in %s seconds" %(ssid,total_wait_time_elapsed))
        else:
            log.info("FAIL: SSID: '%s' is not updated on monitoring page in maximum wait time %s seconds" %(ssid,max_wait_time))
            raise AssertionError("SSID: '%s' is not updated on monitoring page in maximum wait time %s seconds" %(ssid,max_wait_time))
        time.sleep(5)