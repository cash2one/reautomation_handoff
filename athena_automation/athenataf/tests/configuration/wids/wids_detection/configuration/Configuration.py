import logging
logger = logging.getLogger('athenataf')
import time

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest
from athenataf.lib.functionality.common import DeviceLibrary
class Configuration(ConfigurationTest):
    '''
        Test class for Configuration.
    '''
    
    def test_ath_8152_threat_level_high(self):
        self.take_s1_snapshot()
        wids_page = self.LeftPanel.go_to_wids_page()
        wids_page.set_detection_infra_threat_detection_level('High')
        wids_page.assert_detection_infrastructure_tick_icon('High')
        wids_page.set_detection_clients_threat_detection_level('High')
        wids_page.assert_detection_clients_tick_icon('High')
        wids_page.save_settings
        self.take_s2_snapshot()
        wids_page.set_detection_infra_threat_detection_level('Off')
        wids_page.set_detection_clients_threat_detection_level('Off')
        wids_page.save_settings
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(2)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_8153_threat_level_medium(self):
        self.take_s1_snapshot()
        wids_page = self.LeftPanel.go_to_wids_page()
        wids_page.set_detection_infra_threat_detection_level('Medium')
        wids_page.assert_detection_infrastructure_tick_icon('Medium')
        wids_page.set_detection_clients_threat_detection_level('Medium')
        wids_page.assert_detection_clients_tick_icon('Medium')
        self.take_s2_snapshot()
        wids_page.set_detection_infra_threat_detection_level('Off')
        wids_page.set_detection_clients_threat_detection_level('Off')
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(2)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_8154_threat_level_low(self):
        self.take_s1_snapshot()
        wids_page = self.LeftPanel.go_to_wids_page()
        wids_page.set_detection_infra_threat_detection_level('Low')
        wids_page.assert_detection_infrastructure_tick_icon('Low')
        wids_page.set_detection_clients_threat_detection_level('Low')
        wids_page.assert_detection_clients_tick_icon('Low')
        self.take_s2_snapshot()
        wids_page.set_detection_infra_threat_detection_level('Off')
        wids_page.set_detection_clients_threat_detection_level('Off')
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(2)
        self.assert_s1_s3_diff()
        self.clear()
    
    def test_ath_8155_threat_level_custom(self):
        self.take_s1_snapshot()
        wids_page = self.LeftPanel.go_to_wids_page()
        wids_page.set_detection_infra_threat_detection_level('Custom')
        wids_page.assert_detection_infra_custom_level()
        wids_page.set_detection_clients_threat_detection_level('Custom')
        wids_page.assert_detection_clients_custom_level()
        wids_page.set_detection_clients_threat_detection_level('Custom')
        wids_page.set_detection_clients_custom_level_to_detect_omerta_attack()
        self.take_s2_snapshot()
        wids_page.set_detection_infra_threat_detection_level('Off')
        wids_page.set_detection_clients_threat_detection_level('Off')
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(2)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_8156_threat_level_custom_nagative(self):
        self.take_s1_snapshot()
        wids_page = self.LeftPanel.go_to_wids_page()
        wids_page.set_detection_infra_threat_detection_level_custom('Custom')
        wids_page.set_detection_clients_threat_detection_level_custom('Custom')
        wids_page.set_detection_infra_threat_detection_level('Off')
        wids_page.set_detection_clients_threat_detection_level('Off')
        wids_page.set_detection_infra_threat_detection_level_custom_changes('Custom')
        wids_page.set_detection_clients_threat_detection_level_custom_changes('Custom')
        wids_page.set_detection_infra_threat_detection_level('Low')
        wids_page.assert_detection_infrastructure_tick_icon('Low')
        wids_page.set_detection_clients_threat_detection_level('Low')
        wids_page.assert_detection_clients_tick_icon('Low')
        self.take_s2_snapshot()
        wids_page.set_detection_infra_threat_detection_level('Off')
        wids_page.set_detection_clients_threat_detection_level('Off')
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(2)
        self.assert_s1_s3_diff()
        self.clear()
        
    
    def test_ath_8157_threat_level_edit(self):
        self.take_s1_snapshot()
        wids_page = self.LeftPanel.go_to_wids_page()
        wids_page.set_detection_infra_threat_detection_level('High')
        wids_page.assert_detection_infrastructure_tick_icon('High')
        wids_page.set_detection_clients_threat_detection_level('High')
        wids_page.assert_detection_clients_tick_icon('High')
        wids_page.save_settings
        self.take_s2_snapshot()
        wids_page.set_detection_infra_threat_detection_level('Off')
        wids_page.set_detection_clients_threat_detection_level('Off')
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(2)
        self.assert_s1_s3_diff()
        self.clear()

    def test_ath_8158_check_wids_detection_config_override_flag(self):
        self.take_s1_snapshot()
        wids_page = self.LeftPanel.go_to_wids_page()
        wids_page.select_default_instant()
        wids_page.change_wids_detection_settings()
        wids_page.assert_detection_resolve_override_flag()
        self.take_s2_snapshot()
        wids_page.set_wids_detection_default()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(None)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_11129_threat_level_high(self):
        self.take_s1_snapshot()
        wids_page = self.LeftPanel.go_to_wids_page()
        wids_page.set_detection_infra_threat_detection_level('High')
        wids_page.assert_detection_infrastructure_tick_icon('High')
        wids_page.set_detection_clients_threat_detection_level('High')
        wids_page.assert_detection_clients_tick_icon('High')
        wids_page.save_settings
        self.take_s2_snapshot()
        wids_page.set_detection_infra_threat_detection_level('Off')
        wids_page.set_detection_clients_threat_detection_level('Off')
        wids_page.save_settings
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(2)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_11130_threat_level_medium(self):
        self.take_s1_snapshot()
        wids_page = self.LeftPanel.go_to_wids_page()
        wids_page.set_detection_infra_threat_detection_level('Medium')
        wids_page.assert_detection_infrastructure_tick_icon('Medium')
        wids_page.set_detection_clients_threat_detection_level('Medium')
        wids_page.assert_detection_clients_tick_icon('Medium')
        self.take_s2_snapshot()
        wids_page.set_detection_infra_threat_detection_level('Off')
        wids_page.set_detection_clients_threat_detection_level('Off')
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(2)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_11131_threat_level_low(self):
        self.take_s1_snapshot()
        wids_page = self.LeftPanel.go_to_wids_page()
        wids_page.set_detection_infra_threat_detection_level('Low')
        wids_page.assert_detection_infrastructure_tick_icon('Low')
        wids_page.set_detection_clients_threat_detection_level('Low')
        wids_page.assert_detection_clients_tick_icon('Low')
        self.take_s2_snapshot()
        wids_page.set_detection_infra_threat_detection_level('Off')
        wids_page.set_detection_clients_threat_detection_level('Off')
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(2)
        self.assert_s1_s3_diff()
        self.clear()
    
    def test_ath_11132_threat_level_custom(self):
        self.take_s1_snapshot()
        wids_page = self.LeftPanel.go_to_wids_page()
        wids_page.set_detection_infra_threat_detection_level('Custom')
        wids_page.assert_detection_infra_custom_level()
        wids_page.set_detection_clients_threat_detection_level('Custom')
        wids_page.assert_detection_clients_custom_level()
        wids_page.set_detection_clients_threat_detection_level('Custom')
        wids_page.set_detection_clients_custom_level_to_detect_omerta_attack()
        self.take_s2_snapshot()
        wids_page.set_detection_infra_threat_detection_level('Off')
        wids_page.set_detection_clients_threat_detection_level('Off')
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(2)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_11133_threat_level_custom_nagative(self):
        self.take_s1_snapshot()
        wids_page = self.LeftPanel.go_to_wids_page()
        wids_page.set_detection_infra_threat_detection_level_custom('Custom')
        wids_page.set_detection_clients_threat_detection_level_custom('Custom')
        wids_page.set_detection_infra_threat_detection_level('Off')
        wids_page.set_detection_clients_threat_detection_level('Off')
        wids_page.set_detection_infra_threat_detection_level_custom_changes('Custom')
        wids_page.set_detection_clients_threat_detection_level_custom_changes('Custom')
        wids_page.set_detection_infra_threat_detection_level('Low')
        wids_page.assert_detection_infrastructure_tick_icon('Low')
        wids_page.set_detection_clients_threat_detection_level('Low')
        wids_page.assert_detection_clients_tick_icon('Low')
        self.take_s2_snapshot()
        wids_page.set_detection_infra_threat_detection_level('Off')
        wids_page.set_detection_clients_threat_detection_level('Off')
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(2)
        self.assert_s1_s3_diff()
        self.clear()
        
    
    def test_ath_11134_threat_level_edit(self):
        self.take_s1_snapshot()
        wids_page = self.LeftPanel.go_to_wids_page()
        wids_page.set_detection_infra_threat_detection_level('High')
        wids_page.assert_detection_infrastructure_tick_icon('High')
        wids_page.set_detection_clients_threat_detection_level('High')
        wids_page.assert_detection_clients_tick_icon('High')
        wids_page.save_settings
        self.take_s2_snapshot()
        wids_page.set_detection_infra_threat_detection_level('Off')
        wids_page.set_detection_clients_threat_detection_level('Off')
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(2)
        self.assert_s1_s3_diff()
        self.clear()

    def test_ath_11135_wids_config_vc_level(self):
        self.take_s1_snapshot()
        wids_page = self.LeftPanel.go_to_wids_page()
        wids_page.select_default_instant()
        wids_page.change_wids_detection_settings()
        wids_page.assert_detection_resolve_override_flag()
        self.take_s2_snapshot()
        wids_page.set_wids_detection_default()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(None)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_11137_wids_config_all_iaps_in_swarm(self):
        self.take_s1_snapshot()
        import os
        os.environ['device'] = "IAP_1"
        self.take_s1_snapshot('show_ids_detection_config')
        import os
        os.environ['device'] = "IAP_2"
        time.sleep(140)
        self.take_s1_snapshot('show_ids_detection_config')
        time.sleep(30)
        inner_left_panel = self.TopPanel.click_slider_icon()
        inner_left_panel.select_master_slave_group()
        wids_page = self.LeftPanel.go_to_wids_page()
        wids_page.set_detection_infra_threat_detection_level_custom('High')
        wids_page.set_detection_clients_threat_detection_level_custom_changes('Custom')
        wids_page.setting_attacks()
        wids_page.save_settings()
        import os
        os.environ['device'] = "IAP_1"
        self.take_s2_snapshot('show_ids_detection_config')
        import os
        os.environ['device'] = "IAP_2"
        time.sleep(30)
        self.take_s2_snapshot('show_ids_detection_config')
        wids_page.assert_attacks()
        wids_page.set_detection_infra_threat_detection_level('Off')
        wids_page.set_detection_clients_threat_detection_level('Off')
        import os
        os.environ['device'] = "IAP_1"
        self.take_s3_snapshot('show_ids_detection_config')
        import os
        os.environ['device'] = "IAP_2"
        time.sleep(30)
        self.take_s3_snapshot('show_ids_detection_config')
        import os
        os.environ['device'] = "IAP_1"
        self.assert_s1_s2_diff(2)
        import os
        os.environ['device'] = "IAP_2"
        self.assert_s1_s2_diff(2)
        import os
        os.environ['device'] = "IAP_1"
        self.assert_s1_s3_diff()
        import os
        os.environ['device'] = "IAP_2"
        self.assert_s1_s3_diff()
        # self.clear()
        
    def test_ath_11339_wids_config_infrastructure_and_clients_detection_level(self):
        conf = self.config.config_vars
        self.take_s1_snapshot()
        inner_left_panel = self.TopPanel.click_slider_icon()
        inner_left_panel.select_device()
        wids_page = self.LeftPanel.go_to_wids_page()
        wids_page.assert_detection_infrastructure_tick_icon('Low')
        wids_page.assert_detection_clients_tick_icon('Low')
        wids_page.set_detection_infra_threat_detection_level_custom_changes('High')
        wids_page.save_settings()
        wids_page.assert_detection_clients_tick_icon('Low')
        wids_page.set_detection_clients_threat_detection_level_custom_changes('Custom')
        wids_page.setting_attacks()
        wids_page.select_detect_block_ack_attack()
        wids_page.save_settings()
        wids_page.set_detection_infra_threat_detection_level_custom_changes('Custom')
        wids_page.click_detection_infra_tick_icon()
        wids_page.select_detect_adhoc_using_valid_ssid()
        wids_page.save_settings()
        wids_page.assert_override_flag(True)
        inner_left_panel = self.TopPanel.click_slider_icon()
        inner_left_panel.select_default_group()
        wids_page = self.LeftPanel.go_to_wids_page()
        wids_page.set_detection_infra_threat_detection_level_custom_changes('Custom')
        wids_page.click_detection_infra_tick_icon()
        wids_page.select_detect_adhoc_using_valid_ssid()
        wids_page.save_settings()
        wids_page.assert_override_flag(False)
        self.take_s2_snapshot()
        wids_page.set_detection_infra_threat_detection_level_custom_changes('Low')
        wids_page.set_detection_clients_threat_detection_level_custom_changes('Low')
        inner_left_panel = self.TopPanel.click_slider_icon()
        inner_left_panel.select_device()
        wids_page.set_detection_infra_threat_detection_level_custom_changes('Low')
        wids_page.set_detection_clients_threat_detection_level_custom_changes('Low')
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
        
        
    def test_ath_11136_wids_config_unprovisioned_iap(self):
        conf=self.config.config_vars
        import os
        os.environ['device'] = "IAP_1"
        self.take_s1_snapshot('show_ids_detection_config')
        self.TopPanel.go_to_allgroups()
        device_mgmt = self.LeftPanel.go_to_device_management()
        device_mgmt.get_and_search_mac_address()
        device_mgmt.select_virtual_controller(device_mgmt.device_selector_1)
        device_mgmt.select_assign_group()
        device_mgmt.all_group.click()
        device_mgmt.click_assign()
        logger.debug('DeviceManagement: Clicking on ok button')
        device_mgmt.ok_button.click()
        device_mgmt.assert_group_name(conf.unprovisioned)
        DeviceLibrary.factoryReset('IAP_1')
        DeviceLibrary.configureWirelessNetwork('IAP_1')
        time.sleep(90)
        DeviceLibrary.getPrompt('IAP_1')
        DeviceLibrary.connect_device_to_server('IAP_1')
        time.sleep(300)
        inner_left_panel = self.TopPanel.click_slider_icon()
        time.sleep(20)
        if not inner_left_panel.verify_unprovision_iap:
            time.sleep(30)
            self.browser.refresh()
            time.sleep(10)
            self.TopPanel.click_slider_icon()
        inner_left_panel.select_unprovision_iap()
        inner_left_panel.assert_unprovisioned_alert_popup()
        inner_left_panel.select_wireless_configuration_module()
        time.sleep(20)
        # if inner_left_panel.assert_group1_and_group2():
            # if inner_left_panel.assert_sample_group_with_vc_present():
                # manage_group_page = inner_left_panel.manage_group()
                # manage_group_page.move_virtual_controller_from_Mygroup(group1=True)
                # inner_left_panel.manage_group()
                # manage_group_page.delete_specific_group(group1=True)
        
        # create_group_page = inner_left_panel.add_group()
        # create_group_page.set_group_name(conf.group_1)
        # create_group_page.select_virtual_controller(create_group_page.select_vc)
        # create_group_page.move_next()
        # create_group_page._set_group_default_device_password1()
        # inner_left_panel.select_group(inner_left_panel.group_1)
        # inner_left_panel.expand_group1.click()
        # inner_left_panel.select_vc_inside_group.click()
        
        wids_page = self.LeftPanel.go_to_wids_page()
        time.sleep(20)
        wids_page.set_detection_infra_threat_detection_level_custom('Medium')
        if inner_left_panel.close_hide_popup:
            inner_left_panel.assert_unprovisioned_alert_popup()
        wids_page.set_detection_clients_threat_detection_level_custom('High')
        if inner_left_panel.close_hide_popup:
            inner_left_panel.assert_unprovisioned_alert_popup()
        # wids_page.save_settings()
        # if inner_left_panel.close_hide_popup:
            # inner_left_panel.assert_unprovisioned_alert_popup()
        
        monitoring_page = self.LeftPanel.go_to_monitoring_page()
        time.sleep(10)
        monitoring_wids_page = self.LeftPanel.go_to_monitoring_wids()
        time.sleep(10)
        self.browser.assert_element(monitoring_page.infrastructure_detection_level_medium, "Infrastructure detection level is not set to medium ")
        time.sleep(10)
        self.browser.assert_element(monitoring_page.client_detection_level_high, "Client detection level is not set to high ")
        import os
        os.environ['device'] = "IAP_1"
        self.take_s2_snapshot('show_ids_detection_config')
        inner_left_panel.select_wireless_configuration_module()
        time.sleep(10)
        wids_page = self.LeftPanel.go_to_wids_page()
        time.sleep(20)
        wids_page.set_detection_infra_threat_detection_level_custom_changes('Off')
        if inner_left_panel.close_hide_popup:
            inner_left_panel.assert_unprovisioned_alert_popup()
        wids_page.set_detection_clients_threat_detection_level_custom_changes('Off')
        if inner_left_panel.close_hide_popup:
            inner_left_panel.assert_unprovisioned_alert_popup()
        
        # inner_left_panel = self.TopPanel.click_slider_icon()
        # if inner_left_panel.assert_group1_and_group2():
            # if inner_left_panel.assert_sample_group_with_vc_present():
                # manage_group_page = inner_left_panel.manage_group()
                # manage_group_page.move_virtual_controller_from_Mygroup(group1=True)
                # inner_left_panel.select_group(inner_left_panel.default_group_click)
                # inner_left_panel = self.TopPanel.click_slider_icon()
                # inner_left_panel.manage_group()
                # manage_group_page.delete_specific_group(group1=True)
        import os
        os.environ['device'] = "IAP_1"
        self.take_s3_snapshot('show_ids_detection_config')
        self.assert_s1_s2_diff(0)
        import os
        os.environ['device'] = "IAP_1"
        self.assert_s1_s3_diff()
        # self.clear()
        