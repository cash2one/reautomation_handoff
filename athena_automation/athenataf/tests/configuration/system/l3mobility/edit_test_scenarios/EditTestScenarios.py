import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class EditTestScenarios(ConfigurationTest):
	'''
	Test class for System L3 Mobility Delete Test Scenarios.
	'''
	
		
	def test_ath_11952_edit_vc_ip_subnet_values(self):
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
		
		system_page.set_home_agent_load_balancing('enabled')
		system_page._save_settings()
		
		system_page.click_l3_mobility()
		system_page.edit_vc_ip_address.click()
		system_page.create_virtual_controller(config.edited_vcip)
		system_page.click_save_vc()
		
		system_page.edit_subnet.click()
		system_page.create_subnet(config.edited_vcaddress,config.vcmask,config.edited_vlanid,config.edited_vcip)
		system_page.click_save_subnet()
			
		system_page.set_home_agent_load_balancing('enabled')
		system_page._save_settings()
		
		
		self.take_s2_snapshot()
		system_page.click_l3_mobility()
		
		system_page.delete_vc_ip_address.click()
		system_page.delete_subnet.click()

		system_page.set_home_agent_load_balancing('disabled')
		system_page._save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	