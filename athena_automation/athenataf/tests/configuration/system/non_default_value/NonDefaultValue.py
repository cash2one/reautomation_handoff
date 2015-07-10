import logging
logger = logging.getLogger('athenataf')
import time
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class NonDefaultValue(ConfigurationTest):
	'''
	Test class for System General.
	'''
	
	def test_ath_11340_check_dhcp_non_default_values(self):
		self.take_s1_snapshot()
		conf = self.config.config_vars
		system_page = self.LeftPanel.go_to_system_page()
		system_page.go_to_dhcp_tab()
		system_page.set_dhcp_values()
		system_page.set_dhcp_domain_name(conf.proxy_server_value)
		system_page.set_dhcp_dns_server(conf.vc_gateway)
		system_page.set_dhcp_lease_time(conf.packet_count, conf.least_time_days)
		system_page.set_dhcp_network(conf.vcaddress)
		system_page.set_dhcp_netmask(conf.vcmask)
		system_page._save_settings()
		system_page.go_to_dhcp_tab()
		system_page.set_dhcp_lease_time(conf.least_time, conf.least_time_hours)
		system_page._save_settings()
		system_page.assert_lease_time_error()
		system_page.set_dhcp_lease_time(conf.least_time, conf.least_time_minute)
		system_page._save_settings()
		system_page.assert_lease_time_error()
		self.take_s2_snapshot()
		system_page.restore_dhcp_default_values()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		

	def test_ath_11050_check_dhcp_non_default_values(self):
		path = self.config.config_vars
		system_page = self.LeftPanel.go_to_system_page()
		system_page.edit_dhcp_non_default_values()
		logger.debug("SystemPage : Click 'Save Settings' button")
		system_page._save_settings()
		system_page.click_reboot_ok_button()
		time.sleep(60)
		system_page.assert_system_page_vc_field_values("IAP_1","sh ru | inc allow","allowed-vlan all")
		system_page.assert_system_page_vc_field_values("IAP_1","sh ru | inc telnet","telnet-server")
		system_page.assert_system_page_vc_field_values("IAP_1","sh ru | inc led","led-off")
		system_page.assert_system_page_vc_field_values("IAP_1","sh ru | inc deny","deny-inter-user-bridging")
		system_page.assert_system_page_vc_field_values("IAP_1","sh ru | inc dynamic","dynamic-radius-proxy")
		system_page.assert_system_page_vc_field_values("IAP_1","sh ru | inc mas","mas-integration")
		
		system_page.set_dropdown_value_default('auto join mode')
		system_page.set_dropdown_value_default('telnet server')
		system_page.set_dropdown_value_default('led display')
		system_page.set_dropdown_value_default('extended ssid')
		system_page.set_dropdown_value_default('deny inter')
		system_page.set_dropdown_value_default('deny local routing')

		logger.debug("SystemPage : Set value in 'dynamic_radius_proxy' drop-down")
		system_page.dynamic_radius_proxy.set(path.sys_disable)
		logger.debug("SystemPage : Set value in 'mas_integration' drop-down")
		system_page.mas_integration.set(path.sys_disable)
		logger.debug("SystemPage : Click 'Save Settings' button")
		system_page._save_settings()
		system_page.click_reboot_ok_button()