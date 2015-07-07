__author__ = 'aarunakirisamy'
from athenataf.lib.util.WebPage import WebPage
#from athenataf.lib.functionality.page.common.LeftPanel import LeftPanel
#import athenataf.lib.functionality.page.common.LeftPanel
import traceback
import logging
log = logging.getLogger('athenataf')
import time
import os
import re
from Device_Module.ObjectModule import Device


class MonitoringNotificationPage(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "Monitoring", test, browser, config)
        self.test.assertPageLoaded(self)

    def isPageLoaded(self):
        if self.notification_page:
            return True
        else:
            return False    
    
    def go_to_notifications_icon(self):
        self.all_page_message_icon.click()
        
    def go_to_notifications_settings(self):
        self.all_page_notifications_settings.click()
            
    def assert_notifications_icon(self):
        if self.all_page_message_icon:
            self.all_page_message_icon.click()
            if not self.all_page_notifications_close:
                raise AssertionError("Close Icon is not present")
            if not self.all_page_notifications_settings:
                raise AssertionError("Settings Icon is not present")
        else:
            raise AssertionError("Message icon does not appear : Traceback : %s" %traceback.format_exc())

    def assert_notifications_settings(self):
        if self.all_page_notifications_settings:
            self.all_page_notifications_settings.click()
            time.sleep(5)
            if not self.add_notification:
                raise AssertionError("Add notification button is not present  Traceback : %s" %traceback.format_exc())
        else:
            raise AssertionError("Settings icon is not present  Traceback : %s" %traceback.format_exc())

    def disable_all_mail_options_in_notification_settings(self):
        all_mail_options = self.browser._browser.find_elements_by_xpath("//input[contains(@id, 'notification_emailCheck_')]")
        for index in range(len(all_mail_options)):
            #Wrapper will be changed after disabling the email-option. so retrieving the objects each time
            current_mail_options = self.browser._browser.find_elements_by_xpath("//input[contains(@id, 'notification_emailCheck_')]") 
            mail_option=current_mail_options[index]
            mail_option.click()
            save_buttons = self.browser._browser.find_elements_by_xpath("//a[contains(@id, 'notification_save_')]")
            current_save_button = save_buttons[index]
            current_save_button.click()
            time.sleep(2)
            
            
                
    def delete_all_notifications_in_settings(self):
        if self.any_notification_delete:
            current_notifications = self.browser._browser.find_elements_by_xpath("//a[contains(@id, 'notification_delete_')]")
            while not current_notifications == []:
                try:
                    current_notifications[0].click()
                    time.sleep(2)
                except:
                    pass
                current_notifications = self.browser._browser.find_elements_by_xpath("//a[contains(@id, 'notification_delete_')]")
                
    def add_list_of_notifications(self,list_types,list_types_events,group,email_option = False):
        for type, type_events in zip(list_types, list_types_events):
            for event in type_events:
                log.info("Add notification for Type: \"%s\" and Event: \"%s\"" %(type,event))
                self.add_notification(type,event,group,email_option)
                self.assert_notification(event)
                
    def close_notifications(self):
        if self.notifications_settings_close:
            self.notifications_settings_close.click()
        else:
            raise AssertionError("Close Icon is not present  Traceback : %s" %traceback.format_exc())

    def add_notification(self,type,event,group,email_option):
        if self.add_notification_button:
            self.add_notification_button.click()
            self.add_notification_type.set(type)
            self.add_notification_event.set(event)
            if not type == "User Management":
                self.add_notification_group.set(group)
            if email_option:
                email = "aarunakirisamy@arubanetworks.com"
                self.enable_notification_email.click()
                self.add_notification_email.send_keys(email)
            self.add_notification_save.click()
            # if self.warning_message:
                # self.warning_ok_button.click()
                # self.add_notification_cancel.click()
        else:
            raise AssertionError("Add notification button is not present")

    def assert_notification(self,event):
        time.sleep(3)
        try:
            event_name = self.browser._browser.find_element_by_xpath("//h3[text()='%s']" %event).text
            log.info("PASS: Notification for \"%s\" is added at notification settings page" %event)
        except:
            log.info("FAIL: Notification for \"%s\" is not added at notification settings page" %event)
            raise AssertionError("Added Notification for \"%s\" is not existing.Traceback : %s" %(event,traceback.format_exc()))
            
    def verify_acknowledge_all_notifications_button(self):
        if not self.acknowledge_all_button:
            log.info("FAIL: \"Acknowledge All\" button is not existing")
            raise AssertionError("\"Acknowledge All\" link is not existing.Traceback : %s" %traceback.format_exc())
        else:
            log.info("PASS: \"Acknowledge All\" link is existing")
            
            
    def assert_acknowledge_all_notifications(self):
        if not self.acknowledge_all_button:
            log.info("FAIL: \"Acknowledge All\" button is not existing")
            raise AssertionError("\"Acknowledge All\" link is not existing.Traceback : %s" %traceback.format_exc())
        else:
            log.info("PASS: \"Acknowledge All\" link is existing")
            self.acknowledge_all_button.click()
            time.sleep(10)
            if not self.notification_count.text == '':
                log.info("FAIL: \"Acknowledge All\" link did not acknowledge all the notifications")
                raise AssertionError("\"Acknowledge All\" link did not acknowledge all the notifications")
            else:
                log.info("PASS: \"Acknowledge All\" link works which acknowledged all the notifications")
                
    def assert_show_all_notifications(self):
        self.all_page_message_icon.click()
        if not self.all_notifications:
            log.info("FAIL: \"Show All\" link is not existing")
            raise AssertionError("\"Show All\" link is not existing.Traceback : %s" %traceback.format_exc())
        else:
            log.info("PASS: \"Show All\" link is existing")
            self.all_notifications.click()
            if not self.notification_page:
                log.info("FAIL: \"Show All\" link did not take us to notification page.")
                raise AssertionError("\"Show All\" link did not take us to notification page.Traceback : %s" %traceback.format_exc())
            else:
                log.info("PASS: \"Show All\" link works which took us to notification page.")
    
    def delete_notifications_in_settings(self):
        self.go_to_notifications_icon()
        self.go_to_notifications_settings()
        self.delete_all_notifications_in_settings()
        self.close_notifications()
        
        
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

    def assert_help_option(self,element):
        '''
        asserts help text
        '''
        action_chain = self.browser.get_action_chain()
        ele_object = eval("self.%s" %element)
        action_chain.move_to_element(ele_object).perform()
        if self.help_content:
            log.info("PASS: Help text for \"%s\" is existing." %element)
        else:
            log.info("FAIL: Help text for \"%s\" is not existing/Empty." %element)
            raise AssertionError("Help content is not opened/Empty i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(1)
    
    def assert_ap_count_in_overview_page(self):
        if not int(self.check_ap_count()) == int(self.get_number_of_input_devices("iap")):
            raise AssertionError("Number of IAP in overview page does not match with given number of IAPs in Device File")

    def set_default_device(self, device):
        os.environ['device'] = device

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
            
    def disconnect_device_from_server(self, device):

        myDevice = Device.getDeviceObject(device)
        myDevice.connect_device_to_server("1.1.1.1")
        log.info(myDevice.get_device_status())
        i = 1
        while i < 10:
            log.info(myDevice.get_device_status())
            if not myDevice.get_device_status():
                break
            else:
                time.sleep(5)
            i = i + 1

        if myDevice.get_device_status():
            raise AssertionError("Device is not attached to Athena Yet")
            
    def disconnect_client_from_ap(self, device):
        myDevice = Device.getDeviceObject(device)
        try:
            myDevice.disconnect_client_from_ap()
        except:
            myDevice.connect()
            myDevice.disconnect_client_from_ap()
            pass

    def connect_client_to_ap(self, device, SSID=None):
        myDevice = Device.getDeviceObject(device)
        myDevice.connect_client_to_ap(SSID=SSID)

    def assert_wifi_client_count(self, value):
        i = 1
        while i < 10:
            if int(self.wifi_client.text) == value:
                break
            else:
                self.browser.refresh()
                time.sleep(90)
            i = i + 1
        if not int(self.wifi_client.text) == value:
            raise AssertionError("Number of IAP in overview page does not match with given number of IAPs in Device File")

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
    
    def get_notifications_count(self):
        notifications = self.notification_count.text
        if notifications == '':
            notifications = 0
        else:
            notifications = int(notifications)
        return notifications
    def verify_virtual_controller_disconnected_notification(self,group="All Groups"):
        '''
            Verify the notification should be created when virtual controller is disconnected
        '''    
        self.go_to_notifications_icon()
        self.go_to_notifications_settings()
        log.info("Click on Add Notification for enabling Device Notification for Virtual Controller disconnected  ")
        self.add_notification("Device","Virtual controller disconnected","All Groups",False)
        self.close_notifications()
        log.info("Get the notifications count before disconnect vc")
        initial_notifications_count = self.get_notifications_count()
        log.info("Disconnect an AP from athena")
        self.disconnect_device_from_server("IAP_1")
        log.info("wait for 150 seconds to update the notification")
        time.sleep(180)
        self.browser.refresh()
        log.info("Get the notifications count after disconnecting vc")
        current_notifications_count = self.get_notifications_count()
        log.info("Verify the current notifications count should be one more from initial notifications count")
        if int(current_notifications_count) - int(initial_notifications_count) == 1:
            log.info("PASS: Notifications count is incremented by one expectedly.")
            self.verify_new_notification_virtual_controller_disconnected()
        else:
            log.info("FAIL: Notifications count is not incremented by one after vc disconnected.")
            #raise AssertionError("Notifications count is not incremented by one after virtual controller disconnected")
            
    def verify_new_notification_virtual_controller_disconnected(self):
        '''
            Verify the latest notification is virtual controller disconnected
        '''
        latest_notification = self.latest_notification.text
        re_match = re.compile('Virtual Controller.*disconnected', re.IGNORECASE)
        if not re_match.match(latest_notification):
            log.info("FAIL: Notification is not generated for \"Virtual Controller disconnected\" event.")
            raise AssertionError("Notification is not generated for virtual controller disconnected")
        else:
            log.info("PASS: Notification is generated for \"Virtual Controller disconnected\" event successfully.")
            if not self.acknowledge_button:
                log.info("FAIL: Acknowledge Button is not existing for \"Virtual Controller disconnected\" event notification")
                raise AssertionError("Acknowledge Button is not existing for newly generated virtual controller disconnected notification")
            else:
                log.info("PASS: Acknowledge Button is existing for newly generated virtual controller disconnected notification.")
    
    def verify_virtual_controller_connected_notification(self,group="All Groups"):
        '''
            Verify the notification should be created when virtual controller is connected
        '''    
        self.go_to_notifications_icon()
        self.go_to_notifications_settings()
        log.info("Click on Add Notification for enabling Device Notification for Virtual Controller connected  ")
        self.add_notification("Device","AP re-connected",group,False)
        self.close_notifications()
        log.info("Get the notifications count before connect vc")
        initial_notifications_count = self.get_notifications_count()
        log.info("connect an AP to athena")
        self.connect_device_to_server("IAP_1")
        log.info("wait for 150 seconds to update the notification")
        time.sleep(180)
        self.browser.refresh()
        log.info("Get the notifications count after connecting vc")
        current_notifications_count = self.get_notifications_count()
        log.info("Verify the current notifications count should be one more from initial notifications count")
        if int(current_notifications_count) - int(initial_notifications_count) == 1:
            log.info("PASS: Notifications count is incremented by one expectedly.")
            self.verify_new_notification_virtual_controller_connected()
        else:
            log.info("FAIL: Notifications count is not incremented by one after vc connected.")
            raise AssertionError("Notifications count is not incremented by one after virtual controller connected")
            
    def verify_new_notification_virtual_controller_connected(self):
        '''
            Verify the latest notification is virtual controller connected
        '''
        latest_notification = self.latest_notification.text
        re_match = re.compile('AP.*re-connected', re.IGNORECASE)
        if not re_match.match(latest_notification):
            log.info("FAIL: Notification is not generated for \"Virtual Controller connected\" event.")
            raise AssertionError("Notification is not generated for virtual controller connected")
        else:
            log.info("PASS: Notification is generated for \"Virtual Controller connected\" event successfully.")
            if not self.acknowledge_button:
                log.info("FAIL: Acknowledge Button is not existing for \"Virtual Controller connected\" event notification")
                raise AssertionError("Acknowledge Button is not existing for newly generated virtual controller connected notification")
            else:
                log.info("PASS: Acknowledge Button is existing for newly generated virtual controller connected notification.")

    def verify_new_client_connected_notification(self,client,ssid,group="All Groups"):
        '''
            Verify the notification should be created when new client is connected
        '''    
        self.go_to_notifications_icon()
        self.go_to_notifications_settings()
        log.info("Click on Add Notification for enabling client Notification for New client connected")
        self.add_notification("Client","New client connected",group,False)
        self.close_notifications()
        log.info("Get the notifications count before connect vc")
        initial_notifications_count = self.get_notifications_count()
        log.info("connect a client to athena")
        #self.connect_client_to_ap("Client_1", "ssid_0")
        self.connect_client_to_ap(client,ssid)
        log.info("wait for 250 seconds to update the notification")
        time.sleep(250)
        self.browser.refresh()
        log.info("Get the notifications count after connecting client")
        current_notifications_count = self.get_notifications_count()
        log.info("Verify the current notifications count should be one more from initial notifications count")
        if int(current_notifications_count) - int(initial_notifications_count) == 1:
            log.info("PASS: Notifications count is incremented by one expectedly.")
            self.verify_new_notification_new_client_connected()
        else:
            log.info("FAIL: Notifications count is not incremented by one after client connected.")
            raise AssertionError("Notifications count is not incremented by one after client connected")
            
    def verify_new_notification_new_client_connected(self):
        '''
            Verify the latest notification is new client connected
        '''
        latest_notification = self.latest_notification.text
        re_match = re.compile('New Client.*connected', re.IGNORECASE)
        if not re_match.match(latest_notification):
            log.info("FAIL: Notification is not generated for \"New client connected\" event.")
            raise AssertionError("Notification is not generated for New client connected")
        else:
            log.info("PASS: Notification is generated for \"New client connected\" event successfully.")
            if not self.acknowledge_button:
                log.info("FAIL: Acknowledge Button is not existing for \"New client connected\" event notification")
                raise AssertionError("Acknowledge Button is not existing for newly generated New client connected notification")
            else:
                log.info("PASS: Acknowledge Button is existing for newly generated New client connected notification.")

    def verify_client_disconnected_notification(self,client,group="All Groups"):
        '''
            Verify the notification should be created when new client is connected
        '''    
        self.go_to_notifications_icon()
        self.go_to_notifications_settings()
        log.info("Click on Add Notification for enabling client Notification for New client connected")
        self.add_notification("Client","Client disconnected",group,False)
        self.close_notifications()
        log.info("Get the notifications count before disconnect vc")
        initial_notifications_count = self.get_notifications_count()
        log.info("connect a client to athena")
        self.disconnect_client_from_ap(client)
        log.info("wait for 20 minutes to update the notification")
        time.sleep(600)
        self.browser.refresh()
        time.sleep(700)
        self.browser.refresh()
        log.info("Get the notifications count after connecting client")
        current_notifications_count = self.get_notifications_count()
        log.info("Verify the current notifications count should be one more from initial notifications count")
        if int(current_notifications_count) - int(initial_notifications_count) == 1:
            log.info("PASS: Notifications count is incremented by one expectedly.")
            self.verify_new_notification_client_disconnected()
        else:
            log.info("FAIL: Notifications count is not incremented by one after client disconnected.")
            raise AssertionError("Notifications count is not incremented by one after client disconnected")
            
    def verify_new_notification_client_disconnected(self):
        '''
            Verify the latest notification is new client connected
        '''
        latest_notification = self.latest_notification.text
        re_match = re.compile('Client.*disconnected', re.IGNORECASE)
        if not re_match.match(latest_notification):
            log.info("FAIL: Notification is not generated for \"Client disconnected\" event.")
            raise AssertionError("Notification is not generated for client disconnected")
        else:
            log.info("PASS: Notification is generated for \"Client disconnected\" event successfully.")
            if not self.acknowledge_button:
                log.info("FAIL: Acknowledge Button is not existing for \"Client disconnected\" event notification")
                raise AssertionError("Acknowledge Button is not existing for newly generated Client disconnected notification")
            else:
                log.info("PASS: Acknowledge Button is existing for newly generated Client disconnected notification.")
                
    def set_default_notifications(self,types,types_default_events):
        '''
            Delete all the notifications and set the default notifications in settings
        '''
        self.go_to_notifications_icon()
        self.go_to_notifications_settings()
        self.delete_all_notifications_in_settings()
        self.add_list_of_notifications(types,types_default_events,"All Groups")
        self.close_notifications()