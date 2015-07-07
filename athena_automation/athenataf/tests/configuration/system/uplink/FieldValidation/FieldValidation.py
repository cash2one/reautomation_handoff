import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class FieldValidation(ConfigurationTest):
	'''
	Test class for System uplink module.
	'''

	def test_ath_11946_check_help_text(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.click_uplink()
		system_page.enable_help()
		system_page.assert_help_option_for_uplink_accordion
	
	def test_ath_11349_uplink_field_validation(self):
		conf=self.config.config_vars
		system_page = self.LeftPanel.go_to_system_page()
		system_page.click_uplink()
		system_page.set_wifi_name(conf.wifi_name1)
		system_page.set_wifi_management(None)
		system_page.set_wifi_passphrase_text(conf.wifi_passphrase)
		system_page._save_settings()
		system_page.assert_wifi_passphrase_text_error1('true')
		system_page.set_wifi_passphrase_format(True)
		system_page.assert_wifi_passphrase_text_error2('true')
		
		system_page.set_management_enforce_uplink(conf.enforce_uplink1)
		system_page.set_management_Pre_emption(True)
		system_page.set_management_vpn_failover_timeout(conf.management_failover)
		system_page.set_management_internet_failover(True)
		system_page.assert_management_vpn_failover_timeout_error('true')
		system_page.set_management_failover_internet_packet_freq(conf.management_failover)
		system_page.set_management_failover_packet_lost_count(conf.management_failover)
		system_page.set_management_internet_check_timeout(conf.management_failover)
		system_page._save_settings()
		system_page.assert_management_packet_send_frequency_error('true')
		system_page.assert_management_packet_lost_count_error('true')
		system_page.assert_management_internet_check_timeout_error('true')
		
		system_page.pppoe_service_name(conf.pppoe_service_name)
		system_page.set_pp_chap_secret1(conf.chap_secret)
		system_page.set_pp_chap_secret2(conf.re_chap_secret)
		system_page.set_pp_password(conf.chap_secret)
		system_page.set_pp_retype_password(conf.re_chap_secret)
		system_page._save_settings()
		system_page.assert_pp_chap_secret_error('true')
		system_page.assert_password_error('true')
		system_page.click_on_cancel_settings()