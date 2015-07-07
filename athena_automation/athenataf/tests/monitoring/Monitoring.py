__author__ = 'rrkrishnan'
import logging
log = logging.getLogger('athenataf')
import os
from athenataf.lib.functionality.test.MonitoringTest import MonitoringTest
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest
from athenataf.lib.functionality.page.monitoring.MonitoringAPDetailsPage import MonitoringAPDetailsPage
from athenataf.lib.functionality.common import DeviceLibrary
import time
from Device_Module.ObjectModule import Device
from athenataf.config import devices

class Monitoring(ConfigurationTest, MonitoringTest):

    def test_ath_11511_assert_customer(self):
        """
        ################################################################################################################
        NAME : Ramakrishnan R
        ################################################################################################################
        REQUIREMENT : 1 IAP with no network as test1
        RUNTIME     : 10.3 Minutes
        ################################################################################################################
        1
            1.Attach 1 or 2 IAPs to Athena
            2.Create two to three different networks
            3.Navigate to Monitoring-> overview
            4.Click on any WLAN network from wlan tables
            5.Check whether hand pointers appear for WLAN network to click
            6.Check for 32 char network tool tip is provided to view the complete name in WLAN table of overview page
        2
            1.Click on the total AP Count from overview page
            2.Click on the UP AP page or down AP page
            3.Click on the Wireless client count
            4.Click on the wired client count
        ################################################################################################################
        """
        log.info("Test Setup :")
        log.info("STEP 1")
        log.info("STEP 1.1 : Assuming Devices are attached ")
        log.info("#"*80)
        log.info("STEP 1.2 : Create two to three different networks")
        log.info("Deleting Network if present")
        #self.NetworkPage.delete_network_if_present()
        #overview_page = self.LeftPanel.goto_monitoringPage()
        #overview_page.go_to_default_group()
        #self.LeftPanel.go_to_network_page()
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        log.info("Taking Running Config before configuration")
        log.info("Creating New Network")
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True,False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network()
        time.sleep(100)
        log.info("#"*80)
        log.info("STEP 1.3 : Navigate to Monitoring-> overview")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        time.sleep(1)
        log.info("#"*80)
        log.info("STEP 1.4 : Click on any WLAN network from wlan tables")
        log.info("STEP 1.5 : Check whether hand pointers appear for WLAN network to click")
        log.info("Verify wlan table values")
        self.browser.refresh()
        monitor_page.wlan_table_enable_check()
        log.info("#"*80)
        log.info("STEP 1.6 : Check for 32 char network tool tip is provided to view the complete name in WLAN table of overview page")
        log.info("Verifying tool tip for the WLAN Table")
        monitor_page.verify_tool_tip()
        log.info("#"*80)
        log.info("STEP 2")
        log.info("STEP 2.1 : Click on the total AP Count from overview page")
        if monitor_page.check_ap_count() >= 0:
            log.info("APs are attached to the instance")
            pass
        else:
            assert False, "APs are not added"
        log.info("Click on All AP Link")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.go_to_all_ap()
        log.info("Navigated to Access Points page")
        log.info("#"*80)
        log.info("STEP 2.2 : Click on the UP AP page or down AP page")
        log.info("Click on UP AP link")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.go_to_up_ap()
        log.info("Navigated to Access Points page")
        log.info("Click on DOWN AP link")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.go_to_down_ap()
        log.info("Navigated to Access Points page")
        log.info("#"*80)
        log.info("STEP 2.3 : Click on the Wireless client count")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.go_to_wifi_clients()
        log.info("Navigated to Clients page")
        log.info("#"*80)
        log.info("STEP 2.4 : Click on the Wired client count")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.go_to_wired_clients()
        log.info("Navigated to Clients page")
        log.info("CLEANUP :")
        log.info("Deleting Network if present")
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        log.info("END OF TESTCASE : ATH-11511")
##

    def test_ath_11400_assert_customer(self):
        """
        ################################################################################################################
        NAME : Ramakrishnan R
        ################################################################################################################
        REQUIREMENT : 1 IAP with no network as test1
        RUNTIME     : 7.74 Minutes
        ################################################################################################################
        1
            1.Attach 1 or 2 IAPs to Athena
            2.Create two to three different networks
            3.Navigate to Monitoring-> overview
            4.Click on any WLAN network from wlan tables
            5.Check whether hand pointers appear for WLAN network to click
            6.Check for 32 char network tool tip is provided to view the complete name in WLAN table of overview page
         2
            Delete few of network which is already pushed to IAP
        ################################################################################################################
        """
        log.info("Test Setup :")
        log.info("STEP 1")
        log.info("STEP 1.1 : Assuming Devices are attached ")
        log.info("#"*80)
        log.info("STEP 1.2 : Create two to three different networks")
        log.info("Deleting Network if present")
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()
        self.LeftPanel.go_to_network_page()
        #self.NetworkPage.delete_network_if_present()
        self.NetworkPage.delete_all_networks()
        log.info("Creating New Network")
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True,False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network()
        time.sleep(100)
        log.info("#"*80)
        log.info("STEP 1.3 : Navigate to Monitoring-> overview")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        time.sleep(2)
        log.info("#"*80)
        log.info("STEP 1.4 : Click on any WLAN network from wlan tables")
        log.info("STEP 1.5 : Check whether hand pointers appear for WLAN network to click")
        log.info("Verify wlan table values")
        self.browser.refresh()
        monitor_page.wlan_table_enable_check()
        monitor_page.assert_network_in_ap("IAP_1", "test1")
        log.info("#"*80)
        log.info("STEP 1.6 : Check for 32 char network tool tip is provided to view the complete name in WLAN table of overview page")
        log.info("Verifying tool tip for the WLAN Table")
        monitor_page.verify_tool_tip()
        log.info("#"*80)
        log.info("STEP 2")
        log.info("STEP 2.1 : Delete few of network which is already pushed to IAP")
        log.info("Deleting Network if present")
        self.LeftPanel.goto_configuration_page()
        self.NetworkPage.delete_network_if_present()
        time.sleep(5)
        monitor_page.assert_network_not_in_ap("IAP_1", "test1")
        log.info("END OF TESTCASE : ATH-11400")
