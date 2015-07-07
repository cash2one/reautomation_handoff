from athenataf.lib.util.WebPage import WebPage
import traceback
import logging
logger = logging.getLogger('athenataf')
import time
from Device_Module.ObjectModule import Device

class ReportsNetworkPage(WebPage):
    report_num = 0
    def __init__(self, test, browser, config):
        time.sleep(8)
        WebPage.__init__(self, "ReportsNetwork", test, browser, config)
        self.test.assertPageLoaded(self)
            
        
    def isPageLoaded(self):
        if self.create_new_report:
            return True    
        else:
            return False 
                
    def buy_time(self):
        time.sleep(5)
           
    def delete_report(self,type=None):
        self.buy_time()
        if self.select_all.is_selected():
            self.select_all.click()
        if type == None:
            self.select_all.click()
        if type == 'scheduled':
            self.scheduled_status_chkbx.click()
        if type == 'completed':
            self.completed_status.click()
        self.buy_time()
        logger.debug("ReportsNetworkPage: clicking on 'Delete' Button")
        self.delete_network_report.click()
        self.browser.accept_alert()

    def create_report(self,time_span,run_report,repeat,email="disabled",device_groups="all_groups",email_id=None):

        '''
        create report for network

        '''
        logger.debug("ReportsNetworkPage: clicking on 'CreateNewReport' button")
        self.create_new_report.click()
        self.buy_time()
        logger.debug("ReportsNetworkPage: writing report name")
        report_num = self.report_num + 1
        self.custom_report_name.set("report_%s" %report_num)
        logger.debug("ReportsNetworkPage: select the timespan")
        self.time_span.set(time_span)
        if run_report == 'now':
            logger.debug("ReportsNetworkPage: click on 'now' Radio-Button")
            self.run_report_now.click()
        else:
            logger.debug("ReportsNetworkPage: click on 'Schedule For Later' Radio-Button ")
            self.run_report_schedule_for_later.click()
            logger.debug("ReportsNetworkPage: click on textbox ")
            self.run_report_schedule_later_date.send_keys("")
            time.sleep(2)
            self.next_month.click()
            time.sleep(2)
            logger.debug("ReportsNetworkPage: selecting date 15 ")
            self.date_15.click()
            self.buy_time()
        if time_span != "Custom range":
            self.report_repeat.set(repeat)

        if email == 'enabled':
            if not self.email_report.is_selected():
                if not email_id:
                    logger.debug("ReportsNetworkPage: check the checkbox 'email'")
                    self.email_report.click()
                    logger.debug("ReportsNetworkPage: writing email id in 'email' textbox ")
                    self.report_email.set(self.config.config_vars.report_email)
                else:
                    logger.debug("ReportsNetworkPage: check the checkbox 'email'")
                    self.email_report.click()

                    logger.debug("ReportsNetworkPage: writing email id in 'email' textbox ")
                    self.report_email.set(email_id)
        else:
            if self.email_report.is_selected():
                logger.debug("ReportsNetworkPage: uncheck the checkbox 'email'")
                self.email_report.click()
        if device_groups != "all_groups":
            self.device_groups.send_keys("%s\r" %device_groups)
                       
        logger.debug("ReportsNetworkPage: clicking on 'Create' button")
        self.create.click()
        time.sleep(5)

        self.report_num = report_num
        return self.report_num

    def create_and_cancel(self):
        '''
        click on create new report and 
        click on cancel
        '''
        self.buy_time()
        logger.debug("ReportsNetworkPage: clicking on 'Create New Report' Button")
        self.create_new_report.click()
        logger.debug("ReportsNetworkPage: clicking on 'Cancel' Button")
        self.cancel_report.click()
        self.buy_time()
    
    def cancel_report_creation(self):
        '''
        clicks on cancel button
        '''
        logger.debug("NetworkPage: Clicking on cancel button")
        self.cancel_report.click()
        time.sleep(3)
        
    def check_delete_button_disabled(self):
        if not self.disabled_delete_button:
            raise AssertionError(" Delete button is enabled when no Test Reports are Present  %s " %traceback.format_exc())
    
    def export_report(self,type):
        if type == 'completed':
            if self.completed_export_11:
                self.export_11.click()

    def email_to_user_dashboard_table(self,report_number):
        table = self.browser._browser.find_element_by_xpath("//table[@id='net_summary_reportsTable']/tbody")
        all_reports_email = table.find_elements_by_xpath("//td[8]/div/a[@id='networkReportEmailButton']")
        email_button = all_reports_email[-report_number]
        logger.info("ReportsNetworkPage: Clicking on the report ")
        email_button.click()
        self.buy_time()
        logger.debug("ReportsNetworkPage: Writing Email id")
        self.email_user.set(self.config.config_vars.pci_email)
        logger.debug("ReportsNetworkPage: Clicking on ok button")
        self.email_ok.click()
        if not self.success_msg:
            raise AssertionError("Mail is not  sent successfully .Traceback: %s " %traceback.format_exc())
        self.buy_time()
        if self.email_ok:
            self.email_ok.click()
    def export_network_report(self):
        self.report_export.click()

    def delete_all_reports(self, type=None):
        '''
        Delete the reports
        '''
        self.buy_time()

        if not self.select_all:  # When there is no groups(zero groups)
            return False
        if self.select_all.is_selected():
            self.select_all.click()
        if type == None:
            self.select_all.click()
        elif type == 'scheduled':
            self.pci_scheduled_status.click()
        elif type == 'completed':
            self.pci_completed_status.click()
        logger.debug("ReportsNetworkPage: clicking on 'Delete' button")
        self.delete_network_report.click()
        self.browser.accept_alert()
        time.sleep(10)
        self.report_num = 0

    def go_to_first_report(self):
        self.first_report.click()
        self.buy_time()

    def get_ap_names(self):
        table = self.ap_table
        ap_list = []
        ap_names = table.find_elements_by_xpath("//span[contains(@id, 'reportsNetSumAPs_name_display')]")
        for ap in ap_names:
            ap_list.append(ap.text)
        return ap_list

    def assert_ap_name_present_in_ap_table(self, ap):
        myDevice = Device.getDeviceObject(ap)
        ap_name = myDevice.get("mac")
        ap_name_list = self.get_ap_names()

        if ap_name not in ap_name_list:
            raise AssertionError("IAP is not present in the AP Table of the report")
    
    def verify_email_option_for_scheduled_report(self,report_number):
        table = self.browser._browser.find_element_by_xpath("//table[@id='net_summary_reportsTable']/tbody")
        all_reports_email = table.find_elements_by_xpath("//td[8]/div/a[@id='networkReportEmailButton']")
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
        logger.info("ReportsNetworkPage: Clicking on the report ")
        self.go_to_report_details(report_number)
        self.report_details_email_button.click()
        self.buy_time()
        logger.debug("Writing Email id")
        self.email_user.set(self.config.config_vars.pci_email)
        logger.debug("ReportsNetworkPage: Clicking on ok button")
        self.email_ok.click()
        if not self.email_success_msg_details_page:
            logger.info("FAIL: Mail is not sent successfully")
            raise AssertionError("Mail is not  sent successfully .Traceback: %s " %traceback.format_exc())
        else:
            logger.info("PASS: Mail is sent successfully!")
        self.buy_time()
        if self.email_ok:
            self.email_ok.click()
        logger.info("ReportsNetworkPage: Close the report ")
        self.report_details_close_button.click()

    def verify_report_generation(self, report_number=1, expected_status="Completed"):
        '''
        Verify the new report generated within some delay
        '''
        max_wait_time = int(self.config.config_vars.report_generation_max_time)
        total_wait_time_elapsed = 0
        time_interval = max_wait_time / 5
        report_completion_flag = self.verify_report_status(report_number, expected_status)

        for slot in range(5):
            if report_completion_flag:
                break
            logger.debug("Max wait time: %s s,Total Time elapsed: %s s" % (max_wait_time, total_wait_time_elapsed))
            time.sleep(time_interval)
            total_wait_time_elapsed = total_wait_time_elapsed + time_interval
            report_completion_flag = self.verify_report_status(report_number, expected_status)
        if report_completion_flag:
            logger.info("PASS: Current Report status is '%s' which came in %s seconds" % (
                expected_status, total_wait_time_elapsed))
        else:
            logger.info("FAIL: Expected Report status: '%s' did not come within maximum range wait time: %s s" % (
                expected_status, max_wait_time))
            raise AssertionError("Expected Report status: '%s' did not come within maximum range wait time: %s s" % (
                expected_status, max_wait_time))
        time.sleep(5)

    def verify_report_status(self, report_number, expected_status):
        '''
        Verify the new report completed
        '''
        table = self.browser._browser.find_element_by_xpath("//table[@id='net_summary_reportsTable']/tbody")
        all_reports_statuses = table.find_elements_by_xpath("//td[6]/span[2]")
        report_status = all_reports_statuses[-report_number].text
        if report_status == expected_status:
            logger.info("Report status is '%s'" % expected_status)
            return True
        else:
            logger.info("Report status is not '%s'. Existing status: %s" % (expected_status, report_status))
            return False

    def verify_report_scheduled_type(self, report_number, expected_status):
        '''
        Verify the new report completed
        '''
        table = self.browser._browser.find_element_by_xpath("//table[@id='net_summary_reportsTable']/tbody")
        all_reports_statuses = table.find_elements_by_xpath("//td[7]/span[2]")
        report_status = all_reports_statuses[-report_number].text
        if report_status == expected_status:
            logger.info("Report scheduled_type is '%s'" % expected_status)
            return True
        else:
            logger.info("Report scheduled type is not '%s'. Existing scheduledtype: %s" % (expected_status, report_status))
            return False
    def assert_all_label(self):
        if not self.number_of_aps_label.is_displayed():
            raise AssertionError("NUMBER OF APS LABEL NOT PRESENT")
        if not self.ap_model_label.is_displayed():
            #raise AssertionError("AP Model is not present")
            raise AssertionError("AP MODEL LABEL NOT PRESENT")
        if not self.top_ten_wireless_clients_label.is_displayed():
            raise AssertionError("TOP TEN WIRELESS CLIENTS LABEL NOT PRESENT")
        if not self.device_types_label.is_displayed():
            raise AssertionError("DEVICE TYPES NOT PRESENT")
        if not self.top_ten_aps_usage_label.is_displayed():
            raise AssertionError("TOP TEN APs USAGE NOT PRESENT")
        if not self.top_usage_by_ssid.is_displayed():
            raise AssertionError("TOP USAGE BY SSID NOT PRESENT")
        if not self.wireless_clients_label.is_displayed():
            raise AssertionError("WIRELESS CLIENTS NOT PRESENT")
        if not self.wireless_data_usage.is_displayed():
            raise AssertionError("WIRELESS DATA USAGE NOT PRESENT")

    def close_report(self):
        self.close_detail_report.click()

    def export_from_detail_report(self):
        self.export_detail_report.click()


    def email_from_detail_report(self, email_id):
        self.report_details_email_button.click()
        self.email_id_input.send_keys(email_id)
        self.email_input_ok.click()
        logger.info(self.email_confirmation.text)
        if not self.email_confirmation.is_displayed():
            logger.info("Email is not successfully sent")

    def assert_saved_by_tooltip(self):
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.report_saved_by).perform()
        try:
            if not self.report_saved_by.text in self.toolTip.text:
                logger.info("SAVED BY TOOL TIP IS NOT PRESENT")
        except:
            pass
    def assert_group_name(self, group):
        try:
            if not self.report_group.text == group:
                raise AssertionError("Report created with another group is shown here")
        except:
            pass

    def delete_first_report(self):
        self.select_first_report.click()
        self.delete_network_report.click()
        self.browser.accept_alert()
        time.sleep(10)
        self.report_num = 0

    def delete_report(self,report_number):
        '''
        select the report's checkbox and delete it
        '''
        logger.debug("ReportsNetworkPage: select the report's check box")
        table = self.browser._browser.find_element_by_xpath("//table[@id='net_summary_reportsTable']/tbody")
        all_reports_checkboxes = table.find_elements_by_xpath("//td[contains(@id, reportsTable_row_selector_)]/input[@ng-click='config.toggleRowSelection(rowIndex)']")
        all_reports_checkboxes[-report_number].click()
        logger.debug("ReportsNetworkPage: clicking on 'Delete' button")

        self.delete_network_report.click()
        self.browser.accept_alert()
        time.sleep(10)
        if self.report_num - 1 >= 0:
            self.report_num = self.report_num - 1
            
    def go_to_report_details(self,report_number=1):
        '''
        Verify the new report generated within some delay
        '''

        table = self.browser._browser.find_element_by_xpath("//table[@id='net_summary_reportsTable']/tbody")
        all_reports_title = table.find_elements_by_xpath("//td[2]/span[2]")
        all_reports_title = [x for x in all_reports_title if x.text]
        report_title = all_reports_title[-report_number]
        logger.info("ReportsNetworkPage: Clicking on the report ")
        report_title.click()
        self.buy_time()

    def verify_repeat_option_disabled_for_custom_report(self):

        logger.debug("ReportsNewtorkPage: clicking on 'CreateNewReport' button")
        self.create_new_report.click()

        self.buy_time()
        logger.debug("ReportsNetworkPage: writing report name")
        report_num = self.report_num + 1
        self.custom_report_name.set("report_%s" %report_num)

        logger.debug("ReportsNetworkPage: select the timespan")
        self.set_time_span("Custom range")
        if self.report_repeat:
            raise AssertionError("ReportsNetworkPage: Should not contain Repeat button with Custom range")
        else:
            logger.info("ReportsNetworkPage:PASS Does not contain repeat option")
            self.cancel_report.click()

    def create_custom_report_without_selecting_dates(self):
        logger.debug("ReportsNewtorkPage: clicking on 'CreateNewReport' button")
        self.create_new_report.click()

        self.buy_time()
        logger.debug("ReportsNetworkPage: writing report name")
        report_num = self.report_num + 1
        self.custom_report_name.set("report_%s" %report_num)
        logger.debug("ReportsNetworkPage: select the timespan")
        time.sleep(2)
        self.set_time_span("Custom range")

        self.create.click()
        report_title = self.first_report_title.text
        logger.info("ReportsNetworkPage: Reports title: %s" %report_title)
        import re
        match = re.match(r"(?P<title>.*?-) (?P<start_date>.*?-) (?P<end_date>.*)", report_title)
        starting_date = match.group("start_date").replace("-","").strip()
        ending_date  = match.group("end_date").strip()
        if starting_date != ending_date:
            raise AssertionError("ReportsNetworkPage: Default timespan selected is not same for start: %s and end date: %s "%(starting_date,ending_date))
        logger.info("ReportsNetworkPage:PASS Creates correct title for the report with default option")

    def verify_end_date_greater_than_start_date_shows_error(self):
        logger.debug("ReportsNewtorkPage: clicking on 'CreateNewReport' button")
        self.create_new_report.click()

        self.buy_time()
        logger.debug("ReportsNetworkPage: writing report name")
        report_num = self.report_num + 1
        self.custom_report_name.set("report_%s" %report_num)
        logger.debug("ReportsNetworkPage: select the timespan")
        time.sleep(2)
        self.set_time_span("Custom range")

        logger.debug("ReportsNetworkPage: Click on end_date")
        self.end_date.send_keys("")
        time.sleep(2)
        self.calendar_prev_month.click()
        time.sleep(2)
        self.date_15.click()
        logger.debug("ReportsNetworkPage: clicking on 'Create' button")
        self.create.click()
        if not self.confirm_end_date_less_than_start:
            raise AssertionError("ReportsNetworkPage: Report Created with End Date less than start date ")
        self.warning_button_ok.click()
        self.cancel_report.click()
        logger.info("ReportsNetworkPage:PASS Report not generated for END date lower then satrt date")



    def create_custom_report_prev_day(self, run_report):
        logger.debug("ReportsNewtorkPage: clicking on 'CreateNewReport' button")
        self.create_new_report.click()

        self.buy_time()
        logger.debug("ReportsNetworkPage: writing report name")
        report_num = self.report_num + 1
        self.custom_report_name.set("report_%s" %report_num)
        logger.debug("ReportsNetworkPage: select the timespan")
        time.sleep(2)

        self.set_time_span("Custom range","prev")
        if run_report == 'now':
            logger.debug("ReportsNetworkPage: click on 'now' Radio-Button")
            self.run_report_now.click()
        else:
            logger.debug("ReportsNetworkPage: click on 'Schedule For Later' Radio-Button ")
            self.run_report_schedule_for_later.click()
            logger.debug("ReportsNetworkPage: click on textbox ")
            self.run_report_schedule_later_date.send_keys("")
            self.next_month.click()
            logger.debug("ReportsNetworkPage: selecting date 15 ")
            self.date_15.click()
            time.sleep(2)
        self.create.click()

        logger.info("ReportsNetworkPage:PASS Report generated for previous day")

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
        import datetime
        today = datetime.date.today()
        yesterday = datetime.date.fromordinal(datetime.date.today().toordinal()-1)
        yesterday_date = yesterday.day
        self.start_date.send_keys("")
        if today.day == 1:
            self.calendar_prev_month.click()
        date =self.browser._browser.find_element_by_xpath("//a[text()='%s']" %yesterday_date)
        logger.info("ReportsNetworkPage: Clicking on date %s" %yesterday_date)
        date.click()

    def go_to_all_groups_page(self):
        try:
            logger.info("ReportsNetworkPage: Clicking ALL Groups Tag")
            self.all_groups_tag.click()
            time.sleep(2)
        except:
            pass

    def go_to_default_group(self):
        
        self.select_group_icon.click()
        logger.info("ReportsNetworkPage: Clicking Default Group Label")
        self.select_default_group.click()
        if not self.default_group_label:
            raise AssertionError("Unable to navigate to the default group page : %s" % traceback.format_exc())


    def go_to_vc(self):
        self.select_group_icon.click()
        time.sleep(2)
        logger.info("ReportsNetworkPage: Clicking Default Group Label")
       # self.select_default_group.click()
        logger.info("ReportsNetworkPage: Clicking On Swarm ")
        self.show_swarms.click()
        time.sleep(3)
        logger.info("ReportsNetworkPage: Clicking On VC name ")
        self.vc_name.click()
