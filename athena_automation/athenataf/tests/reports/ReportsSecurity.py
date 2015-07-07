__author__ = 'aarunakirisamy'
import logging
log = logging.getLogger('athenataf')
import pdb
from athenataf.lib.functionality.test.ReportsTest import ReportsTest
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest
from athenataf.lib.functionality.common import DeviceLibrary
import time

class ReportsSecurity(ConfigurationTest, ReportsTest):
    def test_ath_8925_run_report_now(self):
        """
        ################################################################################################################
        NAME : Arunkarthick A
        DATE : 4/06/2015
        ATH-9015:Run Report Now
        1 Create a non-periodic report with Run Report set to "Last day","Now".
        2 Create daily periodic report with "Run Report" set to now.
        ################################################################################################################
        """
        log.info("Go To Monitoring => Overview Page")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        monitor_page.go_to_all_groups_page()
        log.info("Go To Reports => Security Page")
        reports_security_page = self.LeftPanel.go_to_reports_security()
        log.info("Delete all the existing reports")
        reports_security_page.delete_all_reports()
        log.info("STEP 1:Create a non-periodic report with Run Report set to 'now'")
        report1 = reports_security_page.create_security_report("Last day","Now",self.config.config_vars.one_time)
        reports_security_page.verify_report_generation(report1)
        log.info("STEP 2:Create a periodic report with Run Report set to 'now'")
        report2 = reports_security_page.create_security_report("Last day","Now",self.config.config_vars.repeat_daily_interval)
        reports_security_page.verify_report_generation(report2)
        log.info("Verify Another report should be scheduled for the periodic report")
        report3 = report2 + 1
        reports_security_page.verify_report_generation(report3,"Scheduled")
        log.info("Unconfigurations: Delete all the created reports")
        reports_security_page.delete_all_reports()
        monitor_page.go_to_group_page("default")
        log.info("END OF TEST CASE - test_ath_8925_run_report_now")
        
    def test_ath_8926_run_report_schedule_for_later(self):
        """
        ################################################################################################################
        NAME : Arunkarthick A
        DATE : 4/06/2015
        1. Create report with scheduled for later option where scheduled time is less than current date.
        2 Create a non-periodic report with scheduled for later option is set to greater than current date and time based on the time zone.
        3 Create a weekly periodic report with scheduled for later time is set to current time + 1 hour
        4 Repeat the above cases at group level.



        ################################################################################################################
        """
        log.info("Go To Monitoring => Overview Page")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        monitor_page.go_to_all_groups_page()
        log.info("Go To Reports => Security Page")
        reports_security_page = self.LeftPanel.go_to_reports_security()
        log.info("Delete all the existing reports")
        reports_security_page.delete_all_reports()
        
        log.info("STEP 1:Create report with scheduled for later option where scheduled time is less than current date")
        reports_security_page.create_new.click()
        reports_security_page.buy_time()
        reports_security_page.time_span.set("Last day")
        
        log.debug("ReportsSecurityPage: click on 'Schedule For Later' Radio-Button ")
        reports_security_page.run_report_schedule_for_later.click()
        log.debug("ReportsSecurityPage: click on textbox ")
        reports_security_page.run_report_schedule_later_date.send_keys("")
        time.sleep(2)
        reports_security_page.calendar_prev_month.click()
        time.sleep(2)
        reports_security_page.date_22.click()
        time.sleep(2)
        reports_security_page.report_repeat.set(self.config.config_vars.one_time)
        reports_security_page.email_report.click()
        reports_security_page.report_email.set(self.config.config_vars.report_email)
        reports_security_page.create.click()
        if reports_security_page.invalid_schedule_date_message:
            log.info("PASS: Invalid Schedule date message is coming when we give the less than current date")
        else:
            log.info("FAIL: Invalid Schedule date message is coming when we give the less than current date")
            raise AssertionError("Invalid Schedule date message is coming when we give the less than current date")
        reports_security_page.warning_button_ok.click()
        time.sleep(3)
        reports_security_page.cancel_report()
        
        log.info("STEP 2:Create a non-periodic report with scheduled for later option is set to greater than current date and time based on the time zone.")

        report1 = reports_security_page.create_security_report("Last day","Later",self.config.config_vars.one_time)

        reports_security_page.verify_report_generation(report1,"Scheduled")
        
        log.info("STEP 3:Create a non-periodic report at group level")
        report2 = reports_security_page.create_security_report("Last day","Later",self.config.config_vars.one_time,"disabled","default")
        reports_security_page.verify_report_generation(report2,"Scheduled")
        
        log.info("Unconfigurations: Delete all the created reports")
        reports_security_page.delete_all_reports()
        monitor_page.go_to_group_page("default")
        log.info("END OF TEST CASE - test_ath_8926_run_report_schedule_for_later")

    def test_ath_8937_8938_8939_8940_8941_delete_scheduled_and_completed_report(self):
        """
        ################################################################################################################
        NAME : Arunkarthick A
        DATE : 4/06/2015
        1 Schedule a report. When the report is in scheduled status, delete the report.
        2 Run a report and click on detele button once the status changes to Completed.
        3.Delete all the reports
        4.Delete completed periodic report
        5.delete scheduled periodic report
        ################################################################################################################
        """
        log.info("Go To Monitoring => Overview Page")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        monitor_page.go_to_all_groups_page()
        log.info("Go To Reports => Security Page")
        reports_security_page = self.LeftPanel.go_to_reports_security()
        log.info("Delete all the existing reports")
        reports_security_page.delete_all_reports()
        log.info("ATH-8937:Schedule a report. When the report is in scheduled status, delete the report.")
        report1 = reports_security_page.create_security_report("Last day","Later",self.config.config_vars.one_time)
        reports_security_page.verify_report_generation(report1,"Scheduled")
        reports_security_page.delete_security_report(report1)
        
        log.info("ATH-8938:Run a report and click on delete button once the status changes to Completed.")
        report2 = reports_security_page.create_security_report("Last day","Now",self.config.config_vars.one_time)
        reports_security_page.verify_report_generation(report2,"Completed")
        reports_security_page.delete_security_report(report2)
        
        log.info("ATH-8940:Delete completed periodic report")
        log.info("create the periodic report,after completed it will create one scheduled report")
        report3 = reports_security_page.create_security_report("Last day","Now",self.config.config_vars.repeat_daily_interval)
        reports_security_page.verify_report_generation(report3,"Completed")
        log.info("Verify Another report should be scheduled for the periodic report")
        report4 = report3 + 1
        reports_security_page.verify_report_generation(report4,"Scheduled")
        log.info("Delete completed periodic report")
        reports_security_page.delete_security_report(report3)
        report4 = report4 - 1
        log.info("Verify the periodic report in scheduled status is not impacted")
        reports_security_page.verify_report_generation(report4,"Scheduled")
        reports_security_page.delete_security_report(report4)
        
        log.info("ATH-8941:Delete scheduled periodic report")
        log.info("create the periodic report,after completed it will create one scheduled report")
        report5 = reports_security_page.create_security_report("Last day","Now",self.config.config_vars.repeat_daily_interval)
        reports_security_page.verify_report_generation(report5,"Completed")
        log.info("Verify Another report should be scheduled for the periodic report")
        report6 = report5 + 1
        reports_security_page.verify_report_generation(report6,"Scheduled")
        log.info("Delete scheduled periodic report")
        reports_security_page.delete_security_report(report6)
        log.info("Verify the periodic report in completed status is not impacted")
        reports_security_page.verify_report_generation(report5,"Completed")
        reports_security_page.delete_all_reports()

        
        log.info("ATH-8939:Create Many Reports then delete all reports")
        report = reports_security_page.create_security_report("Last day","Now",self.config.config_vars.one_time,"enabled")
        reports_security_page.verify_report_generation(report,"Completed")
        report7 = reports_security_page.create_security_report("Last day","Now",self.config.config_vars.repeat_daily_interval)
        reports_security_page.verify_report_generation(report7,"Completed")
        log.info("Verify Another report should be scheduled for the periodic report")
        report8 = report7 + 1
        reports_security_page.verify_report_generation(report8,"Scheduled")
        report9 = reports_security_page.create_security_report("Last day","Now",self.config.config_vars.one_time)
        reports_security_page.verify_report_generation(report9,"Scheduled")
        report10 = reports_security_page.create_security_report("Last day","Later",self.config.config_vars.one_time)
        reports_security_page.verify_report_generation(report10,"Scheduled")


        log.info("Delete all the created reports")
        reports_security_page.delete_all_reports()
        monitor_page.go_to_group_page("default")
        log.info("END OF TEST CASE - test_ath_8937_8938_8939_8940_8941_delete_scheduled_and_completed_report")
        
        
