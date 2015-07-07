# Last edited by : Ishan Anand
# On date : 07th Aug 2014

from athenataf.lib.util.WebPage import WebPage
from athenataf.lib.functionality.page.configuration.network.NetworkAssignmentPage import NetworkAssignmentPage
import logging
logger = logging.getLogger('athenataf')
import traceback
import time

class AccessPage(WebPage):
	def __init__(self, test, browser, config):
		WebPage.__init__(self, "Access", test, browser, config)
		self.test.assertPageLoaded(self)
		
	def isPageLoaded(self):
		if self.access_rules:
			return True	
		else:
			return False
			
	def finish_network_setup(self):
		logger.debug('AccessPage: Clicking on finish button')
		self.finish.click()
		self.buy_time()
		if self.finish:
			logger.debug('AccessPage: Clicking on finish button')
			self.finish.click()
		
	def use_access_defaults(self):
		if self.access_radio and self.role_radio :
			logger.debug('AccessPage: Clicking on Role Radio button')
			self.role_radio.click()
			logger.debug('AccessPage: Clicking on Access Radio Button')
			self.access_radio.click()
			logger.debug('AccessPage: Clicking on next button')
			self.next.click()
			self.buy_time()
			return NetworkAssignmentPage(self.test, self.browser, self.config)
		
	def click_network_access(self):
		logger.debug('AccessPage: Clicking on Network based button')
		self.network_based.click()

	def click_role_access(self):
		logger.debug('AccessPage: Clicking on Role based button')
		self.role_radio.click()
		#self.default_role.click()
		
	def access_rule_type_calea(self):
		logger.debug('AccessPage: Clicking on Add rule button')
		self._add_new_rule()
		self.rule_type_dropdown.set(self.config.config_vars.rule_calea_type)
		logger.debug('AccessPage: Clicking on save setting button')
		self.save_settings.click()
		
	def assert_calea(self):
		logger.debug('AccessPage: Asserting the CALEA Rule')
		if not self.calea_bar:
			import traceback
			raise AssertionError("Calea Rule not selected .Traceback: %s " %traceback.format_exc())
		
	def access_rule_type_1(self):
		self.buy_time()
		logger.debug('AccessPage: Clicking on Edit icon')
		self.edit_pencil.click()
		self._assert_rule_fields()
		self.new_rule_type_1.set(self.config.config_vars.rule_type)
		logger.debug('AccessPage: Clicking on Description tag checkbox')
		self.new_dscp_tag_1.click()
		logger.debug('AccessPage: Clicking on priority checkbox')
		self.new_dot1_priority_1.click()
		logger.debug('AccessPage: Setting the value of DSCP tag in dropdown list')
		self.dscp_tag_values.set(self.config.config_vars.dscp_tag_value)
		logger.debug('AccessPage: Setting the value of Priority in dropdown list')
		self.dot_1_priority_values.set(self.config.config_vars.dot_1_priority_value)
		logger.debug('AccessPage: Clicking on save setting button')
		self.save1.click()
		
	def access_rule_type_2(self):
		logger.debug('AccessPage: Clicking on Add rule button')
		self._add_new_rule()
		logger.debug('Adding rule 2')
		if not self.rule:
			self._add_new_rule()
		self.buy_time()
		logger.debug('AccessPage: Setting the value of Rule Type')
		self.rule.set(self.config.config_vars.rule_type)
		logger.debug('AccessPage: Setting the value of Action field')
		self.action.set(self.config.config_vars.action)
		logger.debug('AccessPage: Setting the ip address under action field')
		self.action_ip4.set(self.config.config_vars.action_ip)
		logger.debug('AccessPage: Setting the port value under action field')
		self.action_port4.set(self.config.config_vars.action_port)
		logger.debug('AccessPage: Clicking on Log checkbox')
		self.log.click()
		logger.debug('AccessPage: Clicking oo Media checkbox')
		self.media.click()
		logger.debug('AccessPage: Clicking on Description tag checkbox')
		self.dscp.click()
		logger.debug('AccessPage: Clicking on BlackList checkbox')
		self.blacklist.click()
		logger.debug('AccessPage: Clicking on 802.1 Priority checkbox')
		self.p_802.click()
		logger.debug('AccessPage: Clicking on save setting button')
		self.save_settings.click()
		
	def access_rule_type_3(self):
		logger.debug('AccessPage: Clicking on Add rule button')
		self._add_new_rule()
		logger.debug('Adding rule 3')
		logger.debug('AccessPage: Setting the value of Rule Type')
		self.rule1.set(self.config.config_vars.rule_type)
		logger.debug('AccessPage: Setting the value of Service field')		
		self.service.set(self.config.config_vars.service)
		logger.debug('AccessPage: Setting the protocol value')
		self.service_protocol.set(self.config.config_vars.svc_protocol)
		logger.debug('AccessPage: Setting the port value')
		self.custom_tcp_port.set(self.config.config_vars.svc_port)
		logger.debug('AccessPage: Clicking on save setting button')
		self.save_settings.click()
		
	def access_rule_type_4(self):
		logger.debug('AccessPage: Clicking on Add rule button')
		self._add_new_rule()
		logger.debug('Adding rule 4')
		logger.debug('AccessPage: Setting the value of Rule Type')
		self.rule2.set(self.config.config_vars.rule_type)
		logger.debug('AccessPage: Setting the value Destination field')
		self.destination1.set(self.config.config_vars.destination)
		logger.debug('AccessPage: Setting the Destination ip')
		self.destination_ip1.set(self.config.config_vars.destination_ip)
		logger.debug('AccessPage: Clicking on save setting button')
		self.save_settings.click()
		
	def access_rule_type_5(self):
		logger.debug('AccessPage: Clicking on Add rule button')
		self._add_new_rule()
		logger.debug('Adding rule 5')
		logger.debug('AccessPage: Setting the value of Rule Type')
		self.rule3.set(self.config.config_vars.rule_type)
		logger.debug('AccessPage: Setting the value Destination field')
		self.destination2.set(self.config.config_vars.destination2)
		logger.debug('AccessPage: Setting the Destination ip')
		self.destination_ip2.set(self.config.config_vars.destination_ip)
		logger.debug('AccessPage: Setting the Destination netmask')
		self.destination_mask1.set(self.config.config_vars.destination_mask)
		logger.debug('AccessPage: Clicking on Log checkbox')
		self.log.click()
		logger.debug('AccessPage: Clicking oo Media checkbox')
		self.media.click()
		logger.debug('AccessPage: Clicking on Description tag checkbox')
		self.dscp.click()
		logger.debug('AccessPage: Clicking on BlackList checkbox')
		self.blacklist.click()
		logger.debug('AccessPage: Clicking on 802.1 Priority checkbox')
		self.p_802.click()
		logger.debug('AccessPage: Clicking on save setting button')
		self.save_settings.click()
		
	def rule_type_calea(self):
		logger.debug('AccessPage: Clicking on Add rule button')
		self._add_new_rule()
		logger.debug('AccessPage: Setting the value of Rule Type')
		self.rule3.set(self.config.config_vars.Access_Rule_Captive_portal)
		for i in range(0,5):
			self.browser.key_press(u'\ue004')
		self.browser.key_press(u'\ue007')
		self.browser.key_press('HI')
		self.browser.key_press(u'\ue007')
		self.browser.key_press('THERE')
		logger.debug('AccessPage: Clicking on save setting button')
		self.save_settings.click()
		
	def create_new_role_1(self):
		logger.debug('AccessPage: Clicking on New button to create new Role Assignment Rules')
		self.new_role_assign.click()
		logger.debug('AccessPage: Setting the vlaue of Operator field')
		self.role_operator.set(self.config.config_vars.role_operator1)
		logger.debug('AccessPage: Setting value in String field')
		self.string.set(self.config.config_vars.invalid_character)
		self.ok1.click()
		if not self.string_quote_err:
			raise AssertionError("'Max length error message' for String field is not shown")
		self.string.set(self.config.config_vars.role_string1)
		logger.debug('AccessPage: Clicking ok button')
		time.sleep(5)
		self.browser.key_press(u'\ue004')
		self.ok1.click()
		time.sleep(5)

	def create_new_role_2(self):
		logger.debug('AccessPage: Clicking on New button to create new Role Assignment Rules')
		self.new_role_assign.click()
		logger.debug('AccessPage: Setting the vlaue of Operator field')
		self.role_operator.set(self.config.config_vars.role_operator2)
		logger.debug('AccessPage: Clicking ok button')
		self.ok1.click()
		
	def create_new_role_3(self):
		logger.debug('AccessPage: Clicking on New button to create new Role Assignment Rules')
		time.sleep(5)
		self.new_role_assign.click()
		logger.debug('AccessPage: Setting the vlaue of Operator field')
		self.role_operator.set(self.config.config_vars.role_operator3)
		logger.debug('AccessPage: Setting value in String field')
		self.string.set(self.config.config_vars.role_string3)
		logger.debug('AccessPage: Clicking ok button')
		self.ok1.click()
		
	def role_access_rule(self):
		logger.debug('AccessPage: Clicking on Add rule button')
		self._add_new_rule()
		if self.delete:
			logger.debug('AccessPage: Clicking on Add rule button')
			self._add_new_rule()
			logger.debug('AccessPage: Setting the value of Rule Type')
			self.rule.set(self.config.config_vars.rule_type)
			self.destination2.set(self.config.config_vars.destination2)
			self.destination.set(self.config.config_vars.destination2)
			logger.debug('AccessPage: Setting the Destination ip')
			self.destination_ip4.set(self.config.config_vars.destination_ip)
			logger.debug('AccessPage: Setting the Destination netmask')
			self.destination_mask2.set(self.config.config_vars.destination_mask)
			logger.debug('AccessPage: Clicking on Log checkbox')
			self.log.click()
			logger.debug('AccessPage: Clicking oo Media checkbox')
			self.media.click()
			logger.debug('AccessPage: Clicking on Description tag checkbox')
			self.dscp.click()
			logger.debug('AccessPage: Clicking on BlackList checkbox')
			self.blacklist.click()
			logger.debug('AccessPage: Clicking on 802.1 Priority checkbox')
			self.p_802.click()
			logger.debug('AccessPage: Clicking on save setting button')
			self.save_settings.click()
		
	def click_next(self):
		logger.debug('AccessPage: Clicking on next button')
		self.next.click()	
		return NetworkAssignmentPage(self.test, self.browser, self.config)
	
	def buy_time(self):
		import time
		time.sleep(20)
		
	def create_captive_portal_profile(self,role_based=False,finish=True):
		if not role_based:
			logger.debug('AccessPage: Clicking on Network Based option')
			self.network_based.click()
		else:
			logger.debug('AccessPage: Clicking on Role Based option')
			self.role_radio.click()
		logger.debug('AccessPage: Clicking on Add button')
		self.add_icon.click()
		if not self.rule_type:
			logger.debug('AccessPage: Clicking on Add button')
			self.add_icon.click()
		logger.debug('AccessPage: Setting the value to Rule type')
		self.rule_type.set(self.config.config_vars.Access_Rule_Captive_portal)
		logger.debug('AccessPage: Setting the Captive selection value')
		self.captive_selection.set(self.config.config_vars.Captive_selection_External)
		self.buy_time()
		logger.debug('AccessPage: Setting the Captive Profile value')
		self.captive_profile.set(self.config.config_vars.Captive_Profile_Default)
		logger.debug('AccessPage: Clicking on save setting button')
		self.save_settings.click()
		if finish:
			logger.debug('AccessPage: Clicking on Finishing button')
			self.finish_network_setup()
		
	def create_role_based_captive_portal_profile(self):
		logger.debug('AccessPage: Clicking on Role Based option')
		self.role_radio.click()
		logger.debug('AccessPage: Clicking on Add button')
		self.add_icon.click()
		logger.debug('AccessPage: Setting the value to Rule type')
		self.rule_type.set(self.config.config_vars.Access_Rule_Bandwidth_Contract)
		self.assert_downstream_error_message()
		logger.debug('AccessPage: Setting the value of Access Rule Downstream')
		self.downstream.set(self.config.config_vars.Access_Rule_Downstream)
		logger.debug('AccessPage: Setting the value of Access Rule Upstream')
		self.upstream.set(self.config.config_vars.Access_Rule_Upstream)
		logger.debug('AccessPage: Clicking on save setting button')
		self.save_settings.click()
		logger.debug('AccessPage: Clicking on Finishing button')
		self.finish_network_setup()
		
	def create_domain_name_based_access_rule(self):
		logger.debug('AccessPage: Clicking on Role Based option')
		self.role_radio.click()
		logger.debug('AccessPage: Clicking on Add button')
		self.add_icon.click()
		logger.debug('AccessPage: Setting the value to Rule type')
		self.rule_type.set(self.config.config_vars.Access_Control)
		logger.debug('AccessPage: Setting the destination role ')
		self.destination_role_2.set(self.config.config_vars.Access_Rule_Destination_Role)
		logger.debug('AccessPage: Setting the domain name ')
		self.domain_name.set(self.config.config_vars.Access_Rule_Domain_Name)
		logger.debug('AccessPage: Clicking on save setting button')
		self.save_settings.click()
		logger.debug('AccessPage: Clicking on Finishing button')
		self.finish_network_setup()
		
	
	def assert_downstream_error_message(self):
		import traceback
		logger.debug('AccessPage: Setting the value of Access Rule Downstream')
		self.downstream.set('0')
		logger.debug('AccessPage: Clicking on save setting button')
		self.save_settings.click()
		if not self.downstream_error_message:
			raise AssertionError("Downstream error message has not been shown .Traceback: %s " %traceback.format_exc())
	
	def click_on_next(self):
		logger.debug('AccessPage: Clicking on next button')
		self.next.click()
		return NetworkAssignmentPage(self.test, self.browser, self.config)	
		
	def _assert_rule_fields(self):
		'''
			Asserting the Rule fields value
		'''
		logger.debug('AccessPage: Asserting the Rule fields value')
		import traceback
		if not self.new_rule_type_1:
			raise AssertionError("'Rule Type' drop down not present.Traceback: %s " %traceback.format_exc())
		if not self.new_service_1:
			raise AssertionError("'Services' drop down not present.Traceback: %s " %traceback.format_exc())
		if not self.new_action_1:
			raise AssertionError("'Action' drop down not present.Traceback: %s " %traceback.format_exc())
		if not self.new_destination_1:
			raise AssertionError("'Destination' drop down not present.Traceback: %s " %traceback.format_exc())
		if not self.new_log_1:
			raise AssertionError("'Log' checkbox not present.Traceback: %s " %traceback.format_exc())
		if not self.new_classify_media_1:
			raise AssertionError("'Classify Media' checkbox not present.Traceback: %s " %traceback.format_exc())	
		if not self.new_dscp_tag_1:
			raise AssertionError("'DSCP tag' checkbox not present.Traceback: %s " %traceback.format_exc())
		if not self.blacklist_3:
			raise AssertionError("'Blacklist' checkbox not present.Traceback: %s " %traceback.format_exc())
		# if not self.new_disable_scaning_1:
			# raise AssertionError("'Disable Scanning' checkbox not present.Traceback: %s " %traceback.format_exc())
		if not self.new_dot1_priority_1:
			raise AssertionError("'802.1 priority' checkbox not present.Traceback: %s " %traceback.format_exc())
	
	def create_vlan_rule(self):
		import time
		import traceback
		logger.debug('Access Page : Selecting role radio')
		self.role_radio.click()
		time.sleep(6)
		logger.debug('Access Page : Clicking on Add rule button')
		self.add_icon.click()
		logger.debug('Access Page : Choosing rule type VLAN Assignment')
		self.rule_type.set(self.config.config_vars.access_rule_type_vlan_assignment)
		# logger.debug('Access Page : Entering invalid value in Vlan Id')
		# self.vlan_id.set('0')
		# logger.debug('Access Page : Clicking on Save button')
		# self.save_settings.click()
		# if not self.invalid_vlan_id_error:
			# raise AssertionError("Invalid vlan id error is not present.Traceback: %s " %traceback.format_exc())
		logger.debug('Access Page : Entering valid value in Vlan Id')
		self.vlan_id.set(self.config.config_vars.valid_vlan_id)
		if not self.created_rule_vlan_assignment:
			raise AssertionError("Newly created rule is not present.Traceback: %s " %traceback.format_exc())
		logger.debug('Access Page : Clicking on Save button')
		self.save_settings.click()
		logger.debug('AccessPage: Clicking on Finishing button')
		self.finish_network_setup()
		
	def create_vlan_rule_calea(self):
		import time
		import traceback
		logger.debug('Access Page : Selecting role radio')
		self.role_radio.click()
		time.sleep(6)
		logger.debug('Access Page : Clicking on + icon')
		self.add_icon.click()
		logger.debug('Access Page : Choosing rule type CALEA')
		self.rule_type.set(self.config.config_vars.access_rule_calea)
		logger.debug('Access Page : Clicking on Save button')
		self.save_settings.click()
		if not self.created_rule_calea:
			raise AssertionError("Newly created calea rule is not present.Traceback: %s " %traceback.format_exc())
		logger.debug('Access Page : Clicking on Save button')
		self.finish_network_setup()
		
	def create_bandwidth_contract_rule(self, isCheckboxSelect):
		import time
		import traceback
		logger.debug('Access Page : Selecting role radio')
		self.role_radio.click()
		time.sleep(8)
		logger.debug('Access Page : Clicking on + icon')
		self.add_icon.click()
		logger.debug('Access Page : Choosing rule type Bandwidth Contract')
		self.rule_type.set(self.config.config_vars.rule_type_bandwidth_contract)
		logger.debug('Access Page : Entering invalid value in Downstream and Upstream')
		self.downstream_textbox.set('0')
		self.upstream_textbox.set('0')
		logger.debug('Access Page : Clicking on Save button')
		self.save_settings.click()
		if not self.downstream_error:
			raise AssertionError("Downstream error is not visible.Traceback: %s " %traceback.format_exc())
		if not self.upstream_error:
			raise AssertionError("Upstream error is not visible.Traceback: %s " %traceback.format_exc())
		logger.debug('Access Page : Entering valid value in Downstream and Upstream')
		self.downstream_textbox.set(self.config.config_vars.downstream_value)
		self.upstream_textbox.set(self.config.config_vars.upstream_value)
		if isCheckboxSelect:
			self.select_peruser_chkbox()
		self.save_settings.click()
		if not self.created_bandwidth_contract_assignment:
			raise AssertionError("Newly created rule is not present.Traceback: %s " %traceback.format_exc())
		logger.debug('Access Page : Clicking on Save button')
		self.finish_network_setup()	
		
	def select_peruser_chkbox(self):
		self.peruser_chkbox_1.click()
		self.peruser_chkbox_2.click()
		
	def delete_default_rule_if_present(self):
		logger.debug("AccessPage : looking for default rule...")
		if self.default_rule:
			logger.debug("AccessPage : Delete default rule...")
			self.buy_time()
			self.delete_default.click()
			self.buy_time()
	
	def _add_new_rule(self):
		self.buy_time()
		logger.debug("AccessPage : Click on add icon...")
		self.add_icon.click()

	def _assert_default_rule_settings(self):
		logger.debug("AccessPage : Asserting 'RULE TYPE' default values...")
		if not self.new_rule_type_1.get_selected() == self.config.config_vars.rule_type:
			raise AssertionError("'Rule Type' drop down not set to default.Traceback: %s " %traceback.format_exc())
		if not self.network_service.is_selected():
			raise AssertionError("'Network' radio-button is not selected.Traceback: %s " %traceback.format_exc())
		if not self.new_service_1.get_selected() == self.config.config_vars.service_default_value:
			raise AssertionError("'Service' drop down is not set to default.Traceback: %s " %traceback.format_exc())
		if not self.new_action_1.get_selected() == self.config.config_vars.action_default_value:
			raise AssertionError("'Action' drop down is not set to default.Traceback: %s " %traceback.format_exc())
		if not self.new_destination_1.get_selected() == self.config.config_vars.destination_default_value:
			raise AssertionError("'Destination' drop down is not set to default.Traceback: %s " %traceback.format_exc())
	
	def create_allow_any_to_all_rule(self):
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : set 'SERVICE' drop-down to 'Any'...")
		self.new_service_1.set(self.config.config_vars.service_default_value)
		logger.debug("AccessPage : set 'Action' drop-down to 'Allow'...")
		self.new_action_1.set(self.config.config_vars.action_default_value)
		logger.debug("AccessPage : set 'Destination' drop-down to 'To All Destination'...")
		self.new_destination_1.set(self.config.config_vars.destination_default_value)
		self._save_rule()
	
	def _save_rule(self):
		logger.debug("Click 'SAVE' button..")
		self.save1.click()

	def create_allow_adp_to_all_rule(self):
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : set 'SERVICE' drop-down to 'adp'...")
		self.new_service_1.set(self.config.config_vars.service_adp)
		logger.debug("AccessPage : set 'Action' drop-down to 'Allow'...")
		self.new_action_1.set(self.config.config_vars.action_default_value)
		logger.debug("AccessPage : set 'Destination' drop-down to 'To All Destination'...")
		self.new_destination_1.set(self.config.config_vars.destination_default_value)
		self._save_rule()
		
	def create_allow_bootp_to_a_particular_server_rule(self):
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : set 'SERVICE' drop-down to 'bootp'...")
		self.new_service_1.set(self.config.config_vars.service_bootp)
		logger.debug("AccessPage : set 'Action' drop-down to 'Allow'...")
		self.new_action_1.set(self.config.config_vars.action_default_value)
		logger.debug("AccessPage : set 'Destination' drop-down to 'To a particular server'...")
		self.new_destination_1.set(self.config.config_vars.dest_particular_server)
		logger.debug("AccessPage : Write ip in 'IP' textbox...")
		self.destination_ip4.set(self.config.config_vars.dest_ip)
		self._save_rule()
		
	def create_allow_cfgm_tcp_except_a_particular_server(self):
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : set 'SERVICE' drop-down to 'cfgm'...")
		self.new_service_1.set(self.config.config_vars.service_cfgm)
		logger.debug("AccessPage : set 'Action' drop-down to 'Allow'...")
		self.new_action_1.set(self.config.config_vars.action_default_value)
		logger.debug("AccessPage : set 'Destination' drop-down to 'Except to a particular server'...")
		self.new_destination_1.set(self.config.config_vars.dest_except_partclr_server)
		logger.debug("AccessPage : Write ip in 'IP' textbox...")
		self.destination_ip4.set(self.config.config_vars.dest_ip)
		self._save_rule()
		
	def create_allow_custom_other_to_a_network_rule(self):
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : set 'SERVICE' drop-down to 'CUSTOM'...")
		self.new_service_1.set(self.config.config_vars.service_custom)
		logger.debug("AccessPage : set 'PROTOCOL' drop-down to 'OTHER'...")
		self.service_protocol.set(self.config.config_vars.service_protocol)
		logger.debug("AccessPage : set 'PROTOCOL id' textbox to '56'...")
		self.protocol_id.set(self.config.config_vars.service_protocol_id)
		logger.debug("AccessPage : set 'Action' drop-down to 'Allow'...")
		self.new_action_1.set(self.config.config_vars.action_default_value)
		logger.debug("AccessPage : set 'Destination' drop-down to 'To a network'...")
		self.new_destination_1.set(self.config.config_vars.dest_to_a_ntwrk)
		logger.debug("AccessPage : Write ip in 'IP' textbox...")
		self.destination_ip4.set(self.config.config_vars.dest_ip)
		logger.debug("AccessPage : Write ip in 'NETMASK' textbox...")
		self.destination_netmask.set(self.config.config_vars.dest_netmask)
		self._save_rule()
		
	def create_allow_http_proxy_except_to_a_network_rule(self):
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : set 'SERVICE' drop-down to 'http proxy2'...")
		self.new_service_1.set(self.config.config_vars.service_http_proxy)
		logger.debug("AccessPage : set 'Action' drop-down to 'Allow'...")
		self.new_action_1.set(self.config.config_vars.action_default_value)
		logger.debug("AccessPage : set 'Destination' drop-down to 'Except to a network'...")
		self.new_destination_1.set(self.config.config_vars.dest_except_ntwrk)
		logger.debug("AccessPage : Write ip in 'IP' textbox...")
		self.destination_ip4.set(self.config.config_vars.dest_ip)
		logger.debug("AccessPage : Write ip in 'NETMASK' textbox...")
		self.destination_netmask.set(self.config.config_vars.dest_netmask)
		self._save_rule()
		
	def create_allow_custom_udp_to_a_domain_name_rule(self):
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : set 'SERVICE' drop-down to 'CUSTOM'...")
		self.new_service_1.set(self.config.config_vars.service_custom)
		logger.debug("AccessPage : set 'PROTOCOL' drop-down to 'UDP'...")
		self.service_protocol.set(self.config.config_vars.service_protocol_udp)
		logger.debug("AccessPage : set 'PORT' textbox to '8600'...")
		self.custom_tcp_port.set(self.config.config_vars.service_port)
		logger.debug("AccessPage : set 'Action' drop-down to 'Allow'...")
		self.new_action_1.set(self.config.config_vars.action_default_value)
		logger.debug("AccessPage : set 'Destination' drop-down to 'To a domain name'...")
		self.new_destination_1.set(self.config.config_vars.dest_to_a_domain)
		logger.debug("AccessPage : Write domain name...")
		import time
        time.sleep(10)
		self.domain_name.set(self.config.config_vars.Access_Rule_Domain_Name)
		self._save_rule()
		
	def create_allow_http_to_all_destinations_rule(self):
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : set 'SERVICE' drop-down to 'https'...")
		self.new_service_1.set(self.config.config_vars.service_https)
		logger.debug("AccessPage : set 'Action' drop-down to 'Allow'...")
		self.new_action_1.set(self.config.config_vars.action_default_value)
		logger.debug("AccessPage : set 'Destination' drop-down to 'To All Destination'...")
		self.new_destination_1.set(self.config.config_vars.destination_default_value)
		self._save_rule()
		
	def create_allow_ldp_udp_to_a_particular_server_rule(self):
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : set 'SERVICE' drop-down to 'ldp-udp'...")
		self.new_service_1.set(self.config.config_vars.service_ldp_udp)
		logger.debug("AccessPage : set 'Action' drop-down to 'Allow'...")
		self.new_action_1.set(self.config.config_vars.action_default_value)
		logger.debug("AccessPage : set 'Destination' drop-down to 'To a particular server'...")
		self.new_destination_1.set(self.config.config_vars.dest_particular_server)
		logger.debug("AccessPage : Write ip in 'IP' textbox...")
		self.destination_ip4.set(self.config.config_vars.dest_ip)
		self._save_rule()
		
	def create_allow_netbios_ns_except_to_a_particular_server_rule(self):
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : set 'SERVICE' drop-down to 'netbios-ns'...")
		self.new_service_1.set(self.config.config_vars.service_netbios)
		logger.debug("AccessPage : set 'Action' drop-down to 'Allow'...")
		self.new_action_1.set(self.config.config_vars.action_default_value)
		logger.debug("AccessPage : set 'Destination' drop-down to 'Except to a particular server'...")
		self.new_destination_1.set(self.config.config_vars.dest_except_partclr_server)
		logger.debug("AccessPage : Write ip in 'IP' textbox...")
		self.destination_ip4.set(self.config.config_vars.dest_ip)
		self._save_rule()

	def create_allow_nterm_to_a_network_rule(self):
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : set 'SERVICE' drop-down to 'nterm'...")
		self.new_service_1.set(self.config.config_vars.service_nterm)
		logger.debug("AccessPage : set 'Action' drop-down to 'Allow'...")
		self.new_action_1.set(self.config.config_vars.action_default_value)
		logger.debug("AccessPage : set 'Destination' drop-down to 'To a network'...")
		self.new_destination_1.set(self.config.config_vars.dest_to_a_ntwrk)
		logger.debug("AccessPage : Write ip in 'IP' textbox...")
		self.destination_ip4.set(self.config.config_vars.dest_ip)
		logger.debug("AccessPage : Write ip in 'NETMASK' textbox...")
		self.destination_netmask.set(self.config.config_vars.dest_netmask)
		self._save_rule()

	def create_allow_pptp_except_to_a_network_rule(self):
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : set 'SERVICE' drop-down to 'pptp'...")
		self.new_service_1.set(self.config.config_vars.service_pptp)
		logger.debug("AccessPage : set 'Action' drop-down to 'Allow'...")
		self.new_action_1.set(self.config.config_vars.action_default_value)
		logger.debug("AccessPage : set 'Destination' drop-down to 'Except to a network'...")
		self.new_destination_1.set(self.config.config_vars.dest_except_ntwrk)
		logger.debug("AccessPage : Write ip in 'IP' textbox...")
		self.destination_ip4.set(self.config.config_vars.dest_ip)
		logger.debug("AccessPage : Write ip in 'NETMASK' textbox...")
		self.destination_netmask.set(self.config.config_vars.dest_netmask)
		self._save_rule()

	def create_allow_sip_tcp_to_a_domain_name_rule(self):
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : set 'SERVICE' drop-down to 'sip-tcp'...")
		self.new_service_1.set(self.config.config_vars.service_sip_tcp)
		logger.debug("AccessPage : set 'Action' drop-down to 'Allow'...")
		self.new_action_1.set(self.config.config_vars.action_default_value)
		logger.debug("AccessPage : set 'Destination' drop-down to 'To a domain name'...")
		self.new_destination_1.set(self.config.config_vars.dest_to_a_domain)
		logger.debug("AccessPage : Write domain name...")
		self.domain_name.set(self.config.config_vars.Access_Rule_Domain_Name)
		self._save_rule()

	def create_allow_msrpc_udp_except_to_a_server_rule(self):
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : set 'SERVICE' drop-down to 'msrpc-udp'...")
		self.new_service_1.set(self.config.config_vars.service_mspsc_udp)
		logger.debug("AccessPage : set 'Action' drop-down to 'Allow'...")
		self.new_action_1.set(self.config.config_vars.action_default_value)
		logger.debug("AccessPage : set 'Destination' drop-down to 'Except to a particular server'...")
		self.new_destination_1.set(self.config.config_vars.dest_except_partclr_server)
		logger.debug("AccessPage : Write ip in 'IP' textbox...")
		self.destination_ip4.set(self.config.config_vars.dest_ip)
		self._save_rule()

	def create_allow_syslog_to_a_network(self):
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : set 'SERVICE' drop-down to 'syslog'...")
		self.new_service_1.set(self.config.config_vars.service_syslog)
		logger.debug("AccessPage : set 'Action' drop-down to 'Allow'...")
		self.new_action_1.set(self.config.config_vars.action_default_value)
		logger.debug("AccessPage : set 'Destination' drop-down to 'To a network'...")
		self.new_destination_1.set(self.config.config_vars.dest_to_a_ntwrk)
		logger.debug("AccessPage : Write ip in 'IP' textbox...")
		self.destination_ip4.set(self.config.config_vars.dest_ip)
		logger.debug("AccessPage : Write ip in 'NETMASK' textbox...")
		self.destination_netmask.set(self.config.config_vars.dest_netmask)
		self._save_rule()

	def create_allow_snmp_to_a_domain_name(self):
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : set 'SERVICE' drop-down to 'snmp'...")
		self.new_service_1.set(self.config.config_vars.service_snmp)
		logger.debug("AccessPage : set 'Action' drop-down to 'Allow'...")
		self.new_action_1.set(self.config.config_vars.action_default_value)
		logger.debug("AccessPage : set 'Destination' drop-down to 'To a domain name'...")
		self.new_destination_1.set(self.config.config_vars.dest_to_a_domain)
		logger.debug("AccessPage : Write domain name...")
		self.domain_name.set(self.config.config_vars.Access_Rule_Domain_Name)
		self._select_options()
		self._save_rule()
		
	def _select_options(self):
		logger.debug("AccessPage : Click 'Log' check box...")
		self.new_log_1.click()
		logger.debug("AccessPage : Click 'Classify media' check box...")
		self.new_classify_media_1.click()
		logger.debug("AccessPage : Click 'DSCP tag' check box...")
		self.new_dscp_tag_1.click()
		logger.debug("AccessPage : Click 'Blacklist' check box...")
		self.blacklist_3.click()
		logger.debug("AccessPage : Click 'Disable scanning' check box...")
		self.new_disable_scaning_1.click()
		logger.debug("AccessPage : Click '802.1 priority' check box...")
		self.new_dot1_priority_1.click()
	
	def create_deny_to_a_paticular_sever(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'ANY' ")
		self.new_service_1.set(self.config.config_vars.service_default_value)
		logger.debug("AccessPage : Choosing 'DENY' ")
		self.new_action_1.set(self.config.config_vars.action_deny)
		logger.debug("AccessPage : Choosing 'To a particular server' ")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_To_a_particular_server)
		logger.debug("AccessPage : Writing ip address' ")
		self.destination_ip4.set(self.config.config_vars.invalid_destination_ip)
		self._save_rule()
		if not self.ip_addr_error_msg:
			raise AssertionError("IP field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_ip4.set(self.config.config_vars.destination_ip)
		self._save_rule()
		
	def create_deny_cups_to_all(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'CUPS' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_cups)
		logger.debug("AccessPage : Choosing 'DENY' ")
		self.new_action_1.set(self.config.config_vars.action_deny)
		logger.debug("AccessPage : Choosing 'To all destinations' ")
		self.new_destination_1.set(self.config.config_vars.destination_default_value)
		self._save_rule()
		
	def create_deny_icmp_to_a_particular_server(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'ICMP' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_icmp)
		logger.debug("AccessPage : Choosing 'DENY' ")
		self.new_action_1.set(self.config.config_vars.action_deny)
		logger.debug("AccessPage : Choosing 'To a particular server' ")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_To_a_particular_server)
		logger.debug("AccessPage : Writing ip address' ")
		self.destination_ip4.set(self.config.config_vars.invalid_destination_ip)
		self._save_rule()
		if not self.ip_addr_error_msg:
			raise AssertionError("IP field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_ip4.set(self.config.config_vars.destination_ip)
		self._save_rule()
		
	def create_deny_esp_except_to_a_particular_server(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'ESP' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_esp)
		logger.debug("AccessPage : Choosing 'DENY' ")
		self.new_action_1.set(self.config.config_vars.action_deny)
		logger.debug("AccessPage : Choosing 'Except to a particular server' ")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_Except_to_a_particular_server)
		logger.debug("AccessPage : Writing ip address' ")
		self.destination_ip4.set(self.config.config_vars.invalid_destination_ip)
		self._save_rule()
		if not self.ip_addr_error_msg:
			raise AssertionError("IP field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_ip4.set(self.config.config_vars.destination_ip)
		self._save_rule()
		
	def create_deny_dns_to_a_network(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'DNS' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_dns)
		logger.debug("AccessPage : Choosing 'DENY' ")
		self.new_action_1.set(self.config.config_vars.action_deny)
		logger.debug("AccessPage : Choosing 'To a network' ")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_To_a_network)
		logger.debug("AccessPage : Writing ip address' ")
		self.destination_ip4.set(self.config.config_vars.invalid_destination_ip)
		self._save_rule()
		if not self.ip_addr_error_msg:
			raise AssertionError("IP field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_ip4.set(self.config.config_vars.destination_ip_2)
		logger.debug("AccessPage : Writing netmask' ")
		self.destination_netmask.set(self.config.config_vars.invalid_destination_ip)
		self._save_rule()
		if not self.netmaskd_error:
			raise AssertionError("Netmask field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_netmask.set(self.config.config_vars.dest2_net_mask)
		self._save_rule()
		
	def create_deny_custom_other_except_to_a_network(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'CUSTOM' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_custom)
		logger.debug("AccessPage : Choosing 'OTHER' ")
		self.service_protocol.set(self.config.config_vars.protocols_other)
		logger.debug("AccessPage : Writing protocol id' ")
		self.protocol_id.set(self.config.config_vars.invalid_protocol_id)
		self._save_rule()
		if not self.protocol_id_error_msg:
			raise AssertionError(" Protocol ID field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.protocol_id.set(self.config.config_vars.protocol_id)
		logger.debug("AccessPage : Choosing 'DENY' ")
		self.new_action_1.set(self.config.config_vars.action_deny)
		logger.debug("AccessPage : Choosing 'Except to a network' ")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_Except_to_a_network)
		logger.debug("AccessPage : Writing ip address' ")
		self.destination_ip4.set(self.config.config_vars.invalid_destination_ip)
		self._save_rule()
		if not self.ip_addr_error_msg:
			raise AssertionError("IP field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_ip4.set(self.config.config_vars.destination_ip_2)
		logger.debug("AccessPage : Writing netmask' ")
		self.destination_netmask.set(self.config.config_vars.invalid_destination_ip)
		self._save_rule()
		if not self.netmaskd_error:
			raise AssertionError("Netmask field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_netmask.set(self.config.config_vars.dest2_net_mask)
		self._save_rule()
		
	def create_deny_svp_to_a_domain_name(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'SVP' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_svp)
		logger.debug("AccessPage : Choosing 'DENY' ")
		self.new_action_1.set(self.config.config_vars.action_deny)
		logger.debug("AccessPage : Choosing 'To a Domain Name' ")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_To_a_Domain_Name)
		logger.debug("AccessPage : Writing Domain name' ")
		self.domain_name.set(self.config.config_vars.invalid_domain_name1)
		self._save_rule()
		if not self.invalid_domain_name_error:
			raise AssertionError("Domain Name field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.domain_name.set(self.config.config_vars.domain_names)
		self._save_rule()
		
	def create_deny_http_proxy3_to_all_destinations(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'http-proxy3' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_http_proxy3)
		logger.debug("AccessPage : Choosing 'DENY' ")
		self.new_action_1.set(self.config.config_vars.action_deny)
		logger.debug("AccessPage : Choosing 'To all destinations' ")
		self.new_destination_1.set(self.config.config_vars.destination_default_value)
		self._save_rule()
		
	def create_deny_msrpc_tcp_to_a_particular_server(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'msrpc-tcp' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_msrpc_tcp)
		logger.debug("AccessPage : Choosing 'DENY' ")
		self.new_action_1.set(self.config.config_vars.action_deny)
		logger.debug("AccessPage : Choosing 'To a particular server' ")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_To_a_particular_server)
		logger.debug("AccessPage : Writing ip address' ")
		self.destination_ip4.set(self.config.config_vars.invalid_destination_ip)
		self._save_rule()
		if not self.ip_addr_error_msg:
			raise AssertionError("IP field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_ip4.set(self.config.config_vars.destination_ip)
		self._save_rule()
		
	def create_deny_noe_except_to_a_particular_server(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing ' noe' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_noe)
		logger.debug("AccessPage : Choosing 'DENY' ")
		self.new_action_1.set(self.config.config_vars.action_deny)
		logger.debug("AccessPage : Choosing 'Except to a particular server' ")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_Except_to_a_particular_server)
		logger.debug("AccessPage : Writing ip address' ")
		self.destination_ip4.set(self.config.config_vars.invalid_destination_ip)
		self._save_rule()
		if not self.ip_addr_error_msg:
			raise AssertionError("IP field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_ip4.set(self.config.config_vars.destination_ip)
		self._save_rule()
		
		
	def create_deny_ntp_to_a_network(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'NTP' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_ntp)
		logger.debug("AccessPage : Choosing 'DENY' ")
		self.new_action_1.set(self.config.config_vars.action_deny)
		logger.debug("AccessPage : Choosing 'To a network' ")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_To_a_network)
		logger.debug("AccessPage : Writing ip address' ")
		self.destination_ip4.set(self.config.config_vars.invalid_destination_ip)
		self._save_rule()
		if not self.ip_addr_error_msg:
			raise AssertionError("IP field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_ip4.set(self.config.config_vars.destination_ip_2)
		logger.debug("AccessPage : Writing netmask' ")
		self.destination_netmask.set(self.config.config_vars.invalid_destination_ip)
		self._save_rule()
		if not self.netmaskd_error:
			raise AssertionError("Netmask field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_netmask.set(self.config.config_vars.dest2_net_mask)
		self._save_rule()
		
	def create_deny_rtsp_except_to_a_network(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'RTSP' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_rtsp)
		logger.debug("AccessPage : Choosing 'DENY' ")
		self.new_action_1.set(self.config.config_vars.action_deny)
		logger.debug("AccessPage : Choosing 'Except to a network' ")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_Except_to_a_network)
		logger.debug("AccessPage : Writing ip address' ")
		self.destination_ip4.set(self.config.config_vars.invalid_destination_ip)
		self._save_rule()
		if not self.ip_addr_error_msg:
			raise AssertionError("IP field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_ip4.set(self.config.config_vars.destination_ip_2)
		logger.debug("AccessPage : Writing netmask' ")
		self.destination_netmask.set(self.config.config_vars.invalid_destination_ip)
		self._save_rule()
		if not self.netmaskd_error:
			raise AssertionError("Netmask field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_netmask.set(self.config.config_vars.dest2_net_mask)
		self._save_rule()
		
	def create_deny_smb_tcp_to_a_domain_name(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'SMB-TCP' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_smb_tcp)
		logger.debug("AccessPage : Choosing 'DENY' ")
		self.new_action_1.set(self.config.config_vars.action_deny)
		logger.debug("AccessPage : Choosing 'To a Domain Name' ")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_To_a_Domain_Name)
		logger.debug("AccessPage : Writing Domain name' ")
		self.domain_name.set(self.config.config_vars.invalid_domain_name)
		self._save_rule()
		if not self.invalid_domain_name_error:
			raise AssertionError("Domain Name field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.domain_name.set(self.config.config_vars.domain_names)
		self._save_rule()
		
	def create_deny_vocera_to_all_destinations(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'VOCERA' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_vocera)
		logger.debug("AccessPage : Choosing 'DENY' ")
		self.new_action_1.set(self.config.config_vars.action_deny)
		logger.debug("AccessPage : Choosing 'To all destinations' ")
		self.new_destination_1.set(self.config.config_vars.destination_default_value)
		self._save_rule()
		
	def create_deny_custom_tcp_to_a_particular_server(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'CUSTOM' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_custom)
		logger.debug("AccessPage : Choosing 'TCP' ")
		self.service_protocol.set(self.config.config_vars.protocols_tcp)
		logger.debug("AccessPage : Writing port number' ")
		self.custom_tcp_port.set(self.config.config_vars.invalid_port)
		self._save_rule()
		if not self.invalid_port_error:
			raise AssertionError(" Port field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.custom_tcp_port.set(self.config.config_vars.port)
		logger.debug("AccessPage : Choosing 'DENY' ")
		self.new_action_1.set(self.config.config_vars.action_deny)
		logger.debug("AccessPage : Choosing 'To a particular server' ")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_To_a_particular_server)
		logger.debug("AccessPage : Writing ip address' ")
		self.destination_ip4.set(self.config.config_vars.invalid_destination_ip)
		self._save_rule()
		if not self.ip_addr_error_msg:
			raise AssertionError("IP field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_ip4.set(self.config.config_vars.destination_ip)
		self._save_rule()
		
	def create_calea(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'Calea' ")
		self.new_rule_type_1.set(self.config.config_vars.rule_calea_type)
		self._save_rule()

	def assert_bw_contract_option(self):
		import time
		import traceback
		time.sleep(5)
		logger.debug('AccessPage : Clicking on Network based radio')
		self.network_based.click()
		time.sleep(5)
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		time.sleep(5)
		options = self.rule_type_dropdown.get_options()
		value = False
		index = 0
		for x in options:
			if options[index] == self.config.config_vars.Access_Rule_Bandwidth_Contract:
				value = True
		if value:
			raise AssertionError("Bandwidth Contract option is present.Traceback: %s " %traceback.format_exc())
		
	def assert_vlan_assignment_option(self):
		import time
		import traceback
		time.sleep(5)
		logger.debug('AccessPage : Clicking on Network based radio')
		self.network_based.click()
		time.sleep(5)
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		time.sleep(5)
		logger.debug('AccessPage : Select Vlan assignmet rule type')
		self.rule_type_dropdown.set(self.config.config_vars.access_rule_type_vlan_assignment)
		time.sleep(5)
		logger.debug('AccessPage : Entering vlan id 0 ')
		self.vlan_id.set(self.config.config_vars.vlan_id_0)
		logger.debug('AccessPage : Clicking on Save button')
		self.save_settings.click()
		if not self.invalid_vlan_id_error:
			raise AssertionError("Invalid vlan id error is not present.Traceback: %s " %traceback.format_exc())		
		logger.debug('AccessPage : Entering vlan id 4094 ')
		self.vlan_id.set(self.config.config_vars.vlan_id_4094)
		logger.debug('AccessPage : Clicking on Save button')
		self.save_settings.click()
		if not self.invalid_vlan_id_error:
			raise AssertionError("Invalid vlan id error is not present.Traceback: %s " %traceback.format_exc())
		
	def assert_bw_contract_range_error(self):
		import time
		import traceback
		time.sleep(5)
		logger.debug('AccessPage : Clicking on Role based radio')
		self.role_radio.click()
		time.sleep(5)
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		time.sleep(5)
		logger.debug('AccessPage : Select Bandwidth Contract rule type')
		self.rule_type_dropdown.set(self.config.config_vars.Access_Rule_Bandwidth_Contract)
		time.sleep(5)
		logger.debug('Access Page : Entering invalid value in Downstream and Upstream')
		self.downstream_textbox.set(self.config.config_vars.invalid_downstream)
		self.upstream_textbox.set(self.config.config_vars.invalid_upstream)
		logger.debug('AccessPage : Selecting perusers checkboxs')
		self.select_peruser_chkbox()
		logger.debug('Access Page : Clicking on Save button')
		self.save_settings.click()
		if not self.downstream_error:
			raise AssertionError("Downstream error is not visible.Traceback: %s " %traceback.format_exc())
		if not self.upstream_error:
			raise AssertionError("Upstream error is not visible.Traceback: %s " %traceback.format_exc())
		logger.debug('Access Page : Entering valid value in Downstream and Upstream')
		
	def assert_ip_validation_error(self):
		import time
		import traceback
		time.sleep(5)
		logger.debug('AccessPage : Clicking on Role based radio')
		self.role_radio.click()
		time.sleep(2)
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		time.sleep(2)
		logger.debug('AccessPage : Choosing bootp option from service dropdown')
		self.service_role2.set(self.config.config_vars.service_bootp_value)
		time.sleep(2)
		logger.debug('AccessPage : Choosing To a perticular server option from destination dropdown')
		self.destination_role_2.set(self.config.config_vars.destination_value)
		time.sleep(2)
		logger.debug('AccessPage : Entering invalid ip address')
		self.destination_ip4.set(self.config.config_vars.invalid_destination_ip_1)
		logger.debug('Access Page : Clicking on Save button')
		self.save_settings.click()
		if not self.ip_addr_error_msg:
			raise AssertionError("Destination ip error is not visible.Traceback: %s " %traceback.format_exc())
# 		logger.debug('AccessPage : Entering invalid ip address')
# 		self.destination_ip3.set(self.config.config_vars.invalid_destination_ip_2)
# 		logger.debug('Access Page : Clicking on Save button')
# 		self.save_settings.click()
# 		if not self.ip_addr_error_msg:
# 			raise AssertionError("Destination ip error is not visible.Traceback: %s " %traceback.format_exc())
		logger.debug('AccessPage : Entering invalid ip address')
		self.destination_ip4.set(self.config.config_vars.invalid_destination_ip_3)
		logger.debug('Access Page : Clicking on Save button')
		self.save_settings.click()
		if not self.ip_addr_error_msg:
			raise AssertionError("Destination ip error is not visible.Traceback: %s " %traceback.format_exc())
			
			
	def assert_role_assignment_options(self):
		logger.debug("AccessPage : Click on radio.")
		self.role_radio.click()
		logger.debug("AccessPage : Click on new.")
		self.new_role_assign.click()
		access = self.role_assign_attribute.get_options()
		count = 0 
		for x in access:
			count=count+1
		print count
		if count < 154:
			import traceback
			raise AssertionError("'No of Attribute list less than 154 .Traceback: %s " %traceback.format_exc())
		operator = ['contains','Is the role','equals','not-equals','starts-with','ends-with']
		operator_list = self.role_operator.get_options()
		print operator_list
		for x in range(0,5):
			if not operator_list[x] == operator[x]:
				import traceback
				raise AssertionError("'Operator list doesn't match .Traceback: %s " %traceback.format_exc())
			
	def create_role_assignment_rule(self):
		logger.debug("AccessPage : Click on radio.")
		self.role_radio.click()
		logger.debug("AccessPage : Click on new. button")
		self.new_role_assign.click()
		logger.debug("AccessPage : Create 1st role.")
		logger.debug("AccessPage :  select AP-Group.")
		self.role_assign_attribute.set(self.config.config_vars.dropdown_ap_group)
		logger.debug("AccessPage :Set operator contains.")
		self.role_operator.set(self.config.config_vars.dropdown_contains)
		logger.debug("AccessPage :Set ap group .")
		self.string.set(self.config.config_vars.ap_group)
		logger.debug("AccessPage : Clicking on OK button")
		self.ok1.click()
		logger.debug("AccessPage : Click on new. button")
		self.new_role_assign.click()
		logger.debug("AccessPage : Create 2nd role.")
		logger.debug("AccessPage :  select AP-Name.")
		self.role_assign_attribute.set(self.config.config_vars.dropdown_ap_name)
		logger.debug("AccessPage :Set operator Is the role.")
		self.role_operator.set(self.config.config_vars.dropdown_is_the_role)
		logger.debug("AccessPage : Clicking on OK button")
		self.ok1.click()
		logger.debug("AccessPage : Click on new. button")
		self.new_role_assign.click()
		logger.debug("AccessPage : Create 3rd role.")
		logger.debug("AccessPage :  select Acct-Session-Id.")
		self.role_assign_attribute.set(self.config.config_vars.dropdown_acct_session_id)
		logger.debug("AccessPage :Set operator equals.")
		self.role_operator.set(self.config.config_vars.dropdown_equals)
		logger.debug("AccessPage :Set acct session id .")
		self.string.set(self.config.config_vars.acct_session_id)
		logger.debug("AccessPage : Clicking on OK button")
		self.ok1.click()
		if self.ok1:
			self.ok1.click()
		logger.debug("AccessPage : Click on new. button")
		self.new_role_assign.click()
		logger.debug("AccessPage : Create 4th role.")
		logger.debug("AccessPage :  select Aruba-Port-Id.")
		self.role_assign_attribute.set(self.config.config_vars.dropdown_aruba_port_id)
		logger.debug("AccessPage :Set operator not equals.")
		self.role_operator.set(self.config.config_vars.dropdown_not_equals)
		logger.debug("AccessPage :Set acct session id .")
		self.string.set(self.config.config_vars.aruba_port_id)
		logger.debug("AccessPage : Clicking on OK button")
		self.ok1.click()
		if self.ok1:
			self.ok1.click()
		logger.debug("AccessPage : Click on new. button")
		self.new_role_assign.click()
		logger.debug("AccessPage : Create 5th role.")
		logger.debug("AccessPage :  select dhcp-option.")
		self.role_assign_attribute.set(self.config.config_vars.dropdown_dhcp_option)
		logger.debug("AccessPage :Set operator starts_with.")
		self.role_operator.set(self.config.config_vars.dropdown_starts_with)
		logger.debug("AccessPage :Set dhcp_option as enable .")
		self.string.set(self.config.config_vars.dhcp_option)
		logger.debug("AccessPage : Clicking on OK button")
		self.ok1.click()
		if self.ok1:
			self.ok1.click()
		logger.debug("AccessPage : Click on new. button")
		self.new_role_assign.click()
		logger.debug("AccessPage : Create 6th role.")
		logger.debug("AccessPage :  select mac_address_and_dhcp_options.")
		self.role_assign_attribute.set(self.config.config_vars.dropdown_mac_address_and_dhcp_options)
		logger.debug("AccessPage :Set operator matches_regular_expression.")
		self.role_operator.set(self.config.config_vars.dropdown_matches_regular_expression)
		logger.debug("AccessPage :Set regular_expression 00:03:7F .")
		self.string.set(self.config.config_vars.mac_address_and_dhcp_options)
		logger.debug("AccessPage : Clicking on OK button")
		self.ok1.click()
		if self.ok1:
			self.ok1.click()
		logger.debug("AccessPage : Click on new. button")
		self.new_role_assign.click()
		logger.debug("AccessPage : Create 7th role.")
		logger.debug("AccessPage :  select dropdown_dot1x_authentication_type.")
		self.role_assign_attribute.set(self.config.config_vars.dropdown_dot1x_authentication_type)
		logger.debug("AccessPage :Set operator ends_with.")
		self.role_operator.set(self.config.config_vars.dropdown_ends_with)
		logger.debug("AccessPage :Set string.")
		self.string.set(self.config.config_vars.dot1x_authentication_type)
		logger.debug("AccessPage : Clicking on OK button")
		self.ok1.click()
		if self.ok1:
			self.ok1.click()
		
	def create_role(self):
		logger.debug("AccessPage : Click on new role.")
		self.create_new_role.click()
		logger.debug("AccessPage : Write role name.")
		self.role_input.set(self.config.config_vars.role_name)
		logger.debug("AccessPage : click ok.")
		self.save_role.click()
		
	def edit_role(self):
		logger.debug("AccessPage : Click on 1st role.")
		self.role1.click()
		logger.debug("AccessPage : Click on edit.")
		self.edit_role_assignment_1.click()
		logger.debug("AccessPage : Edit role 1.")
		self.string.set(self.config.config_vars.edit_ap_group)
		logger.debug("AccessPage : Clicking on OK button")
		self.ok1.click()
		
		logger.debug("AccessPage : Click on 3rd role.")
		self.role3.click()
		logger.debug("AccessPage : Click on edit.")
		self.edit_role_assignment_3.click()
		logger.debug("AccessPage : Edit role 2.")
		self.string.set(self.config.config_vars.edit_acct_session_id)
		logger.debug("AccessPage : Clicking on OK button")
		self.ok1.click()
		
		logger.debug("AccessPage : Click on 6th role.")
		self.role6.click()
		logger.debug("AccessPage : Click on edit.")
		self.edit_role_assignment_6.click()
		logger.debug("AccessPage : Edit role 6.")
		self.role_assign_attribute.set(self.config.config_vars.dropdown_mac_address)
		logger.debug("AccessPage : Clicking on OK button")
		self.ok1.click()
		
		
	def delete_role(self):
		logger.debug("AccessPage : Click on 1st role.")
		self.role1.click()
		logger.debug("AccessPage : Click on delete.")
		self.delete_role_assignment_1.click()
		logger.debug("AccessPage : Click on 2nd role.")
		self.role2.click()
		logger.debug("AccessPage : Click on delete.")
		self.delete_role_assignment_2.click()
		logger.debug("AccessPage : Click on 1st role.")
		self.role4.click()
		logger.debug("AccessPage : Click on delete.")
		self.delete_role_assignment_4.click()
		logger.debug("AccessPage : Click on 1st role.")
		self.role6.click()
		logger.debug("AccessPage : Click on delete.")
		self.delete_role_assignment_6.click()
		
		
	def assert_pre_authentication_role(self):
		logger.debug("AccessPage : Click on radio based.")
		self.role_radio.click()
		logger.debug("AccessPage : Check for pre auth checkbox.")
		if not self.ng_wired_pre_auth_role:
			import traceback
			raise AssertionError("Pre auth checkbox not visible .Traceback: %s " %traceback.format_exc())
		
	def assert_mac_authentication_role(self,wireless=False):
		logger.debug("AccessPage : Click on radio based.")
		self.role_radio.click()
		logger.debug("AccessPage : Check for Enforce mac authentication checkbox.")
		if wireless:
			if not self.ng_Wired_Role_Mac_Auth:
				import traceback
				raise AssertionError(" Enforce mac authentication checkbox not visible .Traceback: %s " %traceback.format_exc())
		else:
			if not self.ng_wired_enforce_mac_auth:
				import traceback
				raise AssertionError(" Enforce mac authentication checkbox not visible .Traceback: %s " %traceback.format_exc())

		
	def create_and_edit_role_assignment_rule(self):
		logger.debug("AccessPage : Click on new.")
		self.new_role_assign.click()
		logger.debug("AccessPage : Create 1st role.")
		logger.debug("AccessPage :  select AP-Group.")
		self.role_assign_attribute.set(self.config.config_vars.dropdown_ap_group)
		logger.debug("AccessPage :Set operator contains.")
		self.role_operator.set(self.config.config_vars.dropdown_contains)
		logger.debug("AccessPage :Set ap group .")
		self.string.set(self.config.config_vars.ap_group)
		self.ok1.click()
		logger.debug("AccessPage : Click on edit.")
		self.edit_role_assignment_1.click()
		logger.debug("AccessPage : Edit role 1.")
		self.string.set(self.config.config_vars.edit_ap_group)
		logger.debug("AccessPage : Clicking on OK button")
		self.ok1.click()
		
	def enable_pre_authentication_role(self):
		logger.debug("AccessPage : Click on Enable pre auth only.")
		self.ng_wired_pre_auth_role.click()
		logger.debug("AccessPage : Select pre auth role.")
		self.ng_Wired_Access_pre_Auth.set(self.config.config_vars.Network_name)
		
	def enforce_machine_authentication_role(self):
		logger.debug("AccessPage : Click on Enable mac auth only.")
		self.ng_wired_enforce_mac_auth.click()
		logger.debug("AccessPage : Select pre auth role.")
		self.ng_Wired_Access_Machine_Auth.set(self.config.config_vars.Network_name)
		logger.debug("AccessPage : Select pre auth role.")
		self.ng_Wired_User_Auth.set(self.config.config_vars.Network_name)
		
	def create_access_rule_for_role(self):
		logger.debug("AccessPage : Click on radio based.")
		self.role_radio.click()
		
		logger.debug("AccessPage : Click on add icon.")
		self.add_icon.click()
		logger.debug("AccessPage : Select dhcp.")
		self.service_role2.set(self.config.config_vars.service_role_dhcp)
		logger.debug("AccessPage : Select Destination-NAT.")
		self.action_role2.set(self.config.config_vars.action_role_destination_nat)
		logger.debug("AccessPage : Set Ip Address.")
		self.action_ip4.set(self.config.config_vars.action_ip)
		logger.debug("AccessPage : Set port.")
		self.action_port4.set(self.config.config_vars.action_port)
		logger.debug("AccessPage : Click save")
		self.save_settings.click()

		logger.debug("AccessPage : Click on add icon.")
		self.add_icon.click()
		logger.debug("AccessPage : Select dns.")
		self.service_role3.set(self.config.config_vars.service_role_dns)
		logger.debug("AccessPage : Select Allow.")
		self.action_role3.set(self.config.config_vars.action_role_allow)
		logger.debug("AccessPage : Click save")
		self.save_settings.click()
		
		logger.debug("AccessPage : Click on add icon.")
		self.add_icon.click()
		logger.debug("AccessPage : Select dns.")
		self.service_role4.set(self.config.config_vars.service_role_esp)
		logger.debug("AccessPage : Select Allow.")
		self.action_role4.set(self.config.config_vars.action_role_source_nat)
		logger.debug("AccessPage : Click on log check box")
		self.new_log_1.click()
		logger.debug("AccessPage : Click on media check box")
		self.new_classify_media_1.click()
		logger.debug("AccessPage : Click dscp check box")
		self.new_dscp_tag_1.click()
		logger.debug("AccessPage : Click blacklist check box")
		self.blacklist_3.click()
		logger.debug("AccessPage : Click disable scanning check box")
		self.new_disable_scaning_1.click()
		logger.debug("AccessPage : Click on log check box")
		self.new_dot1_priority_1.click()
		logger.debug("AccessPage : Click save")
		self.save_settings.click()
		
		logger.debug("AccessPage : Click on add icon.")
		self.add_icon.click()
		logger.debug("AccessPage : Select dns.")
		self.service_role5.set(self.config.config_vars.service_role_ftp)
		logger.debug("AccessPage : Select Allow.")
		self.action_role5.set(self.config.config_vars.action_role_deny)
		logger.debug("AccessPage : Click save")
		self.save_settings.click()
		
		logger.debug("AccessPage : Click on add icon.")
		self.add_icon.click()
		logger.debug("AccessPage : Select dns.")
		self.service_role6.set(self.config.config_vars.service_role_gre)
		logger.debug("AccessPage : Select Allow.")
		self.action_role6.set(self.config.config_vars.action_role_allow)
		logger.debug("AccessPage : Click save")
		self.save_settings.click()

		logger.debug("AccessPage : Click on add icon.")
		self.add_icon.click()
		logger.debug("AccessPage : Select dns.")
		self.service_role7.set(self.config.config_vars.service_role_h323_tcp)
		logger.debug("AccessPage : Select Allow.")
		self.action_role7.set(self.config.config_vars.action_role_deny)
		logger.debug("AccessPage : Click save")
		self.save_settings.click()
		
	def create_multiple_roles(self):
		logger.debug("AccessPage : Click on new role.")
		self.create_new_role.click()
		for i in range(1,4):
			logger.debug("AccessPage : Click on new role.")
			self.create_new_role.click()
			element = "role_name_%s"%i
			string = '' 
			exec("string = self.config.config_vars.%s"%element)
			logger.debug("AccessPage : Write role name.")
			self.role_input.set(string)
			logger.debug("AccessPage : click ok.")
			self.save_role.click()


	def create_custom_tcp_access_rule(self):
		logger.debug("AccessPage : Click on add icon.")
		self.add_icon.click()
		logger.debug("AccessPage : Select Custom.")
		self.service_role2.set(self.config.config_vars.service_role_CUSTOM)
		logger.debug("AccessPage : Set invalid port no.")
		self.custom_tcp_port.set('12313132141131651651651654161165165165616')
		self.save_settings.click()
		if not self.invalid_port_error:
			import traceback
			raise AssertionError("Invalid erro * Valid range is 1-65534 message missing .Traceback: %s " %traceback.format_exc())
		logger.debug("AccessPage : Set port no.")
		self.custom_tcp_port.set(self.config.config_vars.tcp_port_range)
		logger.debug("AccessPage : Click save")
		self.save_settings.click()
		
	def create_custom_udp_access_rule(self):
		logger.debug("AccessPage : Click on add icon.")
		self.add_icon.click()
		logger.debug("AccessPage : Select Custom.")
		self.service_role3.set(self.config.config_vars.service_role_CUSTOM)
		logger.debug("AccessPage : Select UDP.")
		self.service_protocol.set(self.config.config_vars.protocol_udp)
		logger.debug("AccessPage : Set port no.")
		self.custom_tcp_port.set(self.config.config_vars.udp_port_range)
		logger.debug("AccessPage : Click save")
		self.save_settings.click()

	def assert_role_in_role_assignment_rules(self):
		logger.debug("AccessPage : Click on new.")
		self.new_role_assign.click()
		logger.debug("AccessPage :Set operator contains.")
		self.role_operator.set(self.config.config_vars.dropdown_contains)
		logger.debug("AccessPage :Set ap group .")
		self.string.set(self.config.config_vars.ap_group)
		flag =False
		for x in self.role_assign_name.options:
			if x == self.config.config_vars.role_name_1:
				flag=True
		if not flag :
			import traceback
			raise AssertionError("Role created not present in Role assignment rules.Traceback: %s " %traceback.format_exc())
		logger.debug("AccessPage :Set Role.")
		self.role_assign_name.set(self.config.config_vars.role_name_1)
		logger.debug("AccessPage :Click save .")		
		self.ok1.click()
		
	def create_vlan_rule_assignment(self):
		import traceback
		logger.debug('Access Page : Clicking on + icon')
		self.add_icon.click()
		logger.debug('Access Page : Choosing rule type VLAN Assignment')
		self.rule_type_dropdown.set(self.config.config_vars.access_rule_type_vlan_assignment)
		logger.debug('Access Page : Entering invalid value in Vlan Id')
		self.vlan_id.set('0')
		logger.debug('Access Page : Clicking on Save button')
		self.save_settings.click()
		if not self.invalid_vlan_id_error:
			raise AssertionError("Invalid vlan id error is not present.Traceback: %s " %traceback.format_exc())
		logger.debug('Access Page : Entering valid value in Vlan Id')
		self.vlan_id.set(self.config.config_vars.valid_vlan_id)
		if not self.created_rule_vlan_assignment:
			raise AssertionError("Newly created rule is not present.Traceback: %s " %traceback.format_exc())
		logger.debug('Access Page : Clicking on Save button')
		self.save_settings.click()

	def access_rule_to_a_network(self):
		logger.debug('Access Page : Clicking on + icon')
		self.add_icon.click()
		logger.debug('Adding to a network access rule')
		logger.debug('Set destination to a network')
		self.destination_role_2.set(self.config.config_vars.destination2)
		logger.debug('Set Destination ip')
		self.destination_ip4.set(self.config.config_vars.destination_ip_1)
		logger.debug('Set Destination netmask')
		self.destination_netmask.set(self.config.config_vars.destination_mask)
		self.save_settings.click()

	def create_external_captive_portal(self):
		logger.debug('Access Page : Clicking on + icon')
		self.add_icon.click()
		if not self.rule_type:
			self.add_icon.click()
		logger.debug('Access Page : Selecting the value of Rule Type')
		self.rule_type.set(self.config.config_vars.Access_Rule_Captive_portal)
		logger.debug('Access Page : Selecting the value of Splash Page Type')
		self.captive_selection.set(self.config.config_vars.Captive_selection_External)
		self.buy_time()
		logger.debug('Access Page : Selecting the value of Captive Portal Profile')
		self.captive_profile.set(self.config.config_vars.Captive_Profile_Default)
		logger.debug('Access Page : Clicking on Save button')
		self.save_settings.click()
		
		
	def create_single_vlan_rule_calea(self):
		import traceback
		logger.debug('Access Page : Clicking on + icon')
		self.add_icon.click()
		logger.debug('Access Page : Choosing rule type CALEA')
		self.rule_type_3.set(self.config.config_vars.access_rule_calea)
		logger.debug('Access Page : Clicking on Save button')
		self.save_settings.click()
		if not self.created_rule_calea:
			raise AssertionError("Newly created calea rule is not present.Traceback: %s " %traceback.format_exc())
		
		
	def move_access_rule(self):
		logger.debug('Access Page : Clicking on down arrow')
		self.access_rule_down_0.click()
		logger.debug('Access Page : Clicking on up arrow')
		self.access_rule_up_1.click()
		
	def no_of_characters_accepted_for_string_field(self):
		logger.debug("AccessPage : Click on new.")
		self.new_role_assign.click()
		logger.debug("AccessPage : Create 1st role.")
		logger.debug("AccessPage :  select AP-Group.")
		self.role_assign_attribute.set(self.config.config_vars.dropdown_ap_group)
		logger.debug("AccessPage :Set operator contains.")
		self.role_operator.set(self.config.config_vars.dropdown_contains)
		logger.debug("AccessPage :Set Valid string greater than 32 .")
		self.string.set(self.config.config_vars.invalid_character)
		logger.debug("AccessPage :Click Ok.")		
		self.ok1.click()
		if not self.maximum_32_chars:
			import traceback
			raise AssertionError("String field denied character greater than 32.Traceback: %s " %traceback.format_exc())
		logger.debug("AccessPage :  select  mac-address-and-dhcp-options")
		self.role_assign_attribute.set(self.config.config_vars.dropdown_mac_address_and_dhcp_options)		
		logger.debug("AccessPage :Set operator matches-regular-expression.")
		self.role_operator.set(self.config.config_vars.dropdown_matches_regular_expression	)
		logger.debug("AccessPage :Set Valid string greater than 255 .")
		self.string.set(self.config.config_vars.string_max_len_mac)
		logger.debug("AccessPage :Click Ok.")		
		self.ok1.click()
		if not self.string_max_255_err:
			raise AssertionError("More than 255 character was accepted... i.e . Traceback: %s" % traceback.format_exc())		
		self.cancel_role_assignments.click()
		logger.debug("AccessPage :Clicking on Cancel button.")
		self.cancel_button.click()
		
	def assert_string_and_role_options(self):
		logger.debug("AccessPage : Click on new.")
		self.new_role_assign.click()
		logger.debug("AccessPage : Create 1st role.")
		logger.debug("AccessPage :  select AP-Group.")
		self.role_assign_attribute.set(self.config.config_vars.dropdown_ap_group)
		logger.debug("AccessPage :Set operator Is the role.")
		self.role_operator.set(self.config.config_vars.dropdown_is_the_role)
		if self.string:
			import traceback
			raise AssertionError("Rule string visible .Traceback: %s " %traceback.format_exc())
		if self.role_assign_name:
			import traceback
			raise AssertionError("Rule option visible .Traceback: %s " %traceback.format_exc())
		
		
	def assert_role_name_validations(self):
		logger.debug("AccessPage : Click on new role.")
		self.create_new_role.click()
		logger.debug("AccessPage : Write role name with single quotes.")
		self.role_input.set(self.config.config_vars.invalid_role_name_single_quotes)
		logger.debug("AccessPage : click ok.")
		self.save_role.click()
		if not self.role_name_validation_error:
			import traceback
			raise AssertionError("'Single quotes role name' Validation error missing .Traceback: %s " %traceback.format_exc())
		logger.debug("AccessPage : Write role name with double quotes.")
		self.role_input.set(self.config.config_vars.invalid_role_name_double_quotes)
		logger.debug("AccessPage : click ok.")
		self.save_role.click()
		if not self.role_name_validation_error:
			import traceback
			raise AssertionError("'Single quotes role name' Validation error missing .Traceback: %s " %traceback.format_exc())
		
	def assert_pre_auth_role_option(self):
		logger.debug("AccessPage : Check for pre auth role options.")
		if self.ng_wired_pre_auth_role:
			import traceback
			raise AssertionError("Assign pre auth role present on bottom page .Traceback: %s " %traceback.format_exc())
		
	def assert_role_delete_button(self,select_role=False):
		logger.debug("AccessPage : Check if delete button is visible.")
		if not select_role:
			if not self.network_delete_button_disabled1:
				import traceback
				raise AssertionError("Delete button visible .Traceback: %s " %traceback.format_exc())
		else:
			logger.debug("AccessPage : Click on role name.")
			self.default_network_role.click()
			import time
			time.sleep(5)
			if not self.network_delete_button_disabled1:
				import traceback
				raise AssertionError("Delete button visible .Traceback: %s " %traceback.format_exc())

	def create_employee_custom_role(self):
		logger.debug("AccessPage : Click on new.")
		self.new_role_assign.click()
		logger.debug("AccessPage : Create 1st role.")
		logger.debug("AccessPage :  select AP-Group.")
		self.role_assign_attribute.set(self.config.config_vars.dropdown_ap_group)
		logger.debug("AccessPage :Set ap group .")
		self.string.set(self.config.config_vars.ap_group)
		logger.debug("AccessPage :Set role .")
		self.role_assign_name.set(self.config.config_vars.default_network_role)
		logger.debug("AccessPage : click ok.")
		self.ok1.click()
		
	def create_captive_portal(self,external=False):
		logger.debug("AccessPage : Click on new.")
		self.add_icon.click()
		if not self.rule_type:
			self.add_icon.click()
		logger.debug("AccessPage : Set rule type as captive portal.")		
		self.rule_type.set(self.config.config_vars.Access_Rule_Captive_portal)
		if external:
			logger.debug("AccessPage : Set splash page type as external.")
			self.captive_selection.set(self.config.config_vars.Captive_selection_External)
		
	def external_captive_portal_change_settings(self):
		logger.debug("AccessPage : Click on edit.")
		self.access_edit.click()
		logger.debug("AccessPage : Set Hostname value.")
		self.captive_ip.set(self.config.config_vars.action_ip4)
		logger.debug("AccessPage : Set captive portal failure as allow internet.")
		self.security_captive_portal_failure.set(self.config.config_vars.captive_portal_failure)
		logger.debug("AccessPage : Disable url white listing.")
		if not self.secuirty_auto_url_whitelisting.is_selected():
			logger.debug("AccessPage : Disable White listing.")
			self.secuirty_auto_url_whitelisting.click()
		logger.debug("AccessPage : Click save.")
		logger.debug("AccessPage : click save.")
		self.cap_save.click()
		logger.debug("AccessPage : click save setting button.")
		self.save_settings.click()
		logger.debug("AccessPage : click finish button.")
		self.finish_network_setup()
		
	def splash_page_settings(self):
		logger.debug("AccessPage :set banner title .")
		self.internal_banner_title.set(self.config.config_vars.banner_title)
		logger.debug("AccessPage : Write welcome text.")
		self.role_welcome_text.set(self.config.config_vars.welcome_text)
		logger.debug("AccessPage : Set policy text.")
		self.policy_text.set(self.config.config_vars.policy_text)
		logger.debug("AccessPage : Click save.")
		self.save_settings.click()
		
	def create_new_external_captive_portal(self):
		logger.debug("AccessPage :set captive portal profile as new.")
		self.captive_profile.set(self.config.config_vars.captive_portal_profile)
		logger.debug("AccessPage :set captive portal name.")
		self.captive_name.set(self.config.config_vars.Role_Name)
		logger.debug("AccessPage : Set Ip.")
		self.captive_ip.set(self.config.config_vars.captive_role_ip)
		logger.debug("AccessPage : Set Url.")
		self.captive_url.set(self.config.config_vars.redirect_url)
		logger.debug("AccessPage : Set port.")
		self.captive_port.set(self.config.config_vars.captive_role_port)
		logger.debug("AccessPage : Click save.")
		self.cap_save.click()

	def select_destination_nat(self):
		logger.debug("AccessPage : Choosing 'Destination-NAT' ")
		self.new_action_1.set(self.config.config_vars.action_dropdown_destination_nat)
		logger.debug("AccessPage : Writing ip address' ")
		self.action_ip4.set(self.config.config_vars.invalid_destination_ip)
		self._save_rule()
		if not self.ip_address_field_error:
			raise AssertionError("IP field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.action_ip4.set(self.config.config_vars.action_ip4)
		logger.debug("AccessPage : Writing port number' ")
		self.action_port4.set(self.config.config_vars.invalid_port)
		self._save_rule()
		if not self.ac_destination_port_error:
			raise AssertionError("Port field accepting invalid values.Traceback: %s " %traceback.format_exc())
		logger.debug("AccessPage : Writing port number' ")
		self.action_port4.set(self.config.config_vars.action_port4)
		
	def select_to_a_network(self):
		logger.debug("AccessPage : Choosing 'To a network' ")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_To_a_network)
		logger.debug("AccessPage : Writing ip address' ")
		self.destination_ip4.set(self.config.config_vars.invalid_destination_ip)
		self._save_rule()
		if not self.ip_addr_error_msg:
			raise AssertionError("IP field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_ip4.set(self.config.config_vars.destination_ip_2)
		logger.debug("AccessPage : Writing netmask' ")
		self.destination_netmask.set(self.config.config_vars.invalid_destination_ip)
		self._save_rule()
		if not self.netmaskd_error:
			raise AssertionError("Netmask field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_netmask.set(self.config.config_vars.dest2_net_mask)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
	
	def select_except_to_a_network(self):
		logger.debug("AccessPage : Choosing 'Except to a network' ")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_Except_to_a_network)
		logger.debug("AccessPage : Writing ip address' ")
		self.destination_ip4.set(self.config.config_vars.invalid_destination_ip)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
		if not self.ip_addr_error_msg:
			raise AssertionError("IP field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_ip4.set(self.config.config_vars.destination_ip_2)
		logger.debug("AccessPage : Writing netmask' ")
		self.destination_netmask.set(self.config.config_vars.invalid_destination_ip)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
		if not self.netmaskd_error:
			raise AssertionError("Netmask field accepting invalid values.Traceback: %s " %traceback.format_exc())
		logger.debug("AccessPage : Writing netmask' ")
		self.destination_netmask.set(self.config.config_vars.dest2_net_mask)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
			
	def create_dst_nat_any_to_a_network(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'Any' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_any)
		self.select_destination_nat()
		self.select_to_a_network()
			
	def create_dst_nat_custom_tcp_except_to_a_network(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'CUSTOM' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_custom)
		logger.debug("AccessPage : Choosing 'TCP' ")
		self.service_protocol.set(self.config.config_vars.protocols_tcp)
		logger.debug("AccessPage : Writing port number' ")
		self.custom_tcp_port.set(self.config.config_vars.invalid_port)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
		if not self.invalid_port_error:
			raise AssertionError(" Port field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.custom_tcp_port.set(self.config.config_vars.port)
		self.select_destination_nat()
		self.select_except_to_a_network()		
		
	def create_dst_nat_http_proxy_to_all_destinations(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'http-proxy' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_http_proxy)
		self.select_destination_nat()
		logger.debug("AccessPage : Choosing 'To all destinations' ")
		self.new_destination_1.set(self.config.config_vars.destination_default_value)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
	
	def create_dst_nat_h323_tcp_to_a_paticular_sever(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'h323-tcp' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_h323_tcp)
		self.select_destination_nat()
		logger.debug("AccessPage : Choosing 'To a particular server' ")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_To_a_particular_server)
		logger.debug("AccessPage : Writing ip address' ")
		self.destination_ip4.set(self.config.config_vars.invalid_destination_ip)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
		if not self.ip_addr_error_msg:
			raise AssertionError("IP field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_ip4.set(self.config.config_vars.destination_ip)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
		
	def create_dst_nat_ike_except_to_a_particular_server(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'ike' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_ike)
		self.select_destination_nat()
		logger.debug("AccessPage : Choosing 'Except to a particular server' ")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_Except_to_a_particular_server)
		logger.debug("AccessPage : Writing ip address' ")
		self.destination_ip4.set(self.config.config_vars.invalid_destination_ip)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
		if not self.ip_addr_error_msg:
			raise AssertionError("IP field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_ip4.set(self.config.config_vars.destination_ip)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
		
	def create_dst_nat_kerberos_to_a_domain_name(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'kerberos' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_kerberos)
		self.select_destination_nat()
		logger.debug("AccessPage : Choosing 'To a Domain Name' ")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_To_a_Domain_Name)
		logger.debug("AccessPage : Writing Domain name' ")
		self.domain_name.set(self.config.config_vars.invalid_domain_name)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
		if not self.invalid_domain_name_error:
			raise AssertionError("Domain Name field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.domain_name.set(self.config.config_vars.domain_names)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
		
	def create_dst_nat_lpd_tcp_to_all_destinations(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'lpd-tcp' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_lpd_tcp)
		self.select_destination_nat()
		logger.debug("AccessPage : Choosing 'To all destinations' ")
		self.new_destination_1.set(self.config.config_vars.destination_default_value)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
		
	def create_dst_nat_netbios_dgm_to_a_particular_server(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'netbios-dgm' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_netbios_dgm)
		self.select_destination_nat()
		logger.debug("AccessPage : Choosing 'To a particular server' ")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_To_a_particular_server)
		logger.debug("AccessPage : Writing ip address' ")
		self.destination_ip4.set(self.config.config_vars.invalid_destination_ip)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
		if not self.ip_addr_error_msg:
			raise AssertionError("IP field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_ip4.set(self.config.config_vars.destination_ip)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
		
	def create_dst_nat_netbios_ssn_except_to_a_particular_server(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing ' netbios-ssn' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_netbios_ssn)
		self.select_destination_nat()
		logger.debug("AccessPage : Choosing 'Except to a particular server' ")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_Except_to_a_particular_server)
		logger.debug("AccessPage : Writing ip address' ")
		self.destination_ip4.set(self.config.config_vars.invalid_destination_ip)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
		if not self.ip_addr_error_msg:
			raise AssertionError("IP field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_ip4.set(self.config.config_vars.destination_ip)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
		
	def create_dst_nat_pop3_to_a_network(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'pop3' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_pop3)
		self.select_destination_nat()
		self.select_to_a_network()
		
	def create_dst_nat_sips_except_to_a_network(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'sips' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_sips)
		self.select_destination_nat()
		self.select_except_to_a_network()
		
	def create_dst_nat_smb_udp_to_a_domain_name(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'smb-udp' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_smb_udp)
		self.select_destination_nat()
		logger.debug("AccessPage : Choosing 'To a Domain Name' ")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_To_a_Domain_Name)
		logger.debug("AccessPage : Writing Domain name' ")
		self.domain_name.set(self.config.config_vars.invalid_domain_name)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
		if not self.invalid_domain_name_error:
			raise AssertionError("Domain Name field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.domain_name.set(self.config.config_vars.domain_names)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
		
	def create_dst_nat_telnet_to_a_particular_server(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'telnet' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_telnet)
		self.select_destination_nat()
		logger.debug("AccessPage : Choosing 'To a particular server' ")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_To_a_particular_server)
		logger.debug("AccessPage : Writing ip address' ")
		self.destination_ip4.set(self.config.config_vars.invalid_destination_ip)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
		if not self.ip_addr_error_msg:
			raise AssertionError("IP field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.destination_ip4.set(self.config.config_vars.destination_ip)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
	
	def create_dst_nat_snmp_trap_except_to_a_network(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'snmp-trap' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_snmp_trap)
		self.select_destination_nat()
		self.select_except_to_a_network()
		
	def create_dst_nat_smtp_to_a_network(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'smtp' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_smtp)
		self.select_destination_nat()
		self.select_to_a_network()
		
	def create_dst_nat_custom_other_to_a_network(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'CUSTOM' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_custom)
		logger.debug("AccessPage : Choosing 'OTHER' ")
		self.service_protocol.set(self.config.config_vars.protocols_other)
		logger.debug("AccessPage : Writing protocol id' ")
		self.protocol_id.set(self.config.config_vars.invalid_protocol_id)
		logger.debug("AccessPage : Click save.")
		self._save_rule()
		if not self.protocol_id_error_msg:
			raise AssertionError(" Protocol ID field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.protocol_id.set(self.config.config_vars.protocol_id)
		self.select_destination_nat()
		self.select_to_a_network()
		
	def create_action_source_nat_rule(self, service, destination, protocol = None, options = False):
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Calling method to Asserting 'RULE TYPE' default values...")
		self._assert_default_rule_settings()
		logger.debug("AccessPage : set 'ACTION' drop-down to 'Source-NAT'...")
		self.new_action_1.set(self.config.config_vars.action_source_nat)
		logger.debug("AccessPage : set 'SERVICE' drop-down to '%s'..." %service)
		self.new_service_1.set(service)
		if protocol == 'OTHER':
			logger.debug("AccessPage : set 'Protocal' drop-down to 'other'...")
			self.service_protocol.set(self.config.config_vars.service_protocol)
			logger.debug("AccessPage : set 'Protocol ID' textbox to '26'...")
			self.protocol_id.set(self.config.config_vars.action_source_nat_port)
		elif protocol == 'UDP':
			logger.debug("AccessPage : set 'Protocal' drop-down to 'UDP'...")
			self.service_protocol.set(self.config.config_vars.service_protocol_udp)
			logger.debug("AccessPage : set 'PORT' textbox to '8600'...")
			self.custom_tcp_port.set(self.config.config_vars.service_port)
		logger.debug("AccessPage : set 'DESTINATION' drop-down to '%s'..." %destination)
		self.new_destination_1.set(destination)
		if ((destination == 'To a particular server') or (destination == 'Except to a particular server')):
			logger.debug("AccessPage : Write ip in 'IP' textbox...")
			self.destination_ip4.set(self.config.config_vars.dest_ip)
		elif ((destination == 'To a network') or (destination == 'Except to a network')):
			logger.debug("AccessPage : Write ip in 'IP' textbox...")
			self.destination_ip4.set(self.config.config_vars.dest_ip)
			logger.debug("AccessPage : Write ip in 'NETMASK' textbox...")
			self.destination_netmask.set(self.config.config_vars.dest_netmask)
		elif destination == 'To a Domain Name':
			logger.debug("AccessPage : Write domain name...")
			self.domain_name.set(self.config.config_vars.Access_Rule_Domain_Name)
		if options:
			self._select_options()
		logger.debug("AccessPage : Click save.")
		self._save_rule()
		
	def check_default_rule(self):
		import time
		import traceback
		time.sleep(5)
		logger.debug('AccessPage : Clicking on Network based radio')
		self.network_based.click()
		time.sleep(8)
		if not self.allow_any_to_all_destination_msg:
			raise AssertionError("Allow any to all destinations message is not visible.Traceback: %s " %traceback.format_exc())
		time.sleep(2)
		logger.debug('AccessPage : Clicking on Finish button')
		self.finish_network_setup()
		
	def change_network_rule(self):
		import time
		time.sleep(5)
		logger.debug('AccessPage : Clicking on Network based radio')
		self.network_based.click()
		time.sleep(5)
		logger.debug('AccessPage : Clicking on Edit button')
		self.buy_time()
		self.edit_pencil.click()
		logger.debug('AccessPage : Setting custom-tcp in service dropdown')
		self.new_service_1.set(self.config.config_vars.service_custom_value)
		logger.debug('AccessPage : Entering invalid value')
		self.custom_tcp_port.set('0')
		logger.debug('AccessPage : Clicking on save button')
		self.save1.click()
		time.sleep(5)
		if not self.invalid_port_error:
			raise AssertionError("Invalid port error is not visible.Traceback: %s " %traceback.format_exc())
		time.sleep(2)
		logger.debug('AccessPage : Entering valid value')
		self.custom_tcp_port.set(self.config.config_vars.custom_port_value)
		logger.debug('AccessPage : Setting action to deny')
		self.new_action_1.set(self.config.config_vars.action_deny)
		logger.debug('AccessPage : Setting destination to a perticular server')
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_To_a_particular_server)
		logger.debug('AccessPage : Entering invalid ip')
		self.destination_ip4.set('0')
		logger.debug('AccessPage : Clicking on save button')		
		self.save1.click()
		time.sleep(5)
		if not self.ip_addr_error_msg:
			raise AssertionError("Invalid ip error is not visible.Traceback: %s " %traceback.format_exc())
		time.sleep(2)
		logger.debug('AccessPage : Entering valid ip address')
		self.destination_ip4.set(self.config.config_vars.ip_valid_value)
		logger.debug('AccessPage : Clicking on  Enabling options')
		self.new_log_1.click()
		self.new_classify_media_1.click()
		self.new_dscp_tag_1.click()
		self.blacklist_3.click()
		self.new_disable_scaning_1.click()
		self.new_dot1_priority_1.click()
		logger.debug('AccessPage : Clicking on save button')			
		self.save1.click()
		if not self.new_created_deny_tcp_role:
			raise AssertionError("Newly created rule name is not visible.Traceback: %s " %traceback.format_exc())			
		time.sleep(2)
		logger.debug('AccessPage : Clicking on Finish button')
		self.finish_network_setup()
		
		
	def create_new_rule(self):
		import time
		time.sleep(5)
		logger.debug('AccessPage : Clicking on Network based radio')
		self.network_based.click()
		time.sleep(5)
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		time.sleep(2)
		logger.debug('AccessPage : Choosing bootp option from service dropdown')
		self.service_role2.set(self.config.config_vars.service_h323_udp)
		logger.debug('AccessPage : Choosing Source-NAT from action dropdown')
		self.action_role2.set(self.config.config_vars.service_action_value)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		if not self.new_created_allow_h323_udp:
			raise AssertionError("Newly created rule name is not visible.Traceback: %s " %traceback.format_exc())			
		time.sleep(2)
		logger.debug('AccessPage : Clicking on Finish button')
		self.finish_network_setup()	
					
		
	def create_new_rule_with_domain(self):
		import time
		time.sleep(5)
		logger.debug('AccessPage : Clicking on Network based radio')
		self.network_based.click()
		time.sleep(5)
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		time.sleep(2)
		logger.debug('AccessPage : Choosing bootp option from service dropdown')
		self.service_role2.set(self.config.config_vars.service_smb_tcp)
		logger.debug('AccessPage : Choosing Deny from action dropdown')
		self.action_role2.set(self.config.config_vars.action_deny)
		logger.debug('AccessPage : Choosing To a domain name from action dropdown')
		self.destination_role_2.set(self.config.config_vars.destination_domain_option)
		logger.debug('AccessPage : Entering invalid value in domain textbox')
		self.domain_name.set('x')
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		if not self.invalid_domain_name_error:
			raise AssertionError("Invalid domain name message is not visible.Traceback: %s " %traceback.format_exc())			
		time.sleep(2)
		logger.debug('AccessPage : Entering valid value in domain textbox')
		self.domain_name.set(self.config.config_vars.valid_domain_name)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		if not self.new_created_deny_smb_domain:
			raise AssertionError("Newly created rule name is not visible.Traceback: %s " %traceback.format_exc())		
		logger.debug('AccessPage : Clicking on Finish button')
		self.finish_network_setup()
		
		
	def delete_existing_rule(self):
		import time
		logger.debug('AccessPage : Clicking on delete(X) button')
		self.rule_delete_button.click()
		time.sleep(2)
		logger.debug('AccessPage : Clicking on Finish button')
		self.finish_network_setup()
		
		
	def create_rule_h323_udp(self):
		import time
		time.sleep(5)
		logger.debug('AccessPage : Clicking on Network based radio')
		self.network_based.click()
		time.sleep(5)
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		time.sleep(2)
		logger.debug('AccessPage : Choosing bootp option from service dropdown')
		self.service_role2.set(self.config.config_vars.service_h323_udp)
		logger.debug('AccessPage : Choosing Source-NAT from action dropdown')
		self.action_role2.set(self.config.config_vars.service_action_value)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()	
		time.sleep(2)
		if not self.new_created_allow_h323:
			raise AssertionError("Newly created rule name message is not visible.Traceback: %s " %traceback.format_exc())			
		time.sleep(2)
		logger.debug('AccessPage : Clicking on Finish button')
		self.finish_network_setup()
		time.sleep(5)
		
	def create_different_rules(self):
		self._create_diff_rule_types()
		logger.debug('AccessPage : Clicking on Finish button')
		self.finish_network_setup()
		time.sleep(5)
		
	def create_deny_adp_to_all_destinations(self):
		logger.debug("AccessPage : Calling method to Delete Default Rule")
		self.delete_default_rule_if_present()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		self._assert_default_rule_settings()
		logger.debug("AccessPage : Choosing 'adp' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_adp)
		logger.debug("AccessPage : Choosing 'DENY' ")
		self.new_action_1.set(self.config.config_vars.action_deny)
		logger.debug("AccessPage : Choosing 'To all destinations' ")
		self.new_destination_1.set(self.config.config_vars.destination_default_value)
		logger.debug('AccessPage : Clicking on Save button')
		self._save_rule()
		
	def validate_ports_udp(self, port_num, protocol, validity):
		logger.debug("AccessPage : click on 'Edit' icon...")
		self.buy_time()
		logger.debug('AccessPage : Clicking on Edit icon')
		self.edit_pencil.click()
		logger.debug("AccessPage : set 'SERVICE' drop-down to 'CUSTOM'...")
		self.new_service_1.set(self.config.config_vars.service_custom)
		logger.debug("AccessPage : set 'PROTOCOL' drop-down to '%s'..." %protocol)
		if protocol == 'udp':
			self.service_protocol.set(self.config.config_vars.service_protocol_udp)
		else:
			self.service_protocol.set(self.config.config_vars.protocols_tcp)
		logger.debug("AccessPage : write 'Port' number...")
		self.custom_tcp_port.set(port_num)
		logger.debug("AccessPage : Click 'Save' button...")
		self.save1.click()
		if validity == 'valid':
			if self.port_range_error_msg_new:
				raise AssertionError("'* Valid range is 1-65534' message present.Traceback: %s " %traceback.format_exc())
		if validity == 'invalid':
			if not self.port_range_error_msg_new:
				raise AssertionError("'* Valid range is 1-65534' message not present.Traceback: %s " %traceback.format_exc())
				
	def validate_vlan_network_based_assignment(self):
		logger.debug("AccessPage : click on 'Edit' icon...")
		self.buy_time()
		logger.debug('AccessPage : Clicking on Edit icon')
		self.edit_pencil.click()
		logger.debug("AccessPage : set 'RULE TYPE' drop-down to 'VLAN Assignment'...")
		self.new_rule_type_1.set(self.config.config_vars.access_rule_type_vlan_assignment)
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlan_id_4.set(self.config.config_vars.vlan_id_alpha)
		logger.debug("VirtualLanPage : Clicking save button...")
		self.save1.click()
		if not self.invalid_vlan_id_error_4:
			raise AssertionError("Vlan ID range error not found. i.e . Traceback: %s" % traceback.format_exc())
		
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlan_id_4.set(self.config.config_vars.vlan_id_num_invalid)
		logger.debug("VirtualLanPage : Clicking save button...")
		self.save1.click()
		if not self.invalid_vlan_id_error_4:
			raise AssertionError("Vlan ID range error not found. i.e . Traceback: %s" % traceback.format_exc())
		
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlan_id_4.set(self.config.config_vars.vlan_id_num_except)
		logger.debug("VirtualLanPage : Clicking save button...")
		self.save1.click()
		if not self.reserve_vlan_id_error:
			raise AssertionError("'VLAN 3333 is reserved' error message not found. i.e . Traceback: %s" % traceback.format_exc())
		
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlan_id_4.set(self.config.config_vars.vlan_id_spcl_char)
		logger.debug("VirtualLanPage : Clicking save button...")
		self.save1.click()
		if not self.invalid_vlan_id_error_4:
			raise AssertionError("Vlan ID range error not found. i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlan_id_4.set('')
		logger.debug("VirtualLanPage : Clicking save button...")
		self.save1.click()
		if not self.invalid_vlan_id_error_4:
			raise AssertionError("Vlan ID range error not found. i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlan_id_4.set(self.config.config_vars.Vlan_Id)
		logger.debug("VirtualLanPage : Clicking save button...")
		self.save1.click()
		if self.invalid_vlan_id_error_4 or self.reserve_vlan_id_error:
			raise AssertionError("Vlan ID as number was not accepted. i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("VirtualLanPage : Clicking edit icon...")
		self.edit_icon_vlan.click()
		logger.debug("AccessPage : set 'RULE TYPE' drop-down to 'Access Control'...")
		self.new_rule_type_vlan.set(self.config.config_vars.rule_type)
		logger.debug("VirtualLanPage : Clicking save button...")
		self.save_vlan.click()
		
	def validate_ip_address_network_based_access_rule(self):
		logger.debug("AccessPage : click on 'Edit' icon...")
		self.buy_time()
		logger.debug('AccessPage : Clicking on Edit icon')
		self.edit_pencil.click()
		logger.debug("AccessPage : set 'ACTION' drop-down to 'Destination-NAT'...")
		self.new_action_1.set(self.config.config_vars.action)
		logger.debug("AccessPage : Writing alphabet in IP Address textbox...")
		self.action_ip4.set(self.config.config_vars.port_alpha)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.ip_address_field_error:
			raise AssertionError("'Invalid IP address' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing number in IP Address textbox...")
		self.action_ip4.set(self.config.config_vars.port_num_valid)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.ip_address_field_error:
			raise AssertionError("'Invalid IP address' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing in-range number in IP Address textbox...")
		self.action_ip4.set(self.config.config_vars.ip_invalid)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.ip_address_field_error:
			raise AssertionError("'Invalid IP address' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing special characters in IP Address textbox...")
		self.action_ip4.set(self.config.config_vars.port_char)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.ip_address_field_error:
			raise AssertionError("'Invalid IP address' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing null characters in IP Address textbox...")
		self.action_ip4.set('')
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.ip_address_field_error:
			raise AssertionError("'Invalid IP address' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing valid ip address in IP Address textbox...")
		self.action_ip4.set(self.config.config_vars.ip_valid_value)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if self.ip_address_field_error:
			raise AssertionError("'Invalid IP address' error message found... i.e . Traceback: %s" % traceback.format_exc())
			
	def validate_port_network_based_access_rule(self):
		logger.debug("AccessPage : click on 'Edit' icon...")
		self.buy_time()
		logger.debug('AccessPage : Clicking on Edit icon')
		self.edit_pencil.click()
		logger.debug("AccessPage : set 'ACTION' drop-down to 'Destination-NAT'...")
		self.new_action_1.set(self.config.config_vars.action)
		logger.debug("AccessPage : Writing alphabet in Port textbox...")
		self.action_port4.set(self.config.config_vars.port_alpha)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.ac_destination_port_error:
			raise AssertionError("'Invalid IP address' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing invalid number in Port textbox...")
		self.action_port4.set(self.config.config_vars.port_num_invalid)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.ac_destination_port_error:
			raise AssertionError("'Invalid IP address' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing invalid number in Port textbox...")
		self.action_port4.set(self.config.config_vars.port_num_invalid_0)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.ac_destination_port_error:
			raise AssertionError("'Invalid IP address' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing special characters in Port textbox...")
		self.action_port4.set(self.config.config_vars.port_char)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.ac_destination_port_error:
			raise AssertionError("'Invalid IP address' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing null characters in Port textbox...")
		self.action_port4.set('')
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.ac_destination_port_error:
			raise AssertionError("'Invalid IP address' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing valid ip address in Port textbox...")
		self.action_port4.set(self.config.config_vars.port_num_valid)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if self.ac_destination_port_error:
			raise AssertionError("'Invalid IP address' error message found... i.e . Traceback: %s" % traceback.format_exc())
			
	def validate_protocol_id(self):
		logger.debug("AccessPage : click on 'Edit' icon...")
		self.buy_time()
		logger.debug('AccessPage : Clicking on Edit icon')
		self.edit_pencil.click()
		logger.debug("AccessPage : set 'SERVICES' drop-down to 'CUSTOM'...")
		self.new_service_1.set(self.config.config_vars.service_role_CUSTOM)
		logger.debug("AccessPage : set 'PROTOCOL' drop-down to 'OTHER'...")
		self.service_protocol.set(self.config.config_vars.protocols_other)
		logger.debug("AccessPage : Write alphabet in 'Protocol Id' textbox...")
		self.protocol_id.set(self.config.config_vars.port_alpha)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.protocol_id_error:
			raise AssertionError("'Valid range is 1 - 255' error message not found. i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Write invalid number in 'Protocol Id' textbox...")
		self.protocol_id.set(self.config.config_vars.port_num_invalid_0)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.protocol_id_error:
			raise AssertionError("'Valid range is 1 - 255' error message not found. i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Write invalid number in 'Protocol Id' textbox...")
		self.protocol_id.set(self.config.config_vars.protocol_id_invalid)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.protocol_id_error:
			raise AssertionError("'Valid range is 1 - 255' error message not found. i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Write special chars in 'Protocol Id' textbox...")
		self.protocol_id.set(self.config.config_vars.port_char)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.protocol_id_error:
			raise AssertionError("'Valid range is 1 - 255' error message not found. i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Write more than 3 chars in 'Protocol Id' textbox...")
		self.protocol_id.set(self.config.config_vars.port_num_valid)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.protocol_id_error:
			raise AssertionError("'Valid range is 1 - 255' error message not found. i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Write null chars in 'Protocol Id' textbox...")
		self.protocol_id.set('')
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.protocol_id_error:
			raise AssertionError("'Valid range is 1 - 255' error message not found. i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Write valid number in 'Protocol Id' textbox...")
		self.protocol_id.set(self.config.config_vars.service_protocol_id)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if self.protocol_id_error:
			raise AssertionError("'Valid range is 1 - 255' error message not found. i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("VirtualLanPage : Clicking edit icon...")
		self.buy_time()
		logger.debug('AccessPage : Clicking on Edit icon')
		self.edit_pencil.click()
		logger.debug("AccessPage : set 'SERVICE' drop-down to 'Any'...")
		self.new_service_1.set(self.config.config_vars.service_default_value)
		logger.debug("VirtualLanPage : Clicking save button...")
		self.save1.click()
		
	def validate_ip_network_based_access_rule(self):
		logger.debug("AccessPage : click on 'Edit' icon...")
		self.buy_time()
		logger.debug('AccessPage : Clicking on Edit icon')
		self.edit_pencil.click()
		logger.debug("AccessPage : set 'Destination' drop down to 'To a particular server'...")
		self.new_destination_1.set(self.config.config_vars.dest_particular_server)
		logger.debug("AccessPage : Writing alphabet in IP Address textbox...")
		self.destination_ip4.set(self.config.config_vars.port_alpha)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.ip_addr_error_msg:
			raise AssertionError("'Invalid IP address' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing number in IP Address textbox...")
		self.destination_ip4.set(self.config.config_vars.port_num_valid)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.ip_addr_error_msg:
			raise AssertionError("'Invalid IP address' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing in-range number in IP Address textbox...")
		self.destination_ip4.set(self.config.config_vars.ip_invalid)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.ip_addr_error_msg:
			raise AssertionError("'Invalid IP address' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing special characters in IP Address textbox...")
		self.destination_ip4.set(self.config.config_vars.port_char)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.ip_addr_error_msg:
			raise AssertionError("'Invalid IP address' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing null characters in IP Address textbox...")
		self.destination_ip4.set('')
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.ip_addr_error_msg:
			raise AssertionError("'Invalid IP address' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing valid ip address in IP Address textbox...")
		self.destination_ip4.set(self.config.config_vars.ip_valid_value)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if self.ip_addr_error_msg:
			raise AssertionError("'Invalid IP address' error message found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("VirtualLanPage : Clicking edit icon...")
		self.buy_time()
		logger.debug('AccessPage : Clicking on Edit icon')
		self.edit_pencil.click()
		logger.debug("AccessPage : set 'DESTINATION' drop-down to 'To all destinations'...")
		self.new_destination_1.set(self.config.config_vars.destination_default_value)
		logger.debug("VirtualLanPage : Clicking save button...")
		self.save1.click()
		
	def validate_netmask_network_based_access_rule(self):
		logger.debug("AccessPage : click on 'Edit' icon...")
		self.buy_time()
		logger.debug('AccessPage : Clicking on Edit icon')
		self.edit_pencil.click()
		logger.debug("AccessPage : set 'Destination' drop down to 'To a network'...")
		self.new_destination_1.set(self.config.config_vars.dest_to_a_ntwrk)
		logger.debug("AccessPage : Writing alphabet in Netmask textbox...")
		self.destination_netmask.set(self.config.config_vars.port_alpha)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.netmaskd_error:
			raise AssertionError("'Enter a valid netmask' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing number in Netmask textbox...")
		self.destination_netmask.set(self.config.config_vars.protocol_id_invalid)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.netmaskd_error:
			raise AssertionError("'Enter a valid netmask' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing in-range number in Netmask textbox...")
		self.destination_netmask.set(self.config.config_vars.ip_invalid)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.netmaskd_error:
			raise AssertionError("'Enter a valid netmask' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing invalid ip in Netmask textbox...")
		self.destination_netmask.set(self.config.config_vars.invalid_ip)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.netmaskd_error:
			raise AssertionError("'Enter a valid netmask' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing special characters in Netmask textbox...")
		self.destination_netmask.set(self.config.config_vars.port_char)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.netmaskd_error:
			raise AssertionError("'Enter a valid netmask' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing null characters in Netmask textbox...")
		self.destination_netmask.set('')
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.netmaskd_error:
			raise AssertionError("'Enter a valid netmask' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing valid netmask in Netmask textbox...")
		self.destination_netmask.set(self.config.config_vars.dest_netmask)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if self.netmaskd_error:
			raise AssertionError("'Enter a valid netmask' error message found... i.e . Traceback: %s" % traceback.format_exc())
			
	def validate_domain_network_based_access_rule(self):
		logger.debug("AccessPage : click on 'Edit' icon...")
		self.buy_time()
		logger.debug('AccessPage : Clicking on Edit icon')
		self.edit_pencil.click()
		logger.debug("AccessPage : set 'Destination' drop down to 'To a domain name'...")
		self.new_destination_1.set(self.config.config_vars.destination_domain_option)
		logger.debug("AccessPage : Writing alphabet in 'Domain Name' textbox...")
		self.domain_name.set(self.config.config_vars.domain_name_alpha)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if self.invalid_domain_name_error:
			raise AssertionError("'Invalid Domain name' error message found... i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("AccessPage : click on 'Edit' icon...")
		self.buy_time()
		logger.debug('AccessPage : Clicking on Edit icon')
		self.edit_pencil.click()
			
		logger.debug("AccessPage : Writing numbers in 'Domain Name' textbox...")
		self.domain_name.set(self.config.config_vars.domain_name_num)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if self.invalid_domain_name_error:
			raise AssertionError("'Invalid Domain name' error message found... i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("AccessPage : click on 'Edit' icon...")
		self.buy_time()
		logger.debug('AccessPage : Clicking on Edit icon')
		self.edit_pencil.click()
			
		logger.debug("AccessPage : Writing invalid special chars in 'Domain Name' textbox...")
		self.domain_name.set(self.config.config_vars.port_char)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.invalid_domain_name_error:
			raise AssertionError("'Invalid Domain name' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing valid special chars in 'Domain Name' textbox...")
		self.domain_name.set(self.config.config_vars.domain_name_spcl_char)
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if self.invalid_domain_name_error:
			raise AssertionError("'Invalid Domain name' error message found... i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("AccessPage : click on 'Edit' icon...")
		self.buy_time()
		logger.debug('AccessPage : Clicking on Edit icon')
		self.edit_pencil.click()
		
		logger.debug("AccessPage : Writing null char in 'Domain Name' textbox...")
		self.domain_name.set('')
		logger.debug("AccessPage : Clicking save button...")
		self.save1.click()
		if not self.domain_name_req_err:
			raise AssertionError("'This field is required' error message not found... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : set 'DESTINATION' drop-down to 'To all destinations'...")
		self.new_destination_1.set(self.config.config_vars.destination_default_value)
		logger.debug("VirtualLanPage : Clicking save button...")
		self.save1.click()
		
	def validate_role_assignment_string(self):
		logger.debug("AccessPage : click 'New' button under Role Assignment Rules...")
		self.new_role_assign.click()
		logger.debug("AccessPage : Writing null char in string text box...")
		self.string.set('')
		logger.debug("AccessPage : Clicking 'Save' button...")
		self.ok1.click()
		if not self.string_req_err:
			raise AssertionError("Null character was not accepted... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing more than 32 char string in string text box...")
		self.string.set(self.config.config_vars.string_max_len)
		logger.debug("AccessPage : Clicking 'Save' button...")
		self.ok1.click()
		if not self.maximum_32_chars:
			raise AssertionError("More than 32 character was accepted... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing special chars in string text box...")
		self.string.set(self.config.config_vars.role_assignment_string_spcl)
		logger.debug("AccessPage : Clicking 'Save' button...")
		self.ok1.click()
		if self.string_quote_err:
			raise AssertionError("Special character was not accepted... i.e . Traceback: %s" % traceback.format_exc())
		self.edit_role_assignment.click()
		
		logger.debug("AccessPage : Writing quotes in string text box...")
		self.string.set(self.config.config_vars.role_assignment_string_quotes)
		logger.debug("AccessPage : Clicking 'Save' button...")
		self.ok1.click()
		if not self.string_quote_err:
			raise AssertionError("Special character-quotes was accepted... i.e . Traceback: %s" % traceback.format_exc())		
		
		logger.debug("AccessPage : Writing alphabet in string text box...")
		self.string.set(self.config.config_vars.port_alpha)
		logger.debug("AccessPage : Clicking 'Save' button...")
		self.ok1.click()
		if self.maximum_32_chars:
			raise AssertionError("Alphabet was not accepted... i.e . Traceback: %s" % traceback.format_exc())
		self.edit_role_assignment.click()
		
		logger.debug("AccessPage : Writing numbers in string text box...")
		self.string.set(self.config.config_vars.port_num_valid)
		logger.debug("AccessPage : Clicking 'Save' button...")
		self.ok1.click()
		if self.maximum_32_chars:
			raise AssertionError("Number was not accepted... i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("AccessPage : Deleting the role...")
		# self.delete_role_assignment.click()
		
	def validate_role_assignment_string_mac_and_dhcp(self):
		logger.debug("AccessPage : click 'New' button under Role Assignment Rules...")
		self.new_role_assign.click()
		logger.debug("AccessPage : set attribute to 'mac address and dhcp options'...")
		self.role_assign_attribute.set(self.config.config_vars.dropdown_mac_address_and_dhcp_options)
		logger.debug("AccessPage : Writing null char in string text box...")
		self.string.set('')
		logger.debug("AccessPage : Clicking 'Save' button...")
		self.ok1.click()
		if not self.string_req_err:
			raise AssertionError("Null character was not accepted... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing more than 255 char string in string text box...")
		self.string.set(self.config.config_vars.string_max_len_mac)
		logger.debug("AccessPage : Clicking 'Save' button...")
		self.ok1.click()
		if not self.string_max_255_err:
			raise AssertionError("More than 255 character was accepted... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing special chars in string text box...")
		self.string.set(self.config.config_vars.role_assignment_string_spcl)
		logger.debug("AccessPage : Clicking 'Save' button...")
		self.ok1.click()
		if self.maximum_32_chars or self.string_quote_err:
			raise AssertionError("Special character was not accepted... i.e . Traceback: %s" % traceback.format_exc())
		self.edit_role_assignment.click()
		
		logger.debug("AccessPage : Writing alphabet in string text box...")
		self.string.set(self.config.config_vars.port_alpha)
		logger.debug("AccessPage : Clicking 'Save' button...")
		self.ok1.click()
		if self.maximum_32_chars:
			raise AssertionError("Alphabet was not accepted... i.e . Traceback: %s" % traceback.format_exc())
		self.edit_role_assignment.click()
		
		logger.debug("AccessPage : Writing numbers in string text box...")
		self.string.set(self.config.config_vars.port_num_valid)
		logger.debug("AccessPage : Clicking 'Save' button...")
		self.ok1.click()
		if self.maximum_32_chars:
			raise AssertionError("Number was not accepted... i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("AccessPage : Deleting the role...")
		self.delete_role_assignment.click()
		
	def assert_duplicate_rule_error_msg(self):
		'''
			Asserting duplicate rule error message
		'''
		logger.debug('Access Page : Clicking on Network Based')
		self.network_based.click()
		logger.debug('Access Page : Clicking on + icon')
		self.add_icon.click()
		logger.debug('Access Page : Clicking on Save button')
		self.save_settings.click()
		if not self.duplicate_rule_error_message:
			raise AssertionError("Duplicate error message is not visible .Traceback: %s " %traceback.format_exc())
			
			
	def assert_string_field_compulsion(self):
		logger.debug("AccessPage : Click on new.")
		self.new_role_assign.click()
		logger.debug("AccessPage : Create 1st role.")
		logger.debug("AccessPage :  select AP-Group.")
		self.role_assign_attribute.set(self.config.config_vars.dropdown_ap_group)
		logger.debug("AccessPage : Clicking 'Save' button...")
		self.ok1.click()
		if not self.string_req_err:
			raise AssertionError(" '*This Field is required' error not shown... i.e . Traceback: %s" % traceback.format_exc())
			
	def assert_string_field_check_for_the_character_length(self):
		logger.debug("AccessPage : Click on new.")
		self.new_role_assign.click()
		logger.debug("AccessPage : Create 1st role.")
		logger.debug("AccessPage :  select AP-Group.")
		self.role_assign_attribute.set(self.config.config_vars.dropdown_ap_group)
		logger.debug("AccessPage : Writing null or zero char in string text box...")
		self.string.set('')
		logger.debug("AccessPage : Clicking 'Save' button...")
		self.ok1.click()
		if not self.string_req_err:
			raise AssertionError("Less than 1 character was not accepted... i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("AccessPage : Writing more than 32 char string in string text box...")
		self.string.set(self.config.config_vars.string_max_len)
		logger.debug("AccessPage : Clicking 'Save' button...")
		self.ok1.click()
		if not self.maximum_32_chars:
			raise AssertionError("More than 32 character was accepted... i.e . Traceback: %s" % traceback.format_exc())

	def assign_created_role(self):
		'''
			Assigning newly created role to the network
		'''
		logger.debug('Access Page : Clicking on New button')
		self.new_role_assign.click()
		logger.debug('Access Page : Selecting operator')
		self.role_operator.set(self.config.config_vars.role_operator3)
		logger.debug('Access Page : Entering String')
		self.string.set(self.config.config_vars.role_string3)
		logger.debug('Access Page : Selecting role')
		self.role_assign_name.set(self.config.config_vars.role_name)
		logger.debug('Access Page : Clicking on OK button')
		self.ok1.click()
		
	def assert_delete_button_for_assigned_role(self):
		'''
			Asserting disable delete button for already assigned role
		'''
		logger.debug('Access Page : Selecting assigned role')
		self.assigned_role_name.click()
		if not self.role_delete_disable:
			import traceback
			raise AssertionError("Delete button visible .Traceback: %s " %traceback.format_exc())
			
	def click_on_cancel_button(self):
		'''
			Clicking on cancel button
		'''
		logger.debug('AccessPage : Clicking on Cancel button')
		self.cancel_button.click()
		
	def assert_duplicate_role_error_msg(self):
		'''
			Asserting duplicate role error message
		'''
		logger.debug("AccessPage : Click on new role.")
		self.create_new_role.click()
		logger.debug("AccessPage : Write role name.")
		self.role_input.set('default_wired_port_profile')
		logger.debug("AccessPage : click ok.")
		self.save_role.click()
		if not self.duplicate_role_error_message:
			import traceback
			raise AssertionError("Duplicate rule error message is not visible .Traceback: %s " %traceback.format_exc())
			
	def assert_access_rule_unrestricted(self):
		if not self.access_radio.is_selected():
			raise AssertionError("accesspage rulebased is not set to unrestricted i.e . Traceback: %s" % traceback.format_exc())
		
	def assert_allow_any_to_all_destination_msg(self):
		if not self.allow_any_to_all_destination_msg:
			raise AssertionError("after creating new role  'allow any to all destination' is not creted as default i.e . Traceback: %s" % traceback.format_exc())

	def click_role_radio_and_click_finish_button(self):
		'''
		clicking 'ROLE BASIC' in 'ACCESS RULES' and 'FINISH' button...
		'''
		logger.debug("AccessPage : Click on ROLE BASED radio button.")
		self.role_radio.click()
		logger.debug("AccessPage : Click on FINISH button.")
		self.finish.click()
		
	def set_rule_service_action_and_destination(self,service,action,destination):
		'''
		Setting service, action, destination dropdown option
		'''
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : set 'Service' drop-down")
		self.new_service_1.set(service)
		logger.debug("AccessPage : set 'Action' drop-down")
		self.new_action_1.set(action)
		logger.debug("AccessPage : Choosing 'To a particular server' ")
		self.new_destination_1.set(destination)
#		logger.debug('Set Destination ip')
#		self.destination_ip3.set(ip)
		
	def set_destination_ip_mask_domain(self,ip,mask,domain):
		'''
		Setting destination ip, mask, domain name
		'''
		if not ip == '':
			logger.debug('Setting Destination ip')
			self.destination_ip4.set(ip)
		if not mask == '':
			logger.debug('Setting Destination mask')
			self.destination_netmask.set(mask)				
		if not domain == '':
			logger.debug('Setting Destination domain')			
			self.domain_name.set(domain)
		logger.debug("AccessPage : Clicking on save button")
		self._save_rule()
		
	def create_source_nat_custom_udp_except_to_network(self):
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : set 'SERVICE' drop-down to 'CUSTOM'...")
		self.new_service_1.set(self.config.config_vars.service_custom)
		logger.debug("AccessPage : set 'PROTOCOL' drop-down to 'UDP'...")
		self.service_protocol.set(self.config.config_vars.service_protocol_udp)
		logger.debug("AccessPage : set 'PORT' textbox to '8600'...")
		self.custom_tcp_port.set(self.config.config_vars.service_port)
		logger.debug("AccessPage : set 'Action' drop-down to 'Source-NAT'...")
		self.new_action_1.set(self.config.config_vars.service_action_value)
		logger.debug("AccessPage : set 'Destination' drop-down to 'Except to a network'...")
		self.new_destination_1.set(self.config.config_vars.Destination_Role1_Except_to_a_network)
		logger.debug("AccessPage : Writing ip address' ")
		self.destination_ip4.set(self.config.config_vars.valid_destination_ip)
		logger.debug("AccessPage : Writing netmask' ")
		self.destination_netmask.set(self.config.config_vars.dest2_net_mask)
		self._save_rule()
		
	def assert_add_rule_plus_button(self):
		if not self.add_rule_plus_button:
			raise AssertionError('AccessPage: add rule plus sign is not present')
		
	def set_rule_type(self, value = 'None'):
		if value == 'VLAN Assignment':
			self.rule_type_dropdown.set(self.config.config_vars.access_rule_type_vlan_assignment)
		elif value == 'Captive portal':
			self.rule_type_dropdown.set(self.config.config_vars.Access_Rule_Captive_portal)
		elif value == 'CALEA':
			self.rule_type_dropdown.set(self.config.config_vars.rule_calea_type)
		else:
			self.rule_type_dropdown.set(self.config.config_vars.Access_Control)
	
	def create_captive_portal_rue_type(self,external=False):
		logger.debug("AccessPage : Click on new.")
		self.add_icon.click()
		if not self.rule_type:
			self.add_icon.click()
		logger.debug("AccessPage : Set rule type as captive portal.")		
		self.rule_type.set(self.config.config_vars.Access_Rule_Captive_portal)
		if external:
			logger.debug("AccessPage : Set splash page type as external.")
			self.captive_selection.set(self.config.config_vars.Captive_selection_External)
			self.save_settings.click()
		else:
			self.save_settings.click()

	def _create_diff_rule_types(self):
		import time
		time.sleep(5)
		logger.debug('AccessPage : Clicking on Network based radio')
		self.network_based.click()
		time.sleep(5)
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		time.sleep(2)
		logger.debug('AccessPage : Choosing adp option from service dropdown')
		self.service_role2.set(self.config.config_vars.service_adp_value)
		logger.debug('AccessPage : Choosing Deny from action dropdown')
		self.action_role2.set(self.config.config_vars.action_deny)
		time.sleep(2)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		time.sleep(2)
		logger.debug('AccessPage : Choosing cfgm-tcp option from service dropdown')
		self.service_role3.set(self.config.config_vars.service_cfgm_value)
		logger.debug('AccessPage : Choosing Source-NAT from action dropdown')
		self.action_role3.set(self.config.config_vars.service_action_value)
		time.sleep(2)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		time.sleep(2)
		logger.debug('AccessPage : Choosing dhcp option from service dropdown')
		self.service_role4.set(self.config.config_vars.service_dhcp_value)
		logger.debug('AccessPage : Choosing Destination-NAT from action dropdown')
		self.action_role4.set(self.config.config_vars.action_dropdown_destination_nat)
		time.sleep(2)
		logger.debug('Entering valid ip and port number')
		self.action_ip4.set(self.config.config_vars.ip_valid_value)
		self.action_port4.set(self.config.config_vars.custom_port_value)
		time.sleep(2)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		time.sleep(2)
		logger.debug('AccessPage : Choosing dns option from service dropdown')
		self.service_role5.set(self.config.config_vars.Service_Role1_dns)
		time.sleep(2)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		time.sleep(2)
		logger.debug('AccessPage : Choosing gre option from service dropdown')
		self.service_role6.set(self.config.config_vars.service_gre)
		time.sleep(2)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		time.sleep(2)
		logger.debug('AccessPage : Choosing h323-tcp option from service dropdown')
		self.service_role7.set(self.config.config_vars.service_h323_tcp_value)
		logger.debug('AccessPage : Choosing Deny from action dropdown')
		self.action_role7.set(self.config.config_vars.action_deny)
		time.sleep(2)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		time.sleep(2)
		logger.debug('AccessPage : Choosing bootp option from service dropdown')
		self.service_bootp_dropdown_6.set(self.config.config_vars.service_bootp_value)
		logger.debug('AccessPage : Enable all networks options')
		self.new_log_1.click()
		self.new_classify_media_1.click()
		self.new_dscp_tag_1.click()
		self.new_blacklist_1.click()
		# self.new_disable_scaning_2.click()
		self.new_dot1_priority_1.click()
		time.sleep(2)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		time.sleep(2)
		logger.debug('AccessPage : Choosing cups option from service dropdown')
		self.service_bootp_dropdown_7.set(self.config.config_vars.service_cups)
		logger.debug('AccessPage : Choosing Deny from action dropdown')
		self.action_dropdown_7.set(self.config.config_vars.action_deny)
		logger.debug('AccessPage : Enable all networks options')
		self.new_log_1.click()
		self.new_classify_media_1.click()
		self.new_dscp_tag_1.click()
		self.blacklist_3.click()
		# self.new_disable_scaning_3.click()
		self.new_dot1_priority_1.click()
		time.sleep(2)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		time.sleep(2)
		logger.debug('AccessPage : Choosing esp option from service dropdown')
		self.service_bootp_dropdown_8.set(self.config.config_vars.service_esp)
		logger.debug('AccessPage : Choosing Source-NAT from action dropdown')
		self.action_dropdown_8.set(self.config.config_vars.service_action_value)
		logger.debug('AccessPage : Enable all networks options')
		self.new_log_1.click()
		self.new_classify_media_1.click()
		self.new_dscp_tag_1.click()
		self.new_blacklist_1.click()	
		# self.new_disable_scaning_4.click()
		self.new_dot1_priority_1.click()
		time.sleep(2)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		time.sleep(2)
		logger.debug('AccessPage : Choosing h323_udp option from service dropdown')
		self.service_bootp_dropdown_9.set(self.config.config_vars.service_h323_udp_value)
		logger.debug('AccessPage : Choosing Destination-NAT from action dropdown')
		self.action_dropdown_9.set(self.config.config_vars.action_dropdown_destination_nat)
		logger.debug('Entering valid ip and port number')
		self.action_ip4.set(self.config.config_vars.ip_valid_value)
		self.action_port4.set(self.config.config_vars.custom_port_value)
		time.sleep(2)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		time.sleep(3)
				
	def create_wired_diff_rule_types(self):
		self._create_diff_rule_types()
		logger.debug('AccessPage: Clicking on Next Button')
		self.next.click()
		return NetworkAssignmentPage(self.test, self.browser, self.config)
	
	def create_wired_vlan_assignment(self):
		import time
		import traceback
		logger.debug('Access Page : Selecting role radio')
		self.role_radio.click()
		time.sleep(6)
		logger.debug('Access Page : Clicking on + icon')
		self.add_icon.click()
		logger.debug('Access Page : Choosing rule type VLAN Assignment')
		self.rule_type.set(self.config.config_vars.access_rule_type_vlan_assignment)
		logger.debug('Access Page : Entering invalid value in Vlan Id')
		self.vlan_id.set('0')
		logger.debug('Access Page : Clicking on Save button')
		self.save_settings.click()
		if not self.invalid_vlan_id_error:
			raise AssertionError("Invalid vlan id error is not present.Traceback: %s " %traceback.format_exc())
		logger.debug('Access Page : Entering valid value in Vlan Id')
		self.vlan_id.set(self.config.config_vars.valid_vlan_id)
		if not self.created_rule_vlan_assignment:
			raise AssertionError("Newly created rule is not present.Traceback: %s " %traceback.format_exc())
		logger.debug('Access Page : Clicking on Save button')
		self.save_settings.click()
					
	def assert_default_rule_edit_and_delete(self):
		if not self.default_rule_edit and self.default_rule_delete:
			raise AssertionError("AccessPage: Default rule edit and delete options are not enabled")

	def create_wireless_rules(self):
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		logger.debug('AccessPage : Choosing http option from service dropdown')
		self.new_service_1.set(self.config.config_vars.service_https)
		logger.debug('AccessPage : Choosing allow from action dropdown')
		self.new_action_1.set(self.config.config_vars.action_role_allow)
		logger.debug('AccessPage : Clicking on save button')			
		self.save1.click()
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		logger.debug('AccessPage : Choosing https option from service dropdown')
		self.service_role2.set(self.config.config_vars.service_http)
		logger.debug('AccessPage : Choosing allow from action dropdown')
		self.action_role2.set(self.config.config_vars.action_role_allow)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		logger.debug('AccessPage : Choosing http-proxy option from service dropdown')
		self.service_role3.set(self.config.config_vars.service_http_proxy)
		logger.debug('AccessPage : Choosing allow from action dropdown')
		self.action_role3.set(self.config.config_vars.action_role_allow)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		logger.debug('AccessPage : Choosing http-proxy3 option from service dropdown')
		self.service_role4.set(self.config.config_vars.Service_Role1_http_proxy3)
		logger.debug('AccessPage : Choosing allow from action dropdown')
		self.action_role4.set(self.config.config_vars.action_role_allow)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		logger.debug('AccessPage : Choosing gre option from service dropdown')
		self.service_role5.set(self.config.config_vars.service_dhcp_value)
		logger.debug('AccessPage : Choosing allow from action dropdown')
		self.action_role5.set(self.config.config_vars.action_role_allow)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		logger.debug('AccessPage : Choosing h323-tcp option from service dropdown')
		self.service_role6.set(self.config.config_vars.service_role_dns)
		logger.debug('AccessPage : Choosing Deny from action dropdown')
		self.action_role6.set(self.config.config_vars.action_role_allow)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		logger.debug('AccessPage : Choosing h323-tcp option from service dropdown')
		self.service_role7.set(self.config.config_vars.service_bootp)
		logger.debug('AccessPage : Choosing Deny from action dropdown')
		self.action_role7.set(self.config.config_vars.action_role_allow)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		logger.debug('AccessPage : Choosing h323-tcp option from service dropdown')
		self.service_bootp_dropdown_6.set(self.config.config_vars.Service_Role1_icmp)
		logger.debug('AccessPage : Choosing Deny from action dropdown')
		self.action_role8.set(self.config.config_vars.action_role_allow)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()		
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		logger.debug('AccessPage : Choosing http option from service dropdown')
		self.service_bootp_dropdown_7.set(self.config.config_vars.service_https)
		logger.debug('AccessPage : Choosing allow from action dropdown')
		self.action_dropdown_7.set(self.config.config_vars.action_deny)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		logger.debug('AccessPage : Choosing https option from service dropdown')
		self.service_bootp_dropdown_8.set(self.config.config_vars.service_http)
		logger.debug('AccessPage : Choosing allow from action dropdown')
		self.action_dropdown_8.set(self.config.config_vars.action_deny)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		logger.debug('AccessPage : Choosing http-proxy option from service dropdown')
		self.service_bootp_dropdown_9.set(self.config.config_vars.service_http_proxy)
		logger.debug('AccessPage : Choosing allow from action dropdown')
		self.action_dropdown_9.set(self.config.config_vars.action_deny)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
						
	def assert_default_rule_edit_and_delete(self):
		if not self.default_rule_edit and self.default_rule_delete:
			raise AssertionError("AccessPage: Default rule edit and delete options are not enabled")	

	
	def create_different_rule_types(self):
		import time
		time.sleep(5)
		logger.debug('AccessPage : Clicking on Network based radio')
		self.network_based.click()
		time.sleep(5)
		self.delete_default_rule_if_present()
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		time.sleep(2)
		self._assert_rule_fields()
		logger.debug("AccessPage : Choosing 'CUSTOM' ")
		self.new_service_1.set(self.config.config_vars.Service_Role1_custom)
		logger.debug("AccessPage : Choosing 'OTHER' ")
		self.service_protocol.set(self.config.config_vars.protocols_other)
		logger.debug("AccessPage : Writing protocol id' ")
		self.protocol_id.set(self.config.config_vars.invalid_protocol_id)
		logger.debug('AccessPage : Clicking on save button')
		self._save_rule()
		if not self.protocol_id_error_msg:
			raise AssertionError(" Protocol ID field accepting invalid values.Traceback: %s " %traceback.format_exc())
		self.protocol_id.set(self.config.config_vars.protocol_id)
		logger.debug('AccessPage : Clicking on + button')
		self._save_rule()
		self.buy_time()
		self.create_vlan_rule_assignment()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		logger.debug("AccessPage : Set rule type as captive portal.")		
		self.rule_type_dropdown.set(self.config.config_vars.Access_Rule_Captive_portal)
		logger.debug('AccessPage : Clicking on save setting button')
		self.save_settings.click()
		logger.debug("AccessPage : Calling method to Click on add button")
		self._add_new_rule()
		self.rule_type_dropdown.set(self.config.config_vars.rule_calea_type)
		logger.debug('AccessPage : Clicking on save setting button')
		self.save_settings.click()
		logger.debug("AccessPage : Delete vlan role rule...")
		self.delete_vlan_role_rule.click()
		logger.debug("AccessPage : Delete captive portal rule...")
		self.delete_captive_portal.click()
		logger.debug("AccessPage : Delete calea rule...")
		self.delete_calea_rule.click()
		logger.debug("AccessPage : Delete role assignment...")
		self.rule_delete_button.click()

	def set_destination_nat_ip_port(self):
		'''
			Setting Destination ip and port
		'''
		logger.debug('AccessPage : Entering Destination NAT ip and port')
		self.action_ip4.set(self.config.config_vars.action_ip4)
		self.action_port4.set(self.config.config_vars.action_port4)
		
	def set_action_ip_port(self,ip,port):
		'''
		Setting action ip and port number
		'''
		if not ip == '':
			logger.debug('Setting Action ip')
			self.action_ip4.set(ip)
		if not port == '':
			logger.debug('Setting Action port')
			self.action_port4.set(port)				
		logger.debug("AccessPage : Clicking on save button")
		self._save_rule()	
		
	def set_port(self,value):
		logger.debug("AccessPage : set 'PORT' number")
		self.custom_tcp_port.set(value)
		
	def check_custom_options_validity(self):
		logger.debug("AccessPage : set 'PROTOCOL' drop-down to 'TCP'...")
		self.service_protocol.set(self.config.config_vars.protocols_tcp)
		self.custom_tcp_port.set(self.config.config_vars.invalid_upstream)
		logger.debug("AccessPage : Click 'Save' button...")
		self.save1.click()
		if not self.invalid_port_error:
			raise AssertionError("'* Valid range is 1-65534' message not present.Traceback: %s " %traceback.format_exc())
		logger.debug("AccessPage : set 'PROTOCOL' drop-down to 'UDP'...")
		self.service_protocol.set(self.config.config_vars.service_protocol_udp)
		self.custom_tcp_port.set(self.config.config_vars.invalid_upstream)
		logger.debug("AccessPage : Click 'Save' button...")
		self.save1.click()
		if not self.invalid_port_error:
			raise AssertionError("'* Valid range is 1-65534' message not present.Traceback: %s " %traceback.format_exc())
		logger.debug("AccessPage : set 'PROTOCOL' drop-down to 'OTHER'...")
		self.service_protocol.set(self.config.config_vars.service_protocol)
		logger.debug("AccessPage : Writing protocol id' ")
		self.protocol_id.set(self.config.config_vars.invalid_protocol_id)
		logger.debug('AccessPage : Clicking on save button')
		self._save_rule()
		if not self.protocol_id_error_msg:
			raise AssertionError(" Protocol ID field accepting invalid values.Traceback: %s " %traceback.format_exc())
		
	def set_ip_mask_domain_checkbox_select_options(self,ip,mask,domain):
		if not ip == '':
			logger.debug('Setting Destination ip')
			self.destination_ip4.set(ip)
		if not mask == '':
			logger.debug('Setting Destination mask')
			self.destination_netmask.set(mask)				
		if not domain == '':
			logger.debug('Setting Destination domain')			
			self.domain_name.set(domain)
					
		logger.debug("AccessPage : Click 'Log' check box...")
		self.new_log_1.click()
		logger.debug("AccessPage : Click 'Classify media' check box...")
		self.new_classify_media_1.click()
		logger.debug("AccessPage : Click 'DSCP tag' check box...")
		self.new_dscp_tag_1.click()
		logger.debug("AccessPage : Click 'Blacklist' check box...")
		self.blacklist_3.click()
		logger.debug("AccessPage : Click 'Disable scanning' check box...")
		self.new_disable_scaning_1.click()
		logger.debug("AccessPage : Click '802.1 priority' check box...")
		self.new_dot1_priority_1.click()
	
	def select_dscp_priority_option(self,dscp,priority):
		'''
		Selecting DSCP TAG and Priority option from drop down list
		'''
		if not dscp == '':
			logger.debug('Selecting DSCP TAG')
			self.dscp_tag_values.set(dscp)
		if not priority == '':
			logger.debug('Selecting Priority')
			self.dot_1_priority_values.set(priority)				
		logger.debug("AccessPage : Clicking on save button")
		self._save_rule()
		
	def create_new_roles_with_different_rules(self):
		'''
		creates new roles with different rules
		
		'''
		logger.debug("AccessPage: Clicking on add button..")
		self.add_rule_plus_button.click()
		logger.debug('AccessPage : Selecting the value of Service Role')
		self.service_role2.set(self.config.config_vars.service_adp)
		logger.debug('AccessPage : Clicking on save setting button')
		self.save_settings.click()
		logger.debug("AccessPage: Clicking on add button..")
		self.add_rule_plus_button.click()
		logger.debug('AccessPage : Selecting the value of Service Role')
		self.service_role3.set(self.config.config_vars.service_bootp)
		logger.debug('AccessPage : Clicking on save button')
		self.save_settings.click()
		logger.debug("AccessPage : Clicking on New button..")
		self.create_new_role.click()
		logger.debug("AccessPage: Writing role name")
		self.role_input.set(self.config.config_vars.role_name_1)
		self.save_role.click()
		import time
		time.sleep(10)
		# import pdb
		# pdb.set_trace()
		logger.debug("AccessPage: Clicking on add button..")
		self.add_rule_plus_button.click()
		logger.debug('AccessPage : Selecting the value of Service Role')
		self.service_role2.set(self.config.config_vars.service_cfgm)
		logger.debug('AccessPage : Selecting the value of Action Role')
		self.action_role2.set(self.config.config_vars.action_deny)
		logger.debug('AccessPage : Clicking on save setting button')
		self.save_settings.click()
		logger.debug("AccessPage: Clicking on add button..")
		self.add_rule_plus_button.click()
		logger.debug('AccessPage : Selecting the value of Service Role')
		self.service_role3.set(self.config.config_vars.service_dhcp_value)
		logger.debug('AccessPage : Selecting the value of Action Role')
		self.action_role3.set(self.config.config_vars.service_action_value)
		logger.debug('AccessPage : Clicking on save setting button')
		self.save_settings.click()
		logger.debug("AccessPage : Clicking on New button..")
		self.create_new_role.click()
		logger.debug("AccessPage: Writing role name")
		self.role_input.set(self.config.config_vars.role_name_2)
		self.save_role.click()
		logger.debug("AccessPage: Clicking on add button..")
		self.add_rule_plus_button.click()
		logger.debug('AccessPage : Selecting the value of Service Role')
		self.service_role2.set(self.config.config_vars.service_cfgm)
		logger.debug('AccessPage : Selecting the value of Action Role')
		self.action_role2.set(self.config.config_vars.action_deny)
		logger.debug('AccessPage : Clicking on save setting button')
		self.save_settings.click()
		logger.debug("AccessPage: Clicking on add button..")
		self.add_rule_plus_button.click()
		logger.debug('AccessPage : Selecting the value of Service Role')
		self.service_role3.set(self.config.config_vars.Service_Role1_vocera)
		logger.debug('AccessPage : Selecting the value of Action Role')
		self.action_role3.set(self.config.config_vars.service_action_value)
		logger.debug('AccessPage : Clicking on save setting button')
		self.save_settings.click()
		# self.finish.click()
		
	def select_role(self,element):
		'''
		clicks on role
		'''
		logger.debug('Network: AccessPage: Clicking on role')
		element.click()

	def create_vlan_assignment_rule(self,vlanid):
		logger.debug('Access Page : Clicking on Add rule button')
		self.add_icon.click()
		logger.debug('Access Page : Choosing rule type VLAN Assignment')
		self.rule_type.set(self.config.config_vars.access_rule_type_vlan_assignment)
		logger.debug('Access Page : Entering invalid value in Vlan Id')
		self.vlan_id.set(vlanid)
		logger.debug('Access Page : Clicking on Save button')
		self.save_settings.click()

	def captive_portal_profile_create(self):
		logger.debug('Access Page : Clicking on Add rule button')
		self.add_icon.click()
		logger.debug('AccessPage: Setting the value to Rule type')
		self.rule_type.set(self.config.config_vars.Access_Rule_Captive_portal)
		logger.debug('AccessPage: Setting the Captive selection value')
		self.captive_selection.set(self.config.config_vars.Captive_selection_External)
		self.buy_time()
		logger.debug('AccessPage: Setting the Captive Profile value')
		self.captive_profile.set(self.config.config_vars.Captive_Profile_Default)
		logger.debug('AccessPage: Clicking on save setting button')
		self.save_settings.click()

	def set_role_assignment_rules_to_roles(self,role,str):
		logger.debug('AccessPage: Clicking on New button to create new Role Assignment Rules')
		self.new_role_assign.click()
		logger.debug("AccessPage :Set Role.")
		self.role_assign_name.set(role)
		logger.debug('AccessPage : writing string')
		self.string.set(str)
		logger.debug("AccessPage :Click save .")  
		self.ok1.click()
		
	def create_rule_one(self):
		'''
		Creates  rule
		'''
		logger.debug('AccessPage :Clicking on Add rule button')
		self.add_rule_plus_button.click()
		logger.debug('AccessPage : Choosing adp option from service dropdown')
		self.new_service_1.set(self.config.config_vars.service_adp_value)
		logger.debug("AccessPage : Click 'Log' check box...")
		self.new_log_1.click()
		logger.debug("AccessPage : Click 'Classify media' check box...")
		self.new_classify_media_1.click()
		logger.debug("AccessPage : Click 'DSCP tag' check box...")
		self.new_dscp_tag_1.click()
		logger.debug("AccessPage : Click 'Blacklist' check box...")
		self.blacklist_3.click()
		logger.debug("AccessPage : Click '802.1 priority' check box...")
		self.new_dot1_priority_1.click()
		logger.debug("AccessPage : checking 'DSCP tag' Dropdown...")
		self.browser.assert_element(self.dscp_tag_values, "DSCP Tag Value dropdown is not present")
		logger.debug("AccessPage : checking '802.1 priority' Dropdown...")
		self.browser.assert_element(self.dot_1_priority_values, "802.1 Priority Value dropdown is not present")
		logger.debug('AccessPage: Clicking on save setting button')
		self.save1.click()
		
	def create_rule_two(self):
		'''
		Creates  rule
		'''	
		logger.debug('AccessPage :Clicking on Add rule button')
		self.add_rule_plus_button.click()
		logger.debug('AccessPage : Choosing adp option from service dropdown')
		self.service_role2.set(self.config.config_vars.service_role_dhcp)
		logger.debug('AccessPage: Clicking on Log checkbox')
		self.log.click()
		logger.debug('AccessPage: Clicking oo Media checkbox')
		self.media.click()
		logger.debug('AccessPage: Clicking on Description tag checkbox')
		self.dscp.click()
		logger.debug('AccessPage: Clicking on BlackList checkbox')
		self.blacklist.click()
		logger.debug('AccessPage: Clicking on 802.1 Priority checkbox')
		self.p_802.click()
		logger.debug('AccessPage: Clicking on save setting button')
		self.save_settings.click()
		
	def create_rule_three(self):
		'''
		Creates  rule
		'''	
		logger.debug('AccessPage :Clicking on Add rule button')
		self.add_rule_plus_button.click()
		logger.debug('AccessPage : Choosing adp option from service dropdown')
		self.service_role3.set(self.config.config_vars.Service_Role1_dns)	
		logger.debug("AccessPage : Click on log check box")
		self.log_7.click()
		logger.debug("AccessPage : Click on media check box")
		self.media_7.click()
		logger.debug("AccessPage : Click dscp check box")
		self.dscp_7.click()
		logger.debug("AccessPage : Click blacklist check box")
		self.blacklist_7.click()
		logger.debug("AccessPage : Click on log check box")
		self.p_802_7.click()
		logger.debug("AccessPage : Click save")
		self.save_settings.click()
		
	def enable_pre_authentication_role1(self):
		'''
		Enables the pre-authentication role.
		'''
		if not self.ng_wired_pre_auth_role.is_selected():
			logger.debug("AccessPage : Click on Enable pre auth only.")
			self.ng_wired_pre_auth_role.click()		
			self.buy_time()		
			
	def click_add_rule_plus_button(self):	
		'''
		Clicks on AddRule button
		'''
		self.buy_time()
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		self.buy_time()
	
	def asserts_service_options(self):
		'''
		Asserts Options of service
		'''
		logger.debug("AccessPage : checking Log checkbox...")
		self.browser.assert_element(self.new_log_1, "Log checkbox is not present")
		logger.debug("AccessPage : checking DSCP tag checkbox...")
		self.browser.assert_element(self.new_dscp_tag_1, "DSCP tag checkbox is not present")
		logger.debug("AccessPage : checking Blacklist checkbox...")
		self.browser.assert_element(self.blacklist_3, "Blacklist checkbox is not present")
		logger.debug("AccessPage : checking 802.1 Priority checkbox...")
		self.browser.assert_element(self.new_dot1_priority_1, "802.1 Priority checkbox is not present")
	
	def create_rule_with_appcategory_antivirus_permit(self):
		'''
		Creates Access Rule with App Category Antivirus Permit 
		'''
		self.click_add_rule_plus_button()
		self.asserts_service_options()
		logger.debug('AccessPage : Choosing allow from action dropdown')
		self.new_action_1.set(self.config.config_vars.action_role_allow)
		logger.debug('AccessPage : Choosing Application Category radio button')
		self.ac_app_category1.click()
		logger.debug('AccessPage : Clicking on Antivirus button')
		self.antivirus1.click()
		logger.debug('AccessPage : Clicking on save button')			
		self.save1.click()
		
	def create_rule_with_appcategory_collaboration_deny(self):
		'''
		Creates Access Rule with App Category Collaboration Deny 
		'''
		self.click_add_rule_plus_button()
		logger.debug('AccessPage : Choosing Deny from action dropdown')
		self.action_role2.set(self.config.config_vars.action_role_deny)
		logger.debug('AccessPage : Choosing Application Category radio button')
		self.ac_app_category2.click()
		logger.debug('AccessPage : Clicking on Collaboration button')
		self.Collaboration1.click()
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
	
	def create_rule_with_appcategory_gaming_allow(self):
		'''
		Creates Access Rule with App Category Gaming Permit 
		'''
		self.click_add_rule_plus_button()
		logger.debug('AccessPage : Choosing Application Category radio button')
		self.ac_app_category3.click()
		logger.debug('AccessPage : Choosing allow from action dropdown')
		self.action_role3.set(self.config.config_vars.action_role_allow)
		logger.debug('AccessPage : Clicking on Gaming button')
		self.Gaming1.click()
		logger.debug("AccessPage : Click on log check box")
		self.log_7.click()
		logger.debug("AccessPage : Click dscp check box")
		self.dscp_7.click()
		logger.debug("AccessPage : Choose DS2 value")
		self.dscp_tag_value7.set(self.config.config_vars.dscp_tag_value_DS2)
		logger.debug("AccessPage : Click blacklist check box")
		self.blacklist_7.click()
		logger.debug("AccessPage : Click on log check box")
		self.p_802_7.click()
		self.dot_1_priority_value6.set(self.config.config_vars.custom_port_value)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
	
	def creating_different_application_access_rule(self):
		logger.debug('AccessPage :Clicking on Add rule button')
		self.add_rule_plus_button.click()
		logger.debug('AccessPage :Clicking on Application Service')
		self.service_application.click()
		logger.debug("AccessPAge: Asserts Options of service")
		self.asserts_service_options()
		logger.debug("AccessPAge: Asserts Destination field")
		self.assert_destination_dropdown()
		logger.debug("AccessPAge: Asserts Action Options")
		self.assert_action_dropdown_options()
		logger.debug('AccessPage :Clicking on "01 Net" checkbox')
		self.application_01_net.click()
		logger.debug('AccessPage: Clicking on save setting button')
		self.save1.click()
		
		logger.debug('AccessPage :Clicking on Add rule button')
		self.add_rule_plus_button.click()
		logger.debug('AccessPage :Clicking on Application Service')
		self.service_application_5.click()
		logger.debug('AccessPage :Clicking on "4399 Com " checkbox')
		self.application_4399_com.click()
		logger.debug('AccessPage : Choosing Deny from action dropdown')
		self.action_role2.set(self.config.config_vars.action_deny)
		logger.debug('AccessPage: Clicking on save setting button')
		self.save_settings.click()		
		
		logger.debug('AccessPage :Clicking on Add rule button')
		self.add_rule_plus_button.click()
		logger.debug('AccessPage :Clicking on Application Service')
		self.service_application_6.click()
		logger.debug('AccessPage :Clicking on "Adobe Update " checkbox')
		self.application_adobe_update.click()
		logger.debug('AccessPage : Choosing Deny from action dropdown')
		self.action_role3.set(self.config.config_vars.action_deny)
		logger.debug('AccessPage: Clicking on save setting button')
		self.save_settings.click()
		
		logger.debug('AccessPage :Clicking on Add rule button')
		self.add_rule_plus_button.click()
		logger.debug('AccessPage :Clicking on Application Service')
		self.service_application_7.click()
		logger.debug('AccessPage :Clicking on "Yahoo" checkbox')
		self.application_yahoo.click()
		logger.debug('AccessPage: Clicking on Log checkbox')
		self.log_3.click()
		logger.debug('AccessPage: Clicking on Description tag checkbox')
		self.dscp_3.click()
		self.dscp_tag.set(self.config.config_vars.dscp_tag_value_59)
		logger.debug('AccessPage: Clicking on BlackList checkbox')
		self.blacklist_3.click()
		logger.debug('AccessPage: Clicking on 802.1 Priority checkbox')
		self.new_dot1_priority_1.click()
		self.dot_1_priority.set(self.config.config_vars.priority_value_4)
		logger.debug('AccessPage: Clicking Application Throttling checkbox')
		self.application_throttling.click()
		logger.debug('AccessPage: Setting Throttling Downstream value')
		self.throttle_downstream.set(self.config.config_vars.downstream)
		logger.debug('AccessPage: Setting Throttling Upstream value')
		self.throttle_upstream.set(self.config.config_vars.upstream)
		logger.debug('AccessPage: Clicking on save setting button')
		self.save_button_2.click()
	
	def create_rule_with_webtegory_shopping_permit(self):
		'''
		Creates Access Rule with Web Category Shopping Permit 
		'''
		self.click_add_rule_plus_button()
		logger.debug('AccessPage : Choosing allow from action dropdown')
		self.new_action_1.set(self.config.config_vars.action_role_allow)
		logger.debug('AccessPage : Choosing Web Category radio button')
		self.ac_web_category.click()
		logger.debug('AccessPage : Clicking on shopping button')
		self.shopping.click()
		logger.debug('AccessPage : Clicking on save button')			
		self.save1.click()
	
	def create_rule_with_webtegory_travel_deny(self):
		'''
		Creates Access Rule with Web Category Shopping Permit 
		'''
		self.click_add_rule_plus_button()
		logger.debug('AccessPage : Choosing Deny from action dropdown')
		self.action_role2.set(self.config.config_vars.action_role_deny)
		logger.debug('AccessPage : Choosing Web Category radio button')
		self.ac_web_category1.click()
		logger.debug('AccessPage : Clicking on shopping button')
		self.travel.click()
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
	
	def asserts_sevices_options(self):
		'''
		Asserts Services Options
		'''
		logger.debug('AccessPage : Clicking on Application Category button')
		self.ac_app_category1.click()
		self.asserts_service_options()
		logger.debug('AccessPage : Clicking on Application button')
		self.service_application.click()
		self.asserts_service_options()
		logger.debug('AccessPage : Clicking on Web Category button')
		self.ac_web_category.click()
		logger.debug("AccessPage : checking Log checkbox...")
		self.browser.assert_element(self.new_log_1, "Log checkbox is not present")
		logger.debug("AccessPage : checking Blacklist checkbox...")
		self.browser.assert_element(self.blacklist_3, "Blacklist checkbox is not present")
		logger.debug('AccessPage : Clicking on Web Reputation button')
		self.webreputation1.click()
		logger.debug("AccessPage : checking Log checkbox...")
		self.browser.assert_element(self.new_log_1, "Log checkbox is not present")
		logger.debug("AccessPage : checking Blacklist checkbox...")
		self.browser.assert_element(self.blacklist_3, "Blacklist checkbox is not present")
		
	def validate_application_throttening_option(self):
		'''
		Asserts and validate Application Throttening options
		'''
		logger.debug('AccessPage : Clicking on Application button')
		self.service_application.click()
		self.asserts_service_options()
		logger.debug('AccessPage : Clicking on Application Throttening Ckeckbox')
		self.application_throttling1.click()
		logger.debug("AccessPage : checking Downstream Textbox...")
		self.browser.assert_element(self.throttle_downstream1, "Downstream Textbox is not present")
		logger.debug("AccessPage : checking UPtream Textbox...")
		self.browser.assert_element(self.throttle_upstream1, "UPtream Textbox is not present")
		logger.debug("AccessPage : Write value in 'Downstream' textbox...")
		self.throttle_downstream1.set(self.config.config_vars.invalid_upstream)
		logger.debug("AccessPage : Write value in 'Upstream' textbox...")
		self.throttle_upstream1.set(self.config.config_vars.invalid_downstream)
		logger.debug('AccessPage : Clicking on Antivirus button')
		self.antivirus1.click()
		logger.debug('AccessPage : Clicking on save button')			
		self.save1.click()
		logger.debug("AccessPage : checking Downstream Textbox Error message...")
		self.browser.assert_element(self.throttle_downstream_error1, "Downstream Textbox Error message is not present")
		logger.debug("AccessPage : checking Upstream Textbox Error message...")
		self.browser.assert_element(self.throttle_upstream_error1, "Upstream Textbox Error message is not present")
		
	def assert_dscp_tag_options(self):
		'''
		'''
		logger.debug('AccessPage: Clicking on Description tag checkbox')
		self.new_dscp_tag_1.click()
		options = self.dscp_tag_values.get_options()
		for x in range(0,64):
			if not options[x] == 'DS'+str(x):
				raise AssertionError("DSCP TAG option DS%x is not present.Traceback: %s")
		
	def assert_destination_dropdown(self):
		'''
		Asserts Destination Dropdown
		'''
		self.browser.assert_element(self.new_destination_1,'Destination Dropdown is present',False)
		
	def assert_action_dropdown_options(self):
		'''
		Asserts Actions dropDown options
		'''
		conf = self.config.config_vars
		logger.debug('AccessPage :  Getting  option from Actions DropDown')
		options = self.new_action_1.get_options()
		if not options[0] == self.config.config_vars.action_role_allow:
			raise AssertionError("Option Allow element not matched i.e. Traceback: %s" %traceback.format_exc())
		if not options[1] == conf.action_role_deny:
			raise AssertionError("Option Deny element not found i.e. Traceback: %s" %traceback.format_exc())
			
	def assert_rules_before_moving(self):
		time.sleep(5)
		if self.allow_rule_before_moving and self.deny_rule_before_moving :
			logger.debug('AccessPage : Allow any to all destinations Rule is Above Deny any to all destinations Rules ')
			
	def assert_rules_after_moving(self):
		time.sleep(8)
		if self.allow_rule_after_moving and self.deny_rule_after_moving :
			logger.debug('AccessPage : Rules arre moved... Deny any to all destinations Rules is now Above Allow any to all destinations Rule ')
		else :
			raise AssertionError("Allow any to all destinations Rule and Deny any to all destinations Rules are not moved i.e . Traceback: %s" % traceback.format_exc())
			
	def assert_network_based_rule_type_options(self):
		'''
		Asserts the options of network based rule type dropdown.
		'''
		conf = self.config.config_vars
		options = self.rule_type.get_options()
		if not options[0] == conf.Access_Control:
			raise AssertionError("'Access Control' Option not found in Rule Type dropdown.Traceback: %s " %traceback.format_exc())
		if not options[1] == conf.access_rule_type_vlan_assignment:
			raise AssertionError("'VLAN Assignment' Option not found in Rule Type dropdown.Traceback: %s " %traceback.format_exc())
		if not options[2] == conf.Access_Rule_Captive_portal:
			raise AssertionError("'Captive portal' Option not found in Rule Type dropdown.Traceback: %s " %traceback.format_exc())
		if not options[3] == conf.rule_calea_type:
			raise AssertionError("'CALEA' Option not found in Rule Type dropdown.Traceback: %s " %traceback.format_exc())
			
	def assert_role_based_rule_type_options(self):
		'''
		Asserts the options of role based rule type dropdown.
		'''
		conf = self.config.config_vars
		logger.debug("AccessPage : Asserting all options of role based rule type dropdown...")
		options = self.rule_type_dropdown.get_options()
		if not options[0] == conf.Access_Control:
			raise AssertionError("'Access Control' Option not found in Rule Type dropdown.Traceback: %s " %traceback.format_exc())
		if not options[1] == conf.access_rule_type_vlan_assignment:
			raise AssertionError("'VLAN Assignment' Option not found in Rule Type dropdown.Traceback: %s " %traceback.format_exc())
		if not options[2] == conf.Access_Rule_Captive_portal:
			raise AssertionError("'Captive portal' Option not found in Rule Type dropdown.Traceback: %s " %traceback.format_exc())
		if not options[3] == conf.rule_calea_type:
			raise AssertionError("'CALEA' Option not found in Rule Type dropdown.Traceback: %s " %traceback.format_exc())	
		if not options[4] == conf.Access_Rule_Bandwidth_Contract:
			raise AssertionError("'Bandwidth Contract' Option not found in Rule Type dropdown.Traceback: %s " %traceback.format_exc())
			
	def click_on_role_based_add_rule(self):
		'''
		Clicks on 'ADD RULE' button in role based network.
		'''
		logger.debug("AccessPage : Clicking on 'ADD RULE' button...")
		self.add_rule_plus_button.click()
		self.buy_time()
		
	def create_h323_to_all_destinations(self):
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		time.sleep(2)
		logger.debug('AccessPage : Choosing bootp option from service dropdown')
		self.service_role2.set(self.config.config_vars.service_h323_udp)
		logger.debug('AccessPage : Choosing Source-NAT from action dropdown')
		self.action_role2.set(self.config.config_vars.service_action_value)
		logger.debug('AccessPage : Clicking on save button')   
		self.save_settings.click()
		
	def assert_options(self,logoption = False, dscptag = False, blacklist = False, priority_802 = False,media = False,scanning = False):
		'''
		asserts visibility of options
		'''
		if logoption:
			logger.debug('AccessPage : Checking log checkbox')
			self.browser.assert_element(self.log,'Log checkbox is not present')
		if dscptag:
			logger.debug('AccessPage : Checking dscp checkbox')
			self.browser.assert_element(self.dscp,'dscp checkbox is not present')
		if blacklist:
			logger.debug('AccessPage : Checking blacklist checkbox')
			self.browser.assert_element(self.blacklist,'blacklist checkbox is not present')
		if priority_802:
			logger.debug('AccessPage : Checking priority_802 checkbox')
			self.browser.assert_element(self.p_802,'priority_802 checkbox is not present')
		if media:
			logger.debug('AccessPage : Checking log checkbox')
			self.browser.assert_element(self.media,'media checkbox is not present')
		if scanning:
			logger.debug('AccessPage : Checking scanning checkbox')
			self.browser.assert_element(self.scanning,'scanning checkbox is not present')
			
	def select_slider(self):
		'''
		selects slider
		'''
		logger.debug('AccessPage: clicking on slider')
		self.selector_reputation.click()
		
	def select_sites(self,site):
		'''
		select sites
		'''
		if site == 'Trustworthy WRI > 81':
			logger.debug('AccessPage : Selecting Trust worthy sites')
			self.browser.key_press(u'\ue013')
			self.browser.key_press(u'\ue013')
		if site == 'Low Risk WRI 61-80':
			logger.debug('AccessPage : Selecting Trust worthy sites')
			self.browser.key_press(u'\ue013')
		if site == 'Suspicious WRI 21-40':
			logger.debug('AccessPage : Selecting Trust worthy sites')
			self.browser.key_press(u'\ue015')
		if site == 'High Risk WRI < 20':
			logger.debug('AccessPage : Selecting Trust worthy sites')
			self.browser.key_press(u'\ue015')
			self.browser.key_press(u'\ue015')
			
			
			
	def tcp_port_range_validation(self):
		'''
		validates tcp port range
		'''
		logger.debug('AccessPage: Clicking on Network based button')
		self.network_based.click()
		time.sleep(2)
		logger.debug('AccessPage : Clicking on + button')
		self.add_rule_plus_button.click()
		time.sleep(2)
		logger.debug('AccessPage : Choosing Custom option from service dropdown')
		self.service_role2.set(self.config.config_vars.service_custom)
		logger.debug("AccessPage : write 'Port' number...")
		self.custom_tcp_port.set(self.config.config_vars.invalid_port_range)
		logger.debug("AccessPage : Click 'Save' button...")
		self.save_settings.click()
		if not self.port_range_error:
			raise AssertionError("'* End must be > start' message not present.Traceback: %s " %traceback.format_exc())
			
	def check_mac_address_and_dhcp_option_in_wired_network(self):
		'''
		checks mac_address_and_dhcp_option in wired_network (#Bug: Option must not be present)
		'''
		logger.debug("AccessPage : Click on new. button")
		self.new_role_assign.click()
		logger.debug("AccessPage :  check mac_address_and_dhcp_option.")
		self.role_assign_attribute.set(self.config.config_vars.dropdown_mac_address_and_dhcp_options)
		options = self.role_assign_attribute.get_options()
		for x in range(0,160):
			if options[x] == self.config.config_vars.dropdown_mac_address_and_dhcp_options:
				raise AssertionError("mac_address_and_dhcp_option is present.Traceback: %s " %traceback.format_exc())
	
	def create_access_rule_for_role_based_1(self,service = None,action=None,destination=None,ip=None):
		logger.debug("AccessPage : Click on radio based.")
		self.role_radio.click()
		logger.debug("AccessPage : Click on add icon.")
		self.add_icon.click()
		logger.debug("AccessPage : Select Service Role")
		self.service_role2.set(service)
		logger.debug("AccessPage : Select Action Role")
		self.action_role2.set(action)
		logger.debug('AccessPage : Select destination Role')
		self.destination_role_2.set(destination)
		if ip:
			logger.debug("AccessPage : Set Ip Address.")
			self.destination_ip3.set(ip)
		logger.debug("AccessPage : Click save")
		self.save_settings.click()
		
	def create_access_rule_for_role_based_2(self,service = None,action=None,destination=None,ip=None):
		logger.debug("AccessPage : Click on add icon.")
		self.add_icon.click()
		logger.debug("AccessPage : Select Service Role")
		self.service_role3.set(service)
		logger.debug("AccessPage : Select Action Role")
		self.action_role3.set(action)
		logger.debug('AccessPage : Select destination Role')
		self.destination_role_3.set(destination)
		if ip:
			logger.debug("AccessPage : Set Ip Address.")
			self.destination_ip6.set(ip)
		logger.debug("AccessPage : Click save")
		self.save_settings.click()
		
	def create_access_rule_for_role_based_3(self,service = None,action=None,destination=None,ip=None):
		logger.debug("AccessPage : Click on add icon.")
		self.add_icon.click()
		logger.debug("AccessPage : Select Service Role")
		self.service_role4.set(service)
		logger.debug("AccessPage : Select Action Role")
		self.action_role4.set(action)
		logger.debug('AccessPage : Select destination Role')
		self.destination_role_4.set(destination)
		if ip:
			logger.debug("AccessPage : Set Ip Address.")
			self.destination_ip1.set(ip)
		logger.debug("AccessPage : Click save")
		self.save_button_2.click()
		
	def create_access_rule_for_role_based_4(self,service = None,action=None,destination=None,ip=None):
		logger.debug("AccessPage : Click on add icon.")
		self.add_icon.click()
		logger.debug("AccessPage : Select Service Role")
		self.service_role5.set(service)
		logger.debug("AccessPage : Select Action Role")
		self.action_role5.set(action)
		logger.debug('AccessPage : Select destination Role')
		self.destination_role_5.set(destination)
		if ip:
			logger.debug("AccessPage : Set Ip Address.")
			self.destination_ip2.set(ip)
		logger.debug("AccessPage : Click save")
		self.save_button_3.click()		
	def create_access_role_assignment_rule(self, str, operator=False, attribute=False, role=False):
		logger.debug("AccessPage : Click on new.")
		self.new_role_assign.click()
		if operator:
			logger.debug('Access Page : Selecting operator')
			self.role_operator.set(operator)
		if attribute:
			logger.debug("AccessPage : select Attribute value.")
			self.role_assign_attribute.set(attribute)
		if role:
			logger.debug("AccessPage :Set role .")
			self.role_assign_name.set(role)
		logger.debug("AccessPage :Set String .")
		self.string.set(str)
		logger.debug("AccessPage : click ok.")
		self.ok1.click()
		
	def assert_disabled_app_rf_rule(self):
		'''
		Asserts Disabled App RF Rules 
		'''
		logger.debug("AccessPage : checking Disabed App Category Radio button ...")
		self.browser.assert_element(self.ac_app_category_disabled, "App Category Radio button is not disabled")
		logger.debug("AccessPage : checking Disabed App  Radio button...")
		self.browser.assert_element(self.ac_app_disabled, "App  Radio button is not disabled")
		logger.debug("AccessPage : checking Disabed Web Category Radio button...")
		self.browser.assert_element(self.ac_web_category_disabled, "Web Category  Radio button is not disabled")
		logger.debug("AccessPage : checking Disabed App Web Reputation Radio button...")
		self.browser.assert_element(self.ac_web_reputation_disabled, "Web Reputation Radio button is not disabled")
		
	def assert_access_disabled_app_rf_rule(self,rule_type):
		if rule_type == 'network_based':
			self.click_network_access()
		if rule_type == 'role_based':
			self.click_role_access()
		self.click_on_role_based_add_rule()
		self.assert_disabled_app_rf_rule()
		self.click_on_cancel_button()
		
	def assert_service(self):
		logger.debug('AccessPage : Asserting Network option')
		self.browser.assert_element(self.network_service,'Network option is not present')
		logger.debug('AccessPage : Asserting Application Category option')
		self.browser.assert_element(self.ac_app_category1,'Application Category option is not present')
		logger.debug('AccessPage : Asserting Application option')
		self.browser.assert_element(self.service_application,'Application option is not present')
		logger.debug('AccessPage : Asserting Web Category option')
		self.browser.assert_element(self.ac_web_category,'Web Category option is not present')
		logger.debug('AccessPage : Asserting Web Reputation option')
		self.browser.assert_element(self.webreputation1,'Web Reputation option is not present')
		
	def asserting_rule_type_options(self, bandwidth = True):
		logger.debug('AccessPage : Asserting Captive Portal option')
		self.browser.assert_element(self.rule_captive_portal,'Captive Portal option is not present')
		logger.debug('AccessPage : Asserting CALEA option')
		self.browser.assert_element(self.rule_calea,'CALEA option is not present')
		if bandwidth:
			logger.debug('AccessPage : Asserting Bandwidth Contract option')
			self.browser.assert_element(self.rule_bandwidth,'Bandwidth Contract option is not present')
		
	def enable_mac_authentication_role1(self,value):
		'''
		Enables the mac-authentication role.
		'''
		if not self.ng_Wired_Role_Mac_Auth.is_selected():
			logger.debug("AccessPage : Click on Enable mac auth only.")
			self.ng_Wired_Role_Mac_Auth.click()		
			self.buy_time()
		logger.debug("AccessPage : Select pre auth role.")
		self.ng_wired_enforce_mac_auth_access.set(value)
			
	def create_rule_with_application_adobe_update_deny(self):
		'''
		Creates Access Rule with Application Adobe Update 
		'''
		logger.debug('AccessPage :Clicking on Add rule button')
		self.add_rule_plus_button.click()
		logger.debug('AccessPage :Clicking on Application Service')
		self.service_application_6.click()
		logger.debug('AccessPage :Clicking on "Adobe Update " checkbox')
		self.application_adobe_update.click()
		logger.debug('AccessPage : Choosing Deny from action dropdown')
		self.action_role3.set(self.config.config_vars.action_deny)
		logger.debug('AccessPage: Clicking on save setting button')
		self.save_settings.click()
	
	def create_rule_with_web_reputation_Selecting_Deny(self):
		'''
		Creates Access Rule with WebReputation Selecting Deny 
		'''	
		access.click_add_rule_plus_button()
		logger.debug('AccessPage : Clicking on Web reputation radio')
		access.webreputation2.click()
		logger.debug('AccessPage : Clicking on slider')
		access.selectorreputation1.click()
		logger.debug('AccessPage : Selecting Deny')
		access.action_role3.set(conf.action_deny)
		access.select_sites('Suspicious WRI 21-40')
		logger.debug('AccessPage : Clicking on save settings')
		access.save_settings.click()
		
	def creating_captive_portal_rule(self):
		logger.debug("AccessPage: Setting Rule Type")
		self.set_rule_type('Captive portal')
		logger.debug("AccessPage: Clicking on save button")
		self.save_settings.click()
		
	def creating_calea_rule(self):
		logger.debug("AccessPage: Setting Rule Type")
		self.set_rule_type('CALEA')
		logger.debug("AccessPage: Clicking on save button")
		self.save_settings.click()
		
	def creating_bandwidth_contract_rule(self):
		logger.debug("AccessPage: Setting Rule Type")
		self.rule_type_dropdown.set(self.config.config_vars.Access_Rule_Bandwidth_Contract)
		logger.debug('Access Page : Entering valid value in Downstream and Upstream')
		self.downstream_textbox.set(self.config.config_vars.downstream_value)
		self.upstream_textbox.set(self.config.config_vars.upstream_value)
		logger.debug("AccessPage: Clicking on save button")
		self.save_settings.click()
	
	def creating_service_application_rule(self):
		logger.debug('AccessPage :Clicking on Add rule button')
		self.add_rule_plus_button.click()
		logger.debug('AccessPage :Clicking on Application Service')
		self.service_application_5.click()
		logger.debug('AccessPage :Clicking on "4399 Com " checkbox')
		self.application_4399_com.click()
		logger.debug('AccessPage : Choosing Deny from action dropdown')
		self.action_role2.set(self.config.config_vars.action_deny)
		logger.debug('AccessPage: Clicking on save setting button')
		self.save_settings.click()
	
	def create_rule_with_webtegory_travel_deny(self):
		'''
		Creates Access Rule with Web Category Shopping Permit 
		'''
		logger.debug('AccessPage :Clicking on Add rule button')
		self.click_add_rule_plus_button()
		logger.debug('AccessPage : Choosing Web Category radio button')
		self.ac_web_category_2.click()
		logger.debug('AccessPage : Clicking on shopping button')
		self.travel.click()
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		
	def create_multiple_app_category_rules(self):
		'''
		Creates Access Rule with App Category Collaboration Deny 
		'''
		self.click_add_rule_plus_button()
		logger.debug('AccessPage : Choosing "Deny" from action dropdown')
		self.new_action_1.set(self.config.config_vars.action_deny)
		logger.debug('AccessPage : Choosing Application Category radio button')
		self.ac_app_category1.click()
		logger.debug('AccessPage : Clicking on Antivirus button')
		self.antivirus1.click()
		logger.debug('AccessPage : Clicking on Application Throttening Ckeckbox')
		self.application_throttling1.click()
		logger.debug("AccessPage : Write value in 'Downstream' textbox...")
		self.throttle_downstream1.set(self.config.config_vars.stream)
		logger.debug("AccessPage : Write value in 'Upstream' textbox...")
		self.throttle_upstream1.set(self.config.config_vars.stream)
		logger.debug("AccessPage : Click 'Log' check box...")
		self.new_log_1.click()
		logger.debug("AccessPage : Click 'DSCP tag' check box...")
		self.new_dscp_tag_1.click()
		logger.debug("AccessPage : Click 'Blacklist' check box...")
		self.blacklist_3.click()
		logger.debug("AccessPage : Click '802.1 priority' check box...")
		self.new_dot1_priority_1.click()
		logger.debug('AccessPage : Clicking on save button')			
		self.save1.click()
		
		
		self.click_add_rule_plus_button()
		logger.debug('AccessPage : Choosing Deny from action dropdown')
		self.action_role2.set(self.config.config_vars.action_role_deny)
		logger.debug('AccessPage : Choosing Application Category radio button')
		self.ac_app_category2.click()
		logger.debug('AccessPage : Clicking on Collaboration button')
		self.Collaboration1.click()
		logger.debug('AccessPage : Clicking on Application Throttening Ckeckbox')
		self.application_throttling_2.click()
		logger.debug("AccessPage : Write value in 'Downstream' textbox...")
		self.throttle_downstream_2.set(self.config.config_vars.stream)
		logger.debug("AccessPage : Write value in 'Upstream' textbox...")
		self.throttle_upstream_2.set(self.config.config_vars.stream)
		logger.debug('AccessPage: Clicking on Log checkbox')
		self.log.click()
		logger.debug('AccessPage: Clicking on Description tag checkbox')
		self.dscp.click()
		logger.debug('AccessPage: Clicking on BlackList checkbox')
		self.blacklist.click()
		logger.debug('AccessPage: Clicking on 802.1 Priority checkbox')
		self.p_802.click()
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
		
		self.click_add_rule_plus_button()
		logger.debug('AccessPage : Choosing Application Category radio button')
		self.ac_app_category3.click()
		logger.debug('AccessPage : Choosing allow from action dropdown')
		self.action_role3.set(self.config.config_vars.action_role_deny)
		logger.debug('AccessPage : Clicking on Gaming button')
		self.Gaming1.click()
		logger.debug('AccessPage : Clicking on Application Throttening Ckeckbox')
		self.application_throttling_3.click()
		logger.debug("AccessPage : Write value in 'Downstream' textbox...")
		self.throttle_downstream_3.set(self.config.config_vars.stream)
		logger.debug("AccessPage : Write value in 'Upstream' textbox...")
		self.throttle_upstream_3.set(self.config.config_vars.stream)
		logger.debug("AccessPage : Click on log check box")
		self.log_7.click()
		logger.debug("AccessPage : Click dscp check box")
		self.dscp_7.click()
		logger.debug("AccessPage : Choose DS2 value")
		self.dscp_tag_value7.set(self.config.config_vars.dscp_tag_value_DS2)
		logger.debug("AccessPage : Click blacklist check box")
		self.blacklist_7.click()
		logger.debug("AccessPage : Click on log check box")
		self.p_802_7.click()
		self.dot_1_priority_value6.set(self.config.config_vars.custom_port_value)
		logger.debug('AccessPage : Clicking on save button')			
		self.save_settings.click()
