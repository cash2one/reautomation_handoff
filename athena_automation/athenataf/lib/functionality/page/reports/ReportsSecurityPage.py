from athenataf.lib.util.WebPage import WebPage
import traceback
import logging

logger = logging.getLogger('athenataf')
import time
import datetime


class ReportsSecurityPage(WebPage):
    report_num = 0
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "ReportsSecurity", test, browser, config)
        self.test.assertPageLoaded(self)


    def isPageLoaded(self):
        if self.create_new:
            return True
        else:
            return False

    def create_new_report(self):
        '''
        clicks on create new report
        '''
        logger.debug("Report_Security: Clicking on Create new report")
        self.create_new.click()
        time.sleep(8)
        logger.debug("Report_Security: Clicking on Create button")
        self.create.click()
        return 1

    def create_security_report(self,time_span,run_report,repeat,email="disabled",device_groups="all_groups",email_id=None):
        '''
        create report for security
        '''
        logger.debug("ReportsSecurityPage: clicking on 'CreateNewReport' button")
        self.create_new.click()
        time.sleep(2)
        logger.debug("ReportsSecurityPage: select the timespan")
        self.set_time_span(time_span)
        if run_report == 'Now':
            logger.debug("ReportsSecurityPage: click on 'now' Radio-Button")
            self.run_report_now.click()
        else:
            logger.debug("ReportsSecurityPage: click on 'Schedule For Later' Radio-Button ")
            self.run_report_schedule_for_later.click()
            logger.debug("ReportsSecurityPage: click on textbox ")
            self.run_report_schedule_later_date.send_keys("")
            time.sleep(2)
            self.next_month.click()
            time.sleep(2)
            logger.debug("ReportsSecurityPage: selecting date 15 ")
            self.date_22.click()
            time.sleep(2)
        if time_span != "Custom range":
            self.report_repeat.set(repeat)

        if email == 'enabled':
            if not self.email_report.is_selected():
                if not email_id:
                    logger.debug("ReportsSecurityPage: check the checkbox 'email'")
                    self.email_report.click()
                    logger.debug("ReportsSecurityPage: writing email id in 'email' textbox ")
                    self.report_email.set(self.config.config_vars.report_email)
                else:
                    logger.debug("ReportsSecurityPage: check the checkbox 'email'")
                    self.email_report.click()
                    logger.debug("ReportsSecurityPage: writing email id in 'email' textbox ")
                    self.report_email.set(email_id)
        else:
            if self.email_report.is_selected():
                logger.debug("ReportsSecurityPage: uncheck the checkbox 'email'")
                self.email_report.click()
        logger.debug("ReportsSecurityPage: clicking on 'Create' button")
        self.create.click()
        time.sleep(5)
        self.report_num = self.report_num + 1
        return self.report_num

    def verify_repeat_option_disabled_for_custom_report(self):

        logger.debug("ReportsSecurityPage: clicking on 'CreateNewReport' button")
        self.create_new.click()
        time.sleep(2)
        logger.debug("ReportsSecurityPage: select the timespan")
        self.set_time_span("Custom range")
        if self.report_repeat:
            raise AssertionError("ReportsSecurityPage: Should not contain Repeat button with Custom range")
        else:
            logger.info("ReportsSecurityPage:PASS Does not contain repeat option")
            self.cancel.click()


    def create_custom_report_without_selecting_dates(self):
        logger.debug("ReportsSecurityPage: clicking on 'CreateNewReport' button")
        self.create_new.click()
        time.sleep(2)
        logger.debug("ReportsSecurityPage: select the timespan")
        self.set_time_span("Custom range")
        logger.debug("ReportsSecurityPage: clicking on 'Create' button")
        self.create.click()
        report_title = self.first_report_title.text
        logger.info("ReportsSecurityPage: Reports title: %s" %report_title)
        import re
        match = re.match(r"(?P<title>.*?-) (?P<start_date>.*?-) (?P<end_date>.*)", report_title)
        starting_date = match.group("start_date").replace("-","").strip()
        ending_date  = match.group("end_date").strip()
        if starting_date != ending_date:
            raise AssertionError("ReportsSecurityPage: Default timespan selected is not same for start: %s and end date: %s "%(starting_date,ending_date))
        logger.info("ReportsSecurityPage:PASS Creates correct title for the report with default option")

    def verify_end_date_greater_than_start_date_shows_error(self):
        logger.debug("ReportsSecurityPage: clicking on 'CreateNewReport' button")
        self.create_new.click()
        time.sleep(2)
        logger.debug("ReportsSecurityPage: select the timespan")
        self.set_time_span("Custom range")
        logger.debug("ReportsSecurityPage: Click on end_date")
        self.end_date.send_keys("")
        self.calendar_prev_month.click()
        self.date_22.click()
        logger.debug("ReportsSecurityPage: clicking on 'Create' button")
        self.create.click()
        if not self.confirm_end_date_less_than_start:
            raise AssertionError("ReportsSecurityPage: Report Created with End Date less than start date ")
        self.warning_button_ok.click()
        self.cancel.click()
        logger.info("ReportsSecurityPage:PASS Report not generated for END date lower then satrt date")

    def create_custom_report_prev_day(self, run_report):
        logger.debug("ReportsSecurityPage: clicking on 'CreateNewReport' button")
        self.create_new.click()
        time.sleep(2)
        logger.debug("ReportsSecurityPage: select the timespan")
        self.set_time_span("Custom range","prev")
        if run_report == 'Now':
            logger.debug("ReportsSecurityPage: click on 'now' Radio-Button")
            self.run_report_now.click()
        else:
            logger.debug("ReportsSecurityPage: click on 'Schedule For Later' Radio-Button ")
            self.run_report_schedule_for_later.click()
            logger.debug("ReportsSecurityPage: click on textbox ")
            self.run_report_schedule_later_date.send_keys("")
            self.next_month.click()
            logger.debug("ReportsSecurityPage: selecting date 15 ")
            self.date_22.click()
            time.sleep(2)
        self.create.click()

        logger.info("ReportsSecurityPage:PASS Report generated for previous day")


    def set_time_span(self, value, custom_span=None):
        '''
        selects time-span
        '''
        if value == 'Last week':
            self.time_span.set(self.config.config_vars.last_week)
        elif value == 'Last month':
            self.time_span.set(self.config.config_vars.last_month)
        elif value == 'Last year':
            self.time_span.set(self.config.config_vars.last_year)
        elif value == 'Custom range':
            self.time_span.set(self.config.config_vars.custom_range)
            if custom_span == "prev":
                self.set_prev_day()

        else:
            self.time_span.set(self.config.config_vars.last_day)


    def set_prev_day(self):
        today = datetime.date.today()
        yesterday = datetime.date.fromordinal(datetime.date.today().toordinal()-1)
        yesterday_date = yesterday.day
        self.start_date.send_keys("")
        if today.day == 1:
            self.calendar_prev_month.click()
        date =self.browser._browser.find_element_by_xpath("//a[text()='%s']" %yesterday_date)
        logger.info("ReportsSecurityPage: Clicking on date %s" %yesterday_date)

        date.click()

    def select_start_and_end_date(self):
        time.sleep(4)
        logger.debug("SecurityPage: clicking start date textbox")
        self.start_date.send_keys("")
        self.calendar_prev_month.click()
        self.date_22.click()

    def set_run_report(self, value):
        '''
        selects now or schedule for later
        '''
        if value == 'Now':
            self.run_report_now.click()
        elif value == 'Schedule for later':
            self.run_report_schedule_for_later.click()

    def set_repeat(self, value):
        '''
        selects repeat value
        '''
        if value == 'One Time':
            logger.debug("SecurityPage: Selecting one-time")
            self.report_repeat.set(self.config.config_vars.one_time)
        elif value == 'Daily Interval':
            logger.debug("SecurityPage: Selecting daily interval")
            self.report_repeat.set(self.config.config_vars.daily_interval)
        elif value == 'Weekly Interval':
            logger.debug("SecurityPage: Selecting weekly interval")
            self.report_repeat.set(self.config.config_vars.weekly_interval)
        elif value == 'Monthly Interval':
            logger.debug("SecurityPage: Selecting monthly interval")
            self.report_repeat.set(self.config.config_vars.monthly_interval)
        elif value == 'Yearly Interval':
            logger.debug("SecurityPage: Selecting yearly interval")
            self.report_repeat.set(self.config.config_vars.yearly_interval)
        elif value == 'Custom range':
            logger.debug("SecurityPage: Selecting custom range")
            self.report_repeat.set(self.config.config_vars.custom_range)

    def create_report(self):
        '''
        clicks on create button
        '''
        logger.debug('SecurityPage: Clicking on create button')
        self.create.click()
        time.sleep(5)

    def cancel_report(self):
        '''
        clicks on cancel button
        '''
        logger.debug("SecurityPage: Clicking on cancel button")
        self.cancel.click()
        time.sleep(3)

    def set_email_report(self):
        '''
        selects email report check-box

        '''
        if not self.email_report.is_selected():
            logger.debug("SecurityPage: clicking on email report check-box")
            self.email_report.click()
            self.report_email.set(self.config.config_vars.email_security)

    def set_schedule_time(self, time):
        '''
        Selects schedule time
        '''
        if time == '1:00 AM':
            self.time_list.set(self.config.config_vars.one_am)
        if time == '2:00 AM':
            self.time_list.set(self.config.config_vars.two_am)
        if time == '3:00 AM':
            self.time_list.set(self.config.config_vars.three_am)
        if time == '4:00 AM':
            self.time_list.set(self.config.config_vars.four_am)
        if time == '5:00 AM':
            self.time_list.set(self.config.config_vars.five_am)
        if time == '6:00 AM':
            self.time_list.set(self.config.config_vars.six_am)
        if time == '7:00 AM':
            self.time_list.set(self.config.config_vars.seven_am)
        if time == '8:00 AM':
            self.time_list.set(self.config.config_vars.eight_am)
        if time == '9:00 AM':
            self.time_list.set(self.config.config_vars.nine_am)
        if time == '10:00 AM':
            self.time_list.set(self.config.config_vars.ten_am)
        if time == '11:00 AM':
            self.time_list.set(self.config.config_vars.eleven_am)
        if time == '12:00 AM':
            self.time_list.set(self.config.config_vars.twelve_am)
        if time == '1:00 PM':
            self.time_list.set(self.config.config_vars.one_pm)
        if time == '2:00 PM':
            self.time_list.set(self.config.config_vars.two_pm)
        if time == '3:00 PM':
            self.time_list.set(self.config.config_vars.three_pm)
        if time == '4:00 PM':
            self.time_list.set(self.config.config_vars.four_pm)
        if time == '5:00 PM':
            self.time_list.set(self.config.config_vars.five_pm)
        if time == '6:00 PM':
            self.time_list.set(self.config.config_vars.six_pm)
        if time == '7:00 PM':
            self.time_list.set(self.config.config_vars.seven_pm)
        if time == '8:00 PM':
            self.time_list.set(self.config.config_vars.eight_pm)
        if time == '9:00 PM':
            self.time_list.set(self.config.config_vars.nine_pm)
        if time == '10:00 PM':
            self.time_list.set(self.config.config_vars.ten_pm)
        if time == '11:00 PM':
            self.time_list.set(self.config.config_vars.eleven_pm)

    def select_scheduled_report(self):
        if self.scheduled_one:
            logger.debug("SecurityPage: selecting scheduled report")
            self.scheduled_one.click()
        if self.scheduled_two:
            logger.debug("SecurityPage: selecting scheduled report")
            self.scheduled_two.click()
        if self.scheduled_three:
            logger.debug("SecurityPage: selecting scheduled report")
            self.scheduled_three.click()

    def select_completed_report(self):
        if self.completed_one:
            logger.debug("SecurityPage: selecting completed report")
            self.completed_one.click()
        if self.completed_two:
            logger.debug("SecurityPage: selecting completed report")
            self.completed_two.click()
        if self.completed_three:
            logger.debug("SecurityPage: selecting completed report")
            self.completed_three.click()

    def delete_reports(self):
        if self.delete_report:
            logger.debug("SecurityPage: Clicking on delete button")
            self.delete_report.click()
            self.browser.accept_alert()
            time.sleep(4)
    
    def buy_time(self):
        time.sleep(2)
        

    def select_title(self):
        time.sleep(4)
        logger.debug("SecurityPage: Selecting title checkbox")
        self.title.click()




        #self.start_date.set(self.config.config_vars.sep_22)
        # time.sleep(4)
        #         logger.debug("SecurityPage: selecting date")
        #         self.date_22.click()
        #         logger.debug("SecurityPage: Clicking end date textbox")
        #         self.end_date.click()

    def verify_report_generation(self,report_number=1,expected_status="Completed"):
        '''
        Verify the new report generated within some delay
        '''
        max_wait_time = int(self.config.config_vars.report_generation_max_time)
        total_wait_time_elapsed = 0
        time_interval = max_wait_time / 5
        report_completion_flag = False
        for slot in range(5):
            logger.debug("Max wait time: %s s,Total Time elapsed: %s s" %(max_wait_time,total_wait_time_elapsed))
            time.sleep(time_interval)
            total_wait_time_elapsed = total_wait_time_elapsed + time_interval
            report_completion_flag = self.verify_report_completion(report_number,expected_status)
            if report_completion_flag:
                break
        if report_completion_flag:
            logger.info("PASS: Report generation is completed successfully in %s seconds" %total_wait_time_elapsed)
        else:
            logger.info("FAIL: Report generation is not completed within maximum range wait time: %s s" %max_wait_time)
            raise AssertionError("Report generation is not completed  within maximum range wait time: %s s" %max_wait_time)

        time.sleep(5)

    def verify_report_completion(self,report_number=1,expected_status="Completed"):
        '''
        Verify the new report completed
        '''
        #table = self.pci_compliance_reports_table
        table = self.browser._browser.find_element_by_xpath("//table[@id='security_summary_reportsTable']/tbody")
        all_reports_statuses = table.find_elements_by_xpath("//td[6]/span[2]")
        report_status = all_reports_statuses[-report_number].text
        if report_status == expected_status:
            logger.info("ReportsSecurityPage: Report status is: %s" %expected_status)
            return True
        else:
            logger.info("ReportsSecurityPage: Report status is not 'completed'. Existing status: %s" %report_status)
            return False

    def go_to_verify_report(self,report_number=1):
        '''
        Verify the new report generated within some delay
        '''

        table = self.browser._browser.find_element_by_xpath("//table[@id='security_summary_reportsTable']/tbody")
        all_reports_title = table.find_elements_by_xpath("//td[2]/span[2][@id]")
        all_reports_title = [x for x in all_reports_title if x.text]
        report_title = all_reports_title[-report_number]
        logger.info("ReportsSecurityPage: Clicking on the report ")
        report_title.click()
        time.sleep(4)
        if self.report_details_close_button:

            return True
        else:
            return False

    def verify_report_scheduled_type(self, report_number, expected_status):
        '''
        Verify the new report completed
        '''
        table = self.browser._browser.find_element_by_xpath("//table[@id='security_summary_reportsTable']/tbody")
        all_reports_statuses = table.find_elements_by_xpath("//td[7]/span[2]")
        report_status = all_reports_statuses[-report_number].text
        if report_status == expected_status:
            logger.info("Report scheduled_type is '%s'" % expected_status)
            return True
        else:
            logger.info("Report scheduled type is not '%s'. Existing scheduledtype: %s" % (expected_status, report_status))
            return False



    def get_report_count(self, table_type):
        if table_type.lower() == "wids":
            logger.info("ReportsSecurityPage: Fetching security table values ")
            table_id = "security_summary_reportsTable"
        if table_type.lower() == "aps":
            logger.info("ReportsSecurityPage:  Fetching aps table values ")
            table_id = "reports_sec_rogue_aps_list"

        all_rows = self.browser._browser.find_elements_by_xpath("//table[@id='%s']/tbody/tr" %table_id)
        all_rows_count = len(all_rows)
        logger.info("ReportsSecurityPage:  Count for %s : %d " %(table_type,all_rows_count))
        if all_rows_count > 0:
            return all_rows_count-1
        else:
            return 0




    def get_security_report_title(self):
        return self.security_report_title.text


    def assert_reports_rogue_values(self, report_rogue_ap, monitoring_rogue_aps):

        if not (report_rogue_ap-2 <=   monitoring_rogue_aps <= report_rogue_ap+2):
            logger.info("ReportsSecurityPageRogueAP: Count for Report rogue ap ( %d) does not match monitoring value (%d) " %(report_rogue_ap,monitoring_rogue_aps ))
            return
        logger.info("ReportsSecurityPage:PASS Rogue AP's value matches for Monitoring and Report Page")

    def assert_report_wids_detection(self, report_wids_detection,monitoring_wids_count):
        if not (report_wids_detection-5 <=   monitoring_wids_count <= report_wids_detection+5):
            raise AssertionError("ReportsSecurityPageRogueAP: Count for Report wids( %d) does not match monitoring value (%d):  Redmine Bug no :28871 " %(report_wids_detection,monitoring_wids_count ))
            return
        logger.info("ReportsSecurityPage:PASS Rogue WIDS value matches for Monitoring and Report Page")


   
    def email_report_detail_summary_page(self):
        logger.debug("ReportsSecurityPage: Clicking on email id")
        self.report_details_email_button.click()

        time.sleep(2)
        logger.debug("ReportsSecurityPage: Writing Email id")
        self.email_textbox.set(self.config.config_vars.email_security)
        time.sleep(2)
        logger.debug("ReportsSecurityPage: Clicking on ok button")
        self.email_send_button.click()
        if not self.success_msg:
            raise AssertionError("Mail is not  sent successfully .Traceback: %s " %traceback.format_exc())


    def assert_close(self):
        self.report_details_close_button.click()
        if not self.create_new:
            raise AssertionError("ReportsSecurityPage:Close button did not work")

        logger.info("ReportsSecurityPage:Closed the report")

    def delete_all_reports(self,type=None):
        '''
        Delete the reports
        '''
        time.sleep(2)
        if not self.title:#When there is no groups(zero groups)
            return False
        if self.title.is_selected():
            self.title.click()
        if type == None:
            self.title.click()

        logger.debug("ReportsSecurityPage: clicking on 'Delete' button")
        self.delete_report.click()
        self.browser.accept_alert()
        time.sleep(10)
        self.report_num = 0

    def delete_security_report(self,report_number):
        '''
        select the report's checkbox and delete it
        '''
        logger.debug("ReportsSecurityPage: select the report's check box")
        table = self.browser._browser.find_element_by_xpath("//table[@id='security_summary_reportsTable']/tbody")
        all_reports_checkboxes = table.find_elements_by_xpath("//td[contains(@id, reportsTable_row_selector_)]/input[@ng-click='config.toggleRowSelection(rowIndex)']")
        all_reports_checkboxes[-report_number].click()
        logger.debug("ReportsSecurityPage: clicking on 'Delete' button")
        self.delete_report.click()
        self.browser.accept_alert()
        time.sleep(10)
        if self.report_num - 1 >= 0:
            self.report_num = self.report_num - 1
            
    def assert_delete_button_disabled(self):
        if self.delete_report.is_enabled():
            raise AssertionError("Delete button is enabled when no Test Reports are Present  %s " %traceback.format_exc())
    
    def go_to_first_report(self):
        self.first_report_title.click()
        time.sleep(5)

    def assert_group_name(self, group):
        try:
            if not self.report_group.text == group:
                raise AssertionError("Report has been created for a different group and shown here")
        except:
            pass

    def assert_saved_by_tooltip(self):
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.report_saved_by).perform()
        try:
            if not self.report_saved_by.text in self.toolTip.text:
                logger.info("SAVED BY TOOL TIP IS NOT PRESENT")
        except:
            pass

    def assert_all_label(self):

        if not self.rogue_ap_label.is_displayed():
            raise AssertionError("Rogue AP Table is not displayed")
        if not self.rogue_ap_detected_chart.is_displayed():
            raise AssertionError("Rogue AP Total chart is not displayed")
        if not self.wireless_intrusion_detected_label.is_displayed():
            raise AssertionError("Wireless_intrusion detected table is not displayed")
        if not self.wireless_intrusion_total_chart.is_displayed():
            raise AssertionError("Wireless intrusion total chart is not displayed")
        if not self.security_events_label.is_displayed():
            raise AssertionError("Security events map is not displayed")
			
			
    def email_to_user_dashboard_table(self,report_number):
        table = self.browser._browser.find_element_by_xpath("//table[@id='security_summary_reportsTable']/tbody")
        all_reports_email = table.find_elements_by_xpath("//td[8]/div/a[@id='securityReportEmailButton']")
        email_button = all_reports_email[-report_number]
        logger.info("ReportsSecurityPage: Clicking on the report ")
        email_button.click()
        self.buy_time()
        logger.debug("ReportsSecurityPage: Writing Email id")
        self.email_textbox.set(self.config.config_vars.pci_email)
        logger.debug("ReportsSecurityPage: Clicking on ok button")
        self.email_send_button.click()
        if not self.success_msg:
            logger.info("FAIL: Mail is not sent successfully")
            raise AssertionError("Mail is not  sent successfully .Traceback: %s " %traceback.format_exc())
        else:
            logger.info("PASS: Mail is sent successfully!")
        self.buy_time()
        if self.email_send_button:
            self.email_send_button.click()
            
    def verify_email_option_for_scheduled_report(self,report_number):
        table = self.browser._browser.find_element_by_xpath("//table[@id='security_summary_reportsTable']/tbody")
        all_reports_email = table.find_elements_by_xpath("//td[8]/div/a[@id='securityReportEmailButton']")
        email_button = all_reports_email[-report_number]
        error_msg_thrown = False
        try:
            email_button.click()
        except:
            error_msg_thrown = True
        if not error_msg_thrown:
            raise AssertionError("E-Mail option enabled for scheduled report")
        else:
            logger.info("PASS: E-Mail option disabled for scheduled report")
            
        
            
    def email_from_report_details_page(self,report_number):
        logger.info("ReportsSecurityPage: Clicking on the report ")
        self.go_to_report_details(report_number)
        self.report_details_email_button.click()
        self.buy_time()
        logger.debug("ReportsSecurityPage: Writing Email id")
        self.email_textbox.set(self.config.config_vars.pci_email)
        logger.debug("ReportsSecurityPage: Clicking on ok button")
        self.email_send_button.click()
        if not self.success_msg:
            raise AssertionError("Mail is not  sent successfully .Traceback: %s " %traceback.format_exc())
        self.buy_time()
        if self.email_send_button:
            self.email_send_button.click()
        logger.info("ReportsSecurityPage: Close the report ")
        self.report_details_close_button.click()
        
    def go_to_report_details(self,report_number=1):
        '''
        Verify the new report generated within some delay
        '''

        table = self.browser._browser.find_element_by_xpath("//table[@id='security_summary_reportsTable']/tbody")
        all_reports_title = table.find_elements_by_xpath("//td[2]/span[2]")
        all_reports_title = [x for x in all_reports_title if x.text]
        report_title = all_reports_title[-report_number]
        logger.info("ReportsPCICompliancePage: Clicking on the report ")
        report_title.click()










        self.buy_time()


    def go_to_vc(self):
        self.select_group_icon.click()
        time.sleep(2)
        logger.info("ReportsSecurityPage: Clicking Default Group Label")
       # self.select_default_group.click()
        logger.info("ReportsSecurityPage: Clicking On Swarm ")
        self.show_swarms.click()
        time.sleep(3)
        logger.info("ReportsSecurityPage: Clicking On VC name ")
        self.vc_name.click()
