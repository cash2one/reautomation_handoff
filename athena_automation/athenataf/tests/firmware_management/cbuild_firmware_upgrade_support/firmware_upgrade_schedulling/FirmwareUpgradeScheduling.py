import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase

class FirmwareUpgradeScheduling(AthenaGUITestCase):
	'''
	Test class for Firmware Upgrade Scheduling.
	'''

		
	def test_ath_9174_upgrade_switch_based_on_user_input(self):
		conf = self.config.config_vars
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		firmware_page.click_switches()
		firmware_page.select_first_switch()
		firmware_page.upgrade_button.click()
		firmware_page.click_on_manual_upgrade()
		firmware_page.select_version_type(conf.version_type_value)
		firmware_page.select_later_date_radio()
		firmware_page.set_upgrade_after_ten_mins()
		firmware_page.click_post_firmware_upgrade()
		firmware_page.asser_successfully_upgrading_msg()
		firmware_page.buy_time()
		firmware_page.asserting_device_upgrade_status()
		
		
	def test_ath_9175_cancel_upgrade(self):
		conf = self.config.config_vars
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		firmware_page.click_switches()
		firmware_page.select_first_switch()
		firmware_page.upgrade_button.click()
		firmware_page.click_on_manual_upgrade()
		firmware_page.select_version_type(conf.version_type_value)
		firmware_page.select_later_date_radio()
		firmware_page.schedule_time()
		firmware_page.click_post_firmware_upgrade()
		firmware_page.cancel_upgrade.click()
		self.browser.refresh()
		firmware_page.assert_cancel_upgrade_button()
		
	def test_ath_9248_display_proper_error_message_when_upgrade_fails(self):
		conf = self.config.config_vars
		firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
		firmware_page.select_first_vc()
		firmware_page.clicking_on_upgrade_firmware()
		firmware_page.click_post_firmware_upgrade()
		import time
		time.sleep(600)
		if not firmware_page.upgrade_failed:
			raise AssertionError("Upgrade 'Failed' status label not found Traceback: %s " %traceback.format_exc())