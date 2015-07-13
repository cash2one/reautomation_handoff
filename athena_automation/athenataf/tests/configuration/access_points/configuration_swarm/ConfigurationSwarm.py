import logging
logger = logging.getLogger('athenataf')
import time

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest
from athenataf.lib.functionality.common import DeviceLibrary
from athenataf.config import devices


class ConfigurationSwarm(ConfigurationTest):
    '''
    Test class  for ConfigurationSwarn.
    '''
    def test_ath_8975_configure_single_radio_ap(self):
        self.take_s1_snapshot()
        inner_left_panel = self.TopPanel.click_slider_icon()
        inner_left_panel.select_device()
        self.LeftPanel.go_to_network_page()
        access_point = self.LeftPanel.go_to_access_points()
        access_point.assert_config_single_radio()
        access_point.assign_radio_band('2.4GHz', 'Administrator')
        access_point.edit_access_point()
        access_point.go_to_radio_section()
        access_point.assert_radio_administrator_assigned_fields()
        self.take_s2_snapshot()
        access_point.assign_radio_band('2.4GHz', 'Adaptive')
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(None)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_11238_configure_single_radio_ap_vc(self):
        self.take_s1_snapshot()
        inner_left_panel = self.TopPanel.click_slider_icon()
        inner_left_panel.select_device()
        self.LeftPanel.go_to_network_page()
        access_point = self.LeftPanel.go_to_access_points()
        access_point.edit_access_point()
        access_point.go_to_radio_section()
        access_point.set_24ghz_radio_Administrator_assigned()
        access_point.set_radio_24ghz_band_admn_assgnd_channel(self.config.config_vars.channel_24g_value)
        access_point.set_radio_24ghz_transmit_power(self.config.config_vars.transmit_power_24g_value1)
        access_point.save_settings()
        self.take_s2_snapshot()
        access_point.edit_access_point()
        access_point.go_to_radio_section()      
        access_point.assign_radio_band('2.4GHz', 'Adaptive')
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(None)
        self.assert_s1_s3_diff()
        self.clear()
        
        
    def test_ath_11240_configure_unprovisoined_access_point(self):
        # wirte erase all and factory_reset the IAP. Configure the IAP with wireless network profile and Join the IAP to Athena-central(Configure the IAP with wireless network profile.... has to be done manually)
        conf=self.config.config_vars
        import os
        os.environ['device'] = "IAP_1"
        self.take_s1_snapshot('AP_ENV')
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
        time.sleep(30)
        DeviceLibrary.getPrompt('IAP_1')
        DeviceLibrary.connect_device_to_server('IAP_1')
        time.sleep(300)
        inner_left_panel = self.TopPanel.click_slider_icon()
        # time.sleep(20)
        if not inner_left_panel.verify_unprovision_iap:
            time.sleep(30)
            self.browser.refresh()
            time.sleep(10)
            self.TopPanel.click_slider_icon()
        inner_left_panel.select_unprovision_iap()
        inner_left_panel.assert_unprovisioned_alert_popup()
        inner_left_panel.select_wireless_configuration_module()
        time.sleep(50)
        access_point = self.LeftPanel.go_to_access_points()
        time.sleep(50)
        access_point.edit_access_point()
        access_point.get_ip_from_dhcp.click()
        access_point.click_save_settings()
        if inner_left_panel.close_hide_popup:
            inner_left_panel.assert_unprovisioned_alert_popup()
        time.sleep(10)
        
        default_name = access_point.get_ap_default_name()
        access_point.assert_name_error()
        access_point.set_access_point_name(self.config.config_vars.new_access_point_name)
        if inner_left_panel.close_hide_popup:
            inner_left_panel.assert_unprovisioned_alert_popup()
        time.sleep(10)
        
        access_point.assert_new_access_name()
        access_point.select_static_radio_button()
        access_point.get_and_set_current_server_ip_netmask_dns_ip_gateway()
        access_point.click_save_settings()
        if inner_left_panel.close_hide_popup:
            inner_left_panel.assert_unprovisioned_alert_popup()
        time.sleep(10)
        
        access_point.click_edit_iap()
        access_point.click_radio_accordion()
        
        access_point.aa_radio_24g.click()
        time.sleep(10)
        access_point.aa_radio_5g.click()
        access_point.transmit_power.set(self.config.config_vars.channel_24g_value)
        access_point.transmit_power_5g.set(self.config.config_vars.channel_24g_value)
        access_point.click_save_settings()
        if inner_left_panel.close_hide_popup:
            inner_left_panel.assert_unprovisioned_alert_popup()
        time.sleep(10)
        
        import os
        os.environ['device'] = "IAP_1"
        self.take_s2_snapshot('AP_ENV')
        self.LeftPanel.go_to_network_page()
        access_point = self.LeftPanel.go_to_access_points()
        access_point.edit_access_point()
        access_point.get_set_current_mac_address()
        access_point.get_ip_from_dhcp.click()
        access_point.click_save_settings()
        if inner_left_panel.close_hide_popup:
            inner_left_panel.assert_unprovisioned_alert_popup()
        time.sleep(10)
        
        access_point.set_radio_defaults()
        if inner_left_panel.close_hide_popup:
            inner_left_panel.assert_unprovisioned_alert_popup()
        time.sleep(30)
        import os
        os.environ['device'] = "IAP_1"
        self.take_s3_snapshot('AP_ENV')
        self.assert_s1_s2_diff(0)
        import os
        os.environ['device'] = "IAP_1"
        self.assert_s1_s3_diff()
        # self.clear()
        
    def test_ath_11237_configure_access_points_parameters_swarm_level(self):
        conf = self.config.config_vars
        import os
        os.environ['device'] = "IAP_2"
        time.sleep(30)
        self.take_s1_snapshot('AP_ENV')
        inner_left_panel = self.TopPanel.click_slider_icon()
        inner_left_panel.select_master_slave_group()
        time.sleep(10)
        network_page = self.LeftPanel.go_to_network_page()
        time.sleep(10)
        access_point = self.LeftPanel.go_to_access_points()
        logger.debug('Clicking on edit button')
        access_point.select_particular_vc('IAP_2')
        access_point.select_static_radio_button()
        access_point.get_and_set_slave_iap_details()
        access_point.click_save_settings()
        # access_point.reboot_popup_ok.click()
        import os
        os.environ['device'] = "IAP_2"
        self.take_s2_snapshot('AP_ENV')
        access_point.select_particular_vc('IAP_2')
        access_point.get_ip_from_dhcp.click()
        access_point.click_save_settings()
        import os
        os.environ['device'] = "IAP_2"
        self.take_s3_snapshot('AP_ENV')
        import os
        os.environ['device'] = "IAP_2"
        self.assert_s1_s2_diff(0)
        import os
        os.environ['device'] = "IAP_2"
        self.assert_s1_s3_diff()
        # self.clear('IAP_2')