##
    def test_ath_11401_check_negative_scenarios_in_overview_page(self):
        """
        ################################################################################################################
        NAME : Ramakrishnan R
        ################################################################################################################
        REQUIREMENT : 0 IAP
        RUNTIME     : 6 Minutes
        ################################################################################################################
        1
            Navigate to Monitoring ->overview ->WLAN table
            a. Click on any of the Instant ssid present in the WLAN table
            b. AP/Client/Alert count should exist even if no IAPs are attached
            c. Map view with No IAPs or down IAPs
        ################################################################################################################
        """
        log.info("Test Setup :")
        log.info("STEP 1")
        log.info("STEP 1.1 : Assuming Devices are not attached ")
        log.info("#"*80)
        monitor_page = self.LeftPanel.goto_monitoringPage()
        monitor_page.go_to_all_groups_page()
        monitor_page.go_to_default_group()

        log.info("Verify wlan table values")
        monitor_page.wlan_table_disable_check()
        log.info("#"*80)
        log.info("STEP 1.2 : AP/Client/Alert count should exist even if no IAPs are attached")
        log.info("Click on All AP Link")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.go_to_all_ap()
        log.info("Navigated to Access Points page")
        log.info("#"*80)
        log.info("Click on the UP AP page or down AP page")
        log.info("Click on UP AP link")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.go_to_up_ap()
        log.info("Navigated to Access Points page")
        log.info("Click on DOWN AP link")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.go_to_down_ap()
        log.info("Navigated to Access Points page")
        log.info("#"*80)
        log.info("Click on the Wireless client count")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.go_to_wifi_clients()
        log.info("Navigated to Clients page")
        log.info("#"*80)
        log.info("Click on the Wired client count")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.go_to_wired_clients()
        log.info("Navigated to Clients page")
        log.info("#"*80)
        log.info("STEP 1.3 : Map view with No IAPs or down IAPs")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.check_no_ap_in_map()
        log.info("#"*80)
        log.info("END OF TEST CASE : ATH-11401")

    def test_ath_11399_check_quick_links(self):
        """
        ################################################################################################################
        NAME : Arunkarthick A
        DATE : 3/2/2015
        1
            Navigate to Monitoring ->Overview on all group level
            a.Select create new network from quick links
            b.Select create report
            c.Select manage groups
            d.Select update firmware
            e.Select set security
            f. Select manage devices
        2
            Navigate to Monitoring ->Overview on a group level
            a.Select create new network from quick links
            b.Select create report
            c.Select manage groups
            d.Select update firmware
            e.Select set security
            f. Select manage devices
        ################################################################################################################
        """
        log.info("Test Setup :")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        log.info("STEP 1 : Navigate to Monitoring ->Overview on all group level")
        log.info("#"*80)
        log.info("STEP 1.1 : Select create new network from quick links  ")
        monitor_page.go_to_all_groups_page()
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.create_new_network_quicklink()
        log.info("STEP 1.2 : Select create report from quick links  ")
        monitor_page.go_to_all_groups_page()
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.create_report_quicklink()
        log.info("STEP 1.3 : Select manage groups from quick links  ")
        monitor_page.go_to_all_groups_page()
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.manage_groups_quicklink()
        log.info("STEP 1.4 : Select update device firmware from quick links  ")
        monitor_page.go_to_all_groups_page()
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.update_device_firmware_quicklink()
        log.info("STEP 1.5 : Select set security from quick links  ")
        monitor_page.go_to_all_groups_page()
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.set_security_quicklink()
        log.info("STEP 1.6 : Select manage devices from quick links  ")
        monitor_page.go_to_all_groups_page()
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.manage_devices_quicklink()
        log.info("#"*80)
        log.info("STEP 2 : Navigate to Monitoring ->Overview on a group level")
        log.info("#"*80)
        single_group=True
        log.info("STEP 2.1 : Select create new network from quick links  ")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.go_to_all_groups_page()
        monitor_page.go_to_default_group()
        monitor_page.create_new_network_quicklink(single_group)
        log.info("STEP 2.2 : Select create report from quick links  ")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.create_report_quicklink()
        log.info("STEP 2.3 : Select manage groups from quick links  ")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.manage_groups_quicklink()
        log.info("STEP 2.4 : Select update device firmware from quick links  ")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.update_device_firmware_quicklink()
        log.info("STEP 2.5 : Select set security from quick links  ")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.set_security_quicklink(single_group)
        log.info("STEP 2.6 : Select manage devices from quick links  ")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.manage_devices_quicklink(single_group)
        log.info("#"*80)
        log.info("END OF TEST CASE - test_ath_11399_check_quick_links")

    def test_ath_11403_check_ap_help_text(self):
        """
        a.Navigate to Monitoring ->Access Point
        b.Enable help which will look like a Question mark next to Notifications
        """
        log.info("Test Setup :")
        log.info("STEP 1: Enable Help ")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        monitor_page.enable_help()
        log.info("STEP 2: Navigate to Montitoing Access Page ")
        monitor_access_page = self.LeftPanel.go_to_monitoring_access_page()

        log.info("STEP 3: Click on the highlighted help labels ")
        monitor_access_page.assert_help_option_for_access_points_flagged()
        monitor_access_page.assert_help_option_for_access_points_clients()
        monitor_access_page.assert_help_option_for_access_points_throughput()
        monitor_access_page.assert_help_option_for_access_points_flagged_ap()
        monitor_access_page.assert_help_option_for_access_points_flagged_util()
        monitor_access_page.assert_help_option_for_access_points_flagged_table_noise()
        monitor_access_page.assert_help_option_for_access_points_flagged_table_errors()
        monitor_access_page.assert_help_option_for_access_points_flagged_table_clients()
        monitor_access_page.assert_help_option_for_access_points_flagged_table_memory()
        monitor_access_page.assert_help_option_for_access_points_ap_location()
        monitor_access_page.assert_help_option_for_access_points_ap_status()
        monitor_access_page.assert_help_option_for_access_points_ap_clients()
        monitor_access_page.assert_help_option_for_access_points_ap_uptime()


        monitor_page.enable_help()
        log.info("#"*80)
        log.info("END OF TEST CASE - test_ath_11403_check_ap_help_text")


    def test_ath_11402_check_overview_help_text(self):
        """
        1.a Navigate to Monitoring ->overview
        1.b Enable help which will look like a Question mark next to Notifications
        """
        log.info("Test Setup :")
        log.info("STEP 1b:Navigate to Monitoring ->overview")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        log.info("STEP 1b: Enable Help ")
        monitor_page.enable_help()
        monitor_page.assert_help_option_for_access_points()
        monitor_page.assert_help_option_for_alerts()
        monitor_page.assert_help_option_for_clients()
        monitor_page.assert_help_option_for_access_throughput()
        monitor_page.enable_help()
        log.info("#"*80)
        log.info("END OF TEST CASE - test_ath_11402_check_overview_help_text")

    def test_ath_11466_page_with_zero_ap(self):
        """
        ################################################################################################################
            Navigate to Monitoring ->Access points

            a. make sure that the Down AP count is '0'

            b. Click on down AP count should display the AP table with no entries.

            c. Make sure that Monitoring overview page has Down AP count '0' and is not in RED
        ################################################################################################################
        """
        log.info("Test Setup :")
        self.LeftPanel.goto_monitoringPage()

        log.info("STEP 1")
        log.info("STEP 1.1 : Assuming No Devices are attached ")
        log.info("#"*80)
        log.info("STEP ")
        log.info("Navigate to Monitoring Access points")
        monitor_access_page=self.LeftPanel.go_to_monitoring_access_page()
        log.info("STEP 1A: Check down AP count is 0")
        ap_down_count = monitor_access_page.ap_page_ap_down_count()
        if int(ap_down_count) == 0:
            log.info("No, APs are attached to the instance")
        else:
            assert False, "APs are added"

        monitor_access_page.assert_ap_table_empty_check_down_ap()



        log.info("STEP 1C: Navigate to Monitoring Overview Page")
        overview_page = self.LeftPanel.goto_monitoringPage()
        monitoring_ap__down_count = overview_page.check_monitoring_page_ap_down_count()
        if int(monitoring_ap__down_count) == 0:
            log.info("No, APs are attached to the instance")
        else:
            assert False, "APs are added"




    def test_ath_11516_create_label_with_max_length(self):
        """
        Register multiple IAPs to different groups of athena
        a.Create a label which is of 32 character length from AP detail page and overview page
        """
        log.info("Test Setup :")
        self.LeftPanel.goto_monitoringPage()
        monitor_page = self.LeftPanel.goto_monitoringPage()
        log.info("STEP 1")
        log.info("STEP 1.1 : Assuming Devices are attached ")
        log.info("#"*80)
        log.info("STEP ")
        log.info("STEP 1.2 : Register multiple IAPs to different groups of athena")
        log.info("Assume an IAP is attached to default group")
        monitoring_access_page = self.LeftPanel.go_to_monitoring_access_page()

        log.info("STEP 2")
        log.info("STEP 2.1 : Create a label which is of 32 character length from AP detail page")
        monitoring_access_page.add_label_by_variable_name_length("IAP_1", "a"*32)
        log.info("STEP 2.2 : Create an existing label for another AP or for the same AP")
        if not monitoring_access_page.add_label_by_variable_name_length("IAP_1", "a"*32, True):
            log.info("Error thrown for Label already exists")
        else:
            log.error("Accepted duplicate Label name")
            assert False, "Accepted duplicate Label name"
        self.browser.refresh()
        self.LeftPanel.go_to_monitoring_access_points()
        log.info("STEP 2.3 : Create a label which is more than 32 characters length")
        if not monitoring_access_page.add_label_by_variable_name_length("IAP_1", "a"*33, True):
            log.info("Error thrown for Label length greater then 33")
        else:
            log.error("Accepted Label with 33 chars")
            assert False, "Accepted 33 char Label name"
        monitoring_access_page.delete_label_from_ap("IAP_1", "a"*32)
        log.info("CLEANUP :")
        self.browser.refresh()
        self.LeftPanel.go_to_monitoring_access_points()
        monitoring_access_page.delete_all_label_from_ap("IAP_1")
        log.info("END OF TESTCASE : test_ath_11516_create_label_with_max_length")

    def test_ath_11467_create_max_num_of_labels(self):
        log.info("Test Setup :")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        log.info("STEP 1")
        log.info("STEP 1.1 : Assuming Devices are attached ")
        log.info("#"*80)
        log.info("STEP 2")
        log.info("STEP 2.1 : Register multiple IAPs to different groups of athena")
        log.info("Assume an IAP is attached to default group")
        access_page = self.LeftPanel.go_to_monitoring_access_page()
        log.info("STEP 2.1 : Create more than 10 labels for each AP")
        access_page.add_multiple_label_to_ap("IAP_1", 12)
        log.info("STEP 2.2 : Create an existing label for another AP or for the same AP")
        if not access_page.add_multiple_label_to_ap("IAP_1", 2, True):
            log.info("Error thrown for Label already exists")
        else:
            log.error("Accepted duplicate Label name")
            assert False, "Accepted duplicate Label name"

        self.LeftPanel.go_to_monitoring_access_page()
        access_page.add_multiple_label_to_ap("IAP_1", 1)
        log.info("STEP 2.2 :   Add 1 more label in same AP which already has 14 label associated.")
        if not access_page.add_multiple_label_to_ap("IAP_1", 2, True):
            log.info("Error thrown for adding more than 14 labels")
        else:
            log.error("Able to create 15 labels")
            assert False, "Accepted creation of more then 14 labels"


        self.LeftPanel.go_to_monitoring_access_points()
        log.info("STEP 2.3 : Delete the created labels")
        access_page.delete_label_from_ap("IAP_1", "LABEL1")
        log.info("CLEANUP :")


        self.LeftPanel.go_to_monitoring_access_points()
        access_page.delete_all_label_from_ap("IAP_1")
        log.info("END OF TESTCASE : test_ath_11467_create_max_num_of_labels")

    def test_ath_11518_check_hyperlinks(self):
        """
        Login to Athena
            a.click the count in the total Access point
            b.click the count in the total Access point that are up
        Login to Athena
            a.Click the Count of wireless client
            b.Click the count of wired clients
        Login to Athena
            Click the SSID name which is listed in the WLAN table
        """
        log.info("Test Setup :")
        log.info("Navigate to network page, to create a new network")
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_network_if_present()
        log.info("Creating New Network")
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True,False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network()
        time.sleep(100)
        monitor_page = self.LeftPanel.goto_monitoringPage()
        time.sleep(1)
        log.info("STEP 1")
        log.info("STEP 1.1: Assuming logged into Athena and in monitoring page")
        log.info("#"*80)
        log.info("STEP 1.2 : Click the count in Access point ")
        monitor_page.go_to_all_ap()
        log.info("Navigated to Access Points page")
        log.info("#"*80)
        log.info("STEP 1.3 : Click on the UP AP page or down AP page")
        log.info("Click on UP AP link")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.go_to_up_ap()
        log.info("Navigated to Access Points page")
        log.info("Click on DOWN AP link")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.go_to_down_ap()
        log.info("Navigated to Access Points page")
        log.info("#"*80)
        log.info("STEP 2.1 : Click on the Wireless client count")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.go_to_wifi_clients()
        log.info("Navigated to Clients page")
        log.info("#"*80)
        log.info("STEP 2.2 : Click on the Wired client count")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.go_to_wired_clients()
        log.info("Navigated to Clients page")
        log.info("#"*80)
        self.LeftPanel.go_to_monitoring_page()
        log.info("STEP 3.1 : Click on  WLAN network SSID from wlan tables")
        log.info("Verify wlan table values")
        monitor_page.go_to_ssid_network_page()
        log.info("Navigated to SSID network page")
        log.info("#"*80)
        log.info("CLEANUP :")
        log.info("Deleting Network if present")
        self.NetworkPage.delete_network_if_present()
        self.LeftPanel.go_to_monitoring_page()
        log.info("END OF TESTCASE : 11518_check_hyperlinks")

    def _set_ap_detection_and_protection_settings(self):
        wids_page = self.LeftPanel.go_to_monitoring_wids_page()
        wireless_wids_page = wids_page.navigate_to_wids_change_setting()
        wireless_wids_page.set_detection_infra_threat_detection_level("High")
        wireless_wids_page.set_detection_clients_threat_detection_level("High")
        # set infra client high sets the value high for infra threat and client threat
        wireless_wids_page.set_infra_client_high()
        wireless_wids_page.wired_containment_on()
        wireless_wids_page.wireless_containment_deauthenticate()

    def _set_ap_detection_and_protection_to_off(self):
        wids_page = self.LeftPanel.go_to_monitoring_wids_page()
        wireless_wids_page = wids_page.navigate_to_wids_change_setting()
        wireless_wids_page.set_detection_infra_threat_detection_level("Off")
        wireless_wids_page.set_detection_clients_threat_detection_level("Off")
        wireless_wids_page.set_infra_client_default()



        wireless_wids_page.restore_defaults_wired_wireless_containment_methods()

    def test_ath_11491_check_cumulative_count(self):
        """
        1. Attach multiple IAP to different groups of Athena
        2
            a.Select the group Navigate to Monitoring ->WIDS
            b.Click on change setting
            c.Configure AP with WID level to different levels
                                        Detection - High,High
                                        Protection -High, High

            d.Change wired containment to on and wireless containment to deauthenticate
            e.Click save settings

        3
           a. Check the Rogue AP, Interferring AP, Infra attacks and Client attacks in separate group level
           b.  Check the cumulative results of separate group level
        """
        log.info("Test Setup :")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        log.info("STEP 1 : Navigate to Monitoring ->Overview on all group level")
        log.info("#"*80)
        log.info("STEP 1.1 : Select the group Navigate to Monitoring ->WIDS  ")
        monitor_page.go_to_all_groups_page()
        monitor_page.go_to_default_group()
        self.LeftPanel.goto_monitoringPage()
        log.info("STEP 1.1 : Select the first group Navigate to Monitoring ->WIDS  ")
        self._set_ap_detection_and_protection_settings()
        log.info("STEP 1.1.1: Select the second group and enable the WID Levels to different settings")
        monitor_page.go_to_all_groups_page()
        monitor_page.go_to_second_group()
        self.LeftPanel.go_to_monitoring_page()
        self._set_ap_detection_and_protection_settings()
        log.info("STEP 2.3 : Wait for 10 minutes for the attacks  to be displayed in UI  ")
        time.sleep(600)
        log.info("STEP 2.4.1 : Disable the change settings for second group different levels to default or OFF")
        self.LeftPanel.goto_monitoringPage()
        self._set_ap_detection_and_protection_to_off()
        log.info("STEP 2.4.2 : Disable the change settings for first group different levels to default or OFF")
        monitor_page.go_to_all_groups_page()
        monitor_page.go_to_default_group()
        self.LeftPanel.goto_monitoringPage()
        self._set_ap_detection_and_protection_to_off()
        self.LeftPanel.goto_monitoringPage()
        monitor_page.go_to_all_groups_page()
        wids_page = self.LeftPanel.go_to_monitoring_wids_page()
        log.info("STEP 2.4.3 : Fetch cumulative value")
        ui_all_group_stat_dict = wids_page.get_interfering_attack_count_dict()
        log.info("STEP : Fetch Group 1 count")
        monitor_page.go_to_default_group()
        ui_default_group_stat_dict = wids_page.get_interfering_attack_count_dict()
        log.info("STEP : Fetch Group 2 count")
        monitor_page.go_to_second_group()
        ui_second_group_stat_dict = wids_page.get_interfering_attack_count_dict()
        log.info("STEP: Assert cumulative count ")
        ui_summed_stat = {k:ui_default_group_stat_dict.get(k,0) + ui_second_group_stat_dict.get(k,0) for k in ui_default_group_stat_dict}
        wids_page.assert_cumulative_count(ui_all_group_stat_dict,ui_summed_stat)
        log.info("END OF TESTCASE : 111491_check_cumulative_count")

    def test_ath_11486_check_wids_with_different_levels(self):
        """
        1.Attach multiple IAP to athena using the below command in IAP console
        2.Select the group Navigate to Monitoring ->WIDS
                b.Click on change setting
                c.Configure AP with WID level to different levels
                        Detection - High,Medium
                        Protection -Low, High
                d.Change wired containment to on and wireless containment to deauthenticate only
                e.Click save settings
        3.
            a.Get  Rogue APs/Interfering APs count from IAP and compare it against the WIDs page display
            b.Pie chart data on WIDS monitoring page
            c.MAPs on WIDS monitoring page

        """
        log.info("Test Setup :")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        log.info("STEP 1 : Navigate to Monitoring ->Overview on all group level")
        log.info("#"*80)
        log.info("STEP 1.1 : Select the group Navigate to Monitoring ->WIDS  ")
        monitor_page.go_to_all_groups_page()
        log.info("STEP 2.1 : Select the group Navigate to Monitoring ->WIDS  ")
        monitor_page.go_to_default_group()
        self.LeftPanel.goto_monitoringPage()
        wids_page = self.LeftPanel.go_to_monitoring_wids_page()
        log.info("STEP 2.2 : Change the settings for different levels  ")
        wireless_wids_page = wids_page.navigate_to_wids_change_setting()
        wireless_wids_page.set_detection_infra_threat_detection_level("High")
        wireless_wids_page.set_detection_clients_threat_detection_level("High")
        wireless_wids_page.set_infra_client_high()
        wireless_wids_page.wired_containment_on()
        wireless_wids_page.wireless_containment_deauthenticate()
        log.info("STEP 2.3 : Wait for 10 minutes for the attacks  to be displayed in UI  ")
        time.sleep(600)
        log.info("STEP 2.4 : Disable the change settings for different levels to default or OFF")
        self._set_ap_detection_and_protection_to_off()
        self.LeftPanel.goto_monitoringPage()


        wids_page = self.LeftPanel.go_to_monitoring_wids_page()
        iap_stat_count = wids_page.get_stats_from_ap("IAP_1")
        ui_count_dict = wids_page.get_interfering_attack_count_dict()
        wids_page.assert_ui_and_iap_interference_count(ui_count_dict["RogueAP"],ui_count_dict["InterferingAP"],iap_stat_count)

    def test_ath_11493_wired_and_wireless_containment(self):
        """
        1.Attach multiple IAP to athena using the below command in IAP console
        2

            a.Select the group Navigate to Monitoring ->WIDS
            b.Click on change setting
            c.Configure AP with WID level to different levels
                                        Detection - High,Medium
                                        Protection -Low, Low

            d.Change wired containment to on and wireless containment to Tarpit invalid stations only
            e.Click save settings

        3
            Select the group and Navigate to Monitoring ->WIDS
            Click on change setting
            a.Change wired containment to on and wireless containment to Tarpit all stations only
            b.Click save settings


        4   Click Restore defaults
        :return:
        """
        """
        :return:
        """
        log.info("Test Setup :")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        log.info("STEP 1 : Navigate to Monitoring ->Overview on all group level")
        log.info("#"*80)
        log.info("STEP 1.1 : Select the group Navigate to Monitoring ->WIDS  ")
        monitor_page.go_to_all_groups_page()
        log.info("STEP 2.1 : Select the group Navigate to Monitoring ->WIDS  ")
        monitor_page.go_to_default_group()
        self.LeftPanel.goto_monitoringPage()
        wids_page = self.LeftPanel.go_to_monitoring_wids_page()
        log.info("STEP 2.2 : Change the settings for different levels  ")
        wireless_wids_page = wids_page.navigate_to_wids_change_setting()
        wireless_wids_page.set_detection_infra_threat_detection_level("High")
        wireless_wids_page.set_detection_clients_threat_detection_level("Medium")
        wireless_wids_page.set_infra_client_low()
        wireless_wids_page.wired_containment_on()
        wireless_wids_page.wireless_tarpit_invalid()
        log.info("STEP 2.3 : Check the setting values are reflected in monitoring page")
        self.LeftPanel.goto_monitoringPage()

        self.LeftPanel.go_to_monitoring_wids_page()
        log.info("STEP 2.4 : Retrieving values from monitoring page")
        wids_page.assert_monitoring_wids_client_detection_level("Medium")
        wids_page.assert_monitoring_wids_infrastructure_detection_level("High")
        wids_page.assert_monitoring_wids_client_protection_level("Low")
        wids_page.assert_monitoring_wids_infrastructure_protection_level("Low")
        wids_page.assert_wireless_containment("tarpit-non-valid-sta")
        wids_page.assert_wired_containment("On")
        log.info("Tear Down : Clean up of Wids settings")
        self._set_ap_detection_and_protection_to_off()
        log.info("STEP 3.1 : Change the settings for wired containment and tarpit only  ")
        self.LeftPanel.goto_monitoringPage()
        self.LeftPanel.go_to_monitoring_wids_page()
        wids_page.navigate_to_wids_change_setting()
        wireless_wids_page.wired_containment_on()
        wireless_wids_page.wireless_tarpit_all()

        log.info("STEP 2.3 : Check the setting values are reflected in monitoring page")
        self.LeftPanel.goto_monitoringPage()
        self.LeftPanel.go_to_monitoring_wids_page()
        log.info("STEP 3.2 : Retrieving values from monitoring page")
        wids_page.assert_wireless_containment("tarpit-all-sta")
        wids_page.assert_wired_containment("On")
        log.info("3.3 : Set the restore defaults")
        self._set_ap_detection_and_protection_to_off()
        log.info("3.4 : Verify the deault values in Monitoring WIDS page")

        self.LeftPanel.goto_monitoringPage()
        self.LeftPanel.go_to_monitoring_wids_page()
        wids_page.assert_monitoring_wids_client_detection_level("Off")
        wids_page.assert_monitoring_wids_infrastructure_detection_level("Off")
        wids_page.assert_monitoring_wids_client_protection_level("Off")
        wids_page.assert_monitoring_wids_infrastructure_protection_level("Off")
        wids_page.assert_wireless_containment("None")
        wids_page.assert_wired_containment("Off")
        log.info("END OF TEST CASE")
        
        
    def test_ath_11470_ap_map(self):
        """
            1. Register multiple IAPs to different groups of athena
                a.Change the location of AP
                b.Register AP from different locations
            2
                a.Expand the map in AP overview page
                b.Click on the AP MAP in AP overview page

            3
                a. Zoom in and out
                b. Map should show the zoom in and zoom out view

        ################################################################################################################
            REQUIREMENT : 1 IAP
            RUNTIME     : 6 Minutes
        ################################################################################################################
        """

        log.info("Test Setup :")
        log.info("SETUP")
        log.info("STEP 1.1 : Register multiple IAPs to different groups of athena")
        log.info("Assume 1 or more IAP is attached in athena")
        log.info("#" * 80)
        overview_page = self.LeftPanel.goto_monitoringPage()
        #overview_page.go_to_default_group()
        log.info("Click on AP in map")
        ap_details_page = overview_page.go_to_ap_details_page()
        log.info("STEP 1.2 : Change the location of AP")
        log.info("STEP 1.3 : Register AP from different locations")
        log.info("STEP 1.4.1 : change location and check")
        ap_details_page.assert_edit_location_changed()
        self.LeftPanel.goto_monitoringPage()
        ap_page = self.LeftPanel.go_to_monitoring_access_page()
        log.info("STEP 2.1 : Expand Map on AP detail page")
        ap_page.expand_map()


        log.info("STEP 1.6 : Assert click on Map")
        self.LeftPanel.goto_monitoringPage()
        overview_page.assert_click_ap_on_map()
        monitoring_access_page = self.LeftPanel.go_to_monitoring_access_page()

        log.info("STEP 3.1 : Zoom in zoom out")
        monitoring_access_page.map_zoom("zoom-in")
        monitoring_access_page.map_zoom("zoom-out")

    def test_ath_11492_wids_search(self):
        """"
        1.Attach multiple IAP to athena using the below command in IAP console
        2.
            a.Select the group Navigate to Monitoring ->WIDS
            b.Click on change setting
            c.Configure AP with WID level to different levels
                    Detection - High,high
                    Protection -High, high
            d.Change wired containment to on and wireless containment to de-authenticate only
            e.Click save setting

        3. Once the Event page log is created check the following -
            a. Try to filter out the logs based on different search fields and try to filter out using patial MAC for ex :65 or :03:04 and search based on time/date
            b. Modify the search based on  Description, Type, VC, Radio
            c. Check the entire log page for hand pointers and check whether the horizontal bar at the end is alligned with the headers for different search criteria
            d. Check whether we are able to scroll the page and header shouldn't be hidden when we scroll down
        4.  Change the count on per page to different values like 5,10,20,50,100
        5.  a.Try clicking the up and down page number
            b.Enter a particular page no
        6.  Check whether the level ,type, detecting AP and Radio has a proper value displayed
        """
        log.info("Test Setup :")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        log.info("STEP 1 : Navigate to Monitoring ->Overview on all group level")
        log.info("#"*80)
        log.info("STEP 2.a : Select the group Navigate to Monitouoring ->WIDS  ")
        monitor_page.go_to_all_groups_page()
        monitor_page.go_to_default_group()
        self.LeftPanel.goto_monitoringPage()
        wids_page = self.LeftPanel.go_to_monitoring_wids_page()
        log.info("STEP 2.b : Select the group Navigate to Change Settings ")
        wireless_wids_page = wids_page.navigate_to_wids_change_setting()
        log.info("STEP 2.c Configure AP with WID level to different levels, all High")
        wireless_wids_page.set_detection_infra_threat_detection_level("High")
        wireless_wids_page.set_detection_clients_threat_detection_level("High")
        log.info("STEP 2.d Change wired containment to on and wireless containment to de-authenticate only")
        wireless_wids_page.set_infra_client_high()
        wireless_wids_page.wired_containment_on()
        wireless_wids_page.wireless_containment_deauthenticate()
        self.LeftPanel.goto_monitoringPage()
        self.LeftPanel.go_to_monitoring_wids_page()
        log.info("Step 3. Sleep for 5 minutes for even log to be generated ")
        time.sleep(300)
        log.info("STEP 3 : Try to filter based on the different options")
        log.info("STEP 3.1 : Level")
        wids_page.assert_search_table_by_field('LEVEL')
        log.info("STEP 3.1 : DESCRIPTION")
        wids_page.assert_search_table_by_field('DESCRIPTION')
        log.info("STEP 3.1 : TYPE")
        wids_page.assert_search_table_by_field('TYPE')
        log.info("STEP 3.1 : DETECTING AP")
        wids_page.assert_search_table_by_field('DETECTING AP')
        log.info("STEP 3.1 : VIRTUAL CONTROLLER")
        wids_page.assert_search_table_by_field('VIRTUAL CONTROLLER')
        log.info("STEP 3.1 : STATION MAC")
        wids_page.assert_search_table_by_field('STATION MAC')
        log.info("STEP 3.1 : RADIO")
        wids_page.assert_search_table_by_field('RADIO')
        monitor_page.wlan_table_enable_check()
        log.info("STEP 4: Change count on page to different levels")
        wids_page.select_value_per_page('5')
        wids_page.assert_value_per_page('5')
        wids_page.select_value_per_page('10')
        wids_page.assert_value_per_page('10')
        wids_page.select_value_per_page('20')
        wids_page.assert_value_per_page('20')
        wids_page.select_value_per_page('50')
        wids_page.assert_value_per_page('50')
        wids_page.select_value_per_page('100')
        wids_page.assert_value_per_page('100')
        wids_page.select_value_per_page('5')
        log.info("Assert page count selected")
        log.info("STEP 5a: Enter a particular page no. Page no randomly selected and checked")

        log.info("STEP 5b: Enter a particular page no. Page no randomly selected and checked")
        wids_page.assert_page_selected()
        self.LeftPanel.goto_monitoringPage()
        log.info("Tear Down: Restoring default values in wids page")
        self._set_ap_detection_and_protection_to_off()
        log.info("End of test case")
        
        
    def test_ath_11422_Edit_delete_Label(self):
        """
        ################################################################################################################
        NAME : Ramakrishnan R
        ################################################################################################################
        REQUIREMENT : 1 IAP
        RUNTIME     : 19 Minutes
        ################################################################################################################
        1
            Attach multiple IAP to athena using the below command in IAP console
        2
            Register multiple IAPs to different groups of athena
            a.Create more than 10 labels for each AP
            b.Create an existing label for another AP or for the same AP
            c.Delete the created labels
        ################################################################################################################
        """
        log.info("Test Setup :")
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()

        monitor_page = self.LeftPanel.go_to_monitoring_access_page()
        log.info("STEP 1")
        log.info("STEP 1.1 : Assuming Devices are attached ")
        log.info("#"*80)
        log.info("STEP 2 : Register multiple IAPs to different groups of athena")
        log.info("Assume an IAP is attached to default group")
        self.LeftPanel.go_to_monitoring_access_points()
        log.info("STEP 2.1 : Create more than 10 labels for each AP")
        monitor_page.add_multiple_label_to_ap("IAP_1", count=12)
        log.info("STEP 2.2 : Create an existing label for another AP or for the same AP")
        if not monitor_page.add_multiple_label_to_ap("IAP_1", count=2, check=True):
            log.info("Error thrown for Label already exists")
        else:
            log.error("Accepted duplicate Label name")
            assert False, "Accepted duplicate Label name"
        self.browser.refresh()
        self.LeftPanel.go_to_monitoring_access_points()
        log.info("STEP 2.3 : Delete the created labels")
        monitor_page.delete_label_from_ap("IAP_1", "LABEL1")
        log.info("CLEANUP :")
        self.browser.refresh()
        self.LeftPanel.go_to_monitoring_access_points()
        monitor_page.delete_all_label_from_ap("IAP_1")
        log.info("END OF TESTCASE : test_ath_11422_Edit_delete_Label")

    def test_ath_11473_Client_section(self):
        """
        ################################################################################################################
        NAME : Ramakrishnan R
        DATE : 3/6/2015
        ################################################################################################################
        REQUIREMENT : 1 IAP, 1 CLIENT, NETWORK WPA2-Personal (TEST_Monitoring, pwd : 123456789)
        RUNTIME     : 4 Minutes
        ################################################################################################################
        1
            Register multiple APs to different groups of athena
            Navigate to Monitoring ->Access point ->
            a.Click on any of the VC from the AP table
        2
            Associate clients with different OS to APs
            Navigate to Client section in AP details page of any VC
        ################################################################################################################
        """
        log.info("Test Setup :")
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        ssid_wpa2 = self.config.config_vars.monitoring_network
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_wpa2)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True, False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_wpa2)
        time.sleep(100)
        self.LeftPanel.go_to_monitoring_page()
        monitor_page = self.LeftPanel.go_to_monitoring_access_page()
        log.info("STEP 1")
        log.info("STEP 1.1 : Assuming Devices are attached ")
        log.info("#"*80)
        log.info("STEP 1.2 : Register multiple IAPs to different groups of athena")
        log.info("Assume an IAP is attached to default group")
        self.LeftPanel.go_to_monitoring_access_points()
        log.info("STEP 1.3 : Click on any of the VC from the AP table")
        monitor_page.go_to_vc_page()
        self.LeftPanel.go_to_monitoring_access_points()
        log.info("STEP 2.1 : Associate clients with different OS to APs")
        overview_page = self.LeftPanel.goto_monitoringPage()
        time.sleep(100)
        DeviceLibrary.connect_client_to_ap("Client_1", "TEST_Monitoring")
        time.sleep(150)
        log.info("STEP 2.2 : Navigate to Client section in AP details page of any VC")
        self.LeftPanel.go_to_monitoring_access_points()
        ap_detail_page = monitor_page.go_to_ap_page("IAP_1")
        #from athenataf.lib.functionality.page.monitoring.MonitoringAPDetailsPage import MonitoringAPDetailsPage
        ap_detail_page.verify_clients_table("Client_1")
        log.info("CLEANUP")
        self.LeftPanel.go_to_monitoring_page()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        log.info("END OF TESTCASE : test_ath_11473_Client_section")

    def test_ath_11394_check_non_default_values_in_overview_page(self):
        """
        ################################################################################################################
        REQUIREMENT : 1 IAP, 1 CLIENT, NETWORK WPA2-Personal (TEST_Monitoring, pwd : 123456789)
        RUNTIME     : 26 Minutes
        ################################################################################################################
        ################################################################################################################
        1
            1.Attach multiple IAP to athena using the below command in IAP console
        2
            Register multiple IAPs to different groups of athena
            a.Create labels for each AP
        3
            Try to filter based on the following options
            1.In AP- Type column  try searching for "AP-135"
            2.Only half of the MAC in name and VC
            3.Status is up or down
            4.Location is " Chennai" or "sunnyvale"
        4
            Associate clients to all the VCs registed to athena
        5
            Check flagged AP table
        :return:
        ################################################################################################################
        """
        log.info("TEST SETUP :")
        log.info("STEP 1 : Attach multiple IAP to athena using the below command in IAP console")
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        ssid_wpa2 = self.config.config_vars.monitoring_network
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_wpa2)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True, False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_wpa2)
        time.sleep(100)
        self.LeftPanel.go_to_monitoring_page()
        monitor_page = self.LeftPanel.go_to_monitoring_access_page()
        log.info("#"*80)
        log.info("STEP 2 : Assume an IAP is attached to default group")
        log.info("STEP 2.1 : Create labels for each AP")
        monitor_page.add_multiple_label_to_ap("IAP_1", count=1)
        monitor_page.assert_verification_of_multiple_label(1)
        log.info("#"*80)
        log.info("STEP 3 : Try to filter based on the different options")
        log.info("STEP 3.1 : AP-Type")
        monitor_page.display_elem_in_ap("type")
        monitor_page.search_ap_with_type()
        log.info("#"*80)
        log.info("STEP 3.2 : MAC/VC")
        monitor_page.display_elem_in_ap("vc")
        monitor_page.search_ap_with_name()
        monitor_page.search_ap_with_vc()
        log.info("#"*80)
        log.info("STEP 3.3 : STATUS")
        monitor_page.search_ap_with_status()
        log.info("#"*80)
        log.info("STEP 3.4 : LOCATION")
        monitor_page.search_ap_with_location()
        log.info("STEP 4.1 : Associate clients to all the VCs registed to athena")
        overview_page = self.LeftPanel.goto_monitoringPage()
        DeviceLibrary.connect_client_to_ap("Client_1", "TEST_Monitoring")
        DeviceLibrary.disconnect_client_from_ap("Client_1")
        #AP Cannot be moved to flagged by this way. Wrong TC.
        #time.sleep(1200)
        #self.LeftPanel.go_to_monitoring_access_points()
        #try:
        #    monitor_page.verify_flagged_ap_table("IAP_1")
        #except:
        #    log.error("AP IS NOT IN THE FLAGGED TABLE")
        log.info("CLEANUP :")
        self.browser.refresh()
        self.LeftPanel.go_to_monitoring_access_points()
        monitor_page.delete_all_label_from_ap("IAP_1")
        self.LeftPanel.go_to_monitoring_page()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        log.info("END OF TESTCASE : test_ath_11394_check_non_default_values_in_overview_page")

    def test_ath_11465_change_vc(self):
        """
        ################################################################################################################
        REQUIREMENT : 2 IAPs, Make them Swarm
        RUNTIME     : 9 Minutes
        ################################################################################################################
        ################################################################################################################
        1.Create one or more swarms with one master and multiple slaves
        2.Navigate to AP page ->Click on master AP MAC which will take us to the AP Details page.
        3.Shutdown the master of a swarm

        :return:
        ################################################################################################################
        """
        log.info("TEST SETUP :")
        log.info("STEP 1 : Create one or more swarms with one master and multiple slaves")
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()
        monitor_page = self.LeftPanel.go_to_monitoring_access_page()
        log.info("Assume swarm is created with 1 master and 1 slave")
        log.info("#"*80)
        log.info("STEP 2 : Navigate to AP page ->Click on master AP MAC which will take us to the AP Details page.")
        monitor_page.go_to_vc_page()
        monitor_page.assert_verification_of_vc_ap("IAP_1")
        log.info("#"*80)
        log.info("STEP 3 : Shutdown the master of a swarm")
        monitor_page.reboot_ap()
        time.sleep(60)
        monitor_page.set_default_device("IAP_2")
        DeviceLibrary.connect_device_to_server("IAP_2")
        time.sleep(40)
        #pdb.set_trace()
        self.LeftPanel.go_to_monitoring_access_points()
        time.sleep(100)
        self.browser.refresh()
        monitor_page.go_to_vc_page()
        monitor_page.assert_verification_of_vc_ap("IAP_2")
        log.info("#"*80)

    def test_ath_11395_Check_non_default_values_of_AP_Details_Page(self):
        """
        ################################################################################################################
        REQUIREMENT : 2 IAPs, Make them Swarm and 1 Client, NETWORK WPA2-Personal (TEST_Monitoring, pwd : 123456789)
        RUNTIME     : 26 Minutes
        ################################################################################################################
        ################################################################################################################
        1
            Register multiple APs to different groups of athena
            Navigate to Monitoring ->Access point ->
            a.Click on any of the VC from the AP table
        2
            a.Click on AP which is not the master of swarm from AP overview page
            b.Click on AP which is the master of swarm
        3
            AP MAP in AP details page
        4
            a.Add and Delete Clients to AP
            b.Induce Alerts to AP
            a.The client number should be changed accordingly
            b.The alerts should be displayed right.
        5
            Navigate to event logs which is at the bottom of AP details page
        ################################################################################################################
        """
        log.info("SETUP :")
        log.info("Assume IAPs are attached to athena")
        log.info("STEP 1 :")
        log.info("Register multiple APs to different groups of athena")
        log.info("STEP 1.1 : Navigate to Monitoring ->Access point ->")
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        ssid_wpa2 = self.config.config_vars.monitoring_network
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_wpa2)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True, False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_wpa2)
        time.sleep(100)
        self.LeftPanel.go_to_monitoring_page()
        access_point_page = self.LeftPanel.go_to_monitoring_access_page()
        #self.LeftPanel.go_to_monitoring_page()
        log.info("#"*80)
        log.info("STEP 1.2 : Click on any of the VC from the AP table")
        access_point_page.go_to_vc_page()
        access_point_page.assert_verification_of_vc_ap("IAP_1")
        log.info("#" * 80)
        log.info("STEP 2 :")
        log.info("STEP 2.1 : Click on AP which is not the master of swarm from AP overview page")
        self.LeftPanel.go_to_monitoring_access_points()
        access_point_page.go_to_non_vc_page()
        log.info("#" * 80)
        log.info("STEP 2.2 : Click on AP which is the master of swarm")
        self.LeftPanel.go_to_monitoring_access_points()
        access_point_page.go_to_vc_page()
        access_point_page.assert_verification_of_vc_ap("IAP_1")
        log.info("#" * 80)
        log.info("STEP 3 : Check AP MAP in AP details page")
        overview_page.check_ap_in_map("IAP_1")
        log.info("STEP 4.1 : Add and Delete Clients to AP")
        overview_page = self.LeftPanel.goto_monitoringPage()
        #self.LeftPanel.go_to_monitoring_access_points()
        DeviceLibrary.connect_client_to_ap("Client_1", "TEST_Monitoring")
        time.sleep(100)
        overview_page.assert_wifi_client_count(1)
        DeviceLibrary.disconnect_client_from_ap("Client_1")
        time.sleep(100)
        overview_page.assert_wifi_client_count(0)
        log.info("STEP 4.2 : Induce Alerts to AP")
        #self.LeftPanel.go_to_monitoring_access_points()
        #ap_details_page = access_point_page.go_to_ap_page("IAP_1")
        DeviceLibrary.disconnect_device_from_server("IAP_1")
        time.sleep(100)
        self.browser.refresh()
        self.LeftPanel.go_to_monitoring_access_points()
        ap_details_page = access_point_page.go_to_ap_page("IAP_1")
        ap_details_page.assert_latest_alert("IAP_1", "down")
        DeviceLibrary.connect_device_to_server("IAP_1")
        time.sleep(100)
        self.browser.refresh()
        self.LeftPanel.go_to_monitoring_access_points()
        ap_details_page = access_point_page.go_to_ap_page("IAP_1")
        ap_details_page.assert_latest_alert("IAP_1", "up")
        log.info("STEP 5.1 : Navigate to event logs which is at the bottom of AP details page")
        ap_details_page.assert_empty_event_log()
        ap_details_page.assert_tooltip_event_log()
        log.info("CLEANUP")
        self.LeftPanel.go_to_monitoring_page()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        log.info("END OF TESTCASE : test_ath_11395_Check_non_default_values_of_AP_Details_Page")


    def test_ath_11390_Check_AP_and_Client_count_in_different_scenarios(self):
        """
        ################################################################################################################
        REQUIREMENT : 2 IAPs, 1 in default and another in Group1 and 1 Client, NETWORK WPA2-Personal (TEST_Monitoring, pwd : 123456789)
        RUNTIME     : 26 Minutes
        ################################################################################################################
        1
            1.Attach multiple IAP to athena using the below command in IAP console
            debug-cloud-server <server name>
        2
            1.Register multiple IAPs to different groups of athena
            a.Navigate to Monitoring -> Overview on All Group level
            b.Navigate to Monitoring -> Overview on group level (check one after another group)
            c.Remove an AP from athena
            d. Add the AP back to athena
            e.Disconnect an client from IAP which is attached to athena
            f.Associate it back to IAP
        3
            a.Remove the AP with associated clients from Athena
            b.Add the AP back to Athena
            c.Move client from one AP to another AP ( both  APs are registered to Athena)
        4
            a.Check the client type matched with the clients associated
            b.Compare the client type chart in Overview page and in Client detail page
        5
            a. Inject Alerts on APs registered to Athena
            b.Monitor the Alert count on a All group level, Group level and a VC level
            c.Check the alerts count on the top of the page and in map
        6
            Navigate to Monitoring ->Overview->Alerts
         ################################################################################################################
        """
        log.info("SETUP")
        log.info("STEP 1 : Attach multiple IAP to athena using the below command in IAP console")
        log.info("Assume more than 1 IAP is attached in athena")

        log.info("STEP 2 : Register multiple IAPs to different groups of athena")
        log.info("STEP 2.1 : Navigate to Monitoring -> Overview on All Group level")
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        ssid_wpa2 = self.config.config_vars.monitoring_network
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_wpa2)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True, False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_wpa2)
        time.sleep(100)
        self.LeftPanel.go_to_monitoring_page()
        overview_page.go_to_all_groups_page()
        #self.LeftPanel.go_to_monitoring_page()
        overview_page.assert_ap_count_in_overview_page(2)
        overview_page.create_new_group("Group1", "test123")
        self.TopPanel.click_slider_icon()
        inner_left_panel = self.TopPanel.click_slider_icon()
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.move_vc_to_group("Group1", "IAP_2")
        time.sleep(300)
        DeviceLibrary.reconnect("IAP_2")
        self.LeftPanel.go_to_monitoring_page()
        log.info("STEP 2.1.1 : Navigate to Monitoring -> Overview on group level (check one after another group)")
        #self.LeftPanel.go_to_monitoring_page()
        #overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()
        overview_page.assert_ap_count_in_overview_page(1)
