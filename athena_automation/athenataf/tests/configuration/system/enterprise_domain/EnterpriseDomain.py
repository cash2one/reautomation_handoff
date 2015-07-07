import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class EnterpriseDomain(ConfigurationTest):
	'''
	Test class for System General.
	'''
	
	def test_ath_1434_create_domain(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.click_enterprise_domain()
		system_page.assert_enterprise_domain_page()
		system_page.delete_domain()
		self.take_s1_snapshot()
		# system_page.click_enterprise_domain()
		system_page.assert_enterprise_domain_page()
		system_page.create_domain()
		system_page.assert_create_domain()
		self.take_s2_snapshot()
		# system_page.click_enterprise_domain()
		system_page.assert_enterprise_domain_page()
		system_page.delete_domain()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
		
	def test_ath_1435_delete_domain(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.click_enterprise_domain()
		system_page.assert_enterprise_domain_page()
		system_page.delete_domain()
		self.take_s1_snapshot()
		# system_page.click_enterprise_domain()
		system_page.assert_enterprise_domain_page()
		system_page.create_domain()
		system_page.assert_create_domain()
		# system_page.click_enterprise_domain()
		system_page.assert_enterprise_domain_page()
		system_page.delete_domain()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()