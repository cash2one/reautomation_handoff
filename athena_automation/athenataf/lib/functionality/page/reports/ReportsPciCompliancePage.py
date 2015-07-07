from athenataf.lib.util.WebPage import WebPage
import traceback
import logging
logger = logging.getLogger('athenataf')
import time
import pdb
class ReportsPciCompliancePage(WebPage):
    report_num = 0
    def __init__(self, test, browser, config):
        time.sleep(5)
        WebPage.__init__(self, "ReportsPciCompliance", test, browser, config)
        self.test.assertPageLoaded(self)

    def isPageLoaded(self):
        if self.create_new_pci_report:
            return True    
        else:
            return False

    def buy_time(self):
        time.sleep(2)

    def go_to_all_groups_page(self):
        try:
            self.all_groups_tag.click()
            time.sleep(2)
        except:
            pass
    
    def go_to_default_group(self):
        self.select_group_icon.click()
        self.select_default_group.click()
        if not self.default_group_label:
            raise AssertionError("Unable to navigate to the default group page : %s" % traceback.format_exc())
            
    def create_pci_compliance_report(self,run_report,repeat,cde_option="cde_subnets",cde_ssid=None,email="disabled",device_groups="all_groups",email_id=None, cde_subnet=None, cde_mask=None, group=None):
        '''
        create report for Pci Compliance
        '''
        logger.debug("ReportsPciCompliancePage: clicking on 'CreateNewReport' button")
        self.create_new_pci_report.click()
        if run_report == 'now':
            logger.debug("ReportsPciCompliancePage: click on 'now' Radio-Button")
            self.pci_run_report_now.click()
        else:
            logger.debug("ReportsPciCompliancePage: click on 'Schedule For Later' Radio-Button ")
            self.pci_run_report_later.click()
            logger.debug("ReportsPciCompliancePage: click on textbox ")
            self.pci_run_report_schedule_later_date.send_keys("")
            self.buy_time()
            self.pci_next_month.click()
            self.buy_time()
            logger.debug("ReportsPciCompliancePage: selecting date september 30 ")
            self.date_15.click()
            self.buy_time()
        self.report_repeat.set(repeat)
        if email == 'enabled':
            if not self.pci_email_report.is_selected():
                if not email_id:
                    logger.debug("ReportsPciCompliancePage: check the checkbox 'email'")
                    self.pci_email_report.click()
                    logger.debug("ReportsPciCompliancePage: writing email id in 'email' textbox ")
                    self.pci_report_email.set(self.config.config_vars.pci_email)
                else:
                    logger.debug("ReportsPciCompliancePage: check the checkbox 'email'")
                    self.pci_email_report.click()
                    logger.debug("ReportsPciCompliancePage: writing email id in 'email' textbox ")
                    self.pci_report_email.set(email_id)
        else:
            if self.pci_email_report.is_selected():
                logger.debug("ReportsPciCompliancePage: uncheck the checkbox 'email'")
                self.pci_email_report.click()
        if group != None:
            self.select_group(group)

        if cde_option == "cde_subnets":
            self.buy_time()
            logger.debug("ReportsPciCompliancePage: clicking on 'CDE SUBNETs' Radio Button")
            self.cde_subnets.click()
            logger.debug("ReportsPciCompliancePage: clicking on 'New'  Button")
            self.create_new_cde_subnets.click()
            logger.debug("ReportsPciCompliancePage: Writing Network ip in 'Network' TextBox")
            if cde_subnet == None:
                self.cde_subnets_network.set(self.config.config_vars.cde_subnets_network)
            else:
                self.cde_subnets_network.set(cde_subnet)
            logger.debug("ReportsPciCompliancePage: Writing NetworkMask in 'Mask' TextBox")
            if cde_mask == None:
                self.cde_subnets_mask.set(self.config.config_vars.cde_subnets_mask)
            else:
                self.cde_subnets_mask.set(cde_mask)
            logger.debug("ReportsPciCompliancePage: clicking on 'Add' button")
            self.cde_subnets_add.click()
        else:
            logger.debug("ReportsPciCompliancePage: clicking on 'CDE SSIDs' Radio Button")
            self.cde_ssids.click()
            if cde_ssid == "all_ssids":
                logger.debug("ReportsPciCompliancePage: select the 'select all cde ssids' checkbox")
                self.select_all_cde_ssids.click()
            else:
                table = self.browser._browser.find_element_by_xpath("//table[@id='cdessids_grid']")
                for tr in table.find_elements_by_tag_name("tr"):

                    check_box = tr.find_element_by_tag_name("input")
                    if tr.text == cde_ssid:
                        logger.info("ReportsPciCompliancePage: select the 'select the cde ssid: %s' checkbox" %cde_ssid)
                        check_box.click()
                        break
        if device_groups != "all_groups":
            self.device_groups.send_keys("%s\r" %device_groups)

        logger.debug("ReportsPciCompliancePage: clicking on 'Create' button")
        self.generate_pci_report.click()
        time.sleep(10)
        self.report_num = self.report_num + 1
        return self.report_num
        
    def assert_create_failure_pci_compliance_report_without_ssid(self):
        self.buy_time()
        '''
        create report for Pci Compliance
        '''
        logger.debug("ReportsPciCompliancePage: clicking on 'CreateNewReport' button")
        self.create_new_pci_report.click()
        logger.debug("ReportsPciCompliancePage: click on 'now' Radio-Button")
        self.pci_run_report_now.click()
        self.buy_time()
        logger.debug("ReportsPciCompliancePage: clicking on 'CDE SSID's Radio Button")
        self.cde_ssids.click()
        logger.debug("ReportsPciCompliancePage: clicking on 'Create' button without selecting SSID")
        self.generate_pci_report.click()
        if not self.pci_report_confirm_content:
            raise AssertionError("ReportsPciCompliancePage: Created a report without SSID")
        self.warning_button_ok.click()
        self.pci_create_new_report_close.click()
    


    def assert_create_failure_pci_compliance_report_without_cde_subnet (self):
        self.buy_time()
        '''
        create report for Pci Compliance

        '''
        logger.debug("ReportsPciCompliancePage: clicking on 'CreateNewReport' button")
        self.create_new_pci_report.click()

        logger.debug("ReportsPciCompliancePage: click on 'now' Radio-Button")
        self.pci_run_report_now.click()

        self.buy_time()
        logger.debug("ReportsPciCompliancePage: clicking on 'CDE SUBNETs' Radio Button")
        self.cde_subnets.click()

        logger.debug("ReportsPciCompliancePage: clicking on 'New'  Button")
        self.create_new_cde_subnets.click()

        logger.debug("ReportsPciCompliancePage: clicking on 'Add' button")
        self.cde_subnets_add.click()
        if not self.pci_cde_subnet_required_network:
            raise AssertionError("ReportsPciCompliancePage: Required Network is empty")
        if not self.pci_cde_subnet_required_mask:
            raise AssertionError("ReportsPciCompliancePage: Required Mask is empty")
        self.pci_create_new_report_close.click()
    
    def cancel_report(self):
        '''
        clicks on cancel button
        '''
        logger.debug("PCI Compliance Page: Clicking on cancel button")
        self.cancel_new_report.click()
        time.sleep(3)
        
    def delete_all_reports(self,type=None):
        '''
        Delete the reports
        '''
        self.buy_time()


        if not self.multiSelect:#When there is no groups(zero groups)
            return False
        if self.multiSelect.is_selected():
            self.multiSelect.click()
        if type == None:
            self.multiSelect.click()
        elif type == 'scheduled':
            self.pci_scheduled_status.click()
        elif type == 'completed':
            self.pci_completed_status.click()
        logger.debug("ReportsPciCompliancePage: clicking on 'Delete' button")
        self.delete_pci_reports.click()
        self.browser.accept_alert()
        time.sleep(10)
        self.report_num = 0

    def assert_delete_button_disabled(self):
        if self.delete_pci_reports.is_enabled():
            raise AssertionError("Delete button is enabled when no Test Reports are Present  %s " %traceback.format_exc())

    def export_pci_report(self,type):
        '''
        Export the Report
        '''
        self.buy_time()
        if type == 'completed':
            if self.pci_completed_export:
                logger.debug("ReportsPciCompliancePage: clicking on 'Export' button")
                self.pci_completed_export.click()
    def export_pci_dashboard_table(self,report_number):
        table = self.browser._browser.find_element_by_xpath("//table[@id='pci_summary_reportsTable']/tbody")
        all_export_reports = table.find_elements_by_xpath("//td[8]/div/a[@id='pciReportExportButton']")
        export_button = all_export_reports[-report_number]
        logger.info("ReportsPCICompliancePage: Clicking on the report ")
        export_button.click()
        logger.info("ReportsPCICompliancePage: File exported ")
        
    def email_to_user(self):
        '''
        Email the report to the Specified User
        '''
        self.buy_time()
        time.sleep(30)
        if self.pci_email_user_button :
            logger.debug("ReportsPciCompliancePage: clicking on 'Email' button")
            self.pci_email_user_button.click()
        logger.debug("ReportsPciCompliancePage: Writing Email id")
        self.pci_email_user.set(self.config.config_vars.pci_email)
        logger.debug("ReportsPciCompliancePage: Clicking on ok button")
        self.email_ok.click()
        if not self.success_msg:
            raise AssertionError("Mail is not  sent successfully .Traceback: %s " %traceback.format_exc())
        self.buy_time()
        if self.email_ok:
            self.email_ok.click()

    def create_and_cancel(self):
        '''
        click on create new report and 
        click on cancel
        '''
        self.buy_time()
        logger.debug("ReportsPciCompliancePage: clicking on 'Create New Report' Button")
        self.create_new_pci_report.click()
        logger.debug("ReportsPciCompliancePage: clicking on 'Cancel' Button")
        self.cancel_new_report.click()
        self.buy_time()
    def verify_report_cancellation(self):
        """
        Check if the table is empty
        """
        if self.pci_compliance_table_empty:
            return True
        else:
            raise AssertionError("ReportsPciCompliancePage: Report generated, cancel did not work. Traceback: %s" %traceback.format_exc())
        
    def check_delete_button_disabled(self):
        '''
        check Delete button is Enabled or not when,
        no reports are there
        '''
        if self.delete_pci_reports.is_enabled():
            raise AssertionError(" Delete button is enabled when no Test Reports are Present  %s " %traceback.format_exc())
            

    def verify_report_generation(self,report_number=1,expected_status="Completed"):
        '''
        Verify the new report generated within some delay
        '''
        max_wait_time = int(self.config.config_vars.report_generation_max_time)
        total_wait_time_elapsed = 0
        time_interval = max_wait_time / 5
        report_completion_flag = self.verify_report_status(report_number,expected_status)

        for slot in range(5):
            if report_completion_flag:   
                break
            logger.debug("Max wait time: %s s,Total Time elapsed: %s s" %(max_wait_time,total_wait_time_elapsed))
            time.sleep(time_interval)
            total_wait_time_elapsed = total_wait_time_elapsed + time_interval
            report_completion_flag = self.verify_report_status(report_number,expected_status)
            
        if report_completion_flag:
            logger.info("PASS: Current Report status is '%s' which came in %s seconds" %(expected_status,total_wait_time_elapsed))
        else:
            logger.info("FAIL: Expected Report status: '%s' did not come within maximum range wait time: %s s" %(expected_status,max_wait_time))
            raise AssertionError("Expected Report status: '%s' did not come within maximum range wait time: %s s" %(expected_status,max_wait_time))
        time.sleep(5)
        
    def verify_report_status(self,report_number,expected_status):
        '''
        Verify the new report completed
        '''

        table = self.browser._browser.find_element_by_xpath("//table[@id='pci_summary_reportsTable']/tbody")
        all_reports_statuses = table.find_elements_by_xpath("//td[6]/span[2]")
        report_status = all_reports_statuses[-report_number].text
        if report_status == expected_status:
            logger.info("Report status is '%s'" %expected_status)
            return True
        else:
            logger.info("Report status is not '%s'. Existing status: %s" %(expected_status, report_status))
            return False

    def delete_report(self,report_number):
        '''
        select the report's checkbox and delete it
        '''
        logger.debug("ReportsPciCompliancePage: select the report's check box")
        table = self.browser._browser.find_element_by_xpath("//table[@id='pci_summary_reportsTable']/tbody")
        all_reports_checkboxes = table.find_elements_by_xpath("//td[contains(@id, reportsTable_row_selector_)]/input[@ng-click='config.toggleRowSelection(rowIndex)']")
        all_reports_checkboxes[-report_number - 1].click()
        logger.debug("ReportsPciCompliancePage: clicking on 'Delete' button")
        self.delete_pci_reports.click()
        self.browser.accept_alert()
        time.sleep(10)
        if self.report_num - 1 >= 0:
            self.report_num = self.report_num - 1
            
    def email_to_user_dashboard_table(self,report_number):
        table = self.browser._browser.find_element_by_xpath("//table[@id='pci_summary_reportsTable']/tbody")
        all_reports_email = table.find_elements_by_xpath("//td[8]/div/a[@id='pciReportEmailButton']")
        email_button = all_reports_email[-report_number]
        logger.info("ReportsPCICompliancePage: Clicking on the report ")
        email_button.click()
        self.buy_time()
        logger.debug("ReportsPCICompliancePage: Writing Email id")
        self.pci_email_user.set(self.config.config_vars.pci_email)
        logger.debug("ReportsPCICompliancePage: Clicking on ok button")
        self.email_ok.click()
        if not self.success_msg:
            logger.info("FAIL: Mail is not sent successfully")
            raise AssertionError("Mail is not  sent successfully .Traceback: %s " %traceback.format_exc())
        else:
            logger.info("PASS: Mail is sent successfully!")
        self.buy_time()
        if self.email_ok:
            self.email_ok.click()
            
    def verify_email_option_for_scheduled_report(self,report_number):
        table = self.browser._browser.find_element_by_xpath("//table[@id='pci_summary_reportsTable']/tbody")
        all_reports_email = table.find_elements_by_xpath("//td[8]/div/a[@id='pciReportEmailButton']")
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
        logger.info("ReportsPCICompliancePage: Clicking on the report ")
        self.go_to_report_details(report_number)
        self.report_details_email_button.click()
        self.buy_time()
        logger.debug("Writing Email id")
        self.pci_email_user.set(self.config.config_vars.pci_email)
        logger.debug("ReportsPCICompliancePage: Clicking on ok button")
        self.email_ok.click()
        if not self.success_msg:
            raise AssertionError("Mail is not  sent successfully .Traceback: %s " %traceback.format_exc())
        self.buy_time()
        if self.email_ok:
            self.email_ok.click()
        logger.info("ReportsPCICompliancePage: Close the report ")
        self.report_details_close_button.click()
        
    def go_to_report_details(self,report_number=1):
        '''
        Verify the new report generated within some delay
        '''

        table = self.browser._browser.find_element_by_xpath("//table[@id='pci_summary_reportsTable']/tbody")
        all_reports_title = table.find_elements_by_xpath("//td[2]/span[2]")
        all_reports_title = [x for x in all_reports_title if x.text]
        report_title = all_reports_title[-report_number]
        logger.info("ReportsPCICompliancePage: Clicking on the report ")
        report_title.click()
        self.buy_time()
        

    def get_table_values(self):
        table_dict = dict()
        table = self.pci_report_details_table
        for tr in table.find_elements_by_tag_name("tr"):
            if tr.text.startswith("PCI"):
                continue
            value_array = tr.text.split('\n')
            for td in tr.find_elements_by_tag_name("td"):
                if td.get_attribute('title') == "false":
                    table_dict[value_array[0].strip()] = False
                else:
                    table_dict[value_array[0].strip()] = True
        return table_dict

    def assert_negative_pci_table(self, rule):
        dict = self.get_table_values()
        if not isinstance(rule, list):
            rule = rule.split(" ")
        for rul in rule:
            if dict[rul]:
                raise AssertionError("PCI Complaince %s passed" %rul)
            else:
                logger.info("Expected Rule : %s has Failed" %rul)

    def assert_pci_table(self, rule):
        dict = self.get_table_values()
        if not isinstance(rule, list):
            rule = rule.split(" ")
        for rul in rule:
            if not dict[rul]:
                raise AssertionError("PCI Complaince %s Failed" % rul)
            else:
                logger.info("Expected Rule : %s has passed" % rul)

    def go_to_first_report(self):
        self.pci_report_1.click()
        self.buy_time()

    def select_group(self, group):
        from selenium.webdriver.common.keys import Keys
        self.pci_select_group.clear()
        self.pci_select_group.send_keys(group)
        self.pci_select_group.send_keys(Keys.RETURN)
        