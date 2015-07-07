import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class L3Mobility(ConfigurationTest):
	'''
	Test class for System General.
	'''
	
	def test_ath_1433_subnet_non_default(self):
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.click_l3_mobility()
		system_page.assert_l3_mobility_page()
		system_page.create_virtual_controller_ip_address()
		system_page.create_subnets()
		self.take_s2_snapshot()
		system_page.click_l3_mobility()
		system_page.delete_subnets()
		system_page.delete_virtual_controller_ip_address()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		# system_page.assert_virtual_controller_ip_address()