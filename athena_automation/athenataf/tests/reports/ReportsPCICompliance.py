__author__ = 'aarunakirisamy'
import logging
log = logging.getLogger('athenataf')
import pdb
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest
from athenataf.lib.functionality.common import DeviceLibrary
from Device_Module.ObjectModule import Device
from athenataf.lib.functionality.test.ReportsTest import ReportsTest
import time

class ReportsPCICompliance(ConfigurationTest, ReportsTest):
    def test_ath_9015_9016_run_report_now_and_later(self):
        """
        ################################################################################################################
        NAME : Arunkarthick A
        DATE : 4/06/2015
        ATH-9015:Run Report now
        1 Create a non-periodic report with Run Report set to "now".
        2 Create daily periodic report with "Run Report" set to now.
        ################################################################################################################
        """
        log.info("Create the CDE ssid for PCI compliance")
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        ssid_name = self.config.config_vars.Network_name
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_name)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True,False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_name)
        
        log.info("Go To Monitoring => Overview Page")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        monitor_page.assert_new_network_in_monitoring(ssid_name)
        


        log.info("Go To Reports => PCI compliance Page")
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        log.info("Delete all the existing reports before ")
        pci_compliance_page.go_to_all_groups_page()
        pci_compliance_page.delete_all_reports()

        log.info("STEP 1:Create a non-periodic report with Run Report set to 'now'")
        report1 = pci_compliance_page.create_pci_compliance_report("now",self.config.config_vars.one_time,"cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report1)
        
        log.info("STEP 2:Create a periodic report with Run Report set to 'now'")
        report2 = pci_compliance_page.create_pci_compliance_report("now",self.config.config_vars.repeat_daily_interval,"cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report2)
        log.info("Verify Another report should be scheduled for the periodic report")
        report3 = report2 + 1
        pci_compliance_page.verify_report_generation(report3,"Scheduled")
        log.info("Unconfigurations: Delete all the created reports")
        pci_compliance_page.delete_all_reports()
        
        log.info("ATH-9016 - run_report_schedule_for_later")
        log.info("Create a non-periodic report with Run Report set to Later")
        report1 = pci_compliance_page.create_pci_compliance_report("Later",self.config.config_vars.one_time,"cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report1,"Scheduled")
        
        log.info("Unconfigurations: Delete all the created reports")
        pci_compliance_page.delete_all_reports()
        pci_compliance_page.go_to_default_group()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        
        log.info("END OF TEST CASE - test_ath_9015_9016_run_report_schedule_for_later")
    
    def test_ath_8337_factory_default_values(self):
        """
        ################################################################################################################
        NAME : Ramakrishnan R
        DATE : 4/08/2015
        ################################################################################################################
            REQUIREMENT : 1 IAP and only default group without any network
            RUNTIME     : 4 Minutes
        ################################################################################################################
        ATH-8337:Factory default values
        1. Do write erase all on one of the APs associated to a customer.
        2. Run PCI report on this device for SSID instant.
        ################################################################################################################
        """
        log.info("SETUP")
        log.info("Assume IAPs attached to the athena with customer")
        log.info("STEP 1 : Do write erase all on one of the APs associated to a customer.")
        DeviceLibrary.write_erase_all("IAP_1")
        DeviceLibrary.reload("IAP_1")
        time.sleep(300)
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        report1 = pci_compliance_page.create_pci_compliance_report("now", self.config.config_vars.one_time, "cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report1)
        pci_compliance_page.go_to_first_report()
        pci_compliance_page.assert_negative_pci_table("2.1.1")
        log.info("END OF TESTCASE : ATH-8337")


    def test_ath_8342_Check_11_1_11_4(self):
        """
        ################################################################################################################
        NAME : Ramakrishnan R
        DATE : 4/09/2015
        ################################################################################################################
            REQUIREMENT : 1 IAP attached to default group
            RUNTIME     : 6 Minutes
        ################################################################################################################
        ATH-8337:Factory default values
        1  Configure a group with scanning disabled and run PCI report on that group.
        2  now enable the scanning on that group and run PCI report again.
        3  Create multiple groups and configure some with scanning and some with disabled. Run PCI report on all the SSID from all group level.
        ################################################################################################################
        """
        conf = self.config.config_vars
        log.info("SETUP")
        log.info("Assume IAPs attached to the athena with customer")
        log.info("STEP 1 : Configure a group with scanning disabled and run PCI report on that group.")
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.create_new_group("GroupA", "test123")
        inner_left_panel = self.TopPanel.get_inner_left_panel()
        manage_group_page = inner_left_panel.manage_group()
        #manage_group_page.delete_empty_groups()
        manage_group_page.move_vc_to_group("GroupA", "IAP_1")
        overview_page.go_to_group_page("GroupA")
        time.sleep(200)
        DeviceLibrary.reconnect("IAP_1")
        log.info("Create the CDE ssid for PCI compliation")
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        ssid_name = conf.Network_name
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_name)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True, False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_name)
        time.sleep(300)
        rf_page = self.LeftPanel.go_to_rf_page()
        rf_page.assert_scanning_options()
        rf_page.set_rf_arm_access_point_control_scanning(conf.new_scanning_value)
        try:
            rf_page.assert_save_settings_button()
            rf_page.save_settings.click()
        except:
            pass
#        time.sleep(500)
        #DeviceLibrary.write_erase_all("IAP_1")
        #DeviceLibrary.reload("IAP_1")
        log.info("Go To Reports => PCI compliance Page")
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        log.info("Delete all the existing reports before ")
        pci_compliance_page.delete_all_reports()
        log.info("Create a non-periodic report with Run Report set to 'now'")
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        time.sleep(300)
        report1 = pci_compliance_page.create_pci_compliance_report("now", self.config.config_vars.one_time, "cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report1)
        pci_compliance_page.go_to_first_report()
        pci_compliance_page.assert_negative_pci_table(["11.1", "11.4"])
        self.LeftPanel.goto_configuration_page()
        rf_page = self.LeftPanel.go_to_rf_page()
        rf_page.assert_scanning_options()
        rf_page.set_rf_arm_access_point_control_scanning(conf.enable_scanning)
        try:
            rf_page.assert_save_settings_button()
            rf_page.save_settings.click()
        except:
            pass
        time.sleep(100)
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        pci_compliance_page.delete_all_reports()
        report1 = pci_compliance_page.create_pci_compliance_report("now", self.config.config_vars.one_time, "cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report1)
        pci_compliance_page.go_to_first_report()
        pci_compliance_page.assert_pci_table(["11.1", "11.4"])
        log.info("CLEANUP")
        self.LeftPanel.go_to_monitoring_page()
        inner_left_panel = self.TopPanel.click_slider_icon()
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.move_vc_to_group("default", "IAP_1")
        time.sleep(300)
        DeviceLibrary.reconnect("IAP_1")
        log.info("END OF TESTCASE : ATH-8342")

    def test_ath_1707_run_report_now(self):
        """

        1.1Configure multiple SSIDs in a VC.
        1.2Configure one with authentication WPA2 and one with Static WEP.
        1.3Run PCI report by selecting both the SSIDs

        2.1 Run PCI report on SSID with static WEP configuration
        2.2 Run PCI report on SSID with WPA2 configuration


        """
        log.info("Test Setup :")
        log.info("STEP 1")
        log.info("Deleting Network if present")

        log.info("Create the CDE ssid for PCI compliation")
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()
        self.LeftPanel.go_to_network_page()

        self.NetworkPage.delete_all_networks()

        ssid_wpa2 = self.config.config_vars.Network_name
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_wpa2)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True, False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_wpa2)

        ssid_wep = "test3"
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_wep)
        security = virtual_lan.use_vlan_defaults()
        security.set_security_level_and_key_management("Personal")
        access = security.use_security_default()
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_wep)

        log.info("Navigating to Reports Page")
        self.LeftPanel.go_to_reports_page()
        log.info("Waiting for the network to be be displayed in reports page")

        monitor_page = self.LeftPanel.goto_monitoringPage()
        monitor_page.assert_new_network_in_monitoring(ssid_wpa2)
        monitor_page.assert_new_network_in_monitoring(ssid_wep)

        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        log.info("STEP: Run PCI report on SSID with static WEP and WAP configuration")
        report_number = pci_compliance_page.create_pci_compliance_report("now", self.config.config_vars.one_time, "cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report_number)
        pci_compliance_page.go_to_report_details(report_number)
        pci_compliance_page.assert_negative_pci_table("4.1.1")
        self.LeftPanel.go_to_reports_pci_compliance()
        pci_compliance_page.delete_all_reports()
        log.info("STEP: Run PCI report on SSID with  WAP configuration")
        report_number = pci_compliance_page.create_pci_compliance_report("now",self.config.config_vars.one_time, "cde_ssids","test1")
        pci_compliance_page.verify_report_generation(report_number)

        pci_compliance_page.go_to_report_details(report_number)
        pci_compliance_page.assert_pci_table("4.1.1")
        self.LeftPanel.go_to_reports_pci_compliance()
        pci_compliance_page.delete_all_reports()
        log.info("STEP: Run PCI report on SSID with static WEP configuration")
        report_number = pci_compliance_page.create_pci_compliance_report("now", self.config.config_vars.one_time,"cde_ssids",ssid_wep)

        pci_compliance_page.verify_report_generation(report_number)

        pci_compliance_page.go_to_report_details(report_number)
        pci_compliance_page.assert_negative_pci_table("4.1.1")




        log.info("Cleaning up")
        self.LeftPanel.go_to_reports_pci_compliance()
        pci_compliance_page.delete_all_reports()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()


    def test_ath_7837_report_ssid_validation_negative(self):
        """
        1. Create PCI Report for CDE SSIDs without any networks ( No networks configured ) in a group/device.
        2.
            1.  Go to Reports
            2.  Navigate through PCI compliance
            3.  Create new report
            4.  click cde Subnets
            5.  Enter nothing in the IP and Mask and click Add
        """
        log.info("Test Setup :")
        log.info("STEP 1")
        log.info("Deleting Network if present")
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()

        log.info("Navigating to Reports Page")
        self.LeftPanel.go_to_reports_page()

        log.info("Navigating to PCI Compliance Page")
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        time.sleep(2)
        log.info("Assert report is not generated without ssid")
        pci_compliance_page.assert_create_failure_pci_compliance_report_without_ssid()
        log.info("Assert report is not generated without Cde Subnets")
        pci_compliance_page.assert_create_failure_pci_compliance_report_without_cde_subnet()
        log.info("END OF TEST CASE - test_ath_7837_report_ssid_validation_negative")


    # def test_ath_8340_Test_Case_2_1_1(self):
    #     """
    #     ################################################################################################################
    #     NAME : Ramakrishnan R
    #     DATE : 4/09/2015
    #     ################################################################################################################
    #         REQUIREMENT : 2 IAPs
    #         RUNTIME     : 6 Minutes
    #     ################################################################################################################
    #     ATH-8340:Test Case 2.1.1
    #     1  Make sure the SSID is default SSID which is Instant. Configure Admin username and password as admin1/admin1. Run PCI report for that SSID.
    #     2  Configure a network for this device, but keep the admin user ID and password to default values, i.e., admin/admin.
    #     3  Configure the network and change the default admin credentials.
    #     4  Create multiple groups and configure some groups with default admin credentials and some with non-default credentials. Run PCI report by selecting all the SSIDs from all the groups.
    #     ################################################################################################################
    #     """
    #     conf = self.config.config_vars
    #     log.info("SETUP")
    #     log.info("Assume IAPs attached to the athena with customer")
    #     log.info("STEP 1 : Make sure the SSID is default SSID which is Instant. Configure Admin username and password as admin1/admin1. Run PCI report for that SSID.")
    #     DeviceLibrary.write_erase_all("IAP_1")
    #     DeviceLibrary.reload("IAP_1")
    #     time.sleep(300)
    #     overview_page = self.LeftPanel.goto_monitoringPage()
    #     overview_page.go_to_all_groups_page()
    #     conf_page = self.LeftPanel.go_to_configuration()
    #     time.sleep(4)
    #     network_page = conf_page.go_to_networks()
    #     time.sleep(2)
    #     network_page.delete_network_if_present()
    #     time.sleep(2)
    #     system_page = self.LeftPanel.go_to_system_page()
    #     system_page.go_to_admin_tab()
    #     system_page.modify_username_and_password("admin1", "admin1")
    #     try:
    #         system_page.assert_error_message_present()
    #     except:
    #         pass
    #     myDevice = Device.getDeviceObject("IAP_1")
    #     time.sleep(300)
    #     myDevice.setUsername("admin1")
    #     myDevice.setPassword("admin1")
    #     pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
    #     pci_compliance_page.delete_all_reports()
    #     report1 = pci_compliance_page.create_pci_compliance_report("now", self.config.config_vars.one_time, "cde_ssids","all_ssids")
    #     ####Commenting following lines bcoz of SW bug. Report generation will fail.
    #     #pci_compliance_page.verify_report_generation(report1)
    #     #pci_compliance_page.go_to_first_report()
    #     #pci_compliance_page.assert_negative_pci_table("2.1.1")
    #
    #     log.info("STEP 2 : Configure a network for this device, but keep the admin user ID and password to default values, i.e., admin/admin.")
    #     log.info("INVALID STEP")
    #     # DeviceLibrary.getPrompt("IAP_1")
    #     # DeviceLibrary.write_erase_all("IAP_1")
    #     # DeviceLibrary.reload("IAP_1")
    #     # time.sleep(300)
    #     # log.info("Create the CDE ssid for PCI compliation")
    #     # self.LeftPanel.goto_configuration_page()
    #     # self.LeftPanel.go_to_network_page()
    #     # self.NetworkPage.delete_all_networks()
    #     # ssid_name = conf.Network_name
    #     # basic_info = self.NetworkPage.create_new_network()
    #     # virtual_lan = basic_info.employee_network_info(ssid_name)
    #     # security = virtual_lan.use_vlan_defaults()
    #     # access = security.assert_roaming_defaults(True, False)
    #     # access.finish_network_setup()
    #     # self.NetworkPage.assert_new_network(ssid_name)
    #     # myDevice = Device.getDeviceObject("IAP_1")
    #     # time.sleep(300)
    #     # myDevice.setUsername("admin")
    #     # myDevice.setPassword("admin")
    #     # pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
    #     # pci_compliance_page.delete_all_reports()
    #     # report1 = pci_compliance_page.create_pci_compliance_report("now", self.config.config_vars.one_time, "cde_ssids","all_ssids")
    #     # pci_compliance_page.verify_report_generation(report1)
    #     # pci_compliance_page.go_to_first_report()
    #     # pci_compliance_page.assert_negative_pci_table("2.1.1")
    #     log.info("STEP 3 : Configure the network and change the default admin credentials.")
    #     log.info("Create the CDE ssid for PCI compliation")
    #     # self.LeftPanel.goto_configuration_page()
    #     # self.LeftPanel.go_to_network_page()
    #     # self.NetworkPage.delete_all_networks()
    #     # ssid_name = conf.Network_name
    #     # basic_info = self.NetworkPage.create_new_network()
    #     # virtual_lan = basic_info.employee_network_info(ssid_name)
    #     # security = virtual_lan.use_vlan_defaults()
    #     # access = security.assert_roaming_defaults(True, False)
    #     # access.finish_network_setup()
    #     # self.NetworkPage.assert_new_network(ssid_name)
    #     system_page = self.LeftPanel.go_to_system_page()
    #     system_page.go_to_admin_tab()
    #     system_page.modify_username_and_password("admin", "test123")
    #     try:
    #         system_page.assert_error_message_present()
    #     except:
    #         pass
    #     myDevice = Device.getDeviceObject("IAP_1")
    #     time.sleep(300)
    #     myDevice.setUsername("admin")
    #     myDevice.setPassword("test123")
    #     pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
    #     pci_compliance_page.delete_all_reports()
    #     report1 = pci_compliance_page.create_pci_compliance_report("now", self.config.config_vars.one_time, "cde_ssids","all_ssids")
    #     pci_compliance_page.verify_report_generation(report1)
    #     pci_compliance_page.go_to_first_report()
    #     pci_compliance_page.assert_pci_table("2.1.1")
    #     #
    #     # DeviceLibrary.write_erase_all("IAP_1")
    #     # DeviceLibrary.reload("IAP_1")
    #     # time.sleep(300)
    #     # myDevice.setUsername("admin")
    #     # myDevice.setPassword("admin")
    #     log.info("STEP 4 : Create multiple groups and configure some groups with default admin credentials and some with non-default credentials. Run PCI report by selecting all the SSIDs from all the groups.")
    #     overview_page = self.LeftPanel.goto_monitoringPage()
    #     overview_page.create_new_group("GroupA", "test123")
    #     inner_left_panel = self.TopPanel.get_inner_left_panel()
    #     manage_group_page = inner_left_panel.manage_group()
    #     manage_group_page.move_one_vc_to_group("GroupA")
    #     overview_page.go_to_all_groups_page()
    #     pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
    #     pci_compliance_page.delete_all_reports()
    #     report1 = pci_compliance_page.create_pci_compliance_report("now", self.config.config_vars.one_time, "cde_ssids","all_ssids")
    #     pci_compliance_page.verify_report_generation(report1)
    #     pci_compliance_page.go_to_first_report()
    #     pci_compliance_page.assert_negative_pci_table("2.1.1")
    #
    #     log.info("CLEANUP")
    #     self.LeftPanel.go_to_monitoring_page()
    #     inner_left_panel = self.TopPanel.click_slider_icon()
    #     manage_group_page = inner_left_panel.manage_group()
    #     manage_group_page.move_all_ap_to_group("default")
    #     time.sleep(300)
    #     DeviceLibrary.reload("IAP_1")
    #     DeviceLibrary.reload("IAP_2")
    #     time.sleep(300)
    #     log.info("END OF TESTCASE : ATH-8340")

    def test_ath_8341_Test_case_4_1_1(self):
        """
        1  Configure open SSID on one of the groups and run PCI report for that SSID.
        2  Configure SSID with WPA2 and run PCI report on that SSID.
        3  Configure SSID with static WEP and run PCI report for that SSID.
        4  Run PCI report on SSID created from step 2 and step 3.
        5  Create multiple groups and configure some with open SSIDs and some with WPA2. Run PCI report on all groups (all SSIDs).
        :return:
        """

        log.info("SETUP")
        log.info("STEP 1 : Configure open SSID on one of the groups and run PCI report for that SSID.")
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()
        self.LeftPanel.goto_configuration_page()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        security.set_security_level_open()
        security.assert_open_roaming_value()
        security.set_open_roaming_nondefault()
        access = security.use_security_default()
        access.finish_network_setup()
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        pci_compliance_page.delete_all_reports()
        time.sleep(300)
        report1 = pci_compliance_page.create_pci_compliance_report("now", self.config.config_vars.one_time, "cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report1)
        pci_compliance_page.go_to_first_report()
        pci_compliance_page.assert_negative_pci_table("4.1.1")
        self.LeftPanel.go_to_monitoring_page()
        #overview_page.go_to_all_groups_page()
        self.LeftPanel.goto_configuration_page()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()

        log.info("STEP 2 : Configure SSID with WPA2 and run PCI report on that SSID.")
        ssid_wpa2 = self.config.config_vars.Network_name
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_wpa2)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True, False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_wpa2)
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        pci_compliance_page.delete_all_reports()
        time.sleep(300)
        report1 = pci_compliance_page.create_pci_compliance_report("now", self.config.config_vars.one_time, "cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report1)
        pci_compliance_page.go_to_first_report()
        pci_compliance_page.assert_pci_table("4.1.1")
        self.LeftPanel.go_to_monitoring_page()
        self.LeftPanel.goto_configuration_page()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()

        log.info("STEP 3 : Configure SSID with static WEP and run PCI report for that SSID.")
        ssid_wep = "test3"
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_wep)
        security = virtual_lan.use_vlan_defaults()
        security.set_security_level_and_key_management("Personal")
        access = security.use_security_default()
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_wep)
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        pci_compliance_page.delete_all_reports()
        time.sleep(300)
        report1 = pci_compliance_page.create_pci_compliance_report("now", self.config.config_vars.one_time, "cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report1)
        pci_compliance_page.go_to_first_report()
        pci_compliance_page.assert_negative_pci_table("4.1.1")
        self.LeftPanel.go_to_monitoring_page()
        self.LeftPanel.goto_configuration_page()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()

        #import pdb
        ##pdb.set_trace()
        log.info("STEP 4 : Run PCI report on SSID created from step 2 and step 3.")
        ssid_wpa2 = self.config.config_vars.Network_name
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_wpa2)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True, False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_wpa2)
        time.sleep(300)
        ssid_wep = "test3"
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_wep)
        security = virtual_lan.use_vlan_defaults()
        security.set_security_level_and_key_management("Personal")
        access = security.use_security_default()
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_wep)
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        pci_compliance_page.delete_all_reports()
        time.sleep(300)
        report1 = pci_compliance_page.create_pci_compliance_report("now", self.config.config_vars.one_time, "cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report1)
        pci_compliance_page.go_to_first_report()
        pci_compliance_page.assert_negative_pci_table("4.1.1")
        self.LeftPanel.go_to_monitoring_page()
        self.LeftPanel.goto_configuration_page()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()

        log.info("STEP 5 : Create multiple groups and configure some with open SSIDs and some with WPA2. Run PCI report on all groups (all SSIDs).")
        self.LeftPanel.go_to_monitoring_page()
        overview_page.create_new_group("GroupA", "test123")
        inner_left_panel = self.TopPanel.get_inner_left_panel()
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.move_one_vc_to_group("GroupA")
        overview_page.go_to_group_page("GroupA")
        self.LeftPanel.go_to_monitoring_page()
        self.LeftPanel.goto_configuration_page()
        self.LeftPanel.go_to_network_page()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        security.set_security_level_open()
        security.assert_open_roaming_value()
        security.set_open_roaming_nondefault()
        access = security.use_security_default()
        access.finish_network_setup()
        time.sleep(200)
        DeviceLibrary.reconnect("IAP_1")
        #self.NetworkPage.assert_new_network()

        overview_page.go_to_default_group()
        ssid_wep = "test3"
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_wep)
        security = virtual_lan.use_vlan_defaults()
        security.set_security_level_and_key_management("Personal")
        access = security.use_security_default()
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_wep)

        overview_page.go_to_all_groups_page()
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        pci_compliance_page.delete_all_reports()
        time.sleep(300)
        self.browser.refresh()
        report1 = pci_compliance_page.create_pci_compliance_report("now", self.config.config_vars.one_time, "cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report1)
        pci_compliance_page.go_to_first_report()
        pci_compliance_page.assert_negative_pci_table("4.1.1")

        log.info("CLEANUP:")
        overview_page = self.LeftPanel.goto_monitoringPage()
        inner_left_panel = self.TopPanel.click_slider_icon()
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.move_all_ap_to_group("default")
        time.sleep(200)
        DeviceLibrary.reconnect("IAP_1")
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()
        self.LeftPanel.go_to_monitoring_page()
        self.LeftPanel.goto_configuration_page()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        overview_page.go_to_group_page("GroupA")
        self.LeftPanel.go_to_monitoring_page()
        self.LeftPanel.goto_configuration_page()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        
        
    def test_ath_9007_PCI_report_with_IP_address(self):
        """
        1   1. Create PCI report by selecting CDE subnet and click on new button.

            2. Enter the Newrork address of CDE and run report.
        2  Repeat the first step above - now enter some random IP address which is different from the CDE, and run the report.
 `      """
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()
        self.LeftPanel.goto_configuration_page()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        ssid_wpa2 = "TEST_Reporting"
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_wpa2)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True, False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_wpa2)
        time.sleep(200)
        DeviceLibrary.connect_client_to_ap("Client_1", "TEST_Reporting")
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        pci_compliance_page.delete_all_reports()
        time.sleep(100)
        report1 = pci_compliance_page.create_pci_compliance_report("now", self.config.config_vars.one_time, "cde_subnets",cde_subnet="10.29.27.21", cde_mask="255.255.255.248")
        pci_compliance_page.verify_report_generation(report1)
        pci_compliance_page.delete_all_reports()
        report1 = pci_compliance_page.create_pci_compliance_report("now", self.config.config_vars.one_time,"cde_subnets")
        try:
            pci_compliance_page.verify_report_generation(report1)
            raise AssertionError
        except:
            pass
        log.info("CLEANUP")
        overview_page.go_to_default_group()
        self.LeftPanel.goto_configuration_page()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        #pci_compliance_page.assert_negative_pci_table("4.1.1")
        log.info("END OF TEST CASE : 9007")
        
    def test_ath_9027_9028_9029_9030_9031_delete_scheduled_and_completed_report(self):
        """
        ################################################################################################################
        NAME : Arunkarthick A
        DATE : 4/06/2015
        ATH-9015:Run Report now
        1 Schedule a report. When the report is in scheduled status, delete the report.
        2 Run a report and click on detele button once the status changes to Completed.
        3.Delete all the reports
        4.Delete completed periodic report
        5.delete scheduled periodic report
        ################################################################################################################
        """
        log.info("Create the CDE ssid for PCI compliance")
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        ssid_name = self.config.config_vars.Network_name
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_name)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True,False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_name)
        log.info("Go To Monitoring => Overview Page")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        monitor_page.assert_new_network_in_monitoring(ssid_name)


        log.info("Go To Reports => PCI compliance Page")
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        log.info("Delete all the existing reports before ")
        pci_compliance_page.go_to_all_groups_page()
        pci_compliance_page.delete_all_reports()
        

        log.info("ATH-9027:Schedule a report. When the report is in scheduled status, delete the report.")
        report1 = pci_compliance_page.create_pci_compliance_report("Later",self.config.config_vars.one_time,"cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report1,"Scheduled")
        pci_compliance_page.delete_report(report1)
        
        log.info("ATH-9028:Run a report and click on delete button once the status changes to Completed.")
        report2 = pci_compliance_page.create_pci_compliance_report("now",self.config.config_vars.one_time,"cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report2,"Completed")
        pci_compliance_page.delete_report(report2)
        
        log.info("ATH-9030:Delete completed periodic report")
        log.info("create the periodic report,after completed it will create one scheduled report")
        report3 = pci_compliance_page.create_pci_compliance_report("now",self.config.config_vars.repeat_daily_interval,"cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report3,"Completed")
        log.info("Verify Another report should be scheduled for the periodic report")
        report4 = report3 + 1
        pci_compliance_page.verify_report_generation(report4,"Scheduled")
        log.info("Delete completed periodic report")
        pci_compliance_page.delete_report(report3)
        report4 = report4 - 1
        log.info("Verify the periodic report in scheduled status is not impacted")
        pci_compliance_page.verify_report_generation(report4,"Scheduled")
        pci_compliance_page.delete_report(report4)
        
        log.info("ATH-9031:Delete scheduled periodic report")
        log.info("create the periodic report,after completed it will create one scheduled report")
        report5 = pci_compliance_page.create_pci_compliance_report("now",self.config.config_vars.repeat_daily_interval,"cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report5,"Completed")
        log.info("Verify Another report should be scheduled for the periodic report")
        report6 = report5 + 1
        pci_compliance_page.verify_report_generation(report6,"Scheduled")
        log.info("Delete scheduled periodic report")
        pci_compliance_page.delete_report(report6)
        log.info("Verify the periodic report in completed status is not impacted")
        pci_compliance_page.verify_report_generation(report5,"Completed")
        pci_compliance_page.delete_report(report5)        
        pci_compliance_page.delete_all_reports()

        log.info("ATH-9029:Create Many Reports then delete all reports")
        report = pci_compliance_page.create_pci_compliance_report("now",self.config.config_vars.one_time,"cde_ssids","all_ssids","enabled")
        pci_compliance_page.verify_report_generation(report,"Completed")
        report7 = pci_compliance_page.create_pci_compliance_report("now",self.config.config_vars.repeat_daily_interval,"cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report7,"Completed")
        log.info("Verify Another report should be scheduled for the periodic report")
        report8 = report7 + 1
        pci_compliance_page.verify_report_generation(report8,"Scheduled")
        report9 = pci_compliance_page.create_pci_compliance_report("now",self.config.config_vars.one_time,"cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report9,"Scheduled")
        report10 = pci_compliance_page.create_pci_compliance_report("Later",self.config.config_vars.one_time,"cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report10,"Scheduled")


        
        log.info("Unconfigurations: Delete all the created reports")
        pci_compliance_page.delete_all_reports()
        pci_compliance_page.go_to_default_group()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        log.info("END OF TEST CASE - test_ath_9027_9028_9029_9030_9031_delete_scheduled_and_completed_report")
##
    def test_ath_8977_SSIDs_at_group_level(self):
        """
        ################################################################################################################
        ATH-8977:SSIDs at group level
        :return:
        ################################################################################################################
        """
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()
        self.LeftPanel.goto_configuration_page()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        ssid_wpa2 = self.config.config_vars.Network_name
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_wpa2)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True, False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_wpa2)
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        time.sleep(200)
        self.browser.refresh()
        overview_page.go_to_all_groups_page()
        pci_compliance_page.delete_all_reports()
        report1 = pci_compliance_page.create_pci_compliance_report("now", self.config.config_vars.one_time, "cde_ssids","all_ssids", group="default")
        pci_compliance_page.verify_report_generation(report1)
        pci_compliance_page.go_to_first_report()
        import pdb
        #pdb.set_trace()
        pci_compliance_page.assert_pci_table("4.1.1")

        self.LeftPanel.go_to_monitoring_page()
        overview_page.go_to_default_group()
        self.LeftPanel.goto_configuration_page()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()

        overview_page.create_new_group("GroupA", "test123")
        inner_left_panel = self.TopPanel.get_inner_left_panel()
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.move_one_vc_to_group("GroupA")
        self.LeftPanel.go_to_monitoring_page()
        self.LeftPanel.goto_configuration_page()
        overview_page.go_to_group_page("GroupA")
        self.LeftPanel.go_to_network_page()

        self.NetworkPage.delete_all_networks()
        time.sleep(200)
        DeviceLibrary.reconnect("IAP_1")
        ssid_wep = "test3"
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_wep)
        security = virtual_lan.use_vlan_defaults()
        security.set_security_level_and_key_management("Personal")
        access = security.use_security_default()
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_wep)
        overview_page.go_to_all_groups_page()
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        pci_compliance_page.delete_all_reports()
        time.sleep(200)
        self.browser.refresh()
        overview_page.go_to_all_groups_page()
        report1 = pci_compliance_page.create_pci_compliance_report("now", self.config.config_vars.one_time, "cde_ssids","all_ssids", group="GroupA")
        pci_compliance_page.verify_report_generation(report1)
        pci_compliance_page.go_to_first_report()
        pci_compliance_page.assert_negative_pci_table("4.1.1")
        overview_page.go_to_group_page("GroupA")
        self.LeftPanel.go_to_monitoring_page()
        self.LeftPanel.goto_configuration_page()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        overview_page.go_to_all_groups_page()
        self.LeftPanel.go_to_monitoring_page()
        inner_left_panel = self.TopPanel.click_slider_icon()
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.move_all_ap_to_group("default")
        overview_page.go_to_group_page("default")
        time.sleep(200)
        DeviceLibrary.reconnect("IAP_1")

    def test_ath_9017_9018_9019_9020_9021_9022_9023_email_report(self):
        """
        ################################################################################################################
        NAME : Arunkarthick A
        DATE : 4/06/2015
        1 Email for single user.
        2 Email with multiple users.
        3.Invalid emailid
        4.Email for periodic reports
        5.Email existing report from landing page
        6.Email existing report from detail report
        7.Email scheduled report
        ################################################################################################################
        """
        log.info("Create the CDE ssid for PCI compliance")
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        ssid_name = self.config.config_vars.Network_name
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_name)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True,False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_name)
        log.info("Go To Monitoring => Overview Page")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        monitor_page.assert_new_network_in_monitoring(ssid_name)    


        log.info("Go To Reports => PCI compliance Page")
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        log.info("Delete all the existing reports before ")
        pci_compliance_page.go_to_all_groups_page()
        pci_compliance_page.delete_all_reports()
        

        log.info("ATH-9017:Run a report with Email for single user")
        report1 = pci_compliance_page.create_pci_compliance_report("now",self.config.config_vars.one_time,"cde_ssids","all_ssids","enabled","all_groups",self.config.config_vars.single_email)
        pci_compliance_page.verify_report_generation(report1,"Completed")
        #Verify email received - Pending
        pci_compliance_page.delete_report(report1)
        
        log.info("ATH-9018:Run a report with Email for multiple users")
        report2 = pci_compliance_page.create_pci_compliance_report("now",self.config.config_vars.one_time,"cde_ssids","all_ssids","enabled","all_groups",self.config.config_vars.multiple_emails)
        pci_compliance_page.verify_report_generation(report2,"Completed")
        #Verify email received - Pending
        pci_compliance_page.delete_report(report2)
        
        log.info("ATH-9020:Email for periodic reports")
        log.info("case 1: For All groups")
        report3 = pci_compliance_page.create_pci_compliance_report("now",self.config.config_vars.repeat_daily_interval,"cde_ssids","all_ssids","enabled")
        pci_compliance_page.verify_report_generation(report3)
        log.info("Verify Another report should be scheduled for the periodic report")
        report4 = report3 + 1
        pci_compliance_page.verify_report_generation(report4,"Scheduled")
        log.info("case 2: For single group")
        report5 = pci_compliance_page.create_pci_compliance_report("now",self.config.config_vars.repeat_daily_interval,"cde_ssids","all_ssids","enabled","default")
        pci_compliance_page.verify_report_generation(report5)
        log.info("Verify Another report should be scheduled for the periodic report")
        report6 = report5 + 2 #Adding 2, since one periodic scheduled had been created for all groups already 
        pci_compliance_page.verify_report_generation(report6,"Scheduled")
        
        log.info("ATH-9019:Run a report with Invalid email")
        pci_compliance_page.create_new_pci_report.click()
        pci_compliance_page.buy_time()
        pci_compliance_page.pci_run_report_now.click()
        pci_compliance_page.report_repeat.set(self.config.config_vars.one_time)
        log.debug("ReportsSecurityPage: check the checkbox 'email'")
        pci_compliance_page.pci_email_report.click()
        log.debug("ReportsSecurityPage: writing invalid email id without '@' character")
        pci_compliance_page.pci_report_email.set(self.config.config_vars.email_without_at_character)
        pci_compliance_page.select_all_cde_ssids.click()
        pci_compliance_page.generate_pci_report.click()
        if pci_compliance_page.invalid_email_message:
            log.info("PASS: Invalid email message is existing after the invalid email id\(email without '@' symbol\)input")
        else:
            log.info("FAIL: Invalid email message is not coming after the invalid email id\(email without '@' symbol\)input")
            raise AssertionError("Invalid email message is not coming after the invalid email id\(email without '@' symbol\)input")
        time.sleep(3)
        log.debug("ReportsSecurityPage: writing invalid email id without .com")
        pci_compliance_page.pci_report_email.set(self.config.config_vars.email_without_dot_com)
        pci_compliance_page.generate_pci_report.click()
        if pci_compliance_page.invalid_email_message:
            log.info("PASS: Invalid email message is existing after the invalid email id\(email without .com\)input")
        else:
            log.info("FAIL: Invalid email message is not coming after the invalid email id\(email without .com\)input")
            raise AssertionError("Invalid email message is not coming after the invalid email id\(email without .com\)input")
        time.sleep(3)
        pci_compliance_page.cancel_report()
        
        log.info("ATH-9021:Email existing report from landing page")
        pci_compliance_page.email_to_user_dashboard_table(report5)
        
        log.info("ATH-9022:Email existing report from detail report")
        pci_compliance_page.email_from_report_details_page(report3)
        
        log.info("ATH-9023:Email scheduled report - email option should be disabled for scheduled status reports")
        pci_compliance_page.verify_email_option_for_scheduled_report(report6)
        
        log.info("Delete all the created reports")
        pci_compliance_page.delete_all_reports()
        pci_compliance_page.go_to_default_group()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        log.info("END OF TEST CASE - test_ath_9017_9018_9019_9020_9021_9022_9023_email_report")
    
    def test_ath_1616_create_report(self):
        """
        1.Create a PCI compliance report with runtime set to now.
        2.Select the report and export it
        3.Select the report and email it.
        4.Delete a report
        5.Create a report with runtime set to schedule later.
        6.Delete a report scheduled to run later
        7.Click on cancel button in the Create New Report popup window.
        8.Create a report with now and scheduled later with email option set
        """
        overview_page = self.LeftPanel.goto_monitoringPage()
        overview_page.go_to_all_groups_page()
        overview_page.go_to_default_group()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_all_networks()
        ssid_name = self.config.config_vars.Network_name
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_name)
        security = virtual_lan.use_vlan_defaults()
        access = security.assert_roaming_defaults(True,False)
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_name)
        time.sleep(120)
        log.info("Go To Reports => PCI compliance Page")
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        log.info("Delete all the existing reports before ")
        pci_compliance_page.delete_all_reports()
        log.info("STEP 1:   Create a non-periodic report with Run Report set to 'now'")
        report1 = pci_compliance_page.create_pci_compliance_report("now",self.config.config_vars.one_time,"cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report1)
        # log.info("STEP2: Export the Report")
        # pci_compliance_page.export_pci_report("completed")
        log.info("STEP3:   Email report to User")
        pci_compliance_page.email_to_user_dashboard_table(1)
        log.info("STEP4:  Delete a Report")
        pci_compliance_page.delete_all_reports()
        log.info("Go To Reports => PCI compliance Page")
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        log.info("Delete all the existing reports before ")
        pci_compliance_page.delete_all_reports()
        log.info("STEP 5:  Check if report generated for Scheduled later")
        report1 = pci_compliance_page.create_pci_compliance_report("Later",self.config.config_vars.one_time,"cde_ssids","all_ssids")
        log.info("Check if report generated for Scheduled later")
        pci_compliance_page.verify_report_generation(report1,"Scheduled")
        log.info("STEP 6: Delete a report scheduled to run later")
        pci_compliance_page.delete_all_reports()
        log.info("STEP7: Click on cancel button on create new report popup window")
        log.info("Go To Reports => PCI compliance Page")
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        log.info("Delete all the existing reports before ")
        pci_compliance_page.delete_all_reports()
        pci_compliance_page.create_and_cancel()
        pci_compliance_page.verify_report_cancellation()
        log.info("STEP8:Create a report with now and scheduled later with email option set")
        log.info("Go To Reports => PCI compliance Page")
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        report1 = pci_compliance_page.create_pci_compliance_report("now",self.config.config_vars.one_time,"cde_ssids","all_ssids", "enabled")
        pci_compliance_page.verify_report_generation(report1)
        pci_compliance_page.delete_all_reports()
        log.info("STEP8b:Create a report with now and scheduled later with email option set")
        report1 = pci_compliance_page.create_pci_compliance_report("Later",self.config.config_vars.one_time,"cde_ssids","all_ssids", "enabled")
        pci_compliance_page.verify_report_generation(report1,"Scheduled")
        pci_compliance_page.delete_all_reports()
        log.info("Test cases at ALL Group Level ")
        log.info("Go To Reports => PCI compliance Page")
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        pci_compliance_page.go_to_all_groups_page()
        log.info("Delete all the existing reports before ")
        pci_compliance_page.delete_all_reports()
        log.info("STEP 1:   Create a non-periodic report with Run Report set to 'now'")
        report1 = pci_compliance_page.create_pci_compliance_report("now",self.config.config_vars.one_time,"cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report1)
        pci_compliance_page.delete_all_reports()

        log.info("***********ALL GROUP LEVEL REPORTS *************")
        log.info("Go To Reports => PCI compliance Page")
        overview_page = self.LeftPanel.goto_monitoringPage()

        overview_page.go_to_all_groups_page()
        self.LeftPanel.go_to_reports_pci_compliance()

        log.info("Delete all the existing reports before ")
        pci_compliance_page.delete_all_reports()

        log.info("STEP 1:   Create a non-periodic report with Run Report set to 'now'")
        report1 = pci_compliance_page.create_pci_compliance_report("now",self.config.config_vars.one_time,"cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report1)
        ## log.info("STEP2: Export the Report")
        ## pci_compliance_page.export_pci_report("completed")
        log.info("STEP3:   Email report to User")
        pci_compliance_page.email_to_user_dashboard_table(1)
        log.info("STEP4:  Delete a Report")
        pci_compliance_page.delete_all_reports()
        log.info("Go To Reports => PCI compliance Page")
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        log.info("Delete all the existing reports before ")
        pci_compliance_page.delete_all_reports()
        log.info("STEP 5:  Check if report generated for Scheduled later")
        report1 = pci_compliance_page.create_pci_compliance_report("Later",self.config.config_vars.one_time,"cde_ssids","all_ssids")
        log.info("Check if report generated for Scheduled later")
        pci_compliance_page.verify_report_generation(report1,"Scheduled")
        log.info("STEP 6: Delete a report scheduled to run later")
        pci_compliance_page.delete_all_reports()
        log.info("STEP7: Click on cancel button on create new report popup window")
        log.info("Go To Reports => PCI compliance Page")
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        log.info("Delete all the existing reports before ")
        pci_compliance_page.delete_all_reports()
        pci_compliance_page.create_and_cancel()
        pci_compliance_page.verify_report_cancellation()
        log.info("STEP8:Create a report with now and scheduled later with email option set")
        log.info("Go To Reports => PCI compliance Page")
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        report1 = pci_compliance_page.create_pci_compliance_report("now",self.config.config_vars.one_time,"cde_ssids","all_ssids", "enabled")
        pci_compliance_page.verify_report_generation(report1)
        pci_compliance_page.delete_all_reports()
        log.info("STEP8b:Create a report with now and scheduled later with email option set")
        report1 = pci_compliance_page.create_pci_compliance_report("Later",self.config.config_vars.one_time,"cde_ssids","all_ssids", "enabled")
        pci_compliance_page.verify_report_generation(report1,"Scheduled")
        pci_compliance_page.delete_all_reports()
        log.info("Test cases at ALL Group Level ")
        log.info("Go To Reports => PCI compliance Page")
        pci_compliance_page = self.LeftPanel.go_to_reports_pci_compliance()
        pci_compliance_page.go_to_all_groups_page()
        log.info("Delete all the existing reports before ")
        pci_compliance_page.delete_all_reports()
        log.info("STEP :   Create a non-periodic report with Run Report set to 'now'")
        report1 = pci_compliance_page.create_pci_compliance_report("now",self.config.config_vars.one_time,"cde_ssids","all_ssids")
        pci_compliance_page.verify_report_generation(report1)
        pci_compliance_page.delete_all_reports()
        pci_compliance_page.assert_delete_button_disabled()

        
    