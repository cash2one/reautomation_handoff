from athenataf.lib.util.WebPage import WebPage
import logging
logger = logging.getLogger('athenataf')
import traceback
import time

class EditWiredNetworkPage(WebPage):
	def __init__(self, test, browser, config):
		WebPage.__init__(self, "EditWiredNetwork", test, browser, config)
		self.test.assertPageLoaded(self)


	def isPageLoaded(self):
		if self.uplink:
			return True    
		else:
			return False

	def edit_basic_info_setting(self):
		'''
		Editing Basic Info page Fields
		'''
		logger.debug('EditwiredNetwork page : Setting Wired Speed value')
		self.speed.set(self.config.config_vars.speed_edit)
		logger.debug(' EditwiredNetwork page : Setting Wired Duplex value')
		self.duplex.set(self.config.config_vars.duplex_edit) 
		logger.debug(' EditwiredNetwork page : Setting Wired Admin Status to Up')
		self.admin_status.set(self.config.config_vars.admin_edit)
		logger.debug(' EditwiredNetwork page : Disable Wired Content Filtering ')
		self.content.set(self.config.config_vars.content)
		logger.debug(' EditwiredNetwork page : Enable Wired Uplink ')
		self.uplink.set(self.config.config_vars.uplink)
		logger.debug(' EditwiredNetwork page :Setting Wired Spanning Tree ')
		self.spanning_tree.set(self.config.config_vars.uplink)
		time.sleep(4)
		if self.save:
			time.sleep(4)
			self.save.click()
			time.sleep(8)

	def edit_net_assign_setting(self):
		'''
		Editing Network Assign page Fields
		'''
		logger.debug(' EditwiredNetwork page :clicking on network assign')
		self.network_assign.click()
		time.sleep(30)
		if self.profile_1:
			if self.profile_1.get_selected() == self.config.config_vars.edit_profile1:
				logger.debug('EditwiredNetwork page : Setting Wired Profile1  to wired-instant')
				self.profile_1.set(self.config.config_vars.edit_profile2)
			else:
				logger.debug('EditwiredNetwork page : Setting Wired Profile1 to default_wired_port_profile')
				self.profile_1.set(self.config.config_vars.edit_profile1)
		time.sleep(10)
		if self.save:
			time.sleep(10)
			logger.debug(' EditwiredNetwork page :clicks on Save')
			self.save.click()
			time.sleep(10)

	def edit_net_assign_default(self):
		'''
		Editing Network Assign page Defaults
		'''
		logger.debug(' EditwiredNetwork page :clicking on network assign')
		self.network_assign.click()
		if not self.network_assign_content:
			logger.debug(' EditwiredNetwork page :clicking on network assign')
			self.network_assign.click()
		time.sleep(30)
		if self.profile_0:
			logger.debug('EditwiredNetwork page : Setting Wired Profile0  to default assign port')
			self.profile_0.set(self.config.config_vars.default_assign_port)
		time.sleep(10)
		if self.save:
			logger.debug(' EditwiredNetwork page :clicks on Save')
			self.save.click()
		time.sleep(10)

	def assert_edited_value(self):
		if self.speed_assert and self.duplex_assert and self.admin_assert:
			return True
		else:
			raise AssertionError("Edited element not found: %s" % traceback.format_exc() )

	def edit_basic_info_setting_employee_primary_usage(self):
		'''
		Editing Basic Info page Fields
		'''
		logger.debug('EditwiredNetwork page : Setting Wired Speed value')
		self.speed.set(self.config.config_vars.speed_edit)
		logger.debug(' EditwiredNetwork page : Setting Wired Duplex value')
		self.duplex.set(self.config.config_vars.duplex_edit)
		logger.debug(' EditwiredNetwork page : Setting Wired POE value')
		self.poe.set(self.config.config_vars.poe_disabled1)
		logger.debug(' EditwiredNetwork page : Setting Wired Admin Status to Down')
		self.admin_status.set(self.config.config_vars.admin_down1)
		logger.debug(' EditwiredNetwork page : Enable Wired Content Filtering ')
		self.content.set(self.config.config_vars.uplink)
		logger.debug(' EditwiredNetwork page : Enable Wired Uplink ')
		self.uplink.set(self.config.config_vars.uplink)
		logger.debug(' EditwiredNetwork page :Enable Wired Spanning tree value ')
		self.spanning_tree.set(self.config.config_vars.uplink)
		time.sleep(4)
		
	def click_employee_primary_usage(self):
		'''
		Clicks on 'Employee' radio button
		'''
		if self.primary_usage_employee:
			logger.debug('EditwiredNetwork page : clicking on employee radio button')
			self.primary_usage_employee.click()
		else:
			raise AssertionError("Employee radio button not found: %s" % traceback.format_exc() )
			

	def click_vlans_accordion(self):
		'''
		Clicks on 'VLANS' accordion
		'''
		if self.vlans_accordion:
			logger.debug('EditwiredNetwork page : clicking on VLANS accordion')
			self.vlans_accordion.click()
			self.buy_time(5)
			
	def click_security_accordion(self):
		'''
		Clicks on 'SECURITY' accordion
		'''
		if self.security_accordion:
			logger.debug('EditwiredNetwork page : clicking on SECURITY accordion')
			self.security_accordion.click()
		if not self.mac_authentication_no_enterprise:
			logger.debug('EditwiredNetwork page : clicking on SECURITY accordion')
			self.security_accordion.click()
		
	def click_access_accordion(self):
		'''
		Clicks on 'ACCESS' accordion
		'''
		if self.access_accordion:
			logger.debug('EditwiredNetwork page : clicking on ACCESS accordion')
			self.access_accordion.click()
			
	def click_network_assign_accordion(self):
		'''
		Clicks on 'NETWORK ASSIGN' accordion
		'''
		if self.network_assign:
			logger.debug('EditwiredNetwork page : clicking on NETWORK ASSIGN accordion')
			self.network_assign.click()
			
	def edit_vlans_access_mode_network_assigned_access_vlan(self,access_vlan_value,rule_type,operator,string,vlan_id):
		'''
		Edits VALNS access mode fields
		'''
		logger.debug('EditwiredNetwork page : Selecting Access mode in mode dropdown')
		self.mode.set(self.config.config_vars.mode_access)
		logger.debug('EditwiredNetwork page : clicking on NETWORK ASSIGNED radio button')
		self.network_assigned.click()
		logger.debug('EditwiredNetwork page : Setting ACCESS VLAN value')
		self.access_vlan.set(access_vlan_value)
		# logger.debug('EditwiredNetwork page : Clicking NEW button')
		# self.new_vlan_rule_button.click()
		self.click_new_vlan_assignment_role_button()
		logger.debug('EditwiredNetwork page : Setting ATTRIBUTE value')
		self.vlan_rule_type.set(rule_type)
		logger.debug('EditwiredNetwork page : Setting OPERATOR value')
		self.vlan_rule_assign_operator.set(operator)
		logger.debug('EditwiredNetwork page : Setting STRING value')
		self.vlan_rule_name.set(string)
		logger.debug('EditwiredNetwork page : Setting STRING value')
		self.rule_vlan.set(vlan_id)
		logger.debug('EditwiredNetwork page : Clicking OK button')
		self.submit_vlan_form_button.click()
		self.buy_time(5)
		
	def buy_time(self,seconds):
		logger.debug("EditwiredNetwork page : Waiting for '%s' seconds"%seconds)
		time.sleep(seconds)
		
	def click_new_vlan_assignment_role_button(self):
		'''
		Clicks new button to create new vlan assignment_role.
		'''
		logger.debug('EditwiredNetwork page : Clicking NEW button')
		if self.new_vlan_rule_button:
			self.new_vlan_rule_button.click()
		self.buy_time(3)

	def create_new_vlan_assignment_role(self,attribute='AP-Group',operator='contains',string=None,rule_vlan_value=None):
		logger.debug("EditwiredNetwork page : Selecting Attribute '%s'"%attribute)
		self.vlan_rule_type.set(attribute)
		logger.debug("EditwiredNetwork page : Selecting Operator '%s'"%operator)
		self.vlan_rule_assign_operator.set(operator)
		logger.debug("EditwiredNetwork page : Setting Vlan_rule_name '%s'"%string)
		self.vlan_rule_name.set(string)
		logger.debug("EditwiredNetwork page : Setting Vlan_rule '%s'"%string)
		self.rule_vlan.set(rule_vlan_value)	
		logger.debug('EditwiredNetwork page : Clicking OK button')
		self.submit_vlan_form_button.click()
		self.buy_time(6)
		
	def edit_security_internal_authenticated_all_fields(self,mac_auth='Disabled',auth_server='-- Select --',reauth_interval_time=0,reauth_unit_value='min.'):
		self.click_security_accordion()
		# logger.debug("EditwiredNetwork page : Selecting Splash page type '%s'"%self.config.config_vars.internal_authenticated)
		# self.splash_page_type.set(self.config.config_vars.internal_authenticated)		
		logger.debug("EditwiredNetwork page : Selecting Mac_authentication '%s'"%mac_auth)
		self.mac_authentication_no_enterprise.set(mac_auth)
		logger.debug("EditwiredNetwork page : Selecting AuthServer1 '%s'"%auth_server)
		self.authentication_server.set(auth_server)
		logger.debug("EditwiredNetwork page : Setting reauth_interval '%s'"%reauth_interval_time)
		self.reauth_interval.set(reauth_interval_time)
		logger.debug("EditwiredNetwork page : Selecting reauth_unit '%s'"%reauth_unit_value)
		self.reauth_unit.set(reauth_unit_value)
	
	def select_3g_4g_wifi_ethernet(self,threeg_fourg=False,wifi=False,ethernet=False):
		'''
		Selects 3G/4G or Wifi or Ethernet.
		'''
		if threeg_fourg:
			logger.debug("EditwiredNetwork page : clicking on 3G/4G checkbox")
			if self.checkbox_box_3g:
				self.checkbox_box_3g.click()
		if wifi:
			logger.debug("EditwiredNetwork page : clicking on wifi checkbox")
			if self.checkbox_box_wifi:
				self.checkbox_box_wifi.click()
		if ethernet:
			logger.debug("EditwiredNetwork page : clicking on ethernet checkbox")
			if self.checkbox_box_ethernet:
				self.checkbox_box_ethernet.click()
		self.buy_time(6)
		
	def edit_access_role_based_all_fields(self,new_role=None,attribute='AP-Group',operator='contains',string=None,role='default_wired_port_profile'):
		logger.debug("EditwiredNetwork page : clicking on role based radio button")
		self.role_based.click()
		self.create_role_based_new_role(new_role)
		self.create_new_role_assignment_rule(attribute,operator,string,role)
		
	def create_role_based_new_role(self,new_role):
		logger.debug("EditwiredNetwork page : clicking on NEW button")
		self.create_role.click()
		logger.debug("EditwiredNetwork page : Setting  '%s'"%new_role)
		self.role_input.set(new_role)
		logger.debug("EditwiredNetwork page : clicking on OK button")
		self.create_role_ok.click()

	def create_new_role_assignment_rule(self,attribute,operator,string,role):
		logger.debug("EditwiredNetwork page : clicking on NEW button")
		self.new_role_assignment.click()
		logger.debug("EditwiredNetwork page : Selecting attribute '%s'"%attribute)
		self.role_assign_attribute.set(attribute)
		logger.debug("EditwiredNetwork page : Selecting operator '%s'"%operator)
		self.role_assign_operator.set(operator)
		logger.debug("EditwiredNetwork page : Setting string '%s'"%string)
		self.role_assign_operand.set(string)
		logger.debug("EditwiredNetwork page : Selecting role '%s'"%role)
		self.role_assign_name.set(role)
		logger.debug("EditwiredNetwork page : Clicking SAVE button")
		self.save_role_assignments.click()

	def edit_network_assignment_all_fields(self,port_profile0,port_profile1,port_profile2,port_profile3,port_profile4):
		self.click_network_assign_accordion()
		logger.debug("EditwiredNetwork page : Selecting 0/0 '%s'"%port_profile0)
		self.profile_0.set(port_profile0)
		logger.debug("EditwiredNetwork page : Selecting 0/1 '%s'"%port_profile1)
		self.profile_1.set(port_profile1)
		logger.debug("EditwiredNetwork page : Selecting 0/2 '%s'"%port_profile2)
		self.wired_profile_2.set(port_profile2)
		logger.debug("EditwiredNetwork page : Selecting 0/3 '%s'"%port_profile3)
		self.wired_profile_3.set(port_profile3)
		logger.debug("EditwiredNetwork page : Selecting 0/4 '%s'"%port_profile4)
		self.wired_profile_4.set(port_profile4)

	def click_save_settings(self):
		'''
		Clicks on save_settings button
		'''
		if self.save_settings:
			logger.debug("EditwiredNetwork page : Clicking SAVE_SETTINGS button")
			self.save_settings.click()
		self.buy_time(10)
		
	def select_internalserver(self):
		self.buy_time(5)
		logger.debug("EditWiredNetworkPage : Selecting  InternalServer for Authentication Server feild ")
		self.authentication_server.set(self.config.config_vars.edit_Authentication_server)
		self.buy_time(5)

	def add_internal_sever_user(self):
		'''
		creates internal server user
		'''
		logger.debug("EditWiredNetworkPage: Clicking on internal server user link ")
		self.show_users_link.click()
		logger.debug("EditWiredNetworkPage: Writing user name")
		self.userTxt.set(self.config.config_vars.userTxt)
		logger.debug("EditWiredNetworkPage: Writing password")
		self.pswdTxt.set(self.config.config_vars.pswdTxt)
		logger.debug("EditWiredNetworkPage: Re-writing password")
		self.pswdTxt2.set(self.config.config_vars.pswdTxt2)
		logger.debug("EditWiredNetworkPage: selecting type as guest")
		self.typeTxt.set(self.config.config_vars.typeTxt)
		logger.debug("EditWiredNetworkPage: Clicking on add button")
		self.updateButton.click()
		logger.debug("EditWiredNetworkPage: Clicking on ok button")
		self.okButton.click()

	def checking_for_authentication_servers_visibility(self):
		logger.debug("EditWiredNetworkPage : Checking whether authentication_server1 feild is visible")
		if not self.authentication_server:
			raise AssertionError("authentication_server1 feild is not visible .Traceback: %s " %traceback.format_exc())
		
		logger.debug("EditWiredNetworkPage : Checking whether authentication_server2 feild is visible")
		if self.authentication_server_2:
			raise AssertionError("authentication_server2 feild is visible .Traceback: %s " %traceback.format_exc())
			
	def click_on_vlan_network_assigned(self):
		'''
		clicks on Network Assigned Radio button
		'''
		logger.debug('EditwiredNetwork page : clicking on NETWORK ASSIGNED radio button')
		self.network_assigned.click()
		
	def set_security_authentication_802_1x(self,value):
		'''
		Sets Security 802.1x Authentication 
		'''
		logger.debug('EditwiredNetwork page : clicking on NETWORK ASSIGNED radio button')
		self.authentication_802_1x.set(value)
		
	def create_external_radius_server_in_auth_servers(self,server):
		'''
		Create new external radius in auth server 1 
		'''
		if server == 'one':
			logger.debug('EditwiredNetwork : Setting new external server to Authentication Server 1')
			self.authentication_server.set(self.config.config_vars.new_external_server)
			logger.debug('EditwiredNetwork : Entering Auth Server Name')
			self.auth_server_name.set(self.config.config_vars.auth_server_value)
		if server == 'two':
			logger.debug('EditwiredNetwork : Setting new external server to Authentication Server 1')
			self.authentication_server_2.set(self.config.config_vars.new_external_server)
			self.buy_time(5)
			logger.debug('EditwiredNetwork : Entering details')
			self.auth_server_name.set(self.config.config_vars.auth_server_value_2)
		logger.debug('EditwiredNetwork : Entering Auth IP Address')
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr_value)
		logger.debug('EditwiredNetwork : Entering Auth sharedKey')
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug('EditwiredNetwork : Entering Auth sharedKey')
		self.Retype_auth_shared_key.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug('EditwiredNetwork : Saving external radius server')
		self.save_server.click()
		
	def configure_wired_mac_authentication_fail_through(self,value):
		'''
		configure Mac Authentication fail through 
		'''	
		logger.debug("EditwiredNetwork : Sets Mac Authentication fail through . ")		
		self.mac_authentication_fail_through.set(value)		
	
	def set_load_balancing_field(self,value):
		'''
		sets given value to load balancing field
		'''
		logger.debug("EditwiredNetwork :Setting load balancing.")
		self.load_balancing_dropdown.set(value)