import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest
from athenataf.lib.functionality.common import DeviceLibrary

class Configuration(ConfigurationTest):
    '''
        Test class for Configuration.
    '''
    def test_ath_8186_check_rf_config_override_flag(self):
        self.take_s1_snapshot()
        rf_page = self.LeftPanel.go_to_rf_page()
        rf_page.select_default_instant()
        rf_page.set_legacy_radio_parameter()
        self.take_s2_snapshot()
        rf_page.assert_detection_resolve_override_flag()
        rf_page.set_legacy_radio_parameter_default()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_11099_radio_config_edit_group_level(self):
        conf = self.config.config_vars
        rf_page = self.LeftPanel.go_to_rf_page()
        rf_page.open_radio_accordion()
        self.take_s1_snapshot()
        rf_page.set_legacy_only_24ghz(conf.legacy_only_enabled)
        rf_page.set_dropdown_11d_11h_24ghz(conf.band_802_enabled)
        rf_page.set_beacon_interval_24ghz(conf.new_beacon_interval_value)
        rf_page.set_interface_immunity_24ghz(conf.interface_immunity_5)
        rf_page.set_channel_switch_announce_24ghz(conf.new_channel_switch_announce_5ghz_value)
        rf_page.set_background_spectrum_24ghz(conf.new_background_spectrum_24ghz_value)
        rf_page.set_legacy_only_5ghz(conf.legacy_only_enabled)
        rf_page.set_dropdown_11d_11h_5ghz(conf.band_802_enabled)
        rf_page.set_beacon_interval_5ghz(conf.beacon_interval_value_200)
        rf_page.set_interface_immunity_5ghz(conf.interface_immunity_1)
        rf_page.set_channel_switch_announce_5ghz(conf.new_channel_switch_announce_5)
        rf_page.set_background_spectrum_5ghz(conf.new_background_spectrum_5ghz_value)
        rf_page.save_changes()
        rf_page.set_legacy_only_24ghz(conf.legacy_only_24ghz_value)
        rf_page.set_dropdown_11d_11h_24ghz(conf.band_802_disabled)
        rf_page.set_beacon_interval_24ghz(conf.beacon_interval_value_120)
        rf_page.set_interface_immunity_24ghz(conf.interface_immunity_24ghz_value)
        rf_page.set_channel_switch_announce_24ghz(conf.channel_switch_announce_24ghz_value)
        rf_page.set_background_spectrum_24ghz(conf.background_spectrum_24ghz_value)
        rf_page.save_changes()
        self.take_s2_snapshot()
        rf_page.set_2ghz_band_values_to_default()
        rf_page.set_5ghz_band_values_to_default()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_11103_single_radio_config(self):
        conf = self.config.config_vars
        rf_page = self.LeftPanel.go_to_rf_page()
        rf_page.open_radio_accordion()
        rf_page.set_2ghz_band_values_to_default()
        rf_page.set_5ghz_band_values_to_default()
        self.take_s1_snapshot()
        rf_page.set_beacon_interval_24ghz(conf.new_beacon_interval_value)
        rf_page.set_beacon_interval_5ghz(conf.beacon_interval_value_200)
        rf_page.set_channel_switch_announce_24ghz(conf.new_channel_switch_announce_5ghz_value)
        rf_page.set_channel_switch_announce_5ghz(conf.new_channel_switch_announce_5)
        rf_page.set_background_spectrum_24ghz(conf.new_background_spectrum_24ghz_value)
        rf_page.set_background_spectrum_5ghz(conf.new_background_spectrum_5ghz_value)
        rf_page.save_changes()
        self.take_s2_snapshot()
        rf_page.set_2ghz_band_values_to_default()
        rf_page.set_5ghz_band_values_to_default()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_11100_radio_config_vc_level(self):
        conf = self.config.config_vars
        rf_page = self.LeftPanel.go_to_rf_page()
        rf_page.select_default_instant()
        rf_page.open_radio_accordion()
        self.take_s1_snapshot()
        rf_page.set_legacy_only_24ghz(conf.legacy_only_enabled)
        rf_page.set_dropdown_11d_11h_24ghz(conf.band_802_enabled)
        rf_page.set_beacon_interval_24ghz(conf.new_beacon_interval_value)
        rf_page.set_interface_immunity_24ghz(conf.interface_immunity_5)
        rf_page.set_channel_switch_announce_24ghz(conf.new_channel_switch_announce_5ghz_value)
        rf_page.set_background_spectrum_24ghz(conf.new_background_spectrum_24ghz_value)
        rf_page.set_legacy_only_5ghz(conf.legacy_only_enabled)
        rf_page.set_dropdown_11d_11h_5ghz(conf.band_802_enabled)
        rf_page.set_beacon_interval_5ghz(conf.beacon_interval_value_200)
        rf_page.set_interface_immunity_5ghz(conf.interface_immunity_1)
        rf_page.set_channel_switch_announce_5ghz(conf.new_channel_switch_announce_5)
        rf_page.set_background_spectrum_5ghz(conf.new_background_spectrum_5ghz_value)
        rf_page.save_changes()
        rf_page.set_legacy_only_24ghz(conf.legacy_only_24ghz_value)
        rf_page.set_dropdown_11d_11h_24ghz(conf.band_802_disabled)
        rf_page.set_beacon_interval_24ghz(conf.beacon_interval_value_120)
        rf_page.set_interface_immunity_24ghz(conf.interface_immunity_24ghz_value)
        rf_page.set_channel_switch_announce_24ghz(conf.channel_switch_announce_24ghz_value)
        rf_page.set_background_spectrum_24ghz(conf.background_spectrum_24ghz_value)
        rf_page.save_changes()
        self.take_s2_snapshot()
        rf_page.assert_detection_resolve_override_flag()
        rf_page.set_legacy_radio_parameter_default()
        rf_page.set_2ghz_band_values_to_default()
        rf_page.set_5ghz_band_values_to_default()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_11101_radio_config_unprovisioned_iap(self):
        conf = self.config.config_vars
        inner_left_panel = self.TopPanel.click_slider_icon()
        inner_left_panel.click_all_groups_label()
        device_mgmt = self.LeftPanel.go_to_device_management()
        device_mgmt.get_and_search_mac_address()
        device_mgmt.select_virtual_controller(device_mgmt.device_selector_1)
        device_mgmt.select_assign_group()
        device_mgmt.all_group.click()
        device_mgmt.click_assign()
        logger.debug('DeviceManagement: Clicking on ok button')
        device_mgmt.ok_button.click()
        device_mgmt.assert_group_name(conf.unprovisioned)
        time.sleep(10)
        DeviceLibrary.factoryReset('IAP_1')
        time.sleep(10)
        inner_left_panel = self.TopPanel.click_slider_icon()
        inner_left_panel.select_unprovision_iap()
        inner_left_panel.assert_unprovisioned_alert_popup()
        rf_page = self.LeftPanel.go_to_rf_page()
        rf_page.open_radio_accordion()
        import os
        os.environ['device'] = "IAP_1"
        self.take_s1_snapshot("show_radio_config")
        rf_page.set_legacy_only_24ghz(conf.legacy_only_enabled)
        rf_page.set_dropdown_11d_11h_24ghz(conf.band_802_enabled)
        rf_page.set_beacon_interval_24ghz(conf.new_beacon_interval_value1)
        rf_page.set_interface_immunity_24ghz(conf.interface_immunity_1)
        rf_page.set_channel_switch_announce_24ghz(conf.new_channel_switch_announce_3)
        rf_page.set_background_spectrum_24ghz(conf.new_background_spectrum_24ghz_value)
        rf_page.set_legacy_only_5ghz(conf.legacy_only_enabled)
        rf_page.set_dropdown_11d_11h_5ghz(conf.band_802_enabled)
        rf_page.set_beacon_interval_5ghz(conf.sixty)
        rf_page.set_interface_immunity_5ghz(conf.interface_immunity_5)
        rf_page.set_channel_switch_announce_5ghz(conf.new_channel_switch_announce_5)
        rf_page.set_background_spectrum_5ghz(conf.new_background_spectrum_5ghz_value)
        rf_page.save_changes()
        time.sleep(20)
        import os
        os.environ['device'] = "IAP_1"
        self.take_s2_snapshot("show_radio_config")
        rf_page.set_2ghz_band_values_to_default()
        rf_page.set_5ghz_band_values_to_default()
        rf_page.save_changes()
        os.environ['device'] = "IAP_1"
        self.take_s3_snapshot("show_radio_config")
        create_group_page = inner_left_panel.click_configuration_page_new_group_button()
        create_group_page.create_empty_group1('group1')
        import os
        os.environ['device'] = "IAP_1"
        self.assert_s1_s2_diff(0)
        os.environ['device'] = "IAP_1"
        self.assert_s1_s3_diff()
        self.clear()
    
    def test_ath_11102_radio_config_swarm_level(self):
        conf = self.config.config_vars
        rf_page = self.LeftPanel.go_to_rf_page()
        rf_page.open_radio_accordion()
        self.take_s1_snapshot("show_radio_config")
        rf_page.set_legacy_only_24ghz(conf.legacy_only_5ghz_value)
        rf_page.set_dropdown_11d_11h_24ghz(conf.band_802_enabled)
        rf_page.set_beacon_interval_24ghz(conf.cm_calculating_interval_85)
        rf_page.set_interface_immunity_24ghz(conf.interface_immunity_5)
        rf_page.set_channel_switch_announce_24ghz(conf.announcement_count_8)
        rf_page.set_background_spectrum_24ghz(conf.new_background_spectrum_24ghz_value)
        
        rf_page.set_legacy_only_5ghz(conf.legacy_only_enabled)
        rf_page.set_dropdown_11d_11h_5ghz(conf.band_802_enabled)
        rf_page.set_beacon_interval_5ghz(conf.beacon_interval_450)
        rf_page.set_interface_immunity_5ghz(conf.one_cm_threshold_value)
        rf_page.set_channel_switch_announce_5ghz(conf.new_interface_immunity_24ghz_value)
        rf_page.set_background_spectrum_5ghz(conf.background_spectrum_5ghz_value)
        rf_page.save_changes()
        self.take_s2_snapshot("show_radio_config")
        rf_page.set_2ghz_band_values_to_default()
        rf_page.set_5ghz_band_values_to_default()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        