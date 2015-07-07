__author__ = 'aarunakirisamy'
import logging
log = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.MonitoringTest import MonitoringTest
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest
import time

class Notifications(ConfigurationTest, MonitoringTest):
    all_types = ["Device","Client","IDS Events","User Management"]
    all_types_events = [["New Virtual Controller detected","Virtual controller disconnected","New AP detected","AP disconnected","AP re-connected",
                         "Flagged AP","Unflagged AP"],["New client connected","Client disconnected","Flagged client","Unflagged client"],
                         ["Rogue AP detected","Interfering AP detected","Infrastructure attack detected","Client attack detected"],
                         ["New User account added","User account deleted","User account edited"]]
    all_types_default_events = [["Virtual controller disconnected","Flagged AP"],["Flagged client"],["Rogue AP detected"],["New User account added"]]
    
    def test_ath_11501_Check_default_in_notification(self):
        """
        ################################################################################################################
        NAME : Arunkarthick A
        DATE : 3/12/2015
        1 Navigate to Monitoring ->Click on Notifications
        
        2 a.Click on the message type icon  which is next to login details which is above search box 
        b.Click on the show all option at the bottom 
        ################################################################################################################
        """
        log.info("Navigate to Monitoring ->Click on Notifications")
        notification_page = self.LeftPanel.goto_monitoring_notification_page()
        log.info("Verify Acknowledge all option in the right corner")
        notification_page.verify_acknowledge_all_notifications_button()
        log.info("Click on the message type icon  which is next to login details which is above search box ")
        notification_page.assert_notifications_icon()
        log.info("Click on settings icon")
        notification_page.assert_notifications_settings()
        log.info("Verify the default notifications")
        for type_events in self.all_types_default_events:
            for event in type_events:
                notification_page.assert_notification(event)
        notification_page.close_notifications()
        log.info("Click on the show all option at the bottom")
        notification_page.assert_show_all_notifications()
        log.info("#"*80)
        log.info("END OF TEST CASE - test_ath_11501_Check_default_in_notification")
##
    
    def test_ath_11507_Check_default_notification_settings(self):
        """
        ################################################################################################################
        NAME : Arunkarthick A
        DATE : 3/12/2015
        1 Navigate to notifications settings -->click the message icon at the top of the page and click settings icon from that.
        
        2 Select a group and repeat above test cases.

        ################################################################################################################
        """
        log.info("Navigate to notifications settings -->click the message icon at the top of the page and click settings icon from that.")
        notification_page = self.LeftPanel.goto_monitoring_notification_page()
        notification_page.assert_notifications_icon()
        notification_page.assert_notifications_settings()
        log.info("Verify the default notifications")
        for type_events in self.all_types_default_events:
            for event in type_events:
                notification_page.assert_notification(event)
        log.info("#"*80)
        log.info("Before adding all the notifications, delete the existing notifications")
        notification_page.delete_all_notifications_in_settings()
        log.info("Click on Add Notification for setting up all the default notifications for a single(default) group")
        notification_page.add_list_of_notifications(self.all_types,self.all_types_default_events,"default")
        notification_page.close_notifications()
        log.info("#"*80)
        log.info("Clean Up - set the default notifications only in notifications settings")
        notification_page.set_default_notifications(self.all_types,self.all_types_default_events)
        log.info("#"*80)
        log.info("END OF TEST CASE - test_ath_11507_Check_default_notification_settings")
