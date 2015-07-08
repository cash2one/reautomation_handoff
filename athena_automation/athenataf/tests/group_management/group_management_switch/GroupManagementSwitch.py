import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.SwitchConfigurationTest import SwitchConfigurationTest
from athenataf.lib.functionality.common import DeviceLibrary
import time
class GroupManagementSwitch(SwitchConfigurationTest):
    '''
    Test class for GroupManagementSwitch 
    '''
    def test_ath_6434_Create_new_empty_group_with_no_switches(self):
        inner_left_panel = self.TopPanel.click_slider_icon()
        # self.take_s1_snapshot()
        group_page=inner_left_panel.add_group()
        group_page.create_empty_switch_group()
        group_page.assert_sample_group()
        manage_group_page1 = inner_left_panel.manage_group()
        manage_group_page1.assert_sample_group_witn_no_vc()
        # self.take_s2_snapshot()
        manage_group_page1.delete_empty_group()
        # self.take_s3_snapshot()
        # self.assert_s1_s2_diff(None)
        # self.assert_s1_s3_diff()
        # self.clear()
        
    def test_ath_6438_create_new_group_with_single_switch(self):
        inner_left_panel = self.TopPanel.click_slider_icon()
        # self.take_s1_snapshot()
        group_page=inner_left_panel.add_group()
        group_page.create_switch_group1()
        group_page.assert_group1()
        group_page.expand_group1()
        group_page.select_swicth()
        group_page.assert_switch_on_title_area()
        group_page.select_group1_at_title()
        group_page.assert_group1_with_switch_at_title()
        self.TopPanel.click_slider_icon()
        group_page.select_default_switch()
        self.TopPanel.click_slider_icon()
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.move_virtual_controller3()
        manage_group_page.manage_group()
        # self.take_s2_snapshot()
        manage_group_page.delete_group1()
        # self.take_s3_snapshot()
        # self.assert_s1_s2_diff(None)
        # self.assert_s1_s3_diff()
        # self.clear()
        
    def test_ath_6732_select_group_name_from_switch_configuration(self):
        inner_left_panel = self.TopPanel.click_slider_icon()
        # self.take_s1_snapshot()
        group_page=inner_left_panel.add_group()
        group_page.create_empty_switch_group()
        # self.TopPanel.click_slider_icon()
        inner_left_panel.select_all_group()
        all_grp = self.LeftPanel.go_to_switch_configuration()
        sw_page = all_grp.go_to_samplegroup()
        sw_page.assert_switch_page()
        self.TopPanel.click_slider_icon()
        inner_left_panel.select_default_switch()
        self.TopPanel.click_slider_icon()       
        manage_group_page1 = inner_left_panel.manage_group()
        # self.take_s1_snapshot()
        manage_group_page1.delete_empty_group()
        # self.take_s3_snapshot()
        # self.assert_s1_s2_diff(None)
        # self.assert_s1_s3_diff()
        # self.clear()
        
    def test_ath_6736_verify_all_created_group_names_are_shown_under_all_groups(self):
        inner_left_panel = self.TopPanel.click_slider_icon()
        # self.take_s1_snapshot()
        group_page=inner_left_panel.add_group()
        group_page.create_switch_group1()
        group_page.refresh()
        self.TopPanel.click_slider_icon()
        group_page=inner_left_panel.add_group()
        group_page.create_switch_group2()       
        inner_left_panel.select_all_group()
        all_grp = self.LeftPanel.go_to_switch_configuration()
        all_grp.assert_group1()
        all_grp.assert_group2()
        self.TopPanel.click_slider_icon()
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.move_virtual_controller4()
        inner_left_panel.manage_group() 
        manage_group_page.delete_group1()
        inner_left_panel.manage_group() 
        # self.take_s2_snapshot()
        manage_group_page.delete_group2()
        # self.take_s3_snapshot()
        # self.assert_s1_s2_diff(None)
        # self.assert_s1_s3_diff()
        # self.clear()
        
    def test_ath_6734_verify_whether_switch_group_displays_its_members(self):
        inner_left_panel = self.TopPanel.click_slider_icon()
        # self.take_s1_snapshot()
        group_page=inner_left_panel.add_group()
        group_page.create_switch_group1()
        group_page.refresh()
        group_page.refresh()
        self.SwitchesPage.assert_switch_group()
        self.LeftPanel.go_to_monitoring_page()
        self.Dashboard.assert_monitoring_page_switch()
        firmware_page = self.LeftPanel.go_to_maintenance()
        firmware_page.click_switches()
        firmware_page.assert_no_data_message()
        self.TopPanel.click_slider_icon()
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.move_virtual_controller3()
        inner_left_panel.manage_group() 
        # self.take_s2_snapshot()
        manage_group_page.delete_group1()
        # self.take_s3_snapshot()
        # self.assert_s1_s2_diff(None)
        # self.assert_s1_s3_diff()
        # self.clear()
    
    def test_ath_6442_clone_a_group_from_existing_switch_device(self):
        inner_left_panel = self.TopPanel.click_slider_icon()
        # self.take_s1_snapshot()
        group_page=inner_left_panel.add_group()
        group_page.create_empty_switch_group()
        inner_left_panel.select_samplegroup()
        vpn_obj = self.LeftPanel.go_to_switch_configuration_vlans()
        vpn_obj.delete_default_vlan()   
        vpn_obj.creating_vlan()
        self.TopPanel.click_slider_icon()
        
        manage_group_page1 = inner_left_panel.manage_group()
        manage_group_page1.cloning_samplegroup2()
        
        inner_left_panel.select_samplegroup2()
        vpn_obj = self.LeftPanel.go_to_switch_configuration_vlans()
        vpn_obj.assert_vlan_test1('Exist')
        self.TopPanel.click_slider_icon()
        inner_left_panel.select_default_switch()
        self.TopPanel.click_slider_icon()
        manage_group_page1 = inner_left_panel.manage_group()
        # self.take_s2_snapshot()
        manage_group_page1.delete_empty_group()
        manage_group_page1 = inner_left_panel.manage_group()
        manage_group_page1.delete_empty_group_samplegroup2()
        # self.take_s3_snapshot()
        # self.assert_s1_s2_diff(None)
        # self.assert_s1_s3_diff()
        # self.clear()
        
    def test_ath_12085_device_management_and_subscription_key_page_should_be_greyed_out(self):
        firmware = self.LeftPanel.go_to_maintenance()
        inner_left_panel = self.TopPanel.click_slider_icon()
        inner_left_panel.select_aruba_switch()
        firmware.assert_subscription_device_management_link()
        
        
    def test_ath_6437_move_a_switch_from_one_hgroup_to_an_empty_group(self):
        inner_left_panel = self.TopPanel.click_slider_icon()
        manage_group = inner_left_panel.manage_group()
        create_group = manage_group.create_new_group_from_manage()
        create_group.set_group_name('group1')
        create_group.move_next()
        create_group._set_group_default_device_password1()
        inner_left_panel.manage_group()
        create_group = manage_group.create_new_group_from_manage()
        create_group.toggle_switch()
        create_group.set_group_name('group2')
        create_group.select_virtual_controller(create_group.switch1)
        create_group.move_next()
        create_group._set_group_default_device_password1()
        inner_left_panel.manage_group()
        manage_group.select_group(manage_group.group2)
        logger.debug('Selecting switch')
        manage_group.select_vc.click()
        manage_group.click_move_button()
        manage_group.select_group(manage_group.move_to_group1)
        manage_group.save_move_vc()
        inner_left_panel.manage_group()
        manage_group.select_group(manage_group.group1)
        logger.debug('Selecting switch')
        manage_group.select_vc.click()
        manage_group.click_move_button()
        manage_group.select_group(manage_group.switch_group)
        manage_group.save_move_vc()
        inner_left_panel.manage_group()
        manage_group.select_group(manage_group.group1)
        manage_group.click_on_delete_button()
        manage_group.select_group(manage_group.group2)
        manage_group.click_on_delete_button()
        manage_group.click_manage_group_close_button()
        
        create_group = inner_left_panel.add_group()
        create_group.set_group_name('group1')
        create_group.move_next()
        create_group._set_group_default_device_password1()
        inner_left_panel.add_group()
        create_group.toggle_switch()
        create_group.set_group_name('group2')
        create_group.select_virtual_controller(create_group.switch1)
        create_group.move_next()
        create_group._set_group_default_device_password1()
        manage_group = inner_left_panel.manage_group()
        manage_group.select_group(manage_group.group2)
        logger.debug('Selecting switch')
        manage_group.select_vc.click()
        manage_group.click_move_button()
        manage_group.select_group(manage_group.move_to_group1)
        manage_group.save_move_vc()
        inner_left_panel.manage_group()
        manage_group.select_group(manage_group.group1)
        logger.debug('Selecting switch')
        manage_group.select_vc.click()
        manage_group.click_move_button()
        manage_group.select_group(manage_group.switch_group)
        manage_group.save_move_vc()
        inner_left_panel.manage_group()
        manage_group.select_group(manage_group.group1)
        manage_group.click_on_delete_button()
        manage_group.select_group(manage_group.group2)
        manage_group.click_on_delete_button()
        manage_group.click_manage_group_close_button()
        
        
        
    def test_ath_6439_create_new_group_with_both_switch_and_iap(self):  
        inner_left_panel = self.TopPanel.click_slider_icon()
        create_group_page = inner_left_panel.add_group()
        create_group_page.create_group_with_user_groupname_password('test','test123')
        manage_group = inner_left_panel.manage_group()
        manage_group.move_device_to_group('test','Switch_1')
        time.sleep(15)
        manage_group = inner_left_panel.manage_group()
        manage_group.move_device_to_group('test','IAP_1')
        time.sleep(400)
        DeviceLibrary.reconnect('IAP_1')
        inner_left_panel.assert_device_in_group('IAP_1','test')
        inner_left_panel.assert_device_in_group('Switch_1','test')
        
        

    def test_ath_6520_verify_unprovisioned_switches_are_seen_in_selection_while_creating_new_group(self):
        # conf=self.config.config_vars
        # firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        # device_management_page = self.LeftPanel.go_to_device_management()
        # device_management_page.search_device_mac_address_and_asserts()
        # device_management_page.assert_non_preconfigured_group()
        # inner_left_panel = self.TopPanel.click_slider_icon()
        # if inner_left_panel.assert_group1_and_group2():
            # if inner_left_panel.assert_sample_group_with_vc_present():
                # manage_group_page = inner_left_panel.manage_group()
                # manage_group_page.move_virtual_controller_from_Mygroup(group1=True)
                # inner_left_panel.manage_group()
                # manage_group_page.delete_specific_group(group1=True)
    
    
        # inner_left_panel = self.TopPanel.click_slider_icon()
        # inner_left_panel.asserting_unprovisioned_switch_list()
        # inner_left_panel.select_unprovision_switch()
        # group_page = inner_left_panel.click_configuration_page_new_group_button()

        # group_page.create_unprovision_switch_group1(self.config.config_vars.group_1)
        # inner_left_panel.click_expand_group1_icon()
        # inner_left_panel.asserting_switch_inside_group()


        # inner_left_panel.select_unprovision_switch()
        # group_page = inner_left_panel.click_configuration_page_existing_group_button()
        # group_page.select_group1_to_move_device()

        # manage_group_page = inner_left_panel.manage_group()
        # manage_group_page.move_all_switch_from_anygroup_to_default(group1=True)
        # inner_left_panel.manage_group()
        # manage_group_page.delete_specific_group(group1=True)
        raw_input('ssss')
        inner_left_panel = self.TopPanel.click_slider_icon()
        # group_page = inner_left_panel.add_group()
        inner_left_panel.assert_device_in_group('Switch_1','Unprovisioned')
        
        
        
    def test_ath_6733_move_an_unprovisioned_switch_to_new_group_using_import_to_new_group_option(self):
        conf=self.config.config_vars
        # firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        # device_management_page = self.LeftPanel.go_to_device_management()
        # device_management_page.search_device_mac_address_and_asserts()
        # device_management_page.assert_non_preconfigured_group()
        # inner_left_panel = self.TopPanel.click_slider_icon()
        # if inner_left_panel.assert_group1_and_group2():
            # if inner_left_panel.assert_sample_group_with_vc_present():
                # manage_group_page = inner_left_panel.manage_group()
                # manage_group_page.move_virtual_controller_from_Mygroup(group1=True)
                # inner_left_panel.manage_group()
                # manage_group_page.delete_specific_group(group1=True)
    
    
        # inner_left_panel = self.TopPanel.click_slider_icon()
        # inner_left_panel.asserting_unprovisioned_switch_list()
        # inner_left_panel.select_unprovision_switch()
        
        # on the right of the top window, the option IMPORT to NEW group should be visible
        # inner_left_panel.browser.assert_element(inner_left_panel.import_msg,'Import message is not visible')
        
        # group_page = inner_left_panel.click_configuration_page_new_group_button()

        # group_page.create_unprovision_switch_group1(self.config.config_vars.group_1)
        # inner_left_panel.click_expand_group1_icon()
        # inner_left_panel.asserting_switch_inside_group()


        # inner_left_panel.select_unprovision_switch()
        # group_page = inner_left_panel.click_configuration_page_existing_group_button()
        # group_page.select_group1_to_move_device()

        # manage_group_page = inner_left_panel.manage_group()
        # manage_group_page.move_all_switch_from_anygroup_to_default(group1=True)
        # inner_left_panel.manage_group()
        # manage_group_page.delete_specific_group(group1=True)
        inner_left_panel = self.TopPanel.click_slider_icon()        
        manage_group_page = inner_left_panel.manage_group()
        import time
        time.sleep(5)
        manage_group_page.group_sidebar_close_icon.click()
        time.sleep(5)
        manage_group_page.move_unprovisioned_device('New Group','switch')

        
    def test_ath_6436_switch_not_in_factory_default_configuration_registered_to_athena_it_appears_as_unprovisioned_device(self):
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        device_management_page = self.LeftPanel.go_to_device_management()
        device_management_page.unassign_switch_license("Switch_1")
        monitoring_switch_page = self.LeftPanel.go_to_monitoring_switches_page()
        monitoring_switch_page.delete_switch_device_based_on_ip("Switch_1")
        DeviceLibrary.factoryReset("Switch_1")
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        device_management_page = self.LeftPanel.go_to_device_management()
        device_management_page.add_switch_and_assign_license("Switch_1")
        DeviceLibrary.connect_device_to_server("Switch_1")
        import time
        time.sleep(120)
        self.browser.refresh()
        
        inner_left_panel = self.TopPanel.click_slider_icon()
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.group_sidebar_close_icon.click()
        manage_group_page.move_unprovisioned_device('Switch_1','New Group','switch')
        
        inner_left_panel.manage_group()
        manage_group_page.move_device_to_group('default','Switch_1')
        
        inner_left_panel.manage_group()
        manage_group_page.delete_group('switch')

        
    def test_ath_6435_verify_factory_defaults_switch_shows_up_in_default_group_on_registration_to_athena(self):
        inner_left_panel = self.TopPanel.click_slider_icon()
        inner_left_panel.expand_switch_group_icon()
        inner_left_panel.asserting_switch_inside_default_group()
        
    def test_ath_6521_verify_multiple_iap_switch_move_from_one_group_to_another(self):
        # firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        # device_management_page = self.LeftPanel.go_to_device_management()
        # device_management_page.unassign_switch_license("Switch_1")
        # monitoring_switch_page = self.LeftPanel.go_to_monitoring_switches_page()
        # monitoring_switch_page.delete_switch_device_based_on_ip("Switch_1")
        # DeviceLibrary.factoryReset("Switch_1")
        # firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        # device_management_page = self.LeftPanel.go_to_device_management()
        # device_management_page.add_switch_and_assign_license("Switch_1")
        # DeviceLibrary.connect_device_to_server("Switch_1")

        # device_management_page.unassign_switch_license("Switch_2")
        # monitoring_switch_page = self.LeftPanel.go_to_monitoring_switches_page()
        # monitoring_switch_page.delete_switch_device_based_on_ip("Switch_2")
        # DeviceLibrary.factoryReset("Switch_2")
        # import time
        # firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        # device_management_page = self.LeftPanel.go_to_device_management()
        # time.sleep(50)
        # device_management_page.add_switch_and_assign_license("Switch_2")
        # time.sleep(20)
        # DeviceLibrary.connect_device_to_server("Switch_2")
        
        # import time
        # time.sleep(120)
        # self.browser.refresh()
        
        inner_left_panel = self.TopPanel.click_slider_icon()
        # manage_group_page = inner_left_panel.manage_group()
        # manage_group_page.group_sidebar_close_icon.click()
        # manage_group_page.move_unprovisioned_device('Switch_1','New Group','group1')
        # manage_group_page.move_unprovisioned_device('Switch_2','New Group','group2')        

        manage_group = inner_left_panel.manage_group()
        # manage_group.move_device_to_group('group2','IAP_1')
        # time.sleep(400)
        # DeviceLibrary.reconnect('IAP_1')
        
        # inner_left_panel.manage_group()
        # inner_left_panel.manage_group()
        # manage_group.move_device_to_group('group1','Switch_1')
        # inner_left_panel.manage_group()
        manage_group.move_device_to_group('group1','IAP_1')
        time.sleep(400)
        DeviceLibrary.reconnect('IAP_1')
        

        

        
    def test_ath_6441_move_multiple_switches_from_one_group_to_another_group_having_a_switch(self):
        # firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        # device_management_page = self.LeftPanel.go_to_device_management()
        # device_management_page.unassign_switch_license("Switch_1")
        # monitoring_switch_page = self.LeftPanel.go_to_monitoring_switches_page()
        # monitoring_switch_page.delete_switch_device_based_on_ip("Switch_1")
        # DeviceLibrary.factoryReset("Switch_1")
        # firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        # device_management_page = self.LeftPanel.go_to_device_management()
        # device_management_page.add_switch_and_assign_license("Switch_1")
        # DeviceLibrary.connect_device_to_server("Switch_1")

        # device_management_page.unassign_switch_license("Switch_2")
        monitoring_switch_page = self.LeftPanel.go_to_monitoring_switches_page()
        # monitoring_switch_page.delete_switch_device_based_on_ip("Switch_2")
        DeviceLibrary.factoryReset("Switch_2")
        import time
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        device_management_page = self.LeftPanel.go_to_device_management()
        time.sleep(50)
        device_management_page.add_switch_and_assign_license("Switch_2")
        time.sleep(20)
        DeviceLibrary.connect_device_to_server("Switch_2")
        
        # device_management_page.unassign_switch_license("Switch_3")
        # monitoring_switch_page = self.LeftPanel.go_to_monitoring_switches_page()
        # monitoring_switch_page.delete_switch_device_based_on_ip("Switch_3")
        # DeviceLibrary.factoryReset("Switch_3")
        # time.sleep(20)
        # firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        # device_management_page = self.LeftPanel.go_to_device_management()
        # device_management_page.add_switch_and_assign_license("Switch_3")
        # time.sleep(20)
        # DeviceLibrary.connect_device_to_server("Switch_3")
        
        import time
        time.sleep(120)
        self.browser.refresh()
        
        inner_left_panel = self.TopPanel.click_slider_icon()
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.group_sidebar_close_icon.click()
        manage_group_page.move_unprovisioned_device('Switch_1','New Group','group1')
        manage_group_page.move_unprovisioned_device('Switch_2','New Group','group2')        
        # manage_group_page.move_unprovisioned_device('Switch_3','Existing Group','group2') 
        
        inner_left_panel.manage_group()
        manage_group_page.move_device_to_group('group1','Switch_2')
        # inner_left_panel.manage_group()
        # manage_group_page.move_device_to_group('group1','Switch_3')

    
    def test_ath_6440_move_single_switch_from_one_group_to_another_group_having_a_switch(self):
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        device_management_page = self.LeftPanel.go_to_device_management()
        
        device_management_page.unassign_switch_license("Switch_1")
        monitoring_switch_page = self.LeftPanel.go_to_monitoring_switches_page()
        monitoring_switch_page.delete_switch_device_based_on_ip("Switch_1")
        DeviceLibrary.factoryReset("Switch_1")
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        device_management_page = self.LeftPanel.go_to_device_management()
        device_management_page.add_switch_and_assign_license("Switch_1")
        DeviceLibrary.connect_device_to_server("Switch_1")

        device_management_page.unassign_switch_license("Switch_2")
        monitoring_switch_page = self.LeftPanel.go_to_monitoring_switches_page()
        monitoring_switch_page.delete_switch_device_based_on_ip("Switch_2")
        DeviceLibrary.factoryReset("Switch_2")
        import time
        time.sleep(120)
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        device_management_page = self.LeftPanel.go_to_device_management()
        device_management_page.add_switch_and_assign_license("Switch_2")
        DeviceLibrary.connect_device_to_server("Switch_2")
        import time
        time.sleep(120)
        self.browser.refresh()
        time.sleep(60)
        
        inner_left_panel = self.TopPanel.click_slider_icon()
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.group_sidebar_close_icon.click()
        manage_group_page.move_unprovisioned_device('Switch_1','New Group','group1')
        manage_group_page.move_unprovisioned_device('Switch_2','New Group','group2')        
        
        inner_left_panel.manage_group()
        manage_group_page.move_device_to_group('group1','Switch_2')

        

    def test_ath_6443_clone_a_new_group_from_existing_group(self):
        # firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        # device_management_page = self.LeftPanel.go_to_device_management()
        
        # device_management_page.unassign_switch_license("Switch_1")
        # monitoring_switch_page = self.LeftPanel.go_to_monitoring_switches_page()
        # monitoring_switch_page.delete_switch_device_based_on_ip("Switch_1")
        # DeviceLibrary.factoryReset("Switch_1")
        # firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        # device_management_page = self.LeftPanel.go_to_device_management()
        # device_management_page.add_switch_and_assign_license("Switch_1")
        # DeviceLibrary.connect_device_to_server("Switch_1")
        
        # device_management_page.unassign_switch_license("Switch_2")
        # monitoring_switch_page = self.LeftPanel.go_to_monitoring_switches_page()
        # monitoring_switch_page.delete_switch_device_based_on_ip("Switch_2")
        # DeviceLibrary.factoryReset("Switch_2")
        # import time
        # time.sleep(40)
        # firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        # device_management_page = self.LeftPanel.go_to_device_management()
        # device_management_page.add_switch_and_assign_license("Switch_2")
        # DeviceLibrary.connect_device_to_server("Switch_2")
        # time.sleep(40)
        # self.browser.refresh()
        

        inner_left_panel = self.TopPanel.click_slider_icon()
        # manage_group_page = inner_left_panel.manage_group()
        # manage_group_page.group_sidebar_close_icon.click()
        # manage_group_page.move_unprovisioned_device('Switch_1','New Group','group1')
        
        # manage_group_page = inner_left_panel.manage_group()
        # manage_group_page.clone_group('group1','test')
        
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.group_sidebar_close_icon.click()        
        manage_group_page.move_unprovisioned_device('Switch_2','Existing Group','test')
