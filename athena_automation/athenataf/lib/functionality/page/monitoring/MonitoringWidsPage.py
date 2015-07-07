__author__ = 'nmehta'
from athenataf.lib.util.WebPage import WebPage
from Device_Module.ObjectModule import Device
from athenataf.lib.functionality.page.configuration.wids.WidsPage import WidsPage
import traceback

import logging
log = logging.getLogger('athenataf')
import time
import re

class MonitoringWidsPage(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "Monitoring", test, browser, config)
        self.test.assertPageLoaded(self)

    def isPageLoaded(self):
        if self.wids_label:
            return True
        else:
            return False

    def navigate_to_wids_change_setting(self):
        time.sleep(2)
        self.wids_change_setting.click()
        return WidsPage(self.test, self.browser, self.config)

    def connect_device_to_server(self, device):
        myDevice = Device.getDeviceObject(device)
        myDevice.connect_device_to_server()
        i = 1
        while i < 10:
            if myDevice.get_device_status():
                break
            else:
                time.sleep(5)
            i = i+1

        if not myDevice.get_device_status():
            raise AssertionError("Device is not attached to Athena Yet")
        return myDevice




    def get_rogue_aps_count(self):
        if not self.monitoring_wids_rogue_aps.text:
            return 0
        return int(self.monitoring_wids_rogue_aps.text)

    def get_interfering_aps_count(self):
        if not self.monitoring_wids_interfing_aps.text:
            return 0
        return int(self.monitoring_wids_interfing_aps.text)

    def get_infrastructure_attacks_count(self):
        if not self.monitoring_wids_infrasturucture_attacks.text:
            return 0
        return int(self.monitoring_wids_infrasturucture_attacks.text)

    def get_client_attacks_count(self):
        if not self.monitoring_wids_infrasturucture_attacks.text:
            return 0
        return int(self.monitoring_client_attacks_count.text)

    def get_interfering_attack_count_dict(self):
        count_dict = dict()
        count_dict["RogueAP"] = int(self.get_rogue_aps_count())
        count_dict["InterferingAP"] = int(self.get_interfering_aps_count())
        count_dict["InfraAttack"] = int(self.get_infrastructure_attacks_count())
        count_dict["ClientAttack"] = int(self.get_client_attacks_count())
        return count_dict

    def assert_cumulative_count(self, ui_all_group_stat_dict,ui_summed_count):

        if not (ui_summed_count["RogueAP"]-5 <=   ui_all_group_stat_dict["RogueAP"] <= ui_summed_count["RogueAP"]+5):
            raise AssertionError("RogueAP cumulative count does not match all group count")
        if not (ui_summed_count["InterferingAP"]-5 <=   ui_all_group_stat_dict["InterferingAP"] <= ui_summed_count["InterferingAP"]+5):
            raise AssertionError("InterferingAP cumulative count does not match all group count")
        if not (ui_summed_count["InfraAttack"]-5 <=   ui_all_group_stat_dict["InfraAttack"] <= ui_summed_count["InfraAttack"]+5):
            raise AssertionError("InfraAttack cumulative count does not match all group count")
        if not (ui_summed_count["ClientAttack"]-5 <=   ui_all_group_stat_dict["ClientAttack"] <= ui_summed_count["ClientAttack"]+5):
            raise AssertionError("ClientAttack cumulative count does not match all group count")

        log.info("UI All group count matches sum of group accounts")




    def assert_wired_containment(self, value):
        monitor_value = self.monitoring_wids_wired_containment.text
        if not monitor_value.lower() == value.lower():
            raise AssertionError(" wired  containment value not displayed.  i.e. Traceback: %s" %traceback.format_exc())
        else:
            log.info("MonitoringWIDSPage: Wired Contaiment value matches displayed value %s: "  %value)

    def assert_wireless_containment(self, value):
        monitor_value = self.monitoring_wids_wireless_containment.text
        if not monitor_value.lower() == value.lower():
            raise AssertionError(" wireless containment  value not displayed..  i.e. Traceback: %s" %traceback.format_exc())
        else:
            log.info("MonitoringWIDSPage: Wireless Contaiment value matches displayed value %s: "  %value)


    def assert_monitoring_wids_client_protection_level(self, value):
        if not (self.monitoring_wids_client_protection_level.text).lower() == value.lower():
            raise AssertionError(" monitoring_wids_client_protection_level value not displayed.  i.e. Traceback: %s" %traceback.format_exc())
        else:
            log.info("MonitoringWIDSPage: Client Protection Level value matches displayed value %s: "  %value)

    def assert_monitoring_wids_infrastructure_protection_level(self, value):
        if not (self.monitoring_wids_infrastructure_protection_level.text).lower() == value.lower():
            raise AssertionError(" monitoring_wids_infrastructure_protection_leve  i.e. Traceback: %s" %traceback.format_exc())
        else:
            log.info("MonitoringWIDSPage: Infrastructure_protection_level value matches displayed value %s: "  %value)



    def assert_monitoring_wids_client_detection_level(self, value):
        monitor_value = self.monitoring_wids_client_detection_level.text

        if not monitor_value.lower() == value.lower():
            raise AssertionError(" Could not retrieve values.  i.e. Traceback: %s" %traceback.format_exc())
        else:
            log.info("MonitoringWIDSPage: Wids client detection level value matches displayed value %s: "  %value)


    def assert_monitoring_wids_infrastructure_detection_level(self, value):
        if not (self.monitoring_wids_infrastructure_detection_level.text).lower() == value.lower():
            raise AssertionError(" Default recommended settings link not displayed.  i.e. Traceback: %s" %traceback.format_exc())




    def get_stats_from_ap(self, device):
        import re
        myDevice = Device.getDeviceObject(device)
        output = myDevice.get_running_config("GET_IDS_CONFIG")
        time.sleep(20)
        log.info(output)
        stat_dict = dict()
        stat_dict["Rogue"] = len(re.findall('Rogue',output, re.I))
        stat_dict["Interfering"] = len(re.findall('Interfering', output, re.I))
        return stat_dict


    def assert_ui_and_iap_interference_count(self,ui_rogue_count=None,ui_interfering_count=None,iap_stat_count=None):

        iap_rogue = iap_stat_count["Rogue"]
        iap_interfering = iap_stat_count["Interfering"]
        if not (iap_rogue-5<= int(ui_rogue_count) <= iap_rogue+5):
            raise AssertionError ("Monitoring WIDS Page : Value for rogue count does not match ")
        if not self.assertTrue(iap_interfering-5<= int(ui_interfering_count) <= iap_interfering+5):
            raise AssertionError("Monitoring WIDS Page : Value for Interfering does not match")



    def wlan_table_enable_check(self):
        self.browser.refresh()
        try:
            table = self.wlan_table
            log.info(table)
            for tr in table.find_elements_by_tag_name("tr"): ### All rows in the
                log.info(tr.text)
                try:
                    for td in tr.find_elements_by_tag_name("td"): ### Search for TD tag
                        log.info(td.text)
                        if td.text == "test1":
                            return True
                except:
                    pass
        except:
            log.error("Wlan Table Not Enabled")
            return False
        return False


    def get_table_values(self):

        wids_table_first_row = self.monitoring_wids_table_first_row
        table_header_values = ["DATE/TIME", "LEVEL","DESCRIPTION","TYPE","DETECTING AP","VIRTUAL CONTROLLER","RADIO","STATION MAC"]

        try:
            table_row = wids_table_first_row.find_elements_by_tag_name("td")
            if 8 < len(table_row) > 8:
                raise AssertionError ("Error in fetching values for  columns of the table")
            table_row_values = [x.text for x in table_row]
            row_value_dict =dict(zip(table_header_values, table_row_values))

        except:
            pass

        return row_value_dict

    def assert_search_table_by_field(self, type):
        table_values_dict = self.get_table_values()
        search_value = table_values_dict[type]
        self.monitoring_wids_table_search.click()
        log.info("Monitoring Wids Page: Search for %s %s" %(type, search_value))

        if type == "LEVEL":
            result_value = self.search_table_by_field_level(type,search_value)
            time.sleep(2)
            if result_value not in search_value:
                raise AssertionError("Monitoring Wids Page: Level search did not return searched value")
            self.monitoring_wids_search_level.clear()
            self.clear_search()
            partial_value = search_value[:len(search_value)//2]
            log.info("Search for Level partial value %s" %partial_value)
            self.monitoring_wids_table_search.click()
            result_value = self.search_table_by_field_level(type,partial_value)
            if result_value not in search_value:
                raise AssertionError("Monitoring Wids Page: Level search did not return partial searched value")
            self.monitoring_wids_search_level.clear()

        if type == "DESCRIPTION":

            partial_value = search_value[:len(search_value)//4]
            result_value = self.search_table_by_description(type,partial_value)
            time.sleep(2)
            if result_value.strip() not in search_value.strip():
                raise AssertionError("Monitoring Wids Page: Description search did not return searched value")
            self.monitoring_wids_search_description.clear()


        if type == "TYPE":

            result_value = self.search_table_by_type(type,search_value)
            time.sleep(2)
            if result_value not in search_value:
                raise AssertionError("Monitoring Wids Page: Type search did not return searched value")
            self.monitoring_wids_search_type.clear()

        if type == "DETECTING AP":

            result_value = self.search_table_by_detecting_ap(type,search_value)
            time.sleep(2)
            if result_value not in search_value:
                raise AssertionError("Monitoring Wids Page: DETECTING AP search did not return searched value")
            self.monitoring_wids_search_detecting_ap.clear()
            self.clear_search()
            partial_value = search_value[:len(search_value)//2]
            log.info("Monitoring Wids Page: Search for DETECTING AP partial value %s" %partial_value)
            self.monitoring_wids_table_search.click()
            result_value = self.search_table_by_detecting_ap(type,partial_value)
            if result_value not in search_value:
                raise AssertionError("Monitoring Wids Page: DETECTING AP search did not return partial searched value")
            self.monitoring_wids_search_detecting_ap.clear()

        if type == "VIRTUAL CONTROLLER":

            result_value = self.search_table_by_vc(type,search_value)
            time.sleep(2)
            if result_value not in search_value:
                raise AssertionError("Monitoring Wids Page: VIRTUAL CONTROLLER search did not return searched value")
            self.monitoring_wids_search_virtual_controller.clear()
            self.clear_search()
            partial_value = search_value[len(search_value)//2:]
            log.info("Monitoring Wids Page: Search for VIRTUAL CONTROLLER partial value %s" %partial_value)
            self.monitoring_wids_table_search.click()
            result_value = self.search_table_by_vc(type,partial_value)
            if result_value not in search_value:
                raise AssertionError("Monitoring Wids Page: VIrtual Controller search did not return partial searched value")
            self.monitoring_wids_search_virtual_controller.clear()

        if type == "STATION MAC":

            result_value = self.search_table_by_station_mac(type,search_value)
            time.sleep(2)
            if result_value not in search_value:
                raise AssertionError("STATION MAC search did not return searched value")
            self.monitoring_wids_search_station_mac.clear()
            self.clear_search()
            partial_value = search_value[len(search_value)//2:]
            log.info("Search for STATION MAC partial value %s" %partial_value)
            self.monitoring_wids_table_search.click()
            result_value = self.search_table_by_station_mac(type,partial_value)
            if result_value not in search_value:
                raise AssertionError("STATION MAC search did not return partial searched value")
            self.monitoring_wids_search_station_mac.clear()


        if type == "RADIO":

            result_value = self.search_table_by_radio(type,search_value)
            time.sleep(2)
            if result_value not in search_value:
                raise AssertionError("RADIO search did not return searched value")
            self.monitoring_wids_search_radio.clear()
            self.clear_search()
            partial_value = search_value[:len(search_value)//2]
            log.info("Search for RADIO partial value %s" %partial_value)
            self.monitoring_wids_table_search.click()
            result_value = self.search_table_by_radio(type,partial_value)
            if result_value not in search_value:
                raise AssertionError("RADIO search did not return partial searched value")
            self.monitoring_wids_search_radio.clear()

        self.clear_search()
        log.info("Cleared and exited the search")

    def clear_search(self):
        self.monitoring_wids_search_clear_values.click()
        self.monitoring_wids_search_submit.click()
        self.monitoring_wids_table_search.click()

    def search_table_by_field_level(self, type, search_value):
        self.monitoring_wids_search_level.send_keys(search_value)
        self.monitoring_wids_search_submit.click()
        table_value_dict_after_search = self.get_table_values()
        return table_value_dict_after_search[type]


    def search_table_by_description(self, type, search_value):
        self.monitoring_wids_search_description.send_keys(search_value.strip())
        self.monitoring_wids_search_submit.click()
        table_value_dict_after_search = self.get_table_values()
        time.sleep(2)
        return table_value_dict_after_search[type]

    def search_table_by_type(self, type, search_value):
        self.monitoring_wids_search_type.send_keys(search_value)
        self.monitoring_wids_search_submit.click()
        table_value_dict_after_search = self.get_table_values()
        time.sleep(2)
        return table_value_dict_after_search[type]


    def search_table_by_detecting_ap(self, type, search_value):
        self.monitoring_wids_search_detecting_ap.send_keys(search_value)
        self.monitoring_wids_search_submit.click()

        table_value_dict_after_search = self.get_table_values()
        return table_value_dict_after_search[type]

    def search_table_by_vc(self, type, search_value):
        self.monitoring_wids_search_virtual_controller.send_keys(search_value)
        self.monitoring_wids_search_submit.click()

        table_value_dict_after_search = self.get_table_values()
        return table_value_dict_after_search[type]


    def search_table_by_station_mac(self, type, search_value):
        self.monitoring_wids_search_station_mac.send_keys(search_value)
        self.monitoring_wids_search_submit.click()
        table_value_dict_after_search = self.get_table_values()
        return table_value_dict_after_search[type]


    def search_table_by_radio(self, type, search_value):
        self.monitoring_wids_search_radio.send_keys(search_value)
        self.monitoring_wids_search_submit.click()
        table_value_dict_after_search = self.get_table_values()
        return table_value_dict_after_search[type]


    def select_value_per_page(self,value):
        try:
            self.monitoring_wids_table_rows_per_page.set(value)
            time.sleep(4)
        except Exception, e:
            log.info("Could not change the value, error message %s"  %e.message)

    def assert_value_per_page(self, value):
        rows_per_page = self.browser._browser.find_elements_by_xpath("//table[@id='Wids_AccessPoints']/tbody/tr")
        log.info("Rows per page: %d " %len(rows_per_page))
        rows_per_page = len(rows_per_page)
        if not rows_per_page <= int(value):
            raise AssertionError("Rows size is %s  actual row value is  is %d incorrect" %(value, rows_per_page))


    def assert_page_selected(self):
        import random
        time.sleep(2)
        pagination = self.browser._browser.find_elements_by_xpath("//div[contains(@id,'monitoringWIDSEventsTable_pagination_nav')]/div[@class='pager']/a")
        pagination_size = len(pagination)
        self.monitoring_wids_jump_input.clear()
        rand_value = random.randint(1, pagination_size)
        log.debug("Pagination size value %d" %pagination_size)
        log.info("MontoringWidsPage : Jump to page number %d" %rand_value)
        self.monitoring_wids_jump_input.send_keys(str(rand_value))
        self.monitoring_wids_jump_input_confirm.click()
        path = "//a[@class='ng-scope ng-binding current_page enable' and text()=%s]"  %rand_value
        if not (self.browser._browser.find_element_by_xpath(path)):
            raise AssertionError("Page not selected %s" %rand_value)
        else:
            log.info("MontoringWidsPage : Jumped to page number %d" %rand_value)

            
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
            ele_object = eval("self.monitoring_wids_%s" %element)
            time.sleep(2)
            action_chain.move_to_element(ele_object).perform()
            if re.search('\S+',self.help_content.text):
                log.info("PASS: Help text for \"%s\" is existing." %element)
            else:
                log.info("FAIL: Help text for \"%s\" is not existing/Empty." %element)
                raise AssertionError("Help content is not opened/Empty i.e. Traceback: %s" %traceback.format_exc())
            self.help_content.click()
            time.sleep(3)




    def click_on_timeline(self, duration):
        duration = duration.lower()
        if duration == "onehour":
            log.info("MonitoringWidsPage: Clicking on one hour")
            self.monitoring_wids_1h.click()
        if duration == "oneday":
            log.info("MonitoringWidsPage: Clicking on one day")
            self.monitoring_wids_1d.click()
        if duration == "oneweek":
            log.info("MonitoringWidsPage: Clicking on one week")
            self.monitoring_wids_1w.click()