#
        log.info("STEP 2.1.2 : Remove an AP from athena")
        DeviceLibrary.disconnect_device_from_server("IAP_1")
        overview_page.assert_up_ap_count_in_overview_page(0)
        overview_page.assert_down_ap_count_in_overview_page(1)
#
        log.info("STEP 2.1.3 : Add an AP to athena")
        DeviceLibrary.connect_device_to_server("IAP_1")
        overview_page.assert_up_ap_count_in_overview_page(1)
        overview_page.assert_down_ap_count_in_overview_page(0)
#
        log.info("STEP 2.1.4 : Disconnect an client from IAP which is attached to athena")
        DeviceLibrary.disconnect_client_from_ap("Client_1")
        overview_page.assert_wifi_client_count(0)
#
        overview_page = self.LeftPanel.goto_monitoringPage()
        log.info("STEP 2.1.5 : Associate it back to IAP")
        time.sleep(100)
        DeviceLibrary.connect_client_to_ap("Client_1", "TEST_Monitoring")
        overview_page.assert_wifi_client_count(1)
#
        log.info("STEP 2.2.1 : Navigate to Monitoring -> Overview on group level (check one after another group)")
        #self.LeftPanel.go_to_monitoring_page()
        #overview_page.go_to_all_groups_page()
        self.LeftPanel.go_to_monitoring_page()

        overview_page.go_to_group_page("Group1")
