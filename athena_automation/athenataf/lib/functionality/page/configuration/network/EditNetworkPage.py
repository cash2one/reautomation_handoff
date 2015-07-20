from athenataf.lib.util.WebPage import WebPage
from selenium.webdriver.common.action_chains import ActionChains
import logging
logger = logging.getLogger('athenataf')
import traceback
import time


class EditNetworkPage(WebPage):
	def __init__(self, test, browser, config):
		time.sleep(5)
		WebPage.__init__(self, "EditNetwork", test, browser, config)
		self.test.assertPageLoaded(self)

		
	def isPageLoaded(self):
		if self.network_type:
			return True    
		else:
			return False

	def edit_vlan_settings(self,network_assigned=False):
		logger.debug("EditNetworkPage: Clicking on vlan setting button")
		self.buy_time()
		self.vlan_settings.click()
		self.buy_time()
		if not self.vlan_networks_form:
			logger.debug("EditNetworkPage: Clicking on vlan setting button")
			self.vlan_settings.click()
		if network_assigned:
			logger.debug("EditNetworkPage: Clicking on Network Assigned Radio button")
			self.network_assigned.click()
		else:
			logger.debug("EditNetworkPage: Clicking on dynamic  Radio button")
			self.dynamic.click()
		logger.debug("EditNetworkPage: Clicking on save setting button")
		self.save_settings.click()
		for i in range(1,4):
			if self.network_list:
				break
			logger.debug("EditNetworkPage: Clicking on save setting button")
			self.save_settings.click()
		time.sleep(20)

	def set_uppercase_delimiter_option(self):
		logger.debug("EditNetworkPage: Clicking on security accordian")
		self.security_accordion.click()
		logger.debug("EditNetworkPage: Setting auth delimiter as blank")
		self.mac_auth_delimiter.set('')
		logger.debug('EditNetworkPage : Setting uppercase support to Disabled')
		self.open_uppercase_support.set('Disabled')
		logger.debug("EditNetworkPage: Clicking on save setting button")
		self.save_settings.click()
		time.sleep(20)

	def delete_existing_rule(self):
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Deleting rule')
		self.rule_delete_button.click()
		logger.debug('EditNetworkPage : Clicking on Save button')
		self.save_settings.click()
		time.sleep(20)
		logger.debug('EditNetworkPage : Clicking on Network option')
		self.network_button.click()

	def change_existing_vlan_id_1(self):
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(8)
		logger.debug('EditNetworkPage : Editing rule')
		self.rule_edit_button.click()
		logger.debug('EditNetworkPage : Changing vlan id to 1')
		self.vlan_id.set(self.config.config_vars.vlan_id_1)
		logger.debug('EditNetworkPage : Clicking on Save')
		self.save.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Clicking on Save button')
		self.save_settings.click()
		time.sleep(20)
		logger.debug('EditNetworkPage : Clicking on Network option')
		self.network_button.click()
		time.sleep(8)

	def change_existing_vlan_id_4093(self):
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Editing rule')
		self.rule_edit_button.click()
		logger.debug('EditNetworkPage : Changing vlan id to 4093')
		self.vlan_id.set(self.config.config_vars.vlan_id_4093)
		logger.debug('EditNetworkPage : Clicking on Save')
		self.save.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Clicking on Save button')
		time.sleep(5)
		logger.debug("EditNetworkPage: Clicking on save setting button")
		self.save_settings.click()
		time.sleep(20)
		logger.debug('EditNetworkPage : Clicking on Network option')
		self.network_button.click()
		time.sleep(8)

	def change_vlan_to_calea(self):
		time.sleep(8)
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Editing rule')
		self.rule_edit_button.click()
		logger.debug('EditNetworkPage : Changing Rule type to CALEA')
		self.rule_type_dropdown.set(self.config.config_vars.access_rule_vlan_calea)
		logger.debug('EditNetworkPage : Clicking on Save')
		self.save.click()
		time.sleep(5)
		if self.created_vlan_assignment:
			raise AssertionError("Vlan assignment rule is present.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Save button')
		self.save_settings.click()
		time.sleep(20)      
        

	def create_new_vlan_rule(self):
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Clicking on Add(+) button')
		self.add_rule_plus_button.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Choosing rule type VLAN Assignment')
		self.rule_type_dropdown_1.set(self.config.config_vars.access_rule_vlan_assignment)
		logger.debug('Access Page : Entering valid value in Vlan Id')
		self.vlan_id.set(self.config.config_vars.vlan_id_4093)
		logger.debug('Access Page : Clicking on Save button')
		self.save.click()
		logger.debug("EditNetworkPage: Clicking on save setting button")
		self.save_settings.click()
		time.sleep(20)

	def change_vlan_to_captive_portal(self):
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Editing rule')
		self.rule_edit_button.click()
		logger.debug('EditNetworkPage : Choosing rule type Captive Portal')
		self.rule_type_dropdown.set(self.config.config_vars.access_rule_captive_portal)
		logger.debug('Access Page : Clicking on Save button')
		self.save.click()
		time.sleep(5)
		logger.debug("EditNetworkPage: Clicking on save setting button")
		self.save_settings.click()
		time.sleep(20)

	def change_vlan_to_access_control(self):
		time.sleep(8)
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Editing rule')
		self.rule_edit_button.click()
		logger.debug('EditNetworkPage : Changing Rule type to Access Control')
		self.rule_type_dropdown.set(self.config.config_vars.access_rule_access_control)
		logger.debug('EditNetworkPage : Changing action to deny')
		self.action_dropdown.set(self.config.config_vars.action_deny)
		logger.debug('EditNetworkPage : Clicking on Save')
		self.save.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Clicking on Save button')
		self.save_settings.click()
		time.sleep(20)
		logger.debug('EditNetworkPage : Checking EditNetworkPage rule is present or not')
		if self.created_vlan_assignment:
			raise AssertionError("EditNetworkPage rule is present.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Network option')
		self.network_button.click()
		time.sleep(8)

	def delete_existing_bandwidth_contract_rule(self):
		time.sleep(5)
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Clicking on network based radio')
		time.sleep(5)
		self.network_based.click()
		logger.debug('EditNetworkPage : Deleting rule')
		self.bw_rule_delete_button.click()
		logger.debug('EditNetworkPage : Clicking on Save button')
		self.save_settings.click()
		time.sleep(20)
		logger.debug('EditNetworkPage : Checking bandwidth contract rule is present or not')
		if self.bw_rule_assignment:
			raise AssertionError("EditNetworkPage rule is present.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Network option')
		time.sleep(5)
		logger.debug('EditNetworkPage : Clicking on Network option')
		self.network_button.click()

	def change_to_captive_portal(self):
		time.sleep(8)
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Editing rule')
		self.rule_edit_button.click()
		logger.debug('EditNetworkPage : Changing Rule type to Captive Portal')
		self.rule_type_dropdown.set(self.config.config_vars.access_rule_captive_portal)
		logger.debug('EditNetworkPage : Clicking on Save')
		self.save.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Clicking on Save button')
		self.save_settings.click()
		time.sleep(20)
		#         if self.created_vlan_assignment:
		#             raise AssertionError("EditNetworkPage rule is present.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Network option')
		self.network_button.click()
		time.sleep(8)

	def change_bw_to_vlan(self):
		time.sleep(8)
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Clicking on network based radio')
		if not self.network_based.is_selected():
			self.network_based.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Editing rule')
		self.bw_rule_edit_button.click()
		logger.debug('EditNetworkPage : Changing Rule type to vlan assignment')
		self.bw_dropdown_1.set(self.config.config_vars.access_rule_vlan_assignment)
		logger.debug('EditNetworkPage : Setting vlan id')
		self.vlan_id_1.set(self.config.config_vars.vlan_id_1)
		logger.debug('EditNetworkPage : Clicking on Save')
		self.save_2.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Clicking on Save button')
		self.save_settings.click()
		time.sleep(20)
		#         if not self.bw_rule_assignment:
		#             raise AssertionError("EditNetworkPage bandwidth contract rule is present.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Network option')
		self.network_button.click()
		time.sleep(8)

	def change_bw_to_captive_portal(self):
		time.sleep(8)
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Clicking on network based radio')
		if not self.network_based.is_selected():
			self.network_based.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Editing rule')
		self.bw_rule_edit_button.click()
		logger.debug('EditNetworkPage : Changing Rule type to captive portal')
		self.bw_dropdown_1.set(self.config.config_vars.access_rule_captive_portal)
		logger.debug('EditNetworkPage : Clicking on Save')
		self.save_2.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Checking bandwidth contract rule is present or not')
		if self.bw_rule_assignment:
			raise AssertionError("EditNetworkPage bandwidth contract rule is present.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Save button')
		self.save_settings.click()
		time.sleep(20)
		logger.debug('EditNetworkPage : Clicking on Network option')
		self.network_button.click()
		time.sleep(8)

	def _click_access_accordion(self):
		logger.debug("EditNetworkPage : clicking 'ACCESS' accordion...")
		self.access_accordion.click()
		if not self.role_based:
			logger.debug("EditNetworkPage : clicking 'ACCESS' accordion...")
			self.access_accordion.click()

	def delete_access_rule(self):
		logger.debug("EditNetworkPage : clicking 'Delete' icon...")
		self.delete.click()
		logger.debug("EditNetworkPage : clicking 'Save Settings' button...")
		self.save_settings.click()
		time.sleep(20)

	def assert_new_rule_created(self, service, destination):
		self._click_access_accordion()
		logger.debug("EditNetworkPage : clicking 'Network Based' radio button...")
		self.network_based.click()
		time.sleep(8)
		logger.debug("EditNetworkPage : clicking 'Edit' icon...")
		self.edit.click()
		logger.debug("EditNetworkPage : Assert 'SERVICE' drop down value...")
		if not self.new_service_0.get_selected() == service:
			raise AssertionError("'SERVICE' drop down not set to '%s'.Traceback: %s " %(traceback.format_exc(), service))
		logger.debug("EditNetworkPage : Assert 'DESTINATION' drop down value...")
		if not self.new_destination_0.get_selected() == destination:
			raise AssertionError("'DESTINATION' drop down not set to '%s'.Traceback: %s " %(traceback.format_exc(), destination))

	def delete_calea_rule(self):
		logger.debug("EditNetworkPage : Calling _click_access_accordion method ...")
		self._click_access_accordion()
		logger.debug("EditNetworkPage : clicking 'Network Based' radio button...")
		self.network_based.click()
		time.sleep(5)
		logger.debug("EditNetworkPage : clicking 'Delete' icon...")
		self.delete.click()
		logger.debug("EditNetworkPage : clicking Calea Delete icon...")
		self.calea_delete.click()
		logger.debug("EditNetworkPage : clicking 'Save Settings' button...")
		time.sleep(5)		
		logger.debug("EditNetworkPage : clicking 'Save Settings' button...")
		self.save_settings.click()
		time.sleep(20)

	def edit_calea_rule(self):
		logger.debug("EditNetworkPage : Calling _click_access_accordion method ...")
		self._click_access_accordion()
		logger.debug("EditNetworkPage : clicking 'Network Based' radio button...")
		self.network_based.click()
		time.sleep(5)
		logger.debug("EditNetworkPage : clicking Calea Edit icon...")
		self.calea_edit.click()
		logger.debug("EditNetworkPage : Asserting 'RULE TYPE' values...")
		if not self.new_rule_type_1.get_selected() == self.config.config_vars.rule_type_calea:
			raise AssertionError("'Rule Type' drop down not set to CALEA.Traceback: %s " %traceback.format_exc())
		logger.debug("EditNetworkPage : Choosing 'Access Control' ")
		self.new_rule_type_1.set(self.config.config_vars.default_rule_type)
		self._save_rule()
		logger.debug("EditNetworkPage : clicking 'Save Settings' button...")
		time.sleep(5)		
		logger.debug("EditNetworkPage : clicking 'Save Settings' button...")
		self.save_settings.click()
		time.sleep(20)

	def _save_rule(self):
		logger.debug("Click 'SAVE' button..")
		self.save1.click()

	def delete_edited_calea_rule(self):
		logger.debug("EditNetworkPage : Calling _click_access_accordion method ...")
		self._click_access_accordion()
		logger.debug("EditNetworkPage : clicking 'Network Based' radio button...")
		self.network_based.click()
		time.sleep(5)
		logger.debug("EditNetworkPage : clicking 'Delete' icon...")
		self.delete.click()
		logger.debug("EditNetworkPage : clicking Calea Delete icon...")
		self.delete.click()
		logger.debug("EditNetworkPage : clicking 'Save Settings' button...")
		time.sleep(5)		
		logger.debug("EditNetworkPage : clicking 'Save Settings' button...")
		self.save_settings.click()
		time.sleep(20)

	def change_network_based_to_unrestricted(self):
		time.sleep(8)
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Choosing Unrestricted radio button')
		self.unrestricted_radio.click()
		time.sleep(8)
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(20)

	def delete_role(self):
		logger.debug("EditNetworkPage : Click on 1st role.")
		self.role1.click()
		logger.debug("EditNetworkPage : Click on delete.")
		self.delete_role_assignment_1.click()
		logger.debug("EditNetworkPage : Click on 2nd role.")
		self.role2.click()
		logger.debug("EditNetworkPage : Click on delete.")
		self.delete_role_assignment_2.click()
		logger.debug("EditNetworkPage : Click on 1st role.")
		self.role4.click()
		logger.debug("EditNetworkPage : Click on delete.")
		self.delete_role_assignment_4.click()
		logger.debug("EditNetworkPage : Click on 1st role.")
		self.role6.click()
		logger.debug("EditNetworkPage : Click on delete.")
		self.delete_role_assignment_6.click()
		logger.debug("EditNetworkPage : calling _save_settings method...")
		self._save_settings() 

	def delete_multiple_access_rule(self):
		logger.debug("EditNetworkPage : Delete second access rule.")
		self.access_control_delete_1.click()
		logger.debug("EditNetworkPage : Delete third access rule.")
		self.access_control_delete_2.click()
		logger.debug("EditNetworkPage : Delete fourth access rule..")
		self.access_control_delete_3.click()
		logger.debug("EditNetworkPage : calling _save_settings method...")
		self._save_settings()

	def move_access_rule(self):
		logger.debug("EditNetworkPage : Move 1st access rule down.")
		self.access_control_down_0.click()
		logger.debug("EditNetworkPage : Move 2nd access rule down.")
		self.access_control_down_2.click()
		logger.debug("EditNetworkPage : Move 3rd access rule down.")
		self.access_control_up_3.click()      
		logger.debug("EditNetworkPage : Move last access rule down.")
		self.access_control_up_6.click()
		logger.debug("EditNetworkPage : calling _save_settings method...")
		self._save_settings()

	def _save_settings(self):
		logger.debug("EditNetworkPage : Click save settings.")
		self.save_settings.click()
		time.sleep(10)

	def delete_captive_rule(self):
		logger.debug("EditNetworkPage : Click on delete button.")
		self.delete_captive_portal.click()
		logger.debug("EditNetworkPage : calling _save_settings method...")
		self._save_settings()
		
	def assert_captive_portal(self):
		logger.debug("EditNetworkPage : Check for captive portal.")
		if not self.enforce_captive_portal:		
			raise AssertionError("'Enforce Captive Portal' not present.Traceback: %s " %traceback.format_exc())

	def modify_captive_portal_assignment_rule(self,default=False):
		logger.debug("EditNetworkPage : Click on edit button.")
		self.edit_captive_portal.click()
		if default:
			self.delete.click()
			logger.debug("EditNetworkPage : Click on edit button.")
			self.edit_captive_portal.click()
			logger.debug("EditNetworkPage : set rule type to calea.")
			self.rule_type_1.set(self.config.config_vars.default_rule_type)
		else:
			logger.debug("EditNetworkPage : Click on edit button.")
			self.edit_captive_portal.click()
			logger.debug("EditNetworkPage : set rule type to calea.")
			self.rule_type_1.set(self.config.config_vars.rule_type_calea)
		logger.debug("EditNetworkPage : Click save.")
		self.save_button.click()
		logger.debug("EditNetworkPage : calling _save_settings method...")
		self._save_settings()

	def change_unrestricted_to_network_based(self):
		time.sleep(8)
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Choosing Network based radio button')
		self.network_based.click()
		time.sleep(8)
		if not self.present_rules_check:
			raise AssertionError("'Rules are present.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(20)
		
	def change_rule_to_deny_h323(self):
		time.sleep(8)
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug("EditNetworkPage : clicking 'Network Based' radio button...")
		self.network_based.click()
		logger.debug('EditNetworkPage : Clicking on edit button of rule')
		self.buy_time()
		self.edit.click()
		self.buy_time()
		logger.debug('EditNetworkPage : Selecting service h323-tcp')
		self.new_service_1.set(self.config.config_vars.service_h323_tcp)
		logger.debug('EditNetworkPage : Selecting action deny')
		time.sleep(5)
		self.edit_action_dropdown.set(self.config.config_vars.action_deny_option)
		logger.debug('EditNetworkPage : Clicking on Save button')
		self.save_rule_button.click()
		time.sleep(5)
		if not self.modified_rule_deny_h323tcp:
			raise AssertionError("'Deny h323-tcp to all destinations is not present .Traceback: %s " %traceback.format_exc())		
		time.sleep(8)
		logger.debug('EditNetworkPage : Clicking on Save settings button')
		self.save_settings.click()
		time.sleep(20)
		
	def change_rule_to_allow_any(self):
		time.sleep(8)
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug("EditNetworkPage : clicking 'Network Based' radio button...")
		self.network_based.click()
		logger.debug('EditNetworkPage : Clicking on edit button of rule')
		self.edit.click()
		logger.debug('EditNetworkPage : Selecting service Any')
		self.new_service_1.set(self.config.config_vars.service_any)
		logger.debug('EditNetworkPage : Selecting action Allow')
		self.edit_action_dropdown.set(self.config.config_vars.action_allow)
		logger.debug('EditNetworkPage : Clicking on Save Setting button')
		time.sleep(5)
		self.save_rule_button.click()
		time.sleep(5)
		if not self.present_rules_check:
			raise AssertionError("'Allow any to all destinations is not present .Traceback: %s " %traceback.format_exc())		
		time.sleep(8)
		logger.debug('EditNetworkPage : Clicking on Save settings button')
		self.save_settings.click()
		time.sleep(20)
		
	def change_access_rule_to_captive_portal(self):
		time.sleep(8)
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug("EditNetworkPage : clicking 'Network Based' radio button...")
		self.network_based.click()
		logger.debug('EditNetworkPage : Clicking on edit button of rule')
		self.edit.click()
		logger.debug('EditNetworkPage : Setting rule type Captive Portal')
		self.change_rule_type.set(self.config.config_vars.access_rule_captive_portal)
		time.sleep(2)
		logger.debug('EditNetworkPage : Clicking on save button')
		self.save_rule_button.click()
		if not self.created_captive_portal_msg:
			raise AssertionError("Captive portal rule is not present .Traceback: %s " %traceback.format_exc())
		time.sleep(2)
		logger.debug('EditNetworkPage : Clicking on Save settings button')
		self.save_settings.click()
		time.sleep(20)
		
	def create_calea_rule(self):
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Clicking on Add(+) button')
		self.add_rule_plus_button.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Choosing rule type CALEA')
		self.rule_type_dropdown_1.set(self.config.config_vars.access_rule_vlan_calea)
		logger.debug('Access Page : Clicking on Save button')
		self.save_1.click()
		if not self.access_rule_type_CALEA:
			raise AssertionError("Calea rule is not present .Traceback: %s " %traceback.format_exc())	
		if not self.created_deny_rule:
			raise AssertionError("Deny any to all rule is not present .Traceback: %s " %traceback.format_exc())				
		logger.debug('Access Page : Clicking on Save Setting button')
		self.save_settings.click()	
		time.sleep(20)
		
	def assert_duplicate_rule_message(self):	
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Clicking on Add(+) button')
		self.add_rule_plus_button.click()
		logger.debug('EditNetworkPage : Clicking on save button')
		self.save_rule_button_2.click()
		time.sleep(5)
		if not self.duplicate_rule_msg:
			raise AssertionError("This rule already exists is not present .Traceback: %s " %traceback.format_exc())	
		logger.debug('EditNetworkPage : Clicking on message box OK button')
		self.msg_ok_button.click()		
		time.sleep(2)
		logger.debug('EditNetworkPage : Clicking on Network link')	
		self.network_button.click()
		time.sleep(5)
		
	def assert_deny_rule_message(self):
		time.sleep(4)
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		logger.debug('EditNetworkPage : Clicking on Network based radio button')
		self.network_based.click()
		time.sleep(5)
		if not self.created_deny_rule:
			raise AssertionError("Deny any to all destinations is not present .Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on network')
		self.networks.click()
		
	def assert_deny_rule_message_after_delete(self):
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		logger.debug('EditNetworkPage : Clicking on Network based radio button')
		self.network_based.click()
		time.sleep(5)
		if self.created_deny_rule:
			raise AssertionError("Deny any to all destinations is not present .Traceback: %s " %traceback.format_exc())
		time.sleep(2)
		logger.debug('Access Page : Clicking on Save Setting button')
		self.save_settings.click()
		time.sleep(10)
		
		
	def delete_created_h323_udp_rule(self):
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Clicking on delete button')
		self.rule_delete_button_1.click()
		logger.debug('EditNetworkPage : Clicking on Save settings button')
		self.save_settings.click()
		time.sleep(20)
		
	def delete_and_edit_rules(self):
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Editing a rule')
		self.rule_edit_pencil_button.click()
		time.sleep(2)
		self.service_dropdown.set(self.config.config_vars.service_h323_udp_value)
		logger.debug('EditNetworkPage : Clicking on Save button')
		self.save_1.click()
		logger.debug('EditNetworkPage : Deleting some rules')
		self.rule_delete_button_1.click()
		self.rule_delete_button_2.click()
		self.rule_delete_button_3.click()
		time.sleep(2)
		if self.deleted_rule_1:
			raise AssertionError("Rule1 is present .Traceback: %s " %traceback.format_exc())
# 		if self.deleted_rule_2:
# 			raise AssertionError("Rule2 is present .Traceback: %s " %traceback.format_exc())
		if self.deleted_rule_3:
			raise AssertionError("Rule3 is present .Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(20)
		
	def change_roaming_mac_authentication_settings(self):
		logger.debug('EditNetworkPage : Clicking on Security accordion')
		self.security_accordion.click()
		time.sleep(4)
		logger.debug('EditNetworkPage : Disabling 802.11r option')
		self.roaming_open.click()
		time.sleep(4)
		logger.debug('EditNetworkPage : Enabling MAC authentication option')
		self.mac_authentication.set(self.config.config_vars.mac_authentication_value)
		time.sleep(15)
		if not self.authentication_server.get_selected() == self.config.config_vars.authentication_server_value:
			raise AssertionError("Authentication server is not set to InternalServer .Traceback: %s " %traceback.format_exc())				
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(5)
		
	def assert_roaming_mac_authentication_changes(self):
		logger.debug('EditNetworkPage : Clicking on Security accordion')
		self.security_accordion.click()
		time.sleep(4)
		if self.roaming_open.is_selected():
			raise AssertionError("802.11r Roaming checkbox is not  Disabled .Traceback: %s " %traceback.format_exc())							
		if not self.mac_authentication.get_selected() == self.config.config_vars.mac_authentication_value:
			raise AssertionError("MAC Authentication is not set to Enabled .Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Network option')
		self.network_button.click()
		time.sleep(5)	
		
	def change_to_external_server(self):
		logger.debug('EditNetworkPage : Clicking on Security accordion')
		self.security_accordion.click()
		time.sleep(20)
		logger.debug('EditNetworkPage : Setting new external server')
		self.authentication_server.set(self.config.config_vars.new_external_server)
		time.sleep(3)
		logger.debug('EditNetworkPage : Entering details')
		self.auth_server_name.set(self.config.config_vars.auth_server_value)
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr_value)
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey_value)
		self.Retype_auth_shared_key.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug('EditNetworkPage : Saving external radius server')
		self.save_server.click()
		time.sleep(12)
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(8)		
# 		logger.debug('EditNetworkPage : Clicking on Network option')
# 		self.network_button.click()
# 		time.sleep(5)
		
	def assert_authentication_server_changes(self):
		logger.debug('EditNetworkPage : Clicking on Security accordion')
		self.security_accordion.click()
		time.sleep(20)
		if not self.authentication_server.get_selected() == self.config.config_vars.auth_server_value:
			raise AssertionError("Authentication Server 1 is not set to external server .Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Network option')
		self.network_button.click()
		time.sleep(5)
		
	def change_auth_server_2_to_external_server(self):
		logger.debug('EditNetworkPage : Clicking on Security accordion')
		self.security_accordion.click()
		time.sleep(20)
		logger.debug('EditNetworkPage : Setting new external server to Authentication Server 1')
		self.authentication_server.set(self.config.config_vars.new_external_server)
		time.sleep(3)
		logger.debug('EditNetworkPage : Entering details')
		self.auth_server_name.set(self.config.config_vars.auth_server_value)
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr_value)
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey_value)
		self.Retype_auth_shared_key.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug('EditNetworkPage : Saving external radius server')
		self.save_server.click()
		time.sleep(12)
		
		logger.debug('EditNetworkPage : Setting new external server to Authentication Server 2')
		self.authentication_server_2.set(self.config.config_vars.new_external_server)
		time.sleep(3)
		logger.debug('EditNetworkPage : Entering details')
		self.auth_server_name.set(self.config.config_vars.auth_server_value_2)
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr_value)
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey_value)
		self.Retype_auth_shared_key.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug('EditNetworkPage : Saving external radius server')
		self.save_server.click()
		time.sleep(12)
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(15)
		
	def change_delimiter_uppercase_rauth(self):
		logger.debug('EditNetworkPage : Clicking on Security accordion')
		self.security_accordion.click()
		time.sleep(4)
		# logger.debug('EditNetworkPage : Setting delimeter to :')
		# self.mac_auth_delimiter.set(self.config.config_vars.enterprise_delimeter)
		logger.debug('EditNetworkPage : Setting delimeter to :')
		self.mac_auth_delimiter.set(self.config.config_vars.enterprise_delimeter)
		logger.debug('EditNetworkPage : Setting uppercase support to enabled')
		self.open_uppercase_support.set(self.config.config_vars.uppercase_support_value_enabled)
		logger.debug('EditNetworkPage : Setting reauth interval to 10')
		self.reauth_interval.set(self.config.config_vars.reauth_interval_value)			
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(15)
		
	def assert_authentication_server_delimeter_uppercase_reauth_changes(self):
		conf = self.config.config_vars
		logger.debug('EditNetworkPage : Clicking on Security accordion')
		self.security_accordion.click()
		time.sleep(20)
		if not self.authentication_server_2.get_selected() == self.config.config_vars.auth_server_value_2:
			raise AssertionError("Authentication Server 2 is not set to external server .Traceback: %s " %traceback.format_exc())	
		self.browser.assert_drop_down_value(self.open_uppercase_support,conf.uppercase_support_value_enabled, "uppercase support option is not selected to 'Enabled'")
		self.browser.assert_text(self.mac_auth_delimiter,conf.enterprise_delimeter,'Delimiter not set to ":"','value')
		self.browser.assert_text(self.reauth_interval,conf.reauth_interval_value,'Reauth interval not set to "10"','value')
		logger.debug('EditNetworkPage : Clicking on Network option')
		self.network_button.click()
		time.sleep(5)
		
	def set_blacklisting_authentication_server2(self):
		logger.debug('EditNetworkPage : Clicking on Security accordion')
		self.security_accordion.click()
		time.sleep(20)
		logger.debug('EditNetworkPage : Enabling Blacklisting option')
		self.blacklisting.set(self.config.config_vars.blacklisting_value)
		logger.debug('EditNetworkPage : Changing Authentication Server 2 to InternalServer')
		self.authentication_server_2.set(self.config.config_vars.authentication_server_value)
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(20)
		
	def assert_blacklisting_auth_server_2_changes(self):
		logger.debug('EditNetworkPage : Clicking on Security accordion')
		self.security_accordion.click()
		time.sleep(20)
		if not self.authentication_server_2.get_selected() == self.config.config_vars.authentication_server_value:
			raise AssertionError("Authentication Server 2 is not set to InternalServer .Traceback: %s " %traceback.format_exc())
		if not self.blacklisting.get_selected() == self.config.config_vars.blacklisting_value:
			raise AssertionError("Blacklisting is not set to Enabled .Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Network option')
		self.network_button.click()
		time.sleep(5)

	def assert_network_changes(self):
		if not self.created_network_name:
			raise AssertionError("Created network name is not present .Traceback: %s " %traceback.format_exc())
		if not self.selected_voice_button:
			raise AssertionError("Selected voice radio is not present .Traceback: %s " %traceback.format_exc())
		time.sleep(2)
		logger.debug('EditNetworkPage : Clicking security accordion')
		self.security_accordion.click()
		time.sleep(5)
		if not self.roaming_open.is_selected():
			raise AssertionError("802.11r roaming is not  enabled .Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Network link')
		self.networks.click()
		time.sleep(5)
		
	def assert_network_blacklist_max_auth_changes(self):
		if not self.created_network_name:
			raise AssertionError("Created network name is not present .Traceback: %s " %traceback.format_exc())
		if not self.selected_employee_button:
			raise AssertionError("Selected employee radio is not present .Traceback: %s " %traceback.format_exc())
		time.sleep(2)
		logger.debug('EditNetworkPage : Clicking security accordion')
		self.security_accordion.click()
		time.sleep(2)
		if not self.blacklisting.get_selected() == 'Enabled':
			raise AssertionError("Blacklisting dropdown is not selected to enabled .Traceback: %s " %traceback.format_exc())
		if not self.max_auth_failures:
			raise AssertionError("Max Auth Failure textbox is not visible .Traceback: %s " %traceback.format_exc())					
		logger.debug('EditNetworkPage : Clicking on Network link')
		self.networks.click()
		time.sleep(5)	
	
	def edit_network_with_blacklisting_max_auth(self):
		if not self.created_network_name:
			raise AssertionError("Created network name is not present .Traceback: %s " %traceback.format_exc())
		if not self.selected_employee_button:
			raise AssertionError("Selected employee radio is not present .Traceback: %s " %traceback.format_exc())
		time.sleep(2)
		logger.debug('EditNetworkPage : Clicking security accordion')
		self.security_accordion.click()
		time.sleep(2)
		logger.debug('EditNetworkPage : Selecting Blacklisting value')
		self.blacklisting.set(self.config.config_vars.blacklisting_disabled)
		try:
			logger.debug('EditNetworkPage : Changing max authentication value to 0')
			self.max_auth_failures.set(self.config.config_vars.max_authentication_zero)
		except:
			logger.debug('EditNetworkPage : Clicking on Save Settings')
			self.save_settings.click()
		time.sleep(5)
		
	def verify_network_with_blacklisting_max_auth_changes(self):
		if not self.created_network_name:
			raise AssertionError("Created network name is not present .Traceback: %s " %traceback.format_exc())
		if not self.selected_employee_button:
			raise AssertionError("Selected employee radio is not present .Traceback: %s " %traceback.format_exc())
		time.sleep(2)
		logger.debug('EditNetworkPage : Clicking security accordion')
		self.security_accordion.click()
		time.sleep(2)
		if not self.blacklisting.get_selected() == 'Disabled':
			raise AssertionError("Blacklisting dropdown is not selected to enabled .Traceback: %s " %traceback.format_exc())
		if not self.max_auth_failures:
			raise AssertionError("Max Auth Failure textbox is not visible .Traceback: %s " %traceback.format_exc())					
		logger.debug('EditNetworkPage : Clicking on Network link')
		self.networks.click()
		time.sleep(5)
		
	def assert_security_level_enterprise(self):
		logger.debug('EditNetworkPage : Clicking on Security accordion')
		self.security_accordion.click()
		time.sleep(8)
		logger.debug('EditNetworkPage : Check security level selected as enterprise.')
		if not self.enteprise.is_selected():
			raise AssertionError("Security level not set as enterprise .Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Check key management.')
		if not self.security_key_management.get_selected() ==	self.config.config_vars.wpa2_enterprise:
			raise AssertionError("Key management not set to wpa2 enterprise .Traceback: %s " %traceback.format_exc())

	def assert_802_roaming_options(self):
		if not self.roaming_open:
			self.security_accordion.click()
		if not self.roaming_open.is_selected():
			raise AssertionError("802.11 roaming not enabled .Traceback: %s " %traceback.format_exc())
		if not self.authentication_server.get_selected() == self.config.config_vars.authentication_server_value:
			raise AssertionError("Authentication Server 1 is not set to InternalServer .Traceback: %s " %traceback.format_exc())

	def edit_advance_settings_and_reauth_interval(self):
		self.click_advanced_settings_accordion()
		logger.debug('EditNetworkPage : Disable Can be used without uplink')
		self.without_uplink.click()
		logger.debug('EditNetworkPage : Clicking security accordion')
		self.security_accordion.click()
		logger.debug('EditNetworkPage : disable okc')
		self.okc_checkbox.click()
		logger.debug("EditNetworkPage : Set auth interval time.")		
		self.reauth_interval.set(self.config.config_vars.edit_reauth_interval)
		self.reauth_unit.set('hrs.')
		logger.debug("EditNetworkPage : calling _save_settings method...")
		self._save_settings()
		
	def edit_max_client_threshold_and_mac_authentication(self):
		self.click_advanced_settings_accordion()		
		logger.debug("EditNetworkPage : Set max client threshold.")		
		self.max_client_threshold.set(self.config.config_vars.max_client_threshold)
		logger.debug('EditNetworkPage : Clicking security accordion')
		self.security_accordion.click()
		logger.debug('EditNetworkPage : Clicking Perform MAC authentication before 802.1X.')
		self.mac_authentication_enterprise.click()
		logger.debug('EditNetworkPage : Clicking MAC authentication fail-thru.')
		self.auth_failthru_enterprise.click()
		logger.debug('EditNetworkPage : Set upper case support.')
		self.open_uppercase_support.set(self.config.config_vars.Uppercase_Support_Enabled)
		logger.debug('EditNetworkPage : Setting value of auth delimeter')
		self.mac_auth_delimiter.set(self.config.config_vars.enterprise_delimeter)
		logger.debug('EditNetworkPage : Clicking on Save Settings')
		self._save_settings()
		
	def edit_enterprise_employee_network_blacklisting_enabled(self):
		self.click_advanced_settings_accordion()		
		logger.debug("EditNetworkPage : Set max client threshold.")		
		self.max_client_threshold.set('0')
		logger.debug('EditNetworkPage : Clicking security accordion')
		self.security_accordion.click()
		logger.debug('EditNetworkPage : Setting value of auth delimeter')
		self.mac_auth_delimiter.set('')
		logger.debug('EditNetworkPage : Selecting uppercase support value')
		self.open_uppercase_support.set(self.config.config_vars.disable_option)
		logger.debug('EditNetworkPage : Selecting Blacklisting value')
		self.blacklisting.set(self.config.config_vars.enable_option)
		logger.debug('EditNetworkPage : Clicking on Save Settings')
		self._save_settings()
		
	def disable_mac_authentication(self):
		logger.debug('EditNetworkPage : Clicking security accordion')
		self.security_accordion.click()
		logger.debug('EditNetworkPage : Disable Perform MAC authentication before 802.1X.')
		self.mac_authentication_enterprise.click()
		logger.debug('EditNetworkPage : Disable MAC authentication fail-thru.')
		self.auth_failthru_enterprise.click()
		logger.debug('EditNetworkPage : Disable okc.')
		self.okc_checkbox.click()
		logger.debug("EditNetworkPage : calling _save_settings method...")
		self._save_settings()				

	def set_accounting_delimeter_loadbalance_uppercase(self):
		'''
			Enabling Accounting dropdown, Entering Accounting Interval 10, Entering Delimeter to /, Enabling Uppercase Support
		'''
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.security_accordion.click()
		time.sleep(15)
		logger.debug('EditNetworkPage : Editing Accounting and Accouting Interval')
		self.accounting_dropdown.set(self.config.config_vars.accounting_enabled)
		self.account_interval.set(self.config.config_vars.edit_accounting_interval60)
		logger.debug('EditNetworkPage : Editing delimeter option')
		self.mac_auth_delimiter.set(self.config.config_vars.delimeter_textbox_value)
		logger.debug('EditNetworkPage : Editing Uppercase support option')
		self.open_uppercase_support.set(self.config.config_vars.uppercase_support_disabled)
		logger.debug('EditNetworkPage : Enabling load balancing')
		self.load_balancing_dropdown.set(self.config.config_vars.enabled_option)
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(20)	
		
	def verify_accounting_delimeter_loadbalance_uppercase_changes(self):
		'''
			Verifying changes
		'''
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.security_accordion.click()
		time.sleep(15)
		if not self.accounting_dropdown.get_selected() == self.config.config_vars.accounting_enabled:
			raise AssertionError("Accounting dropdown is not enabled .Traceback: %s " %traceback.format_exc())
		if not self.open_uppercase_support.get_selected() == self.config.config_vars.uppercase_support_disabled:
			raise AssertionError("Uppercase support is not disabled.Traceback: %s " %traceback.format_exc())
		if not self.load_balancing_dropdown.get_selected() == self.config.config_vars.accounting_enabled:
			raise AssertionError("LoadBalancing dropdown is not enabled .Traceback: %s " %traceback.format_exc())
		delimeter = self.mac_auth_delimiter.get()
		if not delimeter == self.config.config_vars.delimeter_textbox_value:
			raise AssertionError("Delimeter is not set to /.Traceback: %s " %traceback.format_exc())
		if not self.account_interval.get() == self.config.config_vars.edit_accounting_interval60:
			raise AssertionError("Accounting interval is not set to 60.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Network link')
		self.networks.click()
		time.sleep(5)
		
	def set_accounting_uppercase_auth_server(self):
		'''
		Editing Blacklisting, external auth server2
		'''
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.security_accordion.click()
		time.sleep(15)
		logger.debug('EditNetworkPage : Selecting Blacklisting value')
		self.blacklisting.set(self.config.config_vars.enable_option)
		logger.debug('EditNetworkPage : Setting new InternalServer to Authentication Server 2')
		self.authentication_server_2.set(self.config.config_vars.authentication_server_value)
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(20)
		
	def verify_accounting_uppercase_auth_server(self):
		'''
		verifying Blacklisting and authentication server 2
		'''
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.security_accordion.click()
		time.sleep(30)
		if not self.blacklisting.get_selected() == self.config.config_vars.enable_option:
			raise AssertionError("Blacklisting dropdown is not enabled .Traceback: %s " %traceback.format_exc())
		if not self.authentication_server_2.get_selected() == self.config.config_vars.authentication_server_value:
			raise AssertionError("Authentication server 2 is not set to InternalServer.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Network link')
		self.networks.click()
		time.sleep(5)
		
	def buy_time(self):
		time.sleep(15)
		
	def click_advanced_settings_accordion(self):
		time.sleep(15)
		logger.debug("EditNetworkPage : clicking 'Advanced Settings' accordion...")
		self.advanced_settings_accordion.click()
		if not self.broadcasefiltering:
			logger.debug("EditNetworkPage : clicking 'Advanced Settings' accordion...")
			self.advanced_settings_accordion.click()
			
	def click_vlans_accordion(self):
		logger.debug("EditNetworkPage : clicking 'Vlans' accordion...")
		self.vlans_accordion.click()
		if not self.virtual_controller_assigned:
			self.vlans_accordion.click()
			
	def click_security_accordion(self):
		logger.debug("EditNetworkPage : clicking 'Security' accordion...")
		self.security_accordion.click()
		if not self.passphrase_format:
			logger.debug("EditNetworkPage : clicking 'Security' accordion...")
			self.security_accordion.click()
			
			
	def check_security_configurations(self):
		logger.debug("EditNetworkPage : Checking whether 802.11r ROAMING feild is enabled")
		if not self.roaming_open.is_selected():
			raise AssertionError("802.11r ROAMING feild is disabled .Traceback: %s " %traceback.format_exc())
			
	def edit_advanced_settings(self):
		logger.debug('EditNetworkPage : Selecting ALL option from dropdown menu')
		self.broadcasefiltering.set(self.config.config_vars.edit_broadcasefiltering_all)
		logger.debug('EditNetworkPage : Selecting 7 beacons option from dropdown menu')
		self.dtiminterval.set(self.config.config_vars.edit_dtiminterval_7_beacons)
					
	def edit_security_configurations(self):
		logger.debug("EditNetworkPage : Disable 802.11r ROAMING.")
		self.roaming_open.click()
		logger.debug("EditNetworkPage : Enable Mac Authentication.")
		self.mac_authentication.set(self.config.config_vars.edit_Security_Mac_Authentication_Enabled)
		self.buy_time()
		logger.debug("EditNetworkPage : Checking whether Authentication Server feild is set to InternalServer")
		if not self.authentication_server.get_selected()=='InternalServer':
			raise AssertionError("Authentication Server feild is not set to InternalServer .Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Save Settings')
		self._save_settings()
		
		
	def edit_advanced_settings_default(self):
		logger.debug('EditNetworkPage : Selecting Disable option from dropdown menu')
		self.broadcasefiltering.set(self.config.config_vars.edit_broadcasefiltering_disabled)
		logger.debug('EditNetworkPage : Selecting 1 beacon option from dropdown menu')
		self.dtiminterval.set(self.config.config_vars.edit_dtiminterval_1_beacon)
		
	def _select_new_authentication_server(self, number): 
		logger.debug("EditNetworkPage : Select new for authentucation server %s." %number)
		if number == '1':
			self.buy_time()
			self.buy_time()
			self.authentication_server.set(self.config.config_vars.edit_new_server)
			self.buy_time()
			logger.debug('EditNetworkPage : Saving external radius server')
			self.save_server.click()
			self.buy_time()
			logger.debug("EditNetworkPage : Write Server name")
			self.auth_server_name.set(self.config.config_vars.edit_invalid_input)
			if not self.name_error:
				raise AssertionError("Server name error. i.e. Traceback: %s" %traceback.format_exc())
			self.buy_time()
			self.auth_server_name.set(self.config.config_vars.edit_auth_server_name)
		elif number == '2':
			self.buy_time()
			self.buy_time()
			self.authentication_server_2.set(self.config.config_vars.edit_new_server)
			self.buy_time()
			logger.debug('EditNetworkPage : Saving external radius server')
			self.save_server.click()
			self.buy_time()
			logger.debug("EditNetworkPage : Write Server name")
			self.auth_server_name.set(self.config.config_vars.edit_invalid_input)
			if not self.name_error:
				raise AssertionError("Server name error. i.e. Traceback: %s" %traceback.format_exc())
			self.buy_time()
			logger.debug('EditNetworkPage : Settings the auth server value')
			self.auth_server_name.set(self.config.config_vars.edit_auth_server_name2)
					
	def create_external_radiuds_server(self, number):
		logger.debug("EditNetworkPage : Calling  _select_new_authentication_server method")
		self._select_new_authentication_server(number)
		logger.debug("EditNetworkPage : Write Server ip address")
		self.auth_ipaddr.set(self.config.config_vars.edit_invalid_input)
		logger.debug('EditNetworkPage : Saving external radius server')
		self.save_server.click()
		if not self.ip_error:
			raise AssertionError("Invalid IP. i.e. Traceback: %s" %traceback.format_exc())
		self.buy_time()
		logger.debug('EditNetworkPage : Settings the auth ip address value')
		self.auth_ipaddr.set(self.config.config_vars.edit_auth_ipaddr)
		
		logger.debug("EditNetworkPage : Write Shared key.")
		self.Auth_Sharedkey.set(self.config.config_vars.edit_invalid_input)
		if not self.shared_key_error:
			raise AssertionError("Length error. i.e. Traceback: %s" %traceback.format_exc())
		self.buy_time()
		logger.debug('EditNetworkPage : Settings the auth shared key value')
		self.Auth_Sharedkey.set(self.config.config_vars.edit_Auth_Sharedkey)
		
		logger.debug("EditNetworkPage : Write retype - Shared key.")
		self.Retype_auth_shared_key.set(self.config.config_vars.edit_pswdTxt)
		logger.debug('EditNetworkPage : Saving external radius server')
		self.save_server.click()
		if not self.retype_shared_key_error:
			raise AssertionError("Fields do not match error. i.e. Traceback: %s" %traceback.format_exc())
		self.buy_time()
		logger.debug("EditNetworkPage : Write retype - Shared key.")
		self.Retype_auth_shared_key.set(self.config.config_vars.edit_Retype_auth_shared_key)
		if self.drpvlan_error:
			self.drpvlan.set(self.config.config_vars.reauth_2)
		self.buy_time()
		logger.debug('EditNetworkPage : Saving external radius server')
		self.save_server.click()
		self.buy_time()
				
	def check_security_configurations1(self):
		logger.debug("EditNetworkPage : Checking whether 802.11r ROAMING feild is enabled")
		if self.roaming_open.is_selected():
			raise AssertionError("802.11r ROAMING feild is enabled .Traceback: %s " %traceback.format_exc())
		
		logger.debug("EditNetworkPage : Checking whether Mac Authentication feild is enabled")
		if not self.mac_authentication.get_selected()=='Enabled':
			raise AssertionError("Mac Authentication feild is disabled .Traceback: %s " %traceback.format_exc())
		self.buy_time()
		self.buy_time()
		logger.debug("EditNetworkPage : Checking whether Authentication Server feild is set to InternalServer")
		if not self.authentication_server.get_selected()=='InternalServer':
			raise AssertionError("Authentication Server feild is not set to InternalServer .Traceback: %s " %traceback.format_exc())

			
	def check_security_configurations_for_external_radius_server(self):
		self.buy_time()
		self.buy_time()
		logger.debug("EditNetworkPage : Checking whether external radius server1 is created")
		if not self.authentication_server.get_selected()=='authradius':
			raise AssertionError("External radius server1 is  not created .Traceback: %s " %traceback.format_exc())
			
	def edit_security_configurations_external_radiuds_server2(self):
		logger.debug("EditNetworkPage : Set Reauth Interval.")
		self.reauth_interval.set(self.config.config_vars.edit_reauth_interval)
		logger.debug("EditNetworkPage : Enable Uppercase Support.")
		self.open_uppercase_support.set(self.config.config_vars.Uppercase_Support_Enabled)
		logger.debug("EditNetworkPage : Set delimeter to :.")
		self.mac_auth_delimiter.set(self.config.config_vars.enterprise_delimeter)
		logger.debug("EditNetworkPage : calling _save_settings method...")
		self._save_settings()
		
	def check_security_configurations_for_external_radius_server2(self):
		logger.debug("EditNetworkPage : Checking whether Uppercase Support feild is enabled")
		if not self.open_uppercase_support.get_selected()=='Enabled':
			raise AssertionError("Uppercase Support feild is disabled .Traceback: %s " %traceback.format_exc())
		self.buy_time()
		self.buy_time()
		logger.debug("EditNetworkPage : Checking whether external radius server1 is created")
		if not self.authentication_server.get_selected()=='authradius':
			raise AssertionError("External radius server1 is  not created .Traceback: %s " %traceback.format_exc())
		self.buy_time()
		self.buy_time()
		logger.debug("EditNetworkPage : Checking whether external radius server2 is created")
		if not self.authentication_server_2.get_selected()=='testradius_2':
			raise AssertionError("External radius server2 is  not created .Traceback: %s " %traceback.format_exc())
		
			
	def set_besteffort_wmm_share(self):
		self.buy_time()
		logger.debug("EditNetworkPage : Set Best Effort wmm share to 100")
		self.besteffort_wmm_share.set(self.config.config_vars.edit_besteffort)
		
	def set_static_vlan(self):
		self.vlan_static.click()
		logger.debug('EditNetworkPage : Settings the vlan id value')
		self.vlanid.set(self.config.config_vars.vlan)
		
	def enable_mac_authentication(self):	
		logger.debug("EditNetworkPage : Enable Mac Authentication.")
		self.mac_authentication.set(self.config.config_vars.edit_Security_Mac_Authentication_Enabled)
		
	def check_security_configurations_for_two_external_radius_servers(self):
		logger.debug("EditNetworkPage : Checking whether Mac Authentication feild is enabled")
		if not self.mac_authentication.get_selected()=='Enabled':
			raise AssertionError("Mac Authentication feild is disabled .Traceback: %s " %traceback.format_exc())
		self.buy_time()
		self.buy_time()
		logger.debug("EditNetworkPage : Checking whether external radius server1 is created")
		if not self.authentication_server.get_selected()=='authradius':
			raise AssertionError("External radius server1 is  not created .Traceback: %s " %traceback.format_exc())
		self.buy_time()
		self.buy_time()
		logger.debug("EditNetworkPage : Checking whether external radius server2 is created")
		if not self.authentication_server_2.get_selected()=='testradius_2':
			raise AssertionError("External radius server2 is  not created .Traceback: %s " %traceback.format_exc())
			
	def select_internalserver(self):
		self.buy_time()
		self.buy_time()
		logger.debug("EditNetworkPage : Selecting  InternalServer for Authentication Server feild ")
		self.authentication_server.set(self.config.config_vars.edit_Authentication_server)
		self.buy_time()
		
	def checking_for_authentication_server2_visibility(self):
		logger.debug("EditNetworkPage : Checking whether authentication_server2 feild is visible")
		if self.authentication_server_2:
			raise AssertionError("authentication_server2 feild is visible .Traceback: %s " %traceback.format_exc())
		
		
	def set_besteffort_wmm_share_default(self):
		self.buy_time()
		logger.debug("EditNetworkPage : Set Best Effort wmm share to 0")
		self.besteffort_wmm_share.set(self.config.config_vars.edit_besteffort_default)
		
	def checking_for_authentication_server(self):	
		self.buy_time()
		self.buy_time()
		logger.debug("EditNetworkPage : Checking whether Authentication Server feild is set to InternalServer")
		if not self.authentication_server.get_selected()=='InternalServer':
			raise AssertionError("Authentication Server feild is not set to InternalServer .Traceback: %s " %traceback.format_exc())
			
	def edit_both_wpa_2_wpa_64passphrase_format(self):
		logger.debug("EditNetworkPage : Set Key Management to Both(WPA-2 & WPA) .")
		self.security_key_management.set(self.config.config_vars.Wpa2_WPA_Enterprise)
		logger.debug("EditNetworkPage : enable blacklisting.")
		self.blacklisting.set(self.config.config_vars.enabled)
		logger.debug("EditNetworkPage : disable mac authentication.")
		self.mac_authentication.set(self.config.config_vars.disabled)
		logger.debug("EditNetworkPage : Set Passphrase.")
		self.passphrase.set(self.config.config_vars.edit_Retype_auth_shared_key)
		logger.debug("EditNetworkPage : Set Re Passphrase.")
		self.retype_passphrase.set(self.config.config_vars.	edit_Retype_auth_shared_key)
		logger.debug("EditNetworkPage : Set passphrase format to 8-63 chars.")
		self.passphrase_format.set(self.config.config_vars.edit_passphrase_format_8)
		
		
	def set_video_wmm_share_default(self):
		self.buy_time()
		logger.debug("EditNetworkPage : Set video wmm share to 0")
		self.video_wmm_share.set(self.config.config_vars.edit_video_wmm_share)
		
	def checking_key_managementpassphrase_format(self):
		logger.debug("EditNetworkPage : Checking whether Key Management feild is set to Both(WPA-2 & WPA)")
		if not self.security_key_management.get_selected()=='Both(WPA-2 & WPA)':
			raise AssertionError("Key Management feild is set not to Both(WPA-2 & WPA) .Traceback: %s " %traceback.format_exc())
		logger.debug("EditNetworkPage : Checking whether blacklisting feild is Enabled")
		if not self.blacklisting.get_selected()=='Enabled':
			raise AssertionError("Blacklisting feild is Disabled .Traceback: %s " %traceback.format_exc())
			
		logger.debug("EditNetworkPage : Checking whether Mac Authentication feild is Disabled")
		if not self.mac_authentication.get_selected()=='Disabled':
			raise AssertionError("Mac Authentication feild is enabled .Traceback: %s " %traceback.format_exc())
		self.buy_time()
		
		logger.debug("EditNetworkPage : Checking whether passphrase format  is set to 8-63 chars")
		if not self.passphrase_format.get_selected()=='8-63 chars':
			raise AssertionError("passphrase format  is not set to 8-63 chars .Traceback: %s " %traceback.format_exc())
			
			
	def assert_broadcasefiltering_dtiminterval(self, broad, dtim):
		logger.debug("EditNetworkPage : Assert 'Broadcasefiltering' drop down value...")
		if not self.broadcasefiltering.get_selected() == broad:
			raise AssertionError("'Broadcasefiltering' drop down not set to '%s'.Traceback: %s " %(broad,traceback.format_exc()))
		logger.debug("EditNetworkPage : Assert 'Dtiminterval' drop down value...")
		if not self.dtiminterval.get_selected() == dtim:
			raise AssertionError("'Dtiminterval' drop down not set to '%s'.Traceback: %s " %(dtim,traceback.format_exc()))
			
	def check_static_wep_Tx_key(self):
		logger.debug("EditNetworkPage : Checking whether Key Management feild is set to Static WEP")
		if not self.security_key_management.get_selected()=='Static WEP':
			raise AssertionError("Key Management feild is set not to Static WEP .Traceback: %s " %traceback.format_exc())
			
		logger.debug("EditNetworkPage : Checking whether Mac Authentication feild is enabled")
		if not self.mac_authentication.get_selected()=='Enabled':
			raise AssertionError("Mac Authentication feild is disabled .Traceback: %s " %traceback.format_exc())
			
		logger.debug("EditNetworkPage : Checking whether Tx Key is set to 1")
		if not self.wep_key_index.get_selected()=='1':
			raise AssertionError("Tx Key is not set to 1 .Traceback: %s " %traceback.format_exc())
			
		logger.debug("EditNetworkPage : Checking whether WEP Key Size is set to 128-bit")
		if not self.wep_key_size.get_selected()=='128-bit':
			raise AssertionError("WEP Key Size is  not set to 128-bit .Traceback: %s " %traceback.format_exc())
			
	def edit_voice_wmm_share_default(self):
		self.buy_time()
		logger.debug("EditNetworkPage : Set voice wmm share to 0")
		self.voice_wmm_share.set(self.config.config_vars.edit_video_wmm_share)
	
	def edit_static_wep_network(self):
		logger.debug("EditNetworkPage : enable blacklisting.")
		self.blacklisting.set(self.config.config_vars.enabled)
		logger.debug("EditNetworkPage : set max_auth_failure value of to 5.")
		self.max_auth_failures.set(self.config.config_vars.max_auth_failures)
		logger.debug("EditNetworkPage : Enable Mac Authentication.")
		self.mac_authentication.set(self.config.config_vars.edit_Security_Mac_Authentication_Enabled)
		logger.debug("EditNetworkPage : set reauth interval value of to 3.")
		self.reauth_interval.set(self.config.config_vars.edit_reauth_intervals)
		logger.debug("EditNetworkPage : set value of reauth_unit  to hours.")
		self.reauth_unit.set(self.config.config_vars.reauth_unit_hrs)
		logger.debug("EditNetworkPage : set value of Tx Key to 4 .")
		self.wep_key_index.set(self.config.config_vars.tx4)
		self.buy_time()
		logger.debug('EditNetworkPage : Clicking on save Setting')
		self._save_settings()
		
	def check_static_network_changes(self):
		logger.debug("EditNetworkPage : Checking whether Key Management feild is set to Static WEP")
		if not self.security_key_management.get_selected()=='Static WEP':
			raise AssertionError("Key Management feild is set not to Static WEP .Traceback: %s " %traceback.format_exc())
			
		logger.debug("EditNetworkPage : Checking whether Mac Authentication feild is enabled")
		if not self.mac_authentication.get_selected()=='Enabled':
			raise AssertionError("Mac Authentication feild is disabled .Traceback: %s " %traceback.format_exc())
			
		logger.debug("EditNetworkPage : Checking whether Tx Key is set to 4")
		if not self.wep_key_index.get_selected()=='4':
			raise AssertionError("Tx Key is not set to 4 .Traceback: %s " %traceback.format_exc())
		
		logger.debug("EditNetworkPage : Checking whether blacklisting feild is Enabled")
		if not self.blacklisting.get_selected()=='Enabled':
			raise AssertionError("Blacklisting feild is Disabled .Traceback: %s " %traceback.format_exc())
			
	def check_wpa_blacklisting_enable(self):
		logger.debug("EditNetworkPage : Checking whether Key Management feild is set to WPA Personal")
		if not self.security_key_management.get_selected()=='WPA Personal':
			raise AssertionError("Key Management feild is set not to WPA Personal .Traceback: %s " %traceback.format_exc())
			
		logger.debug("EditNetworkPage : Checking whether blacklisting feild is Enabled")
		if not self.blacklisting.get_selected()=='Enabled':
			raise AssertionError("Blacklisting feild is Disabled .Traceback: %s " %traceback.format_exc())
		
		logger.debug("EditNetworkPage : Checking whether passphrase format  is set to 8-63 chars")
		if not self.passphrase_format.get_selected()=='8-63 chars':
			raise AssertionError("passphrase format  is not set to 8-63 chars .Traceback: %s " %traceback.format_exc())
			
	def edit_background_wmm_default(self):
		self.buy_time()
		logger.debug("EditNetworkPage : Set background_wmme to 0")
		self.background_wmm.set(self.config.config_vars.edit_video_wmm_share)
			
	def edit_wpa_blacklisting_disable(self):
		logger.debug("SecurityPage : Setting  max_auth_failure value to 0.")
		self.max_auth_failures.set(self.config.config_vars.max_auth_failure0)
		logger.debug("SecurityPage : Disable blacklisting.")
		self.blacklisting.set(self.config.config_vars.disabled)
		logger.debug("SecurityPage : Set passphrase format to 64 hexadecimal chars.")
		self.passphrase_format.set(self.config.config_vars.passphrase_format_64)
		logger.debug("SecurityPage : Setting 64 hexadecimal chars Passphrase.")
		self.passphrase.set(self.config.config_vars.passphrase)
		logger.debug("SecurityPage : Setting  Retype 64 hexadecimal chars Passphrase.")
		self.retype_passphrase.set(self.config.config_vars.passphrase)
		self.buy_time()
		logger.debug('EditNetworkPage : Clicking on save Setting')
		self._save_settings()
		
		
	def check_wpa_blacklisting_disable(self):
		logger.debug("EditNetworkPage : Checking whether Key Management feild is set to WPA Personal")
		if not self.security_key_management.get_selected()=='WPA Personal':
			raise AssertionError("Key Management feild is set not to WPA Personal .Traceback: %s " %traceback.format_exc())
			
		logger.debug("EditNetworkPage : Checking whether blacklisting feild is Disabled")
		if not self.blacklisting.get_selected()=='Disabled':
			raise AssertionError("Blacklisting feild is Enabled .Traceback: %s " %traceback.format_exc())
		
		logger.debug("EditNetworkPage : Checking whether passphrase format  is set to 64 hexadecimal chars")
		if not self.passphrase_format.get_selected()=='64 hexadecimal chars':
			raise AssertionError("passphrase format  is not set to 64 hexadecimal chars .Traceback: %s " %traceback.format_exc())
			
	def checking_key_wpa_2_and_wpa_64_passphrase_format(self):
		logger.debug("EditNetworkPage : Checking whether Key Management feild is set to Both(WPA-2 & WPA)")
		if not self.security_key_management.get_selected()=='Both(WPA-2 & WPA)':
			raise AssertionError("Key Management feild is set not to Both(WPA-2 & WPA) .Traceback: %s " %traceback.format_exc())
		logger.debug("EditNetworkPage : Checking whether 802.11r ROAMING feild is enabled")
		if not self.roaming_open.is_selected():
			raise AssertionError("802.11r ROAMING feild is disabled .Traceback: %s " %traceback.format_exc())
			
		logger.debug("EditNetworkPage : Checking whether Mac Authentication feild is Disabled")
		if not self.mac_authentication.get_selected()=='Enabled':
			raise AssertionError("Mac Authentication feild is enabled .Traceback: %s " %traceback.format_exc())
		self.buy_time()
		
		logger.debug("EditNetworkPage : Checking whether passphrase format  is set to 8-63 chars")
		if not self.passphrase_format.get_selected()=='64 hexadecimal chars':
			raise AssertionError("passphrase format  is not set to 64 hexadecimal chars .Traceback: %s " %traceback.format_exc())
		
	def edit_advance_options(self,uplink=False,max_threshold=False,hide_ssid=False,timeout=False,disable_ssid=False,hide_ssid_uncheck=False,local_probe=False,disable_ssid_uncheck=False):
		logger.debug('EditNetworkPage : Clicking advanced Setting accordion')
		self.click_advanced_settings_accordion()
		if hide_ssid:
			logger.debug('EditNetworkPage : Enable hide ssid.')
			self.hide_ssid.click()
		if timeout:
			logger.debug('EditNetworkPage : Edit Inactivity timeout.')
			self.inactivity_timeout.set(self.config.config_vars.default_inactivity_timeout)
		if disable_ssid:
			logger.debug('EditNetworkPage : Enable disable ssid.')
			self.disable_ssid.click()
		if hide_ssid_uncheck:
			logger.debug('EditNetworkPage : Disable hide ssid.')
			self.hide_ssid.click()
		if local_probe:
			logger.debug("EditNetworkPage: Set LOCAL PROBE REQUEST THRESHOLD.")		
			self.localprobe.set(self.config.config_vars.localprobe_request_threshold)
		if disable_ssid_uncheck:
			logger.debug('EditNetworkPage : Disable disable ssid.')
			self.disable_ssid.click()
		

	def open_security_accordion(self):
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.security_accordion.click()
		
			
	def edit_security_settings(self,okc=False):
		if okc :
			logger.debug('EditNetworkPage : disable okc')
			self.okc_checkbox.click()
		logger.debug("EditNetworkPage : calling _save_settings method...")
		self._save_settings()
		
	def configure_mac_authentication(self,enable=False):
		if enable:
			logger.debug('EditNetworkPage : Enable mac authentication.')
			self.mac_authentication.set(self.config.config_vars.enable_option)
		else:
			logger.debug('EditNetworkPage : Disable mac authentication.')
			self.mac_authentication.set(self.config.config_vars.disable_option)
			
	def create_external_radius_server_in_auth_server_one(self):
		'''
		Create new external radius in auth server 1 
		'''
		logger.debug('EditNetworkPage : Setting new external server to Authentication Server 1')
		self.authentication_server.set(self.config.config_vars.new_external_server)
		logger.debug('EditNetworkPage : Entering details')
		self.auth_server_name.set(self.config.config_vars.auth_server_value)
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr_value)
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey_value)
		self.Retype_auth_shared_key.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug('EditNetworkPage : Saving external radius server')
		self.save_server.click()

	def assert_security_level(self,enterprise=False,open=False):
		'''
		Assert security level 
		If enterprise true : Check if enterprise is enabled.
		If open true : Check if open is enabled.
		default : Check if personal is enabled.
		'''
		logger.debug('EditNetworkPage : Clicking security accordion')
		self.open_security_accordion()
		if enterprise:
			logger.debug("EditNetworkPage : Check if enterprise is enabled.")
			if not self.security_enterprise.is_selected():
				raise AssertionError("Enterprise is not enabled.Traceback: %s " %traceback.format_exc())
		elif open:
			logger.debug("EditNetworkPage : Check if open is enabled.")
			if not self.security_open.is_selected():
				raise AssertionError("Open is not enabled.Traceback: %s " %traceback.format_exc())		
		else:
			logger.debug("EditNetworkPage : Check if personal is enabled.")
			if not self.security_personal.is_selected():
				raise AssertionError("Personal is not enabled.Traceback: %s " %traceback.format_exc())
			
	def assert_auth_server_settings(self,accounting_enable=False,acc_interval=False,balancing=False,auth_survivability=False,okc=False,blacklisting=False,max_auth_failures=False, termination_disable=False, termination_enable=False):
		'''
		Check if accounting,balancing,auth_survivability is eneabled.
		Check if okc is disabled
		'''
		if accounting_enable:
			logger.debug("EditNetworkPage :Check if accounting is enabled.")
			if not self.accounting_dropdown.get_selected() == self.config.config_vars.enabled:
				raise AssertionError("Accounting is not enabled.Traceback: %s " %traceback.format_exc())
			if acc_interval:
				logger.debug('EditNetworkPage :Check accounting interval value.')
				if not self.account_interval.get() == self.config.config_vars.edit_accounting_interval :
					raise AssertionError("Acoouting interval mismatch.Traceback: %s " %traceback.format_exc())
		if balancing:
			logger.debug("EditNetworkPage :Check if load balancing is enabled.")
			if not self.load_balancing_dropdown.get_selected() == self.config.config_vars.enabled:
				raise AssertionError("Balancing is not enabled.Traceback: %s " %traceback.format_exc())
			
			
		if auth_survivability:
			logger.debug("EditNetworkPage :Check if auth survivability is enable.")
			if not self.auth_survivability.get_selected() == self.config.config_vars.enabled:
				raise AssertionError("Auth survivability is not enabled.Traceback: %s " %traceback.format_exc())
	
		if okc:
			logger.debug("EditNetworkPage :Check if okc is disabled.")
			if self.okc_checkbox.is_selected():
				raise AssertionError("EditNetworkPage : Okc is not disabled.Traceback: %s " %traceback.format_exc())
				
		if termination_disable:
			logger.debug("EditNetworkPage :Check if termination is disabled.")
			if not self.security_termination.get_selected() == self.config.config_vars.disabled:
				raise AssertionError("EditNetworkPage : termination is not disabled.Traceback: %s " %traceback.format_exc())
				
		if termination_enable:
			logger.debug("EditNetworkPage :Check if termination is enabled.")
			if not self.security_termination.get_selected() == self.config.config_vars.enabled:
				raise AssertionError("EditNetworkPage : termination is not enabled.Traceback: %s " %traceback.format_exc())
		
		if blacklisting:
			logger.debug("EditNetworkPage :Check if blacklisting is enabled.")
			if not self.blacklisting.get_selected() == self.config.config_vars.enabled:
				raise AssertionError("blacklisting is not enabled.Traceback: %s " %traceback.format_exc())
			if max_auth_failures:
				logger.debug('EditNetworkPage :Check max auth failure value.')
				if not self.max_auth_failures.get() == self.config.config_vars.edit_max_auth_failures:
					raise AssertionError("max auth failure interval mismatch.Traceback: %s " %traceback.format_exc())
				
		
			
	def assert_external_radius_auth_server_one(self):
		'''
		Check if auth server 1 is external radius.
		'''
		self.buy_time()
		self.buy_time()
		logger.debug("EditNetworkPage :Check if auth server 1 is external radius.")		
		if not self.authentication_server.get_selected() == self.config.config_vars.auth_server_value:
			raise AssertionError("EditNetworkPage: Authentication Server 1 is not set to external server .Traceback: %s " %traceback.format_exc())
		
	def assert_external_radius_auth_server_two(self):
		'''
		Check if auth server 2 is external radius.
		'''
		self.buy_time()
		self.buy_time()
		if not self.authentication_server_2.get_selected() == self.config.config_vars.auth_server_value_2:
			raise AssertionError("EditNetworkPage: Authentication Server 2 is not set to external server .Traceback: %s " %traceback.format_exc())
	
	def assert_edited_advance_options(self,uplink=False,max_threshold=False,without_uplink=False):
		self.click_advanced_settings_accordion()
		if uplink:
			logger.debug("EditNetworkPage: Check 'can be used without uplink is enabled.")
			if not self.without_uplink.is_selected():
				raise AssertionError("EditNetworkPage: Can be used without uplink is disabled.Traceback: %s " %traceback.format_exc())
		elif max_threshold:
			logger.debug("EditNetworkPage: Check whether max client threshold matches with pushed config .")		
			if not self.max_client_threshold.get() == self.config.config_vars.max_client_threshold:
				raise AssertionError("EditNetworkPage: Max client threshold is not equal to pushed config.Traceback: %s " %traceback.format_exc())		
		else:
			logger.debug("EditNetworkPage: Check whether inactivity timeout matches with pushed config .")		
			if not self.inactivity_timeout.get() == self.config.config_vars.valid_inactivity_timeout:
				raise AssertionError("EditNetworkPage: Max client threshold is not equal to pushed config.Traceback: %s " %traceback.format_exc())
			
	def configure_auth_server_settings(self,accounting_disable=False,acc_interval=False,balancing=False,auth_survivability=False,roaming=False,okc=False,termination_disable=False,accounting_enable=False,termination_enable=False):
		if accounting_disable:
			logger.debug("EditNetworkPage :Disable accounting")
			self.accounting_dropdown.set(self.config.config_vars.disable_option)
# 			if acc_interval:
# 				logger.debug('EditNetworkPage :Set Accouting Interval.')
# 				self.account_interval.set(self.config.config_vars.edit_accounting_interval)

		if balancing:
			logger.debug("EditNetworkPage :Disable load balancing.")
			self.load_balancing_dropdown.set(self.config.config_vars.disable_option)
			
		if auth_survivability:
			logger.debug("EditNetworkPage :Disable auth survivability.")
			self.auth_survivability.set(self.config.config_vars.disable_option)
			
		if roaming:
			if self.roaming_open.is_selected():
				logger.debug("EditNetworkPage : Disable 802.11r ROAMING.")
				self.roaming_open.click()
			# self.selected_roaming_dropdown.set(self.config.config_vars.disable_option)
			
		if okc:
			logger.debug("EditNetworkPage : Enable OKC .")
			self.okc_checkbox.click()
			
		if termination_disable:
			logger.debug("EditNetworkPage : Disable termination.")
			self.security_termination.set(self.config.config_vars.disable_option)
			
		if termination_enable:
			logger.debug("EditNetworkPage : Enable termination.")
			self.security_termination.set(self.config.config_vars.enable_option)
			
		if accounting_enable:
			logger.debug("EditNetworkPage :Enable accounting")
			self.accounting_dropdown.set(self.config.config_vars.enable_option)
			if acc_interval:
				logger.debug('EditNetworkPage :Set Accouting Interval.')
				self.account_interval.set(self.config.config_vars.edit_accounting_interval)
		self.buy_time()
		logger.debug('EditNetworkPage : Clicking on Save Setting')
		self._save_settings()
		
	def set_band_default(self):
		self.buy_time()
		logger.debug("EditNetworkPage : Set Band to All")
		self.band.set(self.config.config_vars.edit_band_all)
		
	def checking_for_band_all(self):	
		logger.debug("EditNetworkPage : Checking whether Band feild is set to ALL")
		if not self.band.get_selected()=='All':
			raise AssertionError("Band feild is not set to ALL.Traceback: %s " %traceback.format_exc())
			
	def edit_network_wpa_2_personal(self):
		logger.debug("EditNetworkPage : Set Key Management to WPA-2 Personal .")
		self.security_key_management.set(self.config.config_vars.wpa_2_personal)
		logger.debug("EditNetworkPage : Set Passphrase.")
		self.passphrase.set(self.config.config_vars.Network_Passphrase)
		logger.debug("EditNetworkPage : Set retype Passphrase.")
		self.retype_passphrase.set(self.config.config_vars.Network_Passphrase)
		
		
		
	def checking_for_wep_key_visibility(self):	
		logger.debug("EditNetworkPage : Checking whether wep key feild is present")
		if self.wep_key:
			raise AssertionError("wep key feild is present.Traceback: %s " %traceback.format_exc())
			
	def checking_network_wpa_2_personal(self):
		logger.debug("EditNetworkPage : Checking whether Key Management feild is set to WPA-2 Personal")
		if not self.security_key_management.get_selected()=='WPA-2 Personal':
			raise AssertionError("Key Management feild is set not to WPA-2 Personal .Traceback: %s " %traceback.format_exc())
		self.checking_for_wep_key_visibility()
		
	def enable_content_filtering(self):
		self.buy_time()
		logger.debug("EditNetworkPage : Enable content_filtering")
		self.content_filtering_dropdown.set(self.config.config_vars.enabled)
		
	def enable_optimization_feilds(self):
		logger.debug("EditNetworkPage : Enable Dynamic Multicast Optimization")
		self.multicastratetransmission.set(self.config.config_vars.enabled)
		logger.debug("EditNetworkPage : Enable Multicast Transmission Optimization")
		self.dynamicmulticast.set(self.config.config_vars.enabled)
		logger.debug("EditNetworkPage : Set DMO Channel Utilization Threshold to 1")
		self.channelutilizationthresh.set(self.config.config_vars.channelutilizationthresh)
		
	def edit_personal_employee_network_with_dynamic_multicast_optimization(self):
		logger.debug("EditNetworkPage :Enable accounting")
		self.accounting_dropdown.set(self.config.config_vars.enabled)
		logger.debug('EditNetworkPage :Set Accouting Interval.')
		self.account_interval.set(self.config.config_vars.edit_accounting_interval60)
		logger.debug("EditNetworkPage :Enable load balancing")
		self.load_balancing_dropdown.set(self.config.config_vars.enabled)
		logger.debug("EditNetworkPage :Disable uppercase support")
		self.open_uppercase_support.set(self.config.config_vars.disabled)
		logger.debug("EditNetworkPage : Set delimeter to /.")
		self.mac_auth_delimiter.set(self.config.config_vars.edit_personal_delimeter)
		self.buy_time()
		logger.debug('EditNetworkPage : Clicking on Save Setting')
		self._save_settings()
		
	def check_enable_optimization_feilds(self):
		logger.debug("EditNetworkPage : Checking whether Dynamic Multicast Optimization feild is Enabled")
		if not self.multicastratetransmission.get_selected()=='Enabled':
			raise AssertionError("Dynamic Multicast Optimization feild is disabled .Traceback: %s " %traceback.format_exc())
			
		logger.debug("EditNetworkPage : Checking whether Multicast Transmission Optimization feild is Enabled")
		if not self.dynamicmulticast.get_selected()=='Enabled':
			raise AssertionError("Multicast Transmission Optimization feild is disabled .Traceback: %s " %traceback.format_exc())
			
	def check_personal_employee_network_with_dynamic_multicast_optimization(self):	
		logger.debug("EditNetworkPage : Checking whether accounting is Enabled")
		if not self.accounting_dropdown.get_selected()=='Enabled':
			raise AssertionError("accounting feild is disabled .Traceback: %s " %traceback.format_exc())
			
		logger.debug("EditNetworkPage : Checking whether load balancing feild is Enabled")
		if not self.load_balancing_dropdown.get_selected()=='Enabled':
			raise AssertionError("load balancing feild is disabled .Traceback: %s " %traceback.format_exc())
			
		logger.debug("EditNetworkPage : Checking whether uppercase support feild is Disabled")
		if not self.open_uppercase_support.get_selected()=='Disabled':
			raise AssertionError("Uppercase support feild is disabled .Traceback: %s " %traceback.format_exc())
			
	def set_localprobe_feilds(self):
		logger.debug("EditNetworkPage : Set localprobe feildsd to 100")
		self.localprobe.set(self.config.config_vars.edit_localprobe)
		
	def enable_auth_server_settings(self,accounting=False,acc_interval=False,balancing=False,auth_survivability=False,roaming=False,okc=False,blacklisting=False,max_auth_failures=False, termination=False):
		if accounting:
			logger.debug("EditNetworkPage :Enable accounting")
			self.accounting_dropdown.set(self.config.config_vars.enabled)
			if acc_interval:
				logger.debug('EditNetworkPage :Set Accouting Interval.')
				self.account_interval.set(self.config.config_vars.edit_accounting_interval)

		if balancing:
			logger.debug("EditNetworkPage :Enable load balancing.")
			self.load_balancing_dropdown.set(self.config.config_vars.enabled)
			
		if auth_survivability:
			logger.debug("EditNetworkPage :Enable auth survivability.")
			self.auth_survivability.set(self.config.config_vars.enabled)
			
		if blacklisting:
			logger.debug("EditNetworkPage :Enable blacklisting")
			self.blacklisting.set(self.config.config_vars.enabled)
			if max_auth_failures:
				logger.debug('EditNetworkPage :Set Check max auth failure value.')
				self.max_auth_failures.set(self.config.config_vars.edit_max_auth_failures)
			
		if roaming:
			logger.debug("EditNetworkPage : Enable 802.11r ROAMING.")
			self.selected_roaming_dropdown.set(self.config.config_vars.enabled)
			
		if okc:
			logger.debug("EditNetworkPage : Enable OKC .")
			self.okc_checkbox.click()
		
		if termination:
			logger.debug("EditNetworkPage :Enable Termination.")
			self.security_termination.set(self.config.config_vars.enabled)
			
	def edit_enterprise_employee_network_with_disabled_ssid(self):
		logger.debug("EditNetworkPage :Disable termination")
		self.security_termination.set(self.config.config_vars.disabled)
		logger.debug("EditNetworkPage :Enable accounting")
		self.accounting_dropdown.set(self.config.config_vars.enabled)
		logger.debug('EditNetworkPage :Set Accouting Interval.')
		self.account_interval.set(self.config.config_vars.edit_accounting_interval60)
		
		
	def check_disable_ssid_checkbox(self,flag):
		self.click_advanced_settings_accordion()
		if flag == 'check' :
			logger.debug("EditNetworkPage :Check if disable ssid is enabled.")
			if not self.disable_ssid.is_selected():
				raise AssertionError("EditNetworkPage : disable ssid is not enabled.Traceback: %s " %traceback.format_exc())
		elif flag == 'uncheck':
			logger.debug("EditNetworkPage :Check if disable ssid is disabled.")
			if self.disable_ssid.is_selected():
				raise AssertionError("EditNetworkPage : disable ssid is not disabled.Traceback: %s " %traceback.format_exc())
		
	def uncheck_disable_ssid(self):
		logger.debug("EditNetworkPage :Uncheck disable ssid ")
		if self.disable_ssid.is_selected():
			logger.debug("EditNetworkPage :Uncheck disable ssid ")
			self.disable_ssid.click()
			
	def set_advance_settings_and_reauth_interval(self):
		self.click_advanced_settings_accordion()
		logger.debug('EditNetworkPage : Disable Can be used without uplink')
		self.without_uplink.click()
		logger.debug('EditNetworkPage : Clicking security accordion')
		self.security_accordion.click()
		logger.debug("EditNetworkPage : Set auth interval time.")		
		self.reauth_interval.set(self.config.config_vars.edit_reauth_interval)
		logger.debug("EditNetworkPage : Set reauth unit.")	
		self.reauth_unit.set('hrs.')
		self.buy_time()
		logger.debug('EditNetworkPage : Clicking on Save Setting')
		self._save_settings()
		self.buy_time()
		
	def check_advance_settings_and_reauth_interval(self):
		self.click_advanced_settings_accordion()
		logger.debug("EditNetworkPage :Check if Can be used without uplink is disabled.")
		if self.without_uplink.is_selected():
			raise AssertionError("EditNetworkPage : Can be used without uplink is not disabled.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking security accordion')
		self.security_accordion.click()
		logger.debug('EditNetworkPage :Check reauth interval value is set to 3 hours.')
		if not self.reauth_interval.get() == self.config.config_vars.edit_reauth_interval :
			raise AssertionError("Acoouting interval mismatch.Traceback: %s " %traceback.format_exc())
		logger.debug("EditNetworkPage : Checking whether reauth_unit feild is set to hrs")
		if not self.reauth_unit.get_selected()=='hrs.':
			raise AssertionError("reauth unit feild is not set to hrs .Traceback: %s " %traceback.format_exc())
			
	def change_content_filtering(self):
		'''
			Changing content filtering to disabled
		'''
		logger.debug('EditNetworkPage : Clicking on advanced settings accordion')
		self.advance_settings_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Disabling content filtering')
		self.content_filtering_dropdown.set(self.config.config_vars.content_filtering_disabled)
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(20)
		
	def change_key_management(self):
		'''
			Changing Key management to WPA-Personal
		'''
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.security_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Disabling content filtering')
		self.security_key_management.set(self.config.config_vars.key_management_value)
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(20)
		
	def assert_content_filtering_key_management_changes(self):
		'''
			Asserting content filtering and key management
		'''
		logger.debug('EditNetworkPage : Clicking on advanced settings accordion')
		self.advance_settings_accordion.click()
		time.sleep(5)
		if not self.content_filtering_dropdown.get_selected() == self.config.config_vars.content_filtering_disabled:
			raise AssertionError("Content filtering is not set to disabled.Traceback: %s " %traceback.format_exc())
		
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.security_accordion.click()
		time.sleep(7)
		if not self.security_key_management.get_selected() == self.config.config_vars.key_management_value:
			raise AssertionError("Key Management is not set to WPA-Personal.Traceback: %s " %traceback.format_exc())

		logger.debug('EditNetworkPage : Clicking on Network link')
		self.networks.click()
		time.sleep(5)
		
	def change_advanced_band_settings(self):
		'''
			Setting band value 2.4 GHz
		'''
		logger.debug('EditNetworkPage : Clicking on advanced settings accordion')
		self.advance_settings_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Setting band value to 2.4 GHz')
		self.band.set(self.config.config_vars.band_value)
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(20)
		
	def change_key_management_to_both_wpa2_wpa_personal(self):
		'''
			Setting key-management to both wpa2 and wpa personal and enabling mac authentication
		'''
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.security_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Setting key-management to both wpa2 and wpa personal')
		self.security_key_management.set(self.config.config_vars.new_key_management_value)
		logger.debug('EditNetworkPage : Setting mac authentication enabled')
		self.mac_authentication.set(self.config.config_vars.mac_authentication_value)
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(20)
		
	def assert_band_key_management_mac_auth_changes(self):
		'''
			Asserting band,key management,mac authentication changes
		'''
		logger.debug('EditNetworkPage : Clicking on advanced settings accordion')
		self.advance_settings_accordion.click()
		time.sleep(5)
		if not self.band.get_selected() == self.config.config_vars.band_value:
			raise AssertionError("Band value is not set to 2.4 GHz.Traceback: %s " %traceback.format_exc())			
		
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.security_accordion.click()
		time.sleep(7)
		if not self.security_key_management.get_selected() == self.config.config_vars.new_key_management_value:
			raise AssertionError("Key Management is not set to both wpa2 and wpa personal.Traceback: %s " %traceback.format_exc())
		if not self.mac_authentication.get_selected() == self.config.config_vars.mac_authentication_value:
			raise AssertionError("Mac authentication is not set to enabled.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Network link')
		self.networks.click()
		time.sleep(5)
		
	def edit_disable_ssid_auth_server_termination(self):
		'''
			Enabling disabled ssid, Authentication Server 2, Termination 
		'''
		logger.debug('EditNetworkPage : Clicking on advanced settings accordion')
		self.advance_settings_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Disabling disabled ssid')
		self.disable_ssid.click()
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.security_accordion.click()
		time.sleep(15)
		logger.debug('EditNetworkPage : Setting new external server to Authentication Server 2')
		self.authentication_server_2.set(self.config.config_vars.new_external_server)
		time.sleep(3)
		logger.debug('EditNetworkPage : Entering details')
		self.auth_server_name.set(self.config.config_vars.auth_server_value_2)
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr_value)
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey_value)
		self.Retype_auth_shared_key.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug('SecurityPage : Saving external radius server')
		self.save_server.click()
		time.sleep(12)
		logger.debug('EditNetworkPage : Enabling security termination')
		self.security_termination.set(self.config.config_vars.termination_enabled)
		if self.accounting_dropdown:
			raise AssertionError("Accounting dropdown is not visible.Traceback: %s " %traceback.format_exc())			
		if self.account_interval:
			raise AssertionError("Accounting interval is not visible.Traceback: %s " %traceback.format_exc())			
		if self.auth_survivability:
			raise AssertionError("Auth survivability is not visible.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(30)
		
	def assert_disable_ssid_auth_server_termination_changes(self):
		'''
			Asserting disable ssid, auth server, termination changes
		'''	
		logger.debug('EditNetworkPage : Clicking on advanced settings accordion')
		self.advance_settings_accordion.click()
		time.sleep(5)
		if self.disable_ssid.is_selected():
			raise AssertionError("Disable ssid checkbox is not checked.Traceback: %s " %traceback.format_exc())				
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.security_accordion.click()
		time.sleep(20)
		if not self.authentication_server_2.get_selected() == self.config.config_vars.auth_server_value_2:
			raise AssertionError("Auth server 2 is not set to external server.Traceback: %s " %traceback.format_exc())				
		if not self.security_termination.get_selected() == self.config.config_vars.termination_enabled:
			raise AssertionError("Edit termination is not set to enabled.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Network link')
		self.networks.click()
		time.sleep(5)
		
	def assert_key_management_reauth_interval_use_session_key_changes(self):
		logger.debug('EditNetworkPage : Clicking on advanced settings accordion')
		self.advance_settings_accordion.click()
		time.sleep(5)
		if not self.without_uplink.is_selected():
			raise AssertionError("Can be used without uplink checkbox is not checked.Traceback: %s " %traceback.format_exc())			
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.security_accordion.click()
		if not self.security_enterprise.is_selected():
			raise AssertionError("Enterprise radio button is not selected.Traceback: %s " %traceback.format_exc())			
		if not self.security_key_management.get_selected() == self.config.config_vars.key_management_dynamic:
			raise AssertionError("Key Management is not set to Dynamic WEP.Traceback: %s " %traceback.format_exc())				
		if not self.use_session_key.is_selected():
			raise AssertionError("Use session key for LEAP is not set to enabled.Traceback: %s " %traceback.format_exc())
		if not self.reauth_interval.get() == '10':
			raise AssertionError("Reauth interval is not set 10.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Network link')
		self.networks.click()
		time.sleep(5)
		
	def edit_reauth_interval_session_key_with_advanced_settings(self):
		'''
			Settings reauth interval, use session key for leap
		'''
		logger.debug('EditNetworkPage : Clicking on advanced settings accordion')
		self.advance_settings_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Disabling can be used without uplink')
		self.without_uplink.click()
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.security_accordion.click()
		logger.debug('EditNetworkPage : Setting reauth interval 3 hr')
		self.reauth_interval.set('3')
		self.reauth_unit.set(self.config.config_vars.reauth_unit_hrs)
		logger.debug('EditNetworkPage : Disabling Use Session key for LEAP')
		self.use_session_key.click()
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(30)
		
		
	def assert_reauth_interval_session_key_with_advanced_settings_changes(self):
		'''
			Asserting changes : Reauth interval, Use session key for leap
		'''
		logger.debug('EditNetworkPage : Clicking on advanced settings accordion')
		self.advance_settings_accordion.click()
		time.sleep(5)
		if self.without_uplink.is_selected():
			raise AssertionError("CAN BE USED WITHOUT UPLINK is selected.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.security_accordion.click()
		if not self.reauth_interval.get() == '180':
			raise AssertionError("Reauth interval is not set to 180.Traceback: %s " %traceback.format_exc())
		if not self.reauth_unit.get_selected() == 'min.':
			raise AssertionError("Reauth interval unit is not set to hrs.Traceback: %s " %traceback.format_exc())
		if self.use_session_key.is_selected():
			raise AssertionError("Use session key for LEAP is selected.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Network link')
		self.networks.click()
		time.sleep(5)
		
	def set_max_client_threshold(self,value):	
		'''
			Setting max client threshold to 255
		'''	
		logger.debug('EditNetworkPage : Clicking on advanced settings accordion')
		self.advance_settings_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Entering invalid value in MAX Client Threashold ')
		self.max_client_threshold.set(self.config.config_vars.invalid_max_client_threshold)
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(6)
		if not self.max_client_threshold_error:
			raise AssertionError("Max Client Threshold error is not visible.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Entering valid value in MAX Client Threashold ')
		self.max_client_threshold.set(value)
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(20)
		
	def set_delimiter_uppercase_support_mac_auth_options(self):
		'''
			Settings delimiter option, uppercase support and mac authentications options
		'''	
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.security_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Enabling mac authentication options')		
		self.mac_authentication_enterprise.click()
		self.auth_failthru_enterprise.click()
		logger.debug('EditNetworkPage : Setting delimiter option to :')
		self.mac_auth_delimiter.set(self.config.config_vars.enterprise_delimeter)
		logger.debug('EditNetworkPage : Editing Uppercase support option')
		self.open_uppercase_support.set(self.config.config_vars.uppercase_support_value_enabled)
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(20)
		
	def assert_delimiter_uppercase_support_mac_auth_options_check(self):
		'''
			Assert delimiter option, uppercase support and mac authentications options
		'''	
		logger.debug('EditNetworkPage : Clicking on advanced settings accordion')
		self.advance_settings_accordion.click()
		time.sleep(5)
		if not self.max_client_threshold.get() == self.config.config_vars.valid_max_client_threshold_value:
			raise AssertionError("Max Client Threshold is not set to 255.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.security_accordion.click()
		time.sleep(5)
		if not self.mac_authentication_enterprise.is_selected():
			raise AssertionError("Perform MAC authentication is not checked.Traceback: %s " %traceback.format_exc())
		if not self.auth_failthru_enterprise.is_selected():
			raise AssertionError("MAC authentication fail-thru is not checked.Traceback: %s " %traceback.format_exc())
		if not self.mac_auth_delimiter.get() == self.config.config_vars.enterprise_delimeter:
			raise AssertionError("Delimiter option is not set to :.Traceback: %s " %traceback.format_exc())
		if not self.open_uppercase_support.get_selected() == self.config.config_vars.uppercase_support_value_enabled:
			raise AssertionError("Uppercase support is not set to enabled.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Network link')
		self.networks.click()
		time.sleep(5)
		
	def set_blacklisting_uppercase_support_delimiter_options(self):
		'''
			Setting blacklisting, uppercase support, delimiter options
		'''
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.security_accordion.click()
		time.sleep(4)
		logger.debug('EditNetworkPage : Enabling blacklisting option')
		self.blacklisting.set(self.config.config_vars.blacklisting_value)
		logger.debug('EditNetworkPage : Setting delimiter option to blank')
		self.mac_auth_delimiter.set('')
		logger.debug('EditNetworkPage : Editing Uppercase support option')
		self.open_uppercase_support.set(self.config.config_vars.uppercase_support_disabled)
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(20)
		
	def assert_blacklisting_uppercase_support_delimiter_changes(self):
		'''
			Asserting blacklisting, uppercase support, delimiter options
		'''
		logger.debug('EditNetworkPage : Clicking on advanced settings accordion')
		self.advance_settings_accordion.click()
		time.sleep(5)
		if not self.max_client_threshold.get() == '0':
			raise AssertionError("Max Client Threshold is not set to 255.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.security_accordion.click()
		if not self.blacklisting.get_selected() == self.config.config_vars.blacklisting_value:
			raise AssertionError("Blacklisting dropdown is not set to enabled .Traceback: %s " %traceback.format_exc())
		if not self.open_uppercase_support.get_selected() == self.config.config_vars.uppercase_support_disabled:
			raise AssertionError("Uppercase support dropdown is not set to disabled .Traceback: %s " %traceback.format_exc())
		if not self.mac_auth_delimiter.get() == '':
			raise AssertionError("Delimiter is not set to blank.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Network link')
		self.networks.click()
		time.sleep(5)
		
	def set_local_probe_request(self,value):
		'''
			Setting local probe request to 100
		'''	
		logger.debug('EditNetworkPage : Clicking on advanced settings accordion')
		self.advance_settings_accordion.click()
		time.sleep(5)
		logger.debug('EditNetworkPage : Entering invalid value in local probe request')
		self.localprobe.set('1000')
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(6)
		if not self.local_probe_req_error:
			raise AssertionError("Local Probe Request error is not visible.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Entering valid value in local probe request')
		self.localprobe.set(value)
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(20)
		
		
	def set_auth_server_loadbalancing_max_auth_failure(self):
		'''
			Setting auth servers, load balancing, max authentication failure
		'''
		time.sleep(20)
		logger.debug('EditNetworkPage : Clicking on Security accordion')
		self.security_accordion.click()
		time.sleep(20)
		if not self.authentication_server:
			self.security_accordion.click()
		time.sleep(20)
		logger.debug('EditNetworkPage : Setting new external server')
		self.authentication_server.set(self.config.config_vars.new_external_server)
		time.sleep(3)
		logger.debug('EditNetworkPage : Entering details')
		self.auth_server_name.set(self.config.config_vars.auth_server_value)
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr_value)
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey_value)
		self.Retype_auth_shared_key.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug('EditNetworkPage : Saving external radius server')
		self.save_server.click()
		time.sleep(12)
		logger.debug('SecurityPage : Setting new external server to Authentication Server 2')
		self.authentication_server_2.set(self.config.config_vars.new_external_server)
		time.sleep(3)
		logger.debug('SecurityPage : Entering details')
		self.auth_server_name.set(self.config.config_vars.auth_server_value_2)
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr_value)
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey_value)
		self.Retype_auth_shared_key.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug('SecurityPage : Saving external radius server')
		self.save_server.click()
		time.sleep(12)
		logger.debug('EditNetworkPage : Enabling blacklisting option')
		self.blacklisting.set(self.config.config_vars.blacklisting_value)
		logger.debug('EditNetworkPage : Changing max authentication value to 10')
		self.max_auth_failures.set(self.config.config_vars.max_authentication_ten)
		logger.debug('EditNetworkPage : Enabling load balancing')
		self.load_balancing_dropdown.set(self.config.config_vars.load_balancing_enabled)
		logger.debug('EditNetworkPage : Clicking on Save settings')
		self.save_settings.click()
		time.sleep(20)
		
	def assert_auth_server_loadbalancing_max_auth_failure(self):
		'''
			Asserting auth servers, load balancing, max authentication failure
		'''	
		logger.debug('EditNetworkPage : Clicking on advanced settings accordion')
		self.advance_settings_accordion.click()
		time.sleep(5)
		if not self.localprobe.get() == '100':
			raise AssertionError("Local Probe Request is not set to 100.Traceback: %s " %traceback.format_exc())			
		logger.debug('EditNetworkPage : Clicking on Security accordion')
		self.security_accordion.click()
		time.sleep(20)
		if not self.authentication_server.get_selected() == self.config.config_vars.auth_server_value:
			raise AssertionError("Auth server 1 is not set to external server.Traceback: %s " %traceback.format_exc())
		if not self.authentication_server_2.get_selected() == self.config.config_vars.auth_server_value_2:
			raise AssertionError("Auth server 2 is not set to external server.Traceback: %s " %traceback.format_exc())
		if not self.load_balancing_dropdown.get_selected() == self.config.config_vars.load_balancing_enabled:
			raise AssertionError("Load balancing is not set to enabled.Traceback: %s " %traceback.format_exc())
		if not self.max_auth_failures.get() == self.config.config_vars.max_authentication_ten:
			raise AssertionError("Max auth failure is not set to 10.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Network link')
		self.networks.click()
		time.sleep(5)
		
		
		
		
		
		
	def click_on_security_accordion(self):
		'''
			Clicking on security accordion
		'''
		logger.debug('EditNetworkPage : Clicking on Security accordion')
		self.security_accordion.click()
		if not self.passphrase:
			logger.debug("EditNetworkPage : clicking 'Security' accordion...")
			self.security_accordion.click()
			time.sleep(50)
		
	def click_on_advanced_settings_accordion(self):
		'''
			Clicking on advanced settings accordion
		'''
		logger.debug('EditNetworkPage : Clicking on advanced settings accordion')
		self.advance_settings_accordion.click()
		time.sleep(5)
		
	def set_mac_authentication_options(self):
		'''
			Setting mac authentication options
		'''
		logger.debug('EditNetworkPage : Clicking on mac authentication options')		
		self.mac_authentication_enterprise.click()
		self.auth_failthru_enterprise.click()
		time.sleep(3)
		
	def set_inactive_timeout_option(self,value):
		'''
			Setting inactive timeout option
		'''
		logger.debug('EditNetworkPage : Inactive timeout option')		
		self.inactivity_timeout.set(value)
		time.sleep(3)		
		
		
	def set_session_key_for_leap(self):
		'''
			Setting session key for LEAP
		'''
		logger.debug('EditNetworkPage : Enabling Use Session key for LEAP')
		self.use_session_key.click()
		time.sleep(3)
		
	def click_on_disable_ssid(self):
		'''
			Clicking on ssid
		'''
		logger.debug('EditNetworkPage : Disabling disabled ssid')
		self.disable_ssid.click()
		
	def click_on_hide_ssid(self):
		'''
			Clicking on hide ssid
		'''
		logger.debug('EditNetworkPage : Clicking on hide ssid')
		self.hide_ssid.click()		
		
		
	def assert_uppercase_support_delimiter_options(self):
		'''
			Asserting uppercase support and delimiter options
		'''
		if self.open_uppercase_support:
			raise AssertionError("Uppercase support is not visible.Traceback: %s " %traceback.format_exc())
		if self.mac_auth_delimiter:
			raise AssertionError("Delimiter option is not visible.Traceback: %s " %traceback.format_exc())
		
	def assert_disabled_mac_authentication_options_and_session_key_for_leap(self):
		'''
			Asserting mac authentication options and session key for leap
		'''
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.click_on_security_accordion()
		if self.mac_authentication_enterprise.is_selected():
			raise AssertionError("Mac authentication checkbox is not selected.Traceback: %s " %traceback.format_exc())
		if self.auth_failthru_enterprise.is_selected():
			raise AssertionError("Mac authentication fail thru checkbox is not selected.Traceback: %s " %traceback.format_exc())
		if not self.use_session_key.is_selected():
			raise AssertionError("Use session key checkbox is not selected.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Network link')
		self.networks.click()
		time.sleep(5)
		
	def setting_termination_option(self,flag):
		'''
			setting terminal option
		'''
		if flag:
			logger.debug('EditNetworkPage : Enabling termination option')
			self.security_termination.set(self.config.config_vars.enabled_option)
		else:
			logger.debug('EditNetworkPage : Disabling termination option')
			self.security_termination.set(self.config.config_vars.disabled_option)
			
	def setting_accounting_interval_option(self,flag,value):
		'''
			Setting accounting option
		'''
		if flag:
			logger.debug('EditNetworkPage : Enabling accounting option')
			self.accounting_dropdown.set(self.config.config_vars.enabled_option)
			self.account_interval.set(value)
		else:
			logger.debug('EditNetworkPage : Disabling accounting option')
			self.terminal_dropdown.set(self.config.config_vars.disabled_option)
			
	def assert_disable_ssid_termination_accounting_option(self):
		'''
			Asserting disable ssid, termination, accounting options
		'''
		logger.debug('EditNetworkPage :  Clicking advanced settings accordion')
		self.click_on_advanced_settings_accordion()
		if not self.disable_ssid.is_selected():
			raise AssertionError("Disable SSID checkbox is not selected.Traceback: %s " %traceback.format_exc())			
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.click_on_security_accordion()
		if not self.security_termination.get_selected() == self.config.config_vars.disabled_option:
			raise AssertionError("Termination dropdown is not disabled.Traceback: %s " %traceback.format_exc())
		if not self.accounting_dropdown.get_selected() == self.config.config_vars.enabled_option:
			raise AssertionError("Accounting dropdown is not enabled.Traceback: %s " %traceback.format_exc())
		if not self.account_interval.get() == '60':
			raise AssertionError("Accounting interval is not set to 60.Traceback: %s " %traceback.format_exc())	
		logger.debug('EditNetworkPage : Clicking on Network link')
		self.networks.click()
		time.sleep(5)	
		
	def set_external_radius_server_1(self):
		'''
			Setting external radius server 1
		'''
		logger.debug('SecurityPage : Setting new external server to Authentication Server 1')
		self.authentication_server.set(self.config.config_vars.new_external_server)
		time.sleep(3)
		logger.debug('SecurityPage : Entering details')
		self.auth_server_name.set(self.config.config_vars.auth_server_value)
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr_value)
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey_value)
		self.Retype_auth_shared_key.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug('SecurityPage : Saving external radius server')
		self.save_server.click()
		time.sleep(12)
		
	def set_external_radius_server_2(self):
		'''
			Setting external radius server 2
		'''
		logger.debug('SecurityPage : Setting new external server to Authentication Server 2')
		self.authentication_server_2.set(self.config.config_vars.new_external_server)
		time.sleep(3)
		logger.debug('SecurityPage : Entering details')
		self.auth_server_name.set(self.config.config_vars.auth_server_value_2)
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr_value)
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey_value)
		self.Retype_auth_shared_key.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug('SecurityPage : Saving external radius server')
		self.save_server.click()
		time.sleep(12)		
		
	def assert_hide_ssid_termination_session_key_for_leap(self):
		'''
			Asserting hide ssid, termination, session key for leap
		'''	
		logger.debug('EditNetworkPage :  Clicking advanced settings accordion')
		self.click_on_advanced_settings_accordion()
		if not self.hide_ssid.is_selected():
			raise AssertionError("Hide SSID checkbox is not selected.Traceback: %s " %traceback.format_exc())			
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.click_on_security_accordion()
		if not self.security_termination.get_selected() == self.config.config_vars.enabled_option:
			raise AssertionError("Termination dropdown is not enabled.Traceback: %s " %traceback.format_exc())	
		if not self.use_session_key.is_selected():
			raise AssertionError("Use session key LEAP checkbox is not selected.Traceback: %s " %traceback.format_exc())			
		if not self.authentication_server.get_selected() == self.config.config_vars.auth_server_value:
			raise AssertionError("Authentication server is not set to external server.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Network link')
		self.networks.click()
		time.sleep(5)
		
	def assert_inactive_timeout_vlan_security_level_key_management(self):
		'''
			Asserting inactive timeout, vlan, security level, key management
		'''
		logger.debug('EditNetworkPage :  Clicking advanced settings accordion')
		self.click_on_advanced_settings_accordion()
		if not self.inactivity_timeout.get() == '3600':
			raise AssertionError("Inactivity timeout is not set to 3600.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage :  Clicking on vlan accordion')
		self.vlan_accordion.click()
		if not self.virtual_controller_assigned.is_selected():
			raise AssertionError("Virtual controller assigned is not selected.Traceback: %s " %traceback.format_exc())					
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.click_on_security_accordion()
		if not self.security_enterprise.is_selected():
			raise AssertionError("Enterprise radio button is not selected.Traceback: %s " %traceback.format_exc())
		if not self.security_key_management.get_selected() == self.config.config_vars.key_management_dynamic:
			raise AssertionError("Key Management is not set to Dynamic WEP.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Network link')
		self.networks.click()
		time.sleep(5)
		
		
	def click_on_can_be_used_without_uplink(self):
		'''
			Clicking on can be used without uplink
		'''	
		logger.debug('EditNetworkPage : Clicking on can be used without uplink')
		self.without_uplink.click()
		
		
	def click_on_okc(self,value=None):
		'''
			Clicking on OKC checkbox
		'''
		logger.debug('SecurityPage : Clicking on OKC checkbox')
		self.buy_time()
		if value == 'Enable':
			if not self.okc_checkbox.is_selected():
				self.okc_checkbox.click()
		elif value == 'Disable':
			if self.okc_checkbox.is_selected():
				self.okc_checkbox.click()
		
	def set_reauth_interval(self):
		'''
			Setting reauth interval to 3 Hrs
		'''
		logger.debug('SecurityPage : Editing reauth interval')
		self.reauth_interval.set(self.config.config_vars.new_reauth_value)
		self.reauth_unit.set('hrs.')
		
		
	def assert_can_be_used_without_uplink_okc_reauth_interval(self):
		'''
			Asserting can be used without uplink,okc,reauth interval
		'''
		logger.debug('EditNetworkPage :  Clicking advanced settings accordion')
		self.click_on_advanced_settings_accordion()
		if self.without_uplink.is_selected():
			raise AssertionError("Can Be Used Without Checkbox is selected.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on security accordion')
		self.click_on_security_accordion()
		if not self.okc_checkbox.is_selected():
			raise AssertionError("OKC Checkbox is not selected.Traceback: %s " %traceback.format_exc())
		if not self.reauth_interval.get() == '3' and self.reauth_unit.get_selected() == 'hrs.':
			raise AssertionError("Reauth interval is not set to 3Hrs.Traceback: %s " %traceback.format_exc())					
		logger.debug('EditNetworkPage : Clicking on Network link')
		self.networks.click()
		time.sleep(5)
		
		
	def assert_auth_survivability_cache_timeout(self):
		'''
			Assert authenticate survivability and cache timeout
		'''
		if self.auth_survivability:
			raise AssertionError("Authentication Survivability is visible.Traceback: %s " %traceback.format_exc())			
		if self.cache_timeout:
			raise AssertionError("Cache timeout is visible.Traceback: %s " %traceback.format_exc())
		logger.debug('EditNetworkPage : Clicking on Network link')
		self.networks.click()
		time.sleep(5)
		
		
	def assert_hide_ssid_enabled(self):
		'''
			Asserting hide ssid
		'''	
		if not self.hide_ssid.is_selected():
			raise AssertionError("Hide SSID checkbox is not selected.Traceback: %s " %traceback.format_exc())
		
	def assert_hide_ssid_disabled(self):
		'''
			Asserting hide ssid
		'''	
		if self.hide_ssid.is_selected():
			raise AssertionError("Hide SSID checkbox is selected.Traceback: %s " %traceback.format_exc())
		
	def assert_auth_survivability(self,value):
		'''
			Assert authenticate survivability
		'''					
		if not self.auth_survivability.get_selected() == str(value):
			raise AssertionError("Authentication Survivability "+str(value)+".Traceback: %s " %traceback.format_exc())		
	
	def assert_cache_timeout(self,value):
		'''
			Assert cache timeout
		'''
		if not self.cache_timeout.get() == str(value):
			raise AssertionError("Cache timeout is not set to "+str(value)+".Traceback: %s " %traceback.format_exc())			
								
		
	def assert_auth_server_2(self,flag):
		'''
			Asserting authentication server 2
		'''
		if flag:
			if not self.auth_server_2_disable:
				raise AssertionError("Authentication server 2 is not visible.Traceback: %s " %traceback.format_exc())
		else:
			if self.auth_server_2_disable:
				raise AssertionError("Authentication server 2 is visible.Traceback: %s " %traceback.format_exc())
	
	def assert_okc_checkbox(self,flag):
		'''
			Asserting okc checkbox
		'''
		if flag:
			if self.okc_checkbox.is_selected():
				raise AssertionError("OKC Checkbox is selected.Traceback: %s " %traceback.format_exc())
		else:
			if not self.okc_checkbox.is_selected():
				raise AssertionError("OKC Checkbox is not selected.Traceback: %s " %traceback.format_exc())
		
	def assert_termination_dropdown(self,value):
		'''
			Asserting termination dropdown
		'''
		if value == 'Enabled':
			if not self.security_termination.get_selected() == self.config.config_vars.enabled_option:
				raise AssertionError("Termination dropdown is not enabled.Traceback: %s " %traceback.format_exc())			
		else:
			if not self.security_termination.get_selected() == self.config.config_vars.disabled_option:
				raise AssertionError("Termination dropdown is not disabled.Traceback: %s " %traceback.format_exc())
	
	def assert_inactivity_timeout(self,value):
		'''
			Asserting inactivity timeout
		'''
		if not self.inactivity_timeout.get() == str(value):
			raise AssertionError("Inactivity timeout is not set to 3600.Traceback: %s " %traceback.format_exc())
		
	def set_delimiter_option(self):
		'''
			Setting delimiter option
		'''
		logger.debug('EditNetworkPage : Editing delimeter option')
		self.mac_auth_delimiter.set(self.config.config_vars.enterprise_delimeter)
		
	def set_delimiter_option_empty(self):
		'''
			Setting delimiter option empty
		'''
		logger.debug('EditNetworkPage : Editing delimeter option')
		self.mac_auth_delimiter.set('')
		
	def set_uppercase_support_option(self,value):
		'''
			Setting uppercase support
		'''
		if value == 'Enabled':
			logger.debug('EditNetworkPage : Enabling uppercase support')
			self.open_uppercase_support.set(self.config.config_vars.enabled_option)		
		else:
			logger.debug('EditNetworkPage : Disabling uppercase support')
			self.open_uppercase_support.set(self.config.config_vars.disabled_option)
			
	def set_blacklisting_option(self,value=None):
		'''
			Setting blacklisting option
		'''
		if value == 'Enabled':
			logger.debug('EditNetworkPage : Enabling blacklisting option')
			self.blacklisting.set(self.config.config_vars.enabled_option)	
		else:
			logger.debug('EditNetworkPage : Disabling blacklisting option')
			self.blacklisting.set(self.config.config_vars.disabled_option)	
		
	def set_max_authentication_option(self,value):
		'''
			Setting max authentication option
		'''
		logger.debug('EditNetworkPage : Setting max authentication option')
		self.max_auth_failures.set(value)
		
	def set_load_balancing_option(self,value):
		'''
			Setting load balancing option
		'''
		if value == 'Enabled':
			logger.debug('EditNetworkPage : Enabling load balancing')
			self.load_balancing_dropdown.set(self.config.config_vars.enabled_option)
		else:
			logger.debug('EditNetworkPage : Disabling load balancing')
			self.load_balancing_dropdown.set(self.config.config_vars.disabled_option)
			
	def select_auth_server_internalserver(self,value):
		'''
			Setting internal server
		'''		
		if value == '1':
			logger.debug("EditNetworkPage : Selecting  InternalServer for Authentication Server feild ")
			self.authentication_server.set(self.config.config_vars.authentication_server_value)
			self.buy_time()
		if value == '2':
			logger.debug("EditNetworkPage : Selecting  InternalServer for Authentication Server feild ")
			self.authentication_server_2.set(self.config.config_vars.authentication_server_value)
			self.buy_time()
			
	def assert_inactive_timeout(self,value):
		'''
			Asserting inactive timeout
		'''
		if not self.inactivity_timeout.get() == str(value):
			raise AssertionError("Inactivity timeout is not set to "+str(value)+".Traceback: %s " %traceback.format_exc())

	def assert_auth_server_2_internal_auth_server_1_external_server(self):
		'''
			Asserting auth server 2 to internal server and auth server 1 to external server
		'''
		if not self.authentication_server.get_selected() == self.config.config_vars.auth_server_value:
			raise AssertionError("External server 1 is not set to External Server.Traceback: %s " %traceback.format_exc())
		if not self.authentication_server_2.get_selected() == self.config.config_vars.authentication_server_value:
			raise AssertionError("External server 2 is not set to Internal Server.Traceback: %s " %traceback.format_exc())			
		
	
	def enable_authentication_survivability(self):
		'''
			Enabling authentication survivability
		'''
		logger.debug('SecurityPage : Enabling authentication survivability')
		self.auth_survivability.set(self.config.config_vars.auth_survivability)
		time.sleep(3)
		
	def set_cache_timeout(self,value):
		'''
			Setting cache timeout
		'''
		logger.debug('SecurityPage : Setting cache timeout')
		self.cache_timeout.set(value)
		time.sleep(3)		
	
	
	
	def click_on_network(self):
		'''
			Clicking network link
		'''
		logger.debug('EditNetworkPage : Clicking on Network link')
		self.networks.click()
		time.sleep(5)
		
	def assert_auth_survivability_and_cache_timeout(self):		
		if self.auth_survivability:
			raise AssertionError("auth survivability feild is present.Traceback: %s " %traceback.format_exc())
		if self.cache_timeout:
			raise AssertionError("cache timeout feild is present.Traceback: %s " %traceback.format_exc())
			
	def check_hide_ssid_checkbox(self,flag):
		logger.debug('EditNetworkPage : Clicking Advanced Setting accordian')
		self.click_advanced_settings_accordion()
		if flag == 'check' :
			logger.debug("EditNetworkPage :Check if hide ssid is enabled.")
			if not self.hide_ssid.is_selected():
				raise AssertionError("EditNetworkPage : hide ssid is not enabled.Traceback: %s " %traceback.format_exc())
		elif flag == 'uncheck':
			logger.debug("EditNetworkPage :Check if hide ssid is disabled.")
			if self.hide_ssid.is_selected():
				raise AssertionError("EditNetworkPage : hide ssid is not disabled.Traceback: %s " %traceback.format_exc())
				
	def assert_edit_network_page_ui(self,accounting_disable=False,acc_interval=False,balancing=False,auth_survivability=False,roaming=False,auth_cache_timeout=False):
		'''
		Check if field dropdown,checkbox,radio button , input box is visible on UI or not .
		'''
		if auth_survivability:
			logger.debug("EditNetworkPage :Check if auth survivability is visible or not.")
			if self.auth_survivability:
				raise AssertionError("EditNetworkPage: Auth survivability is visible.Traceback: %s " %traceback.format_exc())
		if auth_cache_timeout:		
			logger.debug("EditNetworkPage :Check if auth cache timeout is visible.")		
			if self.auth_cache_timeout:
				raise AssertionError("EditNetworkPage: Auth cache timeout is visible.Traceback: %s " %traceback.format_exc())

	def create_external_radius_server_in_auth_server_two(self):
		'''
		Create new external radius in auth server 2
		'''
		self.buy_time()
		logger.debug('EditNetworkPage : Setting new external server to Authentication Server 1')
		self.authentication_server_2.set(self.config.config_vars.new_external_server)
		self.buy_time()
		logger.debug('EditNetworkPage : Entering details')
		self.auth_server_name.set(self.config.config_vars.auth_server_value_2)
		logger.debug('EditNetworkPage : Set auth ip address')		
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr_value)
		logger.debug('EditNetworkPage : Set auth shared key')
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug('EditNetworkPage : Retype auth shared key')
		self.Retype_auth_shared_key.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug('EditNetworkPage : Saving external radius server')
		self.save_server.click()
		
	def configure_blacklisting(self,blacklisting_enable=False,max_authentication_failure=False):
		'''
		Configure blacklisting on security page 
		param : blacklist_enable : Enable blacklisting
				max auth failure : Set max authentication failure 
		'''
		if blacklisting_enable:
			logger.debug("EditNetworkPage :Enable accounting")
			self.blacklisting.set(self.config.config_vars.enable_option)
		if max_authentication_failure:
			logger.debug('EditNetworkPage :Set max authentication failure.')
			self.max_auth_failures.set(self.config.config_vars.max_auth_failures)
				
	def configure_okc(self,enable=False):
		'''
		Configure okc radio button 
		param : enable Type : Str
		If enable check radio button 
		else
		uncheck
		'''
		if enable:
			if not self.okc_checkbox.is_selected():
				logger.debug('EditNetworkPage :Enable okc.')
				self.okc_checkbox.click()
		else:
			if self.okc_checkbox.is_selected():
				logger.debug('EditNetworkPage :Disable okc.')
				self.okc_checkbox.click()
			
	def configure_mac_authentication_radio_button(self,enable=False):
		'''
		Configure Perform mac authentication radio button 
		param : enable Type : Str
		If enable check radio button 
		else
		uncheck
		'''

		if enable:
			if not self.mac_authentication_enterprise.is_selected():
				logger.debug('EditNetworkPage :Enable Perform mac authentication.')
				self.mac_authentication_enterprise.click()
		else:
			if self.mac_authentication_enterprise.is_selected():
				logger.debug('EditNetworkPage :Disable Perform mac authentication.')
				self.mac_authentication_enterprise.click()
				
	def configure_auth_failthru_enterprise_radio_button(self,enable=False):
		'''
		Configure auth_failthru_enterprise
		param : enable Type : Str
		If enable check radio button 
		else
		uncheck
		'''

		if enable:
			if not self.auth_failthru_enterprise.is_selected():
				logger.debug('EditNetworkPage :Enable auth_failthru_enterprise.')
				self.auth_failthru_enterprise.click()
		else:
			if self.auth_failthru_enterprise.is_selected():
				logger.debug('EditNetworkPage :Disable auth_failthru_enterprise.')
				self.auth_failthru_enterprise.click()

	def select_internal_server_in_auth_server_2(self):
		'''
		Select internal server in auth server 2 
		'''
		logger.debug('EditNetworkPage : Changing Authentication Server 2 to InternalServer')
		self.authentication_server_2.set(self.config.config_vars.authentication_server_value)

	def save_configuration(self):
		logger.debug("EditNetworkPage : Click save settings.")
		self.save_settings.click()
		time.sleep(20)

	def assert_role_radio_role_assignment_rules_default_role_edit_disable(self):
		logger.debug("EditNetworkPage : Click ROLE BASED radio.")
		self.role_based.click()
		logger.debug("EditNetworkPage : Click Default role.")
		self.role_test1.click()
		logger.debug("EditNetworkPage : Click Default role in ROLE ASSIGNMENT RULES accordian.")
		self.default_role_test1.click()
		logger.debug("EditNetworkPage : Checking for Default role under Roles Assignment Rule should not be editable.")
		if not self.edit_disabled:
			raise AssertionError("EditNetworkPage: 'EDIT' button is not diabled.Traceback: %s " %traceback.format_exc())

	def assert_role_radio_role_assignment_rules_default_role_delete_disable(self):
		logger.debug("EditNetworkPage : Click ROLE BASED radio.")
		self.role_based.click()
		logger.debug("EditNetworkPage : Click Default role.")
		self.role_test1.click()
		logger.debug("EditNetworkPage : Click Default role in ROLE ASSIGNMENT RULES accordian.")
		self.default_role_test1.click()
		logger.debug("EditNetworkPage : Checking for Default role under Roles Assignment Rule should not be deleteable.")
		if not self.delete_disabled:
			raise AssertionError("EditNetworkPage: 'DELETE' button is not diabled.Traceback: %s " %traceback.format_exc())
			
	def assert_new_rule_deny(self):
		'''
		Asserting created rule deny
		'''
		self._click_access_accordion()
		logger.debug("EditNetworkPage : clicking 'Network Based' radio button...")
		self.network_based.click()
		time.sleep(8)
		logger.debug("EditNetworkPage : clicking 'Edit' icon...")
		self.edit.click()
		logger.debug("EditNetworkPage : Assert 'ACTION' drop down value...")
		if not self.edit_action_dropdown.get_selected() == 'Deny':
			raise AssertionError("'Action' drop down not set to Deny.Traceback: %s " %(traceback.format_exc()))
			
	def set_auth_cache_timeout(self,value):
		logger.debug("EditNetworkPage : Set auth cache timeout.")		
		self.auth_cache_timeout.set(value)

	def assert_on_action(self, action):
		logger.debug("EditNetworkPage : Assert 'ACTION' drop down value...")
		if not self.edit_action_dropdown.get_selected() == action:
			raise AssertionError("'ACTION' drop down not set to '%s'.Traceback: %s " %(traceback.format_exc(), action))
			
	def assert_new_rule_action(self,action):
		self._click_access_accordion()
		logger.debug("EditNetworkPage : clicking 'Network Based' radio button...")
		self.network_based.click()
		time.sleep(8)
		logger.debug("EditNetworkPage : clicking 'Edit' icon...")
		self.edit.click()
		logger.debug("EditNetworkPage : Assert 'ACTION' drop down value...")
		if not self.edit_action_dropdown.get_selected() == action:
			raise AssertionError("'Action' drop down not set to Deny.Traceback: %s " %(traceback.format_exc()))
			
	def assert_new_rule_destination_nat(self):
		'''
		Asserting created rule Destination-NAT
		'''
		self._click_access_accordion()
		logger.debug("EditNetworkPage : clicking 'Network Based' radio button...")
		self.network_based.click()
		time.sleep(8)
		logger.debug("EditNetworkPage : clicking 'Edit' icon...")
		self.edit.click()
		logger.debug("EditNetworkPage : Assert 'ACTION' drop down value...")
		if not self.edit_action_dropdown.get_selected() == 'Destination-NAT':
			raise AssertionError("'Action' drop down not set to Destination-NAT.Traceback: %s " %(traceback.format_exc()))
			
	def assert_splash_page_option(self, option):
		if not self.splash_page_type.get_selected() == option:
			raise AssertionError("'SPLASH PAGE TYPE' drop down not set to None.Traceback: %s " %(traceback.format_exc()))
			
	def assert_on_security_key_management(self, action):
		logger.debug("EditNetworkPage : Assert 'KEY MANAGEMENT' drop down value...")
		if not self.security_key_management.get_selected() == action:
			raise AssertionError("'KEY MANAGEMENT' drop down not set to '%s'.Traceback: %s " %(traceback.format_exc(), action))
			
	def delete_access_role(self):
		logger.debug("EditNetworkPage:Access accordion: Clicking on role1")
		self.role1_rule.click()
		logger.debug("EditNetworkPage:Access accordion: Clicking on delete button")
		try:
			self.delete_role_1.click()
		except:
			pass
		self.browser.accept_alert()
		time.sleep(5)
		logger.debug("EditNetworkPage:Access accordion: Clicking on role2")
		self.role2_rule.click()
		logger.debug("EditNetworkPage:Access accordion: Clicking on delete button")
		try:
			self.delete_role_1.click()
		except:
			pass
		self.browser.accept_alert()
		logger.debug('EditNetworkPage : Clicking on Save Setting')
		self.save_settings.click()
		
	def move_rules(self):
		logger.debug('EditNetworkPage : Clicking on Role Based option')
		self.role_based.click()
		logger.debug("EditNetworkPage:Access accordion: Clicking on role1")
		self.role1_rule.click()
		logger.debug("EditNetworkPage:Access accordion: Clicking on access control down button")
		self.access_control_down_0.click()
		logger.debug("EditNetworkPage:Access accordion: Clicking on access control up button")
		self.access_control_up_2.click()
		logger.debug("EditNetworkPage:Access accordion: Clicking on role1")
		self.role2_rule.click()
		logger.debug("EditNetworkPage:Access accordion: Clicking on access control down button")
		self.access_control_down_0.click()
		logger.debug("EditNetworkPage:Access accordion: Clicking on access control up button")
		self.access_control_up_2.click()

	def select_role(self):
		logger.debug("EditNetworkPage : Click Default role in ROLE ASSIGNMENT RULES accordian.")
		self.role_test1.click()
		
	def select_basic_info_accordion(self):
		logger.debug('EditNetworkPage: Clicking on Basic Info Accordion')
		self.basic_info_accordion.click()
		self.buy_time()
		
	def select_group_user(self):
		logger.debug('EditNetworkPage: Clicking on Guest user')
		self.guest_option.click()
		
	def setting_splash_page_type_internal_acknowledge(self,value=None):
		logger.debug('EditNetworkPage: Clicking on Security accordion')
		self.security_accordion.click()
		logger.debug('EditNetworkPage: Selecting splash page type ')
		self.splash_page_type.set(value)
		
	def click_vc_assigned(self):
		logger.debug("EditNetworkPage : clicking 'Vlans' accordion...")
		self.vlans_accordion.click()
		if not self.virtual_controller_assigned:
			self.vlans_accordion.click()
		logger.debug("EditNetworkPage : clicking Client IP assignment as VC assigned")
		self.virtual_controller_assigned.click()
		
	def asserting_modified_created_network(self):
		# self.basic_info_accordion()
		if not self.guest_option.is_selected():
			raise AssertionError("EditNetworkPage: Primary usage is not set to Guest")
		self.security_accordion.click()
		if not self.splash_page_type.get_selected() == self.config.config_vars.internal_acknowledge:
			raise AssertionError("EditNetworkPage: Splash Page Type is not set to internal_acknowledge")
		self.vlans_accordion.click()
		if not self.virtual_controller_assigned.is_selected :
			raise AssertionError("EditNetworkPage: Client IP Assignment is not set to VC assigned")
		
	def setting_security_page_value(self,roaming = True):
		logger.debug("EditNetworkPage: Clicking on Security Accordion")
		self.click_security_accordion()
		logger.debug("EditNetworkPage: Selecting AuthenticationServer1 value")
		self.authentication_server.set(self.config.config_vars.auth_server_value)
		logger.debug("EditNetworkPage: Selecting AuthenticationServer2 value")
		self.authentication_server_2.set(self.config.config_vars.authentication_server_value)
		logger.debug("EditNetworkPage: Clicking on 802.11r roaming")
		if roaming:
			if self.roaming_open.is_selected():
				logger.debug("EditNetworkPage : Disable 802.11r ROAMING.")
				self.roaming_open.click()		
		logger.debug('EditNetworkPage : Clicking on Save Setting')
		self.save_settings.click()

	def assert_security_page_value(self, roaming = True):
		logger.debug("EditNetworkPage: Clicking on Advanced Setting Accordion")
		self.click_on_advanced_settings_accordion()
		self.assert_inactivity_timeout(self.config.config_vars.default_inactivity_timeout)
		logger.debug("EditNetworkPage: Clicking on Security Accordion")
		self.click_security_accordion()
		self.assert_auth_server_2_internal_auth_server_1_external_server()
		logger.debug("EditNetworkPage : Checking whether 802.11r ROAMING feild is disable")
		if roaming:
			if self.roaming_open.is_selected():
				raise AssertionError("802.11r ROAMING feild is enable .Traceback: %s " %traceback.format_exc())
		
		
	def assert_auth_server_2_internal(self):
		'''
			Asserting auth server 2 to internal server
		'''
		if not self.authentication_server_2.get_selected() == self.config.config_vars.authentication_server_value:
			raise AssertionError("External server 2 is not set to Internal Server.Traceback: %s " %traceback.format_exc())	
		
		
	def set_enterprise_both_wpa_2_and_wpa_enterprise_voice(self):
		logger.debug("EditNetworkPage: Clicking on Advanced Setting Accordion")
		self.click_on_advanced_settings_accordion()
		logger.debug("EditNetworkPage: Clicking on Disable SSID")
		if self.disable_ssid.is_selected():
			self.disable_ssid.click()
		logger.debug("EditNetworkPage: Clicking on Security Accordion")
		self.click_security_accordion()
		logger.debug("EditNetworkPage: Setting the value of authentication server 2")
		self.authentication_server_2.set(self.config.config_vars.auth_server_value_2)
		logger.debug("EditNetworkPage: Selecting the value of Termination field")
		self.configure_mac_authentication(True)
		logger.debug("EditNetworkPage: Asserting the Accounting Internal field")
		if not self.account_interval.get() == '0' :
				raise AssertionError("EditNetworkPage: Accounting Internal field is not set to '0' ")
		logger.debug('EditNetworkPage : Clicking on Save Setting')
		self.save_settings.click()
		
	def asserting_enterprise_both_wpa_2_and_wpa_enterprise_voice(self):
		logger.debug("EditNetworkPage: Clicking on Advanced Setting Accordion")
		self.click_on_advanced_settings_accordion()
		if self.disable_ssid.is_selected():
			raise AssertionError("EditNetworkPage: Disable SSId value is not 'disabled'")
		logger.debug("EditNetworkPage: Clicking on Security Accordion")
		self.click_security_accordion()
		logger.debug("EditNetworkPage: Clicking on Security Accordion")
		logger.debug("EditNetworkPage: Assert the value of authentication server 2")
		if not self.authentication_server_2.get_selected() == self.config.config_vars.auth_server_value_2:
			raise AssertionError("EditNetworkPage: Authentication Server 2 is not set 'authradius'")
		logger.debug("EditNetworkPage: Selecting the value of Termination field")
		if not self.security_termination.get_selected()  == self.config.config_vars.enable_option:
			raise AssertionError("EditNetworkPage: Termination field is not set to 'enable'")
		logger.debug("EditNetworkPage: Asserting the Accounting Internal field")
		if not self.account_interval.get() == '0' :
				raise AssertionError("EditNetworkPage: Accounting Internal field is not set to '0' ")
				
	def edit_dynamic_wep_voice_network_value(self):
		logger.debug("EditNetworkPage: Clicking on Advanced Setting Accordion")
		self.click_on_advanced_settings_accordion()
		logger.debug("EditNetworkPage : Set localprobe feilds to 0")
		self.localprobe.set(self.config.config_vars.edit_besteffort_default)
		logger.debug("EditNetworkPage: Clicking on Security Accordion")
		self.click_security_accordion()
		logger.debug("EditNetworkPage: Selecting the value of authentication server 2")
		self.select_auth_server_internalserver('1')
		logger.debug('SecurityPage : Selecting Blacklisting value')
		self.set_blacklisting_option()
		logger.debug('SecurityPage : Editing reauth interval')
		self.reauth_interval.set(self.config.config_vars.edit_besteffort_default)
		self.reauth_unit.set('min.')
		self.save_settings.click()
		
	def assert_dynamic_wep_voice_network_value(self):
		conf = self.config.config_vars
		logger.debug("EditNetworkPage: Clicking on Advanced Setting Accordion")
		self.click_on_advanced_settings_accordion()
		self.browser.assert_text(self.localprobe,conf.edit_besteffort_default,'Local Probe value not set to "0"','value')
		logger.debug("EditNetworkPage: Clicking on Security Accordion")
		self.click_security_accordion()
		logger.debug("EditNetworkPage: Asserting SecurityPage Fields ")
		self.browser.assert_drop_down_value(self.authentication_server,conf.authentication_server_value, "AuthenticationServer1 is not selected to 'InternalServer'")
		self.browser.assert_drop_down_value(self.blacklisting,conf.disabled_option, "BlackListing option is not selected to 'Disabled'")
		self.browser.assert_text(self.reauth_interval,conf.edit_besteffort_default,'Reauth interval is not set to "0"','value')
		self.browser.assert_drop_down_value(self.reauth_unit,'min.', "Reauth interval is not set to 'min.'")
		
		
	def edit_personal_static_wep_voice_network_with_content_filtering_blacklisting(self):
		logger.debug("EditNetworkPage: Clicking on Advanced Setting Accordion")
		self.click_on_advanced_settings_accordion()
		logger.debug("EditNetworkPage: Selecting Content Filtering value ")
		self.enable_content_filtering()
		logger.debug("EditNetworkPage: Clicking on Security Accordion")
		self.click_security_accordion()
		logger.debug('SecurityPage : Selecting Blacklisting value')
		self.set_blacklisting_option()
		logger.debug('SecurityPage : Selecting MAC Authentication value')
		self.mac_authentication.set(self.config.config_vars.disabled_option)
		logger.debug("EditNetworkPage: Setting WEP KEY SIZE fields value ")
		self.wep_key_size.set(self.config.config_vars.wep_key_size_64)
		self.wep_key_index.set(self.config.config_vars.tx_key_1)
		self.wep_key.set(self.config.config_vars.wep_key_64_num_valid)
		self.wep_key_retype.set(self.config.config_vars.wep_key_64_num_valid)
		self.save_settings.click()
		
	def assert_personal_static_wep_voice_network_with_content_filtering_blacklisting(self):
		conf = self.config.config_vars
		logger.debug("EditNetworkPage: Clicking on Advanced Setting Accordion")
		self.click_on_advanced_settings_accordion()
		self.browser.assert_drop_down_value(self.content_filtering_dropdown,conf.enabled, "Content Filtering option is not selected to 'Enabled'")
		logger.debug("EditNetworkPage: Clicking on Security Accordion")
		self.click_security_accordion()
		logger.debug("EditNetworkPage: Asserting SecurityPage Fields ")
		self.browser.assert_drop_down_value(self.blacklisting,conf.disabled_option, "BlackListing option is not selected to 'Disabled'")
		self.browser.assert_drop_down_value(self.mac_authentication,conf.disabled_option, "MAC Authentication option is not selected to 'Disabled'")
		self.browser.assert_drop_down_value(self.wep_key_size,conf.wep_key_size_64, "WEP Key Size option is not set to '64-bit'")
		
	def edit_personal_both_wpa_2_and_wpa_personal_voice_network(self):
		logger.debug("EditNetworkPage: Clicking on Advanced Setting Accordion")
		self.click_on_advanced_settings_accordion()
		logger.debug("EditNetworkPage: Setting the value of Video WMM Share")
		self.set_video_wmm_share_default()
		logger.debug("EditNetworkPage: Clicking on Security Accordion")
		self.click_security_accordion()
		logger.debug("EditNetworkPage: Editing the value of SecutityPage")
		self.edit_both_wpa_2_wpa_64passphrase_format()
		self.save_settings.click()

	def assert_personal_both_wpa_2_and_wpa_personal_voice_network(self):
		conf = self.config.config_vars
		logger.debug("EditNetworkPage: Clicking on Advanced Setting Accordion")
		self.click_on_advanced_settings_accordion()
		self.browser.assert_text(self.video_wmm_share,conf.edit_video_wmm_share,'Video WMM Share not set to "0"','value')
		logger.debug("EditNetworkPage: Clicking on Security Accordion")
		self.click_security_accordion()
		logger.debug("EditNetworkPage: Asserting SecurityPage Fields ")
		self.browser.assert_drop_down_value(self.security_key_management,conf.Wpa2_WPA_Enterprise, "Key Management not set to 'WPA2 & WPA'")
		self.browser.assert_drop_down_value(self.blacklisting,conf.enabled_option, "BlackListing option is not selected to 'Disabled'")
		self.browser.assert_drop_down_value(self.mac_authentication,conf.disabled_option, "MAC Authentication option is not selected to 'Disabled'")
		self.browser.assert_drop_down_value(self.passphrase_format,conf.edit_passphrase_format_8, "Passphrase format not set to '8-63 char'")
		
	def edit_enterprise_both_wpa2_and_wpa_enterprise_voice_network_with_local_probe_req(self):
		conf = self.config.config_vars
		self.edit_advance_options()
		self.localprobe.set(conf.vlan_id_0)
		self.open_security_accordion()
		self.select_internalserver()
		self.set_blacklisting_option(conf.content_filtering_default)
		self.reauth_interval.set('0')
		self.save_configuration()

	def set_2_4ghz_max_min_transmit_rates(self, minvalue , maxvalue):
		'''
		sets 2.4ghz max and min rates
		'''
		logger.debug('selecting min value for 2.4ghz')
		self.min24ghz.set(minvalue)
		logger.debug('selecting max value for 2.4ghz')
		self.max24ghz.set(maxvalue)
		
	def set_5ghz_max_min_transmit_rates(self, minvalue , maxvalue):
		'''
		sets 2.4ghz max and min rates
		'''
		logger.debug('selecting min value for 2.4ghz')
		self.min5ghz.set(minvalue)
		logger.debug('selecting max value for 2.4ghz')
		self.max5ghz.set(maxvalue)

	def assert_edit_personal_both_wpa2_personal_enterprise_voice_network_with_2_4ghz_5ghz(self):
		'''
		asserts edited values 
		2.4ghz max : 36
		2.4ghz min : 11
		5ghz max : 48 
		5ghz min : 9
		mac authentication : disabled 
		'''
		conf = self.config.config_vars
		self.edit_advance_options()
		self.browser.assert_drop_down_value(self.min24ghz,conf.max_auth_failure_invalid_num, '2.4ghz min is not set to 11')
		self.browser.assert_drop_down_value(self.max24ghz,conf.max_value_36, '2.4ghz max is not set to 36')
		self.browser.assert_drop_down_value(self.min5ghz,conf.min_value_9, '5ghz min is not set to 9')
		self.browser.assert_drop_down_value(self.max5ghz,conf.max_value_48, '5ghz max is not set to 48')
		self.open_security_accordion() 
		self.browser.assert_drop_down_value(self.mac_authentication, conf.edit_new_open_roaming_value_default, 'mac authentication is not disabled')
		
	def assert_edited_values(self):
		'''
		local probe : 0
		authentication server : internal server
		blacklisting : disabled
		reauth interval : 0 mins.
		'''
		conf = self.config.config_vars
		self.edit_advance_options()
		self.browser.assert_text(self.localprobe, conf.vlan_id_0, 'local probe is not set to zero', 'value')
		self.open_security_accordion()        
		self.browser.assert_drop_down_value(self.authentication_server, conf.edit_Authentication_server, 'authentication server is not set to internal server')
		self.browser.assert_drop_down_value(self.blacklisting, conf.content_filtering_default, 'Blacklisting is not disabled')
		self.browser.assert_text(self.reauth_interval,conf.vlan_id_0, 'reauth interval is not set to zero', 'value')
		
	def edit_enterprise_both_wpa2_and_wpa_enterprise_employee_network_with_inactive_timeout(self):
		'''
		sets following fields
		inactivity time out : 1000
		auth server1 : external radius server
		auth server2 : internal server
		802.11r      : disable
		'''
		conf = self.config.config_vars
		self.edit_advance_options()
		self.set_inactive_timeout_option(conf.default_inactivity_timeout)
		self.open_security_accordion()
		logger.debug('Network: EditNetwork : Security : SElecting authentication server 1')
		self.authentication_server.set(conf.auth_server_name)
		self.select_internal_server_in_auth_server_2()
		self.configure_auth_server_settings(roaming = True)

	def assert_edit_enterprise_both_wpa2_and_wpa_enterprise_employee_network_with_inactive_timeout(self):
		'''
		asserts following fields
		inactivity time out : 1000
		auth server1 : external radius server
		auth server2 : internal server
		802.11r      : disable
		'''
		conf = self.config.config_vars
		self.edit_advance_options()
		self.browser.assert_text(self.inactivity_timeout,conf.default_inactivity_timeout, 'inactivity time out is not set to 1000', 'value')
		self.open_security_accordion()
		self.browser.assert_drop_down_value(self.authentication_server, conf.auth_server_name, 'authentication server is not set to authradius')
		self.browser.assert_drop_down_value(self.authentication_server_2, conf.edit_Authentication_server, 'authentication server 2 is not set to internal server')
		self.browser.assert_check_box_value(self.roaming_open, '802.11r is not unchecked', check = False)
		
	def setting_airtime_value(self,airtime=None,value=None):	
		logger.debug("EditNetworkPage: Setting the value of Airtime field")
		if airtime == 'Enable':
			if not self.airtime_check_box.is_selected():
				self.airtime_check_box.click()
				logger.debug("EditNetworkPage: Setting Air time value")
				self.airtime.set(value)
		else:
			if self.airtime_check_box.is_selected():
				self.airtime_check_box.click()
		
	def setting_each_radio_value(self,radio=None,value=None):	
		logger.debug("EditNetworkPage: Setting the value of Each Radio field")
		if radio == 'Enable':
			if not self.each_radio_check_box.is_selected():
				self.each_radio_check_box.click()
				logger.debug("EditNetworkPage: Setting Air time value")
				self.each_radio.set(value)
		else:
			if self.each_radio_check_box.is_selected():
				self.each_radio_check_box.click()
		
	def edit_wpa_2_personal_voice_network_with_airtime_each_radio_value(self):
		logger.debug("EditNetworkPage: Clicking on Advanced Setting Accordion")
		self.click_on_advanced_settings_accordion()
		self.setting_airtime_value('Enable',self.config.config_vars.edit_localprobe)
		# self.setting_each_radio_value('Enable',self.config.config_vars.value_65535)
		logger.debug("EditNetworkPage : Disable Multicast Transmission Optimization")
		self.multicastratetransmission.set(self.config.config_vars.disabled)
		logger.debug("EditNetworkPage : Set DMO Channel Utilization Threshold to 100")
		self.channelutilizationthresh.set(self.config.config_vars.edit_localprobe)
		logger.debug("EditNetworkPage: Clicking on Security Accordion")
		self.click_security_accordion()
		logger.debug('SecurityPage : Selecting Blacklisting value')
		self.set_blacklisting_option('Enabled')
		logger.debug("EditNetworkPage: Selecting AuthenticationServer2 value")
		self.authentication_server_2.set(self.config.config_vars.authentication_server_value)
		logger.debug('EditNetworkPage : Clicking on Save Setting')
		self.save_settings.click()
		
	def assert_wpa_2_personal_voice_network_with_airtime_each_radio_value(self):	
		conf = self.config.config_vars
		logger.debug("EditNetworkPage: Clicking on Advanced Setting Accordion")
		self.click_on_advanced_settings_accordion()
		logger.debug("EditNetworkPage: Asserting Advance Setting Fields ")
		self.browser.assert_check_box_value(self.airtime_check_box, 'Airtime is not checked', uncheck = True)
		self.browser.assert_text(self.airtime,conf.edit_localprobe,'AirTime not set to "100"','value')
		# self.browser.assert_check_box_value(self.each_radio_check_box, 'Each Radio is not checked', uncheck = True)
		# self.browser.assert_text(self.each_radio,conf.value_65535,'Each Radio not set to "65535"','value')
		self.browser.assert_text(self.channelutilizationthresh,conf.edit_localprobe,'DMO Channel Utilization not set to "100"','value')
		self.browser.assert_drop_down_value(self.multicastratetransmission,conf.disabled, "Multicast Transmission Optimization not selected to 'Disabled'")
		logger.debug("EditNetworkPage: Clicking on Security Accordion")
		self.click_security_accordion()
		logger.debug("EditNetworkPage: Asserting SecurityPage Fields ")
		self.browser.assert_drop_down_value(self.blacklisting,conf.enabled_option, "BlackListing not selected to 'Enabled'")
		self.browser.assert_drop_down_value(self.authentication_server_2,conf.authentication_server_value, "AuthenticationServer 2 not set to 'InternalServer'")
		
	def edit_wpa_2_personal_voice_network_with_airtime_dmo_channel_value(self):
		logger.debug("EditNetworkPage: Clicking on Advanced Setting Accordion")
		self.click_on_advanced_settings_accordion()
		logger.debug("EditNetworkPage : Disable the AirTime and Each Radio field")
		self.setting_airtime_value()
		self.setting_each_radio_value()
		logger.debug("EditNetworkPage : Disable Dynamic Multicast Optimization")
		self.dynamicmulticast.set(self.config.config_vars.disabled)
		logger.debug("EditNetworkPage : Set DMO Channel Utilization Threshold to 90")
		self.channelutilizationthresh.set(self.config.config_vars.background_wmm)
		logger.debug("EditNetworkPage: Clicking on Security Accordion")
		self.click_security_accordion()
		logger.debug("EditNetworkPage: Selecting AuthenticationServer2 value")
		self.authentication_server_2.set(self.config.config_vars.auth_server_value_2)
		logger.debug("EditNetworkPage: Setting the Accounting Interval")
		self.setting_accounting_interval_option(True,self.config.config_vars.new_accounting_interval)
		logger.debug("EditNetworkPage: Setting Uppercase Support field")
		self.set_uppercase_support_option("Enabled")
		logger.debug('EditNetworkPage : Clicking on Save Setting')
		self.save_settings.click()
		
	def assert_wpa_2_personal_voice_network_with_airtime_dmo_channel_value(self):
		conf = self.config.config_vars
		logger.debug("EditNetworkPage: Clicking on Advanced Setting Accordion")
		self.click_on_advanced_settings_accordion()
		logger.debug("EditNetworkPage: Asserting Advance Setting Fields ")
		self.browser.assert_check_box_value(self.airtime_check_box, 'AirTime is checked', check = True)
		# self.browser.assert_check_box_value(self.each_radio_check_box, 'Each Radio is checked', check = True)
		self.browser.assert_text(self.channelutilizationthresh,conf.background_wmm,'DMO Channel Utilization not set to "90"','value')
		self.browser.assert_drop_down_value(self.dynamicmulticast,conf.disabled, "Dynamic Multicast Optimization not selected to 'Disabled'")
		logger.debug("EditNetworkPage: Clicking on Security Accordion")
		self.click_security_accordion()
		logger.debug("EditNetworkPage: Asserting SecurityPage Fields ")
		self.browser.assert_drop_down_value(self.authentication_server_2,conf.auth_server_value_2, "AuthenticationServer 2 not set to 'testradius_2'")
		self.browser.assert_drop_down_value(self.accounting_dropdown,conf.enabled_option, "Accounting field is not set to 'Enable'")
		self.browser.assert_text(self.account_interval,conf.new_accounting_interval,'Accounting interval not set to "60"','value')
		self.browser.assert_drop_down_value(self.open_uppercase_support,conf.enabled_option, "Uppercase Support field is not set to 'Enable'")

	def assert_configure_security_radio_fields(self):
		self.browser.assert_check_box_value(self.okc_checkbox, 'OKC checkbox is not unchecked', check=True)
		self.browser.assert_check_box_value(self.mac_authentication_enterprise, 'mac authentication enterprise checkbox is not unchecked', check=True)
		self.browser.assert_check_box_value(self.auth_failthru_enterprise, 'auth failthru enterprise checkbox is not unchecked', check=True)
		
	def set_miscellaneous_band(self,value):
		'''
		Set Miscellaneous band value
		'''
		self.buy_time()
		logger.debug("BasicInfoPage : Set band to 5 GHZ ")
		self.band.set(value)
	
	def set_security_key_management(self,key):
		'''
		setting value for Key Management 
		'''
		logger.debug("EditNetworkPage : Set Key Management to Both(WPA-2 & WPA) .")
		self.security_key_management.set(key)
	
	def set_wep_key_and_retype_wep_key(self,value):
		'''
		writes Wep Key and Retype Wep Key
		'''
		logger.debug("EditNetworkPage : writting  Wep Key .")
		self.wep_key.set(value)
		logger.debug("EditNetworkPage : writting Re Wep Key .")
		self.wep_key_retype.set(value)
		
	def assert_static_wep_and_wep_key(self):
		'''
		Band : 2.4ghz
		Security Managament : Static wep
		'''
		conf = self.config.config_vars
		self.browser.assert_drop_down_value(self.band,conf.band_value,'Band value is not set to 2.4 GHz')
		self.click_security_accordion()
		self.browser.assert_drop_down_value(self.security_key_management,conf.static_wep_value,'Security Managament is not set to Static wep')
		
	def change_advanced_band_settings_5_ghz(self):
		'''
		Setting band value 5 GHz
		'''
		logger.debug('EditNetworkPage : Clicking on advanced settings accordion')
		self.advance_settings_accordion.click()
		self.buy_time()
		logger.debug('EditNetworkPage : Setting band value to 5 GHz')
		self.band.set(self.config.config_vars.band_value_5ghz)
		self.buy_time()
		
	def assert_blacklisting(self):
		'''
		Blacklisting  : Disabled
		'''
		logger.debug("EditNetworkPage :checking  By default Blacklisting is set to Disabled or not")
		self.browser.assert_drop_down_value(self.blacklisting,self.config.config_vars.disabled,'By default Load Balancing is not set to Disabled')
		
	def assert_primary_usage_voice(self):
		'''
		Asserts PrimaryUsage as Voice
		'''
		logger.debug("EditNetworkPage :checking PrimaryUsage is selected as Voice or not")
		if not self.selected_voice_button:
			raise AssertionError("Selected Voice radio is not present .Traceback: %s " %traceback.format_exc())
		
	def assert_created_personal_wpa_2_personal_voice_network_with_video_wmm_share(self):
		'''
		asserts following fields :
		vide wmm share : 0
		default vlan : 300
		new vlan : abcdef contains 200
		passphrase : 64 chars
		passphrase_format : 64 
		'''
		conf = self.config.config_vars
		logger.debug("EditNetworkPage: Clicking on Advanced Setting Accordion")
		self.click_on_advanced_settings_accordion()
		logger.debug('EditNetworkPage : Advance Settings :Asserting video wmm share')
		self.browser.assert_text(self.video_wmm_share,conf.edit_video_wmm_share,'Video WMM Share not set to "0"','value')
		self.click_vlans_accordion()
		logger.debug('EditNetworkPage : Vlan Page :Asserting created new vlan and default vlan')
		if not self.vlan_id_200 and self.default_vlan_id_300 :
			raise AssertionError('EditNetworkPage : Vlan Page : created new vlan and default vlan edited does not exist')
		logger.debug("EditNetworkPage: Clicking on Security Accordion")
		self.click_security_accordion()
		self.checking_key_wpa_2_and_wpa_64_passphrase_format()
		
		
	def edit_open_voice_network_with_accounting_interval_uppercase_supported(self):
		self.create_external_radius_server_in_auth_server_two()
		logger.debug("EditNetworkPage :Enable accounting")
		self.accounting_dropdown.set(self.config.config_vars.enabled)
		logger.debug('EditNetworkPage :Set Accouting Interval.')
		self.account_interval.set(self.config.config_vars.edit_accounting_interval60)
		logger.debug("EditNetworkPage: Setting Uppercase Support field")
		self.set_uppercase_support_option("Enabled")
		logger.debug('EditNetworkPage : Clicking on Save Setting')
		self.save_settings.click()

	def assert_open_voice_network_with_accounting_interval_uppercase_supported(self):
		conf = self.config.config_vars
		self.click_security_accordion()
		logger.debug("EditNetworkPage: Asserting SecurityPage Fields ")
		self.browser.assert_drop_down_value(self.authentication_server_2,conf.authentication_server_value, "AuthenticationServer 2 not set to 'InternalServer'")
		self.browser.assert_drop_down_value(self.accounting_dropdown,conf.enabled_option, "Accounting field is not set to 'Enable'")
		self.browser.assert_text(self.account_interval,conf.new_accounting_interval,'Accounting interval not set to "60"','value')
		self.browser.assert_drop_down_value(self.open_uppercase_support,conf.enabled_option, "Uppercase Support field is not set to 'Enable'")
				
	def assert_reauth_interval_reauth_unit(self,value,unit):
		'''
		Asserts reauth_interval and reauth_unit.
		'''
		if not self.reauth_interval.get() == value and self.reauth_unit.get_selected() == unit:
			raise AssertionError("Reauth interval is not set 'value' or reauth unit not set to 'unit' Traceback: %s " %traceback.format_exc())		

	def set_leap_use_session_key(self,enable=False):
		'''
		Enables or Disables the 'leap use session key' checkbox.
		'''
		if enable:
			if self.use_session_key:
				if not self.use_session_key.is_selected():
					logger.debug('SecurityPage : Clicking on Use session key for LEAP')
					self.use_session_key.click()
			else:
				raise AssertionError("SecurityPage : element 'Leap use session key' not found.Traceback: %s " %traceback.format_exc())
		else:
			if self.use_session_key:
				if self.use_session_key.is_selected():
					logger.debug('SecurityPage : Clicking on Use session key for LEAP')
					self.use_session_key.click()
	
	def assert_wpa_personal_roaming_open_mac_auth(self):
		logger.debug("EditNetworkPage : Checking whether Key Management feild is set to WPA Personal")
		if not self.security_key_management.get_selected()=='Both(WPA-2 & WPA)':
			raise AssertionError("Key Management feild is set not to Both(WPA-2 & WPA) .Traceback: %s " %traceback.format_exc())
		logger.debug("EditNetworkPage : Checking whether 802.11r ROAMING feild is enabled")
		if not self.roaming_open.is_selected():
			raise AssertionError("802.11r ROAMING feild is disabled .Traceback: %s " %traceback.format_exc())
		logger.debug("EditNetworkPage : Checking whether Mac Authentication feild is Disabled")
		if not self.mac_authentication.get_selected()=='Enabled':
			raise AssertionError("Mac Authentication feild is enabled .Traceback: %s " %traceback.format_exc())
		self.buy_time()
		logger.debug("EditNetworkPage : Checking whether passphrase format  is set to 8-63 chars")
		if not self.passphrase_format.get_selected()=='64 hexadecimal chars':
			raise AssertionError("passphrase format  is not set to 64 hexadecimal chars .Traceback: %s " %traceback.format_exc())

	def click_network_assigned(self):
		'''
		Clicking network assigned radio button.
		'''
		if self.network_assigned1:
			logger.debug("EditNetworkPage: Clicking on Network Assigned Radio button")
			self.network_assigned1.click()
			self.buy_time()
	
	def set_cative_portal_type(self,auth_text=False):
		'''
		sets cative portal type value.
		'''
		if auth_text:
			logger.debug("EditNetworkPage: Selecting 'Authentication Text'")
			if self.cative_portal_type:
				self.cative_portal_type.set(self.config.config_vars.authentication_text)
		else:
			logger.debug("EditNetworkPage: Selecting 'Radius Authentication'")
			if self.cative_portal_type:
				self.cative_portal_type.set(self.config.config_vars.radius_authentication)
				
	def click_captive_portal_edit_link(self):
		'''
		clicks on 'edit' link
		'''
		logger.debug("EditNetworkPage: Clicking on 'Edit' link")
		if self.captive_portal_edit_link:
			self.captive_portal_edit_link.click()
			self.buy_time()
			
	def set_auth_text(self,value):
		'''
		Sets Auth Text value.
		'''
		logger.debug("EditNetworkPage: Sets AuthText value")
		if self.auth_text:
			self.auth_text.set(value)

	def save_captive_profile_button(self):
		'''
		clicks 'Save' button.
		'''
		logger.debug("EditNetworkPage: Clicking on 'SAVE' button")
		if self.save_captive_profile:
			self.save_captive_profile.click()
			self.buy_time()	

	def set_guest_network_security_level_Splash_page_visuals_defaults(self):
		'''
		writes all splash page visuals default values.
		'''
		logger.debug("SecurityPage : Writing banner title default text")
		self.banner_title.set(self.config.config_vars.banner_title_guest_network_default)
		# logger.debug("SecurityPage : Asserting headercolor default text")
		# self.header_colorset(self.config.config_vars.header_color_default)
		logger.debug("SecurityPage : Asserting  default welcome_text")
		self.welcome_text.set(self.config.config_vars.welcome_text_default)
		logger.debug("SecurityPage : Asserting  default policy_text")
		self.policy_text.set(self.config.config_vars.policy_text_default)
		# logger.debug("SecurityPage : Asserting  default background_color text")
		# self.browser.assert_text(self.background_color, self.config.config_vars.background_color_default,'background color is not set to default value','value')
		logger.debug("SecurityPage : Asserting  default redirect url text")
		self.redirect_url.set(self.config.config_vars.redirect_url_default)
		logger.debug('EditNetworkPage : Clicking on save button')
		self.save_captive_portal_partial.click()
	
	def set_guest_network_security_level_Splash_page_visuals_defaults(self):
		'''
		writes all splash page visuals default values.
		'''
		logger.debug("SecurityPage : Writing banner title default text")
		self.banner_title.set(self.config.config_vars.banner_title_guest_network_default)
		# logger.debug("SecurityPage : Asserting headercolor default text")
		# self.header_colorset(self.config.config_vars.header_color_default)
		logger.debug("SecurityPage : Asserting  default welcome_text")
		self.welcome_text.set(self.config.config_vars.welcome_text_default)
		logger.debug("SecurityPage : Asserting  default policy_text")
		self.policy_text.set(self.config.config_vars.policy_text_default)
		# logger.debug("SecurityPage : Asserting  default background_color text")
		# self.browser.assert_text(self.background_color, self.config.config_vars.background_color_default,'background color is not set to default value','value')
		logger.debug("SecurityPage : Asserting  default redirect url text")
		self.redirect_url.set(self.config.config_vars.redirect_url_default)
		logger.debug('EditNetworkPage : Clicking on save button')
		self.save_captive_portal_partial.click()
		
	def edit_application_service_rules(self):
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug("EditNetworkPage : clicking 'Edit' icon...")
		self.edit.click()
		logger.debug('AccessPage :Clicking on Application Service')
		self.service_application.click()
		logger.debug('EditNetworkPage : Clicking on Log checkbox')
		self.log.click()
		logger.debug('EditNetworkPage : Selecting action deny')
		time.sleep(5)
		self.edit_action_dropdown.set(self.config.config_vars.action_deny_option)
		logger.debug('EditNetworkPage : Clicking on save button')
		self.save.click()
		logger.debug("EditNetworkPage : clicking 'Edit' icon...")
		self.rule_edit_pencil_button.click()
		logger.debug('AccessPage :Clicking on Application Service')
		self.service_application.click()
		logger.debug('EditNetworkPage : Clicking on Log checkbox')
		self.log.click()
		logger.debug('EditNetworkPage : Clicking on DSCP TAG checkbox')
		self.dscp.click()		
		logger.debug('EditNetworkPage : Clicking on save button')
		self.save.click()
		logger.debug("EditNetworkPage : calling _save_settings method...")
		self._save_settings()
		
	def assert_application_service_rules(self):
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug("EditNetworkPage : clicking 'Edit' icon...")
		self.edit.click()
		logger.debug('EditNetworkPage : Assert action deny')
		time.sleep(5)
		self.browser.assert_drop_down_value(self.edit_action_dropdown, self.config.config_vars.action_deny_option, "Action not set to Deny")
		logger.debug('EditNetworkPage : Clicking on Cancel button')
		self.cancel.click()
		logger.debug("EditNetworkPage : clicking 'Edit' icon...")
		self.rule_edit_pencil_button.click()
		logger.debug('EditNetworkPage : Asserting on Log checkbox')
		self.browser.assert_check_box_value(self.log, "Log checkbox is not checked by default", uncheck=False)
		logger.debug('EditNetworkPage : Asserting on DSCP TAG checkbox')
		self.browser.assert_check_box_value(self.dscp, "DSCP TAG checkbox is not checked by default", uncheck=False)		
		logger.debug('EditNetworkPage : Clicking on Cancel button')
		self.cancel.click()

	def delete_application_service_rules(self):
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug("EditNetworkPage : Deleting Rule")
		self.delete_01_net.click()
		logger.debug('EditNetworkPage : Deleting Rule')
		self.delete_4399_com.click()
		logger.debug('EditNetworkPage : Deleting Rule')
		self.delete_adobe_update.click()		
		logger.debug('EditNetworkPage : Deleting Rule')
		self.delete_yahoo.click()
		logger.debug("EditNetworkPage : calling _save_settings method...")
		self._save_settings()
		
	def assert_deleted_application_service_rules(self):
		logger.debug('EditNetworkPage : Clicking on access accordion')
		self.access_accordion.click()
		time.sleep(5)
		logger.debug("EditNetworkPage : Asserting delete botton for 01 Net Rule")
		self.browser.assert_element(self.delete_01_net,'delete botton for 01 Net Rule is displayed',False)
		logger.debug("EditNetworkPage : Asserting delete botton for 4399 com Rule")
		self.browser.assert_element(self.delete_4399_com,'delete botton for 4399 com Rule is displayed',False)
		logger.debug("EditNetworkPage : Asserting delete botton for Adobe Update Rule")
		self.browser.assert_element(self.delete_adobe_update,'delete botton for Adobe Update Rule is displayed',False)
		logger.debug("EditNetworkPage : Asserting delete botton for Yahoo Rule")
		self.browser.assert_element(self.delete_yahoo,'delete botton for Yahoo Rule is displayed',False)
		# logger.debug("EditNetworkPage : calling _save_settings method...")
		# self._save_settings()
		
	def click_on_delete_logo(self):
		'''
		Clicks on Delete button
		'''
		logger.debug("EditNetworkPage: clicking on Delete button")
		self.delete_logo.click()
		self.buy_time()
		
	def click_on_delete_logo(self):
		'''
		Clicks on Delete button
		'''
		logger.debug("EditNetworkPage:SecurityPage: clicking on Delete button")
		self.delete_logo.click()
		self.buy_time()	
		
	def assert_splas_page_visuals_fields(self):
		'''
		Asserts Logo upload, Delete and logo Image button
		'''
		logger.debug('EditNetworkPage :SecurityPage: checking Image is uplloaded or not...')
		self.browser.assert_element(self.no_logo_image, "Image is uploaded in Splash Page visuals ")	
		logger.debug('EditNetworkPage :SecurityPage: checking logo upload button is enable or not...')
		self.browser.assert_element(self.logo_upload, "logo upload button is not Enabled")
		logger.debug('EditNetworkPage :SecurityPage: checking Delete button is Disabled or not...')		
		self.browser.assert_element(self.logo_disabled_delete_button, "Delete button is not disabled")

	def click_on_preview_splash_page(self):
		'''
		Clicks on Preview Splash Page
		'''
		logger.debug("EditNetworkPage:SecurityPage: clicking on preview splash page")
		self.preview_splash_page.click()
		self.buy_time()
		
	def click_on_preview_splash_page_close(self):
		'''
		clicks on Preview Splash Page Close button
		'''
		logger.debug("EditNetworkPage:SecurityPage: clicking on preview splash page close button")
		self.preview_splash_page_close.click()
		self.buy_time()
		
	def assert_security_logo_small_preview_image(self):
		'''
		Asserts SecurityPage small Preview image of captive portal logo
		'''
		logger.debug('EditNetworkPage :SecurityPage: Asserting logo preview image')
		self.browser.assert_element(self.logo_preview,'Logo preview image is not displayed',False)	
	
	def assert_security_splash_banner_logo(self):
		logger.debug("EditNetworkPage : SecurityPage: Checking splash Banner logo is not present or not")
		self.browser.assert_element(self.splash_banner_logo,'splash banner logo is  Present', False)	
		
	def assert_guest_user(self):
		logger.debug('EditNetworkPage: Asserting the Guest user')
		if not self.guest_option.is_selected():
			raise AssertionError("Guest user option is not selected" )
			
	def delete_role_assignment_rules(self):
		logger.debug("EditNetworkPage : Click ROLE BASED radio.")
		self.role_based.click()
		logger.debug("EditNetworkPage : Deleting Role 1")
		self.delete_rule_something.click()
		logger.debug("EditNetworkPage : Deleting Role 2")
		self.delete_rule_something2.click()
		
	def delete_network_based_rule(self):
		logger.debug("EditNetworkPage : Click NETWORK BASED radio.")
		self.network_based.click()
		logger.debug('EditNetworkPage : Deleting rule')
		self.rule_delete_button.click()
		logger.debug("EditNetworkPage : Click save settings.")
		self._save_settings()
		
	def asserted_deleted_roles(self):
		logger.debug("EditNetworkPage : Click ROLE BASED radio.")
		self.role_based.click()
		if self.delete_rule_something:
			raise AssertionError("Role is not deleted")
		if self.delete_rule_something2:
			raise AssertionError("Role is not deleted")
		logger.debug("EditNetworkPage : Click on Cancel Button")
		self.cancel_page.click()
		
	def delete_access_rule_and_assert(self):
		logger.debug("EditNetworkPage : Click ROLE BASED radio.")
		self.role_based.click()
		logger.debug("EditNetworkPage : Deleting Access Rule 1")
		self.delete_noe.click()
		logger.debug("EditNetworkPage : Deleting Access Rule 2")
		self.delete_bootp.click()
		logger.debug("EditNetworkPage: Asserting deleted Access rule")
		if self.delete_noe:
			raise AssertionError(" noe Access Rule is present .Traceback: %s " %traceback.format_exc())
		if self.delete_bootp:
			raise AssertionError("bootp Access Rule is present .Traceback: %s " %traceback.format_exc())
		
	def delete_role_assignment_rules(self):
		logger.debug("EditNetworkPage : Click ROLE BASED radio.")
		self.role_based.click()
		logger.debug("EditNetworkPage : Deleting Role 1")
		self.delete_rule_something.click()
		logger.debug("EditNetworkPage : Deleting Role 2")
		self.delete_rule_something2.click()
		
	def delete_network_based_rule(self):
		logger.debug("EditNetworkPage : Click NETWORK BASED radio.")
		self.network_based.click()
		logger.debug('EditNetworkPage : Deleting rule')
		self.rule_delete_button.click()
		logger.debug("EditNetworkPage : Click save settings.")
		self._save_settings()
		
	def asserted_deleted_roles(self):
		logger.debug("EditNetworkPage : Click ROLE BASED radio.")
		self.role_based.click()
		if self.delete_rule_something:
			raise AssertionError("Role is not deleted")
		if self.delete_rule_something2:
			raise AssertionError("Role is not deleted")
		logger.debug("EditNetworkPage : Click on Cancel Button")
		self.cancel_page.click()
		
	def delete_access_rule_and_assert(self):
		logger.debug("EditNetworkPage : Click ROLE BASED radio.")
		self.role_based.click()
		logger.debug("EditNetworkPage : Deleting Access Rule 1")
		self.delete_noe.click()
		logger.debug("EditNetworkPage : Deleting Access Rule 2")
		self.delete_bootp.click()
		logger.debug("EditNetworkPage: Asserting deleted Access rule")
		if self.delete_noe:
			raise AssertionError(" noe Access Rule is present .Traceback: %s " %traceback.format_exc())
		if self.delete_bootp:
			raise AssertionError("bootp Access Rule is present .Traceback: %s " %traceback.format_exc())
		
	def create_access_rule_for_role_based_3(self,service = None,action=None,destination=None,ip=None):
		logger.debug("AccessPage : Click on add icon.")
		self.add_rule_plus_button.click()
		logger.debug("AccessPage : Select Service Role")
		self.service_role_4.set(service)
		logger.debug("AccessPage : Select Action Role")
		self.action_role_4.set(action)
		logger.debug('AccessPage : Select destination Role')
		self.destination_role4.set(destination)
		if ip:
			logger.debug("AccessPage : Set Ip Address.")
			self.destination_role4.set(ip)
		
	def assert_created_access_rule(self):
		logger.debug("EditNetworkPage: Asserting created Access rule")
		if self.delete_http:
			raise AssertionError("http Access Rule is present .Traceback: %s " %traceback.format_exc())
		
	def assert_ng_wired_pre_and_mac_auth_role(self):
		'''
		Checking pre auth role checkbox present or not
		'''
		logger.debug("EditNetworkPage : SecurityPage: Checking pre auth role checkbox present or not")
		self.browser.assert_element(self.ng_wired_pre_auth_role,'pre auth role checkbox is  Present', False)	
		logger.debug("EditNetworkPage : SecurityPage: Checking mac auth role checkbox present or not")
		self.browser.assert_element(self.ng_Wired_Role_Mac_Auth,'mac auth role checkbox  Present', False)
		
	def setting_password(self,password=None):
		logger.debug("EditNetworkPage : Set Passphrase.")
		self.passphrase.set(password)
		logger.debug("EditNetworkPage : Set Re Passphrase.")
		self.retype_passphrase.set(password)
		
	def page_down(self):
		'''
		scroll down the page
		'''
		self.browser.key_press(u'\ue009')
		self.browser.key_press( u'\ue00f')
		
	def setting_splash_page_type_internal_acknowledge(self,value=None):
		logger.debug('EditNetworkPage: Clicking on Security accordion')
		time.sleep(10)
		self.security_accordion.click()
		time.sleep(10)
		self.security_accordion.click()
		logger.debug('EditNetworkPage: Selecting splash page type ')
		self.splash_page_type.set(value)
