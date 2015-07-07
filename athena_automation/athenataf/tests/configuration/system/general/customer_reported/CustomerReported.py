import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class CustomerReported(ConfigurationTest):
	'''
	Test class for System General->Customer Reported.
	'''

	def test_ath_11385_browse_the_system_page_with_different_browsers(self):
		self.take_s1_snapshot()
		conf = self.config.config_vars
		system_page = self.LeftPanel.go_to_system_page()
		system_page.edit_vc_ip()
		system_page.set_vc_netmask(conf.gen_vc_netmask)
		system_page.set_vc_gateway(conf.gen_vc_gateway)
		system_page.set_vc_vlan(conf.gen_vc_vlan)
		system_page._save_settings()
		self.take_s2_snapshot()
		system_page.edit_virtual_controller_ip_values()
		system_page.set_virtual_controller_ip(conf.empty)
		system_page.save_virtual_controller_ip_address()
		system_page.set_vc_netmask(conf.empty)
		system_page.set_vc_gateway(conf.empty)
		system_page.set_vc_vlan(conf.empty)
		system_page._save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()