#        overview_page.go_to_second_group()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        ssid_wpa2 = self.config.config_vars.monitoring_network1
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_wpa2)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True, False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_wpa2)
        time.sleep(100)
        self.LeftPanel.go_to_monitoring_page()
        overview_page.assert_ap_count_in_overview_page(1)
        DeviceLibrary.connect_client_to_ap("Client_1","TEST_Monitoring1")
#
        log.info("STEP 2.2.2 : Remove an AP from athena")
        import pdb
        #pdb.set_trace()
        DeviceLibrary.disconnect_device_from_server("IAP_2")
        overview_page.assert_up_ap_count_in_overview_page(0)
        overview_page.assert_down_ap_count_in_overview_page(1)
#
        log.info("STEP 2.2.3 : Add an AP to athena")
        DeviceLibrary.connect_device_to_server("IAP_2")
        overview_page.assert_up_ap_count_in_overview_page(1)
        overview_page.assert_down_ap_count_in_overview_page(0)
#
        log.info("STEP 2.2.4 : Disconnect an client from IAP which is attached to athena")
        DeviceLibrary.disconnect_client_from_ap("Client_1")
        overview_page.assert_wifi_client_count(0)
#
        log.info("STEP 2.2.5 : Associate it back to IAP")
        #overview_page.go_to_group_page("Group1")
        time.sleep(100)
        DeviceLibrary.connect_client_to_ap("Client_1", "TEST_Monitoring1")
        overview_page.assert_wifi_client_count(1)
