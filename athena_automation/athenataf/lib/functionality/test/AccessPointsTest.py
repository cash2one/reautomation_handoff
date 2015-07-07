from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase
from athenataf.lib.functionality.page.configuration.network.NetworkPage import NetworkPage
from athenataf.lib.functionality.page.configuration.accessPoints.AccessPointsPage import AccessPointsPage

import logging
logger = logging.getLogger('athenataf')    

class AccessPointsTest(AthenaGUITestCase):

	def __init__(self, config):
		super(AccessPointsTest, self).__init__(config)
		self.NetworkPage = None
		self.config = config

	def setUpTestClass(self, IAP=False):
		logger.debug("AccessPointsTest: setUpTestClass")	
		AthenaGUITestCase.setUpTestClass(self, IAP)
		if not IAP:
			logger.debug("AccessPointsTest: Go To Configuration.")
			all_group_page = self.LeftPanel.go_to_configuration()
			logger.debug("AccessPointsTest: Go To Network.")
			self.NetworkPage = all_group_page.go_to_networks()
			access_point = self.LeftPanel.go_to_access_points()
			access_point.set_adaptive_radio_defaults()
			self.LeftPanel.go_to_access_points()
			access_point.edit_access_point()
			access_point.go_to_uplink()
			access_point.set_default_value_of_uplink_management_vlan()
			access_point.set_default_value_of_etho_bridging()
			access_point.edit_access_point()
			access_point.get_ip_from_dhcp.click()
			access_point.configure_preffered_master(enable=False)
			

	def assertPageLoaded(self, page_name, msg=None):
		msg = msg or ""
		if page_name.isPageLoaded():
			logger.debug("Page Loaded Successfully")
		else:
			raise AssertionError("%s.\n%s Page does not get loaded" % (msg, page_name))

	def tearDown(self):
		self.browser.refresh()
		if self.LeftPanel.save_pop_up:
			self.LeftPanel.save_pop_up.click()
			import time
			time.sleep(15)
		# self.LeftPanel.assert_delta_config_icon()
		self.LeftPanel.configuration.click()