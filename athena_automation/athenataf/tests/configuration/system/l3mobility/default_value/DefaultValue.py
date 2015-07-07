import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DefaultValue(ConfigurationTest):
	'''
	Test class for System L3 Mobility DefaultValue.
	'''
	
		
	def test_ath_11352_check_vc_ip_subnet_defaults(self):
		config = self.config.config_vars
		system_page = self.LeftPanel.go_to_system_page()
		system_page.click_l3_mobility()
		system_page.assert_l3_mobility_page()
		system_page.buy_time()
		if system_page.vc_ip_no_data_msg:
			raise AssertionError("Virtual controller Ip address is not empty!!")
		if system_page.subnet_no_data_msg:
			raise AssertionError("Subnet is not empty!!")
		system_page.assert_home_agent_load_balancing('disable')
		system_page.new_vc_ip_address.click()
		system_page.buy_time()
		system_page.assert_vc_ip_address()
		system_page.vc_ip_cancel_button.click()
		system_page.buy_time()
		system_page.new_subnet.click()
		system_page.assert_subnet_fields()
		system_page.subnet_cancel_button.click()
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	