#
        log.info("STEP 3.1 : Remove the AP with associated clients from Athena")
        self.LeftPanel.go_to_monitoring_page()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_group_page("Group1")
#
        DeviceLibrary.disconnect_device_from_server("IAP_2")
        overview_page.assert_up_ap_count_in_overview_page(0)
        overview_page.assert_down_ap_count_in_overview_page(1)
        overview_page.assert_wifi_client_count(0)
#
        log.info("STEP 3.2 : Add the AP back to Athena")
        DeviceLibrary.connect_device_to_server("IAP_2")
        overview_page.assert_up_ap_count_in_overview_page(1)
        overview_page.assert_down_ap_count_in_overview_page(0)
        #DeviceLibrary.disconnect_client_from_ap("Client_1", "TEST2")
        #overview_page.assert_wifi_client_count(1)
#
        log.info("STEP 3.3 : Move client from one AP to another AP both  APs are registered to Athena")
        time.sleep(100)
        DeviceLibrary.connect_client_to_ap("Client_1", "TEST_Monitoring1")
        self.LeftPanel.go_to_monitoring_page()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_group_page("Group1")
        overview_page.assert_wifi_client_count(1)
#
        DeviceLibrary.connect_client_to_ap("Client_1", "TEST_Monitoring")
        self.LeftPanel.go_to_monitoring_page()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()
        overview_page.assert_wifi_client_count(1)


        log.info("STEP 4.1 : Check the client type matched with the clients associated")
        overview_page = self.LeftPanel.goto_monitoringPage()
        monitoring_client_page = self.LeftPanel.go_to_monitoring_clients_page()
        monitoring_client_page.go_to_client_details_page("Client_1")
        monitoring_client_page.assert_client_type("Client_1")
        log.info("STEP 4.2 : Compare the client type chart in Overview page and in Client detail page")
        log.info("Not in the scope of automation")
        log.info("STEP 5.1 : Inject Alerts on APs registered to Athena")
        access_point_page = self.LeftPanel.go_to_monitoring_access_page()
        ap_details_page = access_point_page.go_to_ap_page("IAP_1")
        DeviceLibrary.disconnect_device_from_server("IAP_1")
        ap_details_page.assert_latest_alert("IAP_1", "down")
        log.info("Bringing the device up")
        DeviceLibrary.connect_device_to_server("IAP_1")
        ap_details_page.assert_latest_alert("IAP_1", "up")
        log.info("STEP 5.2 : Monitor the Alert count on a All group level, Group level and a VC level")
        #import pdb
        #pdb.set_trace()
        #overview_page = self.LeftPanel.goto_monitoringPage()
        self.LeftPanel.go_to_monitoring_page()
        overview_page.go_to_all_groups_page()
        count = overview_page.get_alert_count()
        DeviceLibrary.disconnect_device_from_server("IAP_1")
        log.info("Verifying Alert count : %s" %count)
        import re
        overview_page.assert_alert_count(re.sub(",", "", count))
        log.info("Alert in Group Level")
        #self.LeftPanel.go_to_monitoring_page()
        overview_page.go_to_default_group()
        count = overview_page.get_alert_count()
        DeviceLibrary.connect_device_to_server("IAP_1")
        #time.sleep(100)
        #self.browser.refresh()
        overview_page.assert_alert_count(re.sub(",", "", count))
        log.info("Alert in Swarm Level")
        overview_page.go_to_swarm_in_group("Group1")
        #self.LeftPanel.go_to_monitoring_page()
        #overview_page.go_to_all_groups_page()
        count = overview_page.get_alert_count()
        DeviceLibrary.disconnect_device_from_server("IAP_2")
        #time.sleep(100)
        #self.browser.refresh()
        overview_page.assert_alert_count(re.sub(",", "", count))
        log.info("CLEANUP")
        DeviceLibrary.connect_device_to_server("IAP_2")
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        overview_page.go_to_group_page("Group1")
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        inner_left_panel = self.TopPanel.click_slider_icon()
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.move_vc_to_group("default", "IAP_2")
        time.sleep(200)
        DeviceLibrary.reconnect("IAP_2")

        log.info("STEP 5.3 : Check the alerts count on the top of the page and in map")
        log.info("STEP 6.1 : Navigate to Monitoring ->Overview->Alerts")

    def test_ath_11483_Client_map(self):
        """
        ################################################################################################################
        REQUIREMENT : 1 IAP and 1 Client, NETWORK WPA2-Personal (TEST_Monitoring, pwd : 123456789)
        RUNTIME     : 6 Minutes
        ################################################################################################################

        ################################################################################################################

        1
            Register multiple IAPs to different groups of athena
            Change the location of AP
            Register AP from different locations
            Associate clients to it
        2
            Expand the map in Client detail page
            Zoom in and out

         ################################################################################################################
        """
        log.info("SETUP")
        log.info("#" * 80)
        log.info("STEP 1.1 : Register multiple IAPs to different groups of athena")
        log.info("Assume more than 1 IAP is attached in athena")
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()

        #overview_page.go_to_all_groups_page()
        #overview_page.go_to_default_group()

        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        ssid_wpa2 = self.config.config_vars.monitoring_network
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_wpa2)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True, False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_wpa2)
        time.sleep(100)
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.check_ap_in_map("IAP_1")
        log.info("#" * 80)
        log.info("STEP 1.2 : Change the location of AP")
        log.info("STEP 1.3 : Register AP from different locations")
        access_point_page = self.LeftPanel.go_to_monitoring_access_page()
        access_point_page.go_to_ap_page("IAP_1")
        access_point_page.check_ap_in_map("IAP_1")
        log.info("#" * 80)
        log.info("STEP 1.4 : Associate clients to it")
        DeviceLibrary.connect_client_to_ap("Client_1", "TEST_Monitoring")
        monitoring_client_page = self.LeftPanel.go_to_monitoring_clients_page()
        monitoring_client_page.go_to_client_details_page("Client_1")
        monitoring_client_page.check_client_in_map("Client_1")
        log.info("#" * 80)
        log.info("STEP 2.1 : Expand the map in Client detail page")
        monitoring_client_page.expand_map()
        log.info("#" * 80)
        log.info("STEP 2.2 : Zoom in and out")
        monitoring_client_page.map_zoom("zoom-in")
        monitoring_client_page.map_zoom("zoom-out")


    def test_ath_11405_Check_Client_and_throughput_graph(self):
        """
        ################################################################################################################
        REQUIREMENT : 2 IAPs and 1 Client, NETWORK WPA2-Personal (TEST_Monitoring in default Group and TEST_Monitoring1 in Group1, pwd : password)
        RUNTIME     : 27 Minutes
        ################################################################################################################
        ################################################################################################################
        1
            Associate clients to all the VCs registed to athena
            a.Remove a VC from athena
            b.Remove a client
            c.Register a VC associated clients to athena
            d.Register a VC with no clients to athena and then associate clients to it.
            e.Move clients between the VCs.
            f.Move APs between the VCs.
            g.click on 1h, 3h, 1d, 1w, 1y links
        2
            a.Send traffic on all the APs registered to athena
            b.click on 1h, 3h, 1d, 1w, 1y links
            c.Click the upstream and downstream links individually
        ################################################################################################################
        """
        log.info("SETUP")
        log.info("Assume IAPs are attached to athena")
        log.info("STEP 1.1 : Associate clients to all the VCs registed to athena")
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        ssid_wpa2 = self.config.config_vars.monitoring_network
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_wpa2)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True, False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_wpa2)

        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.go_to_all_groups_page()
        DeviceLibrary.connect_client_to_ap("Client_1", "TEST_Monitoring")
        log.info("#" * 80)
        log.info("STEP 1.2 : Remove a VC from athena")
        DeviceLibrary.disconnect_device_from_server("IAP_1")
        log.info("#" * 80)
        log.info("STEP 1.3 : Remove a client")
        DeviceLibrary.disconnect_client_from_ap("Client_1")
        time.sleep(500)
        overview_page.assert_wifi_client_count(0)
        log.info("#" * 80)
        overview_page = self.LeftPanel.goto_monitoringPage()
        log.info("STEP 1.4 : Register a VC associated clients to athena")
        DeviceLibrary.connect_device_to_server("IAP_1")
        time.sleep(60)
        DeviceLibrary.connect_client_to_ap("Client_1", "TEST_Monitoring")
        time.sleep(100)
        overview_page.assert_wifi_client_count(1)
        log.info("#" * 80)
        log.info("STEP 1.5 : Register a VC with no clients to athena and then associate clients to it")
        overview_page.create_new_group("Group1", "test123")
        self.TopPanel.click_slider_icon()
        inner_left_panel = self.TopPanel.click_slider_icon()
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.move_vc_to_group("Group1", "IAP_2")
        overview_page.go_to_group_page("Group1")
        time.sleep(200)
        DeviceLibrary.reconnect("IAP_2")
