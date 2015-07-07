from athenataf.lib.util.WebPage import WebPage
import traceback
import time
import logging
logger = logging.getLogger('athenataf')

class PortsPage(WebPage):
	def __init__(self, test, browser, config):
		WebPage.__init__(self, "Ports", test, browser, config)
		self.test.assertPageLoaded(self)


	def isPageLoaded(self):
		if self.ports:
			return True    
		else:
			return False 

	def changing_access_vlan_value(self, assert_fields = False):
		'''
			Setting the Access VLAN value
		'''
		logger.debug("Port : clicking on checkbox")
		self.browser.refresh()
		self.check_box_6.click()
		logger.debug("Port : clicking on edit button")        
		self.edit.click()
		logger.debug("Setting port mode")
		self.set_port_mode()
		logger.debug("Setting value of access vlan")
		self.access_vlan.set(self.config.config_vars.access_vlan)
		if assert_fields == True:
			self.assert_option_fields('disabled_native_vlan')
			self.assert_option_fields('disabled_allowed_vlan')
		logger.debug("Clicking on Save button.")
		self.save.click()

	def set_default_access_vlan_value(self):
		'''
			Setting the default value in Access VLAN field
		'''
		logger.debug("Port : clicking on checkbox")
		self.browser.refresh()
		self.check_box_6.click()
		logger.debug("Port : clicking on edit button")        
		self.edit.click()
		logger.debug("Setting port mode")
		self.set_port_mode()
		logger.debug("Setting value of access vlan")
		self.access_vlan.set(self.config.config_vars.access_vlan1)
		logger.debug("Clicking on Save button.")
		self.save.click()

	def assert_option_fields(self, field_name):
		'''
		Asserting option fields of PortsPage
		'''
		if field_name == 'disabled_native_vlan':
			if not self.disable_native_vlan:
				raise AssertionError("Native Vlan field is not disabled .Traceback: %s " %(self.wired_network2,traceback.format_exc()))

		if field_name == 'disabled_allowed_vlan':
			if not self.disable_allowed_vlan:
				raise AssertionError("Allowed Vlan field is not disabled .Traceback: %s " %(self.wired_network2,traceback.format_exc()))

	def change_Admin_status(self):
		'''
			Changing the Admin status field value
		'''
		logger.debug("Port : clicking on checkbox")
		self.browser.refresh()
		self.check_box_6.click()
		logger.debug("Port : clicking on edit button")
		self.edit.click()
		logger.debug("Port : setting admin status")
		self.set_admin_status('Down')
		time.sleep(5)
		logger.debug("Clicking on Save button.")
		self.save.click()

	def set_default_Admin_status(self):
		'''
			Setting the default value in Admin status field
		'''
		logger.debug("Port : clicking on checkbox")
		self.browser.refresh()
		self.check_box_6.click()
		logger.debug("Port : clicking on edit button")        
		self.edit.click()
		logger.debug("Port : setting admin status")
		self.set_admin_status()
		logger.debug("Clicking on Save button.")
		self.save.click()        

	def set_admin_status(self,status=None):
		'''
			Setting the value in Admin status field
		'''
		logger.debug("PortPage: Selecting the value of Admin Field")
		if status=='Down':
			self.admin_status.set(self.config.config_vars.admin_down)
			self.browser.key_press(u'\ue004')
		else:
			self.admin_status.set(self.config.config_vars.admin_up)
			self.browser.key_press(u'\ue004')

	def changing_port_mode_and_native_vlan(self):
		'''
			Setting values in port mode and native vlan field
		'''
		logger.debug("Port : clicking on checkbox")
		self.browser.refresh()
		self.check_box_6.click()
		logger.debug("Port : clicking on edit button")        
		self.edit.click()
		logger.debug("Setting port mode")
		self.set_port_mode('Trunk')
		logger.debug("Setting native vlan value")
		self.native_vlan.set(self.config.config_vars.access_vlan)
		logger.debug("Clicking on Save button.")
		self.save.click()         

	def set_port_mode(self, mode=None):
		'''
			Setting the value in port mode field
		'''
		logger.debug("Setting port mode")
		if mode == 'Trunk':
			self.port_mode.set(self.config.config_vars.portmode_trunk)
			self.browser.key_press(u'\ue004')
		else:
			self.port_mode.set(self.config.config_vars.portmode_access)
			self.browser.key_press(u'\ue004')

	def set_poe(self,value=None):
		'''
			Setting the value in POE field
		'''
		logger.debug("PortPage: Selecting the value of Poe Field")
		if value=='Disabled':
			self.poe.set(self.config.config_vars.poe1_disabled)
			self.browser.key_press(u'\ue004')
		else:
			self.poe.set(self.config.config_vars.poe1_enabled)
			self.browser.key_press(u'\ue004')

	def set_speed_duplex(self,speed=None):
		'''
			Setting the value in Speed/Duplex field
		'''
		logger.debug("PortPage: Selecting the value of Speed/Duplex Field")
		if speed=='10 Mbps':
			self.speed_duplex.set(self.config.config_vars.speed_10mbps)
			self.browser.key_press(u'\ue004')
		elif speed== '100 Mbps':
			self.speed_duplex.set(self.config.config_vars.speed_100mbps)
			self.browser.key_press(u'\ue004')
		elif speed=='1 Gbps':
			self.speed_duplex.set(self.config.config_vars.speed_1gbps)
			self.browser.key_press(u'\ue004')
		else:
			self.speed_duplex.set(self.config.config_vars.speed_auto)
			self.browser.key_press(u'\ue004')

	def setting_port_access_default(self):
		'''
			Setting the default value for Access port mode for checkbox 6
		'''
		logger.debug("Port : clicking on checkbox")
		self.browser.refresh()
		self.check_box_6.click()
		logger.debug("Port : clicking on edit button")        
		self.edit.click()
		logger.debug("Port : setting port mode")
		self.set_port_mode()
		logger.debug("Port : setting access vlan")
		self.access_vlan.set(self.config.config_vars.access_vlan1)
		logger.debug("Port : setting poe field")
		self.set_poe()
		logger.debug("Port : setting speed/duplex")
		self.set_speed_duplex()
		logger.debug("Port : setting admin status")
		self.set_admin_status()
		logger.debug("Clicking on Save button.")
		self.save.click()         

	def setting_port_trunk_default(self):
		'''
			Setting the default value for Trunk port mode for checkbox 6
		'''
		logger.debug("Port : clicking on checkbox")
		self.browser.refresh()
		self.check_box_6.click()
		logger.debug("Port : clicking on edit button")        
		self.edit.click()
		logger.debug("Port : setting port mode")
		self.set_port_mode('Trunk')
		logger.debug("Port : setting native vlan")
		self.native_vlan.set(self.config.config_vars.access_vlan1)
		logger.debug("Port : setting allowed vlan")
		self.allowed_vlan.set(self.config.config_vars.allowed_vlan_default)        
		logger.debug("Port : setting poe field")
		self.set_poe()
		logger.debug("Port : setting speed/duplex")
		self.set_speed_duplex()
		logger.debug("Port : setting admin status")
		self.set_admin_status()
		logger.debug("Clicking on Save button.")
		self.save.click() 

	def verify_port_page_field(self):
		'''
			Assert the label fields of Port page
		'''
		logger.debug("Port : verify port number label")
		if not self.port_number_label:
			raise AssertionError("Port number label is not present .Traceback: %s " %(self.wired_network2,traceback.format_exc()))
		logger.debug("Port : verify admin status label")
		if not self.admin_status_label:
			raise AssertionError("Admin status label is not present .Traceback: %s " %(self.wired_network2,traceback.format_exc()))
		logger.debug("Port : verify port mode label")
		if not self.port_mode_label:
			raise AssertionError("Port mode label is not present .Traceback: %s " %(self.wired_network2,traceback.format_exc()))
		logger.debug("Port : verify vlan label")
		if not self.vlan_label:
			raise AssertionError("VLAN label is not present .Traceback: %s " %(self.wired_network2,traceback.format_exc()))
		logger.debug("Port : verify POE label")
		if not self.poe_label:
			raise AssertionError("POE label is not present .Traceback: %s " %(self.wired_network2,traceback.format_exc()))
		logger.debug("Port : verify speed label")
		if not self.speed_duplex_label:
			raise AssertionError("Speed/Duplex label is not present .Traceback: %s " %(self.wired_network2,traceback.format_exc()))

	def changing_trunk_port_mode_value(self):
		'''
			Changing the value of Port mode as Trunk
		'''
		logger.debug("Port : clicking on checkbox")
		self.browser.refresh()
		self.check_box_6.click()
		logger.debug("Port : clicking on edit button")        
		self.edit.click()
		logger.debug("Setting port mode")
		self.set_port_mode('Trunk')
		logger.debug("Clicking on Save button.")
		self.save.click()              

	def changing_access_port_mode_value(self):
		'''
			Changing the value of Port mode as Access
		'''
		logger.debug("Port : clicking on checkbox")
		self.browser.refresh()      
		self.check_box_6.click()
		logger.debug("Port : clicking on edit button")        
		self.edit.click()
		logger.debug("Setting port mode")
		self.set_port_mode()
		logger.debug("Clicking on Save button.")
		self.save.click()    

	def changing_poe_value_disabled(self):
		'''
			Changing the value of POE as Disable
		'''
		logger.debug("Port : clicking on checkbox")
		self.browser.refresh()
		self.check_box_6.click()
		logger.debug("Port : clicking on edit button")        
		self.edit.click()
		logger.debug("Setting port mode")
		self.set_poe('Disabled')
		logger.debug("Clicking on Save button.")
		self.save.click()              

	def changing_poe_value_enabled(self):
		'''
			Changing the value of POE as Enable
		'''
		logger.debug("Port : clicking on checkbox")
		self.browser.refresh()
		self.check_box_6.click()
		logger.debug("Port : clicking on edit button")        
		self.edit.click()
		logger.debug("Setting port mode")
		self.set_poe()
		logger.debug("Clicking on Save button.")
		self.save.click()    

	def selecting_checkbox_6(self,refresh1=True):
		'''
		 Selecting the ckeckbox 6
		'''
		if refresh1:
			self.browser.refresh()
		logger.debug("Port : clicking on checkbox")
		self.check_box_6.click()
		logger.debug("Port : clicking on edit button")        
		self.edit.click()

	def save_port_setting(self):
		'''
			Clicking on save setting button
		'''
		logger.debug("Clicking on Save button.")
		self.save.click()

	def set_native_vlan(self,value=None):
		'''
			Setting the value of Native vlan field
		'''
		logger.debug("PortPage: Setting the value of Native vlan")
		if value:
			self.native_vlan.set(value)
		else:
			self.native_vlan.set(self.config.config_vars.access_vlan1)

	def set_allowed_vlan(self,value=None):
		'''
			Setting the value of Allowed vlan field
		'''
		logger.debug("PortPage: Setting the value of Allowed vlan")
		if value:
			self.allowed_vlan.set(value)
		else:
			self.allowed_vlan.set(self.config.config_vars.allowed_vlan_default)

	def set_access_vlan(self,value=None):
		'''
			Setting the value of Access vlan field
		'''
		logger.debug("PortPage: Setting the value of Access vlan")
		if value:
			self.access_vlan.set(value)
		else:
			self.access_vlan.set(self.config.config_vars.access_vlan)    

	def selecting_checkbox_3(self,refresh1=True):
		'''
			Selecting the ckeckbox 3
		'''
		if refresh1:
			self.browser.refresh()
		logger.debug("Port : clicking on checkbox")        
		self.check_box_3.click()

	def selecting_checkbox_4(self,refresh1=True):
		'''
			Selecting the ckeckbox 4
		'''
		if refresh1:
			self.browser.refresh()
		logger.debug("Port : clicking on checkbox")        
		self.check_box_4.click()

	def selecting_checkbox_5(self,refresh1=True):
		'''
			Selecting the ckeckbox 5
		'''
		if refresh1:
			self.browser.refresh()
		logger.debug("Port : clicking on checkbox")        
		self.check_box_5.click()

	def cancel_port_setting(self):
		'''
			Clicking on Cancel button
		'''
		logger.debug("Clicking on cancel button.")
		# self.edit_port_label.click()
		self.browser.key_press(u'\ue004')
		time.sleep(8)
		self.cancel.click()
		
	def assert_access_vlan(self):
		'''
			Asserting Access vlan field
		'''
		logger.debug("PortsPage: Writing invalid value into access vlan id text box ")
		self.access_vlan.set(self.config.config_vars.invalid_access_vlan)
		if not self.access_vlan_error_msg :
			raise AssertionError("PortsPage : Access Vlan accepting invalid value")
		logger.debug("PortsPage: Writing invalid value into access vlan id text box ")
		self.access_vlan.set(self.config.config_vars.invalid_access_vlan1)
		if not self.access_vlan_error_msg :
			raise AssertionError("PortsPage : Access Vlan accepting invalid value")
		logger.debug("PortsPage: Writing invalid value into access vlan id text box ")
		self.access_vlan.set(self.config.config_vars.invalid_access_vlan2)
		if not self.access_vlan_error_msg :
			raise AssertionError("PortsPage : Access Vlan accepting invalid value")
	
	def assert_allow_vlan(self):
		'''
			Asserting Allowed vlan field
		'''
		logger.debug("PortsPage: Writing invalid value into access vlan id text box ")
		self.allowed_vlan.set(self.config.config_vars.invalid_access_vlan)
		if not self.allowed_vlan_error_msg :
			raise AssertionError("PortsPage : Access Vlan accepting invalid value")
		logger.debug("PortsPage: Writing invalid value into access vlan id text box ")
		self.allowed_vlan.set(self.config.config_vars.invalid_access_vlan1)
		if not self.allowed_vlan_error_msg :
			raise AssertionError("PortsPage : Access Vlan accepting invalid value")
		logger.debug("PortsPage: Writing invalid value into access vlan id text box ")
		self.allowed_vlan.set(self.config.config_vars.invalid_access_vlan2)
		if not self.allowed_vlan_error_msg :
			raise AssertionError("PortsPage : Access Vlan accepting invalid value")
		
	def assert_ports_number_and_format(self):
		'''
			Asserting ports on Port page
		'''
		logger.debug("PortsPage: validating 48th port on port page ")
		if not self.port_48th:
			raise AssertionError("PortsPage : 48 ports are not available")
		logger.debug("PortsPage: validating 4th uplink port on port page ")
		if not self.uplink_port_4th:
			raise AssertionError("PortsPage : 4 uplink ports are not available")
		logger.debug("PortsPage: validating the port format ")
		if not self.port_format:
			raise AssertionError("PortsPage : ports are not in proper format")
		
	def assert_s1500_12p_ports_number_and_format(self):
		'''
			Asserting ports on Port page for S1500 12p
		'''
		logger.debug("PortsPage: validating 12th port on port page ")
		if not self.port_12th:
			raise AssertionError("PortsPage : 48 ports are not available")
		logger.debug("PortsPage: validating 2nd uplink port on port page ")
		if not self.uplink_port_2nd:
			raise AssertionError("PortsPage : 4 uplink ports are not available")
		logger.debug("PortsPage: validating the port format ")
		if not self.port_format:
			raise AssertionError("PortsPage : ports are not in proper format")
			
	def assert_edit_disable_button(self):
		'''
			Assert Edit button
		'''
		logger.debug("PortsPage: validating the edit button ")
		if not self.edit_disabled:
			raise AssertionError("PortsPage : Edit button is not disabled")
			
	def click_edit_button(self):
		'''
			Clicking on edit button
		'''
		logger.debug("PortsPage: Clicking edit button ")
		self.edit.click()
		
	def setting_port_access_default_value(self):
		'''
			Setting Access mode default values for all fields
		'''
		logger.debug("Port : setting port mode")
		self.set_port_mode()
		logger.debug("Port : setting access vlan")
		self.access_vlan.set(self.config.config_vars.access_vlan1)
		logger.debug("Port : setting poe field")
		self.set_poe()
		logger.debug("Port : setting speed/duplex")
		self.set_speed_duplex()
		logger.debug("Port : setting admin status")
		self.set_admin_status()
		logger.debug("Clicking on Save button.")
		self.save.click()
	
	def assert_access_vlan_value(self,value=None):
		'''
			Assert Access vlan field
		'''
		logger.debug("PortPage: Verifying vlan value ")
		self.selecting_checkbox_3(refresh1=True)
		self.click_edit_button()
		if not self.access_vlan.get() == value:
			raise AssertionError("PortsPage : Given value not saved in access vlan field")
		self.cancel_port_setting()
		
	def assert_trunk_mode(self,value=None):
		'''
			Assert port mode as Trunk
		'''
		logger.debug("PortPage: Verifying vlan value ")
		self.selecting_checkbox_3(refresh1=True)
		self.click_edit_button()
		if not self.port_mode.get_selected() == value:
			raise AssertionError("PortsPage : Trunk is not selected in port mode field")
		self.cancel_port_setting()	
		
	def setting_port_trunk_default_value(self):
		'''
			Setting Trunk mode default values for all fields
		'''
		logger.debug("Port : setting port mode")
		self.set_port_mode('Trunk')
		logger.debug("Port : setting native vlan")
		self.native_vlan.set(self.config.config_vars.access_vlan1)
		logger.debug("Port : setting allowed vlan")
		self.allowed_vlan.set(self.config.config_vars.allowed_vlan_default)        
		logger.debug("Port : setting poe field")
		self.set_poe()
		logger.debug("Port : setting speed/duplex")
		self.set_speed_duplex()
		logger.debug("Port : setting admin status")
		self.set_admin_status()
		logger.debug("Clicking on Save button.")
		self.save.click()
		
	def assert_trunk_mode_allowed_vlan(self,value=None,vlan=None):
		'''
			Assert Trunk mode and Allowed vlan field
		'''
		logger.debug("PortPage: Verifying vlan value ")
		self.selecting_checkbox_3(refresh1=True)
		self.click_edit_button()
		if not self.port_mode.get_selected() == value:
			raise AssertionError("PortsPage : Trunk is not selected in port mode field")
		if not self.allowed_vlan.get() == vlan:
			raise AssertionError("PortsPage : Allowed vlan not showing the given value")
		self.cancel_port_setting()
	
	def assert_trunk_mode_native_and_allowed_vlan(self,check=True,value=None,n_vlan=None,a_vlan=None,alow_vlan=True):
		'''
			Assert Trunk mode and Native vlan field
		'''
		if check:
			self.selecting_checkbox_3(refresh1=True)
			self.click_edit_button()
		logger.debug("PortPage: Verifying vlan value ")
		if not self.port_mode.get_selected() == value:
			raise AssertionError("PortsPage : Trunk is not selected in port mode field")
		if not self.native_vlan.get() == n_vlan:
			raise AssertionError("PortsPage : Allowed vlan not showing the given value")
		if not alow_vlan:
			if not self.allowed_vlan.get() == a_vlan:
				raise AssertionError("PortsPage : Allowed vlan not showing the given value")		
	
	def assert_poe_field(self,value=None):
		'''
			Assert POE field
		'''
		logger.debug("PortPage: Verifying vlan value ")
		self.selecting_checkbox_3(refresh1=True)
		self.click_edit_button()
		if not self.poe.get_selected() == value:
			raise AssertionError("PortsPage : Trunk is not selected in port mode field")
		self.cancel_port_setting()	
	
	def assert_speed_duplex_value(self,value=None):
		logger.debug("PortPage: checking speed/duplex is set to the given value")
		if not self.speed_duplex.get_selected() == value :
			raise AssertionError("PortsPage : speed/duplex mode is not set to the given value")
	
	def selecting_checkbox_0(self,refresh1=True):
		'''
			Selecting the checkbox 0
		'''
		if refresh1:
			self.browser.refresh()
		logger.debug("Port : clicking on checkbox")        
		self.check_box_0.click()
	
	def assert_admin_status(self,value=None):
		logger.debug("PortPage: checking admin status is set to the given value")
		if not self.admin_status.get_selected() == value :
			raise AssertionError("PortsPage : admin status is not set to the given value")
	
	def assert_access_vlan_mode(self, value):
		'''
		checks whether access vlan field is editable or not
		'''
		if value == 'enabled':
			if not self.access_vlan_enabled:
				raise AssertionError("PortsPage : Access Vlan field is not editable")
		if value == 'disabled':
			if not self.access_vlan_disabled:
				raise AssertionError("PortsPage : Access Vlan field is editable")
				
	def assert_native_vlan_mode(self, value):
		'''
		checks whether native vlan field is editable or not
		'''
		if value == 'enabled':
			if not self.native_vlan_enabled:
				raise AssertionError("PortsPage : Native Vlan field is not editable")
		if value == 'disabled':
			if not self.native_vlan_disabled:
				raise AssertionError("PortsPage : Native Vlan field is editable")
	
	def assert_allowed_vlan_mode(self, value):
		'''
		checks whether allowed vlan field is editable or not
		'''
		if value == 'enabled':
			if not self.allowed_vlan_enabled:
				raise AssertionError("PortsPage : Allowed Vlan field is not editable")
		if value == 'disabled':
			if not self.allowed_vlan_disabled:
				raise AssertionError("PortsPage : Native Vlan field is editable")
				
	def _verify_admin_status(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_admin_status_1(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_1.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_1(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_1.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_1(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_1.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_1(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_1.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_1(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_1.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	
	def _verify_admin_status_2(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_2.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_2(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_2.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_2(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_2.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_2(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_2.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_2(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_2.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	
	def _verify_admin_status_3(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_3.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_3(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_3.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_3(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_3.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_3(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_3.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_3(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_3.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	
	def _verify_admin_status_4(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_4.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_4(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_4.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_4(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_4.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_4(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_4.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_4(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_4.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")	
	
	
	def _verify_admin_status_5(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_5.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_5(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_5.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_5(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_5.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_5(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_5.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_5(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_5.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")	
	
	
	def _verify_admin_status_6(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_6.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_6(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_6.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_6(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_6.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_6(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_6.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_6(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_6.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")	
	
	
	def _verify_admin_status_7(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_7.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_7(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_7.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_7(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_7.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_7(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_7.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_7(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_7.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")	
	
	
	def _verify_admin_status_8(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_8.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_8(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_8.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_8(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_8.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_8(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_8.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_8(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_8.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")	
	
	
	def _verify_admin_status_9(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_9.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_9(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_9.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_9(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_9.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_9(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_9.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_9(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_9.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")	
	
	
	def _verify_admin_status_10(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_10.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_10(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_10.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_10(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_10.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_10(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_10.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_10(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_10.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")	
	
	
	def _verify_admin_status_11(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_11.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_11(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_11.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_11(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_11.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_11(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_11.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_11(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_11.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")	
	
	
	def _verify_admin_status_12(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_12.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_12(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_12.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_12(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_12.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_12(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_12.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_12(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_12.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")	
	
	
	def _verify_admin_status_13(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_13.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_13(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_13.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_13(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_13.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_13(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_13.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_13(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_13.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")	
	
	
	def _verify_admin_status_14(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_14.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_14(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_14.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_14(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_14.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_14(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_14.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_14(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_14.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")	
	
	
	def _verify_admin_status_15(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_15.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_15(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_15.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_15(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_15.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_15(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_15.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_15(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_15.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")	
	
	
	def _verify_admin_status_16(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_16.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_16(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_16.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_16(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_16.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_16(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_16.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_16(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_16.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")	
	
	
	def _verify_admin_status_17(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_17.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_17(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_17.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_17(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_17.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_17(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_17.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_17(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_17.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")	
	
	
	def _verify_admin_status_18(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_18.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_18(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_18.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_18(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_18.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_18(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_18.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_18(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_18.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")	
	
	
	def _verify_admin_status_19(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_19.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_19(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_19.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_19(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_19.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_19(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_19.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_19(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_19.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")	
	
	
	def _verify_admin_status_20(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_20.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_20(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_20.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_20(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_20.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_20(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_20.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_20(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_20.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")	
	
	
	def _verify_admin_status_21(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_21.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_21(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_21.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_21(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_21.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_21(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_21.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_21(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_21.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")	
	
	
	def _verify_admin_status_22(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_22.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_22(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_22.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_22(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_22.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_22(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_22.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_22(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_22.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")	
	
	
	def _verify_admin_status_23(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_23.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_23(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_23.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_23(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_23.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_23(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_23.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_23(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_23.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")	
	
	
	def _verify_admin_status_24(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_24.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_24(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_24.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_24(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_24.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_24(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_24.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_24(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_24.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	
	def _verify_admin_status_25(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_25.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_25(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_25.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_25(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_25.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_25(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_25.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_25(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_25.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	
	def _verify_admin_status_26(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_26.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_26(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_26.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_26(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_26.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_26(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_26.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_26(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_26.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	
	def _verify_admin_status_27(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_27.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_27(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_27.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_27(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_27.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_27(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_27.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_27(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_27.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	
	def _verify_admin_status_28(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_28.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_28(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_28.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_28(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_28.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_28(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_28.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_28(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_28.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	
	def _verify_admin_status_29(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_29.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_29(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_29.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_29(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_29.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_29(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_29.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_29(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_29.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	
	def _verify_admin_status_30(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_30.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_30(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_30.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_30(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_30.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_30(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_30.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_30(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_30.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_admin_status_31(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_31.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_31(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_31.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_31(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_31.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_31(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_31.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_31(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_31.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_admin_status_32(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_32.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_32(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_32.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_32(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_32.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_32(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_32.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_32(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_32.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_admin_status_33(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_33.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_33(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_33.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_33(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_33.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_33(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_33.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_33(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_33.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_admin_status_34(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_34.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_34(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_34.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_34(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_34.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_34(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_34.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_34(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_34.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_admin_status_35(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_35.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_35(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_35.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_35(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_35.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_35(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_35.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_35(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_35.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_admin_status_36(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_36.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_36(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_36.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_36(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_36.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_36(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_36.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_36(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_36.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_admin_status_37(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_37.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_37(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_37.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_37(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_37.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_37(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_37.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_37(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_37.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_admin_status_38(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_38.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_38(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_38.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_38(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_38.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_38(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_38.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_38(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_38.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	
	def _verify_admin_status_39(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_39.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_39(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_39.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_39(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_39.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_39(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_39.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_39(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_39.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	
	def _verify_admin_status_40(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_40.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_40(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_40.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_40(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_40.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_40(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_40.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_40(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_40.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_admin_status_41(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_41.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_41(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_41.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_41(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_41.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_41(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_41.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_41(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_41.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_admin_status_42(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_42.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_42(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_42.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_42(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_42.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_42(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_42.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_42(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_42.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_admin_status_43(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_43.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_43(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_43.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_43(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_43.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_43(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_43.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_43(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_43.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_admin_status_44(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_44.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_44(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_44.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_44(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_44.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_44(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_44.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_44(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_44.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_admin_status_45(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_45.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_45(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_45.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_45(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_45.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_45(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_45.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_45(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_45.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_admin_status_46(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_46.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_46(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_46.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_46(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_46.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_46(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_46.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_46(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_46.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_admin_status_47(self, admin_status = None):
		'''
			Asserting admin status field
		'''
		status = self.port_page_admin_status_47.get_label_text()
		if not status == admin_status:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	def _verify_port_mode_47(self, mode = None):
		'''
			Asserting port mode field
		'''
		if not self.port_page_port_mode_47.get_label_text() == mode:
			raise AssertionError("PortPage : Port Mode are not matching ")
			
	def _verify_vlan_47(self, vlan = None):
		'''
			Asserting vlan field
		'''
		if not self.port_page_vlan_47.get_label_text() == vlan:
			raise AssertionError("PortPage : vlan are not matching ")
			
	def _verify_poe_47(self, poe = None):
		'''
			Asserting POE field
		'''
		if not self.port_page_poe_47.get_label_text() == poe:
			raise AssertionError("PortPage : POE are not matching ")
	
	def _verify_speed_47(self, speed = None):
		'''
			Asserting speed/duplex field
		'''
		sped = self.port_page_speed_47.get_label_text()
		if not sped == speed:
			raise AssertionError("PortPage : Admin Status are not matching ")
	
	
	def assert_group_12Port_admin_status(self):
		logger.debug("PortPage: Asserting the value of admin field")
		self._verify_admin_status(self.config.config_vars.admin_up)
		self._verify_admin_status_1(self.config.config_vars.admin_up)		
		self._verify_admin_status_2(self.config.config_vars.admin_up)		
		self._verify_admin_status_3(self.config.config_vars.admin_up)		
		self._verify_admin_status_4(self.config.config_vars.admin_up)		
		self._verify_admin_status_5(self.config.config_vars.admin_up)		
		self._verify_admin_status_6(self.config.config_vars.admin_up)		
		self._verify_admin_status_7(self.config.config_vars.admin_up)		
		self._verify_admin_status_8(self.config.config_vars.admin_up)		
		self._verify_admin_status_9(self.config.config_vars.admin_up)		
		self._verify_admin_status_10(self.config.config_vars.admin_up)		
		self._verify_admin_status_11(self.config.config_vars.admin_up)		

	def assert_group_12Port_port_mode(self):
		logger.debug("PortPage: Asserting the value of Port Mode field")
		self._verify_port_mode(self.config.config_vars.portmode_access)
		self._verify_port_mode_1(self.config.config_vars.portmode_access)
		self._verify_port_mode_2(self.config.config_vars.portmode_access)		
		self._verify_port_mode_3(self.config.config_vars.portmode_access)		
		self._verify_port_mode_4(self.config.config_vars.portmode_access)		
		self._verify_port_mode_5(self.config.config_vars.portmode_access)		
		self._verify_port_mode_6(self.config.config_vars.portmode_access)		
		self._verify_port_mode_7(self.config.config_vars.portmode_access)		
		self._verify_port_mode_8(self.config.config_vars.portmode_access)		
		self._verify_port_mode_9(self.config.config_vars.portmode_access)		
		self._verify_port_mode_10(self.config.config_vars.portmode_access)		
		self._verify_port_mode_11(self.config.config_vars.portmode_access)		
		
		
	def assert_group_12Port_vlan(self):
		logger.debug("PortPage: Asserting the value of VLAN field")
		self._verify_vlan(self.config.config_vars.access_vlan1)
		self._verify_vlan_1(self.config.config_vars.access_vlan1)
		self._verify_vlan_2(self.config.config_vars.access_vlan1)		
		self._verify_vlan_3(self.config.config_vars.access_vlan1)		
		self._verify_vlan_4(self.config.config_vars.access_vlan1)		
		self._verify_vlan_5(self.config.config_vars.access_vlan1)		
		self._verify_vlan_6(self.config.config_vars.access_vlan1)		
		self._verify_vlan_7(self.config.config_vars.access_vlan1)		
		self._verify_vlan_8(self.config.config_vars.access_vlan1)		
		self._verify_vlan_9(self.config.config_vars.access_vlan1)
		self._verify_vlan_10(self.config.config_vars.access_vlan1)		
		self._verify_vlan_11(self.config.config_vars.access_vlan1)
		
	def assert_group_12Port_poe(self):
		logger.debug("PortPage: Asserting the value of POE field")
		self._verify_poe(self.config.config_vars.poe1_enabled)
		self._verify_poe_1(self.config.config_vars.poe1_enabled)		
		self._verify_poe_2(self.config.config_vars.poe1_enabled)				
		self._verify_poe_3(self.config.config_vars.poe1_enabled)				
		self._verify_poe_4(self.config.config_vars.poe1_enabled)				
		self._verify_poe_5(self.config.config_vars.poe1_enabled)				
		self._verify_poe_6(self.config.config_vars.poe1_enabled)				
		self._verify_poe_7(self.config.config_vars.poe1_enabled)				
		self._verify_poe_8(self.config.config_vars.poe1_enabled)				
		self._verify_poe_9(self.config.config_vars.poe1_enabled)				
		self._verify_poe_10(self.config.config_vars.poe1_enabled)				
		self._verify_poe_11(self.config.config_vars.poe1_enabled)				
		
	def assert_group_12Port_speed_duplex(self):
		logger.debug("PortPage: Asserting the value of Speed/Duplex field")
		self._verify_speed(self.config.config_vars.speed_auto)
		self._verify_speed_1(self.config.config_vars.speed_auto)		
		self._verify_speed_2(self.config.config_vars.speed_auto)				
		self._verify_speed_3(self.config.config_vars.speed_auto)				
		self._verify_speed_4(self.config.config_vars.speed_auto)				
		self._verify_speed_5(self.config.config_vars.speed_auto)				
		self._verify_speed_6(self.config.config_vars.speed_auto)				
		self._verify_speed_7(self.config.config_vars.speed_auto)				
		self._verify_speed_8(self.config.config_vars.speed_auto)				
		self._verify_speed_9(self.config.config_vars.speed_auto)				
		self._verify_speed_10(self.config.config_vars.speed_auto)				
		self._verify_speed_11(self.config.config_vars.speed_auto)				
	
	def assert_switch_12Port_admin_status(self):
		logger.debug("PortPage: Asserting the value of admin field")
		self._verify_admin_status(self.config.config_vars.admin_up)
		self._verify_admin_status_1(self.config.config_vars.admin_up)		
		self._verify_admin_status_2(self.config.config_vars.admin_up)		
		self._verify_admin_status_3(self.config.config_vars.admin_up)		
		self._verify_admin_status_4(self.config.config_vars.admin_up)		
		self._verify_admin_status_5(self.config.config_vars.admin_up)		
		self._verify_admin_status_6(self.config.config_vars.admin_up)		
		self._verify_admin_status_7(self.config.config_vars.admin_up)		
		self._verify_admin_status_8(self.config.config_vars.admin_up)		
		self._verify_admin_status_9(self.config.config_vars.admin_up)		
		self._verify_admin_status_10(self.config.config_vars.admin_up)		
		self._verify_admin_status_11(self.config.config_vars.admin_up)

	def assert_switch_12Port_port_mode(self):
		logger.debug("PortPage: Asserting the value of Port Mode field")
		self._verify_port_mode(self.config.config_vars.portmode_access)
		self._verify_port_mode_1(self.config.config_vars.portmode_access)
		self._verify_port_mode_2(self.config.config_vars.portmode_access)		
		self._verify_port_mode_3(self.config.config_vars.portmode_access)		
		self._verify_port_mode_4(self.config.config_vars.portmode_access)		
		self._verify_port_mode_5(self.config.config_vars.portmode_access)		
		self._verify_port_mode_6(self.config.config_vars.portmode_access)		
		self._verify_port_mode_7(self.config.config_vars.portmode_access)		
		self._verify_port_mode_8(self.config.config_vars.portmode_access)		
		self._verify_port_mode_9(self.config.config_vars.portmode_access)		
		self._verify_port_mode_10(self.config.config_vars.portmode_access)		
		self._verify_port_mode_11(self.config.config_vars.portmode_access)
		
	def assert_switch_12Port_vlan(self):
		logger.debug("PortPage: Asserting the value of VLAN field")
		self._verify_vlan(self.config.config_vars.access_vlan1)
		self._verify_vlan_1(self.config.config_vars.access_vlan1)
		self._verify_vlan_2(self.config.config_vars.access_vlan1)		
		self._verify_vlan_3(self.config.config_vars.access_vlan1)		
		self._verify_vlan_4(self.config.config_vars.access_vlan1)		
		self._verify_vlan_5(self.config.config_vars.access_vlan1)		
		self._verify_vlan_6(self.config.config_vars.access_vlan1)		
		self._verify_vlan_7(self.config.config_vars.access_vlan1)		
		self._verify_vlan_8(self.config.config_vars.access_vlan1)		
		self._verify_vlan_9(self.config.config_vars.access_vlan1)
		self._verify_vlan_10(self.config.config_vars.access_vlan1)		
		self._verify_vlan_11(self.config.config_vars.access_vlan1)
		
	def assert_switch_12Port_poe(self):
		logger.debug("PortPage: Asserting the value of POE field")
		self._verify_poe(self.config.config_vars.poe1_enabled)
		self._verify_poe_1(self.config.config_vars.poe1_enabled)		
		self._verify_poe_2(self.config.config_vars.poe1_enabled)				
		self._verify_poe_3(self.config.config_vars.poe1_enabled)				
		self._verify_poe_4(self.config.config_vars.poe1_enabled)				
		self._verify_poe_5(self.config.config_vars.poe1_enabled)				
		self._verify_poe_6(self.config.config_vars.poe1_enabled)				
		self._verify_poe_7(self.config.config_vars.poe1_enabled)				
		self._verify_poe_8(self.config.config_vars.poe1_enabled)				
		self._verify_poe_9(self.config.config_vars.poe1_enabled)				
		self._verify_poe_10(self.config.config_vars.poe1_enabled)				
		self._verify_poe_11(self.config.config_vars.poe1_enabled)				
		
	def assert_switch_12Port_speed_duplex(self):
		logger.debug("PortPage: Asserting the value of Speed/Duplex field")
		self._verify_speed(self.config.config_vars.speed_auto)
		self._verify_speed_1(self.config.config_vars.speed_auto)		
		self._verify_speed_2(self.config.config_vars.speed_auto)				
		self._verify_speed_3(self.config.config_vars.speed_auto)				
		self._verify_speed_4(self.config.config_vars.speed_auto)				
		self._verify_speed_5(self.config.config_vars.speed_auto)				
		self._verify_speed_6(self.config.config_vars.speed_auto)				
		self._verify_speed_7(self.config.config_vars.speed_auto)				
		self._verify_speed_8(self.config.config_vars.speed_auto)				
		self._verify_speed_9(self.config.config_vars.speed_auto)				
		self._verify_speed_10(self.config.config_vars.speed_auto)				
		self._verify_speed_11(self.config.config_vars.speed_auto)
	
	def assert_group_24Port_admin_status(self):
		logger.debug("PortPage: Asserting the value of admin field")
		self._verify_admin_status(self.config.config_vars.admin_up)
		self._verify_admin_status_1(self.config.config_vars.admin_up)		
		self._verify_admin_status_2(self.config.config_vars.admin_up)		
		self._verify_admin_status_3(self.config.config_vars.admin_up)		
		self._verify_admin_status_4(self.config.config_vars.admin_up)		
		self._verify_admin_status_5(self.config.config_vars.admin_up)		
		self._verify_admin_status_6(self.config.config_vars.admin_up)		
		self._verify_admin_status_7(self.config.config_vars.admin_up)		
		self._verify_admin_status_8(self.config.config_vars.admin_up)		
		self._verify_admin_status_9(self.config.config_vars.admin_up)		
		self._verify_admin_status_10(self.config.config_vars.admin_up)		
		self._verify_admin_status_11(self.config.config_vars.admin_up)	
		self._verify_admin_status_12(self.config.config_vars.admin_up)		
		self._verify_admin_status_13(self.config.config_vars.admin_up)		
		self._verify_admin_status_14(self.config.config_vars.admin_up)		
		self._verify_admin_status_15(self.config.config_vars.admin_up)		
		self._verify_admin_status_16(self.config.config_vars.admin_up)		
		self._verify_admin_status_17(self.config.config_vars.admin_up)		
		self._verify_admin_status_18(self.config.config_vars.admin_up)		
		self._verify_admin_status_19(self.config.config_vars.admin_up)		
		self._verify_admin_status_20(self.config.config_vars.admin_up)		
		self._verify_admin_status_21(self.config.config_vars.admin_up)
		self._verify_admin_status_22(self.config.config_vars.admin_up)
		self._verify_admin_status_23(self.config.config_vars.admin_up)	

	def assert_group_24Port_port_mode(self):
		logger.debug("PortPage: Asserting the value of Port Mode field")
		self._verify_port_mode(self.config.config_vars.portmode_access)
		self._verify_port_mode_1(self.config.config_vars.portmode_access)
		self._verify_port_mode_2(self.config.config_vars.portmode_access)		
		self._verify_port_mode_3(self.config.config_vars.portmode_access)		
		self._verify_port_mode_4(self.config.config_vars.portmode_access)		
		self._verify_port_mode_5(self.config.config_vars.portmode_access)		
		self._verify_port_mode_6(self.config.config_vars.portmode_access)		
		self._verify_port_mode_7(self.config.config_vars.portmode_access)		
		self._verify_port_mode_8(self.config.config_vars.portmode_access)		
		self._verify_port_mode_9(self.config.config_vars.portmode_access)		
		self._verify_port_mode_10(self.config.config_vars.portmode_access)		
		self._verify_port_mode_11(self.config.config_vars.portmode_access)
		self._verify_port_mode_12(self.config.config_vars.portmode_access)		
		self._verify_port_mode_13(self.config.config_vars.portmode_access)		
		self._verify_port_mode_14(self.config.config_vars.portmode_access)		
		self._verify_port_mode_15(self.config.config_vars.portmode_access)		
		self._verify_port_mode_16(self.config.config_vars.portmode_access)		
		self._verify_port_mode_17(self.config.config_vars.portmode_access)		
		self._verify_port_mode_18(self.config.config_vars.portmode_access)		
		self._verify_port_mode_19(self.config.config_vars.portmode_access)		
		self._verify_port_mode_20(self.config.config_vars.portmode_access)		
		self._verify_port_mode_21(self.config.config_vars.portmode_access)
		self._verify_port_mode_22(self.config.config_vars.portmode_access)		
		self._verify_port_mode_23(self.config.config_vars.portmode_access)
		
	def assert_group_24Port_vlan(self):
		logger.debug("PortPage: Asserting the value of VLAN field")
		self._verify_vlan(self.config.config_vars.access_vlan1)
		self._verify_vlan_1(self.config.config_vars.access_vlan1)
		self._verify_vlan_2(self.config.config_vars.access_vlan1)		
		self._verify_vlan_3(self.config.config_vars.access_vlan1)		
		self._verify_vlan_4(self.config.config_vars.access_vlan1)		
		self._verify_vlan_5(self.config.config_vars.access_vlan1)		
		self._verify_vlan_6(self.config.config_vars.access_vlan1)		
		self._verify_vlan_7(self.config.config_vars.access_vlan1)		
		self._verify_vlan_8(self.config.config_vars.access_vlan1)		
		self._verify_vlan_9(self.config.config_vars.access_vlan1)
		self._verify_vlan_10(self.config.config_vars.access_vlan1)		
		self._verify_vlan_11(self.config.config_vars.access_vlan1)
		self._verify_vlan_12(self.config.config_vars.access_vlan1)		
		self._verify_vlan_13(self.config.config_vars.access_vlan1)		
		self._verify_vlan_14(self.config.config_vars.access_vlan1)		
		self._verify_vlan_15(self.config.config_vars.access_vlan1)		
		self._verify_vlan_16(self.config.config_vars.access_vlan1)		
		self._verify_vlan_17(self.config.config_vars.access_vlan1)		
		self._verify_vlan_18(self.config.config_vars.access_vlan1)		
		self._verify_vlan_19(self.config.config_vars.access_vlan1)
		self._verify_vlan_20(self.config.config_vars.access_vlan1)		
		self._verify_vlan_21(self.config.config_vars.access_vlan1)
		self._verify_vlan_22(self.config.config_vars.access_vlan1)
		self._verify_vlan_23(self.config.config_vars.access_vlan1)
		
	def assert_group_24Port_poe(self):
		logger.debug("PortPage: Asserting the value of POE field")
		self._verify_poe(self.config.config_vars.poe1_enabled)
		self._verify_poe_1(self.config.config_vars.poe1_enabled)		
		self._verify_poe_2(self.config.config_vars.poe1_enabled)				
		self._verify_poe_3(self.config.config_vars.poe1_enabled)				
		self._verify_poe_4(self.config.config_vars.poe1_enabled)				
		self._verify_poe_5(self.config.config_vars.poe1_enabled)				
		self._verify_poe_6(self.config.config_vars.poe1_enabled)				
		self._verify_poe_7(self.config.config_vars.poe1_enabled)				
		self._verify_poe_8(self.config.config_vars.poe1_enabled)				
		self._verify_poe_9(self.config.config_vars.poe1_enabled)				
		self._verify_poe_10(self.config.config_vars.poe1_enabled)				
		self._verify_poe_11(self.config.config_vars.poe1_enabled)	
		self._verify_poe_12(self.config.config_vars.poe1_enabled)				
		self._verify_poe_13(self.config.config_vars.poe1_enabled)				
		self._verify_poe_14(self.config.config_vars.poe1_enabled)				
		self._verify_poe_15(self.config.config_vars.poe1_enabled)				
		self._verify_poe_16(self.config.config_vars.poe1_enabled)				
		self._verify_poe_17(self.config.config_vars.poe1_enabled)				
		self._verify_poe_18(self.config.config_vars.poe1_enabled)				
		self._verify_poe_19(self.config.config_vars.poe1_enabled)				
		self._verify_poe_20(self.config.config_vars.poe1_enabled)				
		self._verify_poe_21(self.config.config_vars.poe1_enabled)
		self._verify_poe_22(self.config.config_vars.poe1_enabled)
		self._verify_poe_23(self.config.config_vars.poe1_enabled)	
		
	def assert_group_24Port_speed_duplex(self):
		logger.debug("PortPage: Asserting the value of Speed/Duplex field")
		self._verify_speed(self.config.config_vars.speed_auto)
		self._verify_speed_1(self.config.config_vars.speed_auto)		
		self._verify_speed_2(self.config.config_vars.speed_auto)				
		self._verify_speed_3(self.config.config_vars.speed_auto)				
		self._verify_speed_4(self.config.config_vars.speed_auto)				
		self._verify_speed_5(self.config.config_vars.speed_auto)				
		self._verify_speed_6(self.config.config_vars.speed_auto)				
		self._verify_speed_7(self.config.config_vars.speed_auto)				
		self._verify_speed_8(self.config.config_vars.speed_auto)				
		self._verify_speed_9(self.config.config_vars.speed_auto)				
		self._verify_speed_10(self.config.config_vars.speed_auto)				
		self._verify_speed_11(self.config.config_vars.speed_auto)	
		self._verify_speed_12(self.config.config_vars.speed_auto)				
		self._verify_speed_13(self.config.config_vars.speed_auto)				
		self._verify_speed_14(self.config.config_vars.speed_auto)				
		self._verify_speed_15(self.config.config_vars.speed_auto)				
		self._verify_speed_16(self.config.config_vars.speed_auto)				
		self._verify_speed_17(self.config.config_vars.speed_auto)				
		self._verify_speed_18(self.config.config_vars.speed_auto)				
		self._verify_speed_19(self.config.config_vars.speed_auto)				
		self._verify_speed_20(self.config.config_vars.speed_auto)				
		self._verify_speed_21(self.config.config_vars.speed_auto)
		self._verify_speed_22(self.config.config_vars.speed_auto)
		self._verify_speed_23(self.config.config_vars.speed_auto)	
	
	def assert_switch_24Port_admin_status(self):
		logger.debug("PortPage: Asserting the value of admin field")
		self._verify_admin_status(self.config.config_vars.admin_up)
		self._verify_admin_status_1(self.config.config_vars.admin_up)		
		self._verify_admin_status_2(self.config.config_vars.admin_up)		
		self._verify_admin_status_3(self.config.config_vars.admin_up)		
		self._verify_admin_status_4(self.config.config_vars.admin_up)		
		self._verify_admin_status_5(self.config.config_vars.admin_up)		
		self._verify_admin_status_6(self.config.config_vars.admin_up)		
		self._verify_admin_status_7(self.config.config_vars.admin_up)		
		self._verify_admin_status_8(self.config.config_vars.admin_up)		
		self._verify_admin_status_9(self.config.config_vars.admin_up)		
		self._verify_admin_status_10(self.config.config_vars.admin_up)		
		self._verify_admin_status_11(self.config.config_vars.admin_up)	
		self._verify_admin_status_12(self.config.config_vars.admin_up)		
		self._verify_admin_status_13(self.config.config_vars.admin_up)		
		self._verify_admin_status_14(self.config.config_vars.admin_up)		
		self._verify_admin_status_15(self.config.config_vars.admin_up)		
		self._verify_admin_status_16(self.config.config_vars.admin_up)		
		self._verify_admin_status_17(self.config.config_vars.admin_up)		
		self._verify_admin_status_18(self.config.config_vars.admin_up)		
		self._verify_admin_status_19(self.config.config_vars.admin_up)		
		self._verify_admin_status_20(self.config.config_vars.admin_up)		
		self._verify_admin_status_21(self.config.config_vars.admin_up)
		self._verify_admin_status_22(self.config.config_vars.admin_up)
		self._verify_admin_status_23(self.config.config_vars.admin_up)

	def assert_switch_24Port_port_mode(self):
		logger.debug("PortPage: Asserting the value of Port Mode field")
		self._verify_port_mode(self.config.config_vars.portmode_access)
		self._verify_port_mode_1(self.config.config_vars.portmode_access)
		self._verify_port_mode_2(self.config.config_vars.portmode_access)		
		self._verify_port_mode_3(self.config.config_vars.portmode_access)		
		self._verify_port_mode_4(self.config.config_vars.portmode_access)		
		self._verify_port_mode_5(self.config.config_vars.portmode_access)		
		self._verify_port_mode_6(self.config.config_vars.portmode_access)		
		self._verify_port_mode_7(self.config.config_vars.portmode_access)		
		self._verify_port_mode_8(self.config.config_vars.portmode_access)		
		self._verify_port_mode_9(self.config.config_vars.portmode_access)		
		self._verify_port_mode_10(self.config.config_vars.portmode_access)		
		self._verify_port_mode_11(self.config.config_vars.portmode_access)
		self._verify_port_mode_12(self.config.config_vars.portmode_access)		
		self._verify_port_mode_13(self.config.config_vars.portmode_access)		
		self._verify_port_mode_14(self.config.config_vars.portmode_access)		
		self._verify_port_mode_15(self.config.config_vars.portmode_access)		
		self._verify_port_mode_16(self.config.config_vars.portmode_access)		
		self._verify_port_mode_17(self.config.config_vars.portmode_access)		
		self._verify_port_mode_18(self.config.config_vars.portmode_access)		
		self._verify_port_mode_19(self.config.config_vars.portmode_access)		
		self._verify_port_mode_20(self.config.config_vars.portmode_access)		
		self._verify_port_mode_21(self.config.config_vars.portmode_access)
		self._verify_port_mode_22(self.config.config_vars.portmode_access)		
		self._verify_port_mode_23(self.config.config_vars.portmode_access)
		
	def assert_switch_24Port_vlan(self):
		logger.debug("PortPage: Asserting the value of VLAN field")
		self._verify_vlan(self.config.config_vars.access_vlan1)
		self._verify_vlan_1(self.config.config_vars.access_vlan1)
		self._verify_vlan_2(self.config.config_vars.access_vlan1)		
		self._verify_vlan_3(self.config.config_vars.access_vlan1)		
		self._verify_vlan_4(self.config.config_vars.access_vlan1)		
		self._verify_vlan_5(self.config.config_vars.access_vlan1)		
		self._verify_vlan_6(self.config.config_vars.access_vlan1)		
		self._verify_vlan_7(self.config.config_vars.access_vlan1)		
		self._verify_vlan_8(self.config.config_vars.access_vlan1)		
		self._verify_vlan_9(self.config.config_vars.access_vlan1)
		self._verify_vlan_10(self.config.config_vars.access_vlan1)		
		self._verify_vlan_11(self.config.config_vars.access_vlan1)
		self._verify_vlan_12(self.config.config_vars.access_vlan1)		
		self._verify_vlan_13(self.config.config_vars.access_vlan1)		
		self._verify_vlan_14(self.config.config_vars.access_vlan1)		
		self._verify_vlan_15(self.config.config_vars.access_vlan1)		
		self._verify_vlan_16(self.config.config_vars.access_vlan1)		
		self._verify_vlan_17(self.config.config_vars.access_vlan1)		
		self._verify_vlan_18(self.config.config_vars.access_vlan1)		
		self._verify_vlan_19(self.config.config_vars.access_vlan1)
		self._verify_vlan_20(self.config.config_vars.access_vlan1)		
		self._verify_vlan_21(self.config.config_vars.access_vlan1)
		self._verify_vlan_22(self.config.config_vars.access_vlan1)
		self._verify_vlan_23(self.config.config_vars.access_vlan1)
		
	def assert_switch_24Port_poe(self):
		logger.debug("PortPage: Asserting the value of POE field")
		self._verify_poe(self.config.config_vars.poe1_enabled)
		self._verify_poe_1(self.config.config_vars.poe1_enabled)		
		self._verify_poe_2(self.config.config_vars.poe1_enabled)				
		self._verify_poe_3(self.config.config_vars.poe1_enabled)				
		self._verify_poe_4(self.config.config_vars.poe1_enabled)				
		self._verify_poe_5(self.config.config_vars.poe1_enabled)				
		self._verify_poe_6(self.config.config_vars.poe1_enabled)				
		self._verify_poe_7(self.config.config_vars.poe1_enabled)				
		self._verify_poe_8(self.config.config_vars.poe1_enabled)				
		self._verify_poe_9(self.config.config_vars.poe1_enabled)				
		self._verify_poe_10(self.config.config_vars.poe1_enabled)				
		self._verify_poe_11(self.config.config_vars.poe1_enabled)	
		self._verify_poe_12(self.config.config_vars.poe1_enabled)				
		self._verify_poe_13(self.config.config_vars.poe1_enabled)				
		self._verify_poe_14(self.config.config_vars.poe1_enabled)				
		self._verify_poe_15(self.config.config_vars.poe1_enabled)				
		self._verify_poe_16(self.config.config_vars.poe1_enabled)				
		self._verify_poe_17(self.config.config_vars.poe1_enabled)				
		self._verify_poe_18(self.config.config_vars.poe1_enabled)				
		self._verify_poe_19(self.config.config_vars.poe1_enabled)				
		self._verify_poe_20(self.config.config_vars.poe1_enabled)				
		self._verify_poe_21(self.config.config_vars.poe1_enabled)
		self._verify_poe_22(self.config.config_vars.poe1_enabled)
		self._verify_poe_23(self.config.config_vars.poe1_enabled)
		
	def assert_switch_24Port_speed_duplex(self):
		logger.debug("PortPage: Asserting the value of Speed/Duplex field")
		self._verify_speed(self.config.config_vars.speed_auto)
		self._verify_speed_1(self.config.config_vars.speed_auto)		
		self._verify_speed_2(self.config.config_vars.speed_auto)				
		self._verify_speed_3(self.config.config_vars.speed_auto)				
		self._verify_speed_4(self.config.config_vars.speed_auto)				
		self._verify_speed_5(self.config.config_vars.speed_auto)				
		self._verify_speed_6(self.config.config_vars.speed_auto)				
		self._verify_speed_7(self.config.config_vars.speed_auto)				
		self._verify_speed_8(self.config.config_vars.speed_auto)				
		self._verify_speed_9(self.config.config_vars.speed_auto)				
		self._verify_speed_10(self.config.config_vars.speed_auto)				
		self._verify_speed_11(self.config.config_vars.speed_auto)	
		self._verify_speed_12(self.config.config_vars.speed_auto)				
		self._verify_speed_13(self.config.config_vars.speed_auto)				
		self._verify_speed_14(self.config.config_vars.speed_auto)				
		self._verify_speed_15(self.config.config_vars.speed_auto)				
		self._verify_speed_16(self.config.config_vars.speed_auto)				
		self._verify_speed_17(self.config.config_vars.speed_auto)				
		self._verify_speed_18(self.config.config_vars.speed_auto)				
		self._verify_speed_19(self.config.config_vars.speed_auto)				
		self._verify_speed_20(self.config.config_vars.speed_auto)				
		self._verify_speed_21(self.config.config_vars.speed_auto)
		self._verify_speed_22(self.config.config_vars.speed_auto)
		self._verify_speed_23(self.config.config_vars.speed_auto)
	
	
	
	
	
	
	
	def assert_group_48Port_admin_status(self):
		logger.debug("PortPage: Asserting the value of admin field")
		self._verify_admin_status(self.config.config_vars.admin_up)
		self._verify_admin_status_1(self.config.config_vars.admin_up)		
		self._verify_admin_status_2(self.config.config_vars.admin_up)		
		self._verify_admin_status_3(self.config.config_vars.admin_up)		
		self._verify_admin_status_4(self.config.config_vars.admin_up)		
		self._verify_admin_status_5(self.config.config_vars.admin_up)		
		self._verify_admin_status_6(self.config.config_vars.admin_up)		
		self._verify_admin_status_7(self.config.config_vars.admin_up)		
		self._verify_admin_status_8(self.config.config_vars.admin_up)		
		self._verify_admin_status_9(self.config.config_vars.admin_up)		
		self._verify_admin_status_10(self.config.config_vars.admin_up)		
		self._verify_admin_status_11(self.config.config_vars.admin_up)	
		self._verify_admin_status_12(self.config.config_vars.admin_up)		
		self._verify_admin_status_13(self.config.config_vars.admin_up)		
		self._verify_admin_status_14(self.config.config_vars.admin_up)		
		self._verify_admin_status_15(self.config.config_vars.admin_up)		
		self._verify_admin_status_16(self.config.config_vars.admin_up)		
		self._verify_admin_status_17(self.config.config_vars.admin_up)		
		self._verify_admin_status_18(self.config.config_vars.admin_up)		
		self._verify_admin_status_19(self.config.config_vars.admin_up)		
		self._verify_admin_status_20(self.config.config_vars.admin_up)		
		self._verify_admin_status_21(self.config.config_vars.admin_up)
		self._verify_admin_status_22(self.config.config_vars.admin_up)
		self._verify_admin_status_23(self.config.config_vars.admin_up)
		self._verify_admin_status_24(self.config.config_vars.admin_up)
		self._verify_admin_status_25(self.config.config_vars.admin_up)				
		self._verify_admin_status_26(self.config.config_vars.admin_up)				
		self._verify_admin_status_27(self.config.config_vars.admin_up)				
		self._verify_admin_status_28(self.config.config_vars.admin_up)				
		self._verify_admin_status_29(self.config.config_vars.admin_up)				
		self._verify_admin_status_30(self.config.config_vars.admin_up)				
		self._verify_admin_status_31(self.config.config_vars.admin_up)				
		self._verify_admin_status_32(self.config.config_vars.admin_up)				
		self._verify_admin_status_33(self.config.config_vars.admin_up)				
		self._verify_admin_status_34(self.config.config_vars.admin_up)				
		self._verify_admin_status_35(self.config.config_vars.admin_up)				
		self._verify_admin_status_36(self.config.config_vars.admin_up)				
		self._verify_admin_status_37(self.config.config_vars.admin_up)				
		self._verify_admin_status_38(self.config.config_vars.admin_up)				
		self._verify_admin_status_39(self.config.config_vars.admin_up)				
		self._verify_admin_status_40(self.config.config_vars.admin_up)				
		self._verify_admin_status_41(self.config.config_vars.admin_up)				
		self._verify_admin_status_42(self.config.config_vars.admin_up)				
		self._verify_admin_status_43(self.config.config_vars.admin_up)				
		self._verify_admin_status_44(self.config.config_vars.admin_up)				
		self._verify_admin_status_45(self.config.config_vars.admin_up)				
		self._verify_admin_status_46(self.config.config_vars.admin_up)				
		self._verify_admin_status_47(self.config.config_vars.admin_up)		
		
		
		

	def assert_group_48Port_port_mode(self):
		logger.debug("PortPage: Asserting the value of Port Mode field")
		self._verify_port_mode(self.config.config_vars.portmode_access)
		self._verify_port_mode_1(self.config.config_vars.portmode_access)
		self._verify_port_mode_2(self.config.config_vars.portmode_access)		
		self._verify_port_mode_3(self.config.config_vars.portmode_access)		
		self._verify_port_mode_4(self.config.config_vars.portmode_access)		
		self._verify_port_mode_5(self.config.config_vars.portmode_access)		
		self._verify_port_mode_6(self.config.config_vars.portmode_access)		
		self._verify_port_mode_7(self.config.config_vars.portmode_access)		
		self._verify_port_mode_8(self.config.config_vars.portmode_access)		
		self._verify_port_mode_9(self.config.config_vars.portmode_access)		
		self._verify_port_mode_10(self.config.config_vars.portmode_access)		
		self._verify_port_mode_11(self.config.config_vars.portmode_access)
		self._verify_port_mode_12(self.config.config_vars.portmode_access)		
		self._verify_port_mode_13(self.config.config_vars.portmode_access)		
		self._verify_port_mode_14(self.config.config_vars.portmode_access)		
		self._verify_port_mode_15(self.config.config_vars.portmode_access)		
		self._verify_port_mode_16(self.config.config_vars.portmode_access)		
		self._verify_port_mode_17(self.config.config_vars.portmode_access)		
		self._verify_port_mode_18(self.config.config_vars.portmode_access)		
		self._verify_port_mode_19(self.config.config_vars.portmode_access)		
		self._verify_port_mode_20(self.config.config_vars.portmode_access)		
		self._verify_port_mode_21(self.config.config_vars.portmode_access)
		self._verify_port_mode_22(self.config.config_vars.portmode_access)		
		self._verify_port_mode_23(self.config.config_vars.portmode_access)
		self._verify_port_mode_24(self.config.config_vars.portmode_access)
		self._verify_port_mode_25(self.config.config_vars.portmode_access)
		self._verify_port_mode_26(self.config.config_vars.portmode_access)		
		self._verify_port_mode_27(self.config.config_vars.portmode_access)		
		self._verify_port_mode_28(self.config.config_vars.portmode_access)		
		self._verify_port_mode_29(self.config.config_vars.portmode_access)		
		self._verify_port_mode_30(self.config.config_vars.portmode_access)		
		self._verify_port_mode_31(self.config.config_vars.portmode_access)		
		self._verify_port_mode_32(self.config.config_vars.portmode_access)		
		self._verify_port_mode_33(self.config.config_vars.portmode_access)		
		self._verify_port_mode_34(self.config.config_vars.portmode_access)		
		self._verify_port_mode_35(self.config.config_vars.portmode_access)		
		self._verify_port_mode_36(self.config.config_vars.portmode_access)		
		self._verify_port_mode_37(self.config.config_vars.portmode_access)		
		self._verify_port_mode_38(self.config.config_vars.portmode_access)		
		self._verify_port_mode_39(self.config.config_vars.portmode_access)		
		self._verify_port_mode_40(self.config.config_vars.portmode_access)
		self._verify_port_mode_41(self.config.config_vars.portmode_access)
		self._verify_port_mode_42(self.config.config_vars.portmode_access)
		self._verify_port_mode_43(self.config.config_vars.portmode_access)
		self._verify_port_mode_44(self.config.config_vars.portmode_access)
		self._verify_port_mode_45(self.config.config_vars.portmode_access)
		self._verify_port_mode_46(self.config.config_vars.portmode_access)
		self._verify_port_mode_47(self.config.config_vars.portmode_access)		
		
	def assert_group_48Port_vlan(self):
		logger.debug("PortPage: Asserting the value of VLAN field")
		self._verify_vlan(self.config.config_vars.access_vlan1)
		self._verify_vlan_1(self.config.config_vars.access_vlan1)
		self._verify_vlan_2(self.config.config_vars.access_vlan1)		
		self._verify_vlan_3(self.config.config_vars.access_vlan1)		
		self._verify_vlan_4(self.config.config_vars.access_vlan1)		
		self._verify_vlan_5(self.config.config_vars.access_vlan1)		
		self._verify_vlan_6(self.config.config_vars.access_vlan1)		
		self._verify_vlan_7(self.config.config_vars.access_vlan1)		
		self._verify_vlan_8(self.config.config_vars.access_vlan1)		
		self._verify_vlan_9(self.config.config_vars.access_vlan1)
		self._verify_vlan_10(self.config.config_vars.access_vlan1)		
		self._verify_vlan_11(self.config.config_vars.access_vlan1)
		self._verify_vlan_12(self.config.config_vars.access_vlan1)		
		self._verify_vlan_13(self.config.config_vars.access_vlan1)		
		self._verify_vlan_14(self.config.config_vars.access_vlan1)		
		self._verify_vlan_15(self.config.config_vars.access_vlan1)		
		self._verify_vlan_16(self.config.config_vars.access_vlan1)		
		self._verify_vlan_17(self.config.config_vars.access_vlan1)		
		self._verify_vlan_18(self.config.config_vars.access_vlan1)		
		self._verify_vlan_19(self.config.config_vars.access_vlan1)
		self._verify_vlan_20(self.config.config_vars.access_vlan1)		
		self._verify_vlan_21(self.config.config_vars.access_vlan1)
		self._verify_vlan_22(self.config.config_vars.access_vlan1)
		self._verify_vlan_23(self.config.config_vars.access_vlan1)
		self._verify_vlan_24(self.config.config_vars.access_vlan1)		
		self._verify_vlan_25(self.config.config_vars.access_vlan1)		
		self._verify_vlan_26(self.config.config_vars.access_vlan1)		
		self._verify_vlan_27(self.config.config_vars.access_vlan1)		
		self._verify_vlan_28(self.config.config_vars.access_vlan1)		
		self._verify_vlan_29(self.config.config_vars.access_vlan1)		
		self._verify_vlan_30(self.config.config_vars.access_vlan1)		
		self._verify_vlan_31(self.config.config_vars.access_vlan1)		
		self._verify_vlan_32(self.config.config_vars.access_vlan1)		
		self._verify_vlan_33(self.config.config_vars.access_vlan1)		
		self._verify_vlan_34(self.config.config_vars.access_vlan1)		
		self._verify_vlan_35(self.config.config_vars.access_vlan1)		
		self._verify_vlan_36(self.config.config_vars.access_vlan1)		
		self._verify_vlan_37(self.config.config_vars.access_vlan1)		
		self._verify_vlan_38(self.config.config_vars.access_vlan1)		
		self._verify_vlan_39(self.config.config_vars.access_vlan1)		
		self._verify_vlan_40(self.config.config_vars.access_vlan1)		
		self._verify_vlan_41(self.config.config_vars.access_vlan1)		
		self._verify_vlan_42(self.config.config_vars.access_vlan1)		
		self._verify_vlan_43(self.config.config_vars.access_vlan1)		
		self._verify_vlan_44(self.config.config_vars.access_vlan1)		
		self._verify_vlan_45(self.config.config_vars.access_vlan1)		
		self._verify_vlan_46(self.config.config_vars.access_vlan1)		
		self._verify_vlan_47(self.config.config_vars.access_vlan1)		
		
		
	def assert_group_48Port_poe(self):
		logger.debug("PortPage: Asserting the value of POE field")
		self._verify_poe(self.config.config_vars.poe1_enabled)
		self._verify_poe_1(self.config.config_vars.poe1_enabled)		
		self._verify_poe_2(self.config.config_vars.poe1_enabled)				
		self._verify_poe_3(self.config.config_vars.poe1_enabled)				
		self._verify_poe_4(self.config.config_vars.poe1_enabled)				
		self._verify_poe_5(self.config.config_vars.poe1_enabled)				
		self._verify_poe_6(self.config.config_vars.poe1_enabled)				
		self._verify_poe_7(self.config.config_vars.poe1_enabled)				
		self._verify_poe_8(self.config.config_vars.poe1_enabled)				
		self._verify_poe_9(self.config.config_vars.poe1_enabled)				
		self._verify_poe_10(self.config.config_vars.poe1_enabled)				
		self._verify_poe_11(self.config.config_vars.poe1_enabled)	
		self._verify_poe_12(self.config.config_vars.poe1_enabled)				
		self._verify_poe_13(self.config.config_vars.poe1_enabled)				
		self._verify_poe_14(self.config.config_vars.poe1_enabled)				
		self._verify_poe_15(self.config.config_vars.poe1_enabled)				
		self._verify_poe_16(self.config.config_vars.poe1_enabled)				
		self._verify_poe_17(self.config.config_vars.poe1_enabled)				
		self._verify_poe_18(self.config.config_vars.poe1_enabled)				
		self._verify_poe_19(self.config.config_vars.poe1_enabled)				
		self._verify_poe_20(self.config.config_vars.poe1_enabled)				
		self._verify_poe_21(self.config.config_vars.poe1_enabled)
		self._verify_poe_22(self.config.config_vars.poe1_enabled)
		self._verify_poe_23(self.config.config_vars.poe1_enabled)
		self._verify_poe_24(self.config.config_vars.poe1_enabled)
		self._verify_poe_25(self.config.config_vars.poe1_enabled)
		self._verify_poe_26(self.config.config_vars.poe1_enabled)
		self._verify_poe_27(self.config.config_vars.poe1_enabled)
		self._verify_poe_28(self.config.config_vars.poe1_enabled)
		self._verify_poe_29(self.config.config_vars.poe1_enabled)
		self._verify_poe_30(self.config.config_vars.poe1_enabled)
		self._verify_poe_31(self.config.config_vars.poe1_enabled)
		self._verify_poe_32(self.config.config_vars.poe1_enabled)
		self._verify_poe_33(self.config.config_vars.poe1_enabled)
		self._verify_poe_34(self.config.config_vars.poe1_enabled)
		self._verify_poe_35(self.config.config_vars.poe1_enabled)
		self._verify_poe_36(self.config.config_vars.poe1_enabled)
		self._verify_poe_37(self.config.config_vars.poe1_enabled)
		self._verify_poe_38(self.config.config_vars.poe1_enabled)
		self._verify_poe_39(self.config.config_vars.poe1_enabled)
		self._verify_poe_40(self.config.config_vars.poe1_enabled)
		self._verify_poe_41(self.config.config_vars.poe1_enabled)
		self._verify_poe_42(self.config.config_vars.poe1_enabled)
		self._verify_poe_43(self.config.config_vars.poe1_enabled)
		self._verify_poe_44(self.config.config_vars.poe1_enabled)
		self._verify_poe_45(self.config.config_vars.poe1_enabled)
		self._verify_poe_46(self.config.config_vars.poe1_enabled)		
		self._verify_poe_47(self.config.config_vars.poe1_enabled)		
		
	def assert_group_48Port_speed_duplex(self):
		logger.debug("PortPage: Asserting the value of Speed/Duplex field")
		self._verify_speed(self.config.config_vars.speed_auto)
		self._verify_speed_1(self.config.config_vars.speed_auto)		
		self._verify_speed_2(self.config.config_vars.speed_auto)				
		self._verify_speed_3(self.config.config_vars.speed_auto)				
		self._verify_speed_4(self.config.config_vars.speed_auto)				
		self._verify_speed_5(self.config.config_vars.speed_auto)				
		self._verify_speed_6(self.config.config_vars.speed_auto)				
		self._verify_speed_7(self.config.config_vars.speed_auto)				
		self._verify_speed_8(self.config.config_vars.speed_auto)				
		self._verify_speed_9(self.config.config_vars.speed_auto)				
		self._verify_speed_10(self.config.config_vars.speed_auto)				
		self._verify_speed_11(self.config.config_vars.speed_auto)	
		self._verify_speed_12(self.config.config_vars.speed_auto)				
		self._verify_speed_13(self.config.config_vars.speed_auto)				
		self._verify_speed_14(self.config.config_vars.speed_auto)				
		self._verify_speed_15(self.config.config_vars.speed_auto)				
		self._verify_speed_16(self.config.config_vars.speed_auto)				
		self._verify_speed_17(self.config.config_vars.speed_auto)				
		self._verify_speed_18(self.config.config_vars.speed_auto)				
		self._verify_speed_19(self.config.config_vars.speed_auto)				
		self._verify_speed_20(self.config.config_vars.speed_auto)				
		self._verify_speed_21(self.config.config_vars.speed_auto)
		self._verify_speed_22(self.config.config_vars.speed_auto)
		self._verify_speed_23(self.config.config_vars.speed_auto)
		self._verify_speed_24(self.config.config_vars.speed_auto)
		self._verify_speed_25(self.config.config_vars.speed_auto)
		self._verify_speed_26(self.config.config_vars.speed_auto)
		self._verify_speed_27(self.config.config_vars.speed_auto)
		self._verify_speed_28(self.config.config_vars.speed_auto)
		self._verify_speed_29(self.config.config_vars.speed_auto)
		self._verify_speed_30(self.config.config_vars.speed_auto)
		self._verify_speed_31(self.config.config_vars.speed_auto)
		self._verify_speed_32(self.config.config_vars.speed_auto)
		self._verify_speed_33(self.config.config_vars.speed_auto)
		self._verify_speed_34(self.config.config_vars.speed_auto)
		self._verify_speed_35(self.config.config_vars.speed_auto)
		self._verify_speed_36(self.config.config_vars.speed_auto)
		self._verify_speed_37(self.config.config_vars.speed_auto)
		self._verify_speed_38(self.config.config_vars.speed_auto)
		self._verify_speed_39(self.config.config_vars.speed_auto)
		self._verify_speed_40(self.config.config_vars.speed_auto)
		self._verify_speed_41(self.config.config_vars.speed_auto)
		self._verify_speed_42(self.config.config_vars.speed_auto)
		self._verify_speed_43(self.config.config_vars.speed_auto)
		self._verify_speed_44(self.config.config_vars.speed_auto)
		self._verify_speed_45(self.config.config_vars.speed_auto)
		self._verify_speed_46(self.config.config_vars.speed_auto)
		self._verify_speed_47(self.config.config_vars.speed_auto)		
	
	def assert_switch_48Port_admin_status(self):
		logger.debug("PortPage: Asserting the value of admin field")
		self._verify_admin_status(self.config.config_vars.admin_up)
		self._verify_admin_status_1(self.config.config_vars.admin_up)		
		self._verify_admin_status_2(self.config.config_vars.admin_up)		
		self._verify_admin_status_3(self.config.config_vars.admin_up)		
		self._verify_admin_status_4(self.config.config_vars.admin_up)		
		self._verify_admin_status_5(self.config.config_vars.admin_up)		
		self._verify_admin_status_6(self.config.config_vars.admin_up)		
		self._verify_admin_status_7(self.config.config_vars.admin_up)		
		self._verify_admin_status_8(self.config.config_vars.admin_up)		
		self._verify_admin_status_9(self.config.config_vars.admin_up)		
		self._verify_admin_status_10(self.config.config_vars.admin_up)		
		self._verify_admin_status_11(self.config.config_vars.admin_up)	
		self._verify_admin_status_12(self.config.config_vars.admin_up)		
		self._verify_admin_status_13(self.config.config_vars.admin_up)		
		self._verify_admin_status_14(self.config.config_vars.admin_up)		
		self._verify_admin_status_15(self.config.config_vars.admin_up)		
		self._verify_admin_status_16(self.config.config_vars.admin_up)		
		self._verify_admin_status_17(self.config.config_vars.admin_up)		
		self._verify_admin_status_18(self.config.config_vars.admin_up)		
		self._verify_admin_status_19(self.config.config_vars.admin_up)		
		self._verify_admin_status_20(self.config.config_vars.admin_up)		
		self._verify_admin_status_21(self.config.config_vars.admin_up)
		self._verify_admin_status_22(self.config.config_vars.admin_up)
		self._verify_admin_status_23(self.config.config_vars.admin_up)
		self._verify_admin_status_24(self.config.config_vars.admin_up)
		self._verify_admin_status_25(self.config.config_vars.admin_up)				
		self._verify_admin_status_26(self.config.config_vars.admin_up)				
		self._verify_admin_status_27(self.config.config_vars.admin_up)				
		self._verify_admin_status_28(self.config.config_vars.admin_up)				
		self._verify_admin_status_29(self.config.config_vars.admin_up)				
		self._verify_admin_status_30(self.config.config_vars.admin_up)				
		self._verify_admin_status_31(self.config.config_vars.admin_up)				
		self._verify_admin_status_32(self.config.config_vars.admin_up)				
		self._verify_admin_status_33(self.config.config_vars.admin_up)				
		self._verify_admin_status_34(self.config.config_vars.admin_up)				
		self._verify_admin_status_35(self.config.config_vars.admin_up)				
		self._verify_admin_status_36(self.config.config_vars.admin_up)				
		self._verify_admin_status_37(self.config.config_vars.admin_up)				
		self._verify_admin_status_38(self.config.config_vars.admin_up)				
		self._verify_admin_status_39(self.config.config_vars.admin_up)				
		self._verify_admin_status_40(self.config.config_vars.admin_up)				
		self._verify_admin_status_41(self.config.config_vars.admin_up)				
		self._verify_admin_status_42(self.config.config_vars.admin_up)				
		self._verify_admin_status_43(self.config.config_vars.admin_up)				
		self._verify_admin_status_44(self.config.config_vars.admin_up)				
		self._verify_admin_status_45(self.config.config_vars.admin_up)				
		self._verify_admin_status_46(self.config.config_vars.admin_up)				
		self._verify_admin_status_47(self.config.config_vars.admin_up)


	def assert_switch_48Port_port_mode(self):
		logger.debug("PortPage: Asserting the value of Port Mode field")
		self._verify_port_mode(self.config.config_vars.portmode_access)
		self._verify_port_mode_1(self.config.config_vars.portmode_access)
		self._verify_port_mode_2(self.config.config_vars.portmode_access)		
		self._verify_port_mode_3(self.config.config_vars.portmode_access)		
		self._verify_port_mode_4(self.config.config_vars.portmode_access)		
		self._verify_port_mode_5(self.config.config_vars.portmode_access)		
		self._verify_port_mode_6(self.config.config_vars.portmode_access)		
		self._verify_port_mode_7(self.config.config_vars.portmode_access)		
		self._verify_port_mode_8(self.config.config_vars.portmode_access)		
		self._verify_port_mode_9(self.config.config_vars.portmode_access)		
		self._verify_port_mode_10(self.config.config_vars.portmode_access)		
		self._verify_port_mode_11(self.config.config_vars.portmode_access)
		self._verify_port_mode_12(self.config.config_vars.portmode_access)		
		self._verify_port_mode_13(self.config.config_vars.portmode_access)		
		self._verify_port_mode_14(self.config.config_vars.portmode_access)		
		self._verify_port_mode_15(self.config.config_vars.portmode_access)		
		self._verify_port_mode_16(self.config.config_vars.portmode_access)		
		self._verify_port_mode_17(self.config.config_vars.portmode_access)		
		self._verify_port_mode_18(self.config.config_vars.portmode_access)		
		self._verify_port_mode_19(self.config.config_vars.portmode_access)		
		self._verify_port_mode_20(self.config.config_vars.portmode_access)		
		self._verify_port_mode_21(self.config.config_vars.portmode_access)
		self._verify_port_mode_22(self.config.config_vars.portmode_access)		
		self._verify_port_mode_23(self.config.config_vars.portmode_access)
		self._verify_port_mode_24(self.config.config_vars.portmode_access)
		self._verify_port_mode_25(self.config.config_vars.portmode_access)
		self._verify_port_mode_26(self.config.config_vars.portmode_access)		
		self._verify_port_mode_27(self.config.config_vars.portmode_access)		
		self._verify_port_mode_28(self.config.config_vars.portmode_access)		
		self._verify_port_mode_29(self.config.config_vars.portmode_access)		
		self._verify_port_mode_30(self.config.config_vars.portmode_access)		
		self._verify_port_mode_31(self.config.config_vars.portmode_access)		
		self._verify_port_mode_32(self.config.config_vars.portmode_access)		
		self._verify_port_mode_33(self.config.config_vars.portmode_access)		
		self._verify_port_mode_34(self.config.config_vars.portmode_access)		
		self._verify_port_mode_35(self.config.config_vars.portmode_access)		
		self._verify_port_mode_36(self.config.config_vars.portmode_access)		
		self._verify_port_mode_37(self.config.config_vars.portmode_access)		
		self._verify_port_mode_38(self.config.config_vars.portmode_access)		
		self._verify_port_mode_39(self.config.config_vars.portmode_access)		
		self._verify_port_mode_40(self.config.config_vars.portmode_access)
		self._verify_port_mode_41(self.config.config_vars.portmode_access)
		self._verify_port_mode_42(self.config.config_vars.portmode_access)
		self._verify_port_mode_43(self.config.config_vars.portmode_access)
		self._verify_port_mode_44(self.config.config_vars.portmode_access)
		self._verify_port_mode_45(self.config.config_vars.portmode_access)
		self._verify_port_mode_46(self.config.config_vars.portmode_access)
		self._verify_port_mode_47(self.config.config_vars.portmode_access)
		
	def assert_switch_48Port_vlan(self):
		logger.debug("PortPage: Asserting the value of VLAN field")
		self._verify_vlan(self.config.config_vars.access_vlan1)
		self._verify_vlan_1(self.config.config_vars.access_vlan1)
		self._verify_vlan_2(self.config.config_vars.access_vlan1)		
		self._verify_vlan_3(self.config.config_vars.access_vlan1)		
		self._verify_vlan_4(self.config.config_vars.access_vlan1)		
		self._verify_vlan_5(self.config.config_vars.access_vlan1)		
		self._verify_vlan_6(self.config.config_vars.access_vlan1)		
		self._verify_vlan_7(self.config.config_vars.access_vlan1)		
		self._verify_vlan_8(self.config.config_vars.access_vlan1)		
		self._verify_vlan_9(self.config.config_vars.access_vlan1)
		self._verify_vlan_10(self.config.config_vars.access_vlan1)		
		self._verify_vlan_11(self.config.config_vars.access_vlan1)
		self._verify_vlan_12(self.config.config_vars.access_vlan1)		
		self._verify_vlan_13(self.config.config_vars.access_vlan1)		
		self._verify_vlan_14(self.config.config_vars.access_vlan1)		
		self._verify_vlan_15(self.config.config_vars.access_vlan1)		
		self._verify_vlan_16(self.config.config_vars.access_vlan1)		
		self._verify_vlan_17(self.config.config_vars.access_vlan1)		
		self._verify_vlan_18(self.config.config_vars.access_vlan1)		
		self._verify_vlan_19(self.config.config_vars.access_vlan1)
		self._verify_vlan_20(self.config.config_vars.access_vlan1)		
		self._verify_vlan_21(self.config.config_vars.access_vlan1)
		self._verify_vlan_22(self.config.config_vars.access_vlan1)
		self._verify_vlan_23(self.config.config_vars.access_vlan1)
		self._verify_vlan_24(self.config.config_vars.access_vlan1)		
		self._verify_vlan_25(self.config.config_vars.access_vlan1)		
		self._verify_vlan_26(self.config.config_vars.access_vlan1)		
		self._verify_vlan_27(self.config.config_vars.access_vlan1)		
		self._verify_vlan_28(self.config.config_vars.access_vlan1)		
		self._verify_vlan_29(self.config.config_vars.access_vlan1)		
		self._verify_vlan_30(self.config.config_vars.access_vlan1)		
		self._verify_vlan_31(self.config.config_vars.access_vlan1)		
		self._verify_vlan_32(self.config.config_vars.access_vlan1)		
		self._verify_vlan_33(self.config.config_vars.access_vlan1)		
		self._verify_vlan_34(self.config.config_vars.access_vlan1)		
		self._verify_vlan_35(self.config.config_vars.access_vlan1)		
		self._verify_vlan_36(self.config.config_vars.access_vlan1)		
		self._verify_vlan_37(self.config.config_vars.access_vlan1)		
		self._verify_vlan_38(self.config.config_vars.access_vlan1)		
		self._verify_vlan_39(self.config.config_vars.access_vlan1)		
		self._verify_vlan_40(self.config.config_vars.access_vlan1)		
		self._verify_vlan_41(self.config.config_vars.access_vlan1)		
		self._verify_vlan_42(self.config.config_vars.access_vlan1)		
		self._verify_vlan_43(self.config.config_vars.access_vlan1)		
		self._verify_vlan_44(self.config.config_vars.access_vlan1)		
		self._verify_vlan_45(self.config.config_vars.access_vlan1)		
		self._verify_vlan_46(self.config.config_vars.access_vlan1)		
		self._verify_vlan_47(self.config.config_vars.access_vlan1)
		
	def assert_switch_48Port_poe(self):
		logger.debug("PortPage: Asserting the value of POE field")
		self._verify_poe(self.config.config_vars.poe1_enabled)
		self._verify_poe_1(self.config.config_vars.poe1_enabled)		
		self._verify_poe_2(self.config.config_vars.poe1_enabled)				
		self._verify_poe_3(self.config.config_vars.poe1_enabled)				
		self._verify_poe_4(self.config.config_vars.poe1_enabled)				
		self._verify_poe_5(self.config.config_vars.poe1_enabled)				
		self._verify_poe_6(self.config.config_vars.poe1_enabled)				
		self._verify_poe_7(self.config.config_vars.poe1_enabled)				
		self._verify_poe_8(self.config.config_vars.poe1_enabled)				
		self._verify_poe_9(self.config.config_vars.poe1_enabled)				
		self._verify_poe_10(self.config.config_vars.poe1_enabled)				
		self._verify_poe_11(self.config.config_vars.poe1_enabled)	
		self._verify_poe_12(self.config.config_vars.poe1_enabled)				
		self._verify_poe_13(self.config.config_vars.poe1_enabled)				
		self._verify_poe_14(self.config.config_vars.poe1_enabled)				
		self._verify_poe_15(self.config.config_vars.poe1_enabled)				
		self._verify_poe_16(self.config.config_vars.poe1_enabled)				
		self._verify_poe_17(self.config.config_vars.poe1_enabled)				
		self._verify_poe_18(self.config.config_vars.poe1_enabled)				
		self._verify_poe_19(self.config.config_vars.poe1_enabled)				
		self._verify_poe_20(self.config.config_vars.poe1_enabled)				
		self._verify_poe_21(self.config.config_vars.poe1_enabled)
		self._verify_poe_22(self.config.config_vars.poe1_enabled)
		self._verify_poe_23(self.config.config_vars.poe1_enabled)
		self._verify_poe_24(self.config.config_vars.poe1_enabled)
		self._verify_poe_25(self.config.config_vars.poe1_enabled)
		self._verify_poe_26(self.config.config_vars.poe1_enabled)
		self._verify_poe_27(self.config.config_vars.poe1_enabled)
		self._verify_poe_28(self.config.config_vars.poe1_enabled)
		self._verify_poe_29(self.config.config_vars.poe1_enabled)
		self._verify_poe_30(self.config.config_vars.poe1_enabled)
		self._verify_poe_31(self.config.config_vars.poe1_enabled)
		self._verify_poe_32(self.config.config_vars.poe1_enabled)
		self._verify_poe_33(self.config.config_vars.poe1_enabled)
		self._verify_poe_34(self.config.config_vars.poe1_enabled)
		self._verify_poe_35(self.config.config_vars.poe1_enabled)
		self._verify_poe_36(self.config.config_vars.poe1_enabled)
		self._verify_poe_37(self.config.config_vars.poe1_enabled)
		self._verify_poe_38(self.config.config_vars.poe1_enabled)
		self._verify_poe_39(self.config.config_vars.poe1_enabled)
		self._verify_poe_40(self.config.config_vars.poe1_enabled)
		self._verify_poe_41(self.config.config_vars.poe1_enabled)
		self._verify_poe_42(self.config.config_vars.poe1_enabled)
		self._verify_poe_43(self.config.config_vars.poe1_enabled)
		self._verify_poe_44(self.config.config_vars.poe1_enabled)
		self._verify_poe_45(self.config.config_vars.poe1_enabled)
		self._verify_poe_46(self.config.config_vars.poe1_enabled)		
		self._verify_poe_47(self.config.config_vars.poe1_enabled)
		
	def assert_switch_48Port_speed_duplex(self):
		logger.debug("PortPage: Asserting the value of Speed/Duplex field")
		self._verify_speed(self.config.config_vars.speed_auto)
		self._verify_speed_1(self.config.config_vars.speed_auto)		
		self._verify_speed_2(self.config.config_vars.speed_auto)				
		self._verify_speed_3(self.config.config_vars.speed_auto)				
		self._verify_speed_4(self.config.config_vars.speed_auto)				
		self._verify_speed_5(self.config.config_vars.speed_auto)				
		self._verify_speed_6(self.config.config_vars.speed_auto)				
		self._verify_speed_7(self.config.config_vars.speed_auto)				
		self._verify_speed_8(self.config.config_vars.speed_auto)				
		self._verify_speed_9(self.config.config_vars.speed_auto)				
		self._verify_speed_10(self.config.config_vars.speed_auto)				
		self._verify_speed_11(self.config.config_vars.speed_auto)	
		self._verify_speed_12(self.config.config_vars.speed_auto)				
		self._verify_speed_13(self.config.config_vars.speed_auto)				
		self._verify_speed_14(self.config.config_vars.speed_auto)				
		self._verify_speed_15(self.config.config_vars.speed_auto)				
		self._verify_speed_16(self.config.config_vars.speed_auto)				
		self._verify_speed_17(self.config.config_vars.speed_auto)				
		self._verify_speed_18(self.config.config_vars.speed_auto)				
		self._verify_speed_19(self.config.config_vars.speed_auto)				
		self._verify_speed_20(self.config.config_vars.speed_auto)				
		self._verify_speed_21(self.config.config_vars.speed_auto)
		self._verify_speed_22(self.config.config_vars.speed_auto)
		self._verify_speed_23(self.config.config_vars.speed_auto)
		self._verify_speed_24(self.config.config_vars.speed_auto)
		self._verify_speed_25(self.config.config_vars.speed_auto)
		self._verify_speed_26(self.config.config_vars.speed_auto)
		self._verify_speed_27(self.config.config_vars.speed_auto)
		self._verify_speed_28(self.config.config_vars.speed_auto)
		self._verify_speed_29(self.config.config_vars.speed_auto)
		self._verify_speed_30(self.config.config_vars.speed_auto)
		self._verify_speed_31(self.config.config_vars.speed_auto)
		self._verify_speed_32(self.config.config_vars.speed_auto)
		self._verify_speed_33(self.config.config_vars.speed_auto)
		self._verify_speed_34(self.config.config_vars.speed_auto)
		self._verify_speed_35(self.config.config_vars.speed_auto)
		self._verify_speed_36(self.config.config_vars.speed_auto)
		self._verify_speed_37(self.config.config_vars.speed_auto)
		self._verify_speed_38(self.config.config_vars.speed_auto)
		self._verify_speed_39(self.config.config_vars.speed_auto)
		self._verify_speed_40(self.config.config_vars.speed_auto)
		self._verify_speed_41(self.config.config_vars.speed_auto)
		self._verify_speed_42(self.config.config_vars.speed_auto)
		self._verify_speed_43(self.config.config_vars.speed_auto)
		self._verify_speed_44(self.config.config_vars.speed_auto)
		self._verify_speed_45(self.config.config_vars.speed_auto)
		self._verify_speed_46(self.config.config_vars.speed_auto)
		self._verify_speed_47(self.config.config_vars.speed_auto)
	
	