##

    def test_ath_11502_Check_notification_options(self):
        """
        ################################################################################################################
        NAME : Arunkarthick A
        DATE : 3/12/2015
        1 a.Click on the message type icon  which is next to login details which is above search box 
        b.Click on settings icon 
        
        2 a.Click on Add Notification for setting up all the notifications available for all groups
        b.Navigate to monitoring -> notifications,Click on Acknowledge all option in the right corner 
        c.Wait for sometime till some 4 to 5 new notifications are generated
        d.Now click on notifications list 
        
        3 a.Click on Add Notification for setting up all the notifications available for all groups 
        b.Check the notification screen by clciking in the mesage icon from Google chrome,Firefox and IE browser
        c.Wait for sometime till the notifications floods
        d.Try to scroll down to view all of the notifications from the various browsers
        ################################################################################################################
        """
        log.info("Test Setup :")
        notification_page = self.LeftPanel.goto_monitoring_notification_page()
        log.info("STEP 1")
        log.info("STEP 1.a:Click on the message type icon which is next to login details which is above search box")
        notification_page.assert_notifications_icon()
        log.info("STEP 1.b:Click on settings icon ")
        notification_page.assert_notifications_settings()
        log.info("#"*80)        
        log.info("STEP 2")
        log.info("Before adding all the notifications, delete the existing notifications")
        notification_page.delete_all_notifications_in_settings()
        log.info("STEP 2.a: Click on Add Notification for setting up all the notifications available for all groups")
        notification_page.add_list_of_notifications(self.all_types,self.all_types_events,"All Groups")
        notification_page.close_notifications()
        log.info("STEP 2.b:Navigate to monitoring -> notifications,Click on Acknowledge all option in the right corner")
        notification_page.assert_acknowledge_all_notifications()
        log.info("#"*80)
        log.info("3.d:Try to scroll down to view all of the notifications")
        notification_page.assert_show_all_notifications()
        log.info("#"*80)
        log.info("Clean Up - set the default notifications only in notifications settings")
        notification_page.set_default_notifications(self.all_types,self.all_types_default_events)
        log.info("END OF TEST CASE - test_ath_11502_Check_notification_options")
##        
    def test_ath_11504_notifications_with_email_options(self):
        """
        ################################################################################################################
        NAME : Arunkarthick A
        DATE : 3/12/2015
        1 a.Click on the message type icon  which is next to login details which is above search box 
        b.Click on settings icon 
        
        2 a.Click on Add Notification for setting up all the notifications available for Type User Management
        b.Enable email options for all of the above notifications
        c.Repeat the same for a single group instead of all groups 
        
        3 a.Click on Add Notification for setting up all the notifications available for Type IDS
        b.Enable email options for all of the above notifications
        c.Repeat the same for a single group instead of all groups 
        
        4 a.Click on Add Notification for setting up all the notifications available for Type Clients
        b.Enable email options for all of the above notifications
        c.Repeat the same for a single group instead of all groups 
        ################################################################################################################
        """
        log.info("Test Setup :")
        notification_page = self.LeftPanel.goto_monitoring_notification_page()
        log.info("STEP 1: Verifying the notification icon and settings button")
        log.info("Click on the message type icon which is next to login details which is above search box")
        notification_page.assert_notifications_icon()
        log.info("Click on settings icon")
        notification_page.assert_notifications_settings()
        log.info("#"*80)
        log.info("STEP 2:  Add all the notifications for all groups with email option")        
        log.info("Before adding all the notifications, delete the existing notifications")
        notification_page.delete_all_notifications_in_settings()
        log.info("Click on Add Notification for setting up all the notifications available for all groups")
        notification_page.add_list_of_notifications(self.all_types,self.all_types_events,"All Groups",True)
        notification_page.close_notifications()
        log.info("#"*80)
        log.info("STEP 3:  Add all the notifications for single group with email option")
        log.info("Before adding all the notifications, delete the existing notifications")
        notification_page.go_to_notifications_icon()
        notification_page.go_to_notifications_settings()
        notification_page.delete_all_notifications_in_settings()
        log.info("Click on Add Notification for setting up all the notifications available for default group")
        notification_page.add_list_of_notifications(self.all_types,self.all_types_events,"default",True)
        notification_page.close_notifications()
        log.info("#"*80)
        log.info("Clean Up - set the default notifications only in notifications settings")
        notification_page.set_default_notifications(self.all_types,self.all_types_default_events)
        log.info("END OF TEST CASE - test_ath_11504_notifications_with_email_options")
