import logging
logger = logging.getLogger('athenataf')
import time
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest
import os
import pdb

class Multiversion(ConfigurationTest):
	'''
	Test class for System Admin DefaultValue.
	'''
	
		
	def test_ath_11326_multiversion_check_for_view_only_guest_registration(self):
		'''
			Snapshot command is remaining for multiple devices
		'''
		conf = self.config.config_vars
		system_page = self.LeftPanel.go_to_system_page()
		time.sleep(10)
		os.environ['device'] = "IAP_1"
		self.take_s1_snapshot()
		os.environ['device'] = "IAP_2"
		self.take_s1_snapshot()
		system_page.go_to_admin_tab()
		system_page.view_only_non_default_values(conf.viewonly,conf.viewonly,conf.viewonly)
		system_page._save_settings()
		system_page.go_to_admin_tab()
		system_page.guest_registration_only_non_default_values(conf.guest_username,conf.guest_password,conf.guest_password)
		system_page._save_settings()
		os.environ['device'] = "IAP_1"
		self.take_s2_snapshot()
		os.environ['device'] = "IAP_2"
		self.take_s2_snapshot()
		system_page.go_to_admin_tab()
		system_page.restore_view_only_default_values()
		system_page.go_to_admin_tab()
		system_page.restore_guest_registration_only_default_values()
		os.environ['device'] = "IAP_1"
		self.take_s3_snapshot()
		os.environ['device'] = "IAP_2"
		self.take_s3_snapshot()
		os.environ['device'] = "IAP_1"
		self.assert_s1_s2_diff(0)
		os.environ['device'] = "IAP_2"
		self.assert_s1_s2_diff(0)
		os.environ['device'] = "IAP_1"
		self.assert_s1_s3_diff()
		os.environ['device'] = "IAP_2"
		self.assert_s1_s3_diff()
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	