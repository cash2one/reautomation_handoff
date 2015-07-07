import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.MaintenanceTest import MaintenanceTest

class DeviceManagement(MaintenanceTest):
	'''
	Test class for DeviceManagement.
	'''
	def test_ath_4420_unassign_license(self):
		conf=self.config.config_vars
		self.TopPanel.go_to_allgroups()
		device_mngmt_page = self.LeftPanel.go_to_device_management()
		if device_mngmt_page.unassigned_licence_text:
			device_mngmt_page.change_device1_to_assigned()
			device_mngmt_page.change_device1_to_unassigned()
			device_mngmt_page.assert_device_unassigned()
		elif not device_mngmt_page.unassigned_licence_text:
			device_mngmt_page.change_device1_to_unassigned()
			device_mngmt_page.assert_device_unassigned()
			device_mngmt_page.change_device1_to_assigned()