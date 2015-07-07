import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Configuration(ConfigurationTest):
	'''
		Test class for Configuration.
	'''
	
	def test_ath_8171_change_protection_level_high(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.set_infra_client_high()
		wids_page.assert_infra_client_high()
		self.take_s2_snapshot()
		wids_page.set_infra_client_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8172_change_protection_level_low(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.set_infra_client_low()
		wids_page.assert_infra_client_low()
		self.take_s2_snapshot()
		wids_page.set_infra_client_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8173_change_protection_level_custom(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.set_infra_client_custom()
		wids_page.assert_infra_client_custom()
		self.take_s2_snapshot()
		wids_page.set_infra_client_custom_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8174_change_protection_level_custom_negative(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.set_infra_client_custom_negative()
		wids_page.assert_infra_client_custom_negative()
		self.take_s2_snapshot()
		wids_page.set_infra_client_custom_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8175_edit_protection_level(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.edit_infra_client_protection_level()
		self.take_s2_snapshot()
		wids_page.set_infra_client_protection_level_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8180_set_wireless_containment(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.set_wireless_containment()
		self.take_s2_snapshot()
		wids_page.set_wireless_containment_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(1)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8181_set_wired_containment(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.set_wired_containment()
		wids_page.assert_wired_containment()
		self.take_s2_snapshot()
		wids_page.set_wired_containment_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8182_validate_wid_containment(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.validate_wid_containment()
		wids_page.assert_validated_wid_containment()
		self.take_s2_snapshot()
		wids_page.restore_defaults_wired_wireless_containment_methods()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(1)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8176_check_wids_protection_config_override_flag(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.select_default_instant()
		wids_page.change_wids_protection_settings()
		wids_page.assert_resolve_override_flag()
		self.take_s2_snapshot()
		wids_page.set_wids_protection_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_11164_protection_threat_level_high(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.set_infra_client_high()
		wids_page.assert_infra_client_high()
		self.take_s2_snapshot()
		wids_page.set_infra_client_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11165_protection_threat_level_low(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.set_infra_client_low()
		wids_page.assert_infra_client_low()
		self.take_s2_snapshot()
		wids_page.set_infra_client_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11166_protection_threat_level_custom(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.set_infra_client_custom()
		wids_page.assert_infra_client_custom()
		self.take_s2_snapshot()
		wids_page.set_infra_client_custom_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11167_protection_threat_level_custom_negative(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.set_infra_client_custom_negative()
		wids_page.assert_infra_client_custom_negative()
		self.take_s2_snapshot()
		wids_page.set_infra_client_custom_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11168_protection_threat_level_edit(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.edit_infra_client_protection_level()
		self.take_s2_snapshot()
		wids_page.set_infra_client_protection_level_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_11172_wids_containment_method_configuration(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.set_wired_containment()
		wids_page.set_wireless_containment()
		self.take_s2_snapshot()
		wids_page.set_wireless_containment_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_11174_wids_containment_methods_validation(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.validate_wid_containment()
		wids_page.assert_validated_wid_containment()
		self.take_s2_snapshot()
		wids_page.restore_defaults_wired_wireless_containment_methods()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11350_save_alert_in_wids_protection(self):
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.protection_accordion.click()
		wids_page.infrastructure_protect_custom.click()
		wids_page.click_attacks_protect_infrastructure_custom()
		wids_page.detection_accordion.click()
		wids_page.click_confirm_save_cancel()
		wids_page.click_cancel_settings()
		wids_page.assert_threat_protection_level()
		wids_page.infra_protect_low.click()
		wids_page.click_rf_module()
		
	def test_ath_11170_protection_threat_level_high(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.set_protection_infra_low()
		wids_page.set_protection_client_high()
		wids_page.validate_wid_containment()
		wids_page.assert_validated_wid_containment()
		wids_page.assert_infra_client_high()
		self.take_s2_snapshot()
		wids_page.set_infra_client_default()
		wids_page.set_wids_protection_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11169_wids_protection_config_vc_level(self):
		'''
		Override icon is pending.
		No 'medium' radio button found,Test case is enabling 'low' radio button
		'''
		self.take_s1_snapshot()
		conf = self.config.config_vars
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.click_protection_accordion()
		wids_page.enable_or_disable_rogue_containment(False)
		wids_page.enable_or_disable_protect_ssid(True)
		wids_page.enable_or_disable_protect_ap_impersonation(True)
		wids_page.enable_or_disable_protect_adhoc_network(True)
		wids_page.click_low_protection_client_tick_icon()
		wids_page.save_settings()
		wids_page.set_wired_containment_dropdown(conf.Wired_Containment_On)
		wids_page.set_wireless_containment_dropdown(conf.Wireless_Containment_Tarpit_Invalid)
	
	def test_ath_11348_wids_protection_config_infrastructure_and_client(self):
		self.take_s1_snapshot()
		conf = self.config.config_vars
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.click_protection_accordion()
		wids_page.set_infra_threat_protection_level_high()
		wids_page.save_settings()
		wids_page.assert_infra_level_high()
		wids_page.assert_client_level_off()
		wids_page.set_client_protect_level_low()
		wids_page.save_settings()
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_device()
		wids_page.click_protection_accordion()
		wids_page.set_infra_protection_low_and_wired_wireless_containment('True')
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.select_default_group()
		wids_page.click_protection_accordion()
		wids_page.assert_infra_level_high()
		wids_page.set_infra_protection_low_and_wired_wireless_containment('False')
		wids_page.click_protection_accordion()
		wids_page.set_infra_client_protection_level_default()
		wids_page.set_wired_containment_default()
		wids_page.set_wireless_containment_default()
		
	def test_ath_11171_wids_protection_config_all_iaps_in_a_swarm(self):
		conf = self.config.config_vars
		self.take_s1_snapshot("show_ids_protection_config")
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.click_protection_accordion()
		wids_page.set_infra_threat_protection_level_high()
		logger.debug('WidsPage : Selecting client protection level as custom')
		wids_page.client_protect_custom.click()
		logger.debug('WidsPage : Selecting protect windows bridge')
		wids_page.protect_protect_windows_bridge_checkbox.click()
		wids_page.set_wired_containment_dropdown(conf.Wired_Containment_Off)
		wids_page.set_wireless_containment_dropdown(conf.Wireless_Containment_Tarpit_All)
		self.take_s2_snapshot("show_ids_protection_config")
		wids_page.set_infra_client_default()
		wids_page.set_wids_protection_default()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