##         
    def test_ath_11505_disable_email_options(self):
        """
        ################################################################################################################
        NAME : Arunkarthick A
        DATE : 3/12/2015
        1 a.Click on the message type icon  which is next to login details which is above search box 
        b.Click on settings icon 
        
        2 a.Click on Add Notification for setting up all the notifications available for Type User Management
        b.Enable email options for all of the above notifications
        c.Repeat the same for a single group instead of all groups 
        
        3 a.Click on Add Notification for setting up all the notifications available for Type IDS
        b.Enable email options for all of the above notifications
        c.Repeat the same for a single group instead of all groups 
        
        4 a.Click on Add Notification for setting up all the notifications available for Type Clients
        b.Enable email options for all of the above notifications
        c.Repeat the same for a single group instead of all groups 
        ################################################################################################################
        """
        log.info("Test Setup :")
        notification_page = self.LeftPanel.goto_monitoring_notification_page()
        log.info("STEP 1: Verifying the notification icon and settings button")
        log.info("Click on the message type icon which is next to login details which is above search box")
        notification_page.assert_notifications_icon()
        log.info("Click on settings icon")
        notification_page.assert_notifications_settings()
        notification_page.close_notifications()
        log.info("#"*80)
        log.info("STEP 2:  Add all the notifications for all groups with email option")        
        log.info("Before adding all the notifications, delete the existing notifications")
        notification_page.go_to_notifications_icon()
        notification_page.go_to_notifications_settings()
        notification_page.delete_all_notifications_in_settings()
        log.info("Click on Add Notification for setting up all the notifications available for all groups")
        notification_page.add_list_of_notifications(self.all_types,self.all_types_events,"All Groups",True)
        notification_page.close_notifications()
        log.info("Disable the email options on all the notifications available for all groups")
        notification_page.go_to_notifications_icon()
        notification_page.go_to_notifications_settings()
        time.sleep(5)
        notification_page.disable_all_mail_options_in_notification_settings()
        notification_page.close_notifications()
        log.info("#"*80)
        log.info("STEP 3:  Add all the notifications for single group with email option")
        log.info("Before adding all the notifications, delete the existing notifications")
        notification_page.go_to_notifications_icon()
        notification_page.go_to_notifications_settings()
        notification_page.delete_all_notifications_in_settings()
        log.info("Click on Add Notification for setting up all the notifications available for default group")
        notification_page.add_list_of_notifications(self.all_types,self.all_types_events,"default",True)
        notification_page.close_notifications()
        log.info("Disable the email options on all the notifications available for single group")
        notification_page.go_to_notifications_icon()
        notification_page.go_to_notifications_settings()
        time.sleep(5)
        notification_page.disable_all_mail_options_in_notification_settings()
        notification_page.close_notifications()
        log.info("#"*80)
        log.info("Clean Up - set the default notifications only in notifications settings")
        notification_page.set_default_notifications(self.all_types,self.all_types_default_events)
        log.info("END OF TEST CASE - test_ath_11505_disable_email_options")
##
    def test_ath_11506_check_help_text(self):
        """
        ################################################################################################################
        NAME : Arunkarthick A
        DATE : 3/17/2015
        1 a.Navigate to Monitoring ->Notifications
        
        b.Enable help which will look like a Question mark next to Notifications 
                
        ################################################################################################################
        """
        notification_page = self.LeftPanel.goto_monitoring_notification_page()
        log.info("Click/Enable the Help")
        notification_page.enable_help()
        log.info("Verify the Help text for acknowledge all button")
        notification_page.assert_help_option("acknowledge_all_button")
        if notification_page.acknowledge_button:#sometimes zero notifications are possible
            log.info("Verify the Help text for acknowledge button on single notification")
            notification_page.assert_help_option("acknowledge_button")
        log.info("Disable the Help")
        notification_page.disable_help()
##
    def test_ath_11508_check_device_and_client_notifications_are_generated(self):
        """
        ################################################################################################################
        NAME : Arunkarthick A
        DATE : 3/18/2015
        1 a.Enable Device Notification for Virtual Controller connected via notifications settings for all groups 
        b.Connect VC to athena 
        c.Enable Device Notification for Virtual Controller disconnected and disconnect VC from athena
        d.Create Device Notification for New AP deteced and add a new AP to swarm.
        e.Create Device notification for AP disconnected and reconnected and disconnect and reconnect AP back to the swarm.
        f.Create Device notification for flagged AP and create scenario for AP to be flagged(manipulate the XML with weak signal strength, less memory etc)
        g.Create Device notification for unflagged AP and create scenario for AP to be unflagged(create some networks and push the config to the AP) 
        
        2        
        ################################################################################################################
        """
        notification_page = self.LeftPanel.goto_monitoring_notification_page()
        notification_page.delete_notifications_in_settings()
        
        log.info("Step 1.a:verify the Device Notification for Virtual Controller disconnected for all groups")
        notification_page.verify_virtual_controller_disconnected_notification("All Groups")
        notification_page.delete_notifications_in_settings()
        log.info("Step 1.e:verify the Device Notification for AP re-connected for all groups")
        notification_page.verify_virtual_controller_connected_notification("All Groups")
        
        notification_page.connect_device_to_server("IAP_1")
        
        
        
        log.info("Clean Up - set the default notifications only in notifications settings")
        notification_page.set_default_notifications(self.all_types,self.all_types_default_events)
        log.info("END OF TEST CASE - test_ath_11508_check_device_and_client_notifications_are_generated")
