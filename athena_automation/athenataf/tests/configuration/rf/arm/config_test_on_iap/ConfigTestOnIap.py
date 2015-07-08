import logging
import time
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.common import DeviceLibrary
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class ConfigTestOnIap(ConfigurationTest):
    '''
        Test class for Config Test On Iap.
    '''
    def test_ath_7833_check_rf_arm_override_flag(self):
        self.take_s1_snapshot()
        rf_page = self.LeftPanel.go_to_rf_page()
        rf_page.select_default_instant()
        rf_page.set_arm_parameters()
        self.take_s2_snapshot()
        rf_page.assert_resolve_rf_arm_override_flag()
        rf_page.set_arm_parameters_default()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
    
    def test_ath_11083_change_all_default_config_group_level(self): 
        conf = self.config.config_vars
        self.take_s1_snapshot()
        rf_page = self.LeftPanel.go_to_rf_page()
        rf_page.set_rf_arm_client_control_band_sterring_mode(conf.band_streering_balance_band)
        rf_page.set_rf_arm_client_control_airtime_fairness_mode(conf.new_airtime_fairness_mode_value)
        rf_page.set_rf_arm_client_control_client_match(conf.new_client_match_value)
        rf_page.set_rf_arm_client_control_cm_calculating_interval(conf.cm_calculating_interval_boundry_value1)
        rf_page.set_rf_arm_client_control_cm_neighbor_matching(conf.cm_neighbour_matching_value1)
        rf_page.set_rf_arm_client_control_cm_threshold(conf.cm_threshold_value1)
        rf_page.set_rf_arm_client_control_slb_mode(conf.slb_mode_value_3rd)
        rf_page.set_rf_arm_access_point_control_min_transmit_power(conf.new_min_transmit_power_value1)
        rf_page.set_rf_arm_access_point_control_max_transmit_power(conf.max_transmit_power_value1)
        rf_page.set_rf_arm_access_point_control_client_aware(conf.new_client_aware_value)
        rf_page.set_rf_arm_access_point_control_scanning(conf.new_scanning_value)
        rf_page.set_rf_arm_access_point_control_wide_channel_bands(conf.wide_channel_bands_all)
        rf_page.set_rf_arm_access_point_control_mhz_support(conf.new_mhz_support_value)
        rf_page.save_changes()
        rf_page = self.LeftPanel.go_to_rf_page()
        rf_page.set_rf_arm_client_control_slb_mode(conf.slb_mode_value_2nd)
        rf_page.assert_save_settings_button()
        rf_page.set_rf_arm_client_control_cm_calculating_interval(conf.cm_calculating_interval_boundry_value2)
        rf_page.set_rf_arm_client_control_cm_neighbor_matching(conf.cm_neighbour_matching_value2)
        rf_page.set_rf_arm_client_control_cm_threshold(conf.cm_threshold_value2)
        rf_page.click_on_rf_cancel_button()
        rf_page.assert_edited_rf_arm_values()
        self.take_s2_snapshot()
        rf_page.set_rf_arm_client_control_band_sterring_mode(None)
        rf_page.set_rf_arm_client_control_airtime_fairness_mode(None)
        rf_page.set_rf_arm_client_control_client_match(None)
        rf_page.set_rf_arm_client_control_cm_calculating_interval(None)
        rf_page.set_rf_arm_client_control_cm_neighbor_matching(None)
        rf_page.set_rf_arm_client_control_cm_threshold(None)
        rf_page.set_rf_arm_client_control_slb_mode(None)
        rf_page.set_rf_arm_access_point_control_min_transmit_power(None)
        rf_page.set_rf_arm_access_point_control_max_transmit_power(None)
        rf_page.set_rf_arm_access_point_control_client_aware(None)
        rf_page.set_rf_arm_access_point_control_scanning(None)
        rf_page.set_rf_arm_access_point_control_wide_channel_bands(None)
        rf_page.set_rf_arm_access_point_control_mhz_support(None)
        rf_page.save_changes()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_11084_change_all_default_config_vc_level(self): 
        '''
        override icon steps pending
        reboot changes still needs to be updated
        '''
        conf = self.config.config_vars
        self.take_s1_snapshot()
        innerleftpanel = self.TopPanel.click_slider_icon()
        innerleftpanel.select_device()
        rf_page = self.LeftPanel.go_to_rf_page()
        rf_page.set_rf_arm_client_control_band_sterring_mode(conf.band_streering_force_5ghz)
        logger.debug('RFPage : Selecting Default access in airtime fairness mode')
        rf_page.airtime_fairness_mode.set(conf.airtime_fairness_mode_default_access)
        rf_page.cm_calculating_interval.set(conf.sixty)
        rf_page.set_rf_arm_client_control_cm_neighbor_matching(conf.ninty_five)
        logger.debug('RfPage : Setting vale of cm interval threshold to default value')
        rf_page.cm_threshold.set(conf.cm_threshold_value2)
        rf_page.set_rf_arm_client_control_slb_mode(conf.slb_mode_value_2nd)
        logger.debug('RfPage : Setting max transmit power to default values')
        rf_page.max_transmit_power.set(conf.min_transmit_power_value)
        logger.debug('RfPage : Setting min transmit power to default values')
        rf_page.min_transmit_power.set(conf.new_min_transmit_power_value)
        rf_page.set_rf_arm_access_point_control_client_aware(conf.new_mhz_support_value)
        logger.debug('RfPage : Setting scanning values')
        rf_page.scanning.set(conf.new_mhz_support_value)
        rf_page.set_rf_arm_access_point_control_wide_channel_bands(conf.wide_channel_bands_24ghz)
        rf_page.set_rf_arm_access_point_control_mhz_support(conf.new_mhz_support_value)
        logger.debug('RfPage : Clicking on Save button')
        rf_page.save_settings.click()
        self.take_s2_snapshot()
        rf_page.set_config_to_default()
        rf_page.set_default_neighbour_interval()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_11087_save_alert(self):
        conf = self.config.config_vars
        rf_page = self.LeftPanel.go_to_rf_page()
        rf_page.set_rf_arm_client_control_cm_calculating_interval(conf.cm_calculating_interval_85)
        rf_page.assert_save_cancel_button()
        self.LeftPanel.go_to_monitoring_page()
        time.sleep(5)
        rf_page.assert_save_cancel_button()
        rf_page.click_on_rf_cancel_button()
        self.LeftPanel.go_to_monitoring_page()
        self.Dashboard.isPageLoaded()
    
        
        
    def test_ath_11088_change_all_default_config_unprovisioned_vc(self): 
        '''
        first part of step 1 and step 2 not yet done
        '''
        conf = self.config.config_vars
        self.take_s1_snapshot()
        rf_page = self.LeftPanel.go_to_rf_page()
        rf_page.set_rf_arm_client_control_band_sterring_mode(conf.band_streering_balance_band)
        rf_page.set_rf_arm_client_control_airtime_fairness_mode(conf.new_airtime_fairness_mode_value)
        rf_page.set_rf_arm_client_control_client_match(conf.new_client_match_value)
        rf_page.set_rf_arm_client_control_cm_calculating_interval(conf.cm_calculating_interval_boundry_value1)
        rf_page.set_rf_arm_client_control_cm_neighbor_matching(conf.cm_neighbour_matching_value1)
        rf_page.set_rf_arm_client_control_cm_threshold(conf.cm_threshold_value1)
        rf_page.set_rf_arm_client_control_slb_mode(conf.slb_mode_value_3rd)
        rf_page.set_rf_arm_access_point_control_min_transmit_power(conf.new_min_transmit_power_value1)
        rf_page.set_rf_arm_access_point_control_max_transmit_power(conf.max_transmit_power_value1)
        rf_page.set_rf_arm_access_point_control_client_aware(conf.new_client_aware_value)
        rf_page.set_rf_arm_access_point_control_scanning(conf.new_scanning_value)
        rf_page.set_rf_arm_access_point_control_wide_channel_bands(conf.wide_channel_bands_all)
        rf_page.set_rf_arm_access_point_control_mhz_support(conf.new_mhz_support_value)
        rf_page.save_changes()
        self.take_s2_snapshot()
        rf_page.set_rf_arm_client_control_band_sterring_mode(None)
        rf_page.set_rf_arm_client_control_airtime_fairness_mode(None)
        rf_page.set_rf_arm_client_control_client_match(None)
        rf_page.set_rf_arm_client_control_cm_calculating_interval(None)
        rf_page.set_rf_arm_client_control_cm_neighbor_matching(None)
        rf_page.set_rf_arm_client_control_cm_threshold(None)
        rf_page.set_rf_arm_client_control_slb_mode(None)
        rf_page.set_rf_arm_access_point_control_min_transmit_power(None)
        rf_page.set_rf_arm_access_point_control_max_transmit_power(None)
        rf_page.set_rf_arm_access_point_control_client_aware(None)
        rf_page.set_rf_arm_access_point_control_scanning(None)
        rf_page.set_rf_arm_access_point_control_wide_channel_bands(None)
        rf_page.set_rf_arm_access_point_control_mhz_support(None)
        rf_page.save_changes()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()

    def test_ath_11323_Transmit_Power_Verification_in_Access_Control_Country_Code_Specific(self):
        '''
        US swarm should be in default group
        row is in group1
        '''
        conf=self.config.config_vars
        # inner_left_panel = self.TopPanel.click_slider_icon()
        # if  inner_left_panel.assert_mygroup_without_vc_present():
            # manage_group_page = inner_left_panel.manage_group()
            # manage_group_page.delete_group1()
        # if inner_left_panel.assert_mygroup_with_vc_present():
            # manage_group_page = inner_left_panel.manage_group()
            # manage_group_page.move_virtual_controller_group1()
            # manage_group_page = inner_left_panel.manage_group()
            # manage_group_page.delete_group1()
        # DeviceLibrary.reconnect('IAP_2')
        # import os
        # os.environ['device'] = 'IAP_1'
        # self.take_s1_snapshot()
        # import os
        # os.environ['device'] = "IAP_2"
        # self.take_s1_snapshot()
        innerleftpanel = self.TopPanel.click_slider_icon()
        # create_group = innerleftpanel.add_group()
        # create_group.create_empty_group1(self.config.config_vars.group_1)
        # import time
        # time.sleep(4)
        # managegroup = innerleftpanel.manage_group()
        # managegroup.move_vc_to_group(self.config.config_vars.group_1,'IAP_2')
        # time.sleep(400)
        # DeviceLibrary.reconnect('IAP_2')
        innerleftpanel.select_default_group()
        rf_page = self.LeftPanel.go_to_rf_page()
        rf_page.set_rf_arm_access_point_control_min_transmit_power(conf.new_min_transmit_power_value1)
        rf_page.set_rf_arm_access_point_control_max_transmit_power(conf.max_transmit_power_value1)
        rf_page.save_changes()
        time.sleep(120)
        rf_page.assert_arm_configuration('IAP_1','Minimum Transmit Power            :9')
        rf_page.assert_arm_configuration('IAP_1','Maximum Transmit Power            :24')
        rf_page.assert_min_max_transmit_power_for_country_us_and_in()
        innerleftpanel = self.TopPanel.click_slider_icon()
        innerleftpanel.select_group1_with_one_vc()
        rf_page = self.LeftPanel.go_to_rf_page()
        rf_page.set_rf_arm_access_point_control_min_transmit_power(conf.new_min_transmit_power_value1)
        rf_page.set_rf_arm_access_point_control_max_transmit_power(conf.max_transmit_power_value1)
        rf_page.save_changes()
        time.sleep(120)
        rf_page.assert_arm_configuration('IAP_2','Minimum Transmit Power            :9')
        rf_page.assert_arm_configuration('IAP_2','Maximum Transmit Power            :24')       
        rf_page.assert_min_max_transmit_power_for_country_us_and_in()
        # import os
        # os.environ['device'] = 'IAP_1'
        # self.take_s2_snapshot()
        # import os
        # os.environ['device'] = "IAP_2"
        # self.take_s2_snapshot()
        rf_page.set_rf_arm_access_point_control_min_transmit_power(None)
        rf_page.set_rf_arm_access_point_control_max_transmit_power(None)
        rf_page.save_changes()
        innerleftpanel = self.TopPanel.click_slider_icon()
        innerleftpanel.select_default_group()
        rf_page = self.LeftPanel.go_to_rf_page()
        rf_page.set_rf_arm_access_point_control_min_transmit_power(None)
        rf_page.set_rf_arm_access_point_control_max_transmit_power(None)
        rf_page.save_changes()      
        # import os
        # os.environ['device'] = "IAP_1"
        # self.take_s3_snapshot()
        # import os
        # os.environ['device'] = "IAP_2"
        # self.take_s3_snapshot()
        # import os
        # os.environ['device'] = "IAP_1"
        # self.assert_s1_s2_diff(0)
        # import os
        # os.environ['device'] = "IAP_2"
        # self.assert_s1_s2_diff(0)
        # import os
        # os.environ['device'] = "IAP_1"
        # self.assert_s1_s3_diff()
        # import os
        # os.environ['device'] = "IAP_2"
        # self.assert_s1_s3_diff()
        # self.clear()
        # self.TopPanel.go_to_allgroups()
        # inner_left_panel = self.TopPanel.click_slider_icon()
        # if  inner_left_panel.assert_mygroup_without_vc_present():
            # manage_group_page = inner_left_panel.manage_group()
            # manage_group_page.delete_group1()
        # if inner_left_panel.assert_mygroup_with_vc_present():
            # manage_group_page = inner_left_panel.manage_group()
            # manage_group_page.move_virtual_controller_group1()
            # manage_group_page = inner_left_panel.manage_group()
            # manage_group_page.delete_group1()
 
        
	def test_ath_11085_edit_config(self):
		'''
		as suggested by Michael
		IAP1 : 4.1.1.7
		IAP_2: 4.1.2.3
		'''
		conf = self.config.config_vars
		import os
		os.environ['device'] = 'IAP_2'
		self.take_s1_snapshot("SHOW_ARM_CONFIG")
		import os
		os.environ['device'] = "IAP_1"
		self.take_s1_snapshot("SHOW_ARM_CONFIG")
		innerleftpanel = self.TopPanel.click_slider_icon()
		create_group = innerleftpanel.add_group()
		create_group.create_empty_group1(self.config.config_vars.group_1)
		manage_group = innerleftpanel.manage_group()
		manage_group.move_vc_to_group(self.config.config_vars.group_1,'IAP_2')
		time.sleep(500)
		DeviceLibrary.reconnect('IAP_2')
		innerleftpanel = self.TopPanel.click_slider_icon()
		innerleftpanel.click_on_expand_group_icon(innerleftpanel.expand_group_icon)
		innerleftpanel.select_vc('IAP_1')
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.set_rf_arm_client_control_band_sterring_mode(conf.band_streering_force_5ghz)
		logger.debug('RFPage : Selecting Default access in airtime fairness mode')
		rf_page.airtime_fairness_mode.set(conf.airtime_fairness_mode_default_access)
		rf_page.cm_calculating_interval.set(conf.sixty)
		rf_page.set_rf_arm_client_control_cm_neighbor_matching(conf.ninty_five)
		logger.debug('RfPage : Setting vale of cm interval threshold to default value')
		rf_page.cm_threshold.set(conf.cm_threshold_value2)
		rf_page.set_rf_arm_client_control_slb_mode(conf.slb_mode_value_2nd)
		logger.debug('RfPage : Setting max transmit power to default values')
		rf_page.max_transmit_power.set(conf.min_transmit_power_value)
		logger.debug('RfPage : Setting min transmit power to default values')
		rf_page.min_transmit_power.set(conf.new_min_transmit_power_value)
		rf_page.set_rf_arm_access_point_control_client_aware(conf.new_mhz_support_value)
		logger.debug('RfPage : Setting scanning values')
		rf_page.scanning.set(conf.new_mhz_support_value)
		rf_page.set_rf_arm_access_point_control_wide_channel_bands(conf.wide_channel_bands_24ghz)
		rf_page.set_rf_arm_access_point_control_mhz_support(conf.new_mhz_support_value)
		logger.debug('RfPage : Clicking on Save button')
		rf_page.save_settings.click()
		rf_page.set_rf_arm_fields(set=True)
		self.browser.refresh()
		rf_page.assert_override_flag_button(check='True')
		rf_page.click_on_override_flag()
		rf_page.aserts_overrides_diff()
		rf_page.click_on_close_overrides_overlay()
		innerleftpanel.click_on_close_icon()
		innerleftpanel = self.TopPanel.click_slider_icon()
		innerleftpanel.select_default_group()
		rf_page.set_rf_arm_fields(set=True)
		self.browser.refresh()
		rf_page.assert_override_flag_button(check='False')
		innerleftpanel = self.TopPanel.click_slider_icon()
		innerleftpanel.click_expand_group1_icon()
		innerleftpanel.select_vc('IAP_2')
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.set_rf_arm_client_control_cm_calculating_interval(conf.cm_calculating_interval_66)
		rf_page.set_rf_arm_client_control_cm_neighbor_matching(conf.vlanid)
		rf_page.set_rf_arm_client_control_cm_threshold(conf.transmit_power_24g_value2)
		rf_page.set_rf_arm_access_point_control_min_transmit_power(conf.min_transmit_power_value)
		rf_page.set_rf_arm_access_point_control_max_transmit_power(conf.max_transmit_power_value1)
		rf_page.set_rf_arm_access_point_control_customized_valid_channel(check = 'true')
		rf_page.enable_custom_valid_channel_and_set()
		rf_page.save_changes()
		self.browser.refresh()
		rf_page.click_on_override_flag()
		rf_page.click_on_resolve_all_overrides()
		import os
		os.environ['device'] = "IAP_1"
		self.take_s2_snapshot("SHOW_ARM_CONFIG")
		import os
		os.environ['device'] = "IAP_2"
		self.take_s2_snapshot("SHOW_ARM_CONFIG")
		rf_page.set_rf_arm_fields(set=False)
		rf_page.save_changes()
		innerleftpanel = self.TopPanel.click_slider_icon()
		innerleftpanel.select_default_group()
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.set_rf_arm_fields(set=False)
		rf_page.save_changes()
		innerleftpanel = self.TopPanel.click_slider_icon()
		manage_group = innerleftpanel.manage_group()
		manage_group.move_vc_to_group(self.config.config_vars.default_group,'IAP_2')
		time.sleep(300)
		DeviceLibrary.reconnect('IAP_2')
		manage_group = innerleftpanel.manage_group()
		manage_group.delete_group(manage_group.group1)
		import os
		os.environ['device'] = "IAP_1"
		self.take_s3_snapshot("SHOW_ARM_CONFIG")
		import os
		os.environ['device'] = "IAP_2"
		self.take_s3_snapshot("SHOW_ARM_CONFIG")
		import os
		os.environ['device'] = "IAP_1"
		self.assert_s1_s2_diff(0)
		import os
		os.environ['device'] = "IAP_2"
		self.assert_s1_s2_diff(0)
		import os
		os.environ['device'] = "IAP_1"
		self.assert_s1_s3_diff()
		import os
		os.environ['device'] = "IAP_2"
		self.assert_s1_s3_diff()
		# self.clear()
		
    def test_ath_11322_custom_channel_verification_in_access_control_country_code_specific(self):
        '''
		test case executed on row swarm as suggested by Michael
        '''
        inner_left = self.TopPanel.click_slider_icon()
        inner_left.select_master_slave_group()
        rf_page = self.LeftPanel.go_to_rf_page()
        rf_page.set_rf_arm_access_point_control_customized_valid_channel(check='true')
        rf_page.click_on_edit_24_ghz()
        rf_page.assert_24ghz_checkbox_values()
        rf_page.click_on_close_24_ghz()
        rf_page.click_on_edit_5_ghz()
        rf_page.assert_5ghz_checkbox_values()
        rf_page.click_on_close_5_ghz()
        raw_input('wait')
        rf_page.enable_custom_valid_channel_and_set() #show arm-channel
        rf_page.save_changes()
        time.sleep(120)
        rf_page.assert_arm_channels('IAP_1','6        enable')
        rf_page.assert_arm_channels('IAP_1','6+       enable')
        rf_page.assert_arm_channels('IAP_1','153      enable')
        rf_page.assert_arm_channels('IAP_1','157      enable')
        rf_page.set_rf_arm_access_point_control_customized_valid_channel(check=False)
        rf_page.save_changes()
        time.sleep(120)
        rf_page.assert_arm_channels('IAP_1','153      disable')
        rf_page.assert_arm_channels('IAP_1','157      disable')
