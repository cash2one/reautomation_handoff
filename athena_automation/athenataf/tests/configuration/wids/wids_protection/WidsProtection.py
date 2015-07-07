import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class WidsProtection(ConfigurationTest):
	'''
	Test class for WIDS Protection.
	'''

	def test_ath_699_check_default_ui_settings(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.assert_wids_protection_section_expanded()
		wids_page.assert_threat_protection_level()
		wids_page.assert_all_attactks_infrastructure_client()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_701_infrastructure_high(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.assert_infrastructure_protection_high_checked()
		self.take_s2_snapshot()
		wids_page.revert_infrastructure_default_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_702_infrastructure_low(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.assert_infrastructure_protection_low_checked()
		self.take_s2_snapshot()
		wids_page.revert_infrastructure_default_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_705_clients_high(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.assert_clients_protection_high_checked()
		self.take_s2_snapshot()
		wids_page.revert_clients_default_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_706_clients_low(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.assert_clients_protection_low_checked()
		self.take_s2_snapshot()
		wids_page.revert_clients_default_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_708_containment_default_settings(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.assert_containment_methods()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_709_containment_wireless_deauth(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.wireless_containment_deauthenticate()
		self.take_s2_snapshot()
		wids_page.restore_default_ui()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(1)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_710_containment_wired_on(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.wired_containment_on()
		self.take_s2_snapshot()
		wids_page.restore_default_ui()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_711_containment_wireless_tarpit_invalid(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.wireless_tarpit_invalid()
		self.take_s2_snapshot()
		wids_page.restore_default_ui()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(1)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_712_containment_wireless_tarpit_all(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.wireless_tarpit_all()
		self.take_s2_snapshot()
		wids_page.restore_default_ui()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(1)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_713_containment_restore(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.restore_defaults_containment_methods()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_6750_protection_tab_text_check(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.assert_threat_protection_tab()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_700_clients_off(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.protection_tab_clients_off()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_707_clients_custom(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.clients_custom_settings()
		self.take_s2_snapshot()
		wids_page.revert_clients_default_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_6783_infrastructure_custom_changes(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.set_detection_infra_threat_detection_level('Custom')
		wids_page.assert_detection_infra_custom_level()
		wids_page.infrastructure_custom_changes()
		self.take_s2_snapshot()
		wids_page.set_detection_infra_threat_detection_level('Off')	
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_6784_infrastructure_high_changes(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.assert_infrastructure_protection_high_checked()
		wids_page.click_high_protection_infra_tick_icon()
		self.take_s2_snapshot()
		wids_page.revert_infrastructure_default_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_6785_infrastructure_low_changes(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.assert_infrastructure_protection_low_checked()
		wids_page.click_low_protection_infra_tick_icon()
		self.take_s2_snapshot()
		wids_page.revert_infrastructure_default_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_6787_client_high_changes(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.assert_clients_protection_high_checked()
		wids_page.click_high_protection_client_tick_icon()
		self.take_s2_snapshot()
		wids_page.revert_clients_default_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_6788_client_low_changes(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.assert_clients_protection_low_checked()
		wids_page.click_low_protection_client_tick_icon()
		self.take_s2_snapshot()
		wids_page.revert_clients_default_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_704_infrastructure_off(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.assert_infrastructure_protection_off_unchecked()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()

	def test_ath_703_infrastructure_custom(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.infrastructure_custom_settings()
		self.take_s2_snapshot()
		wids_page.revert_infrastructure_default_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_6786_set_infrastructure_custom(self):
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
		
	def test_ath_6754_loading_WIDS_protection_page(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.assert_infrastructure_protection_high_checked()
		self.take_s2_snapshot()
		wids_page.revert_infrastructure_default_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(2)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_6757_protection_help_text_availablility(self):
		self.take_s1_snapshot()
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.assert_wids_protection_section_expanded()
		wids_page.click_help()
		wids_page.check_protection_help_text_availablility()
		self.take_s2_snapshot()
		self.assert_s1_s2_diff(None)
		self.clear()
		
	def test_ath_11155_protection_help_text_availablility(self):
		wids_page = self.LeftPanel.go_to_wids_page()
		wids_page.assert_wids_protection_section_expanded()
		wids_page.click_help()
		wids_page.check_protection_help_text_availablility()
