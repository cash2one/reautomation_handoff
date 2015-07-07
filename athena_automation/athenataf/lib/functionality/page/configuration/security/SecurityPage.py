from athenataf.lib.util.WebPage import WebPage
import logging
logger = logging.getLogger('athenataf')
import traceback
import time


class SecurityPage(WebPage):
	def __init__(self, test, browser, config):
		WebPage.__init__(self, "Security", test, browser, config)
		self.test.assertPageLoaded(self)
		
		
	def isPageLoaded(self):
		if self.create_auth:
			return True	
		else:
			return False 
			
	def click_firewall(self):
		logger.debug('SecurityPage: Clicking on Firewall Setting Label')
		self.firewall_settings.click()

	def assert_management_subnet(self):
		logger.debug('SecurityPage: Asserting Management Subnet field')
		if self.management_subnet:
			return True
		else:
			import traceback
			raise AssertionError("Exception occured in UI feature identification i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
			
	def assert_subnet(self):
		if not self.delete:
			self.create_new_subnet()
		else:
			return True
			
	def create_new_subnet(self):
		logger.debug('SecurityPage: Setting the network subnet value')
		self.network_subnet.set(self.config.config_vars.network_subnet)
		logger.debug('SecurityPage: Setting the netmask value')
		self.network_mask.set(self.config.config_vars.network_mask)
		logger.debug('SecurityPage: Setting the network subnet value')
		self.network_subnet.set(self.config.config_vars.network_subnet)
		logger.debug('SecurityPage: Setting the netmask value')
		self.network_mask.set(self.config.config_vars.network_mask)
		logger.debug('SecurityPage: Clicking add button')
		self.add_subnet.click()
		
	def delete_subnet(self):
		# self.subnet_value.click()
		logger.debug('SecurityPage: Clicking delete button')
		self.delete.click()
		
	def delete_all_subnet(self):
		# self.subnet_value.click()
		logger.debug('SecurityPage: Clicking delete button')
		self.delete_all.click()
		
	def save_settings(self):
		logger.debug('SecurityPage: Clicking save settings button')
		self.save_setting.click()
		self.buy_time()
		
	def buy_time(self):
		time.sleep(15)
		
	def is_external_captive_profile_present(self):
		logger.debug('SecurityPage: Clicking on External Captive Portal Accordion')
		self.external_captive_profile.click()
		if self.captive_role:
			return True
		else:
			return False
			
	def delete_external_captive_role(self):
		'''
			Deleting external captive portal
		'''
		for i in range(1,4):
			self.external_captive_profile.click()
			if not self.captive_role:
				logger.debug('SecurityPage: All Captive Roles deleted')
				break
			self.buy_time()
			logger.debug('SecurityPage: Clicking n Captive Role')
			self.captive_role.click()
			self.buy_time()
			logger.debug('SecurityPage: Clicking delete button')
			self.delete_external_captive.click()
			self.buy_time()
			logger.debug('SecurityPage: Clicking save settings button')
			self.save_setting.click()
			self.buy_time()
		
	def assert_captive_role_deleted(self):	
		if self.captive_role:
			# return True
		# else:
			# import traceback
			raise AssertionError("Delete  action failed .Traceback: %s " %traceback.format_exc())
		
	def go_to_roles(self):
		logger.debug('SecurityPage: Clicking Roles accordion')
		self.roles_accordion.click()
		time.sleep(10)
	
	def assert_new_role_setup(self):
		import traceback
		logger.debug('SecurityPage: Clicking new button')
		self.create_role.click()
		logger.debug('SecurityPage: Asserting the Role fields')
		if not self.role_input:
			raise AssertionError("Role input box not visible i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		if not self.create_new_role:
			raise AssertionError("Ok button not visible i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		if not self.cancel_new_role:
			raise AssertionError("Cancel button not visible i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		
	def create_new_role(self):
		import traceback
		if self.new_role:
			logger.debug('SecurityPage: Clicking ok button')
			self.new_role.click()
			logger.debug('SecurityPage: Clicking delete button')
			self.delete_role.click()
			self.browser.accept_alert()
			time.sleep(15)
		if not self.role_input:
			self.create_role.click()
		self.role_input.set(self.config.config_vars.Role_Name)
		logger.debug('SecurityPage: Clicking ok button')
		self.ok.click()
		if not self.new_role:
			raise AssertionError("New role setup failed i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		logger.debug('SecurityPage: Clicking save settings button')
		self.save_setting.click()
		self.buy_time()
		
	def delete_cppm_server(self):
		'''
			Deleting the authentication server
		'''
		if self.delete_auth_server :
		# self.cppm_server_name.click()
			self.delete_auth_server.click()
			self.browser.accept_alert()
			self.buy_time()
		
	def assert_add_management_subnet_fields(self):
		import traceback
		if not self.network_subnet:
			raise AssertionError("Network subnet field is not present i.e %s. Traceback: %s" % traceback.format_exc())
		if not self.network_mask:
			raise AssertionError("Network mask field is not present i.e %s. Traceback: %s" % traceback.format_exc())
		if not self.restrict_corporate_access_checkbox.get_selected() == self.config.config_vars.default_manage_internet_failover:
			raise AssertionError("Restrict corporate access is not set to Disabled i.e %s. Traceback: %s" % traceback.format_exc())
			
	def delete_roles(self):
		if self.new_role:
			logger.debug('SecurityPage: Clicking ok button')
			self.new_role.click()
			logger.debug('SecurityPage: Clicking delete button')
			self.delete_role.click()
			self.browser.accept_alert()
			time.sleep(20)
			
	def delete_captive_portal(self):
		if self.captive_role:
			time.sleep(3)
			logger.debug('SecurityPage: Clicking n Captive Role')
			self.captive_role.click()
			logger.debug('SecurityPage: Clicking delete button')
			self.delete_external_captive.click()
			logger.debug('SecurityPage: Clicking save settings button')
			self.save_setting.click()
			time.sleep(15)
		if self.captive_portal_name:
			time.sleep(3)
			logger.debug('SecurityPage: Clicking n Captive Role')
			self.captive_portal_name.click()
			logger.debug('SecurityPage: Clicking delete button')
			self.delete_external_captive_2.click()
			logger.debug('SecurityPage: Clicking save settings button')
			self.save_setting.click()
			time.sleep(15)
			
	def create_new_captive_portal(self):
		logger.debug('SecurityPage: Clicking new ')
		self.create_external_captive.click()
		time.sleep(5)
		logger.debug('SecurityPage: Setting the captive portal Name')
		self.name_text_box.set(self.config.config_vars.Role_Name)
		logger.debug('SecurityPage: Selecting the captive portal Type')
		self.captive_portal_type.set(self.config.config_vars.Captive_Role_Text)
		logger.debug('SecurityPage: Setting the captive portal IP or HostName')
		self.captive_portal_ip.set(self.config.config_vars.Captive_Role_Ip)
		logger.debug('SecurityPage: Setting the captive portal URL')
		self.captive_portal_url.set(self.config.config_vars.redirect_url)
		logger.debug('SecurityPage: Setting the captive portal Port')
		self.captive_portal_port.set(self.config.config_vars.Captive_Role_Port)
		logger.debug('SecurityPage: Setting the captive portal Auth Text')
		self.captive_portal_auth_text.set(self.config.config_vars.Captive_Role_Text)
		logger.debug('SecurityPage: Clicking save button')
		self.captive_portal_save_button.click()
		logger.debug('SecurityPage: Clicking save settings button')
		self.save_setting.click()
		time.sleep(15)
		
	def assert_new_captive_portal(self):
		import traceback
		if not self.captive_portal_name:
			raise AssertionError("New portal has not been created i.e %s. Traceback: %s" % traceback.format_exc())
		
	def click_on_external_captive_accordion(self):
		logger.debug('SecurityPage: Clicking on External Captive Portal Accordion')
		self.external_captive_profile.click()
		
	def delete_authentication_server(self):
		'''
			Deleting the authentication server
		'''
		self.buy_time()
		if self.delete_auth_server:
			# self.auth_server_name.click()
			self.buy_time()
			logger.debug('SecurityPage: Clicking delete button')
			self.delete_auth_server.click()
			self.buy_time()
			self.browser.accept_alert()
			self.buy_time()
			
	def delete_user_for_internal_server(self):	
		self.buy_time()
		logger.debug('SecurityPage: Clicking on User for Internal Server Accordion')
		self.user_for_internal_server.click()
		if not self.disabled_delete_user_all:
			logger.debug('SecurityPage: Clicking on Delete all button')
			self.delete_user_all.click()
			self.browser.accept_alert()
			self.buy_time()
			
	def delete_multiple_roles(self):	
		time.sleep(5)
		logger.debug("SecurityPage : open roles accordion.")
		self.roles_accordion.click()
		logger.debug("SecurityPage : Click on role name.")
		self.role1.click()
		logger.debug("SecurityPage : Click Delete.")
		self.delete_role1.click()
		logger.debug("SecurityPage : Access alert.")
		self.browser.accept_alert()
		self.buy_time()
		logger.debug("SecurityPage : Click on role name.")
		self.role2.click()
		logger.debug("SecurityPage : Click Delete.")
		self.delete_role2.click()
		logger.debug("SecurityPage : Access alert.")
		self.browser.accept_alert()
		self.buy_time()
		logger.debug("SecurityPage : Click on role name.")
		self.role3.click()
		logger.debug("SecurityPage : Click Delete.")
		self.delete_role3.click()
		logger.debug("SecurityPage : Access alert.")
		self.browser.accept_alert()
		self.buy_time()

	def assert_delete_button_disabled(self):
		
		time.sleep(5)
		logger.debug("SecurityPage : open roles accordion.")
		self.roles_accordion.click()
		logger.debug("AccessPage : Click on role name.")
		self.default_network_role.click()
		time.sleep(5)
		if not self.network_delete_button_disabled_1:
			import traceback
			raise AssertionError("Delete button visible .Traceback: %s " %traceback.format_exc())

	def delete_new_role(self):
		
		time.sleep(5)
		logger.debug("SecurityPage : open roles accordion.")
		self.roles_accordion.click()
		logger.debug("SecurityPage : Click on role name.")
		self.role4.click()
		logger.debug("SecurityPage : Click Delete.")
		self.delete_role_1.click()
		logger.debug("SecurityPage : Access alert.")
		self.browser.accept_alert()
		self.buy_time()

	def click_walled_garden_accordion(self):
		logger.debug("SecurityPage : Click on Walled Garden accordion.")
		self.buy_time()
		self.walled_garden.click()
		self.buy_time()
		
	def assert_walled_garden_page(self):
		if self.walled_garden_data:
			return True
		else:
			import traceback
			raise AssertionError("Walled Garden page did not load i.e . Traceback: %s" % traceback.format_exc())
				
	def click_walled_garden_link(self):
		logger.debug("SecurityPage : Click on Walled Garden Link.")
		self.buy_time()
		self.walled_garden_data.click()
		self.buy_time()
		
	def assert_walled_garden_link(self):
		if self.walled_garden_header:
			return True
		else:
			import traceback
			raise AssertionError("Walled Garden link did not load i.e . Traceback: %s" % traceback.format_exc())
			
	def create_blacklist_new_domain(self):
		logger.debug("SecurityPage :Creating new blacklist domain.")
		self.blacklist_new.click()
		self.buy_time()
		logger.debug("SecurityPage :Setting the invalid domain name. ")
		self.blacklist_textbox.set(self.config.config_vars.incorrect_domain_name)
		logger.debug('SecurityPage: Clicking save button')
		self.walled_new_save.click()
		if not self.domain_name_error_msg:
			raise AssertionError("Domain Name field accepting invalid values i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage :Setting the domain name. ")
		self.blacklist_textbox.set(self.config.config_vars.blacklist_domain_name)
		logger.debug('SecurityPage: Clicking ok button')
		self.walled_new_save.click()
		if self.walled_new_save:
			self.walled_new_save.click()
			
	def create_whitelist_new_domain(self):
		time.sleep(20)
		logger.debug("SecurityPage :Creating new whitelist domain.")
		self.whitelist_new.click()
		logger.debug("SecurityPage :Setting the invalid domain name. ")
		self.blacklist_textbox.set(self.config.config_vars.incorrect_domain_name)
		self.walled_new_save.click()
		if not self.domain_name_error_msg:
			raise AssertionError("Domain Name field accepting invalid values i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage :Setting the domain name. ")
		self.blacklist_textbox.set(self.config.config_vars.whitelist_domain_name)
		logger.debug('SecurityPage: Clicking Ok button')
		self.walled_new_save.click()	
		if self.walled_new_save:
			self.walled_new_save.click()
		logger.debug('SecurityPage: Clicking save button')
		self.walled_save.click()
		# self.walled_save.click()
		time.sleep(4)
		
	def assert_create_blacklist_new_domain(self):
		logger.debug("SecurityPage :Checking for Blacklist Domain name.")
		if self.blacklist_table_element:
			return True
		else:
			import traceback
			raise AssertionError(" Blacklist Domain name Not Present .i.e Traceback: %s " %traceback.format_exc())
			
	def assert_create_whitelist_new_domain(self):
		logger.debug("SecurityPage :Checking for Whitelist Domain name.")
		if self.whitelist_table_element:
			return True
		else:
			import traceback
			raise AssertionError(" Whitelist Domain name Not Present .i.e Traceback: %s " %traceback.format_exc())
			
	def delete_blacklist_domain(self):
		if self.blacklist_table_element:
			# self.blacklist_table_element.click()
			self.buy_time()
			logger.debug("SecurityPage :Deleting blacklist domain.")
			self.blacklist_delete_domain.click()
		logger.debug('SecurityPage: Clicking save button')
		self.walled_save.click()
		time.sleep(4)
			
	def delete_whitelist_domain(self):
		if self.whitelist_table_element:
			self.whitelist_table_element.click()
			self.buy_time()
			logger.debug("SecurityPage :Deleting whitelist domain.")
			self.blacklist_delete_domain.click()
		logger.debug('SecurityPage: Clicking save button')
		self.walled_save.click()
		time.sleep(4)
		
	def assert_delete_blacklist_domain(self):
		logger.debug("SecurityPage :Checking for Blacklist Domain name.")
		if not self.blacklist_table_element:
			return True
		else:
			import traceback
			raise AssertionError(" Blacklist Domain name Not Deleted .i.e Traceback: %s " %traceback.format_exc())
			
	def assert_delete_whitelist_domain(self):
		logger.debug("SecurityPage :Checking for Whitelist Domain name.")
		if not self.whitelist_table_element:
			return True
		else:
			import traceback
			raise AssertionError(" Whitelist Domain name Not Deleted .i.e Traceback: %s " %traceback.format_exc())
			
	def click_walled_cancel(self):
		logger.debug('SecurityPage: Clicking cancel button')
		self.walled_cancel.click()
			
	def edit_blacklist_domain(self):
		self.blacklist_table_element.click()
		self.buy_time()
		logger.debug("SecurityPage :Editing new blacklist domain.")
		self.blacklist_edit.click()
		logger.debug("SecurityPage :Setting the incorrect domain name. ")
		self.blacklist_textbox.set(self.config.config_vars.incorrect_domain_name)
		logger.debug('SecurityPage: Clicking Ok button')
		self.walled_new_save.click()
		if not self.domain_name_error_msg:
			raise AssertionError("Domain Name field accepting invalid values i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage :Setting the domain name. ")
		self.blacklist_textbox.set(self.config.config_vars.edited_blacklist_domain_name)
		time.sleep(4)
		logger.debug('SecurityPage: Clicking Ok button')
		self.walled_new_save.click()
		time.sleep(4)	
		if self.walled_new_save:
			self.walled_new_save.click()
	def edit_whitelist_domain(self):
		self.whitelist_table_element.click()
		self.buy_time()
		logger.debug("SecurityPage :Editing new whitelist domain.")
		self.whitelist_edit.click()
		logger.debug("SecurityPage :Setting the incorrect domain name. ")
		self.blacklist_textbox.set(self.config.config_vars.incorrect_domain_name)
		logger.debug('SecurityPage: Clicking Ok button')
		self.walled_new_save.click()
		if not self.domain_name_error_msg:
			raise AssertionError("Domain Name field accepting invalid values i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage :Setting the domain name. ")
		self.blacklist_textbox.set(self.config.config_vars.edited_whitelist_domain_name)
		logger.debug('SecurityPage: Clicking Ok button')
		self.walled_new_save.click()
		if self.walled_new_save:
			self.walled_new_save.click()
		logger.debug('SecurityPage: Clicking Save button')
		self.walled_save.click()
		
	def assert_edited_blacklist_domain(self):
		logger.debug("SecurityPage :Checking for edited Blacklist Domain name.")
		if self.edited_blacklist_table_element:
			return True
		else:
			import traceback
			raise AssertionError(" Blacklist Domain name Not edited .i.e Traceback: %s " %traceback.format_exc())
			
	def assert_edited_whitelist_domain(self):
		logger.debug("SecurityPage :Checking for  edited Whitelist Domain name.")
		if self.edited_whitelist_table_element:
			return True
		else:
			import traceback
			raise AssertionError(" Whitelist Domain name Not edited .i.e Traceback: %s " %traceback.format_exc())
			
	
	def delete_edited_blacklist_domain(self):
		if self.edited_blacklist_table_element:
			self.edited_blacklist_table_element.click()
			self.buy_time()
			logger.debug("SecurityPage :Deleting blacklist domain.")
			self.blacklist_delete_domain.click()
					
	def delete_edited_whitelist_domain(self):
		if self.edited_whitelist_table_element:
			self.edited_whitelist_table_element.click()
			self.buy_time()
			logger.debug("SecurityPage :Deleting whitelist domain.")
			self.whitelist_delete.click()
			self.walled_save.click()

	def go_to_blacklisting(self):
		logger.debug("SecurityPage : Clicking blacklisting accordion...")
		self.blacklisting_accordion.click()
		if not self.manual_blacklisting:
			self.blacklisting_accordion.click()
		
		time.sleep(5)
			
	def _assert_invalid_mac_address_msg(self):
		logger.debug("SecurityPage : Writing invalid mac address...")
		self.new_mac_address.set(self.config.config_vars.invalid_mac_address)
		logger.debug("SecurityPage : Clicking OK button...")		
		self.new_blacklist_ok.click()
		logger.debug("SecurityPage : Looking for invalid mac address error message...")
		if not self.invalid_mac_msg:
			import traceback
			raise AssertionError("Invalid Mac Address error message not found. Traceback: %s " %traceback.format_exc())
			
	def _save_settings(self):
		logger.debug("SecurityPage : Clicking 'Save Settings' button...")
		self.save_setting.click()
		
		time.sleep(20)
			
	def create_manual_blacklisting(self):
		logger.debug("SecurityPage : Clicking 'New' button...")
		self.new_blacklisting.click()
		self._assert_invalid_mac_address_msg()
		logger.debug("SecurityPage : Writing mac address...")
		self.new_mac_address.set(self.config.config_vars.valid_mac_address)
		import time
		time.sleep(30)
		logger.debug("SecurityPage : Clicking 'OK' button...")
		self.new_blacklist_ok.click()
		# self.new_blacklist_ok.click()
		import time
		time.sleep(20)
		self._save_settings()
		
	def delete_blacklisting_if_present(self):
		if self.blacklist_bar:
			# logger.debug("SecurityPage : Clicking blacklisting...")
			# self.blacklist_bar.click()
			logger.debug("SecurityPage : Clicking 'Delete' button...")
			self.blacklist_delete.click()
			time.sleep(20)
			logger.debug('SecurityPage: Clicking save setting button')
			self._save_settings()
			self.go_to_blacklisting()
			
	def delete_manual_blacklisting(self):
		# logger.debug("SecurityPage : Clicking blacklisting...")
		# self.blacklist_bar.click()
		logger.debug("SecurityPage : Clicking 'Delete' button...")
		self.blacklist_delete.click()
		time.sleep(20)
		logger.debug('SecurityPage: Clicking save setting button')
		self._save_settings()
		
	def assert_manual_blacklisting_present(self):
		if not self.blacklist_bar:
			import traceback
			raise AssertionError("Manual Blacklisting not present. Traceback: %s " %traceback.format_exc())
			
	def _assert_invalid_range_error_msg(self):
		logger.debug("SecurityPage : Writing out of range time...")
		self.dynamic_blacklist_time_value.set(self.config.config_vars.dynm_blklst_invalid_time)
		logger.debug("SecurityPage : Clicking on save settings...")			
		self._save_settings()
		logger.debug("SecurityPage : Looking for out of range error message...")		
		if not self.dynm_blacklist_range_error:
			import traceback
			raise AssertionError("Valid range error message not found. Traceback: %s " %traceback.format_exc())
			
	def create_dynamic_blacklisting(self, duration, unit):
		self._assert_invalid_range_error_msg()
		logger.debug("SecurityPage : Writing 'AUTH FAILURE BLACKLIST TIME' duration...")
		self.dynamic_blacklist_time_value.set(duration)
		logger.debug("SecurityPage : Writing 'AUTH FAILURE BLACKLIST TIME' unit...")
		self.dynamic_blacklist_time_unit.set(unit)
		logger.debug('SecurityPage: Clicking save setting button')
		self._save_settings()
		
	def set_dynamic_blacklisting_to_default(self):
		logger.debug("SecurityPage : Writing 'AUTH FAILURE BLACKLIST TIME' duration...")
		self.dynamic_blacklist_time_value.set(self.config.config_vars.dynm_blklst_default_time)
		logger.debug("SecurityPage : Writing 'AUTH FAILURE BLACKLIST TIME' unit...")
		self.dynamic_blacklist_time_unit.set(self.config.config_vars.dynm_blklst_time_unit1)
		logger.debug('SecurityPage: Clicking save setting button')
		self._save_settings()
		
	def assert_manual_blacklisting_not_present(self):
		if self.blacklist_bar:
			import traceback
			raise AssertionError("Manual Blacklisting present. Traceback: %s " %traceback.format_exc())
			
	def create_role_with_access_rules(self):
		
		import traceback
		time.sleep(5)
		logger.debug("SecurityPage : open roles accordion.")
		self.role_accordion.click()
		logger.debug('SecurityPage : Clicking on new role button')
		self.create_role.click()
		logger.debug('SecurityPage : Entering invalid values')
		self.role_input.set(self.config.config_vars.role_invalid_input)
		logger.debug('SecurityPage : Clicking on OK button')
		self.ok.click()
		time.sleep(3)
		if not self.new_role_invalid_msg:
			raise AssertionError("Invalid role name is not visible .Traceback: %s " %traceback.format_exc())			
		logger.debug('SecurityPage : Entering valid values')
		self.role_input.set(self.config.config_vars.role_valid_input)
		logger.debug('SecurityPage : Clicking on OK button')
		self.ok.click()
		# self.ok.click()
		time.sleep(3)
		logger.debug('SecurityPage : Clicking on Save Settings button')
		self.save_setting.click()
		time.sleep(5)
		logger.debug("SecurityPage : open roles accordion.")
		self.role_accordion.click()
		time.sleep(5)
		logger.debug('SecurityPage : Selecting newly created role')
		self.newly_created_role.click()
		time.sleep(2)
		logger.debug('SecurityPage : Clicking on add(+) button')
		self.access_rule_add_button.click()
		logger.debug('SecurityPage : Create AccessControl rule')
		self.service_dropdown.set(self.config.config_vars.service_value_adp)
		logger.debug('SecurityPage : Clicking on Save button')
		self.rule_save_button_1.click()
		logger.debug('SecurityPage : Clicking on add(+) button')
		self.access_rule_add_button.click()
		logger.debug('SecurityPage : Create VLAN rule')
		self.rule_type_dropdown_2.set(self.config.config_vars.rule_type_vlan)
		logger.debug('SecurityPage : Entering invalid vlan id')
		self.vlan_id_textbox.set(self.config.config_vars.invalid_vlan_id_value)
		logger.debug('SecurityPage : Clicking on Save button')
		self.rule_save_button_2.click()
		logger.debug('SecurityPage : Entering valid vlan id')
		self.vlan_id_textbox.set(self.config.config_vars.valid_vlan_id_value)
		logger.debug('SecurityPage : Clicking on Save button')
		self.rule_save_button_2.click()
		logger.debug('SecurityPage : Clicking on add(+) button')
		self.access_rule_add_button.click()
		logger.debug('SecurityPage : Create Captive Portal rule')
		self.rule_type_dropdown_2.set(self.config.config_vars.rule_type_captive)
		logger.debug('SecurityPage : Clicking on Save button')
		self.rule_save_button_2.click()
		logger.debug('SecurityPage : Clicking on add(+) button')
		self.access_rule_add_button.click()
		logger.debug('SecurityPage : Create CALEA rule')
		self.rule_type_dropdown_2.set(self.config.config_vars.rule_type_value_calea)
		logger.debug('SecurityPage : Clicking on Save button')
		self.rule_save_button_2.click()
		logger.debug('SecurityPage : Clicking on add(+) button')
		self.access_rule_add_button.click()
		logger.debug('SecurityPage : Create Bandwidth Contract rule')
		self.rule_type_dropdown_2.set(self.config.config_vars.rule_type_bw)
		logger.debug('SecurityPage : Entering invalid upstream, downstream')
		self.downstream_textbox.set(self.config.config_vars.invalid_downstream_value)
		self.upstream_textbox.set(self.config.config_vars.invalid_upstream_value)			
		logger.debug('SecurityPage : Clicking on Save button')
		self.rule_save_button_2.click()
		logger.debug('SecurityPage : Entering valid upstream, downstream')
		self.downstream_textbox.set(self.config.config_vars.valid_downstream)
		self.upstream_textbox.set(self.config.config_vars.valid_downstream)			
		logger.debug('SecurityPage : Clicking on Save button')
		self.rule_save_button_2.click()
		logger.debug('SecurityPage : Clicking on Save settings')
		self.save_setting.click()
		time.sleep(20)
		
		
	def click_on_up_down_arrow(self):
		
		logger.debug("SecurityPage : open roles accordion.")
		self.role_accordion.click()
		time.sleep(5)
		logger.debug('SecurityPage : Clicking on wired instant')
		self.wired_instant_role.click()
		time.sleep(5)
		logger.debug('SecurityPage : Clicking on new_role')
		self.newly_created_role.click()
		logger.debug('SecurityPage : Clicking on role')
		self.newly_created_role.click()
		time.sleep(30)
		logger.debug('SecurityPage : Clicking on DOWN button')
		self.down_arrow_button.click()
		logger.debug('SecurityPage : Clicking on Save settings')
		self.save_setting.click()
		time.sleep(5)
		
		logger.debug("SecurityPage : open roles accordion.")
		self.role_accordion.click()
		time.sleep(5)
		logger.debug('SecurityPage : Clicking on role')
		self.newly_created_role.click()
		time.sleep(5)
		logger.debug('SecurityPage : Clicking on UP button')
		self.up_arrow_button.click()
		logger.debug('SecurityPage : Clicking on Save settings')
		self.save_setting.click()
		
		
	def delete_newly_created_role(self):
		
		logger.debug("SecurityPage : open roles accordion.")
		self.role_accordion.click()
		time.sleep(5)
		if self.newly_created_role:
			logger.debug('SecurityPage : Clicking on role')
			self.newly_created_role.click()
			time.sleep(8)
			logger.debug('SecurityPage : Clicking on delete button')
			self.delete_role_1.click()
			self.browser.accept_alert()
			
	def create_role_if_not_present(self):
		
		import traceback
		if not self.newly_created_role:
			time.sleep(5)
			logger.debug("SecurityPage : open roles accordion.")
			self.role_accordion.click()
			logger.debug('SecurityPage : Clicking on new role button')
			self.create_role.click()
			logger.debug('SecurityPage : Entering invalid values')
			self.role_input.set(self.config.config_vars.role_valid_input)
			logger.debug('SecurityPage : Clicking on OK button')
			self.ok.click()
			logger.debug('SecurityPage : Clicking on Save settings')
			self.save_setting.click()

	def assert_firewall_default_options(self):
		if not self.sip_enable and  self.vocera_enable and self.alcatel_enable and self.cisco_enable and self.drop_arp_enable and self.malformed_dhcp_enable and self.arp_poison_enable:
			import traceback
			raise AssertionError("Default options not visible.Traceback: %s " %traceback.format_exc())
		
	def enable_all_protection_attacks_options(self):
		
		time.sleep(15)
		logger.debug("SecurityPage : Enable DROP BAD ARP .")		
		self.drop_arp_enable.click()	
		logger.debug("SecurityPage : Enable FIX MALFORMED DHCP .")		
		self.malformed_dhcp_enable.click()		
		logger.debug("SecurityPage : Enable ARP POISON CHECK.")		
		self.arp_poison_enable.click()		
		logger.debug('SecurityPage: Clicking save setting button')
		self.save_setting.click()
		self.buy_time()

	def restore_firewall_settings_defaults(self):
		self.click_firewall()
		
		time.sleep(15)
		logger.debug("SecurityPage : Disable DROP BAD ARP .")		
		self.drop_arp_disable.click()		
		logger.debug("SecurityPage : Disable FIX MALFORMED DHCP .")		
		self.malformed_dhcp_disable.click()		
		logger.debug("SecurityPage : Disable ARP POISON CHECK.")		
		self.arp_poison_disable.click()
		logger.debug("SecurityPage : Enable SIP.")		
		self.sip_enable.click()		
		logger.debug("SecurityPage : Enable VOCERA .")		
		self.vocera_enable.click()		
		logger.debug("SecurityPage : Enable ALCATEL NOE.")		
		self.alcatel_enable.click()	
		logger.debug("SecurityPage : Enable ALCATEL NOE.")		
		self.cisco_enable.click()				
		logger.debug('SecurityPage: Clicking save setting button')
		self.save_setting.click()
		self.buy_time()		
		
	def disable_application_layer_gateway(self):
		
		time.sleep(20)
		logger.debug("SecurityPage : Disable SIP.")		
		self.sip_disable.click()		
		logger.debug("SecurityPage : Disable VOCERA .")		
		self.vocera_disable.click()		
		logger.debug("SecurityPage : Disable ALCATEL NOE.")		
		self.alcatel_disable.click()	
		logger.debug("SecurityPage : Disable ALCATEL NOE.")		
		self.cisco_disable.click()
		time.sleep(20)
		logger.debug('SecurityPage: Clicking save setting button')
		self.save_setting.click()
		self.buy_time()
		
	def go_to_user_for_internal_server(self):
		logger.debug("SecurityPage : Click on Interval server.")			
		self.user_for_internal_server_button.click()
	
	def create_user_for_internal_server_guest(self):
		logger.debug("SecurityPage : Click on new.")	
		self.create_new_user.click()
		time.sleep(8)
		logger.debug("SecurityPage : Set username.")		
		self.user_name.set(self.config.config_vars.user_name)
		logger.debug("SecurityPage : Set password.")	
		self.pswd_txt.set(self.config.config_vars.internal_server_password)
		logger.debug("SecurityPage : Retype password.")	
		self.retype_pswd.set(self.config.config_vars.internal_server_password)
		logger.debug("SecurityPage : Set type as guest.")			
		self.user_type.set(self.config.config_vars.internal_server_type_guest)
		logger.debug("SecurityPage : Click on ok.")		
		self.create_user.click()
		time.sleep(15)
		
	def delete_internal_server(self):
		# logger.debug("SecurityPage : Click on server name.")
		# self.internal_server_name.click()
		self.browser.refresh()
		self.go_to_user_for_internal_server()
		if self.internal_server_delete_button :
			logger.debug("SecurityPage : Click delete button.")  
			self.internal_server_delete_button.click()
			logger.debug("SecurityPage : Accept alert.")   
			self.browser.accept_alert()
			
	def create_user_for_internal_server_employee(self):
		time.sleep(3)
		logger.debug("SecurityPage : Click on new.")	
		self.create_new_user.click()
		time.sleep(8)
		logger.debug("SecurityPage : Set username.")		
		self.user_name.set(self.config.config_vars.user_name)
		logger.debug("SecurityPage : Set password.")			
		self.pswd_txt.set(self.config.config_vars.internal_server_password)
		logger.debug("SecurityPage : Retype password.")			
		self.retype_pswd.set(self.config.config_vars.internal_server_password)
		logger.debug("SecurityPage : Set type as employee.")		
		self.user_type.set(self.config.config_vars.internal_server_type_employee)
		logger.debug("SecurityPage : Click on ok.")			
		self.create_user.click()
		time.sleep(15)
		
	def if_internal_server_guest_present(self):
		logger.debug("SecurityPage : Check if server present.")		
		if self.internal_server_delete_button:
			logger.debug("SecurityPage : Internal server present.")	
			return True
		else:
			logger.debug("SecurityPage : Internal server not present.")	
			return False
			
	def edit_user_for_internal_server_employee(self):
		# logger.debug("SecurityPage : Click on internal server name.")		
		# self.internal_server_name.click()
		self.browser.refresh()
		self.go_to_user_for_internal_server()
		logger.debug("SecurityPage : Click edit button.")			
		self.internal_server_edit_button.click()
		time.sleep(8)
		logger.debug("SecurityPage : Set new password.")			
		self.pswd_txt.set(self.config.config_vars.internal_server_edited_password)
		logger.debug("SecurityPage : Retype password.")
		self.retype_pswd.set(self.config.config_vars.internal_server_edited_password)
		if self.user_type.selected==self.config.config_vars.internal_server_type_guest:
			self.user_type.set(self.config.config_vars.internal_server_type_employee)
		else:
			self.user_type.set(self.config.config_vars.internal_server_type_guest)
		self.create_user.click()
		time.sleep(15)
		
	def assert_user_for_internal_server(self):
		logger.debug("SecurityPage : Click on new.")	
		self.create_new_user.click()
		time.sleep(8)
		logger.debug("SecurityPage : Write invalid user name")
		self.user_name.set(self.config.config_vars.invalid_internal_server_name)
		logger.debug("SecurityPage : Write password")
		self.pswd_txt.set(self.config.config_vars.internal_server_password)
		logger.debug("SecurityPage : Write retype password")
		self.retype_pswd.set(self.config.config_vars.internal_server_password)
		logger.debug("SecurityPage : Write user type")
		self.user_type.set(self.config.config_vars.internal_server_type_guest)
		logger.debug("SecurityPage : Click on save.")		
		self.create_user.click()
		if not self.assert_internal_server_name:
			import traceback
			raise AssertionError(" Message * No special characters allowed, only - and _ allowed not visible.Traceback: %s " %traceback.format_exc())
		
	def if_authentication_server_radius_present(self):
		logger.debug("SecurityPage : Check if auth server present.")
		if self.auth_server_name:
			logger.debug("SecurityPage : auth server present.")	
			return True
		else:
			logger.debug("SecurityPage : auth server not present.")	
			return False
		
	def create_authentication_server_radius(self):
		if not self.authentication_server_name:
			logger.debug("SecurityPage : Click new.")			
			self.create_auth_server.click()
		logger.debug("SecurityPage : Set auth server name.")			
		self.authentication_server_name.set(self.config.config_vars.auth_server_name_value)
		logger.debug("SecurityPage : Set ip address.")		
		self.auth_server_ip_address.set(self.config.config_vars.auth_server_ip)
		logger.debug("SecurityPage : Set shared key.")				
		self.auth_server_shared_key.set(self.config.config_vars.auth_server_shared_key_value)
		logger.debug("SecurityPage : Reset shared key.")
		self.auth_server_retype_shared_key.set(self.config.config_vars.auth_server_shared_key_value)
		logger.debug("SecurityPage : Set accounting port no.")		
		self.accounting_port.set(self.config.config_vars.accounting_port_valid)
		logger.debug("SecurityPage : Set auth port no.")		
		self.auth_port.set(self.config.config_vars.auth_port_valid)
		logger.debug("SecurityPage : Set time out.")		
		self.time_out.set(self.config.config_vars.time_out_valid)
		logger.debug("SecurityPage : Set dead time valid.")		
		self.dead_time.set(self.config.config_vars.dead_time_valid)
		logger.debug("SecurityPage : Set retry count.")			
		self.retry_count.set(self.config.config_vars.retry_count_valid)
		self.NAS_ip.set(self.config.config_vars.auth_nas_ip_addr_valid)
		logger.debug("SecurityPage :Click save.")		
		self.auth_server_save.click()
		time.sleep(15)
		
	def delete_authentication_server_radius(self):
		# logger.debug("SecurityPage : Click auth server name.")	
		# self.auth_server_name.click()
		logger.debug("SecurityPage : Click delete button.")			
		self.delete_auth_server.click()
		logger.debug("SecurityPage : Accept alert.")			
		self.browser.accept_alert()
		
		
	def assert_authentication_server_radius(self):
		logger.debug("SecurityPage : Click new.")	
		self.create_auth_server.click()
		logger.debug("SecurityPage : Click radius.")			
		self.radius_auth_server.click()
		logger.debug("SecurityPage : Set invalid auth server name.")
		self.authentication_server_name.set(self.config.config_vars.invalid_auth_server_name_value)
		logger.debug("SecurityPage : Set auth server invalid ip.")		
		self.auth_server_ip_address.set(self.config.config_vars.auth_server_ip_invalid)
		logger.debug("SecurityPage :Set invalid accounting port.")			
		self.accounting_port.set(self.config.config_vars.accounting_port_invalid)
		logger.debug("SecurityPage :Set invalid auth port.")		
		self.auth_port.set(self.config.config_vars.auth_port_invalid)
		logger.debug("SecurityPage :Set invalid timeout.")			
		self.time_out.set(self.config.config_vars.time_out_invalid)
		logger.debug("SecurityPage :Set invalid dead time.")
		self.dead_time.set(self.config.config_vars.dead_time_invalid)
		logger.debug("SecurityPage :Set invalid retry count.")
		self.retry_count.set(self.config.config_vars.retry_count_invalid)
		logger.debug("SecurityPage :Set invalid nas ip address.")
		self.NAS_ip.set(self.config.config_vars.auth_nas_ip_addr_invalid)
		logger.debug("SecurityPage : Set shared key with space.")				
		self.auth_server_shared_key.set(self.config.config_vars.auth_server_invalid_key_value)
		self.auth_server_save.click()
		if not self.auth_server_name_error:
			import traceback
			raise AssertionError("Special characters accepted in auth server name.Traceback: %s " %traceback.format_exc())
		if not self.assert_ip:
			import traceback
			raise AssertionError("Invalid IP Address.Traceback: %s " %traceback.format_exc())
		logger.debug("SecurityPage :Check RFC_3576 is enabeld by default")			
		if self.assert_RFC_3576.is_selected():
			import traceback
			raise AssertionError("RFC 3576 is Enabled.Traceback: %s " %traceback.format_exc())
		if not self.assert_accounting_port:
			import traceback
			raise AssertionError("Must be a number in range 1-65534.Traceback: %s " %traceback.format_exc())
		if not self.assert_auth_port:
			import traceback
			raise AssertionError("Must be a number in range 1-65534.Traceback: %s " %traceback.format_exc())
		if not self.assert_time_out:
			import traceback
			raise AssertionError("Must be a number in range 1-30.Traceback: %s " %traceback.format_exc())
		if not self.assert_dead_time:
			import traceback
			raise AssertionError("Must be a number in range 1-1440.Traceback: %s " %traceback.format_exc())
		if not self.assert_retry_count:
			import traceback
			raise AssertionError("Must be a number in range 1-5.Traceback: %s " %traceback.format_exc())
		if not self.assert_NAS_ipaddress:
			import traceback
			raise AssertionError("Invalid IP Address.Traceback: %s " %traceback.format_exc())
		if not self.auth_sharedkey_space_error:
			import traceback
			raise AssertionError("Error message 'No spaces allowed' not displayed.Traceback: %s " %traceback.format_exc())
		time.sleep(5)
		
	def clear_all_auth_server_fields(self):
		logger.debug('SecurityPage : Clearing all the field values ')
		self.authentication_server_name.set('')
		self.auth_server_ip_address.set('')
		self.accounting_port.set('')
		self.auth_port.set('')
		self.time_out.set('')
		self.dead_time.set('')
		self.retry_count.set('')
		self.NAS_ip.set('')
		self.auth_server_shared_key.set('')
		
	def create_coa_server(self):
		import traceback
		time.sleep(3)
		logger.debug('SecurityPage : Clicking on New button')
		self.create_auth_server.click()
		time.sleep(2)
		logger.debug('SecurityPage : Clicking on CoA_only')
		self.coa_only_checkbox.click()
		logger.debug('SecurityPage : Enter invalid values in the fields')
		logger.debug('SecurityPage : Setting invalid server name ')
		self.authentication_server_name.set(self.config.config_vars.coa_invalid_name)
		logger.debug('SecurityPage : Setting invalid ip')
		self.auth_server_ip_address.set(self.config.config_vars.coa_invalid_ip)
		logger.debug('SecurityPage : Setting invalid shared key ')
		self.auth_server_shared_key.set(self.config.config_vars.coa_invalid_shared_key)
		logger.debug('SecurityPage : Setting invalid retype shared key ')
		self.auth_server_retype_shared_key.set(self.config.config_vars.coa_invalid_retype_shared_key)
		logger.debug('SecurityPage : Clicking on Save Server button')
		self.auth_server_save.click()
		time.sleep(5)
		if not self.auth_server_name_error:
			raise AssertionError("COA invalid name message not visible .Traceback: %s " %traceback.format_exc())
		if not self.coa_invalid_ipaddr_msg:
			raise AssertionError("COA invalid ip message not visible .Traceback: %s " %traceback.format_exc())
		if not self.coa_invalid_sharedkey_msg:
			raise AssertionError("COA invalid shared key message not visible .Traceback: %s " %traceback.format_exc())
		if not self.coa_invalid_retype_shared_msg:
			raise AssertionError("COA invalid retyrp shared key message not visible .Traceback: %s " %traceback.format_exc())
		time.sleep(2)
		logger.debug('SecurityPage : Enter valid values in the fields')
		logger.debug('SecurityPage : Setting server name ')
		self.authentication_server_name.set(self.config.config_vars.coa_valid_name)
		logger.debug('SecurityPage : Setting ip')
		self.auth_server_ip_address.set(self.config.config_vars.coa_valid_ip)
		logger.debug('SecurityPage : Setting shared key ')
		self.auth_server_shared_key.set(self.config.config_vars.coa_valid_shared_key)
		logger.debug('SecurityPage : Setting retype shared key ')
		self.auth_server_retype_shared_key.set(self.config.config_vars.coa_valid_retype_shared_key)
		logger.debug('SecurityPage : Clicking on Save Server button')
		self.auth_server_save.click()			
		time.sleep(5)
		if not self.created_server_name_type:
			raise AssertionError("Created server redius type is not visible .Traceback: %s " %traceback.format_exc())
		time.sleep(2)
		
	def create_ldap_server(self):
		
		import traceback
		time.sleep(3)
		logger.debug('SecurityPage : Clicking on New button')
		self.create_auth_server.click()
		time.sleep(2)
		logger.debug('SecurityPage : Clicking on LDAP radio button')
		self.ldap_radio_button.click()
		logger.debug('SecurityPage : Enter invalid values in the fields')
		self.ldap_server_name.set(self.config.config_vars.ldap_invalid_name)
		self.ldap_ip_header.set(self.config.config_vars.ldap_invalid_ip)
		self.ldap_admin_password.set(self.config.config_vars.ldap_invalid_password)
		self.ldap_admin_repassword.set(self.config.config_vars.ldap_invalid_repassword)
		logger.debug('SecurityPage : Clicking on Save Server button')
		self.auth_server_save.click()
		time.sleep(5)
		if not self.ldap_name_error:
			raise AssertionError("LDAP invalid name message not visible .Traceback: %s " %traceback.format_exc())
		if not self.ldap_ip_error:
			raise AssertionError("LDAP invalid ip message not visible .Traceback: %s " %traceback.format_exc())
		if not self.ldap_admin_password_error:
			raise AssertionError("LADP invalid password message not visible .Traceback: %s " %traceback.format_exc())
		if not self.ldap_admin_repassword_error:
			raise AssertionError("LDAP invalid retyrp password message not visible .Traceback: %s " %traceback.format_exc())
		time.sleep(2)
		logger.debug('SecurityPage : Enter valid values in the fields')
		self.ldap_server_name.set(self.config.config_vars.ldap_valid_name)
		self.ldap_ip_header.set(self.config.config_vars.ldap_valid_ip)
		self.admin_dn.set(self.config.config_vars.dn_value)
		self.base_dn.set(self.config.config_vars.dn_value)
		self.ldap_admin_password.set(self.config.config_vars.ldap_valid_password)
		self.ldap_admin_repassword.set(self.config.config_vars.ldap_valid_repassword)
		logger.debug('SecurityPage : Clicking on Save Server button')
		self.auth_server_save.click()
		time.sleep(5)
			
	def delete_coa_server(self):
		logger.debug('SecurityPage : Delete created server')
		if self.created_server_name:
			self.created_server_name.click()
			self.delete_auth_server.click()
			self.browser.accept_alert()
			
	def delete_ldap_server(self):
		logger.debug('SecurityPage : Delete created server')
		if self.created_ldap_server_name:
			self.created_ldap_server_name.click()
			self.delete_auth_server.click()
			self.browser.accept_alert()

	def delete_external_server(self):
		logger.debug('SecurityPage : Delete external server')
		if self.created_external_server_name:
			logger.debug('SecurityPage : Clicking on external server')
			self.created_external_server_name.click()
			logger.debug('SecurityPage : Clicking on delete button')
			self.delete_auth_server.click()
			self.browser.accept_alert()
			
	def delete_2_external_servers(self):
		
		logger.debug('SecurityPage : Delete external servers')
		if self.created_external_server_name:
			logger.debug('SecurityPage : Clicking on external server 1')
			self.created_external_server_name.click()
			logger.debug('SecurityPage : Clicking on delete button')
			self.delete_auth_server.click()
			self.browser.accept_alert()
			
		if self.created_external_server_name_2:
			time.sleep(5)
			logger.debug('SecurityPage : Clicking on external server 2')
			self.created_external_server_name_2.click()		
			logger.debug('SecurityPage : Clicking on delete button')
			self.delete_auth_server.click()
			self.browser.accept_alert()
			
		logger.debug('SecurityPage : Returning to Network page')
		self.networks.click()
		time.sleep(5)
			
	def delete_authentication_server2(self):
		self.buy_time()
		if self.created_external_server_name_2:
			self.created_external_server_name_2.click()
			self.buy_time()
			logger.debug('SecurityPage : Clicking Delete button ')
			self.delete_auth_server.click()
			self.buy_time()
			self.browser.accept_alert()
			self.buy_time()
			
	def back_to_network_page(self):
		logger.debug('SecurityPage : Returning to Network page')
		self.networks.click()
		time.sleep(5)

	def delete_walled_garden_blacklist_whitelist(self):
		'''
		Deletes Blacklist and Whitelist
		'''
		logger.debug('SecurityPage : clicking on Walled Garden Accordion')
		self.walled_garden.click()
		logger.debug('SecurityPage : clicking on Walled Garden data')
		self.walled_garden_data.click()
		if self.edited_whitelist_table_element and self.edited_blacklist_table_element:
			logger.debug('SecurityPage : calling delete_edited_blacklist_domain')
			self.delete_edited_blacklist_domain()
			logger.debug('SecurityPage : calling delete_edited_whitelist_domain')
			self.delete_edited_whitelist_domain()
			logger.debug('SecurityPage : clicking on Save button')
			time.sleep(5)
			self.walled_save.click()
			time.sleep(5)
		logger.debug('SecurityPage: Clicking save button')
		if self.walled_save :
			self.walled_save.click()
			time.sleep(5)
	
	def click_on_external_captive_protal_button(self):
		'''
		clicks on external captive protal
		'''
		logger.debug('SecurityPage: Clicking external captive protal button')
		self.external_captive_protal_button.click()
		
		
		
	def create_new_captive_portal_1(self,name=None,type=None,ip=None,url=None,port=None,auth_text=None,http1=True,captive_portal=None,whitelisting=None,redirect_url_text=None):
		logger.debug('SecurityPage: Clicking new ')
		self.create_external_captive.click()
		time.sleep(5)
		if name:
			logger.debug('SecurityPage: Setting the captive portal Name')
			self.name_text_box.set(name)
		if type:
			logger.debug('SecurityPage: Selecting the captive portal Type')
			self.captive_portal_type.set(type)
		if ip:
			logger.debug('SecurityPage: Setting the captive portal IP or HostName')
			self.captive_portal_ip.set(ip)
		if url:
			logger.debug('SecurityPage: Setting the captive portal URL')
			self.captive_portal_url.set(url)
		if port:
			logger.debug('SecurityPage: Setting the captive portal Port')
			self.captive_portal_port.set(port)
		if http1:
			logger.debug('SecurityPage: Clicking the Use Https check box')
			self.security_use_https.click()
		if auth_text:
			logger.debug('SecurityPage: Setting the captive portal Auth Text')
			self.captive_portal_auth_text.set(auth_text)
		if captive_portal:
			logger.debug('SecurityPage: Setting the captive portal failure')
			self.captive_portal_failure.set(captive_portal)
		if whitelisting:
			logger.debug('SecurityPage: Enabling Automatic URL whitelisting')
			if not self.auto_url_whitelisting.is_selected():
				self.auto_url_whitelisting.click()
		else:
			logger.debug('SecurityPage: Disabling Automatic URL whitelisting')
			if self.auto_url_whitelisting.is_selected():
				self.auto_url_whitelisting.click()
		if redirect_url_text:
			logger.debug('SecurityPage: Setting the Redirect URL Text')
			self.redirect_url.set(redirect_url_text)
		time.sleep(6)
		logger.debug('SecurityPage: Clicking save button')
		self.captive_portal_save_button.click()
		time.sleep(6)
		
	def asserting_captive_portal(self):
		conf = self.config.config_vars
		logger.debug('SecurityPage: Clicking on External Captive Portal')
		self.edit_testradius1.click()
		logger.debug('SecurityPage: Asserting the IP field')
		self.browser.assert_text(self.captive_portal_ip, conf.auth_ipaddr, "ip not set properly", "value")
		logger.debug('SecurityPage: Asserting the URL field')
		self.browser.assert_text(self.captive_portal_url, conf.domain_name_value, "url is not set properly", "value")
		logger.debug('SecurityPage: Asserting the Port field')
		self.browser.assert_text(self.captive_portal_port, conf.captive_port_default, "port is not set properly", "value")
		logger.debug('SecurityPage: Clicking on Cancel button')
		self.cancel.click()
		
	def delete_external_captive_portal_2(self):
		if self.captive_role_1:
			time.sleep(3)
			logger.debug('SecurityPage: Clicking on Captive Role')
			self.captive_role_1.click()
			logger.debug('SecurityPage: Clicking delete button')
			self.delete_external_captive_1.click()
		if self.captive_role_2:
			time.sleep(3)
			logger.debug('SecurityPage: Clicking on Captive Role')
			self.captive_role_2.click()
			logger.debug('SecurityPage: Clicking delete button')
			self.delete_external_captive_5.click()
		if self.captive_role_3:
			time.sleep(3)
			logger.debug('SecurityPage: Clicking on Captive Role')
			self.captive_role_3.click()
			logger.debug('SecurityPage: Clicking delete button')
			self.delete_external_captive_3.click()
		if self.captive_role_4:
			time.sleep(3)
			logger.debug('SecurityPage: Clicking on Captive Role')
			self.captive_role_4.click()
			logger.debug('SecurityPage: Clicking delete button')
			self.delete_external_captive_4.click()
			logger.debug('SecurityPage: Clicking save settings button')
			self.save_setting.click()
			time.sleep(15)	
	
	def create_new_server(self):
		'''
		clicks on new button
		'''
		logger.debug('Security: Clicks on new button')
		self.create_auth_server.click()
	
	def create_authentication_server(self,name=None, ip=None, sharedkey=None,retypekey=None,rfc=False,actport=None,time=None,timeout=None,retrycount= None,authport = None,mask = None,dip = None,gateway = None,vlan = None,nas_ip=None,nas_identifier_value=None,coa_port=None):
		'''
		creates authentication server
		'''
		if name:
			logger.debug('SecurityPage: Writing server name')
			self.authentication_server_name.set(name)
		if ip: 
			logger.debug('SecurityPage: Writing ip')
			self.auth_server_ip_address.set(ip)
		if sharedkey:
			logger.debug('SecurityPage: Writing SharedKey')
			self.auth_server_shared_key.set(sharedkey)
		if retypekey: 
			logger.debug('SecurityPage: Writing Retype SharedKey')
			self.auth_server_retype_shared_key.set(retypekey)
		if rfc :
			logger.debug('SecurityPage: Selecting rfc checkbox')
			self.assert_RFC_3576.click()
		if actport:	
			logger.debug('SecurityPage: Writing actport')
			self.accounting_port.set(actport)
		if time:	
			logger.debug('SecurityPage: Writing deadtime')
			self.dead_time.set(time)
		if timeout:	
			logger.debug('SecurityPage: Writing timeout')
			self.time_out.set(timeout)
		if retrycount:	
			logger.debug('SecurityPage: Writing retry count')
			self.retry_count.set(retrycount)
		if authport:	
			logger.debug('SecurityPage: Writing authport')
			self.auth_port.set(authport)
		if dip:	
			logger.debug('SecurityPage: Writing drpip')
			self.drpip.set(dip)
		if mask:	
			logger.debug('SecurityPage: Writing drpmask')
			self.drpmask.set(mask)
		if gateway:	
			logger.debug('SecurityPage: Writing gateway')
			self.drpgateway.set(gateway)
		if vlan:	
			logger.debug('SecurityPage: Writing drpvlan')
			self.drpvlan.set(vlan)
		if nas_ip:
			logger.debug('SecurityPage : Setting NAS IP Address. ')
			self.NAS_ip.set(nas_ip)
		if nas_identifier_value:
			logger.debug('SecurityPage : Setting NAS Identifier. ')
			self.nas_identifier.set(nas_identifier_value)
	
	def click_edit_auth_server(self):
		'''
		clicks on Auth Server Edit button
		'''
		logger.debug('Security: Clicks on Edit button')
		self.edit_auth_server.click()
		self.buy_time()
	
	def save_auth_server(self):
		'''
		clicks on Auth Server save button
		'''
		logger.debug('Security: Clicks on Save button')
		self.auth_server_save.click()
		self.buy_time()
	
	def assert_auth_server(self):
		'''
		Checks auth server is disable or not
		'''
		logger.debug('Security: checking whether we can delete auth server which is used in network')
		self.browser.assert_element(self.disabled_auth_server, "auth server 'authradius' can be delete")
	
	def select_tacacs_radio(self):
		'''
		selects default tacacs radio button
		'''
		logger.debug("Services: Clicking on tacacs radio button")
		self.tacacs_radio.click()
		
	def set_new_server_tacacs_name(self,name):
		'''
		writes given name in name field
		'''
		logger.debug('Services: Writing server name')
		self.auth_server_tacacs_name.set(name)
		
	def set_new_server_tacacs_shared_key(self,key):
		'''
		writes given key in Shared key field
		'''
		logger.debug('Services: Writing shared key')
		self.Auth_Tacacs_Sharedkey.set(key)

	def set_new_server_tacacs_retype_shared_key(self,key):
		'''
		writes given key in Shared key field
		'''
		logger.debug('Services: Writing retype shared key')
		self.Retype_auth_tacacs_shared_key.set(key)
		
	def set_new_server_tacacs_ip(self,ip):
		'''
		writes given ip in IP Address field
		'''
		logger.debug('Services: Writing ip address')
		self.auth_tacacs_ipaddr.set(ip)
		
	def assert_radius_radio(self, enable):
		'''
		asserts radius radio button
		'''
		if enable == 'true':
			if not self.radius_auth_server.is_selected() :
				raise AssertionError('Radius Radio button is Disabled')
				
		else :
			if self.radius_auth_server.is_selected() :
				raise AssertionError('Radius Radio button is Enabled')
				
	def assert_ldpa_radio(self, enable):
		'''
		asserts ldpa radio button
		'''
		if enable == 'true':
			if not self.ldap_radio_button.is_selected() :
				raise AssertionError('Radius Radio button is Disabled')
				
		else :
			if self.ldap_radio_button.is_selected() :
				raise AssertionError('Radius Radio button is Enabled')
				
	def assert_tacacs_radio(self, enable):
		'''
		asserts tacacs radio button
		'''
		if enable == 'true':
			if not self.tacacs_radio.is_selected() :
				raise AssertionError('Radius Radio button is Disabled')
				
		else :
			if self.tacacs_radio.is_selected() :
				raise AssertionError('Radius Radio button is Enabled')
				
	def assert_coa_only_checkbox(self, enable):
		'''
		asserts coa only checkbox button
		'''
		if enable == 'true':
			if not self.coa_only_checkbox.is_selected() :
				raise AssertionError('Radius Radio button is Disabled')
				
		else :
			if self.coa_only_checkbox.is_selected() :
				raise AssertionError('Radius Radio button is Enabled')
		
	def assert_rfc_3576(self, enable):
		'''
		asserts rfc 3576 checkbox
		'''
		if enable == 'true':
			if not self.assert_RFC_3576.is_selected() :
				raise AssertionError('Radius Radio button is Disabled')
				
		else :
			if self.assert_RFC_3576.is_selected() :
				raise AssertionError('Radius Radio button is Enabled')
				
	def assert_auth_server_name(self):
		logger.debug("ServicesPage : Check whether the Auth Server Name  textbox is empty. ")
		if self.authentication_server_name:
			if not self.authentication_server_name.get() == '' :
				raise AssertionError("Auth Server Name textbox is not empty.Traceback: %s " %traceback.format_exc())
				
	def assert_auth_ipaddr(self):
		logger.debug("ServicesPage : Check whether the Auth IP Address textbox is empty. ")
		if self.auth_server_ip_address:
			if not self.auth_server_ip_address.get() == '' :
				raise AssertionError("Auth IP Address textbox is not empty.Traceback: %s " %traceback.format_exc())
				
	def assert_auth_sharedkey(self):
		logger.debug("ServicesPage : Check whether the Auth Shared Key textbox is empty. ")
		if self.auth_server_shared_key:
			if not self.auth_server_shared_key.get() == '' :
				raise AssertionError("Shared Key textbox is not empty.Traceback: %s " %traceback.format_exc())
				
	def assert_retype_auth_shared_key(self):
		logger.debug("ServicesPage : Check whether the Auth Retype-Shared Key textbox is empty. ")
		if self.auth_server_retype_shared_key:
			if not self.auth_server_retype_shared_key.get() == '' :
				raise AssertionError("Retype-Shared Key textbox is not empty.Traceback: %s " %traceback.format_exc())
				
	def assert_dead_time(self):
		logger.debug("ServicesPage : Check whether the Dead Time textbox is set to 5. ")
		if self.dead_time:
			if not self.dead_time.get() == self.config.config_vars.dead_time_default :
				raise AssertionError(" Dead Time textbox is not set to 5 .Traceback: %s " %traceback.format_exc())
				
	def assert_timeout(self):
		logger.debug("ServicesPage : Check whether the Timeout textbox is set to 5. ")
		if self.time_out:
			if not self.time_out.get() == self.config.config_vars.dead_time_default :
				raise AssertionError(" Timeout textbox is not set to 5 .Traceback: %s " %traceback.format_exc())
				
				
	def assert_retry_count(self):
		logger.debug("ServicesPage : Check whether the retry count textbox is set to 3")
		if self.retry_count:
			if not self.retry_count.get() == self.config.config_vars.retry_count_default :
				raise AssertionError(" Retry Count textbox is not set to 3 .Traceback: %s " %traceback.format_exc())
				
	def assert_auth_port(self):
		logger.debug("ServicesPage : Check whether the Auth Account Port textbox is set to 1812. ")
		if self.auth_port:
			if not self.auth_port.get() == self.config.config_vars.auth_port_default :
				raise AssertionError(" Auth Account Port textbox is not set to 1812 .Traceback: %s " %traceback.format_exc())
				
	
	
	def assert_optional_feilds(self):
		if not self.NAS_ip.get_attribute_value('placeholder') == self.config.config_vars.optional :
			raise AssertionError('Textbox is not set to optional')
		
		if not self.nas_identifier.get_attribute_value('placeholder') == self.config.config_vars.optional :
			raise AssertionError('Textbox is not set to optional')
	
	def assert_security_page(self):
		logger.debug("SecurityPage: Asserting Security Page")
		self.browser.assert_element(self.configuration_security, "Security Page is not loaded")
		
	def assert_walled_garden_ui(self):
		logger.debug("SecurityPage : clicking on new button to create a new blacklist. ")
		self.blacklist_new.click()
		logger.debug("SecurityPage : Asserting Blacklist new window ")
		self.browser.assert_element(self.black_list_window, "Blacklist window in not displayed")
		logger.debug("SecurityPage : Clicking on cancel button ")
		self.walled_new_cancel.click()
		logger.debug("SecurityPage : Clicking on cancel button ")
		self.walled_cancel.click()		

	def create_blacklist_new_domain_with_single_qoutes(self):
		logger.debug("SecurityPage :Creating new blacklist domain.")
		self.blacklist_new.click()
		self.buy_time()
		logger.debug("SecurityPage :Setting the invalid domain name. ")
		self.blacklist_textbox.set(self.config.config_vars.single_quote_domain_name)
		logger.debug('SecurityPage: Clicking save button')
		self.walled_new_save.click()
		if self.domain_name_error_msg:
			raise AssertionError("Domain Name field accepting invalid values i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage :Setting the domain name. ")
		self.blacklist_textbox.set(self.config.config_vars.single_quote_domain_name)
		logger.debug('SecurityPage: Clicking ok button')
		self.walled_new_save.click()
		if self.walled_new_save:
			self.walled_new_save.click()
			
	def validate_auth_server_1(self):
		'''
		Validate Authentication Server1 fields.
		'''
		conf = self.config.config_vars
		logger.debug('SecurityPage : Clicking on New button')
		self.create_auth_server.click()
		time.sleep(2)
		self.validate_auth_server_default_values()
		self.set_auth_server_name(conf.invalid_radius_server_name)
		self.set_auth_server_ip_address(conf.invalid_radius_server_ip)
		self.set_auth_shared_key_retype(conf.invalid_radius_server_shared_key,conf.invalid_radius_server_shared_key)
		self.set_auth_server_accounting_port(conf.invalid_radius_server_acc_port_0)
		self.set_auth_server_time_out(conf.invalid_radius_server_time_out_31)
		self.set_auth_server_retry_count(conf.invalid_radius_server_retry_count_0)
		self.set_auth_server_auth_port(conf.invalid_radius_server_auth_port_0)
		self.save_auth_server()
		self.assert_auth_server_name_error()
		self.assert_auth_server_ip_address_error()
		self.assert_auth_server_shared_key_error()
		self.assert_auth_server_accounting_port_error()
		self.assert_auth_server_time_out_error()
		self.assert_auth_server_retry_count_error()
		self.assert_auth_server_auth_port_error()
		self.set_auth_shared_key_retype(conf.invalid_input,conf.invalid_input)
		self.set_auth_server_accounting_port(conf.invalid_radius_server_acc_port_65535)
		self.set_auth_server_time_out(conf.invalid_radius_server_time_out_0)
		self.set_auth_server_retry_count(conf.invalid_radius_server_retry_count_6)
		self.set_auth_server_auth_port(conf.invalid_radius_server_auth_port_65535)
		self.save_auth_server()
		self.assert_auth_server_shared_key_error(False)
		self.assert_auth_server_accounting_port_error()
		self.assert_auth_server_time_out_error()
		self.assert_auth_server_retry_count_error()
		self.assert_auth_server_auth_port_error()
		self.auth_server_cancel.click()
		self.buy_time()

	def validate_auth_server_default_values(self):
		self.assert_auth_account_port()
		self.assert_dead_time()
		self.assert_auth_port()
		self.assert_auth_rfc_default()
		self.assert_timeout()
		self.assert_retry_count_default_value()
		
	def set_auth_server_name(self,value=''):
		'''
		Sets auth server name.
		'''
		logger.debug("SecurityPage : Write Server name")
		self.authentication_server_name.set(value)

	def set_auth_server_ip_address(self,value=''):
		'''
		Sets auth server IP address.
		'''
		logger.debug("SecurityPage : Writing Server ip address")
		self.auth_server_ip_address.set(value)
		
	def set_auth_shared_key_retype(self,shared_key='',retype=''):
		'''
		Sets auth server Auth shared key and retype value.
		'''
		logger.debug('SecurityPage : Writing auth Sharedkey value')
		self.auth_server_shared_key.set(shared_key)
		logger.debug("SecurityPage : Write retype - Shared key.")
		self.auth_server_retype_shared_key.set(retype)

	def set_auth_server_accounting_port(self,value='1813'):
		'''
		Sets auth server accounting count.
		'''
		logger.debug("SecurityPage : Write  Accounting Port value.")
		self.accounting_port.set(value)

	def set_auth_server_dead_time(self,value='5'):
		'''
		Sets auth server Dead Time.
		'''
		logger.debug("SecurityPage : Write  Dead Time value.")
		self.dead_time.set(value)
		
	def set_auth_server_time_out(self,value='5'):
		'''
		Sets authentication server time out.
		'''
		logger.debug("SecurityPage : Write  Time out value.")
		self.time_out.set(value)
		
	def set_auth_server_retry_count(self,value='3'):
		'''
		Sets authentication server Retry count.
		'''
		logger.debug("SecurityPage : Write  Retry count value.")
		self.retry_count.set(value)
		
	def set_auth_server_auth_port(self,value='1812'):
		'''
		Sets authentication server auth port.
		'''
		logger.debug("SecurityPage : Write  Auth Port value.")
		self.auth_port.set(value)

	def assert_auth_server_name_error(self):
		'''
		Asserts authentication server name error message.
		'''
		logger.debug("SecurityPage : Checking for Auth server name error.")
		if not self.auth_server_name_error:
			raise AssertionError("SecurityPage : Server name error. i.e. Traceback: %s" %traceback.format_exc())

	def assert_auth_server_ip_address_error(self):
		'''
		Asserts authentication server IP address error message.
		'''
		logger.debug("SecurityPage : Checking for Auth server IP address error.")
		if not self.coa_invalid_ipaddr_msg:
			raise AssertionError("SecurityPage : Invalid IP. i.e. Traceback: %s" %traceback.format_exc())

	def assert_auth_server_shared_key_error(self,value=True):
		'''
		Asserts authentication server shared key length error message.
		'''
		if value:
			logger.debug("SecurityPage : Checking for Auth server shared key space error.")
			if not self.auth_sharedkey_space_error:
				raise AssertionError("SecurityPage : Auth server shared key space error message not found. i.e. Traceback: %s" %traceback.format_exc())
		else:
			logger.debug("SecurityPage : Checking for Auth server shared key length error.")
			if not self.coa_invalid_sharedkey_msg:
				raise AssertionError("SecurityPage : Auth server shared key length error message not found. i.e. Traceback: %s" %traceback.format_exc())

	def assert_auth_server_accounting_port_error(self):
		'''
		Asserts authentication server Accounting port error message.
		'''
		logger.debug("SecurityPage : Checking for Auth server Accounting port error.")
		if not self.assert_accounting_port:
			raise AssertionError("SecurityPage : Auth server Accounting port error message not found. i.e. Traceback: %s" %traceback.format_exc())

	def assert_auth_server_deadtime_error(self):
		'''
		Asserts authentication server Deadtime error message.
		'''
		logger.debug("SecurityPage : Checking for Auth server Dead Time error.")
		if not self.assert_dead_time:
			raise AssertionError("SecurityPage : 'Must be a number in range 1-1440' error msg not present. i.e. Traceback: %s" %traceback.format_exc())

	def assert_auth_server_time_out_error(self):
		'''
		Asserts authentication server Time out error message.
		'''
		logger.debug("SecurityPage : Checking for Auth server Timeout error.")
		if not self.assert_time_out:
			raise AssertionError("SecurityPage : 'Must be a number in range 1-30' error msg not present. i.e. Traceback: %s" %traceback.format_exc())

	def assert_auth_server_retry_count_error(self):
		'''
		Asserts authentication server Retry count error message.
		'''
		logger.debug("SecurityPage : Checking for Auth server Retry count error.")
		if not self.assert_retry_count:
			raise AssertionError("SecurityPage : 'Must be a number in range 1-5' error msg not present. i.e. Traceback: %s" %traceback.format_exc())

	def assert_auth_server_auth_port_error(self):
		'''
		Asserts authentication server Auth port error message.
		'''
		logger.debug("SecurityPage : Checking for Auth server Auth port error.")
		if not self.assert_auth_port:
			raise AssertionError("SecurityPage : 'Must be a number in range 1-65534' error msg not present. i.e. Traceback: %s" %traceback.format_exc())
			
	def assert_retry_count_default_value(self):
		'''
		asserts default value of retry count
		'''
		conf = self.config.config_vars
		logger.debug('SecurityPage : Auth Server : Checking retry count default value')
		self.browser.assert_text(self.retry_count,conf.new_reauth_value,'Retry Count is not set to 3','value')

	def assert_auth_rfc_default(self):
		'''
		Asserts auth rfc checkbox
		'''
		logger.debug('SecurityPage : Auth server : checking is rfc checkbox selected')
		self.browser.assert_check_box_value(self.assert_RFC_3576,'Auth rfc is selected by default',check = True)

	def assert_drp_mask_error(self):
		'''
		Asserts authentication server drpmask_error message.
		'''
		logger.debug("SecurityPage : Checking for drpmask_error.")
		if not self.drpmask_error:
			raise AssertionError("SecurityPage : 'Invalid Net Mask' error msg not present. i.e. Traceback: %s" %traceback.format_exc())

	def assert_drp_vlan_error(self):
		'''
		Asserts authentication server drpVlan_error message.
		'''
		logger.debug("SecurityPage : Checking for drpvlan_error.")
		if not self.drpvlan_error:
			raise AssertionError("SecurityPage : 'Must be a number in range 1-4093' error msg not present. i.e. Traceback: %s" %traceback.format_exc())				
			
	def assert_auth_port(self):
		if not self.auth_port.get() == self.config.config_vars.default_AuthPort:
			raise AssertionError("the default value of auth port is not set to 1812 . i.e. Traceback: %s" %traceback.format_exc())
			
	def assert_auth_account_port(self):
		if not self.accounting_port.get() == self.config.config_vars.default_Auth_Account_Port:
			raise AssertionError("the default value of auth account port is not set to 1813 . i.e. Traceback: %s" %traceback.format_exc())
		
	def assert_dead_time(self):
		if not self.dead_time.get() == self.config.config_vars.default_dead_time:
			raise AssertionError("the default value of dead time is not set to 5 . i.e. Traceback: %s" %traceback.format_exc())
			
	def assert_timeout(self):
		if not self.time_out.get() == self.config.config_vars.default_time_out:
			raise AssertionError("time out value is not set to 5.i.e . Traceback: %s" % traceback.format_exc())
			
	def set_coa_only_checkbox(self,flag=False):
		'''
		Check or Uncheck 'COA only' check box.
		'''
		if flag:
			if not self.coa_only_checkbox.is_selected():
				logger.debug("SecurityPage : Checking 'CoA_only' checkbox")
				self.coa_only_checkbox.click()
				time.sleep(3)
		else:
			if self.coa_only_checkbox.is_selected():
				logger.debug("SecurityPage : Unchecking 'CoA_only' checkbox")
				self.coa_only_checkbox.click()
				time.sleep(3)
				
	def create_coa_server1(self,coa_name=None,coa_ip=None,coa_shared_key=None,coa_retype_key=None,coa_port=None):
		'''
		Creates new coa server.
		'''
		logger.debug('SecurityPage : Setting server name ')
		self.authentication_server_name.set(coa_name)
		logger.debug('SecurityPage : Setting ip')
		self.auth_server_ip_address.set(coa_ip)
		logger.debug('SecurityPage : Setting shared key ')
		self.auth_server_shared_key.set(coa_shared_key)
		logger.debug('SecurityPage : Setting retype shared key ')
		self.auth_server_retype_shared_key.set(coa_retype_key)
		logger.debug('SecurityPage : Setting AirGroup CoA Port ')
		self.air_group_coa_port_1.set(coa_port)
		logger.debug('SecurityPage : Clicking on Save Server button')
		self.auth_server_save.click()
		
	def set_air_group_coa_port(self,port):
		'''
		writes given Port in Port field
		'''
		logger.debug('Security: Writing Port Value')
		self.air_group_coa_port_1.set(port)
	
	def delete_coa_servers(self):
		logger.debug('SecurityPage : Delete created server')
		if self.coa_server:
			logger.debug('SecurityPage : Clicking on created coaServer')
			self.coa_server.click()
			logger.debug('SecurityPage :Calling delete_authentication_server_radius method ')
			self.delete_authentication_server_radius()
		if self.coa_server1:
			logger.debug('SecurityPage : Clicking on created coaServer')
			self.coa_server1.click()
			logger.debug('SecurityPage :Calling delete_authentication_server_radius method ')
			self.delete_authentication_server_radius()
			
	def create_coa_servers(self,name=False,ip=False,sharedkey=False,port=False):
		'''
		creates Coa Servers
		'''
		logger.debug('SecurityPage : Clicking on New button')
		self.create_auth_server.click()
		logger.debug('SecurityPage : Clicking on CoA_only')
		self.coa_only_checkbox.click()
		if name:
			logger.debug('SecurityPage :Calling set_auth_server_name method ')
			self.set_auth_server_name(name)
		if ip:
			logger.debug('SecurityPage :Calling set_auth_server_ip_address method ')
			self.set_auth_server_ip_address(ip)
		if sharedkey:
			logger.debug('SecurityPage :Calling set_auth_shared_key_retype method ')
			self.set_auth_shared_key_retype(sharedkey, sharedkey)
		if port:
			logger.debug('SecurityPage :Calling set_air_group_coa_port method ')
			self.set_air_group_coa_port(port)
		logger.debug('SecurityPage :Calling save_auth_server method ')
		self.save_auth_server()
			
	def delete_ldap_servers(self):
		logger.debug('SecurityPage : Delete created server')
		if self.ldap_server:
			logger.debug('SecurityPage : Clicking on created LDAPServer')
			self.ldap_server.click()
			logger.debug('SecurityPage :Calling delete_authentication_server_radius method ')
			self.delete_authentication_server_radius()
		if self.ldap_server1:
			logger.debug('SecurityPage : Clicking on created LDAPServer')
			self.ldap_server1.click()
			logger.debug('SecurityPage :Calling delete_authentication_server_radius method ')
			self.delete_authentication_server_radius()
			
		
		
	def create_new_ldap_auth_server(self,name = None,ip = None,port = None,admin = None,passphrase = None,retypepass = None,base = None,filter = None,key = None,timeout = None,retry = None):
		'''
		creates ldap server
		'''
		if name:
			logger.debug('SecurityPage : Writing server name')
			self.ldap_server_name.set(name)
		if ip: 
			logger.debug('SecurityPage : Writing ip address')
			self.ldap_ip_header.set(ip)
		if port: 
			logger.debug('SecurityPage : Writing port')
			self.ldap_port.set(port)
		if admin: 
			logger.debug('SecurityPage : Writing admin name')
			self.admin_dn.set(admin)
		if passphrase: 
			logger.debug('SecurityPage : Writing passphrase')
			self.ldap_admin_password.set(self.config.config_vars.ldap_valid_password)
			logger.debug('SecurityPage : Writing retype passphrase')
			self.ldap_admin_repassword.set(retypepass)
		if base:
			logger.debug('SecurityPage : Writing base name')
			self.base_dn.set(base)
		if filter:
			logger.debug('SecurityPage : Writing filter name')
			self.ldap_filter.set(filter)
		if key:
			logger.debug('SecurityPage : Writing key attribute')
			self.LDAP_KeyAttribute.set(key)
		if timeout:
			logger.debug('SecurityPage : Writing timeout')
			self.ldap_timeout.set(timeout)
		if retry:
			logger.debug('SecurityPage : Writing retry count')
			self.LDAP_RetryCount.set(retry)

		logger.debug('SecurityPage : Clicking on Save Server button')
		self.auth_server_save.click()
	
	def set_nas_ip_address(self,value=None):
		'''
		Sets 'NAS IP ADDRESS' field.
		'''
		if value:
			logger.debug('SecurityPage : Setting NAS IP Address. ')
			self.NAS_ip.set(value)
			self.buy_time()
			
			
	def assert_ldpa_name(self):
		logger.debug("ServicesPage : Check whether the LDPA Name  textbox is empty. ")
		if self.ldap_server_name:
			if not self.ldap_server_name.get() == '' :
				raise AssertionError("LDPA Name textbox is not empty.Traceback: %s " %traceback.format_exc())
				
	def assert_ldpa_ipaddr(self):
		logger.debug("ServicesPage : Check whether the LDPA IP Address textbox is empty. ")
		if self.ldap_ip_header:
			if not self.ldap_ip_header.get() == '' :
				raise AssertionError("LDPA IP Address textbox is not empty.Traceback: %s " %traceback.format_exc())
				
	def assert_ldpa_admin_pass(self):
		logger.debug("ServicesPage : Check whether the LDPA Shared Key textbox is empty. ")
		if self.ldap_admin_password:
			if not self.ldap_admin_password.get() == '' :
				raise AssertionError("Shared Key textbox is not empty.Traceback: %s " %traceback.format_exc())
				
	def assert_ldpa_admin_retype_pass(self):
		logger.debug("ServicesPage : Check whether the LDPA Retype-Shared Key textbox is empty. ")
		if self.ldap_admin_repassword:
			if not self.ldap_admin_repassword.get() == '' :
				raise AssertionError("Retype-Shared Key textbox is not empty.Traceback: %s " %traceback.format_exc())
				
	def assert_admin_dn(self):
		logger.debug("ServicesPage : Check whether the LDPA Shared Key textbox is empty. ")
		if self.admin_dn:
			if not self.admin_dn.get() == '' :
				raise AssertionError("Shared Key textbox is not empty.Traceback: %s " %traceback.format_exc())
				
	def assert_base_dn(self):
		logger.debug("ServicesPage : Check whether the LDPA Retype-Shared Key textbox is empty. ")
		if self.base_dn:
			if not self.base_dn.get() == '' :
				raise AssertionError("Retype-Shared Key textbox is not empty.Traceback: %s " %traceback.format_exc())
				
	def assert_ldap_Port(self):
		logger.debug("ServicesPage : Check whether the LDPA Autht Port textbox is set to 389. ")
		if self.ldap_port:
			if not self.ldap_port.get() == self.config.config_vars.ldpa_auth_port_default :
				raise AssertionError(" LDPA Auth Port textbox is not set to 389 .Traceback: %s " %traceback.format_exc())
				
	def assert_ldpa_Filter(self):
		logger.debug("ServicesPage : Check whether the ldpa Filter textbox is set to sAMAccountName. ")
		if self.ldap_filter:
			if not self.ldap_filter.get() == self.config.config_vars.LDAP_Filter :
				raise AssertionError(" Dead Time textbox is not set to sAMAccountName .Traceback: %s " %traceback.format_exc())
				
	def assert_ldpa_KeyAttribute(self):
		logger.debug("ServicesPage : Check whether the ldpa KeyAttribute textbox is set to sAMAccountName. ")
		if self.LDAP_KeyAttribute:
			if not self.LDAP_KeyAttribute.get() == self.config.config_vars.LDAP_KeyAttribute :
				raise AssertionError(" Timeout textbox is not set to sAMAccountName .Traceback: %s " %traceback.format_exc())
				
	def assert_ldpa_timeout(self):
		logger.debug("ServicesPage : Check whether the Timeout textbox is set to 5. ")
		if self.ldap_timeout:
			if not self.ldap_timeout.get() == self.config.config_vars.dead_time_default :
				raise AssertionError(" Timeout textbox is not set to 5 .Traceback: %s " %traceback.format_exc())
						
	def assert_ldpa_retry_count(self):
		logger.debug("ServicesPage : Check whether the retry count textbox is set to 3")
		if self.LDAP_RetryCount:
			if not self.LDAP_RetryCount.get() == self.config.config_vars.retry_count_default :
				raise AssertionError(" Retry Count textbox is not set to 3 .Traceback: %s " %traceback.format_exc())
				
	def drp_disabled_fields(self):
		if not self.drpip_disabled:
			raise AssertionError("Drp ip field not disabled and it Editable i.e. Traceback: %s" %traceback.format_exc())
			
		if not self.drpmask_disabled:
			raise AssertionError("Drp mask field not disabled and it Editable i.e. Traceback: %s" %traceback.format_exc())
			
		if not self.drpgateway_disabled:
			raise AssertionError("Drp gateway field not disabled and it Editable i.e. Traceback: %s" %traceback.format_exc())
			
		if not self.drpvlan_disabled:
			raise AssertionError("Drp vlan field not disabled and it Editable i.e. Traceback: %s" %traceback.format_exc())
			
	def assert_auth_server_tacacs_name(self):
		logger.debug("ServicesPage : Check whether the Tacacs Name  textbox is empty. ")
		if self.auth_server_tacacs_name:
			if not self.auth_server_tacacs_name.get() == '' :
				raise AssertionError("Tacacs Server Name textbox is not empty.Traceback: %s " %traceback.format_exc())
				
	def assert_auth_tacacs_ipaddr(self):
		logger.debug("ServicesPage : Check whether the Tacacs IP Address textbox is empty. ")
		if self.auth_tacacs_ipaddr:
			if not self.auth_tacacs_ipaddr.get() == '' :
				raise AssertionError("Tacacs IP Address textbox is not empty.Traceback: %s " %traceback.format_exc())
				
	def assert_auth_tacacs_sharedkey(self):
		logger.debug("ServicesPage : Check whether the Tacacs Shared Key textbox is empty. ")
		if self.Auth_Tacacs_Sharedkey:
			if not self.Auth_Tacacs_Sharedkey.get() == '' :
				raise AssertionError("Shared Key textbox is not empty.Traceback: %s " %traceback.format_exc())
				
	def assert_retype_auth_tacacs_shared_key(self):
		logger.debug("ServicesPage : Check whether the Tacacs Retype-Shared Key textbox is empty. ")
		if self.Retype_auth_tacacs_shared_key:
			if not self.Retype_auth_tacacs_shared_key.get() == '' :
				raise AssertionError("Retype-Shared Key textbox is not empty.Traceback: %s " %traceback.format_exc())
				
				
	def assert_Auth_Tacacs_Port(self):
		logger.debug("ServicesPage : Check whether the Tacacs Port textbox is set to 49. ")
		if self.Auth_Tacacs_Port:
			if not self.Auth_Tacacs_Port.get() == self.config.config_vars.Auth_Tacacs_Port_default :
				raise AssertionError(" Tacacs Port textbox is not set to 49 .Traceback: %s " %traceback.format_exc())
				
	def assert_auth_tacacs_timeout(self):
		logger.debug("ServicesPage : Check whether the Tacacs Timeout textbox is set to 5. ")
		if self.auth_tacacs_timeout:
			if not self.auth_tacacs_timeout.get() == self.config.config_vars.dead_time_default :
				raise AssertionError(" Timeout textbox is not set to 5 .Traceback: %s " %traceback.format_exc())
				
				
	def assert_auth_tacacs_retry_count(self):
		logger.debug("ServicesPage : Check whether the Tacacs retry count textbox is set to 3")
		if self.auth_tacacs_retry_count:
			if not self.auth_tacacs_retry_count.get() == self.config.config_vars.retry_count_default :
				raise AssertionError(" Retry Count textbox is not set to 3 .Traceback: %s " %traceback.format_exc())
				
	def assert_airGroup_port(self):
		logger.debug("ServicesPage : Check whether the AirGroup Port textbox is set to 5999. ")
		if self.air_group_coa_port_1:
			if not self.air_group_coa_port_1.get() == self.config.config_vars.coa_port :
				raise AssertionError(" AirGroup Port textbox is not set to 5999 .Traceback: %s " %traceback.format_exc())
				
	def create_new_tacacs_auth_server(self,name = None, key = None, retype = None, port = None, timeout = None, ip = None, retry = None):
		'''
		creates tacacs auth server
		'''
		if name:
			logger.debug('Services: Writing server name')
			self.auth_server_tacacs_name.set(name)
		if key:	
			logger.debug('Services: Writing shared key')
			self.Auth_Tacacs_Sharedkey.set(key)
		if retype:	
			logger.debug('Services: Writing retype shared key')
			self.Retype_auth_tacacs_shared_key.set(retype)
		if port:	
			logger.debug('Services: Writing ip address')
			self.auth_tacacs_ipaddr.set(port)
		if timeout:	
			logger.debug('Services: Writing ip address')
			self.Auth_Tacacs_Port.set(timeout)
		if ip:	
			logger.debug('Services: Writing ip address')
			self.auth_tacacs_timeout.set(ip)
		if retry:
			logger.debug('Services: Writing ip address')
			self.auth_tacacs_retry_count.set(retry)
		self.save_auth_server()	
		
	def create_coa_server(self):
		import traceback
		time.sleep(3)
		logger.debug('SecurityPage : Clicking on New button')
		self.create_auth_server.click()
		time.sleep(2)
		logger.debug('SecurityPage : Clicking on CoA_only')
		self.coa_only_checkbox.click()
		logger.debug('SecurityPage : Enter invalid values in the fields')
		logger.debug('SecurityPage : Setting invalid server name ')
		self.authentication_server_name.set(self.config.config_vars.coa_invalid_name)
		logger.debug('SecurityPage : Setting invalid ip')
		self.auth_server_ip_address.set(self.config.config_vars.coa_invalid_ip)
		logger.debug('SecurityPage : Setting invalid shared key ')
		self.auth_server_shared_key.set(self.config.config_vars.coa_invalid_shared_key)
		logger.debug('SecurityPage : Setting invalid retype shared key ')
		self.auth_server_retype_shared_key.set(self.config.config_vars.coa_invalid_retype_shared_key)
		logger.debug('SecurityPage : Clicking on Save Server button')
		self.auth_server_save.click()
		time.sleep(5)
		if not self.auth_server_name_error:
			raise AssertionError("COA invalid name message not visible .Traceback: %s " %traceback.format_exc())
		if not self.coa_invalid_ipaddr_msg:
			raise AssertionError("COA invalid ip message not visible .Traceback: %s " %traceback.format_exc())
		if not self.coa_invalid_sharedkey_msg:
			raise AssertionError("COA invalid shared key message not visible .Traceback: %s " %traceback.format_exc())
		if not self.coa_invalid_retype_shared_msg:
			raise AssertionError("COA invalid retyrp shared key message not visible .Traceback: %s " %traceback.format_exc())
		time.sleep(2)
		logger.debug('SecurityPage : Enter valid values in the fields')
		logger.debug('SecurityPage : Setting server name ')
		self.authentication_server_name.set(self.config.config_vars.coa_valid_name)
		logger.debug('SecurityPage : Setting ip')
		self.auth_server_ip_address.set(self.config.config_vars.coa_valid_ip)
		logger.debug('SecurityPage : Setting shared key ')
		self.auth_server_shared_key.set(self.config.config_vars.coa_valid_shared_key)
		logger.debug('SecurityPage : Setting retype shared key ')
		self.auth_server_retype_shared_key.set(self.config.config_vars.coa_valid_retype_shared_key)
		logger.debug('SecurityPage : Clicking on Save Server button')
		self.auth_server_save.click()			
		time.sleep(5)
		if not self.created_server_name_type:
			raise AssertionError("Created server redius type is not visible .Traceback: %s " %traceback.format_exc())
		time.sleep(2)
		
	def set_air_group_coa_port(self,value='5999'):
		'''
		Sets Air group Coa Port.
		'''
		logger.debug("SecurityPage : Write Air group Coa Port value.")
		self.air_group_coa_port_1.set(value)
		
	def click_coa_only_checkbox(self):
		logger.debug("SecurityPage : Click on CoA Only check box")
		self.coa_only_checkbox.click()
		
	def click_rfc_3576_checkbox(self):
		logger.debug('SecurityPage: Clicking RFC checkbox')
		self.assert_RFC_3576.click()
		
	def setting_nas_ip_and_identifier(self,ip=None,identifier=None):
		if ip:
			logger.debug('SecurityPage: Writing nas ip address')
			self.NAS_ip.set(ip)
		if identifier:
			logger.debug('SecurityPage: Writing nas identifier')
			self.nas_identifier.set(identifier)
	
	def editing_created_authserver_values(self,ip=None,key=None,deadtime=None,timeout=None,retry=None,nas_ip=None,nas_identifier=None,auth_port=None,accounting=None,rfc=True):
		logger.debug('SecurityPage: Writing ip')
		self.set_auth_server_ip_address(ip)
		logger.debug('SecurityPage: Writing SharedKey')
		self.set_auth_shared_key_retype(key,key)
		logger.debug('SecurityPage: Writing deadtime')
		self.set_auth_server_dead_time(deadtime)
		logger.debug('SecurityPage: Writing timeout')
		self.set_auth_server_time_out(timeout)
		logger.debug('SecurityPage: Writing retry count')
		self.set_auth_server_retry_count(retry)
		logger.debug('SecurityPage: Writing nas ip address')
		self.NAS_ip.set(nas_ip)
		logger.debug('SecurityPage: Writing nas identifier')
		self.nas_identifier.set(nas_identifier)
		logger.debug('SecurityPage: Writing auth_port')
		self.set_auth_server_auth_port(auth_port)
		logger.debug('SecurityPage: Writing actport')
		self.set_auth_server_accounting_port(accounting)
		if rfc:
			logger.debug('SecurityPage: Clicking RFC checkbox')
			self.assert_RFC_3576.click()
		
	def clicking_rad2_edit_button(self):
		logger.debug('SecurityPage: Clicking on rad 2 edit button')
		self.edit_rad2.click()
		
	def delete_authentication_server_2(self):
		'''
			Deleting the authentication server
		'''
		self.buy_time()
		if self.delete_auth_server_2:
			# self.auth_server_name.click()
			self.buy_time()
			logger.debug('SecurityPage: Clicking delete button')
			self.delete_auth_server_2.click()
			self.buy_time()
			self.browser.accept_alert()
			self.buy_time()
			
	def delete_authentication_server_3(self):
		'''
			Deleting the authentication server
		'''
		self.buy_time()
		if self.delete_auth_server_3:
			# self.auth_server_name.click()
			self.buy_time()
			logger.debug('SecurityPage: Clicking delete button')
			self.delete_auth_server_3.click()
			self.buy_time()
			self.browser.accept_alert()
			self.buy_time()
			
	def clicking_on_role_accordion(self):
		time.sleep(5)
		logger.debug("SecurityPage : open roles accordion.")
		self.role_accordion.click()
		time.sleep(5)
		
	def clicking_on_add_rule(self):
		time.sleep(5)	
		logger.debug('SecurityPage : Clicking on add rule button')
		self.access_rule_add_button.click()
		
	def delete_default_rule_if_present(self):
		logger.debug("AccessPage : looking for default rule...")
		self.buy_time()
		if self.default_rule:
			logger.debug("SecurityPage: Delete default rule...")
			self.buy_time()
			self.delete_default.click()
			self.buy_time()
	
	def assert_service(self):
		logger.debug('SecurityPage : Asserting Network option')
		self.browser.assert_element(self.network_service,'Network option is not present')
		logger.debug('SecurityPage : Asserting Application Category option')
		self.browser.assert_element(self.ac_app_category1,'Application Category option is not present')
		logger.debug('SecurityPage : Asserting Application option')
		self.browser.assert_element(self.service_application,'Application option is not present')
		logger.debug('SecurityPage : Asserting Web Category option')
		self.browser.assert_element(self.ac_web_category,'Web Category option is not present')
		logger.debug('SecurityPage : Asserting Web Reputation option')
		self.browser.assert_element(self.webreputation1,'Web Reputation option is not present')
		
	def asserting_rule_type_options(self, bandwidth = True):
		logger.debug('SecurityPage : Asserting Captive Portal option')
		self.browser.assert_element(self.rule_captive_portal,'Captive Portal option is not present')
		logger.debug('SecurityPage : Asserting CALEA option')
		self.browser.assert_element(self.rule_calea,'CALEA option is not present')
		if bandwidth:
			logger.debug('SecurityPage : Asserting Bandwidth Contract option')
			self.browser.assert_element(self.rule_bandwidth,'Bandwidth Contract option is not present')
	
	def click_on_cancel_button(self):
		'''
			Clicking on cancel button
		'''
		logger.debug('SecurityPage : Clicking on Cancel button')
		self.cancel_button_1.click()

	def assert_internal_server_user_type_dropdown_values(self):
		'''
			Asserts for Type dropdown values of Internal server user.
		'''
		options = self.user_type.get_options()
		if not options[0] == '-Select-':
			raise AssertionError(" -Select- option not found .Traceback: %s " %traceback.format_exc())
		if not options[1] == 'Guest':
			raise AssertionError(" Guest option not found .Traceback: %s " %traceback.format_exc())
		if not options[2] == 'Employee':
			raise AssertionError(" Employee option not found .Traceback: %s " %traceback.format_exc())

	def click_on_ok_button(self):
		'''
		Clicks on 'OK' button to create new user fpor internal server.
		'''
		logger.debug("SecurityPage : Click on new.")	
		self.create_new_user.click()
		self.buy_time()
		
	def edit_created_captive_portal(self):
		'''
		Clicks on edit icon to edit created captive portal.
		'''
		logger.debug("SecurityPage : Click on edit icon.")
		self.edit_captive_portal1.click()
		self.buy_time()
		
	def edit_captive_portal(self,name=None,type=None,ip=None,url=None,port=None,auth_text=None,http1=True,captive_portal=None,whitelisting=None,redirect_url_text=None):
		'''
		Edits captive portal.
		'''
		logger.debug("SecurityPage : Click on edit icon.")
		self.edit_captive_portal1.click()
		time.sleep(5)
		# logger.debug('SecurityPage: Setting the captive portal Name')
		# self.name_text_box.set(name)
		if type:
			logger.debug('SecurityPage: Selecting the captive portal Type')
			self.captive_portal_type.set(type)
		if ip:
			logger.debug('SecurityPage: Setting the captive portal IP or HostName')
			self.captive_portal_ip.set(ip)
		if url:
			logger.debug('SecurityPage: Setting the captive portal URL')
			self.captive_portal_url.set(url)
		if port:
			logger.debug('SecurityPage: Setting the captive portal Port')
			self.captive_portal_port.set(port)
		if http1:
			logger.debug('SecurityPage: Clicking the Use Https check box')
			self.security_use_https.click()
		if auth_text:
			logger.debug('SecurityPage: Setting the captive portal Auth Text')
			self.captive_portal_auth_text.set(auth_text)
		if captive_portal:
			logger.debug('SecurityPage: Setting the captive portal failure')
			self.captive_portal_failure.set(captive_portal)
		if whitelisting:
			logger.debug('SecurityPage: Enabling Automatic URL whitelisting')
			if not self.auto_url_whitelisting.is_selected():
				self.auto_url_whitelisting.click()
		else:
			logger.debug('SecurityPage: Disabling Automatic URL whitelisting')
			if self.auto_url_whitelisting.is_selected():
				self.auto_url_whitelisting.click()
		if redirect_url_text:
			logger.debug('SecurityPage: Setting the Redirect URL Text')
			self.redirect_url.set(redirect_url_text)
		time.sleep(6)
		logger.debug('SecurityPage: Clicking save button')
		self.captive_portal_save_button.click()
		time.sleep(6)
		
	def delete_captive_portal_testradius1(self):
		'''
		Deletes Captive portal testradius1
		'''
		if self.delete_external_captive_1:
			logger.debug('SecurityPage: Clicking delete button')
			self.delete_external_captive_1.click()	
			
	def edit_cp1(self,type,authtext):
		logger.debug('SecurityPage: Selecting the captive portal Type')
		self.captive_portal_type.set(type)
		logger.debug('SecurityPage: Setting the captive portal Auth Text')
		self.captive_portal_auth_text.set(authtext)
		time.sleep(6)
		logger.debug('SecurityPage: Clicking save button')
		self.captive_portal_save_button.click()
		time.sleep(6)
		
	def deleting_cp1(self):
		if self.delete_cp1 :
			logger.debug('SecurityPage : Deleting Cp1 ...Clicking on Delete button')
			self.delete_cp1.click()
				
	def assert_captive_ip_error(self,ip_error):
		'''
		Asserts Captive Port IP Error 
		'''
		if ip_error == 'True':
			logger.debug('SecurityPage : Asserting Captive Port IP Error')
			self.browser.assert_element(self.captive_ip_error,'Captive Portal IP Error is not present')
		if ip_error == 'False':
			logger.debug('SecurityPage : Asserting Captive Port IP Error')
			self.browser.assert_element(self.captive_ip_error,'Captive Portal IP Error is  present', False)
	
	def assert_captive_url_req_error(self,url_error):
		'''
		Asserts Captive Portal Url Error 
		'''
		if url_error == 'True':
			logger.debug('SecurityPage : Asserting Captive Portal Url Error')
			self.browser.assert_element(self.captive_url_req_error,'Captive Port Url Error is not present')
		if url_error == 'False':
			logger.debug('SecurityPage : Asserting Captive Port IP Error')
			self.browser.assert_element(self.captive_url_req_error,'Captive Portal Url Error is  present', False)
	
	def assert_captive_port_error(self,port_error):
		'''
		Asserts Captive Portal Port Error 
		'''
		if port_error == 'True':
			logger.debug('SecurityPage : Asserting Captive Portal Port Error')
			self.browser.assert_element(self.captive_port_error,'Captive Portal Port Error is not present')
		if port_error == 'False':
			logger.debug('SecurityPage : Asserting Captive Portal port Error')
			self.browser.assert_element(self.captive_port_error,'Captive Portal Port Error is  present', False)
			
	def assert_captive_auth_text_req_error(self,text_error):
		'''
		Asserts Captive Portal Auth Text Required Error 
		'''
		if text_error == 'True':
			logger.debug('SecurityPage : Asserting Captive Portal Auth Text Required  Error')
			self.browser.assert_element(self.captive_auth_text_req_error,'Captive Portal Auth Text Required  Error is not present')
		if text_error == 'False':
			logger.debug('SecurityPage : Asserting Captive Portal Auth Text Required  Error')
			self.browser.assert_element(self.captive_auth_text_req_error,'Captive Portal Auth Text Required  Error is  present', False)
			
	def page_down(self):
		'''
		scroll down the page
		'''
		self.browser.key_press(u'\ue009')
		self.browser.key_press( u'\ue00f')
		
	
	def assert_captive_portal_type_and_options(self):
		'''
		asserts default captive portal type and options
		'''
		logger.debug('SecurityPage: Asserting default captive portal type')
		if not self.captive_portal_type.get_selected() == self.config.config_vars.Captive_Role_Text:
			raise AssertionError('SecurityPage: Captive portal type is not set to Authentication text')
		options = self.captive_portal_type.get_options()
		if not options[1] == self.config.config_vars.Captive_Role_Radius_Authentication:
			raise AssertionError('SecurityPage:In Captive portal type Radius_Authentication is not listed')
			
	def assert_default_captive_portal_values(self):
		'''
		asserts default values of default captive portal 
		'''
		logger.debug('Security : Asserting default value of ip')
		if not self.captive_portal_ip.get() == self.config.config_vars.localhost:
			raise AssertionError('SecurityPage:In Captive portal IP is not set to Localhost')
		logger.debug('Security : Asserting default value of url')
		if not self.captive_portal_url.get() == self.config.config_vars.external_captive_url:
			raise AssertionError('SecurityPage:In Captive portal url is not set to /')
		logger.debug('Security : Asserting default value of captive portal failure')
		if not self.Security_CaptivePortalFailure.get_selected() == self.config.config_vars.external_captive_portal_failure:
			raise AssertionError('SecurityPage:In Captive portal failure is not set to deny internet')
		logger.debug('Security : Asserting automatic url whitelisting')
		if not self.Secuirty_AutoUrlWhitelisting.is_selected():
			raise AssertionError('SecurityPage:In Captive portal url whitelisting is not selected')
		self.Security_CaptivePortalFailure.set(self.config.config_vars.captive_portal_failure_allow)
		logger.debug('Security : Asserting default value of auth text')
		if not self.captive_portal_auth_text.get() == self.config.config_vars.external_captive_auth_text:
			raise AssertionError('SecurityPage:In Captive portal auth text is not set to external_captive_auth_text')
		logger.debug('Security : Asserting default value of redirect url')
		if not self.Captive_RedirectUrl.get() == '':
			raise AssertionError('SecurityPage:In Captive portal redirect url is not set to blank')
			
	def set_captive_portal_type(self,value):
		'''
		set captive portal type
		'''
		logger.debug('SecurityPage:Writing captive portal type')
		self.captive_portal_type.set(value)
		
	def create_app_rf_rules(self):
		self.clicking_on_add_rule()
		self.ac_app_category6.click()
		self.antivirus1.click()
		self.rule_save_button_1.click()
		self.ac_app_category6.click()
		self.Collaboration1.click()
		self.action_role.set(self.config.config_vars.action_role)
		self.rule_save_button_2.click()
		self.save_setting.click()

	def click_app_category_service(self):
		'''
		Clicks 'App category' service radio button.
		'''
		if self.ac_app_category1:
			logger.debug('Security : Selecting app-category service')
			self.ac_app_category1.click()
			
	def click_antivirus(self):
		'''
		Clicks 'Antivirus'  check button.
		'''
		if self.antivirus1:
			logger.debug('Security : Selecting Antivirus checkbox')
			self.antivirus1.click()
			
	def select_application_throttling(self):
		'''
		Select Application throttling checkbox.
		'''
		if self.throttle_enable:
			logger.debug('Security : Selecting Application throttling checkbox')
			self.throttle_enable.click()

	def select_log_option(self):
		'''
		Select log option checkbox.
		'''
		if self.options_log_6:
			logger.debug('Security : Selecting log option checkbox')
			self.options_log_6.click()

	def select_dscp_option(self):
		'''
		Select dscp option checkbox.
		'''
		if self.options_dscp_6:
			logger.debug('Security : Selecting dscp option checkbox')
			self.options_dscp_6.click()

	def select_blacklist_option(self):
		'''
		Select blacklist option checkbox.
		'''
		if self.options_blacklist_6:
			logger.debug('Security : Selecting blacklist option checkbox')
			self.options_blacklist_6.click()

	def select_priority_option(self):
		'''
		Select priority option checkbox.
		'''
		if self.options_p_802_6:
			logger.debug('Security : Selecting priority option checkbox')
			self.options_p_802_6.click()

	def access_control_save_roles_action(self):
		'''
		Clicks on save button
		'''
		if self.rule_save_button_1:
			logger.debug('Security : Clicking on Save button')
			self.rule_save_button_1.click()

	def set_rule_type(self,rule_type):
		'''
		Select rule type dropdown value.
		'''
		logger.debug('SecurityPage : Selecting rule type.')
		self.rule_type_dropdown_2.set(rule_type)

	def calea_save_roles_action(self):
		'''
		Clicks on save button
		'''
		if self.rule_save_button_2:
			logger.debug('Security : Clicking on Save button')
			self.rule_save_button_2.click()

	def set_bandwidth_downstream_value(self,value):
		'''
		Sets Downstream value.
		'''
		if self.downstream_textbox:
			logger.debug('Security : Setting Downstream value')
			self.downstream_textbox.set(value)
			
	def set_bandwidth_upstream_value(self,value):
		'''
		Sets Upstream value.
		'''
		if self.upstream_textbox:
			logger.debug('Security : Setting Upstream value')
			self.upstream_textbox.set(value)
			
	def check_uncheck_bandwidth_contract_options(self,downstream=False,upstream=False):
		'''
		Setting Bandwidth Contract options
		'''
		if downstream:
			logger.debug('Security : Selcting PerUnit for downstream.')
			if not self.peruserdownstream.is_selected():
				self.peruserdownstream.click()
		else:
			logger.debug('Security : Unchecking PerUnit for downstream.')
			if self.peruserdownstream.is_selected():
				self.peruserdownstream.click()
				
		if upstream:
			logger.debug('Security : Selcting PerUnit for upstream.')
			if not self.peruserupstream.is_selected():
				self.peruserupstream.click()
		else:
			logger.debug('Security : Unchecking PerUnit for upstream.')
			if self.peruserupstream.is_selected():
				self.peruserupstream.click()
				
	def click_web_category_service(self):
		'''
		Clicks 'Web category' service radio button.
		'''
		if self.ac_web_category_6:
			logger.debug('Security : Selecting Web-category service')
			self.ac_web_category_6.click()

	def web_category_select_log_blacklist(self,log=False,blacklist=False):
		'''
		Select log and blacklist option checkbox.
		'''
		if log:
			if not self.web_category_log_7.is_selected():
				logger.debug('Security : Selecting log option checkbox')
				self.web_category_log_7.click()
		else:
			if self.web_category_log_7.is_selected():
				logger.debug('Security : Unchecking log option checkbox')
				self.web_category_log_7.click()
				
		if blacklist:
			if not self.web_category_blacklist_7.is_selected():
				logger.debug('Security : Selecting log option checkbox')
				self.web_category_blacklist_7.click()
		else:
			if self.web_category_blacklist_7.is_selected():
				logger.debug('Security : Unchecking log option checkbox')
				self.web_category_blacklist_7.click()
				
	def set_vlan_id(self,vlan_id=None):
		'''
		Set vlan id.
		'''
		logger.debug('SecurityPage : Entering valid vlan id')
		self.vlan_id_textbox.set(vlan_id)		
		
		
	def check_global_search(self,value):
		'''
		searches the given input and displays results
		'''
		logger.debug('SecurityPage :writing into search text box')
		if self.localSearchText:
			self.localSearchText.set(value)
			self.browser.key_press( u'\ue007')
			if self.search_result:
				logger.debug('SecurityPage :Global search tab displaying results')