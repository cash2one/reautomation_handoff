from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class FieldValidation(ConfigurationTest):
	'''
	Test class for System Snmp.
	'''
	
	def test_ath_11354_l3_mobilty_field_validation(self):
		system_page = self.LeftPanel.go_to_system_page()
		conf = self.config.config_vars
		self.take_s1_snapshot()
		system_page.click_l3_mobility()
		system_page.click_new_vc_ip_address()
		system_page.create_virtual_controller(conf.vc_ip_invalid_value)
		system_page.click_save_vc()
		system_page.assert_invalid_ip_adress()
		system_page.discard_ip_address()
		system_page.click_new_subnet()
		system_page.create_subnet(conf.vc_ip_invalid_value,conf.vc_ip_invalid_value,conf.default_least_time,conf.vc_ip_invalid_value)
		system_page.click_save_subnet()
		system_page.assert_subnet_ip_address()
		system_page.assert_subnet_netmask()
		system_page.assert_subnet_vlan_id()
		system_page.assert_subnet_vc_ip()
		system_page.create_subnet(conf.gen_vc_gateway,conf.gen_vc_netmask,conf.vc_invalid_vlan1,conf.vc_gateway)
		system_page.click_save_subnet()
		system_page.assert_subnet_vlan_id()
		system_page.cancel_subnet_settings()
		system_page.click_new_subnet()
		system_page.create_subnet(conf.subnet_ip,conf.gen_vc_netmask,conf.subnet_vlan_id,conf.valid_Proxy_Server_value)
		system_page.click_save_subnet()
		system_page.assert_subnet_netmask()
		system_page.cancel_subnet_settings()
		system_page.click_new_subnet()
		system_page.create_subnet(conf.subnet_ip,conf.valid_syslog_server,conf.subnet_vlan_id,conf.valid_Proxy_Server_value)
		system_page.click_save_subnet()
		system_page.assert_netmask_support_error()
		system_page.cancel_subnet_settings()
		