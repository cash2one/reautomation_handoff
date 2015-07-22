import logging
logger = logging.getLogger('athenataf')

import time
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class FieldValidation(ConfigurationTest):
	'''
		FieldValidation : Test class for network configuration Security.
	'''

	def test_ath_12059_field_validation_for_radius_server(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		#changes made by suganya
		system = self.LeftPanel.go_to_system_page()
		time.sleep(20)
		system.set_general_dynamic_proxy('disabled')
		system._save_settings()
		security = self.LeftPanel.go_to_security()
		security.delete_authentication_server()
		self.take_s1_snapshot()
		security.validate_auth_server_1()
		system = self.LeftPanel.go_to_system_page()
		time.sleep(20)
		system.set_general_dynamic_proxy('enabled')
		system._save_settings()
		security = self.LeftPanel.go_to_security()
		security.create_auth_server.click()		
		#changes made by suganya
		security.create_authentication_server(mask = conf.invalid_radius_server_drp_mask,vlan = conf.invalid_radius_server_drp_vlan_3333)
		security.save_auth_server()	
		security.assert_drp_mask_error()
		#changes made by suganya
		#security.assert_drp_vlan_error()
		#security.create_authentication_server(mask = conf.invalid_radius_server_drp_mask,vlan = conf.invalid_radius_server_drp_vlan_3333)
		security.auth_server_cancel.click()
		self.take_s2_snapshot()
		#changes made by suganya		
		#security.assert_drp_mask_error()
		network_page = self.LeftPanel.go_to_network_page()
		self.NetworkPage.delete_network_if_present()
		system = self.LeftPanel.go_to_system_page()
		time.sleep(20)
		system.set_general_dynamic_proxy('disabled')
		system._save_settings()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		# self.clear()
		
	def test_ath_13334_Field_validation_for_coa_only_server(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		security = self.LeftPanel.go_to_security()
		security.delete_authentication_server()
		security.create_new_server()
		security.set_coa_only_checkbox(True)
		security.create_coa_server1(coa_name=conf.invalid_coa_name,coa_ip=conf.coa_valid_ip,coa_shared_key=conf.coa_valid_shared_key,coa_retype_key=conf.coa_valid_shared_key,coa_port=conf.invalid_coa_air_group_port)
		self.browser.assert_element(security.auth_server_name_error,'CoA name error message not displayed')
		self.browser.assert_element(security.AirGroup_Port_error,'Air Group Port error message not displayed')
		security.set_coa_only_checkbox(True)
		security.create_coa_server1(coa_name=conf.coa_valid_name,coa_ip=conf.coa_valid_ip,coa_shared_key=conf.coa_valid_shared_key,coa_retype_key=conf.coa_valid_shared_key,coa_port=conf.valid_downstream)
		security.delete_authentication_server()
		
		
	def test_ath_12058_delete_the_created_radius_server(self):
		conf = self.config.config_vars
		self.NetworkPage.delete_network_if_present()
		security = self.LeftPanel.go_to_security()
		security.delete_authentication_server()
		self.take_s1_snapshot()
		security = self.LeftPanel.go_to_security()
		security.create_auth_server.click()
		security.create_authentication_server(name=conf.auth_rad1, ip=conf.auth_rad1_ip, sharedkey=conf.internal_server_password,retypekey=conf.internal_server_password)
		security.save_auth_server()
		security.click_edit_auth_server()
		security.create_authentication_server(ip=conf.auth_ip, sharedkey=conf.auth_shared_key1,retypekey=conf.auth_shared_key1,rfc=True,actport=conf.auth_acct_port,timeout=conf.vlan,retrycount= conf.auth_retry_count,authport = conf.auth_port_value,nas_ip=conf.auth_nas_ip,nas_identifier_value=conf.auth_nas_identifier,coa_port=conf.auth_port_valid)
		security.save_auth_server()
		security.create_auth_server.click()
		security.create_authentication_server(name=conf.auth_radius_name1, ip=conf.auth_radius_ip1, sharedkey=conf.auth_radius_shared_key1,retypekey=conf.auth_radius_shared_key1,rfc=True,nas_ip=conf.nas_ip,nas_identifier_value=conf.auth_nsi_identifier_new)
		security.save_auth_server()
		self.take_s2_snapshot()
		security.delete_authentication_server()
		security.delete_authentication_server()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		# self.clear()