#        DeviceLibrary.connect_device_to_server("IAP_2")
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        ssid_wpa2 = self.config.config_vars.monitoring_network1
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_wpa2)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True, False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_wpa2)
        time.sleep(100)
        log.info("#" * 80)
        log.info("STEP 1.6 : Move clients between the VCs")
        self.LeftPanel.go_to_monitoring_page()
        DeviceLibrary.connect_client_to_ap("Client_1", "TEST_Monitoring1")
        time.sleep(200)
        overview_page.assert_wifi_client_count(1)
        log.info("#" * 80)
        log.info("STEP 1.7 : Move APs between the VCs")
        log.info("NEED TO TEST THIS STEP MANUALLY")
        log.info("STEP 2.1 : Send traffic on all the APs registered to athena")
        log.info("MANUALLY NEED TO SEND TRAFFIC")
        log.info("STEP 2.2 : click on 1h, 3h, 1d, 1w, 1y links")
        overview_page = self.LeftPanel.goto_monitoringPage()
        self.LeftPanel.go_to_monitoring_access_points()
        overview_page.select_timeline("1H")
        overview_page.select_timeline("3H")
        overview_page.select_timeline("1D")
        overview_page.select_timeline("1W")
        overview_page.select_timeline("1Y")
        log.info("#" * 80)
        log.info("STEP 2.3 : Click the upstream and downstream links individually")

        overview_page.graph_stream("upstream")
        overview_page.graph_stream("downstream")
        log.info("CLEANUP")
        inner_left_panel = self.TopPanel.click_slider_icon()
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.move_vc_to_group("default", "IAP_2")
        time.sleep(200)
        DeviceLibrary.reconnect("IAP_2")
        log.info("END OF TESTCASE ATH-11405")



    def test_ath_11498_Event_log_search_validation(self):
        """
        ################################################################################################################
        REQUIREMENT : 2 IAPs
        RUNTIME     : 27 Minutes
        ################################################################################################################
        ################################################################################################################
        1
           Register two IAP's say IAP1 and IAP2 to Athena
        2
            Login to central and create a groups Group A, then map IAP1 and IAP2 to Group A .
        3
            Select All groups and navigate to Monitoring -> Eventlog, dont scroll down the scroll bar.
        4
            Select Group A and navigate to Monitoring -> Eventlog
        5 
            Select All groups and navigate Monitoring -> Eventlog and then scroll down the scroll bar to next offset say next 200 lines.
        6 
            Select Group A and navigate to Monitoring -> Eventlog
        7 
            Select swarm under Group A i.e., IAP1 and navigate to Monitoring -> Eventlog
         ################################################################################################################
        """
        log.info("SETUP")
        log.info("#" * 80)
        log.info("STEP 1 : Register two IAP's say IAP1 and IAP2 to Athena")
        log.info("Assume two APs are attached to athena")
        log.info("STEP 2 : Login to central and create a groups Group A, then map IAP1 and IAP2 to Group A")
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()
        overview_page.create_new_group("GroupA", "test123")
        inner_left_panel = self.TopPanel.get_inner_left_panel()
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.move_all_ap_to_group("GroupA")
        time.sleep(200)
        DeviceLibrary.reconnect("IAP_1")
        DeviceLibrary.reconnect("IAP_2")
        log.info("STEP 3 : Select All groups and navigate to Monitoring -> Eventlog, dont scroll down the scroll bar.")
        overview_page.go_to_all_groups_page()
        event_log = self.LeftPanel.go_to_monitoring_event_log_page()
        event_log.display_mac_addr()
        event_log.assert_ap_event_log(["IAP_1", "IAP_2"])
        log.info("STEP 4 : Select Group A and navigate to Monitoring -> Eventlog")
        overview_page.go_to_all_groups_page()
        overview_page.go_to_group_page("GroupA")
        self.LeftPanel.go_to_monitoring_event_log()
        event_log.display_mac_addr()
        event_log.assert_ap_event_log(["IAP_1", "IAP_2"])
        log.info("STEP 5 : Select All groups and navigate Monitoring -> Eventlog and then scroll down the scroll bar to next offset say next 200 lines.")
        log.info("STEP 6 : Select Group A and navigate to Monitoring -> Eventlog")
        overview_page.go_to_all_groups_page()
        overview_page.go_to_group_page("GroupA")
        self.LeftPanel.go_to_monitoring_event_log()
        event_log.display_mac_addr()
        event_log.assert_ap_event_log(["IAP_1", "IAP_2"])
        log.info("STEP 7 : Select swarm under Group A i.e., IAP1 and navigate to Monitoring -> Eventlog")
        overview_page.go_to_all_groups_page()
        swarm = overview_page.go_to_swarm_in_group("GroupA")
        event_log.assert_swarm_event_log(swarm)
        log.info("CLEANUP")
        self.TopPanel.click_slider_icon()
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.move_all_ap_to_group("default")
        time.sleep(200)
        DeviceLibrary.reconnect("IAP_1")
        DeviceLibrary.reconnect("IAP_2")
        log.info("END OF TESTCASE : ATH-11498")

    def test_ath_11496_Client_throughput_check(self):
        """
        ################################################################################################################
        REQUIREMENT : 1 IAP and 1 Client
        RUNTIME     : 6 Minutes
        ################################################################################################################
        ################################################################################################################
        1
            Register multiple IAPs to athena and associate clients to it
            Send traffic on all the APs registered to athena
            Navigate to client Page and click on any clientsIt shpu
            click on 1h, 3h, 1d, 1w, 1y links
            Click the Inbound link
            Click the outbound link
        ################################################################################################################
        """
        log.info("SETUP")
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.go_to_default_group()
        log.info("STEP 1.1 : Register multiple IAPs to athena and associate clients to it")
        log.info("Assume multiple IAPs are attached with clients")
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        ssid_wpa2 = self.config.config_vars.monitoring_network
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_wpa2)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True, False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_wpa2)
        time.sleep(100)
        self.LeftPanel.go_to_monitoring_page()
        DeviceLibrary.connect_client_to_ap("Client_1", "TEST_Monitoring")
        log.info("STEP 1.2 : Send traffic on all the APs registered to athena")
        log.info("Assume traffic is started in clients")
        log.info("STEP 1.3 : Navigate to client Page and click on any clients throughput")
        overview_page.go_to_all_groups_page()
        client_page = self.LeftPanel.go_to_monitoring_clients_page()
        client_page.go_to_client_details_page("Client_1")
        log.info("#" * 80)
        log.info("STEP 1.4 : click on 1h, 3h, 1d, 1w, 1y links")
        client_page.select_timeline("1H")
        client_page.select_timeline("3H")
        client_page.select_timeline("1D")
        client_page.select_timeline("1W")
        client_page.select_timeline("1Y")
        log.info("#" * 80)
        log.info("STEP 1.5 : Click the Inbound link")
        client_page.graph_stream("inbound")
        log.info("#" * 80)
        log.info("STEP 1.6 : Click the outbound link")
        client_page.graph_stream("outbound")
        log.info("#" * 80)
        log.info("END OF TESTCASE : ATH-11496")

    def test_ath_11517_Check_alerts(self):
        """
        ################################################################################################################
        REQUIREMENT : 2 IAPs
        RUNTIME     : 6 Minutes
        ################################################################################################################
        ################################################################################################################
        1
            Register multiple IAPs to various groups of athena
            Check the alerts count
            Bring down one of the AP in the swam. Alert coulnt should go up by one. Mouse over the Alert count
            Bring down all the APs
        2
            Reattach the IAPs
        3
            Mouse over to the alert count under alerts
            Click on any of the MAC or alert count
        ################################################################################################################
        """
        log.info("SETUP")
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()
        log.info("STEP 1.1 : Register multiple IAPs to various groups of athena")
        log.info("Assume multiple IAPs are attached to different groups of Athena")
        log.info("STEP 1.2 : Check the alerts count")
        alert_count = int(overview_page.get_alert_count())
        log.info("#" * 80)
        log.info("STEP 1.3 : Bring down one of the AP in the swam. Alert count should go up by one. Mouse over the Alert count")
        DeviceLibrary.disconnect_device_from_server("IAP_1")
        time.sleep(200)
        #self.browser.refresh()
        overview_page.assert_alert_count(alert_count)
        #alert_count = int(overview_page.get_alert_count())
        log.info("Alert Count at this point after bringing one device down : %s" %alert_count)
        log.info("#" * 80)
        log.info("STEP 1.4 : Bring down all the APs")
        DeviceLibrary.disconnect_device_from_server("IAP_2")
        time.sleep(200)
        #self.browser.refresh()
        alert_count = alert_count + 1
        log.info("Alert Count at this point after bringing all devices down : %s" % alert_count)
        time.sleep(100)
        overview_page.assert_alert_count(alert_count)
        log.info("#" * 80)
        log.info("STEP 2.1 : Reattach the IAPs")
        DeviceLibrary.connect_device_to_server("IAP_1")
        time.sleep(200)
        #self.browser.refresh()
        alert_count = alert_count + 1
        log.info("Alert Count at this point after bringing up one devices  : %s" % alert_count)
        overview_page.assert_alert_count(alert_count)
        DeviceLibrary.connect_device_to_server("IAP_2")
        time.sleep(200)
        #self.browser.refresh()
        alert_count = alert_count + 1
        log.info("Alert Count at this point after bringing up all devices  : %s" % alert_count)
        overview_page.assert_alert_count(alert_count)
        log.info("#" * 80)
        log.info("STEP 2.2 : Mouse over to the alert count under alerts")
        log.info("STEP 2.3 : Click on any of the MAC or alert count")
        log.info("END OF TESTCASE : ATH-11517")

    def test_ath_11479_check_throughput_client_type_chart(self):
        """
        ################################################################################################################
        REQUIREMENT : 1 IAP and 1 Client
        RUNTIME     : 4.5 Minutes
        ################################################################################################################
        ################################################################################################################
        1
            Register multiple APs to different groups of athena
            Associate clients to all the VCs registed to athena
            Send traffic on all the APs registered to athena
            click on 1h, 3h, 1d, 1w, 1y links
            Click the upstream and downstream links individually
        2
            Check the client type chart matched with the clients assoicated
            Compare the client type chart in Overview page and in Client detail page
        ################################################################################################################
        """
        log.info("SETUP")
        log.info("STEP 1.1 : Register multiple APs to different groups of athena")
        log.info("STEP 1.2 : Associate clients to all the VCs registered to athena")
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        ssid_wpa2 = self.config.config_vars.monitoring_network
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_wpa2)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True, False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_wpa2)
        time.sleep(100)
        self.LeftPanel.go_to_monitoring_page()
        DeviceLibrary.connect_client_to_ap("Client_1", "TEST_Monitoring")
        log.info("#" * 80)
        log.info("STEP 1.3 : Send traffic on all the APs registered to athena")
        log.info("Manually send data from the client")
        log.info("STEP 1.4 : click on 1h, 3h, 1d, 1w, 1y links")
        client_page = self.LeftPanel.go_to_monitoring_clients_page()
        client_page.select_timeline("1H")
        client_page.select_timeline("3H")
        client_page.select_timeline("1D")
        client_page.select_timeline("1W")
        client_page.select_timeline("1Y")
        log.info("#" * 80)
        log.info("STEP 1.5 : Click the upstream and downstream links individually")
        client_page = self.LeftPanel.go_to_monitoring_clients_page()
        client_page.graph_stream_overview_page("upstream")
        client_page.graph_stream_overview_page("downstream")
        log.info("STEP 2.1 : Check the client type chart matched with the clients assoicated")
        log.info("STEP 2.2 : Compare the client type chart in Overview page and in Client detail page")
        log.info("END OF TESTCASE : ATH-11479")

    def test_ath_11476_checking_labels(self):
        """
        ################################################################################################################
        NAME : Arunkarthick A
        DATE : 3/9/2015
        Register multiple IAPs to different groups of athena
            a.Create one/two/three labels for each AP

            b.Associate clients to those APs

            c.Navigate to Monitoring ->Clients

            d.Delete the created labels
        ################################################################################################################
        """
        log.info("Test Setup :")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        log.info("Assuming Devices are attached ")
        log.info("#"*80)
        log.info("Register multiple IAPs to different groups of athena:")
        log.info("Assume an IAP is attached to default group")
        access_page = self.LeftPanel.go_to_monitoring_access_page()
        access_page.delete_all_label_from_ap("IAP_1")
        log.info("STEP 1 : Create one/two/three labels for each AP")
        access_page.add_multiple_label_to_ap("IAP_1", 3)
        
        log.info("Verify the created label on each AP")
        access_page.assert_verification_of_multiple_label(3)

        
        log.info("STEP 2 : Associate clients to those APs")






































        self.browser.refresh()
        self.LeftPanel.go_to_monitoring_access_points()
        log.info("STEP 3 : Navigate to Monitoring ->Clients")


        log.info("STEP 4 : Delete the created labels")
        #monitor_page.delete_label_from_ap("IAP_1", "LABEL1")
        log.info("CLEANUP :")
        self.browser.refresh()
        self.LeftPanel.go_to_monitoring_access_points()
        access_page.delete_all_label_from_ap("IAP_1")
        log.info("END OF TESTCASE : test_ath_11476_Edit_delete_Label")

    def test_ath_11472_verify_wired_and_wireless_interfaces_table(self):
        """
        ################################################################################################################



        NAME : Arunkarthick A
        DATE : 3/9/2015
        1. Register multiple APs to different groups of athena 
        Navigate to Monitoring ->Access point ->
        a.Click on any of the VC from the AP table
            
        2.  Navigate to wired interface column
        
        3. Navigate to wireless interface column
        a.Create multiple SSIDs on IAP 
        b.Associate/disassociate clients to AP
        c.Change the TX power on AP
        ################################################################################################################















        """
        log.info("Test Setup :")


        monitor_page = self.LeftPanel.goto_monitoringPage()
        log.info("Assuming Devices are attached ")
        log.info("#"*80)
        log.info("Register multiple IAPs to different groups of athena:")
        log.info("Assume an IAP is attached to default group")

        log.info("STEP 1: Navigate to Monitoring ->Access point -> Click on any of the VC from the AP table")
        access_points_page = self.LeftPanel.go_to_monitoring_access_page()











        log.info("Click on the first VC from the AP table")
        access_point = access_points_page.get_access_point()
        ap_details_page = access_points_page.goto_ap_details_page()
        ap_details_page.verify_ap_details_page(access_point)
        log.info("#"*80)
        
        log.info("STEP 2: Navigate to wired interface column")
        ap_details_page.verify_wired_interface_table()
        log.info("#"*80)
        
        log.info("STEP 3: Navigate to wireless interface column")
        ap_details_page.verify_wireless_interface_table()
        log.info("#"*80)
        log.info("STEP 3.a: Create multiple SSIDs on IAP then Navigate to wireless interface column")
        log.info("Get the initial number of ssids before creating the multiple ssids")
        new_ssids = 4
        log.info("Create the %d ssids" %new_ssids)
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        for i in range(new_ssids):
            ssid_name = "ssid_%s" %i
            basic_info = self.NetworkPage.create_new_network()
            virtual_lan = basic_info.employee_network_info(ssid_name)
            security = virtual_lan.use_vlan_defaults()
            access = security.assert_roaming_defaults(True,False)
            access.finish_network_setup()
            self.NetworkPage.assert_new_network(ssid_name)
        
        log.info("Verify the ssids count in AP Details page")
        self.LeftPanel.go_to_monitoring_page()
        self.LeftPanel.go_to_monitoring_access_page()
        access_points_page.go_to_ap_details_page()






        log.info("wait for 120 seconds to update the new ssids in ap details page")
        time.sleep(120)
        self.browser.refresh()
        access_points_page.go_to_ap_details_page()
        current_ssids_count = ap_details_page.get_ssids_count_from_ap_details_wireless_interface_table()
        if new_ssids == current_ssids_count:
            log.info("PASS: All the %d newly created SSIDs are updated at Wireless instance table in AP Details page." %new_ssids)
        else:
            log.info("FAIL: Expected ssids count - %d , Existing ssids count - %d" %(new_ssids,current_ssids_count))
            raise AssertionError("SSIDs count is not updated at wireless interface table.")      
        log.info("Delete the newly created %d ssids" %new_ssids)
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        log.info("#"*80)
        
        log.info("STEP 3.b: Associate/disassociate clients to AP")
        log.info("STEP 3.c: Change the TX power on AP")
        log.info("Configure max and min TX powers")
        self.LeftPanel.goto_configuration_page()
        rf_page = self.LeftPanel.go_to_rf_page()












        max_tx_power = self.config.config_vars.maximum_transmit_power_value
        min_tx_power = self.config.config_vars.minimum_transmit_power_value
        rf_page.modify_transit_power(False,min_tx_power)
        rf_page.modify_transit_power(True,max_tx_power)
        log.info("wait for 90 seconds to update the TX power in ap details page")
        time.sleep(90)
        self.browser.refresh()
        log.info("Verify TX power in AP details page")
        self.LeftPanel.go_to_monitoring_page()
        self.LeftPanel.go_to_monitoring_access_page()
        access_points_page.go_to_ap_details_page()
        existing_tx_power = ap_details_page.get_tx_power_from_wireless_interface_table()
        if existing_tx_power <= int(max_tx_power) and existing_tx_power >= int(min_tx_power):
            log.info("PASS: Existing tx power - %d is between configured max - %s and min - %s powers" %(existing_tx_power,max_tx_power,min_tx_power))
        else:
            log.info("FAIL: Existing tx power - %d is not between configured max - %s and min - %s powers" %(existing_tx_power,max_tx_power,min_tx_power))
            raise AssertionError("TX Power is not updated at wireless interface table.")
        log.info("Unconfigure max and min TX powers")
        self.LeftPanel.goto_configuration_page()
        self.LeftPanel.go_to_rf_page()
        rf_page.set_access_point_control_values_to_default()
        log.info("#"*80)
        log.info("END OF TESTCASE : test_ath_11472_verify_wired_and_wireless_interfaces_table")

    def test_ath_11469_check_help_text(self):
        """
        ################################################################################################################


        NAME : Arunkarthick A
        DATE : 3/17/2015
        1 Navigate to Monitoring ->Access point ->
        a.Click on any of the VC from the AP table
        b.Enable help which will look like a Question mark next to Notifications
        ################################################################################################################
        """
        log.info("Test Setup :")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        log.info("Assuming Devices are attached ")
        log.info("#"*80)
        log.info("Register multiple IAPs to different groups of athena:")
        log.info("Assume an IAP is attached to default group")
        log.info("Navigate to Monitoring ->Access point -> Click on any of the VC from the AP table")
        access_points_page = self.LeftPanel.go_to_monitoring_access_page()
        log.info("Click on the first VC from the AP table")
        access_point = access_points_page.get_access_point()
        ap_details_page = access_points_page.goto_ap_details_page()
        ap_details_page.verify_ap_details_page(access_point)
        log.info("Click/Enable the Help")
        ap_details_page.enable_help()
        log.info("Verify the Help text for the help enabled elements")
        help_elements = ["reboot_ap_button", "console_access_button", "device_status", "connected_clients", \
            "uplink_type", "alerts", "client_type_distribution", "aggregate", "2_4_ghz", "5_ghz", "wired_interface_mac_address",\
            "wired_interface_status", "wired_interface_link_type", "wired_interface_duplex_mode", "wireless_interface_radio_type",\
            "wireless_interface_status", "wireless_interface_clients", "wireless_interface_ssids", "wireless_interface_channel", \
            "wireless_interface_tx_power", "wireless_interface_antenna_type", "wireless_interface_role", "clients_os", \
            "clients_network", "clients_channel", "clients_type", "clients_role"]
        ap_details_page.assert_help_options(help_elements)
        log.info("Disable the Help")
        ap_details_page.disable_help()
        log.info("#"*80)
        log.info("END OF TESTCASE : test_ath_11469_check_help_text")
    
    def test_ath_11487_check_help_text(self):
        """
        ################################################################################################################







        NAME : Arunkarthick A
        DATE : 3/17/2015
        1 a.Navigate to Monitoring ->WIDS
        b.Enable help which will look like a Question mark next to Notifications
        ################################################################################################################
        """
        log.info("Test Setup :")
        monitor_page = self.LeftPanel.goto_monitoringPage()






















        log.info("Navigate to Monitoring ->WIDS")
        wids_page = self.LeftPanel.go_to_monitoring_wids_page()
        log.info("Click/Enable the Help")
        wids_page.enable_help()
        log.info("Verify the Help text for the help enabled elements")
        help_elements = ["rogue_aps_label", "interfering_aps_label", "infrastructure_attacks_label", "client_attacks_label",\
            "ap_type", "ids_attack_detected", "wids_events_description"]
        wids_page.assert_help_options(help_elements)
        log.info("Disable the Help")
        wids_page.disable_help()
        log.info("#"*80)
        log.info("END OF TESTCASE : test_ath_11487_check_help_text")

        
    def test_ath_11499_check_help_text(self):
        """
        ################################################################################################################


        NAME : Arunkarthick A
        DATE : 3/17/2015
        1 a.Navigate to Monitoring ->Event logs
        b.Enable help which will look like a Question mark next to Notifications
        ################################################################################################################
        """
        log.info("Test Setup :")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        log.info("Navigate to Monitoring ->WIDS")
        event_log_page = self.LeftPanel.go_to_monitoring_event_log_page()
        log.info("Click/Enable the Help")
        event_log_page.enable_help()
        log.info("Verify the Help text for the help enabled elements")
        help_elements = ["date_time", "hostname", "mac_address", "device_type", "event_type", "description"]
        event_log_page.assert_help_options(help_elements)
        log.info("Disable the Help")
        event_log_page.disable_help()
        log.info("#"*80)
        log.info("END OF TESTCASE : test_ath_11499_check_help_text")
        
    def test_ath_11477_check_help_text(self):
        """
        ################################################################################################################
        NAME : Arunkarthick A
        DATE : 3/17/2015
        1 a.Navigate to Monitoring ->Clients 
        b.Enable help which will look like a Question mark next to Notifications
        ################################################################################################################
        """
        log.info("Test Setup :")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        log.info("Navigate to Monitoring ->Clients")
        monitoring_client_page = self.LeftPanel.go_to_monitoring_clients_page()
        log.info("Click/Enable the Help")
        monitoring_client_page.enable_help()
        log.info("Verify the Help text for the help enabled elements")
        #missing: signal
        help_elements = ["flagged", "throughput", "mac_address", "ip_address", \
                        "table_mac_address", "table_ip_address", \
                        "table_host_name","table_connected_to", "table_ssid", \
                        "table_connection", "table_label"]
        monitoring_client_page.assert_help_options(help_elements)
        log.info("Disable the Help")
        monitoring_client_page.disable_help()
        log.info("#"*80)
        log.info("END OF TESTCASE : test_ath_11477_check_help_text")

        
    def test_ath_11478_check_help_text(self):
        """
        ################################################################################################################


        NAME : Arunkarthick A
        DATE : 3/17/2015
        1 a.Navigate to Monitoring ->Clients ,click on any of the client
        b.Enable help which will look like a Question mark next to Notifications
        ################################################################################################################
        """
        monitor_page = self.LeftPanel.goto_monitoringPage()
        log.info("Create the network to connect client")
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        network_name = "ssid_0"
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(network_name)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True,False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(network_name)
        self.browser.refresh()
        time.sleep(180)
        monitor_page.assert_network_in_ap("IAP_1", network_name)
        
        log.info("Connect client with network")
        monitor_page.connect_client_to_ap("Client_1", network_name)
        time.sleep(180)
                

        log.info("Navigate to Monitoring ->Clients")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        monitoring_client_page = self.LeftPanel.go_to_monitoring_clients_page()
        monitoring_client_page.go_to_client_details_page("Client_1")
        log.info("Click/Enable the Help")
        monitoring_client_page.enable_help()
        log.info("Verify the Help text for the help enabled elements")
        #outbound
        help_elements = ["signal", "speed", "ap_ssid", "alerts", "inbound"]
        monitoring_client_page.assert_help_options_client_details(help_elements)
        
        log.info("Unconfigurations")
        log.info("Disable the Help")
        monitoring_client_page.disable_help()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        log.info("END OF TESTCASE : test_ath_11478_check_help_text")
