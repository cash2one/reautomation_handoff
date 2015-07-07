# Developed by :
# On date : 
# Last edited by : Ishan Anand
# On date : 07th Aug 2014

import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.util.WebPage import WebPage
from athenataf.lib.test.TestCase import TestCase
from athenataf.lib.functionality.page.configuration.network.SecurityPage import SecurityPage
import traceback
import time


class VirtualLanPage(WebPage):
	def __init__(self, test, browser, config):
		time.sleep(6)	
		WebPage.__init__(self, "VirtualLan", test, browser, config)
		self.test.assertPageLoaded(self)
		
		
	def isPageLoaded(self):
		logger.debug('VlanPage : Checking whether is loaded..')
		if self.back:
			return True	
		else:
			return False
			
	def use_vlan_defaults(self):
		logger.debug('VlanPage : use_vlan_defaults : Selecting network_assigned option')
		self.network_assigned.click()
		logger.debug("VlanPage : use_vlan_defaults : Selecting client vlan assignment as 'Default'")
		self.default.click()
		logger.debug("VlanPage : use_vlan_defaults : Clicking 'Next' button")
		self.next.click()
		return SecurityPage(self.test, self.browser, self.config)
	
	def wired_network_vlan_defaults(self):
		logger.debug("VlanPage : wired_network_vlan_defaults : Selecting wired network default vlan_mode")
		self.mode.set(self.config.config_vars.Vlan_Mode)
		logger.debug("VlanPage : wired_network_vlan_defaults : Clicking 'Next' button")
		self.next.click()
		return SecurityPage(self.test, self.browser, self.config)
		
	def set_static_vlan(self):
		logger.debug("VlanPage : set_static_vlan : Selecting network_assigned option")
		self.network_assigned.click()
		logger.debug("VlanPage : set_static_vlan : Selecting static option")
		self.static.click()
		logger.debug("VlanPage : set_static_vlan : Setting vlanid")
		self.vlanid.set(self.config.config_vars.Vlan_Id)
		logger.debug("VlanPage : set_static_vlan : Clicking 'Next' button")
		self.next.click()
		return SecurityPage(self.test, self.browser, self.config)
		
	def select_virtual_controller(self):
		logger.debug("VlanPage : select_virtual_controller : Clicking 'virtual_controller'")
		self.virtual_controller.click()
		logger.debug("VlanPage : select_virtual_controller : Clicking 'Next' button")
		self.next.click()
		return SecurityPage(self.test, self.browser, self.config)
		
	def check_dynamic_vlan_attribute_list(self):
		logger.debug("VlanPage : check_dynamic_vlan_attribute_list : Clicking network_assigned option")
		self.network_assigned.click()
		logger.debug("VlanPage : check_dynamic_vlan_attribute_list : Clicking dynamic_vlan option")
		self.dynamic_vlan.click()
		logger.debug("VlanPage : check_dynamic_vlan_attribute_list : Checking vlan attribute list")
		if self.default_vlan_attribute_list:
			return True
		else:
			raise AssertionError("Default attributes missing for this IAP .Traceback: %s " %traceback.format_exc())
					
	def create_vlan_assignment_rules(self):
		logger.debug("VlanPage : create_vlan_assignment_rules : Clicking network_assigned option")
		self.network_assigned.click()
		logger.debug("VlanPage : create_vlan_assignment_rules : Clicking dynamic_vlan option")
		self.dynamic_vlan.click()
		vlan_number = int(self.config.config_vars.Vlan_Number)
		i=1
		logger.debug("VlanPage : create_vlan_assignment_rules : Clicking new button")
		self.new.click()
		for option in self.rule_operator.options:
			if not option.find('matches-') == -1:
				continue
			logger.debug("VlanPage : create_vlan_assignment_rules : Clicking new button")
			self.new.click()
			logger.debug("VlanPage : create_vlan_assignment_rules : Setting rule_attribute")
			self.rule_attribute.set(self.config.config_vars.Vlan_Rule_Attribute)
			logger.debug("VlanPage : create_vlan_assignment_rules : Setting rule_operator")
			self.rule_operator.set(option)
			element = "Vlan_Rule_String%s"%i
			string = '' 
			print string
			exec("string = self.config.config_vars.%s"%element)
			logger.debug("VlanPage : create_vlan_assignment_rules : Setting rule_string value")
			self.rule_string.set(string)
			logger.debug("VlanPage : create_vlan_assignment_rules : Setting rule_vlan value")
			self.rule_vlan_textbox.set(vlan_number)
			logger.debug("VlanPage : create_vlan_assignment_rules : Clicking 'OK' button")
			self.ok.click()
			i+=1
			vlan_number+=1
		logger.debug("VlanPage : create_vlan_assignment_rules : Clicking 'NEXT' button")
		self.next.click()
		return SecurityPage(self.test, self.browser, self.config)
	
	def wired_vlan_defaults(self):
		import traceback
		logger.debug("VlanPage : wired_vlan_defaults : Checking for wired vlan default settings")
		if not self.mode.selected=='Trunk':
			raise AssertionError("Mode not trunk by default .Traceback: %s " %traceback.format_exc())
		if not self.virtual_controller.is_selected():
			raise AssertionError("'CLIENT IP ASSIGNMENT' radio not set to 'Virtual Controller Assigned' .Traceback: %s " %traceback.format_exc())
		if not self.wired_vlan_id_textbox.get() == 'all':
			raise AssertionError("'Allowed Vlan' not set to 'all'")
		self.next.click()
		return SecurityPage(self.test, self.browser, self.config)		
		
	def create_dynamic_vlan_assignment_rule(self):
		logger.debug("VlanPage : create_dynamic_vlan_assignment_rule : Clicking network_assigned option")
		self.network_assigned.click()
		logger.debug("VlanPage : create_dynamic_vlan_assignment_rule : Clicking dynamic_vlan option")
		self.dynamic_vlan.click()
		logger.debug("VlanPage : create_dynamic_vlan_assignment_rule : Clicking 'NEW' button")
		self.new.click()
		logger.debug("VlanPage : create_dynamic_vlan_assignment_rule : Setting rule_attribute")
		self.rule_attribute.set(self.config.config_vars.Vlan_Rule_Attribute1)
		test_case = TestCase(self.config)
		path = self.config.config_vars
		test_case.assertEquals(self.rule_operator.get_selected() ,  path.rule_operator_value , "value of 'VLAN ASSIGNMENT RULE OPERATOR' was not changed to matches-regular-expression")
		logger.debug("VlanPage : create_dynamic_vlan_assignment_rule : Setting rule_string value")
		self.rule_string.set(self.config.config_vars.string_value)
		logger.debug("VlanPage : create_dynamic_vlan_assignment_rule : Setting rule_vlan value")
		self.rule_vlan_textbox.set(self.config.config_vars.invalid_vlan_number_value)
		logger.debug("VlanPage : create_dynamic_vlan_assignment_rule : Clicking 'OK' button")
		self.ok.click()
		logger.debug("VlanPage : create_dynamic_vlan_assignment_rule : Asserting invalid vlan values")
		self.assert_invalid_vlan_values()
		import time
		time.sleep(8)
		if self.rule_vlan_textbox:
			logger.debug("VlanPage : create_dynamic_vlan_assignment_rule : Setting rule_vlan value")
			self.rule_vlan_textbox.set(self.config.config_vars.vlan_number_value)
			logger.debug("VlanPage : create_dynamic_vlan_assignment_rule : Clicking 'OK' button")
			self.ok.click()
		
	def assert_invalid_vlan_values(self):
		if self.vlan_number_value_error: 
			logger.debug("Invalid Vlan value")
			return True
		else:
			import traceback
			raise AssertionError("Vlan  accepting invalid values i.e . Traceback: %s" % traceback.format_exc())
		
	def assert_default_value_vlan(self):
		logger.debug("VlanPage :Check Client IP assignment should be Network Assigned")
		import traceback
		if not self.network_assigned.is_selected():
			raise AssertionError("VlanPage :Client IP assignment should be Network Assigned.Traceback: %s " %traceback.format_exc())
		logger.debug("VlanPage :Check CLIENT VLAN ASSIGNMENT should be set to DEFAULT.")
		if not self.default.is_selected():
			raise AssertionError("VlanPage :CLIENT VLAN ASSIGNMENT' radio not set to DEFAULT.Traceback: %s " %traceback.format_exc())		
			
	def assert_default_value_vlan_static(self):
		logger.debug("VlanPage :Enable to static.")
		self.static.click()		
		logger.debug("VlanPage :Check default values of static vlan.")
		vlan_field = self.vlanid.get()
		import traceback
		if not vlan_field == self.config.config_vars.vlan_default_value :
			raise AssertionError("VlanPage : The VLAN field value is not 1.Traceback: %s " %traceback.format_exc())
		
	def assert_vlan_page(self):
		if not self.client_ip_assignment:
			import traceback
			raise AssertionError("Vlan page not appeared. i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("VirtualLanPage : Clicking 'Back' button...")
		self.back.click()
		
	def _select_client_vlan_assignment(self, mode):
		logger.debug("VirtualLanPage : Clicking '%s' radio-button..." %mode)
		if mode == 'default':
			self.default.click()
		elif mode == 'static':
			self.static.click()
		elif mode == 'dynamic':
			self.dynamic_vlan.click()
			
	def validate_vlan_field(self):
		import traceback
		import time
		self._select_client_vlan_assignment('static')
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlanid.set(self.config.config_vars.vlan_id_alpha)
		time.sleep(3)
		logger.debug("VirtualLanPage : Clicking next button...")
		self.next.click()
		if not self.vlan_id_range_error:
			raise AssertionError("Vlan ID range error not found. i.e . Traceback: %s" % traceback.format_exc())
		
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlanid.set(self.config.config_vars.Vlan_Id)
		time.sleep(3)
		logger.debug("VirtualLanPage : Clicking next button...")
		self.next.click()
		if self.client_ip_assignment:
			raise AssertionError("Vlan ID as number was not accepted. i.e . Traceback: %s" % traceback.format_exc())
		self.back.click()
		
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlanid.set(self.config.config_vars.vlan_id_num_invalid)
		time.sleep(3)
		logger.debug("VirtualLanPage : Clicking next button...")
		self.next.click()
		if not self.vlan_id_range_error:
			raise AssertionError("Vlan ID range error not found. i.e . Traceback: %s" % traceback.format_exc())
		
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlanid.set(self.config.config_vars.vlan_id_num_except)
		time.sleep(3)
		logger.debug("VirtualLanPage : Clicking next button...")
		self.next.click()
		if not self.vlan_id_range_error:
			raise AssertionError("Vlan ID range error not found. i.e . Traceback: %s" % traceback.format_exc())
		
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlanid.set(self.config.config_vars.vlan_id_spcl_char)
		time.sleep(3)
		logger.debug("VirtualLanPage : Clicking next button...")
		self.next.click()
		if not self.vlan_id_range_error:
			raise AssertionError("Vlan ID range error not found. i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlanid.set(self.config.config_vars.vlan_id_valid_char)
		time.sleep(3)
		logger.debug("VirtualLanPage : Clicking next button...")
		self.next.click()
		if self.client_ip_assignment:
			raise AssertionError("Vlan ID containg ',' and '-' was not accepted. i.e . Traceback: %s" % traceback.format_exc())
		self.back.click()
			
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlanid.set('')
		time.sleep(3)
		logger.debug("VirtualLanPage : Clicking next button...")
		self.next.click()
		if not self.vlan_id_req_error:
			raise AssertionError("Vlan ID required error not found. i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlanid.set(self.config.config_vars.vlan_id_max_char)
		time.sleep(3)
		logger.debug("VirtualLanPage : Clicking next button...")
		self.next.click()
		if not self.vlan_id_max_error:
			raise AssertionError("Vlan ID max length error not found. i.e . Traceback: %s" % traceback.format_exc())
			
	def validate_dynamic_default_vlan(self):
		import traceback
		self._select_client_vlan_assignment('dynamic')
		logger.debug("VirtualLanPage : Clicking on default rule...")
		self.default_vlan_id.click()
		logger.debug("VirtualLanPage : Clicking on 'Edit' button...")
		self.default_vlan_edit.click()
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlanid_default.set(self.config.config_vars.vlan_id_alpha)
		self.vlan_id_edit_ok.click()		
		if not self.vlan_id_edit_range_error:
			raise AssertionError("Vlan ID range error not found. i.e . Traceback: %s" % traceback.format_exc())
		
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlanid_default.set(self.config.config_vars.Vlan_Id)
		self.browser.key_press(u'\ue004')
		self.browser.key_press(u'\ue004')
		logger.debug("VirtualLanPage : Clicking ok button...")
		self.vlan_id_edit_ok.click()
		if self.vlan_id_edit_ok:
			raise AssertionError("Vlan ID as number was not accepted. i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("VirtualLanPage : Clicking on default rule...")
		self.default_vlan_id.click()
		logger.debug("VirtualLanPage : Clicking on 'Edit' button...")
		self.default_vlan_edit.click()
		
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlanid_default.set(self.config.config_vars.vlan_id_num_invalid)
		self.vlan_id_edit_ok.click()
		if not self.vlan_id_edit_range_error:
			raise AssertionError("Vlan ID range error not found. i.e . Traceback: %s" % traceback.format_exc())
		
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlanid_default.set(self.config.config_vars.Vlan_Id)
		self.browser.key_press(u'\ue004')
		self.browser.key_press(u'\ue004')		
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlanid_default.set(self.config.config_vars.vlan_id_num_except)
		self.vlan_id_edit_ok.click()
		if not self.vlan_id_edit_range_error:
			raise AssertionError("Vlan ID range error not found. i.e . Traceback: %s" % traceback.format_exc())
		
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlanid_default.set(self.config.config_vars.Vlan_Id)
		self.browser.key_press(u'\ue004')
		self.browser.key_press(u'\ue004')		
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlanid_default.set(self.config.config_vars.vlan_id_spcl_char)
		self.vlan_id_edit_ok.click()
		if not self.vlan_id_edit_range_error:
			raise AssertionError("Vlan ID range error not found. i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlanid_default.set(self.config.config_vars.vlan_id_valid_char)
		self.browser.key_press(u'\ue004')
		self.browser.key_press(u'\ue004')
		logger.debug("VirtualLanPage : Clicking ok button...")
		self.vlan_id_edit_ok.click()
		if self.vlan_id_edit_ok:
			raise AssertionError("Vlan ID containg ',' and '-' was not accepted. i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("VirtualLanPage : Clicking on default rule...")
		self.default_vlan_id.click()
		logger.debug("VirtualLanPage : Clicking on 'Edit' button...")
		self.default_vlan_edit.click()
			
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlanid_default.set(self.config.config_vars.vlan_id_max_char)
		self.vlan_id_edit_ok.click()
		if not self.vlan_id_edit_max_error:
			raise AssertionError("Vlan ID max length error not found. i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlanid_default.set(self.config.config_vars.Vlan_Id)
		self.browser.key_press(u'\ue004')
		self.browser.key_press(u'\ue004')	
		logger.debug("VirtualLanPage : Writing vlan id in text box...")
		self.vlanid_default.set('')
		self.vlan_id_edit_ok.click()
		if not self.vlan_id_edit_range_error:
			raise AssertionError("Vlan ID required error not found. i.e . Traceback: %s" % traceback.format_exc())
			
	def validate_dynamic_vlan_string(self, attribute = None):
		import traceback
		self._select_client_vlan_assignment('dynamic')
		logger.debug("VirtualLanPage : Clicking on 'New' button...")
		self.new.click()
		if attribute == 'mac and dhcp':
			logger.debug("VirtualLanPage : Selecting attribute as 'mac-address-and-dhcp-options'...")
			self.rule_attribute.set(self.config.config_vars.vlan_attribute_mac_and_dhcp)
		logger.debug("VirtualLanPage : Writing string in text box...")
		self.rule_string.set(self.config.config_vars.vlan_id_alpha)
		logger.debug("VirtualLanPage : Clicking 'OK' button...")
		self.ok.click()		
		if self.vlan_rule_strng_req_err:
			raise AssertionError("String not accepted. i.e . Traceback: %s" % traceback.format_exc())
		
		logger.debug("VirtualLanPage : Writing numbers in text box...")
		self.rule_string.set(self.config.config_vars.Vlan_Id)
		logger.debug("VirtualLanPage : Clicking 'OK' button...")
		self.ok.click()		
		if self.vlan_rule_strng_req_err:
			raise AssertionError("Numbers not accepted. i.e . Traceback: %s" % traceback.format_exc())
		
		logger.debug("VirtualLanPage : Writing special chars in text box...")
		self.rule_string.set(self.config.config_vars.vlan_id_spcl_char)
		logger.debug("VirtualLanPage : Clicking 'OK' button...")
		self.ok.click()
		if self.vlan_rule_strng_req_err:
			raise AssertionError("Special characters not accepted. i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("VirtualLanPage : Writing null string in text box...")
		self.rule_string.set('')
		logger.debug("VirtualLanPage : Clicking 'OK' button...")
		self.ok.click()
		if not self.vlan_rule_strng_req_err:
			raise AssertionError("'Required' error msg not found. i.e . Traceback: %s" % traceback.format_exc())
		
		if attribute == None:
			logger.debug("VirtualLanPage : Writing more than 32 characters in text box...")
			self.rule_string.set(self.config.config_vars.vlan_id_max_char)
			logger.debug("VirtualLanPage : Clicking 'OK' button...")
			self.ok.click()
			if not self.vlan_rule_strng_max_err:
				raise AssertionError("'1-32 characters' error msg not found. i.e . Traceback: %s" % traceback.format_exc())
				
		elif attribute == 'mac and dhcp':
			logger.debug("VirtualLanPage : Writing more than 255 characters in text box...")
			self.rule_string.set(self.config.config_vars.vlan_string_max_char_mac_dhcp)
			logger.debug("VirtualLanPage : Clicking 'OK' button...")
			self.ok.click()
			if not self.vlan_strng_max_mac_dhcp_err:
				raise AssertionError("'1-255 characters' error msg not found. i.e . Traceback: %s" % traceback.format_exc())
	
	def validate_dynamic_non_default_vlan(self):
		import traceback
		self._select_client_vlan_assignment('dynamic')
		logger.debug("VirtualLanPage : Clicking on 'New' button...")
		self.new.click()
		logger.debug("VirtualLanPage : Writing null character in text box...")
		self.rule_vlan_textbox.set('')
		logger.debug("VirtualLanPage : Clicking 'OK' button...")
		self.ok.click()
		if not self.vlan_rule_id_req_err:
			raise AssertionError("'Required' error msg not found. i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("VirtualLanPage : Writing alphabets in text box...")
		self.rule_vlan_textbox.set(self.config.config_vars.vlan_id_alpha)
		logger.debug("VirtualLanPage : Clicking 'OK' button...")
		self.ok.click()
		if not self.vlan_number_value_error:
			raise AssertionError("'Must be a number in range 1-4093 except 3333 ' error msg not found. i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("VirtualLanPage : Writing valid numbers in text box...")
		self.rule_vlan_textbox.set(self.config.config_vars.Vlan_Id_vlan)
		logger.debug("VirtualLanPage : Clicking 'OK' button...")
		self.ok.click()
		if self.vlan_number_value_error:
			raise AssertionError("'Must be a number in range 1-4093 except 3333 ' error msg found. i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("VirtualLanPage : Writing invalid numbers in text box...")
		self.rule_vlan_textbox.set(self.config.config_vars.vlan_id_num_invalid)
		logger.debug("VirtualLanPage : Clicking 'OK' button...")
		self.ok.click()
		if not self.vlan_number_value_error:
			raise AssertionError("'Must be a number in range 1-4093 except 3333 ' error msg not found. i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("VirtualLanPage : Writing invalid numbers in text box...")
		self.rule_vlan_textbox.set(self.config.config_vars.vlan_id_num_except)
		logger.debug("VirtualLanPage : Clicking 'OK' button...")
		self.ok.click()
		if not self.vlan_number_value_error:
			raise AssertionError("'Must be a number in range 1-4093 except 3333 ' error msg not found. i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("VirtualLanPage : Writing special characters in text box...")
		self.rule_vlan_textbox.set(self.config.config_vars.vlan_id_spcl_char)
		logger.debug("VirtualLanPage : Clicking 'OK' button...")
		self.ok.click()
		if not self.vlan_number_value_error:
			raise AssertionError("'Must be a number in range 1-4093 except 3333 ' error msg not found. i.e . Traceback: %s" % traceback.format_exc())
			
	def set_static_vlan_defaults(self):
		logger.debug("VirtualLanPage : set_static_vlan_defaults : Selecting 'network_assigned' option")
		self.network_assigned.click()
		logger.debug("VirtualLanPage : set_static_vlan_defaults : Selecting 'static' option")
		self.static.click()
		logger.debug("VirtualLanPage : set_static_vlan_defaults : Setting vlan id... ")
		self.vlanid.set(self.config.config_vars.Vlan_Id_new)
		logger.debug("VirtualLanPage : Clicking 'NEXT' button...")
		self.next.click()
		return SecurityPage(self.test, self.browser, self.config)
		
	def assert_static_vlan_required_message(self):
		logger.debug("VirtualLanPage : assert_static_vlan_required_message : Selecting 'network_assigned' option")
		self.network_assigned.click()
		logger.debug("VirtualLanPage : assert_static_vlan_required_message : Selecting 'static' option")
		self.static.click()
		logger.debug("VirtualLanPage : assert_static_vlan_required_message : Setting vlan id to empty... ")
		self.vlanid.set('')
		logger.debug("VirtualLanPage : Clicking 'NEXT' button...")
		self.next.click()
		import traceback
		if not self.vlan_id_req_error:
			raise AssertionError("Vlan id required message is not visible .Traceback: %s " %traceback.format_exc())
		
	def assert_up_down(self):
		import traceback
		logger.debug('VLAN Page : Selecting default vlan attribute')
		self.default_vlan_attribute_list.click()
		logger.debug('VLAN Page : Asserting UP arrow button')
		if not self.disabled_up_icon:
			raise AssertionError("Up button is enable .Traceback: %s " %traceback.format_exc())
		logger.debug('VLAN Page : Asserting DOWN arrow button')
		if not self.disabled_down_icon:
			raise AssertionError("Down button is enable .Traceback: %s " %traceback.format_exc())
		logger.debug('VLAN Page : Selecting created vlan attribute')
		self.buy_time()
		self.vlan_string.click()
		logger.debug('VLAN Page : Clicking on Delete button')
		self.delete_button.click()

		
	def validate_vlan_assignment_rules(self):
		logger.debug("VirtualLanPage : Clicking network assigned radio button...")
		self.network_assigned.click()
		logger.debug("VirtualLanPage : Clicking dyanamic radio button...")
		self._select_client_vlan_assignment('dynamic')
		logger.debug("VirtualLanPage : Clicking default vlan ...")
		self.default_vlan_attribute_list.click()
		logger.debug("VirtualLanPage : Clicking edit button...")
		self.default_vlan_edit.click()
		logger.debug('VirtualLanPage : writing invalid vlan id')
		self.vlan_id.set(self.config.config_vars.invalid_vlan_Id_new)
		logger.debug("VirtualLanPage : Clicking ok button ...")
		self.vlan_id_edit_ok.click()
		if not self.vlan_id_edit_range_error :
			raise AssertionError("'Required' error msg not found. i.e . Traceback: %s" % traceback.format_exc())
			
	def assert_operator(self):
		import traceback
		logger.debug("VirtualLanPage : assert_operator : Selecting 'Dynamic_vlan'...")
		self.dynamic_vlan.click()
		logger.debug("VirtualLanPage : assert_operator : Clicking 'NEW' button ...")
		self.new.click()
		logger.debug("VirtualLanPage : assert_operator : Setting 'rule_attribute'...")
		self.rule_attribute.set(self.config.config_vars.Vlan_Rule_Attribute1)
		logger.debug("VirtualLanPage : assert_operator : Setting 'rule_operator'...")
		self.rule_operator.set(self.config.config_vars.rule_operator_value)
		import time
		time.sleep(8)
		if self.config.config_vars.rule_operator_value == self.rule_attribute.get_selected():
			raise AssertionError("Operator is not set to Matches regular expression .Traceback: %s " %traceback.format_exc())

	def assert_default_client_ip_assignment(self):
		if not self.network_assigned.is_selected():
			raise AssertionError('Client IP assignment : Network assigned is not selected.i.e . Traceback: %s' % traceback.format_exc())
	
	def assert_default_client_vlan_assignmenet(self):
		if not self.default.is_selected():
			raise AssertionError('Client VLAN assignment : default is not selected.i.e . Traceback: %s' % traceback.format_exc())
	
	def assert_new_vlan_assignment_rule_attribute(self):
		logger.debug("VlanPage :Enable to dyanamic.")
		self._select_client_vlan_assignment('dynamic')
		logger.debug("VLanPage : Clicking new button")
		self.new.click()
		if not self.rule_attribute.get_selected() == self.config.config_vars.Vlan_Rule_Attribute:
			raise AssertionError('VirtualLan page: rule attribute is not set to default value "AP Group".i.e . Tracebsack: %s' % traceback.format_exc())
			
	def assert_default_value_vlan_dyanamic(self):
		logger.debug("VlanPage :Enable to dyanamic.")
		self._select_client_vlan_assignment('dynamic')
		if not self.vlan_rules_list:
			raise AssertionError('VLanPage : Vlan assignment rule table not displayed.i.e . Traceback: %s' % traceback.format_exc())
		self.check_dynamic_vlan_attribute_list()
		
		
	def create_dynamic_vlan_assignment_rule_with_differnt_attribute(self,option):
		self.network_assigned.click()
		logger.debug("VirtualLanPage : Selecting 'Dynamic'...")
		self.dynamic_vlan.click()
		logger.debug("VirtualLanPage : Clicking 'new'...")
		self.new.click()
		logger.debug("VirtualLanPage : Selecting '%s'..." %option)
		self.rule_attribute.set(option)
		
		logger.debug("VirtualLanPage : Writing invalid value in  Vlan text box...")
		self.rule_vlan_textbox.set(self.config.config_vars.invalid_vlan_number_value)
		self.ok.click()
		if not self.vlan_number_value_error: 
			raise AssertionError("Vlan  accepting invalid values i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("VirtualLanPage : Writing null string in text box...")
		self.rule_string.set('')
		logger.debug("VirtualLanPage : Clicking 'OK' button...")
		self.ok.click()
		if not self.vlan_rule_strng_req_err:
			raise AssertionError("'Required' error msg not found. i.e . Traceback: %s" % traceback.format_exc())
			
		self.rule_string.set(self.config.config_vars.string_value)
		self.rule_vlan_textbox.set(self.config.config_vars.vlan_number_value)
		logger.debug("VirtualLanPage : Clicking 'OK' button...")
		self.ok.click()
		#self.ok.click()
		
	def delete_dynamic_vlan_assignment_rule_with_differnt_attribute(self):
		logger.debug('VLAN Page : Selecting created vlan rule')
		self.vlan_string.click()
		logger.debug('VLAN Page : Clicking on Delete button')
		self.delete_button.click()
		if self.vlan_string:
			raise AssertionError("rule not deleted. i.e . Traceback: %s" % traceback.format_exc())
	
	def validate_acct_input_gigawords(self):
		'''
			Validate Vlan Assignment Rule with Acct-Input-Gigawords should be deleteable
		'''
		logger.debug("VLAN Page : Selecting the default value of network")
		self.check_dynamic_vlan_attribute_list()
		logger.debug("VLAN Page : Clicking on new button to create new VLan assignment rule")
		self.new.click()
		logger.debug("VLAN Page : Setting the attribute field in VLan assignment rule")
		self.set_rule_attribute_value("Acct-Input-Gigawords")
		logger.debug("VLAN Page : Setting the operator field in VLan assignment rule")
		self.set_rule_operator_value()
		logger.debug("VLAN Page : Setting the string field in VLan assignment rule")
		self.set_rule_string_value()
		logger.debug("VLAN Page : Setting the VLAN field in VLan assignment rule")
		self.set_rule_vlan_textbox_value()
		logger.debug("VLAN Page : Clicking on OK button to create new VLan assignment rule")
		self._click_ok()
		self.acct_input_gigawords.click()
		logger.debug("VLAN Page : Deleting the selected VLan assignment rule")
		self.delete_button.click()
		
	
	def validate_ARAP_zone_access(self):
		'''
			Validate Vlan Assignment Rule with ARAP-Zone-Access should be deleteable
		'''
		logger.debug("VLAN Page : Selecting the default value of network")
		self.check_dynamic_vlan_attribute_list()
		logger.debug("VLAN Page : Clicking on new button to create new VLan assignment rule")
		self.new.click()
		logger.debug("VLAN Page : Setting the attribute field in VLan assignment rule")
		self.set_rule_attribute_value("ARAP-Zone-Access")
		logger.debug("VLAN Page : Setting the operator field in VLan assignment rule")
		self.set_rule_operator_value()
		logger.debug("VLAN Page : Setting the string field in VLan assignment rule")
		self.set_rule_string_value()
		logger.debug("VLAN Page : Setting the VLAN field in VLan assignment rule")
		self.set_rule_vlan_textbox_value()
		logger.debug("VLAN Page : Clicking on OK button to create new VLan assignment rule")
		self._click_ok()
		self.arap_zone_access.click()
		logger.debug("VLAN Page : Deleting the selected VLan assignment rule")
		self.delete_button.click()			
		
	def validate_delete_default_value(self):
		'''
			Validate Vlan Assignment Rule to delete default value.
		'''
		logger.debug("Selecting the default value of network")
		self.check_dynamic_vlan_attribute_list()
		self.default_vlan_attribute_list.click()
		logger.debug("Checking the assertion message")
		if not self.disable_delete:
			raise AssertionError("Delete button is not disabled. The default value will delete Traceback: %s " %traceback.format_exc())
		self._network_create_cancel()
				
		
	def set_rule_attribute_value(self,value=None):
		logger.debug("VLAN Page : Selecting the attribute value")
		if value == "Acct-Input-Gigawords":
			self.rule_attribute.set(self.config.config_vars.rule_attribute_gigawords)
		elif value == "ARAP-Zone-Access":
			self.rule_attribute.set(self.config.config_vars.rule_attribute_zone_access)
		else:
			self.rule_attribute.set(self.config.config_vars.rule_attribute_default)
		
	
	def set_rule_operator_value(self,value=None):
		logger.debug("VLAN Page : Selecting the operator value")
		if value == "equals":
			self.rule_operator.set(self.config.config_vars.rule_operator_rule_equals)
		else:
			self.rule_operator.set(self.config.config_vars.rule_operator_default)
	
	
	def set_rule_string_value(self,value=None):
		logger.debug("VLAN Page : Selecting the string value")
		if value:
			self.rule_string.set(value)
		else:
			self.rule_string.set(self.config.config_vars.Vlan_Rule_String1)
	
	
	def set_rule_vlan_textbox_value(self,value=None):
		logger.debug("VLAN Page : Selecting the VLAN value")
		if value:
			self.rule_vlan_textbox.set(value)
		else:
			self.rule_vlan_textbox.set(self.config.config_vars.Vlan_Id_vlan)
		
	
	def _click_ok(self):
		import time
		time.sleep(8)
		logger.debug("VLAN Page : Clicking on OK button")
		self.ok.click()
		
	def _network_create_cancel(self):
		import time
		time.sleep(4)
		logger.debug("VLAN Page : Clicking on 'cancle' button")
		self.network_create_cancel.click()

	def validate_static_vlan_id(self,value):
		'''
		Validate static vlan id
		'''
		#logger.debug('Vlan Page : Clicking on static radio button')
		#self._select_client_vlan_assignment('static')
		if value == '3333':
			logger.debug('VlanPage : Entering invalid value in Vlan Id')
			self.wired_vlan_id_textbox.set(value)
			logger.debug("VirtualLanPage : Clicking next button...")
			time.sleep(5)
			self.next.click()
			if not self.wired_invalid_vlan_id_msg:
				raise AssertionError("Vlan id is not accepting value 3333 .Traceback: %s " %traceback.format_exc())
		
		if value == 'over_max_length':
			logger.debug('VlanPage : Entering over max length value in Vlan Id')
			self.wired_vlan_id_textbox.set(value)
			logger.debug("VirtualLanPage : Clicking next button...")
			self.next.click()
			if not self.wired_invalid_vlan_id_msg:
				raise AssertionError("Vlan id is not accepting value having length over 32 chars .Traceback: %s " %traceback.format_exc())
		
		if value == '1,2':
			logger.debug('VlanPage : Entering comma seperated value in Vlan Id')
			self.wired_vlan_id_textbox.set(value)
			logger.debug("VirtualLanPage : Clicking next button...")
			self.next.click()
			if self.wired_invalid_vlan_id_msg:
				raise AssertionError("Vlan id is not invalid input .Traceback: %s " %traceback.format_exc())
			return SecurityPage(self.test, self.browser, self.config)
		
		if value == '100-200':
			logger.debug('VlanPage : Entering valid range in Vlan Id')
			self.wired_vlan_id_textbox.set(value)
			logger.debug("VirtualLanPage : Clicking next button...")
			self.allowed_vlan_label.click()
			self.buy_time()
			self.next.click()
			self.buy_time()
			if self.wired_invalid_vlan_id_msg:
				raise AssertionError("Vlan id is not invalid input .Traceback: %s " %traceback.format_exc())
			return SecurityPage(self.test, self.browser, self.config)			
		
		if value == '2':
			logger.debug('VlanPage : Entering over valid value in Vlan Id')
			self.wired_vlan_id_textbox.set(value)
			logger.debug("VirtualLanPage : Clicking next button...")
			self.next.click()
			if self.wired_invalid_vlan_id_msg:
				raise AssertionError("Vlan id is not invalid input .Traceback: %s " %traceback.format_exc())
			return SecurityPage(self.test, self.browser, self.config)	
			
	def assert_default_vlan_value(self):
		logger.debug("VirtualLanPage : Validating the default value of 'MODE' field ")
		if not self.mode.selected=='Trunk':
			raise AssertionError("Mode not trunk by default .Traceback: %s " %traceback.format_exc())
		logger.debug("VirtualLanPage : Validating the default value of 'CLIENT IP ASSIGNMENT' field ")
		if not self.virtual_controller.is_selected():
			raise AssertionError("'CLIENT IP ASSIGNMENT' radio not set to 'Virtual Controller Assigned' .Traceback: %s " %traceback.format_exc())
		logger.debug("VirtualLanPage : Validating the default value of 'ALLOWED VLAN' field ")
		if not self.wired_vlan_id_textbox.get() == 'all':
			raise AssertionError("'ALLOWED VLAN' not set to 'all' .Traceback: %s " %traceback.format_exc())
		
	def wired_network_mode(self):
		logger.debug("VirtualLanPage : Selecting the Access value in the 'MODE' field ")
		self.set_mode_value(self.config.config_vars.vlan_mode_value)
		logger.debug("VirtualLanPage : Validating the 'ALLOWED VLAN' field ")
		if self.wired_vlan_id_textbox:
			raise AssertionError("'Allowed Vlan' should not be display .Traceback: %s " %traceback.format_exc())
		logger.debug("VirtualLanPage : Clicking on next button. ")
		self.buy_time()
		self.browser.key_press(u'\ue004')
		self.next.click()
		self.buy_time()
		return SecurityPage(self.test, self.browser, self.config)
		
	def set_mode_value(self,value=None):
		logger.debug("VirtualLanPage : Selecting the value in the 'MODE' field ")
		if value:
			self.mode.set(value)
		else:
			self.mode.set(self.config.config_vars.Vlan_Mode)
			

	def edit_default_vlan_id(self,vlanid , next = True):
		import time
		logger.debug("VirtualLanPage : Clicking network assigned radio button...")
		self.network_assigned.click()
		logger.debug("VirtualLanPage : Clicking dyanamic radio button...")
		self._select_client_vlan_assignment('dynamic')
		logger.debug("VirtualLanPage : Clicking default vlan ...")
		self.default_vlan_attribute_list.click()
		logger.debug("VirtualLanPage : Clicking edit button...")
		self.default_vlan_edit.click()
		logger.debug('VirtualLanPage : writing invalid vlan id')
		self.vlan_id.set(vlanid)
		logger.debug("VirtualLanPage : Clicking ok button ...")
		self.vlan_id_edit_ok.click()		
# 		self.browser.key_press(u'\ue004')
		if next :
			self.next.click()
			return SecurityPage(self.test, self.browser, self.config)
		
	def click_on_next(self):
		self.next.click()
		return SecurityPage(self.test, self.browser, self.config)

	def assert_dynamic_operator_default_value(self):
		self.check_dynamic_vlan_attribute_list()
		logger.debug("VirtualLan Page : Clicking on New button")
		self.new.click()
		logger.debug("VirtualLanPage : Checking default value of operator")
		if not self.rule_operator.get_selected() == 'contains' :
			raise AssertionError("VirtualLanPage : default value of operator is not set to 'contains' ")
	
	def buy_time(self):
		import time
		time.sleep(6)
		
	def select_network_assigned(self):
		'''
		Selecting 'Network assigned' option
		'''
		logger.debug("VirtualLan Page : Clicking on 'Network assigned' option")
		self.network_assigned.click()
		time.sleep(2)
	
	def assert_static_vlanid_value(self):
		logger.debug("Asserting the static vlan id field")
		if not self.vlanid.get() == self.config.config_vars.vlan_default_value:
			raise AssertionError("VLanPage: vlan id is not set to default")	

	def assert_dynamic_default_vlanid_value(self):
		logger.debug("Asserting the dynamic default vlan id field")
		if not self.vlanid_default.get() == self.config.config_vars.vlan_default_value:
			raise AssertionError("VLanPage: vlan id is not set to default")
			
	def clicking_network_assigned(self):
		logger.debug("VLanPage: Clicking on 'Network Assigned' option button")
		self.network_assigned.click()
			
	def asserting_vlan_network_assigned_static_value(self):
		logger.debug("Asserting the default value of Client IP Assignment")
		if not self.virtual_controller.is_selected():
			raise AssertionError("'CLIENT IP ASSIGNMENT' radio not set to 'Virtual Controller Assigned' .Traceback: %s " %traceback.format_exc())
		logger.debug("VLanPage: Clicking on 'Network Assigned' option button")
		self.clicking_network_assigned()
		logger.debug("VLanPage: Clicking on 'Static' option button")
		self.static.click()
		self.assert_static_vlanid_value()
		
	def asserting_vlan_network_assigned_dynamic_value(self):
		logger.debug("Asserting the default value of Client IP Assignment")
		if not self.virtual_controller.is_selected():
			raise AssertionError("'CLIENT IP ASSIGNMENT' radio not set to 'Virtual Controller Assigned' .Traceback: %s " %traceback.format_exc())
		logger.debug("VLanPage: Clicking on 'Network Assigned' option button")
		self.clicking_network_assigned()
		logger.debug("VLanPage: Clicking on 'Dynamic' option button")
		self.dynamic_vlan.click()
		logger.debug("VlanPage: Clicking on default valn id ")
		self.default_vlan_id.click()
		logger.debug("VlanPage: Clicking on 'Edit' button ")
		self.default_vlan_edit.click()
		self.assert_dynamic_default_vlanid_value()
		
	def assert_wired_default_native_vlan_textbox(self):
		'''
		Asserts default Native Vlan textbox value
		'''
		logger.debug("VLanPage: Asserting whether Native Vlan textbox is empty")
		self.browser.assert_text(self.wired_native_vlan_textbox,'','Native Vlan textbox  is not empty','value')
		
	def assert_wired_default_allowed_vlan_textbox(self):
		'''
		Asserts default Allowed Vlan textbox value
		'''
		logger.debug("VirtualLanPage : Validating the default value of 'ALLOWED VLAN' field ")
		self.browser.assert_text(self.wired_vlan_id_textbox, self.config.config_vars.allowed_vlan,'"ALLOWED VLAN" not set to "all"','value')	
	
	def set_native_vlan(self,id):
		'''
		Sets Native Vlan id 
		'''
		logger.debug("VirtualLanPage : Writing Native vlan id  value")
		self.wired_native_vlan_textbox.set(id)
		self.buy_time()
		
	def validate_native_vlan(self):
		'''
		Validating Native Vlan values
		'''
		conf = self.config.config_vars
		logger.debug("VirtualLanPage : set wired native vlan  ")
		self.set_native_vlan(conf.invalid_vlan_Id_new)
		logger.debug("VirtualLanPage : clicking on Next button")
		self.click_on_next()
		logger.debug("VirtualLanPage : checking wired native vlan error is present ")
		self.browser.assert_element(self.wired_native_vlan_error, "Accepting invalid range for Native vlan")
		logger.debug("VirtualLanPage : set wired native vlan  ")
		self.set_native_vlan(conf.vlan_id_num_except)
		logger.debug("VirtualLanPage : clicking on Next button")
		self.click_on_next()
		logger.debug("VirtualLanPage : checking wired native vlan error is present ")
		self.browser.assert_element(self.wired_native_vlan_error1, "Accepting reserved value 3333 for Native vlan")
		
	def set_rule_operator_values(self,value):
		logger.debug("VLAN Page : Selecting the operator value")
		if value == "defaults":
			self.rule_operator.set(self.config.config_vars.rule_operator_default)
		else:
			self.rule_operator.set(value)
	
	def click_on_new(self):
		'''
		clicking on New button
		'''
		logger.debug("VLAN Page : clicking on ok ") 
		self.new.click()	
	
	def create_new_vlan_assignment_rule(self,operator,string,vlan):	
		'''
		Creating Vlan Assignment rules
		'''
		conf = self.config.config_vars
		logger.debug("VLAN Page : calling  click_on_new method") 
		self.click_on_new()
		logger.debug("VLAN Page : calling  set_rule_operator_values ") 
		self.set_rule_operator_values(operator)
		logger.debug("VLAN Page : calling  set_rule_string_value ") 
		self.set_rule_string_value(string)
		logger.debug("VLAN Page : calling  set_rule_vlan_textbox_value ") 
		self.set_rule_vlan_textbox_value(vlan)
		self._click_ok()
		
	def get_and_assert_rule_operator_dropdown_elements(self):
		'''
		Asserting Rule Operator dropdown elements and its default value
		'''
		conf = self.config.config_vars
		self.buy_time()
		logger.debug("VLAN Page : gettoing  Rule Operator elements") 
		options = self.rule_operator.get_options()
		logger.debug('SecurityPage : Checking for Rule Operator options') 
		if not options[0] == conf.rule_operator_default:
			raise AssertionError("'contains' element not found i.e. Traceback: %s" %traceback.format_exc())
		if not options[1] == conf.rule_operator_rule_equals:
			raise AssertionError("'equals' element not found i.e. Traceback: %s" %traceback.format_exc())	
		if not options[2] == conf.rule_operator_rule_not_equals:
			raise AssertionError("'not-equals' element not found i.e. Traceback: %s" %traceback.format_exc())
		if not options[3] == conf.rule_operator_rule_starts_with:
			raise AssertionError("'starts-with' element not found i.e. Traceback: %s" %traceback.format_exc())	
		if not options[4] == conf.rule_operator_rule_ends_with:
			raise AssertionError("'ends-with' element not found i.e. Traceback: %s" %traceback.format_exc())	
		
	def assert_vlan_string_error(self):
		'''
		Asserts Vlan String Name error
		'''	
		logger.debug("VLAN Page : checking  error message of Vlan String") 
		self.browser.assert_element(self.wired_vlan_string_error, "Accepting Invalid Vlan String value")
	
	def validate_vlan_assignment(self):
		'''
		Validating  Vlan values
		'''
		conf = self.config.config_vars
		logger.debug("VirtualLanPage : set wired native vlan  ")
		self.set_rule_vlan_textbox_value(conf.invalid_vlan_Id_new)
		logger.debug("VirtualLanPage : clicking on ok button")
		self._click_ok()
		logger.debug("VirtualLanPage : checking wired native vlan error is present ")
		self.browser.assert_element(self.vlan_number_value_error, "Accepting invalid range for Native vlan")
		logger.debug("VirtualLanPage : set wired native vlan  ")
		self.set_rule_vlan_textbox_value(conf.vlan_id_num_except)
		logger.debug("VirtualLanPage : clicking on Ok button")
		self._click_ok()
		logger.debug("VirtualLanPage : checking wired native vlan error is present ")
		self.browser.assert_element(self.vlan_number_value_error, "Accepting reserved value 3333 for Native vlan")
		self.click_on_canel()
		
	def click_on_canel(self):
		'''
		clicking on Cancel button
		'''
		logger.debug("VLAN Page : clicking on Cancel ") 
		self.cancel_vlan_form_button.click()	
		
	def assert_vlan_delete_edit_options(self):
		'''
		Assert Delete, Edit button is present for newly created vlan
		'''
		logger.debug("VLAN Page : clicking on Vlan rule ") 
		self.vlan_string.click()
		logger.debug("VirtualLanPage : checking vlan rule Edit button is present ")
		self.browser.assert_element(self.edit_vlan_rule_button, "Accepting reserved value 3333 for Native vlan")
		logger.debug("VirtualLanPage : checking vlan rule Delete button is present ")
		self.browser.assert_element(self.delete_button, "Accepting reserved value 3333 for Native vlan")
		
		
		
		
		
	def assert_native_allowed_vlan_and_vlan_new(self):
		'''
		Native vlan :
		Allowed vlan : all
		'''
		self.assert_wired_default_native_vlan_textbox()
		self.assert_wired_default_allowed_vlan_textbox()
		self.browser.assert_element(self.new, "New button is not present")
		
	def set_wired_vlan_id(self,id):
		'''
		Sets Wired Vlan id
		'''
		logger.debug('VlanPage : Entering value in Vlan Id')
		self.wired_vlan_id_textbox.set(id)
		
	def validate_allowed_vlan_values(self):
		'''
		Validating Allowed Vlan Field for Different values
		'''
		conf = self.config.config_vars
		logger.debug("VirtualLanPage : sets wired allowed vlan  ")
		self.set_wired_vlan_id(conf.vlan_id_num_except)
		logger.debug("VirtualLanPage : clicking on Next button")
		self.click_on_next()
		logger.debug("VirtualLanPage : checking wired Allowed vlan error is present ")
		self.browser.assert_element(self.wired_invalid_vlan_id_msg, "Vlan id is not invalid input ")
		
		logger.debug("VirtualLanPage : sets wired allowed vlan  ")
		self.set_wired_vlan_id(conf.allowed_valid_vlan_id)
		logger.debug("VirtualLanPage : clicking on Next button")
		self.click_on_next()
		logger.debug("VirtualLanPage : checking wired Allowed vlan error is present ")
		self.browser.assert_element(self.wired_invalid_vlan_id_msg,'Vlan id is not accepting valid input',False)
		
		logger.debug("VirtualLanPage : sets wired allowed vlan  ")
		self.set_wired_vlan_id(conf.valid_vlan_id1)
		logger.debug("VirtualLanPage : clicking on Next button")
		self.click_on_next()
		logger.debug("VirtualLanPage : checking wired Allowed vlan error is present ")
		self.browser.assert_element(self.wired_invalid_vlan_id_msg,'Vlan id is not accepting valid input',False)
	
		logger.debug("VirtualLanPage : sets wired allowed vlan  ")
		self.set_wired_vlan_id(conf.allowed_invalid_vlan_id)
		logger.debug("VirtualLanPage : clicking on Next button")
		self.click_on_next()
		logger.debug("VirtualLanPage : checking wired Allowed vlan error is present ")
		self.browser.assert_element(self.wired_invalid_vlan_id_msg, "Vlan id is not invalid input ")
	
		logger.debug("VirtualLanPage : sets wired allowed vlan  ")
		self.set_wired_vlan_id(conf.allowed_vlan)
		logger.debug("VirtualLanPage : clicking on Next button")
		self.click_on_next()
		logger.debug("VirtualLanPage : checking wired Allowed vlan error is present ")
		self.browser.assert_element(self.wired_invalid_vlan_id_msg,'Vlan id is not accepting valid input',False)
	
		logger.debug("VirtualLanPage : sets wired allowed vlan  ")
		self.set_wired_vlan_id(conf.invalid_vlan_id1)
		logger.debug("VirtualLanPage : clicking on Next button")
		self.click_on_next()
		logger.debug("VirtualLanPage : checking wired Allowed vlan error is present ")
		self.browser.assert_element(self.wired_invalid_vlan_id_msg, "Vlan id is not invalid input ")
	
		logger.debug("VirtualLanPage : sets wired allowed vlan  ")
		self.set_wired_vlan_id(conf.vlan_id_max_char)
		logger.debug("VirtualLanPage : clicking on Next button")
		self.click_on_next()
		logger.debug("VirtualLanPage : checking wired Allowed vlan error is present ")
		self.browser.assert_element(self.allowed_vlan_max_error, "Vlan id is not invalid input ")
	
	def create_multiple_vlan_assignment_rules(self):
		'''
		Creating Assignment rules with combination of attributes and operator with vlan-id
		'''
		conf = self.config.config_vars
		self.create_new_vlan_assignment_rule(conf.rule_operator_rule_equals,conf.Vlan_Rule_String1,conf.Vlan_Id_vlan)
		self.create_new_vlan_assignment_rule(conf.rule_operator_default,conf.Vlan_Rule_String2,conf.Vlan_Id_vlan1)
		self.create_new_vlan_assignment_rule(conf.rule_operator_rule_not_equals,conf.Vlan_Rule_String3,conf.Vlan_Id_vlan2)
		self.create_new_vlan_assignment_rule(conf.rule_operator_rule_starts_with,conf.Vlan_Rule_String3,conf.Vlan_Id_vlan3)
		self.create_new_vlan_assignment_rule(conf.rule_operator_rule_ends_with,conf.Vlan_Rule_String4,conf.Vlan_Id_vlan4)
		self.create_new_vlan_assignment_rule(conf.rule_operator_rule_equals,conf.Vlan_Rule_String5,conf.Vlan_Number)
		self.create_new_vlan_assignment_rule(conf.rule_operator_rule_equals,conf.Vlan_Rule_String1,conf.Vlan_Id_vlan1)
		self.create_new_vlan_assignment_rule(conf.rule_operator_default,conf.Vlan_Rule_String2,conf.Vlan_Id_vlan)
		self.create_new_vlan_assignment_rule(conf.rule_operator_rule_not_equals,conf.Vlan_Rule_String3,conf.Vlan_Id_vlan1)
		self.create_new_vlan_assignment_rule(conf.rule_operator_rule_starts_with,conf.Vlan_Rule_String3,conf.Vlan_Id_vlan4)
		
	def click_rule_down(self):
		'''
		Click on Move selected rule Down
		'''
		logger.debug("VirtualLanPage : clicking on Down arrow button")
		self.move_selected_rule_down.click()
	
	def click_rule_up(self):
		'''
		Click on Move selected rule Up
		'''
		logger.debug("VirtualLanPage : clicking on Up arrow button")
		self.move_selected_rule_up.click()
		
	def move_vlan_assignment_rule_up_and_down(self):
		'''
		move selected Vlan Assignment rule up and down
		'''
		logger.debug("VirtualLanPage : clicking on Vlan Assignment rule")
		self.vlan_string.click()
		logger.debug("VirtualLanPage : clicking on Down arrow button")
		self.click_rule_down()
		logger.debug("VirtualLanPage : clicking on Down arrow button")
		self.click_rule_down()
		logger.debug("VirtualLanPage : clicking on Vlan Assignment rule")
		self.vlan_string5.click()
		logger.debug("VirtualLanPage : clicking on Up arrow button")
		self.click_rule_up()
		logger.debug("VirtualLanPage : clicking on Up arrow button")
		self.click_rule_up()
	
	def validate_access_vlan(self):
		'''
		validates access vlan field
		'''
		logger.debug('Vlan Page : Writing access vlan')
		self.access_vlan.set(self.config.config_vars.vlan_id_spcl_char)
		self.next.click()
		logger.debug('VLanPage : Asserting for access vlan error message ')
		if not self.vlan_access_range_error :
			raise AssertionError('VlanPage : Validation error message is not displayed for invalid value')
		logger.debug('Vlan Page : Writing access vlan')
		self.access_vlan.set(self.config.config_vars.Vlan_Rule_String2)
		self.next.click()
		logger.debug('VLanPage : Asserting for access vlan error message ')
		if not self.vlan_access_range_error :
			raise AssertionError('VlanPage : Validation error message is not displayed for invalid value')
		logger.debug('Vlan Page : Writing access vlan')
		self.access_vlan.set(self.config.config_vars.invalid_vlan_Id_new)
		self.next.click()
		logger.debug('VLanPage : Asserting for access vlan error message ')
		if not self.vlan_access_range_error :
			raise AssertionError('VlanPage : Validation error message is not displayed for invalid value')
		logger.debug('Vlan Page : Writing access vlan')
		self.access_vlan.set(self.config.config_vars.max_auth_failure0)
		self.next.click()
		logger.debug('VLanPage : Asserting for access vlan error message ')
		if not self.vlan_access_range_error :
			raise AssertionError('VlanPage : Validation error message is not displayed for invalid value')
		logger.debug('Vlan Page : Writing access vlan')
		self.access_vlan.set(self.config.config_vars.vlan_id_num_except)
		self.next.click()
		logger.debug('VLanPage : Asserting for access vlan error message ')
		if not self.vlan_access_range_error :
			raise AssertionError('VlanPage : Validation error message is not displayed for invalid value')
		logger.debug('Vlan Page : Writing access vlan')
		self.access_vlan.set(self.config.config_vars.vlan_id_num_invalid)
		self.next.click()
		logger.debug('VLanPage : Asserting for access vlan error message ')
		if not self.vlan_access_range_error :
			raise AssertionError('VlanPage : Validation error message is not displayed for invalid value')

	def set_access_vlan(self, id):
		'''
		writes access vlan 
		'''
		logger.debug('VLanPage: Writing Access vlan')
		self.access_vlan.set(id)
	
	def create_new_dynamic_vlan_assignment_rule(self,string,vlan_id,attribute=None,operator=None):
		'''
		Creates new dynamic vlan assignment rule
		'''
		self._select_client_vlan_assignment('dynamic')
		self.click_on_new()
		if attribute:
			self.set_rule_attribute_value(attribute)
		else:
			self.set_rule_attribute_value()
		if operator:
			self.set_rule_operator_value(operator)
		else:
			self.set_rule_operator_value()
		self.set_rule_string_value(string)
		self.set_rule_vlan_textbox_value(vlan_id)
		self._click_ok()
		
	def assert_default_vlan_value(self):
		'''
		Asserting default value of vlan page.
		'''
		logger.debug('VLanPage: Asserting default value of client IP assignment.')
		if not self.virtual_controller.is_selected():
			raise AssertionError("'CLIENT IP ASSIGNMENT' radio not set to 'Virtual Controller Assigned' .Traceback: %s " %traceback.format_exc())