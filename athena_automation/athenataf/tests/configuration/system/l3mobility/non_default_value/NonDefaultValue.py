import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class NonDefaultValue(ConfigurationTest):
	'''
	Test class for System L3 Mobility Non  Default Value.
	'''
	
		
	def test_ath_11353_check_vc_ip_subnet_non_default_values(self):
		config = self.config.config_vars
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.click_l3_mobility()
		system_page.assert_l3_mobility_page()
		
		system_page.click_new_vc_ip_address()
		system_page.create_virtual_controller(config.vcip)
		system_page.click_save_vc()
		system_page.click_new_subnet()
		system_page.create_subnet(config.vcaddress,config.vcmask,config.vlanid,config.vcip)
		system_page.click_save_subnet()
		
		system_page.click_new_vc_ip_address()
		system_page.create_virtual_controller(config.vcip1)
		system_page.click_save_vc()
		system_page.click_new_subnet()
		system_page.create_subnet(config.vcaddress1,config.vcmask,config.vlanid,config.vcip1)
		system_page.click_save_subnet()
		
		system_page.click_new_vc_ip_address()
		system_page.create_virtual_controller(config.vcip2)
		system_page.click_save_vc()
		system_page.click_new_subnet()
		system_page.create_subnet(config.vcaddress2,config.vcmask,config.vlanid,config.vcip2)
		system_page.click_save_subnet()
		
		system_page.click_new_vc_ip_address()
		system_page.create_virtual_controller(config.vcip3)
		system_page.click_save_vc()
		system_page.click_new_subnet()
		system_page.create_subnet(config.vcaddress3,config.vcmask,config.vlanid,config.vcip3)
		system_page.click_save_subnet()
		
		system_page.click_new_vc_ip_address()
		system_page.create_virtual_controller(config.vcip4)
		system_page.click_save_vc()
		system_page.click_new_subnet()
		system_page.create_subnet(config.vcaddress4,config.vcmask,config.vlanid,config.vcip4)
		system_page.click_save_subnet()
		
		system_page.click_new_vc_ip_address()
		system_page.create_virtual_controller(config.vcip5)
		system_page.click_save_vc()
		system_page.click_new_subnet()
		system_page.create_subnet(config.vcaddress5,config.vcmask,config.vlanid,config.vcip5)
		system_page.click_save_subnet()
		system_page.set_home_agent_load_balancing('enabled')
		
		system_page._save_settings()
		
		self.take_s2_snapshot()
		system_page.click_l3_mobility()
		system_page.delete_vc_ip_address.click()
		system_page.delete_subnet.click()
		system_page.delete_vc_ip_address.click()
		system_page.delete_subnet.click()
		system_page.delete_vc_ip_address.click()
		system_page.delete_subnet.click()
		system_page.delete_vc_ip_address.click()
		system_page.delete_subnet.click()
		system_page.delete_vc_ip_address.click()
		system_page.delete_subnet.click()
		system_page.delete_vc_ip_address.click()
		system_page.delete_subnet.click()
		system_page.set_home_agent_load_balancing('disabled')
		system_page._save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	