##
    def test_ath_9226_Group_Report(self):
        """
        ################################################################################################################
        1   Select a group from group monitoring and create report.
            Move a VC from the group to different group, and click on the report generated before.
            Remove a client associated to an AP of the group.
            Add/remove SSID
        2   Select a group and go to report page.
        ################################################################################################################
        """
        conf = self.config.config_vars
        log.info("STEP 1.1 : Select a group from group monitoring and create report.")
        overview_page = self.LeftPanel.goto_monitoringPage()
        #overview_page.go_to_default_group()
        reports_security_page = self.LeftPanel.go_to_reports_security()
        reports_security_page.delete_all_reports()

        report = reports_security_page.create_security_report("Last day", "Now", self.config.config_vars.one_time)
        reports_security_page.verify_report_generation(report, "Completed")
        reports_security_page.go_to_first_report()
        wids_count = reports_security_page.get_report_count("aps")

        log.info("STEP 1.2 : Move a VC from the group to different group, and click on the report generated before.")
        overview_page.create_new_group("GroupA", "test123")
        inner_left_panel = self.TopPanel.get_inner_left_panel()
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.move_all_ap_to_group("GroupA")
        time.sleep(200)
        DeviceLibrary.reconnect("IAP_1")

        reports_security_page = self.LeftPanel.go_to_reports_security()
        reports_security_page.go_to_first_report()

        wids_count1 = reports_security_page.get_report_count("aps")
        if wids_count != wids_count1:
            raise AssertionError("Report got changed.")

        log.info("STEP 1.3 : Remove a client associated to an AP of the group.")
        DeviceLibrary.disconnect_client_from_ap("Client_1")
        reports_security_page = self.LeftPanel.go_to_reports_security()
        reports_security_page.go_to_first_report()

        wids_count1 = reports_security_page.get_report_count("aps")
        if wids_count != wids_count1:
            raise AssertionError("Report got changed.")
        log.info("STEP 1.4 : Add/remove SSID")
        overview_page.go_to_default_group()
        self.LeftPanel.go_to_network_page()
        ssid_wep = "test3"
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info(ssid_wep)
        security = virtual_lan.use_vlan_defaults()
        security.set_security_level_and_key_management("Personal")
        access = security.use_security_default()
        access.finish_network_setup()
        self.NetworkPage.assert_new_network(ssid_wep)
        reports_security_page = self.LeftPanel.go_to_reports_security()
        reports_security_page.go_to_first_report()

        wids_count1 = reports_security_page.get_report_count("aps")
        if wids_count != wids_count1:
            raise AssertionError("Report got changed.")

        log.info("STEP 2 : Select a group and go to report page.")
        overview_page.go_to_default_group()
        reports_security_page = self.LeftPanel.go_to_reports_security()
        reports_security_page.assert_group_name("default")

        log.info("CLEANUP")
        self.LeftPanel.go_to_monitoring_page()
        inner_left_panel = self.TopPanel.click_slider_icon()
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.move_all_ap_to_group("default")
        time.sleep(200)
        DeviceLibrary.reconnect("IAP_1")

    def test_ath_9229_tooltip(self):
        """
        1   Mouseover to the "Saved By" field in Security report

        :return:
        """
        log.info("STEP 1 : Mouseover to the 'Saved By' field in network report")
        conf = self.config.config_vars
        overview_page = self.LeftPanel.goto_monitoringPage()
        #overview_page.go_to_default_group()
        reports_security_page = self.LeftPanel.go_to_reports_security()
        reports_security_page.delete_all_reports()

        report = reports_security_page.create_security_report("Last day", "Now", self.config.config_vars.one_time)
        reports_security_page.verify_report_generation(report, "Completed")

        reports_security_page.assert_saved_by_tooltip()
        
    def test_ath_8927_8928_8929_8930_8931_8932_8933_email_report(self):

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
        log.info("Go To Monitoring => Overview Page")
        monitor_page = self.LeftPanel.goto_monitoringPage()
        monitor_page.go_to_all_groups_page()
        
        log.info("Go To Reports => Security Page")
        reports_security_page = self.LeftPanel.go_to_reports_security()
        

        log.info("Delete all the existing reports")
        reports_security_page.delete_all_reports()

        log.info("ATH-8927:Run a report with Email for single user")
        report1 = reports_security_page.create_security_report("Last day","Now",self.config.config_vars.one_time,"enabled","all_groups",self.config.config_vars.single_email)
        reports_security_page.verify_report_generation(report1,"Completed")
        #Verify email received - Pending
        reports_security_page.delete_security_report(report1)

        log.info("ATH-8928:Run a report with Email for multiple users")
        report2 = reports_security_page.create_security_report("Last day","Now",self.config.config_vars.one_time,"enabled","all_groups",self.config.config_vars.multiple_emails)
        reports_security_page.verify_report_generation(report2,"Completed")
        #Verify email received - Pending
        reports_security_page.delete_security_report(report2)


        log.info("ATH-8929:Run a report with Invalid email")
        reports_security_page.create_new.click()
        reports_security_page.buy_time()
        reports_security_page.time_span.set("Last day")
        reports_security_page.run_report_now.click()
        reports_security_page.report_repeat.set(self.config.config_vars.one_time)
        log.debug("ReportsSecurityPage: check the checkbox 'email'")
        reports_security_page.email_report.click()
        log.debug("ReportsSecurityPage: writing invalid email id without '@' character")
        reports_security_page.report_email.set(self.config.config_vars.email_without_at_character)
        reports_security_page.create.click()
        if reports_security_page.invalid_email_message:
            log.info("PASS: Invalid email message is existing after the invalid email id\(email without '@' symbol\)input")
        else:
            log.info("FAIL: Invalid email message is not coming after the invalid email id\(email without '@' symbol\)input")
            raise AssertionError("Invalid email message is not coming after the invalid email id\(email without '@' symbol\)input")
        time.sleep(3)
        log.debug("ReportsSecurityPage: writing invalid email id without .com")
        reports_security_page.report_email.set(self.config.config_vars.email_without_dot_com)
        reports_security_page.create.click()
        if reports_security_page.invalid_email_message:
            log.info("PASS: Invalid email message is existing after the invalid email id\(email without .com\)input")
        else:
            log.info("FAIL: Invalid email message is not coming after the invalid email id\(email without .com\)input")
            raise AssertionError("Invalid email message is not coming after the invalid email id\(email without .com\)input")
        time.sleep(3)
        reports_security_page.cancel_report()

        log.info("ATH-8929:Email for periodic reports")
        log.info("case 1: For All groups")
        report3 = reports_security_page.create_security_report("Last day","Now",self.config.config_vars.repeat_daily_interval,"enabled")
        reports_security_page.verify_report_generation(report3)
        log.info("Verify Another report should be scheduled for the periodic report")
        report4 = report3 + 1
        reports_security_page.verify_report_generation(report4,"Scheduled")
        log.info("case 2: For single group")
        report5 = reports_security_page.create_security_report("Last day","Now",self.config.config_vars.repeat_daily_interval,"enabled","default")
        reports_security_page.verify_report_generation(report5)
        log.info("Verify Another report should be scheduled for the periodic report")
        report6 = report5 + 2 #Adding 2, since one periodic scheduled had been created for all groups already
        reports_security_page.verify_report_generation(report6,"Scheduled")

        log.info("ATH-8930:Email existing report from landing page")
        reports_security_page.email_to_user_dashboard_table(report5)

        log.info("ATH-8931:Email existing report from detail report")
        reports_security_page.email_from_report_details_page(report3)


        log.info("ATH-8932:Email scheduled report - email option should be disabled for scheduled status reports")
        reports_security_page.verify_email_option_for_scheduled_report(report6)
        log.info("Delete all the created reports")
        reports_security_page.delete_all_reports()
        monitor_page.go_to_group_page("default")
        log.info("END OF TEST CASE - test_ath_8927_8928_8929_8930_8931_8932_8933_email_report")

    def test_ath_9227_summary_report_detail(self):
        """
        Step1: Create Security summary report and click on it.
        Step2: Click on Export
        Step3: Click on Email
        Step4: Click on close
        """
        self.LeftPanel.go_to_monitoring_page()
        monitoring_wids_page = self.LeftPanel.go_to_monitoring_wids_page()
        monitoring_wids_page.click_on_timeline("oneday")
        monitoring_rogue_aps = monitoring_wids_page.get_rogue_aps_count()
        monitoring_infra_attack_count = monitoring_wids_page.get_infrastructure_attacks_count()
        monitoring_client_attack_count = monitoring_wids_page.get_client_attacks_count()
        self.LeftPanel.go_to_reports_page()
        security_report = self.LeftPanel.go_to_reports_security()
        report1 = security_report.create_new_report()
        security_report.verify_report_generation(report1)
        security_report.go_to_verify_report(report1)
        report_wids_detection = security_report.get_report_count("wids")
        log.debug("report_wids_detection %d" % report_wids_detection)
        report_rogue_ap = security_report.get_report_count("aps")
        log.debug("report_rogue_ap %d" % report_rogue_ap)
        log.info("Navigate to Monitoring Page to fetch values")
        security_report.assert_reports_rogue_values(report_rogue_ap, monitoring_rogue_aps)
        monitoring_wids_count = monitoring_client_attack_count + monitoring_infra_attack_count
        security_report.assert_report_wids_detection(report_wids_detection, monitoring_wids_count)
        security_report.email_report_detail_summary_page()
        security_report.assert_close()

    def test_ath_9223_security_summary_report(self):
        """

        1) Create Security Summary report with different time spans, i.e., 1 week, 1 month, 1 year, etc., with email run report set to "Now".
        2) Select a report in completed status and delete it.
        3) Repeat the same with run report  is "Scheduled for later".
        4) Select a report in scheduled status and delete it.
        5) Create and cancel report
        Repeat steps 1 and 2 above with Email option enabled.
        Click on Create New Report and then cancel it.
        Repeat steps 1 to 4 using custom range time span. Include 1 day report to it.
        """
        security_report = self.LeftPanel.go_to_reports_security()
        security_report.delete_all_reports()
        last_day_report = security_report.create_security_report("Last day","Now",self.config.config_vars.one_time)
        last_week_report = security_report.create_security_report("Last week","Now",self.config.config_vars.one_time)
        last_month_report = security_report.create_security_report("Last month","Now",self.config.config_vars.one_time)
        last_year_report = security_report.create_security_report("Last year","Now",self.config.config_vars.one_time)
        security_report.verify_report_generation(last_day_report)
        security_report.verify_report_generation(last_week_report)
        security_report.verify_report_generation(last_month_report)
        security_report.verify_report_generation(last_year_report)
        security_report.delete_security_report(last_day_report)
        security_report.delete_all_reports()
        last_day_report = security_report.create_security_report("Last day","Daily",self.config.config_vars.one_time)
        last_week_report = security_report.create_security_report("Last week","Later",self.config.config_vars.one_time)
        last_month_report = security_report.create_security_report("Last month","Later",self.config.config_vars.one_time)
        last_year_report = security_report.create_security_report("Last year","Later",self.config.config_vars.one_time)
        security_report.verify_report_generation(last_day_report,"Scheduled")
        security_report.verify_report_generation(last_week_report,"Scheduled")
        security_report.verify_report_generation(last_month_report,"Scheduled")
        security_report.verify_report_generation(last_year_report,"Scheduled")
        
        security_report.delete_security_report(last_day_report)
        security_report.delete_all_reports()
        
        
        last_day_report = security_report.create_security_report("Last day","Now",self.config.config_vars.one_time,"enabled")
        last_week_report = security_report.create_security_report("Last week","Now",self.config.config_vars.one_time,"enabled")
        last_month_report = security_report.create_security_report("Last month","Now",self.config.config_vars.one_time,"enabled")
        last_year_report = security_report.create_security_report("Last year","Now",self.config.config_vars.one_time,"enabled")
        security_report.verify_report_generation(last_day_report)
        security_report.verify_report_generation(last_week_report)
        security_report.verify_report_generation(last_month_report)
        security_report.verify_report_generation(last_year_report)
        security_report.delete_security_report(last_day_report)
        security_report.delete_all_reports()
        last_day_report = security_report.create_security_report("Last day","Later",self.config.config_vars.one_time,"enabled")
        last_week_report = security_report.create_security_report("Last week","Later",self.config.config_vars.one_time,"enabled")
        last_month_report = security_report.create_security_report("Last month","Later",self.config.config_vars.one_time,"enabled")
        last_year_report = security_report.create_security_report("Last year","Later",self.config.config_vars.one_time,"enabled")
        security_report.verify_report_generation(last_day_report,"Scheduled")
        security_report.verify_report_generation(last_week_report,"Scheduled")
        security_report.verify_report_generation(last_month_report,"Scheduled")
        security_report.verify_report_generation(last_year_report,"Scheduled")
        security_report.delete_security_report(last_day_report)
        security_report.delete_all_reports()
        last_day_report = security_report.create_security_report("Custom range","Now","enabled")
        security_report.verify_report_generation(last_day_report)
        security_report.delete_all_reports()
        security_report.assert_delete_button_disabled()


    def test_ath_8923_time_span_peiodic(self):
        """
        1. Create perioidic reports for time span (All Group Level)
        a> Last Day
        b> Last Week
        c> Last Month
        d> Last Year

        2. Create perioidic reports for time span (Group Level)
        a> Last Day
        b> Last Week
        c> Last Month
        d> Last Year

        3.  Create perioidic reports for time span (VC Level)
        a> Last Day
        b> Last Week
        c> Last Month
        d> Last Year
        """

        log.info("Go To Reports => Security Page")
        overview_page = self.LeftPanel.goto_monitoringPage()
        security_report = self.LeftPanel.go_to_reports_security()
        overview_page.go_to_all_groups_page()

        log.info("Delete all the existing reports")
        security_report.delete_all_reports()
        log.info("STEP: Creating reports at ALL GROUP LEVEL")
        log.info("Creating Daily report for Last Day")
        last_day_report = security_report.create_security_report("Last day","Now",self.config.config_vars.repeat_daily_interval)
        security_report.verify_report_generation(last_day_report)
        assert(security_report.verify_report_scheduled_type(last_day_report,"Daily"),True)
        log.info("Verify Another report should be scheduled for the periodic report")
        report_scheduled = last_day_report + 1
        security_report.verify_report_generation(report_scheduled,"Scheduled")
        log.info("Verify report type is Daily")
        assert(security_report.verify_report_scheduled_type(report_scheduled,"Daily"),True)
        security_report.delete_all_reports()

        log.info("Creating Weekly report for Last Week")
        last_week_report = security_report.create_security_report("Last week","Now",self.config.config_vars.repeat_weekly_interval)
        security_report.verify_report_generation(last_week_report)
        assert(security_report.verify_report_scheduled_type(last_week_report,"Weekly"),True)
        log.info("Verify Another Weekly report should be scheduled for the periodic report")
        report_scheduled = last_day_report + 1
        security_report.verify_report_generation(report_scheduled,"Scheduled")
        log.info("Verify report type is Weekly")
        assert(security_report.verify_report_scheduled_type(report_scheduled,"Weekly"),True)
        security_report.delete_all_reports()

        log.info("Creating Monthly report for Last Month")
        last_month_report = security_report.create_security_report("Last month","Now",self.config.config_vars.repeat_monthly_interval)
        security_report.verify_report_generation(last_month_report)
        assert(security_report.verify_report_scheduled_type(last_month_report,"Monthly"),True)
        log.info("Verify Another Monthly report should be scheduled for the periodic report")
        time.sleep(1)
        report_scheduled = last_month_report + 1
        security_report.verify_report_generation(report_scheduled,"Scheduled")
        log.info("Verify report type is Monthly")
        assert(security_report.verify_report_scheduled_type(report_scheduled,"Monthly"),True)
        security_report.delete_all_reports()

        last_year_report = security_report.create_security_report("Last year","Now",self.config.config_vars.repeat_yearly_interval)
        security_report.verify_report_generation(last_year_report)
        assert(security_report.verify_report_scheduled_type(last_year_report,"Yearly"),True)
        log.info("Verify Another Yearly report should be scheduled for the periodic report")
        report_scheduled = last_year_report + 1
        time.sleep(1)
        security_report.verify_report_generation(report_scheduled,"Scheduled")
        log.info("Verify report type is Yearly")
        assert(security_report.verify_report_scheduled_type(report_scheduled,"Yearly"),True)
        security_report.delete_all_reports()




        overview_page.go_to_default_group()
        time.sleep(2)


        log.info("STEP: Creating reports at DEFAULT GROUP LEVEL")
        log.info("Creating Daily report for Last Day")
        last_day_report = security_report.create_security_report("Last day","Now",self.config.config_vars.repeat_daily_interval)
        security_report.verify_report_generation(last_day_report)
        assert(security_report.verify_report_scheduled_type(last_day_report,"Daily"),True)
        log.info("Verify Another report should be scheduled for the periodic report")
        report_scheduled = last_day_report + 1
        security_report.verify_report_generation(report_scheduled,"Scheduled")
        log.info("Verify report type is Daily")
        assert(security_report.verify_report_scheduled_type(report_scheduled,"Daily"),True)
        security_report.delete_all_reports()

        log.info("Creating Weekly report for Last Week")
        last_week_report = security_report.create_security_report("Last week","Now",self.config.config_vars.repeat_weekly_interval)
        security_report.verify_report_generation(last_week_report)
        assert(security_report.verify_report_scheduled_type(last_week_report,"Weekly"),True)
        log.info("Verify Another Weekly report should be scheduled for the periodic report")
        report_scheduled = last_day_report + 1
        security_report.verify_report_generation(report_scheduled,"Scheduled")
        log.info("Verify report type is Weekly")
        assert(security_report.verify_report_scheduled_type(report_scheduled,"Weekly"),True)
        security_report.delete_all_reports()

        log.info("Creating Monthly report for Last Month")
        last_month_report = security_report.create_security_report("Last month","Now",self.config.config_vars.repeat_monthly_interval)
        security_report.verify_report_generation(last_month_report)
        assert(security_report.verify_report_scheduled_type(last_month_report,"Monthly"),True)
        log.info("Verify Another Monthly report should be scheduled for the periodic report")
        time.sleep(1)
        report_scheduled = last_month_report + 1
        security_report.verify_report_generation(report_scheduled,"Scheduled")
        log.info("Verify report type is Monthly")
        assert(security_report.verify_report_scheduled_type(report_scheduled,"Monthly"),True)
        security_report.delete_all_reports()

        last_year_report = security_report.create_security_report("Last year","Now",self.config.config_vars.repeat_yearly_interval)
        security_report.verify_report_generation(last_year_report)
        assert(security_report.verify_report_scheduled_type(last_year_report,"Yearly"),True)
        log.info("Verify Another Yearly report should be scheduled for the periodic report")
        report_scheduled = last_year_report + 1
        time.sleep(1)
        security_report.verify_report_generation(report_scheduled,"Scheduled")
        log.info("Verify report type is Yearly")
        assert(security_report.verify_report_scheduled_type(report_scheduled,"Yearly"),True)
        security_report.delete_all_reports()


        security_report.go_to_vc()
        time.sleep(2)
        log.info("STEP: Creating reports at VC LEVEL")
        log.info("Creating Daily report for Last Day")
        last_day_report = security_report.create_security_report("Last day","Now",self.config.config_vars.repeat_daily_interval)
        security_report.verify_report_generation(last_day_report)
        assert(security_report.verify_report_scheduled_type(last_day_report,"Daily"),True)
        log.info("Verify Another report should be scheduled for the periodic report")
        report_scheduled = last_day_report + 1
        security_report.verify_report_generation(report_scheduled,"Scheduled")
        log.info("Verify report type is Daily")
        assert(security_report.verify_report_scheduled_type(report_scheduled,"Daily"),True)
        security_report.delete_all_reports()

        log.info("Creating Weekly report for Last Week")
        last_week_report = security_report.create_security_report("Last week","Now",self.config.config_vars.repeat_weekly_interval)
        security_report.verify_report_generation(last_week_report)
        assert(security_report.verify_report_scheduled_type(last_week_report,"Weekly"),True)
        log.info("Verify Another Weekly report should be scheduled for the periodic report")
        report_scheduled = last_day_report + 1
        security_report.verify_report_generation(report_scheduled,"Scheduled")
        log.info("Verify report type is Weekly")
        assert(security_report.verify_report_scheduled_type(report_scheduled,"Weekly"),True)
        security_report.delete_all_reports()

        log.info("Creating Monthly report for Last Month")
        last_month_report = security_report.create_security_report("Last month","Now",self.config.config_vars.repeat_monthly_interval)
        security_report.verify_report_generation(last_month_report)
        assert(security_report.verify_report_scheduled_type(last_month_report,"Monthly"),True)
        log.info("Verify Another Monthly report should be scheduled for the periodic report")
        time.sleep(1)
        report_scheduled = last_month_report + 1
        security_report.verify_report_generation(report_scheduled,"Scheduled")
        log.info("Verify report type is Monthly")
        assert(security_report.verify_report_scheduled_type(report_scheduled,"Monthly"),True)
        security_report.delete_all_reports()

        last_year_report = security_report.create_security_report("Last year","Now",self.config.config_vars.repeat_yearly_interval)
        security_report.verify_report_generation(last_year_report)
        assert(security_report.verify_report_scheduled_type(last_year_report,"Yearly"),True)
        log.info("Verify Another Yearly report should be scheduled for the periodic report")
        report_scheduled = last_year_report + 1
        time.sleep(1)
        security_report.verify_report_generation(report_scheduled,"Scheduled")
        log.info("Verify report type is Yearly")
        assert(security_report.verify_report_scheduled_type(report_scheduled,"Yearly"),True)
        security_report.delete_all_reports()

    def test_ath_8924_time_span_custom_range(self):
        """
        1
            1.  Select custom range option from Time span.
            Expectd : Repeat option is not available

        2. Click on Create button without selecting start date or End date or both.
        3. Select Custom range option where end date is less than start date.
        4. 1. Select custom range option with start time less than end time and create report with Run Report set to NOW.
        5. Select custom range report with start date is less than end date, and Run Report set to Schedule for later (run it after a day or two from end date).
        6. Create custom range report with email option

        """
        log.info("SETUP")
        log.info("Navigate to Reports Security")
        security_report = self.LeftPanel.go_to_reports_security()
        log.info("Delete Existing Reports")
        security_report.delete_all_reports()
        log.info("STEP2. Verify Repeat Option Disabled")
        security_report.verify_repeat_option_disabled_for_custom_report()
        log.info("STEP2.1. Verify Report generation with default start and end date")
        security_report.create_custom_report_without_selecting_dates()
        security_report.verify_report_generation()
        security_report.delete_all_reports()
        log.info("STEP3. Select Custom range option where end date is less than start date")
        security_report.verify_end_date_greater_than_start_date_shows_error()
        log.info("STEP4: Select custom range option with start time less than end time and create report with Run Report set to NOW.")
        security_report.create_custom_report_prev_day("Now")
        security_report.verify_report_generation()
        security_report.delete_all_reports()
        log.info("STEP 5: Select custom range report with start date is less than end date, and Run Report set to Schedule for later")
        security_report.create_custom_report_prev_day("Later")
        security_report.verify_report_generation(1,"Scheduled")
        security_report.delete_all_reports()
        log.info("STEP6: Create Custom report with email enabled")
        security_report.create_security_report("Custom range","Now",self.config.config_vars.one_time,"enabled")
        security_report.verify_report_generation()
        security_report.delete_all_reports()

        #security_report.verify_report_generation(report, "Completed")
        log.info("Security")
        security_report.delete_all_reports()
        report = security_report.create_security_report("Custom range","Now","enabled")
        security_report.verify_report_generation(report, "Completed")

        security_report.delete_all_reports()
        report = security_report.create_security_report("Custom range","Later","enabled")
        security_report.verify_report_generation(report, "Scheduled")
        security_report.delete_all_reports()

    def test_ath_8943_detail_report_fields(self):
        """
        1  Click on report that is completed.
         :return:
        """
        log.info("STEP 1 : Click on report that is completed.")
        security_report = self.LeftPanel.go_to_reports_security()
        security_report.delete_all_reports()
        last_day_report = security_report.create_security_report("Last day", "Now", self.config.config_vars.one_time)
        security_report.verify_report_generation(last_day_report)
        security_report.go_to_first_report()

        security_report.assert_all_label()
        log.info("END OF TEST CASE : 8943")