##
    def test_ath_11510_edit_delete_the_created_notifications(self):
        """
        ################################################################################################################
        NAME : Arunkarthick A
        DATE : 3/18/2015
        1 a.Enable Device Notification for Virtual Controller connected via notifications settings for all groups 
        b.Connect VC to athena 
        
        2 a. Edit the Device notification to Client notification 
        b.Associate a client to any group.
        c.Create a Client Notification for  "Client disconnected" and disassociate client from the same group.
        
        3 a.Delete the created client notifications 
        b.Associate a client to any group.
        c.Create a Client Notification for  "Client disconnected" and disassociate client from the same group
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
                
        notification_page = self.LeftPanel.goto_monitoring_notification_page()
        notification_page.delete_notifications_in_settings()
        
        log.info("Step 1.a:verify the Device Notification for Virtual Controller disconnected for all groups")
        notification_page.verify_virtual_controller_disconnected_notification("All Groups")
        notification_page.delete_notifications_in_settings()
        log.info("Step 1.b:verify the Device Notification for Virtual Controller disconnected for all groups")
        notification_page.verify_virtual_controller_connected_notification("All Groups")
        
        log.info("Get the notifications count before connect client")
        initial_notifications_count = int(notification_page.notification_count.text)
        log.info("Step 2.a:Edit the Device notification to Client notification")
        notification_page.go_to_notifications_icon()
        notification_page.go_to_notifications_settings()
        time.sleep(2)        
        notification_page.add_notification_type.set("Client")
        notification_page.add_notification_event.set("New client connected")
        notification_page.add_notification_group.set("default")
        notification_page.add_notification_save.click()
        notification_page.close_notifications()
        log.info("Step 2.b:Associate a client to any group.")
        notification_page.connect_client_to_ap("Client_1", "ssid_0")
        time.sleep(250)
        self.browser.refresh()
        log.info("Get the notifications count after connecting client")
        current_notifications_count = int(notification_page.notification_count.text)
        log.info("Verify the current notifications count should be one more from initial notifications count")
        if int(current_notifications_count) - int(initial_notifications_count) == 1:
            log.info("PASS: Notifications count is incremented by one expectedly.")
            notification_page.verify_new_notification_new_client_connected()
        else:
            log.info("FAIL: Notifications count is not incremented by one after client connected.")
            raise AssertionError("Notifications count is not incremented by one after client connected")
        log.info("Step 2.c:Create a Client Notification for \"Client disonnected\" and disassociate client from the same group.")  
        notification_page.go_to_notifications_icon()
        notification_page.go_to_notifications_settings()
        time.sleep(2) 
        initial_notifications_count = int(notification_page.notification_count.text)        
        notification_page.add_notification("Client","Client disconnected","default",False)
        notification_page.close_notifications()
        notification_page.disconnect_client_from_ap("Client_1")
        time.sleep(600)
        self.browser.refresh()
        time.sleep(700)
        self.browser.refresh()
        log.info("Get the notifications count after connecting client")
        current_notifications_count = int(notification_page.notification_count.text)
        log.info("Verify the current notifications count should be one more from initial notifications count")
        if int(current_notifications_count) - int(initial_notifications_count) == 1:
            log.info("PASS: Notifications count is incremented by one expectedly.")
            notification_page.verify_new_notification_client_disconnected()
        else:
            log.info("FAIL: Notifications count is not incremented by one after client connected.")
            raise AssertionError("Notifications count is not incremented by one after client connected")
            
        log.info("Step 3.a:Delete the created client notifications")
        notification_page.delete_notifications_in_settings()
        log.info("Step 3.b:Create a Client Notification for  Client connected& disconnected and disassociate client from the same group")
        notification_page.verify_new_client_connected_notification("Client_1", "ssid_0", "default")
        notification_page.verify_client_disconnected_notification("Client_1", "default")
        
        log.info("Clean Up - set the default notifications only in notifications settings")
        notification_page.set_default_notifications(self.all_types,self.all_types_default_events)
        log.info("END OF TEST CASE - 11510_edit_delete_the_created_notifications")