##        
    def test_ath_11513_search_for_ssid_and_label(self):
        """
        ################################################################################################################
        NAME : Arunkarthick A
        DATE : 3/27/2015
        1 Create group 1 and group 2 
        b. Attach 1 VC to each group
        c.Create 3 to 4 networks for each group with different names as shown below and have one common name.
        group 1 
        "Aruba"
        "IAP"
        "ABCD"
        "ABCD123"
        d.Once the networks are created, try searching the SSID from global search
        
        2 Try to search the SSID using half the name or with one or two characters etc
        
        3 Register multiple IAPs to different groups of athena 
        a.Create more than 10 labels for each AP which includes numbers, alphanumeric labels.
        
        4 a.search for abcd in label
        b.search for bc string
        c.search for 12 in label string
        d.search for bc1 in label string
        ################################################################################################################
        """
        log.info("Create 3 to 4 networks for each group with different names as shown below and have one common name.")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        networks_list = ["Aruba", "IAP", "ABCD", "ABCD123"]
        for network_name in networks_list:
            basic_info = self.NetworkPage.create_new_network()
            virtual_lan = basic_info.employee_network_info(network_name)
            security = virtual_lan.use_vlan_defaults()
            access = security.assert_roaming_defaults(True,False)
            access.finish_network_setup()
            self.NetworkPage.assert_new_network(network_name)
        log.info("STEP 1.d: Try searching the SSID from global search")
        self.LeftPanel.go_to_monitoring_page()
        for network_name in networks_list:
            monitor_page.verify_global_search(network_name,"NETWORKS",network_name)
        
        log.info("Try to search the SSID using half the name or with one or two characters etc")
        log.info("Half the name")
        for network_name in networks_list:
            monitor_page.verify_global_search(network_name[0:len(network_name)/2],"NETWORKS",network_name)
        log.info("One character")
        for network_name in networks_list:
            monitor_page.verify_global_search(network_name[0],"NETWORKS",network_name)
        log.info("Two characters")
        for network_name in networks_list:
            monitor_page.verify_global_search(network_name[0:1],"NETWORKS",network_name)
        
        log.info("Delete all the labels")
        access_page = self.LeftPanel.go_to_monitoring_access_page()
        access_page.delete_all_label_from_ap("IAP_1")
        log.info("Create more than 10 labels")
        labels_list = ["FIRST123", "SECOND234", "THIRD345", "FOUR456", "FIVE567",\
            "SIX678", "SEVEN789", "EIGHT890", "NINE901", "TEN012", "ELEVEN321"]
        for label in labels_list:
            access_page.add_label_by_variable_name_length("IAP_1",label)
        log.info("Enter the complete label string in the search box.")
        for label in labels_list:
            monitor_page.verify_global_search(label,"LABELS",label)
        log.info("search for alphabetic letters in label")
        for label in labels_list:
            monitor_page.verify_global_search(label[0:-3],"LABELS",label)
        log.info("search for numbers in label string")
        for label in labels_list:
            monitor_page.verify_global_search(label[-3:-1],"LABELS",label)
        log.info("search for alpha-numeric in label string")
        for label in labels_list:
            monitor_page.verify_global_search(label[-5:-1],"LABELS",label)
        
        log.info("Unconfigurations")
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        self.LeftPanel.go_to_monitoring_page()
        self.LeftPanel.go_to_monitoring_access_points()
        access_page.delete_all_label_from_ap("IAP_1")
        log.info("END OF TESTCASE : test_ath_11513_search_for_ssid_and_label")
    
    
    def test_ath_11514_search_for_ap_and_client_name(self):
        """
        ################################################################################################################
        NAME : Arunkarthick A
        DATE : 3/27/2015
        1a. Create a label for an AP. Enter the complete and partial label string in the search box.
        b.Search on a SSID configured.
        c.Search on AP name
        d.Search on CLinet name
        e.Search on ip address
        f.Search on status of AP
        g.Search on event type, level, description
        ################################################################################################################
        """
        log.info("STEP 1.a : Create a label for an AP. Enter the complete and partial label string in the search box.")


        monitor_page = self.LeftPanel.goto_monitoringPage()





        access_page = self.LeftPanel.go_to_monitoring_access_page()
        access_page.delete_all_label_from_ap("IAP_1")
        label = "FIRST_LABEL"
        access_page.add_label_by_variable_name_length("IAP_1",label)
        log.info("Enter the complete label string in the search box.")
        monitor_page.verify_global_search(label,"LABELS",label)
        log.info("Enter the partial label string in the search box.")
        monitor_page.verify_global_search(label[0:len(label)/2],"LABELS",label)
        
        log.info("STEP 1.b : Search on a SSID configured.")
        self.LeftPanel.go_to_network_page()











        self.NetworkPage.delete_all_networks()
        network_name = "ssid_0"
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(network_name)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True,False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(network_name)
        self.browser.refresh()
        time.sleep(180)
        monitor_page.assert_network_in_ap("IAP_1", network_name)
        log.info("Try searching the SSID from global search")
        self.LeftPanel.go_to_monitoring_page()
        monitor_page.verify_global_search(network_name,"NETWORKS",network_name)
        
        log.info("STEP 1.c: Search on AP name")
        device_name = "IAP_1"
        self.device = getattr(devices, device_name)
        monitor_page.verify_global_search(self.device.mac,"AP",self.device.mac)
                
        log.info("STEP 1.d:Search on Client name")
        client_name = "Client_1"
        self.client = getattr(devices, client_name)
        monitor_page.connect_client_to_ap(client_name, network_name)
        time.sleep(180)
        self.browser.refresh()
        monitor_page.verify_global_search(self.client.mac,"CLIENTS",self.client.mac)
        
        log.info("STEP 1.e:Search on ip address")
        monitor_page.verify_global_search(self.device.ip,"AP",self.device.ip)
        
        log.info("STEP 1.f:Search on status of AP")
        monitor_page.verify_global_search("Up","AP",self.device.mac)
        
        log.info("STEP 1.g:Search on event type, level, description")
        monitor_page.verify_global_search("Security","EVENTS","Event Type : security")
        monitor_page.verify_global_search("Normal","EVENTS","Level : normal")
        monitor_page.verify_global_search("connected","EVENTS","Event Type")
        
        log.info("Unconfigurations")
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        self.LeftPanel.go_to_monitoring_page()
        self.LeftPanel.go_to_monitoring_access_points()
        access_page.delete_all_label_from_ap("IAP_1")
        log.info("END OF TESTCASE : test_ath_11514_search_for_ap_and_client_name")

