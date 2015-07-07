import traceback
from athenataf.lib.util.WebPage import WebPage
import time
import logging
logger = logging.getLogger('athenataf')

class DhcpPage(WebPage):
	def __init__(self, test, browser, config):
		WebPage.__init__(self, "Dhcp", test, browser, config)
		self.test.assertPageLoaded(self)

	def isPageLoaded(self):
		if self.new_dhcp:
			return True    
		else:
			return False

	def is_dhcp_present(self):
		if self.dhcp_name:
			return True    
		else:
			return False

	def delete_dhcp_if_present(self):
		logger.debug("DHCP Page : Deleting dhcp if present...")
		if self.dhcp_name:
			logger.debug("DHCP Page : Clicking on dhcp_name...")
			self.dhcp_name.click()
			logger.debug("DHCP Page : Clicking on 'DELETE' button")
			self.delete_dhcp.click()
			logger.debug("DHCP Page : Accepting alert...")
			self.browser.accept_alert()
			self.buy_time()
			self.browser.refresh()
		self.buy_time()

	def create_new_dhcp(self):
		logger.debug("DHCP Page : Clicking on 'NEW' button...")
		self.new_dhcp.click()
		logger.debug("DHCP Page : Setting Dhcp_name...")
		self.network_name.set(self.config.config_vars.Dhcp_name)
		logger.debug("DHCP Page : Setting Dhcp_Vlan...")
		self.vlan_name.set(self.config.config_vars.Dhcp_Vlan)
		logger.debug("DHCP Page : Setting Dhcp_Netmask...")
		self.netmask.set(self.config.config_vars.Dhcp_Netmask)
		logger.debug("DHCP Page : Setting Default_router...")
		self.default_router.set(self.config.config_vars.Dhcp_Default_Router)
		logger.debug("DHCP Page : Setting DNS_server...")
		self.dns_server.set(self.config.config_vars.Dhcp_Dns_Server)
		logger.debug("DHCP Page : Setting Domain_name...")
		self.domain_name.set(self.config.config_vars.Dhcp_Domain_Name)
		logger.debug("DHCP Page : Setting IP_Address_Range...")		
		self.distributed_ip_start.set(self.config.config_vars.Distributed_Ip_Start)
		self.distributed_ip_end.set(self.config.config_vars.Distributed_Ip_End)
		logger.debug("DHCP Page : Setting Distributed_option_type and option_value...")
		self.distributed_option_type.set(self.config.config_vars.Distributed_Option_Type)
		self.distributed_option_value.set(self.config.config_vars.Distributed_Option_Value)
		logger.debug("DHCP Page : Clicking 'NEXT' button...")
		self.next_button.click()
		logger.debug("DHCP Page : Setting client_per_branch...")
		self.client_per_branch.set(self.config.config_vars.Client_Per_Branch)
		logger.debug("DHCP Page : Clicking 'NEXT' button...")
		self.next_button.click()
		logger.debug("DHCP Page : Setting Reserve field...")
		self.reserve_first.set(self.config.config_vars.Reserve_First)
		self.reserve_last.set(self.config.config_vars.Reserve_Last)
		logger.debug("DHCP Page : Clicking 'FINISH' button...")
		self.finish_button.click()
		self.browser.refresh()
		self.buy_time()

	def edit_dhcp(self):
		if self.dhcp_name:
			logger.debug("DHCP Page : Clicking on Dhcp_name...")
			self.dhcp_name.click()
			logger.debug("DHCP Page : Clicking on 'Edit' button...")
			self.edit.click()

	def buy_time(self):
		import time
		time.sleep(10)

	def edit_network(self):
		'''
		Edit default router,dns router,client per branch, reserve first of distributed dhcp scope.
		'''
		logger.debug("DHCP Page : Editing Network settings...")
		self.edit_dhcp()
		self.default_router.set(self.config.config_vars.Edit_Dhcp_Default_Router)
		self.dns_server.set(self.config.config_vars.Edit_Dhcp_Dns_Server)
		self.network_name.set(self.config.config_vars.Dhcp_name)
		self.vlan_name.set(self.config.config_vars.vlan_number_value)
		self.netmask.set(self.config.config_vars.subnet_mask)
		self.domain_name.set(self.config.config_vars.domain_name)
		self.lease_time.set(self.config.config_vars.lease_time_value)
		self.ipaddress_range_start.set(self.config.config_vars.subnet_address)
		self.ipaddress_range_end.set(self.config.config_vars.vc_ip_address)
		self.option_type.set(self.config.config_vars.vlan_id)  
		self.option_value.set(self.config.config_vars.vlan_number_value)
		time.sleep(4)
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.next_button.click()
		if self.next_button:
			self.next_button.click()
		self.client_per_branch.set(self.config.config_vars.Edit_Client_Per_Branch)
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.next_button.click()
		self.buy_time()
		self.reserve_first.set(self.config.config_vars.Edit_Reserve_First)
		logger.debug("DHCP Page : Clicking on 'FINISH' button...")
		self.finish_button.click()

	def dhcp_field_validation(self):
		logger.debug("DHCP Page : Clicking on 'NEW' button...")
		self.new_dhcp.click()
		logger.debug("DHCP Page : Setting invalid values...")
		self.network_name.set(self.config.config_vars.admin_invalid_u_name)
		self.vlan_name.set(self.config.config_vars.Dhcp_Vlan_Error)
		self.netmask.set(self.config.config_vars.Dhcp_Netmask_Error)
		self.default_router.set(self.config.config_vars.Dhcp_Default_Router_Error)
		self.dns_server.set(self.config.config_vars.Dhcp_Dns_Server_Error)
		self.domain_name.set(self.config.config_vars.Dhcp_Domain_Name_Error)
		self.lease_time.set(self.config.config_vars.Dhcp_Lease_Time_Error)  
		self.distributed_option_type.set(self.config.config_vars.Dhcp_Option_Type_Error)
		self.distributed_option_value.set(self.config.config_vars.Dhcp_Option_Value_Error)
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.next_button.click()
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.next_button.click()		
		if not self.dhcp_name_error_msg:
			raise AssertionError("Dhcp network name length is more than 32 chars .Traceback: %s " %traceback.format_exc())

		if not self.network_type.selected == self.config.config_vars.Dhcp_Network_Type:
			raise AssertionError("Network type is not Distributed,L2 by default .Traceback: %s " %traceback.format_exc())

		if not self.vlan_error:
			raise AssertionError(" Vlan range greater than 4093 .Traceback: %s " %traceback.format_exc())

		if not self.netmask_error:
			raise AssertionError(" Invalid netmask .Traceback: %s " %traceback.format_exc())

		if not self.ip_address_error:
			raise AssertionError(" Invalid Ip address .Traceback: %s " %traceback.format_exc())        

		if not self.dhcp_dns_server_error:
			raise AssertionError(" Invalid dns server .Traceback: %s " %traceback.format_exc())        

		if not self.domain_name_error:
			raise AssertionError(" Invalid domain name .Traceback: %s " %traceback.format_exc())

		if not self.lease_time_error:
			raise AssertionError(" Lease time greater time 1440 .Traceback: %s " %traceback.format_exc())

		if not self.option_type_error:
			raise AssertionError(" option type greater than 254 .Traceback: %s " %traceback.format_exc())
		logger.debug("DHCP Page : Clicking on 'CANCEL' button...")
		self.cancel.click()

	def assert_mandatory_fields(self):
		logger.debug("DHCP Page : Clicking on 'NEW' button...")
		self.new_dhcp.click()
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.next_button.click()
		logger.debug("DHCP Page : Asserting error messages...")
		if not self.dhcp_name_error:
			raise AssertionError(" network name is empty .Traceback: %s " %traceback.format_exc())
		if not self.mandatory_vlan_error:
			raise AssertionError(" Vlan is empty .Traceback: %s " %traceback.format_exc())
		if not self.mandatory_netmask_error:
			raise AssertionError(" Netmask is empty .Traceback: %s " %traceback.format_exc())
		if not self.mandatory_ip_address_error:
			raise AssertionError(" Default router is empty .Traceback: %s " %traceback.format_exc())
		logger.debug("DHCP Page : Clicking on 'CANCEL' button...")
		self.cancel.click()

	def assert_client_per_branch(self):
		logger.debug("DHCP Page : Clicking on 'NEW' button...")
		self.new_dhcp.click()
		logger.debug("DHCP Page : Setting Dhcp_name...")
		self.network_name.set(self.config.config_vars.Dhcp_name)
		logger.debug("DHCP Page : Setting Dhcp_Vlan...")
		self.vlan_name.set(self.config.config_vars.Dhcp_Vlan)
		logger.debug("DHCP Page : Setting Dhcp_Netmask...")
		self.netmask.set(self.config.config_vars.Dhcp_Netmask)
		logger.debug("DHCP Page : Setting Dhcp_Default_Router...")
		self.default_router.set(self.config.config_vars.Dhcp_Default_Router)
		logger.debug("DHCP Page : Setting Dhcp_DNS_Server...")
		self.dns_server.set(self.config.config_vars.Dhcp_Dns_Server)
		logger.debug("DHCP Page : Setting Dhcp_Domain_name...")
		self.domain_name.set(self.config.config_vars.Dhcp_Domain_Name)
		logger.debug("DHCP Page : Setting IP_Address_range...")
		self.distributed_ip_start.set(self.config.config_vars.Distributed_Ip_Start)
		self.distributed_ip_end.set(self.config.config_vars.Distributed_Ip_End)
		logger.debug("DHCP Page : Setting Option_type...")
		self.distributed_option_type.set(self.config.config_vars.Distributed_Option_Type)
		logger.debug("DHCP Page : Setting Option_Value...")
		self.distributed_option_value.set(self.config.config_vars.Distributed_Option_Value)
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.next_button.click()
		self.client_per_branch.set(self.config.config_vars.Client_Per_Branch_Exceed)
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.next_button.click()
		if not self.client_per_branch_error :
			raise AssertionError(" Client per branch is greater than  IP address range in network .Traceback: %s " %traceback.format_exc())
		logger.debug("DHCP Page : Clicking on 'CANCEL' button...")
		self.cancel.click()

	def assert_reserve_first_ip_range(self):
		logger.debug("DHCP Page : Clicking on 'NEW' button...")
		self.new_dhcp.click()
		logger.debug("DHCP Page : Setting Dhcp_name...")
		self.network_name.set(self.config.config_vars.Dhcp_name)
		logger.debug("DHCP Page : Setting Dhcp_Vlan...")
		self.vlan_name.set(self.config.config_vars.Dhcp_Vlan)
		logger.debug("DHCP Page : Setting Dhcp_Netmask...")
		self.netmask.set(self.config.config_vars.Dhcp_Netmask)
		logger.debug("DHCP Page : Setting Dhcp_Default_router...")
		self.default_router.set(self.config.config_vars.Dhcp_Default_Router)
		logger.debug("DHCP Page : Setting Dhcp_DNS_server...")
		self.dns_server.set(self.config.config_vars.Dhcp_Dns_Server)
		logger.debug("DHCP Page : Setting Dhcp_Domain_name...")
		self.domain_name.set(self.config.config_vars.Dhcp_Domain_Name)
		logger.debug("DHCP Page : Setting IP_Address_range...")
		self.distributed_ip_start.set(self.config.config_vars.Distributed_Ip_Start)
		self.distributed_ip_end.set(self.config.config_vars.Distributed_Ip_End)
		logger.debug("DHCP Page : Setting option_type...")
		self.distributed_option_type.set(self.config.config_vars.Distributed_Option_Type)
		logger.debug("DHCP Page : Setting option_value...")
		self.distributed_option_value.set(self.config.config_vars.Distributed_Option_Value)
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.next_button.click()
		logger.debug("DHCP Page : Setting Client_per_branch...")
		self.client_per_branch.set(self.config.config_vars.Client_Per_Branch)
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.next_button.click()
		logger.debug("DHCP Page : Setting dhcp_reserve_field_values...")
		self.reserve_first.set(self.config.config_vars.Reserve_First_Exceed)
		self.reserve_last.set(self.config.config_vars.Reserve_Last_Exceed)
		logger.debug("DHCP Page : Clicking on 'FINISH' button...")
		self.finish_button.click()
		if not self.reserve_first_error :
			raise AssertionError(" Reserve first is greater than 0-clients per branch .Traceback: %s " %traceback.format_exc())
		if not self.reserve_last_error :
			raise AssertionError(" Reserve last is greater than 0-clients per branch .Traceback: %s " %traceback.format_exc())
		logger.debug("DHCP Page : Setting dhcp_reserve_field_values...")
		self.reserve_first.set(self.config.config_vars.Reserve_First)
		self.reserve_last.set(self.config.config_vars.Reserve_Last)
		logger.debug("DHCP Page : Clicking on 'FINISH' button...")
		self.finish_button.click()
		import time
		time.sleep(15)
		self.delete_dhcp_if_present()
		
		
	def click_on_distributed_dhcp_scopes_new(self):
		'''
		click on New button of distributed DHCP Scopes
		'''
		logger.debug("DHCP Page : Clicking on  'New' button")
		self.new_dhcp.click()
		self.buy_time()
		
	def set_distributed_dhcp_usrname(self,value=None):
		'''
		writing distributed DHCP Scopes UserName in  textbox 'Name'
		'''
		logger.debug("DHCP Page :Write  DHCP name into the text-box")
		self.network_name.set(value)
		
	def set_distributed_dhcp_vlan(self,value):
		'''
		writing distributed DHCP Scopes Vlan  in  textbox 'Vlan'
		'''	
		logger.debug("DHCP Page :Write  DHCP Vlan  into the text-box")
		self.vlan_name.set(value)
	
	def set_distributed_dhcp_netmask(self,value):
		'''
		writing distributed DHCP Scopes NetMask  in  textbox 'NetMask'
		'''	
		logger.debug("DHCP Page :Write  DHCP NetMask  into the text-box")
		self.netmask.set(value)
			
	def set_distributed_dhcp_default_router(self,value):		
		'''
		writing distributed DHCP Scopes Default Router  in  textbox 'Default Router'
		'''	
		logger.debug("DHCP Page :Write  DHCP Default Router  into the text-box")
		self.default_router.set(value)	
	
	def set_distributed_dhcp_dns_server(self,value):		
		'''
		writing distributed DHCP Scopes Dns Server  in  textbox 'Dns Server'
		'''	
		logger.debug("DHCP Page :Write  DHCP Dns Server  into the text-box")
		self.dns_server.set(value)		
			
	def set_distributed_dhcp_domain_name(self,value):		
		'''
		writing distributed DHCP Scopes Domain Name  in  textbox 'Domain Name'
		'''	
		logger.debug("DHCP Page :Write  DHCP Domain Name  into the text-box")
		self.domain_name.set(value)			
	
	def set_distributed_dhcp_ipaddress_range_start(self,value):		
		'''
		writing distributed DHCP Scopes IpAddress Range Start  in  textbox 'IpAddress Range'
		'''	
		logger.debug("DHCP Page :Write  DHCP IpAddress Range  into the text-box")
		self.ipaddress_range_start.set(value)	
	
	def set_distributed_dhcp_ipaddress_range_end(self,value):		
		'''
		writing distributed DHCP Scopes IpAddress Range End  in  textbox 'IpAddress Range'
		'''	
		logger.debug("DHCP Page :Write  DHCP IpAddress Range  into the text-box")
		self.ipaddress_range_end.set(value)
			
	def set_distributed_dhcp_option_type(self,value):		
		'''
		writing distributed DHCP Scopes Option Type in  textbox 'Option Type'
		'''	
		logger.debug("DHCP Page :Write  DHCP Option Type  into the text-box")
		self.option_type.set(value)		
			
	def set_distributed_dhcp_option_value(self,value):		
		'''
		writing distributed DHCP Scopes Option Value in  textbox 'Option Value'
		'''	
		logger.debug("DHCP Page :Write  DHCP Option Value  into the text-box")
		self.option_value.set(value)	
	
	def click_on_next_button(self):
		'''
		clicking on Distributed dhcp Next button
		'''
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.next_button.click()
		self.buy_time()
		
	def set_distributed_dhcp_client_per_branch(self,value):		
		'''
		writing distributed DHCP Scopes Client Per Branch in  textbox 'Option Value'
		'''	
		logger.debug("DHCP Page :Write  DHCP Client Per Branch  into the text-box")
		self.client_per_branch.set(value)		
		
	def set_distributed_dhcp_reserve_first(self,value):		
		'''
		writing distributed DHCP Scopes Reserve First in  textbox 'Option Value'
		'''	
		logger.debug("DHCP Page :Write  DHCP Reserve First  into the text-box")
		self.reserve_first.set(value)				

	def set_distributed_dhcp_reserve_last(self,value):		
		'''
		writing distributed DHCP Scopes Reserve Last in  textbox 'Option Value'
		'''	
		logger.debug("DHCP Page :Write  DHCP Reserve Last  into the text-box")
		self.reserve_last.set(value)	

	def click_on_distributed_dhcp_finish_button(self):
		'''
		clicking on Distributed dhcp Finish button
		'''
		logger.debug("DHCP Page : Clicking on 'FINISH' button...")
		self.finish_button.click()
		self.buy_time()

	def delete_distributed_dhcp_scope_if_present(self):
		'''
		deleting Distributed dhcp scope
		'''
		logger.debug("DHCP Page : Deleting Distributed_dhcp if present...")
		if self.delete_dhcp:
			self.buy_time()
			self.delete_dhcp.click()
			self.browser.accept_alert()
			self.buy_time()
			self.browser.refresh()
			self.buy_time()
			
	def click_on_dhcp_distributed_add_new_ip_range(self):
		'''
		clicking on Distributed dhcp plus button 
		'''
		logger.debug("DHCP Page : Clicking on '+' button to add new_ip_range...")
		self.dhcp_distributed_add_new_ip_range.click()
		self.buy_time()
		
	def set_distributed_dhcp_ipaddress_range_start_one(self,value):		
		'''
		writing distributed DHCP Scopes IpAddress Range Start  in  textbox 'IpAddress Range'
		'''	
		logger.debug("DHCP Page :Write  DHCP IpAddress Range  into the text-box")
		self.distributed_ip_start_one.set(value)	
	
	def set_distributed_dhcp_ipaddress_range_end_one(self,value):		
		'''
		writing distributed DHCP Scopes IpAddress Range End  in  textbox 'IpAddress Range'
		'''	
		logger.debug("DHCP Page :Write  DHCP IpAddress Range  into the text-box")
		self.distributed_ip_end_one.set(value)	
			
	def click_centralize_accordion(self):
		'''
			Clicking on the Centralize Accordion
		'''
		logger.debug("Clicking on the Centralize Accordion")
		self.centralize_accordion.click()
		time.sleep(5)
	
	def click_ok(self):
		'''
			Clicking on OK button
		'''
		self.buy_time()
		logger.debug("DHCP Page : Clicking on 'OK' button...")
		self.centralize_ok.click()
		self.buy_time()
		
		
	def setting_centralize_name(self,value=None):
		'''
			Setting the Centralize DHCP Scope Name
		'''
		logger.debug('DHCP Page : Setting the DHCP Name')
		if value:
			self.centralized_name.set(value)
		else:
			self.centralized_name.set("")
	
	def set_centralize_vlan_id(self,value=None):
		logger.debug('DHCP Page : Setting the DHCP vlan_id')
		if value:
			self.centralized_vlan.set(value)
		else:
			self.centralized_vlan.set("")
	
	def clicking_centralize_dhcp_relay(self):
		'''
			Clicking DHCP Replay checkbox
		'''
		logger.debug('DHCP Page : Clicking on relay...')
		self.dhcp_relay.click()
	
	def set_helper_address_value(self,value=None):
		logger.debug('DHCP Page : Setting the DHCP helper_address_value')
		if value:
			self.centralized_helper_address.set(value)
		else:
			self.centralized_helper_address.set("")
	
	def set_vlan_ip_value(self,value=None):
		logger.debug('DHCP Page : Setting the DHCP vlan_ip')
		if value:
			self.centralized_vlanIp.set(value)
		else:
			self.centralized_vlanIp.set("")
		
	def set_vlan_mask_value(self,value=None):
		logger.debug('DHCP Page : Setting the DHCP vlan_netmask')
		if value:
			self.centralized_vlan_mask.set(value)
		else:
			self.centralized_vlan_mask.set("")
		
	def select_option82_value(self,value=None):
		logger.debug('DHCP Page : Setting the DHCP Option_Value')
		if value == "Alcatel":
			self.centralized_option82.set(self.config.config_vars.option_82_alcatel)
		else:
			self.centralized_option82.set(self.config.config_vars.none_default_value)
	
	
	def assert_centralize_name_error(self,value=None):
		logger.debug('DHCP Page : Asserting centralize_name error message')
		if value == 'required' :
			if not self.centralize_name_error:
				raise AssertionError("Field Require error message not shown for DHCP Name ")
		if value == 'maxlength':
			if not self.centralize_name_max_error:
				raise AssertionError("Maximum Character error message not shown for DHCP Name ")
		
	def assert_centralize_vlan_id_error(self,value=None):
		logger.debug('DHCP Page : Asserting centralize_vlan_id error message')
		if value == 'required' :
			if not self.centralize_vlan_error:
				raise AssertionError("Field Require error message not shown for VLAN ID ")
		if value == 'reserved':
			if not self.centralize_vlan_reserved_error:
				raise AssertionError(" VLAN id reserved error message not shown for VLAN ID ")
				
	def delete_centralized_dhcp(self):
		'''
		Deletes the centralized dhcp
		'''
		logger.debug("DhcpPage : Clicking Delete icon")
		#self.delete_centralized_dhcp_button.click()
		self.delete_centralized_dhcp_button.click()
		time.sleep(4)
		self.browser.accept_alert()
		time.sleep(5)
		
	def assert_centralized_dhcp(self):
		'''
		Asserts centralized_dhcp
		'''
		logger.debug("DhcpPage : Asserting centralized dhcp")
		if self.delete_centralized_dhcp_button:
			raise AssertionError(" Centralized dhcp is not deleted .Traceback: %s " %traceback.format_exc())
		time.sleep(2)
		
	def create_new_centralized_dhcp(self):
		'''
		Clicks on 'NEW' button tp create new centralized dhcp
		'''
		logger.debug("DhcpPage : Clicking on 'NEW' button")
		self.centralize_new.click()
		time.sleep(3)
		
	def go_to_local_dhcp_scopes_accordion(self):
		'''
		clicks on local dhcp accordion
		'''
		logger.debug('DhcpPage : Clicking on local dhcp accordion')
		self.local_dhcp_scopes_accordion.click()
	  
	def create_new_local_dhcp(self):
		'''
		clicks on new button
		'''
		logger.debug('DhcpPage :clicking on new button')
		self.new_local_dhcp.click()
	  
	def assert_default_local_dhcp_type(self):
		'''
		asserts whether type is set to Local or not 
		'''
		logger.debug('DhcpPage :Asserting default local_dhcp_type')
		if not self.local_dhcp_type.get_selected() == 'Local':
			raise AssertionError("Type is not set to Local")
	   
	def save_local_dhcp_settings(self):
		'''
		clicks on ok button
		'''
		logger.debug('DhcpPage :clicking on Save button')
		self.local_dhcp_ok.click()
	  
	def assert_local_dhcp_name_error_message(self,value):
		'''
		asserts error messages
		'''
		logger.debug('DhcpPage :Asserting invalid local_dhcp_name error')
		if value == 'invalid':
			if not self.local_dhcp_name_req_field_error or not self.name_max_length_error:
				raise AssertionError("DHCP : Invalid input is accepted.Traceback: %s " %traceback.format_exc())
		else :
			if self.local_dhcp_name_req_field_error:
				raise AssertionError("DHCP : valid input is not accepted.Traceback: %s " %traceback.format_exc())
	   
	def assert_local_dhcp_vlan_error_message(self,value):
		'''
		asserts error messages
		'''
		logger.debug('DhcpPage :Asserting invalid local_dhcp_vlan error')
		if value == 'invalid':
			if not (self.local_dhcp_vlan_range_error or self.local_dhcp_vlan_3333):
				raise AssertionError("DHCP : Invalid input is accepted.Traceback: %s " %traceback.format_exc())
		else :
			if self.local_dhcp_vlan_range_error:
				raise AssertionError("DHCP : valid input is not accepted.Traceback: %s " %traceback.format_exc())

	def assert_local_dhcp_network_error_message(self,value):
		'''
		asserts error messages
		'''
		logger.debug('DhcpPage :Asserting invalid local_dhcp_network error')
		if value == 'invalid':
			if not self.local_dhcp_network_invalid_error:
				raise AssertionError("DHCP : Invalid input is accepted.Traceback: %s " %traceback.format_exc())
		else :
			if self.local_dhcp_network_invalid_error:
				raise AssertionError("DHCP : valid input is not accepted.Traceback: %s " %traceback.format_exc())

	def assert_local_dhcp_netmask_error_message(self,value):
		'''
		asserts error messages
		'''
		logger.debug('DhcpPage :Asserting invalid local_dhcp_netmask error')
		if value == 'invalid':
			if not self.local_dhcp_netmask_req_error:
				raise AssertionError("DHCP : Invalid input is accepted.Traceback: %s " %traceback.format_exc())
		else :
			if self.local_dhcp_netmask_req_error:
				raise AssertionError("DHCP : valid input is not accepted.Traceback: %s " %traceback.format_exc())
				
	def assert_local_dhcp_dns_server_error_message(self):
		'''
		asserts error messages
		'''
		logger.debug('DhcpPage :Asserting invalid local_dhcp_dns_server error')
		logger.debug(self.local_dhcp_dns_server_error)
		if not self.local_dhcp_dns_server_error:
			raise AssertionError("DHCP : Invalid input is accepted.Traceback: %s " %traceback.format_exc())
			
	def assert_local_dhcp_domain_error_message(self):
		'''
		asserts error messages
		'''
		logger.debug('DhcpPage :Asserting invalid local_dhcp_domain error')
		if not self.local_dhcp_domain_name_error:
			raise AssertionError("DHCP : Invalid input is accepted.Traceback: %s " %traceback.format_exc())
			
	def assert_local_dhcp_excluded_error_message(self):
		'''
		asserts error messages
		'''
		logger.debug('DhcpPage :Asserting invalid local_dhcp_excluded error')
		if not (self.local_dhcp_excluded  or self.local_dhcp_exclud_ip_range_error):
			raise AssertionError("DHCP : Invalid input is accepted.Traceback: %s " %traceback.format_exc())
		
	def set_local_dhcp_name(self,name):
		'''
		writes given name into name field
		'''
		logger.debug('DhcpPage :Setting dhcp name')
		self.local_dhcp_name.set(name)
	  
	def assert_local_dhcp_validation_error_message(self):
		self.assert_local_dhcp_name_error_message('invalid')
		self.assert_local_dhcp_vlan_error_message('invalid')
		self.assert_local_dhcp_network_error_message('invalid')
		self.assert_local_dhcp_netmask_error_message('invalid')
	  
	def set_local_dhcp_type(self,option):
		'''
		selects option for type field
		'''
		logger.debug("DhcpPage :Setting dhcp_type to : '%s'"%option)
		self.local_dhcp_type.set(option)
		
	def set_local_dhcp_vlan(self,vlan_value):
		'''
		Enters the local_dhcp vlan value
		'''
		logger.debug("DhcpPage : Entering dhcp vlan value to : '%s'"%vlan_value)
		self.local_dhcp_vlan.set(vlan_value)
		time.sleep(2)

	def set_local_dhcp_network(self,network_value):
		'''
		Enters the local_dhcp network value
		'''
		logger.debug("DhcpPage : Entering dhcp network value to : '%s'"%network_value)
		self.local_dhcp_network.set(network_value)
		time.sleep(2)

	def set_local_dhcp_netmask(self,netmask_value):
		'''
		Enters the local_dhcp netmask value
		'''
		logger.debug("DhcpPage : Entering dhcp netmask value to : '%s'"%netmask_value)
		self.local_dhcp_netmask.set(netmask_value)
		time.sleep(2)

	def set_local_dhcp_excluded_address(self,excluded_value):
		'''
		Enters the local_dhcp excluded_address value
		'''
		logger.debug("DhcpPage : Entering dhcp excluded_address value to : '%s'"%excluded_value)
		self.local_dhcp_excluded_address.set(excluded_value)
		time.sleep(2)	

	def set_local_dhcp_dns_server(self,dns_value):
		'''
		Enters the local_dhcp dns_server value
		'''
		logger.debug("DhcpPage : Entering dhcp dns_server value to : '%s'"%dns_value)
		self.local_dhcp_dns_server.set(dns_value)
		time.sleep(2)

	def set_local_dhcp_domain_name(self,domain_value):
		'''
		Enters the local_dhcp domain_name value
		'''
		logger.debug("DhcpPage : Entering dhcp domain_name value value to : '%s'"%domain_value)
		self.local_dhcp_domain_name.set(domain_value)
		time.sleep(2)
		
	# def set_local_dhcp_option(self,option_value):
		# '''
		# Enters the local_dhcp option value
		# '''
		# logger.debug("DhcpPage : Entering dhcp option value")
		# self.local_dhcp_option.set(option_value)
		# time.sleep(2)
		
	def set_local_dhcp_lease_time(self,lease_value):
		'''
		Enters the local_dhcp lease time value
		'''
		logger.debug("DhcpPage : Entering dhcp lease time value to : '%s'"%lease_value)
		self.local_dhcp_lease_time.set(lease_value)
		time.sleep(2)
		
	def set_local_dhcp_option_type_and_value(self,option_type,option_value):
		'''
		Enters the local_dhcp option type and value
		'''
		logger.debug("DhcpPage : Entering dhcp option type and value")
		self.local_dhcp_option_type.set(option_type)
		self.local_dhcp_option_value.set(option_value)
		time.sleep(2)
		
	def assert_edit_button_and_click(self):
		'''
		Assert the Edit button and click on it
		'''
		logger.debug("DhcpPage : assert_edit_button_and_click : Checking the edit button and clicking on it.")
		if not self.dhcp_edit_button:
			raise AssertionError("DHCP Page : Edit button is not Present!!!! .Traceback: %s " %traceback.format_exc())
		self.dhcp_edit_button.click()
		time.sleep(2)

	def delete_and_accept_alert(self):
		'''
		Delete Dhcp and accept alert!.
		'''
		logger.debug("DhcpPage : delete dhcp  and accept_alert : Click on delete button and accept the alert.")
		if self.dhcp_delete_button:
			self.dhcp_delete_button.click()
			self.browser.accept_alert()
			
	def edit_local_dhcp_scope(self):
		'''
		Clicks edit icon
		'''
		logger.debug("DhcpPage : Clicking on edit icon")
		self.dhcp_edit_button.click()
		time.sleep(4)
		
	def delete_local_scope_and_accept_alert(self, exists=False):
		'''
		Assert the Delete button and accept alert!.
		'''
		logger.debug("DhcpPage : Click on delete button and accept the alert.")
		if self.dhcp_local_scope_delete_button:
			self.dhcp_local_scope_delete_button.click()
			self.browser.accept_alert()
		else:
			raise AssertionError("DHCP Page : Delete button not exists!")
			time.sleep(2)
			
	def assert_local_dhcp_lease_time_error_message(self):
		'''
		asserts error messages
		'''
		logger.debug("DhcpPage : Asserting local_lease_time error.")
		if not self.dhcp_local_lease_time_error:
			raise AssertionError("DHCP Page : Invalid input is accepted.Traceback: %s " %traceback.format_exc())
			
			
	def assert_distributed_dhcp_scopes_network_label(self):
		'''
		Asserting distributed dhcp scopes Network label
		'''
		logger.debug("DhcpPage : Asserting distributed_dhcp_scopes_network_label.")
		self.buy_time()
		if not self.distributed_dhcp_scopes_network_label:
			raise AssertionError("DhcpPage : Network section is not visible in the right pane .Traceback: %s " %traceback.format_exc())
	
	def select_distributed_dhcp_network_type(self,value):
		'''
		selecting distributed dhcp Network Type From the drop-down
		'''
		self.buy_time()
		if value ==  'l2':
			self.network_type.set(self.config.config_vars.Dhcp_Network_Type)
		elif value == 'l3':
			self.network_type.set(self.config.config_vars.Dhcp_Network_Type2)
		
	def assert_distributed_dhcp_netmask_and_default_router(self):
		'''
		Asserting distributed dhcp scopes Netmask and Default router
		'''
		logger.debug("DhcpPage : Asserting distributed_dhcp_netmask_and_default_router.")
		self.buy_time()
		if self.netmask:
			raise AssertionError("DhcpPage : distributed dhcp scopes Netmask is visible  .Traceback: %s " %traceback.format_exc())
		if self.default_router:
			raise AssertionError("DhcpPage : distributed dhcp scopes Default router is  visible .Traceback: %s " %traceback.format_exc())
		
	def assert_distributed_dhcp_vlan_error(self,assert_error):
		'''
		Asserting Distributed Dhcp Vlan Error
		'''
		logger.debug("DhcpPage : Asserting distributed_dhcp_vlan_error.")
		self.buy_time()
		if assert_error == True:
			if not self.vlan_error:
				raise AssertionError("DhcpPage : Accepting invalid range for Vlan  .Traceback: %s " %traceback.format_exc())
		elif assert_error == False:
			if self.vlan_error:
				raise AssertionError("DhcpPage : Vlan Must be number in range 1-4093  .Traceback: %s " %traceback.format_exc())
			
		
	def assert_distributed_dhcp_netmask_error(self,assert_error):
		'''
		Asserting Distributed Dhcp Netmask Error
		'''
		logger.debug("DhcpPage : Asserting distributed_dhcp_Netmask_error.")
		self.buy_time()
		if assert_error == True:
			if not self.netmask_error:
				raise AssertionError("DHCP Page :Accepting invalid   Netmask  .Traceback: %s " %traceback.format_exc())
		elif assert_error == False:
			if self.netmask_error:
				raise AssertionError("DHCP Page :Invalid Netmask  .Traceback: %s " %traceback.format_exc())
				
		
	def assert_distributed_dhcp_scopes_vlan_error(self,assert_error):
		'''
		Asserting Distributed Dhcp reserved Vlan Error
		'''
		logger.debug("DhcpPage : Asserting distributed_dhcp_vlan_error.")
		self.buy_time()
		if assert_error == True:
			if not self.distributed_dhcp_scopes_vlan_error:
				raise AssertionError("DHCP Page :Accepting invalid range for Vlan  .Traceback: %s " %traceback.format_exc())
		elif assert_error == False:
			if self.distributed_dhcp_scopes_vlan_error:
				raise AssertionError("DHCP Page : VLAN 3333 is reserved  .Traceback: %s " %traceback.format_exc())	
	
	def assert_distributed_dhcp_dns_server_error(self,assert_error):
		'''
		Asserting Distributed Dhcp Dns Server Error
		'''
		logger.debug("DhcpPage : Asserting distributed_dhcp_DNS_server_error.")
		self.buy_time()
		if assert_error == True:
			if not self.dhcp_dns_server_error:
				raise AssertionError("DHCP Page : Accepting invalid  IP address .Traceback: %s " %traceback.format_exc())     
		elif assert_error == False:	
			if self.dhcp_dns_server_error:
				raise AssertionError("DHCP Page : * Invalid IP address .Traceback: %s " %traceback.format_exc())  
				
	def assert_distributed_dhcp_domain_name_error(self,assert_error):	
		'''
		Asserting Distributed Dhcp Domain Name Error
		'''	
		logger.debug("DhcpPage : Asserting distributed_dhcp_Domain_name_error.")
		self.buy_time()
		if assert_error == True:
			if not self.domain_name_error:
				raise AssertionError("DHCP Page :Accepting invalid domain name .Traceback: %s " %traceback.format_exc())
		if assert_error == False:
			if  self.domain_name_error:
				raise AssertionError("DHCP Page :Invalid domain name .Traceback: %s " %traceback.format_exc())
				
	def set_distributed_dhcp_lease_time(self,value):		
		'''
		writing distributed DHCP Scopes Lease Time in  textbox 'Option Value'
		'''	
		self.buy_time()
		if value:
			logger.debug("DHCP Page :Setting  DHCP Reserve Last  into the text-box")
			self.lease_time.set(value)	
		else:
			logger.debug("DHCP Page :Setting Default DHCP Reserve Last  into the text-box")
			self.lease_time.set(self.config.config_vars.distributed_dhcp_default_lease_time_value)			
				
	def assert_distributed_dhcp_lease_time_error(self,assert_error):	
		'''
		Asserting Distributed Dhcp Lease Time Error
		'''	
		logger.debug("DhcpPage : Asserting distributed_dhcp_Lease_time_error.")
		self.buy_time()
		if assert_error == True:
			if not self.distributed_dhcp_scopes_lease_time__error:
				raise AssertionError("DHCP Page : Accepting invalid Lease Time .Traceback: %s " %traceback.format_exc())
		if assert_error == False:
			if  self.distributed_dhcp_scopes_lease_time__error:
				raise AssertionError("DHCP Page : * Must be number in range is 2-1440 .Traceback: %s " %traceback.format_exc())			
			
	def assert_distributed_dhcp_ip_address_range_error(self,assert_error):	
		'''
		Asserting Distributed Ip address range Time Error
		'''
		logger.debug("DhcpPage : Asserting distributed_dhcp_IP_address_range_error.")
		self.buy_time()
		if assert_error == True:
			if not self.distributed_dhcp_scopes_ip_error:
				raise AssertionError("DHCP Page : Accepting End IP which is greater than Start .Traceback: %s " %traceback.format_exc())
		if assert_error == False:
			if  self.distributed_dhcp_scopes_ip_error:
				raise AssertionError("DHCP Page : * End IP should be greater than Start IP .Traceback: %s " %traceback.format_exc()) 
				
	def set_distributed_dhcp_ipaddress_range_start_two(self,value):		
		'''
		writing distributed DHCP Scopes IpAddress Range Start  in  textbox 'IpAddress Range'
		'''	
		self.buy_time()
		logger.debug("DHCP Page :Write  DHCP IpAddress Range  into the text-box")
		self.distributed_ip_start_two.set(value)	

	def set_distributed_dhcp_ipaddress_range_end_two(self,value):		
		'''
		writing distributed DHCP Scopes IpAddress Range End  in  textbox 'IpAddress Range'
		'''	
		self.buy_time()
		logger.debug("DHCP Page :Write  DHCP IpAddress Range  into the text-box")
		self.distributed_ip_end_two.set(value)

	def set_distributed_dhcp_ipaddress_range_start_three(self,value):		
		'''
		writing distributed DHCP Scopes IpAddress Range Start  in  textbox 'IpAddress Range'
		'''	
		self.buy_time()
		logger.debug("DHCP Page :Write  DHCP IpAddress Range  into the text-box")
		self.distributed_ip_start_three.set(value)	

	def set_distributed_dhcp_ipaddress_range_end_three(self,value):		
		'''
		writing distributed DHCP Scopes IpAddress Range End  in  textbox 'IpAddress Range'
		'''	
		self.buy_time()
		logger.debug("DHCP Page :Write  DHCP IpAddress Range  into the text-box")
		self.distributed_ip_end_three.set(value)	
			
	def assert_distributed_dhcp_option_type_error(self,assert_error):	
		'''
		Asserting Distributed Option Type Time Error
		'''
		logger.debug("DhcpPage : Asserting distributed_dhcp_Option_type_error.")
		self.buy_time()		
		if assert_error == True:
			if not self.option_type_error:
				raise AssertionError("  Accepting invalid value for  Option Type .Traceback: %s " %traceback.format_exc())
		if assert_error == False:
			if  self.option_type_error:
				raise AssertionError("  Valid range is 1-254.Traceback: %s " %traceback.format_exc())
				
	def validating_branch_size_and_static_ip(self):	
		conf=self.config.config_vars
		if not self.client_per_branch:
			logger.debug("DhcpPage : Clicking on 'NEXT' button.")
			self.click_on_next_button()
		self.set_distributed_dhcp_client_per_branch(conf.Client_Per_Branch_invalid)
		logger.debug("DhcpPage : Clicking on 'NEXT' button.")
		self.click_on_next_button()
		if not self.distributed_dhcp_client_per_branch_error:
			raise AssertionError("  Accepting inValid range .Traceback: %s " %traceback.format_exc())
		self.set_distributed_dhcp_client_per_branch(conf.Client_Per_Branch)
		logger.debug("DhcpPage : Clicking on 'NEXT' button.")
		self.click_on_next_button()
		if not self.reserve_first:
			logger.debug("DhcpPage : Clicking on 'NEXT' button.")
			self.click_on_next_button()
		logger.debug("DhcpPage : Setting Client_Per_Branch1.")
		self.set_distributed_dhcp_reserve_first(conf.Client_Per_Branch1)
		self.set_distributed_dhcp_reserve_last(conf.Client_Per_Branch1)
		logger.debug("DhcpPage : Clicking on 'FINISH' button.")
		self.click_on_distributed_dhcp_finish_button()
		if not self.dist_reverse_range_error:
			raise AssertionError("  Accepting inValid range .Traceback: %s " %traceback.format_exc())
		if not self.dist_reverse_last_range_error:
			raise AssertionError("  Accepting inValid range .Traceback: %s " %traceback.format_exc())
		logger.debug("DhcpPage : Setting distributed_dhcp_reserve.")
		self.set_distributed_dhcp_reserve_first(conf.Reserve_Last)
		logger.debug("DhcpPage : Clicking on 'FINISH' button.")
		self.click_on_distributed_dhcp_finish_button()
		logger.debug("DhcpPage : Setting distributed_dhcp_reserve.")
		self.set_distributed_dhcp_reserve_last(conf.Reserve_Last)
		
	def validate_distributed_dhcp_ip_range_and_lease_time(self):
		conf=self.config.config_vars
		logger.debug("DhcpPage : Setting IP_Address_Range values.")
		self.set_distributed_dhcp_ipaddress_range_start(conf.distributed_dhcp_ipaddress_range_end)
		self.set_distributed_dhcp_ipaddress_range_end(conf.distributed_dhcp_ipaddress_range_start)
		logger.debug("DhcpPage : Clicking on 'NEXT' button.")
		self.click_on_next_button()
		self.assert_distributed_dhcp_lease_time_error(True)
		logger.debug("DhcpPage : Setting lease_time value.")
		self.set_distributed_dhcp_lease_time(conf.lease_time_value)
		logger.debug("DhcpPage : Clicking on 'NEXT' button.")
		self.click_on_next_button()
		self.assert_distributed_dhcp_ip_address_range_error(True)
		self.set_distributed_dhcp_ipaddress_range_start(conf.distributed_dhcp_ipaddress_range_start)
		self.set_distributed_dhcp_ipaddress_range_end(conf.distributed_dhcp_ipaddress_range_end)
		self.click_on_dhcp_distributed_add_new_ip_range()
		self.set_distributed_dhcp_ipaddress_range_start_one(conf.distributed_dhcp_ipaddress_range_start1)
		self.set_distributed_dhcp_ipaddress_range_end_one(conf.distributed_dhcp_ipaddress_range_end1)
		self.dhcp_distributed_add_new_ip_range1.click()
		self.set_distributed_dhcp_ipaddress_range_start_two(conf.distributed_dhcp_ipaddress_range_start2)
		self.set_distributed_dhcp_ipaddress_range_end_two(conf.distributed_dhcp_ipaddress_range_end2)
		self.dhcp_distributed_add_new_ip_range2.click()
		self.set_distributed_dhcp_ipaddress_range_start_three(conf.distributed_dhcp_ipaddress_range_start3)
		self.set_distributed_dhcp_ipaddress_range_end_three(conf.distributed_dhcp_ipaddress_range_end3)
		
	def create_distributed_dhcp_with_type_l2_and_l3(self,type):
		conf=self.config.config_vars
		logger.debug("DhcpPage : Clicking on 'NEW' button.")
		self.click_on_distributed_dhcp_scopes_new()
		if type == 'l3':
			self.set_distributed_dhcp_usrname(conf.distributed_dhcp_name)
			self.select_distributed_dhcp_network_type('l3')
		logger.debug("DhcpPage : Setting dhcp_vlan.")
		self.set_distributed_dhcp_vlan(conf.distributed_dhcp_vlan)
		if type == 'l2':
			logger.debug("DhcpPage : Setting dhcp_name.")
			self.set_distributed_dhcp_usrname(conf.valid_distributed_dhcp_name)
			logger.debug("DhcpPage : Setting dhcp_Netmask.")
			self.set_distributed_dhcp_netmask(conf.Dhcp_Netmask)
			logger.debug("DhcpPage : Setting dhcp_Default_Router.")
			self.set_distributed_dhcp_default_router(conf.distributed_dhcp_default_router)
		logger.debug("DhcpPage : Setting dhcp_DNS_server.")
		self.set_distributed_dhcp_dns_server(conf.distributed_dhcp_dns_server)
		logger.debug("DhcpPage : Setting dhcp_name.")
		self.set_distributed_dhcp_domain_name(conf.distributed_dhcp_domain_name)
		logger.debug("DhcpPage : Setting dhcp_IP_address_range values.")
		self.set_distributed_dhcp_ipaddress_range_start(conf.distributed_dhcp_ipaddress_range_start)
		self.set_distributed_dhcp_ipaddress_range_end(conf.distributed_dhcp_ipaddress_range_end)
		logger.debug("DhcpPage : Setting dhcp_Option_type and Option_value.")
		self.set_distributed_dhcp_option_type(conf.Distributed_Option_Type)
		self.set_distributed_dhcp_option_value(conf.Distributed_Option_Value)
		logger.debug("DhcpPage : Clicking on 'NEXT' button.")
		self.click_on_next_button()
		logger.debug("DhcpPage : Setting dhcp_Client_Per_Branch.")
		self.set_distributed_dhcp_client_per_branch(conf.Client_Per_Branch)
		logger.debug("DhcpPage : Clicking on 'NEXT' button.")
		self.click_on_next_button()
		logger.debug("DhcpPage : Setting dhcp_Reserve.")
		self.set_distributed_dhcp_reserve_first(conf.Reserve_Last)
		self.set_distributed_dhcp_reserve_last(conf.Reserve_First)
		logger.debug("DhcpPage : Clicking on 'FINISH' button.")
		self.click_on_distributed_dhcp_finish_button()
	
	def validate_distributed_dhcp_vlan_dns_domain_lease_fields(self):
		conf=self.config.config_vars
		logger.debug("DhcpPage : Setting distributed_dhcp_vlan value.")
		self.set_distributed_dhcp_vlan(conf.invalid_distributed_dhcp_vlan)
		logger.debug("DhcpPage : Setting distributed_dhcp_Server value.")
		self.set_distributed_dhcp_dns_server(conf.invalid_dhcp_dns_server)
		logger.debug("DhcpPage : Setting distributed_dhcp_domain_name value.")
		self.set_distributed_dhcp_domain_name(conf.valid_distributed_dhcp_domain_name)
		logger.debug("DhcpPage : Clicking on 'NEXT' button.")
		self.click_on_next_button()
		self.assert_distributed_dhcp_vlan_error(True)
		logger.debug("DhcpPage : Setting distributed_dhcp_vlan_id as 3333")
		self.set_distributed_dhcp_vlan(conf.vlan_id_3333)
		self.assert_distributed_dhcp_dns_server_error(True)
		logger.debug("DhcpPage : Setting distributed_dhcp_dns_server value.")
		self.set_distributed_dhcp_dns_server(conf.distributed_dhcp_dns_server)
		logger.debug("DhcpPage : Clicking on 'NEXT' button.")
		self.click_on_next_button()
		self.assert_distributed_dhcp_scopes_vlan_error(True)
		logger.debug("DhcpPage : Setting distributed_dhcp_vlan value.")
		self.set_distributed_dhcp_vlan(conf.distributed_dhcp_vlan)
		logger.debug("DhcpPage : Clicking on 'NEXT' button.")
		self.click_on_next_button()
		self.assert_distributed_dhcp_domain_name_error(False)
		logger.debug("DhcpPage : Setting distributed_dhcp_domain_name value.")
		self.set_distributed_dhcp_domain_name(conf.distributed_dhcp_domain_name)
		logger.debug("DhcpPage : Setting distributed_dhcp_Lease_time.")
		self.set_distributed_dhcp_lease_time(conf.Dhcp_Lease_Time_Error)
		
		
	def click_on_distributed_edit_dhcp_button(self):
		'''
		clicking on edit button
		'''
		self.buy_time()
		self.edit.click()
		self.buy_time()
		
	def assert_helper_address_error(self):
		logger.debug("DhcpPage : Asserting helper_address_error.")
		if not self.helper_address_error:
			raise AssertionError("DHCP: Helper address error message not shown. ")
	
	
	def assert_centralized_L3_scope_40(self):
		logger.debug("DhcpPage : creating new centralized_L3_scope.")
		self.create_new_centralized_dhcp()
		self.click_ok()
		self.assert_centralize_name_error('required')
		self.assert_centralize_vlan_id_error('required')
		self.setting_centralize_name(self.config.config_vars.centralized_dhcp_name_special_char)
		import time
		time.sleep(5)
		self.browser.key_press(u'\ue004')
		import time
		time.sleep(5)
		logger.debug("Woke Up -- Balaajee")
		if self.centralize_name_error:
			raise AssertionError("Field Require error message shown for DHCP Name ")
		if self.centralize_name_max_error:
			raise AssertionError("Maximum Character error message shown for DHCP Name ")
		self.setting_centralize_name(self.config.config_vars.dhcp_name_invalid_2)
		self.click_ok()
		self.assert_centralize_name_error('maxlength')
		self.set_centralize_vlan_id(self.config.config_vars.vlan_id_invalid)
		self.click_ok()
		self.assert_centralize_vlan_id_error('required')
		self.set_centralize_vlan_id(self.config.config_vars.vlan_id_3333)
		self.click_ok()
		self.assert_centralize_vlan_id_error('reserved')
		self.set_centralize_vlan_id(self.config.config_vars.vlan_id)
		self.click_ok()
		if self.centralize_vlan_error:
			raise AssertionError("Field Require error message shown for VLAN ID ")
		if self.centralize_vlan_reserved_error:
			raise AssertionError(" VLAN id 3333 reserved error message shown for VLAN ID ")
		if self.dhcp_relay.is_selected():
			raise AssertionError("DHCP : DHCP Relay checkbox is check")
		self.clicking_centralize_dhcp_relay()
		if not self.centralized_helper_address and not self.centralized_vlanIp and not self.centralized_vlan_mask:
			raise AssertionError("DHCP : Helper Address, Vlan ip and vlan mask fields are not visible")
		self.set_helper_address_value(self.config.config_vars.Dhcp_Dns_Server_Error)
		self.click_ok()
		self.assert_helper_address_error()
		self.set_helper_address_value(self.config.config_vars.local_dhcp_dns_server_valid_2)
		self.click_ok()
		if self.helper_address_error:
			raise AssertionError("DHCP: Helper address error message shown. ")
		self.set_vlan_ip_value(self.config.config_vars.Dhcp_Dns_Server_Error)
		self.set_vlan_mask_value(self.config.config_vars.Dhcp_Dns_Server_Error)
		self.click_ok()
		if not self.centralize_vlan_ip_error and not self.centralize_vlan_mask_error:
			raise AssertionError("DHCP: Error message not shown for vlan ip and vlan mask")
		self.set_vlan_ip_value(self.config.config_vars.dhcp_network_address)
		self.set_vlan_mask_value(self.config.config_vars.edit_Dhcp_Netmask)
		self.click_ok()
		if self.centralize_vlan_ip_error and self.centralize_vlan_mask_error:
			raise AssertionError("DHCP: Error message shown for vlan ip and vlan mask")
		if not self.centralized_option82.get_selected() == 'None':
			raise AssertionError("DHCP: Option 82 not set to default value 'None'")
		self.select_option82_value('Alcatel')
		self.setting_centralize_name(self.config.config_vars.dhcp_name_new)
		self.click_ok()
		
	def delete_centralize_dhcp_if_present(self):
		'''
		DhcpPage : Deletes centralized_dhcp if present...
		'''
		logger.debug("DhcpPage : Deleting Centralized_dhcp if present.")
		if self.centralize_dhcp_name:
			self.centralize_dhcp_name.click()
			self.delete_centralized_dhcp()
			self.browser.refresh()
		self.buy_time()
		
	def edit_centralized_dhcp_icon_click(self):
		'''
		DhcpPage : Clicks on edit icon in centralized dhcp.
		'''
		if self.centralized_dhcp_edit_icon:
			logger.debug("DhcpPage : Clicking on edit icon.")
			self.centralized_dhcp_edit_icon.click()
			self.buy_time()
			
	def click_centralize_dhcp_relay(self,value=False):
		'''
		DhcpPage : Check or uncheck dhcp_delay checkbox.
		'''
		if value:
			if not self.dhcp_relay.is_selected():
				logger.debug('DHCP Page : Checking dhcp_relay checkbox...')
				self.dhcp_relay.click()
		else:
			if self.dhcp_relay.is_selected():
				logger.debug('DHCP Page : Unchecking dhcp_relay checkbox...')
				self.dhcp_relay.click()
				
				
	def assert_centralized_L3_scope_30(self):
		self.create_new_centralized_dhcp()
		self.assert_new_centralized_dhcp_scopes()
		self.click_ok()
		self.assert_centralize_name_error('required')
		self.assert_centralize_vlan_id_error('required')
		self.setting_centralize_name(self.config.config_vars.centralized_dhcp_name_special_char)
		self.browser.key_press(u'\ue004')
		if self.centralize_name_error:
			raise AssertionError("Field Require error message shown for DHCP Name ")
		if self.centralize_name_max_error:
			raise AssertionError("Maximum Character error message shown for DHCP Name ")
		self.setting_centralize_name(self.config.config_vars.dhcp_name_invalid_2)
		self.click_ok()
		self.assert_centralize_name_error('maxlength')
		self.set_centralize_vlan_id(self.config.config_vars.vlan_id_5000)
		self.click_ok()
		self.assert_centralize_vlan_id_error('required')
		self.set_centralize_vlan_id(self.config.config_vars.zero_preceded_value)
		self.click_ok()
		self.assert_centralize_vlan_id_error('required')
		self.set_centralize_vlan_id(self.config.config_vars.vlan_id_3333)
		self.click_ok()
		self.assert_centralize_vlan_id_error('reserved')
		self.set_centralize_vlan_id(self.config.config_vars.vlan_id)
		self.click_ok()
		if self.centralize_vlan_error:
			raise AssertionError("Field Require error message shown for VLAN ID ")
		if self.centralize_vlan_reserved_error:
			raise AssertionError(" VLAN id 3333 reserved error message shown for VLAN ID ")
		if self.dhcp_relay.is_selected():
			raise AssertionError("DHCP : DHCP Relay checkbox is check")
		self.clicking_centralize_dhcp_relay()
		if not self.centralized_helper_address and not self.centralized_vlanIp and not self.centralized_vlan_mask:
			raise AssertionError("DHCP : Helper Address, Vlan ip and vlan mask fields are not visible")
		self.set_helper_address_value(self.config.config_vars.incomplete_helper_address)
		self.click_ok()
		self.assert_helper_address_error()
		self.set_helper_address_value(self.config.config_vars.dhcp_dns_server_valid_1)
		self.click_ok()
		if self.helper_address_error:
			raise AssertionError("DHCP: Helper address error message shown. ")
		self.set_helper_address_value(self.config.config_vars.dhcp_dns_server_invalid_3)
		self.click_ok()
		self.assert_helper_address_error()
		self.set_helper_address_value(self.config.config_vars.dhcp_dns_server_valid_2)
		self.click_ok()
		if self.helper_address_error:
			raise AssertionError("DHCP: Helper address error message shown. ")
		# self.set_vlan_ip_value(self.config.config_vars.Dhcp_Dns_Server_Error)
		# self.set_vlan_mask_value(self.config.config_vars.Dhcp_Dns_Server_Error)
		# self.click_ok()
		# if not self.centralize_vlan_ip_error and not self.centralize_vlan_mask_error:
			# raise AssertionError("DHCP: Error message not shown for vlan ip and vlan mask")
		self.set_vlan_ip_value(self.config.config_vars.dhcp_network_address)
		self.set_vlan_mask_value(self.config.config_vars.edit_Dhcp_Netmask)
		self.click_ok()
		# if self.centralize_vlan_ip_error and self.centralize_vlan_mask_error:
			# raise AssertionError("DHCP: Error message shown for vlan ip and vlan mask")
		if not self.centralized_option82.get_selected() == 'None':
			raise AssertionError("DHCP: Option 82 not set to default value 'None'")
		# self.select_option82_value('Alcatel')
		self.setting_centralize_name(self.config.config_vars.dhcp_name_new)
		self.click_ok()
		
	def assert_new_centralized_dhcp_scopes(self):
		logger.debug("DHCPPage :Checking  By default Name Field is empty or not")
		self.browser.assert_text(self.centralized_name,'','Name Field is not empty','value')
		logger.debug("DHCPPage :Checking  By default Vlan Field is empty or not")
		self.browser.assert_text(self.centralized_vlan,'','Name Field is not empty','value')
		logger.debug("DHCPPage :Checking  By default option82 is set to None ")
		self.browser.assert_drop_down_value(self.centralized_option82,self.config.config_vars.None_option,'Option 82 not set to default value None')
		if self.dhcp_relay.is_selected():
			raise AssertionError("DHCP : DHCP Relay checkbox is not disabled by default")

	def create_local_dhcp_scope(self):
		'''
		creates local dhcp scope
		'''
		self.create_new_local_dhcp()
		self.set_local_dhcp_name(self.config.config_vars.centralized_dhcp_name)
		self.set_local_dhcp_type(self.config.config_vars.local_dhcp_type_local_l3)
		self.set_local_dhcp_vlan(self.config.config_vars.vlan_id)
		self.set_local_dhcp_network(self.config.config_vars.local_dhcp_network)
		self.set_local_dhcp_netmask(self.config.config_vars.local_dhcp_netmask)
		self.set_local_dhcp_excluded_address(self.config.config_vars.local_dhcp_excluded_addr_valid)
		self.set_local_dhcp_dns_server(self.config.config_vars.local_dhcp_excluded_addr_valid)
		self.set_local_dhcp_domain_name(self.config.config_vars.edit_Dhcp_Domain_Name)
		self.set_local_dhcp_lease_time(self.config.config_vars.local_dhcp_lease_time)
		self.set_local_dhcp_option_type_and_value(self.config.config_vars.local_dhcp_option_type,self.config.config_vars.local_dhcp_option_value)
		self.save_local_dhcp_settings()

	def edit_created_local_dhcp_scope(self):
		'''
		creates local dhcp scope
		'''
		self.edit_local_dhcp_scope()
		self.set_local_dhcp_name(self.config.config_vars.edit_dhcp_name_new)
		self.set_local_dhcp_type(self.config.config_vars.local_dhcp_type_local_l3)
		self.set_local_dhcp_vlan(self.config.config_vars.edit_Dhcp_Vlan)
		self.set_local_dhcp_network(self.config.config_vars.edit_dhcp_network_address)
		self.set_local_dhcp_netmask(self.config.config_vars.edit_Dhcp_Netmask)
		self.set_local_dhcp_excluded_address(self.config.config_vars.edit_dhcp_excluded_address)
		self.set_local_dhcp_dns_server(self.config.config_vars.local_dhcp_excluded_addr_valid)
		self.set_local_dhcp_domain_name(self.config.config_vars.edit_Dhcp_Domain_Name)
		self.set_local_dhcp_lease_time(self.config.config_vars.dhcp_lease_time_spl_char)
		self.set_local_dhcp_option_type_and_value(self.config.config_vars.edit_dhcp_option_type,self.config.config_vars.edit_lease_time_value)
		self.save_local_dhcp_settings()

	def create_distributed_dhcp(self,name = None,type = None,vlan = None,nmask = None,router = None,server = None,domain = None,time = None,startip = None,endip = None,optype = None,value = None,clients = None,first = None,last = None):
		'''
		creates distributed dhcp
		'''
		logger.debug("DHCP Page : Setting Dhcp_name...")
		self.network_name.set(name)
		logger.debug("DHCP Page : Setting Dhcp_type...")
		self.network_type.set(type)
		logger.debug("DHCP Page : Setting Dhcp_Vlan...")
		self.vlan_name.set(vlan)
		if nmask :
			logger.debug("DHCP Page : Setting Dhcp_Netmask...")
			self.netmask.set(nmask)
		if 	router:
			logger.debug("DHCP Page : Setting Default_router...")
			self.default_router.set(router)
		if server :
			logger.debug("DHCP Page : Setting DNS_server...")
			self.dns_server.set(server)
		if domain:	
			logger.debug("DHCP Page : Setting Domain_name...")
			self.domain_name.set(domain)
		if time:	
			logger.debug("DHCP Page :Setting Default DHCP Reserve Last  into the text-box")
			self.lease_time.set(time)
			
		logger.debug("DHCP Page : Setting IP_Address_Range...")		
		self.distributed_ip_start.set(startip)
		self.distributed_ip_end.set(endip)
		if optype:
			logger.debug("DHCP Page : Setting Distributed_option_type and option_value...")
			self.distributed_option_type.set(optype)
		if value:	
			self.distributed_option_value.set(value)
		logger.debug("DHCP Page : Clicking 'NEXT' button...")
		self.next_button.click()
		logger.debug("DHCP Page : Setting client_per_branch...")
		self.client_per_branch.set(clients)
		logger.debug("DHCP Page : Clicking 'NEXT' button...")
		self.next_button.click()
		logger.debug("DHCP Page : Setting Reserve field...")
		self.reserve_first.set(first)
		self.reserve_last.set(last)
		logger.debug("DHCP Page : Clicking 'FINISH' button...")
		self.finish_button.click()
		self.browser.refresh()
		self.buy_time()

	def create_centralized_dhcp_scope(self,name = None,vlan = None, relay = False,option82 = None,helper = None,ip = None, mask = None):
		'''
		creates centralized dhcp scope
		'''
		logger.debug('DHCP Page : Setting the DHCP Name')
		self.centralized_name.set(name)
		logger.debug('DHCP Page : Setting the DHCP vlan_id')
		self.centralized_vlan.set(vlan)
		if relay :
			logger.debug('DHCP Page : Clicking on relay...')
			self.dhcp_relay.click()
		if helper:
			logger.debug('DHCP Page : Setting the DHCP helper_address_value')
			self.centralized_helper_address.set(helper)
		if ip:
			logger.debug('DHCP Page : Setting the DHCP vlan_ip')
			self.centralized_vlanIp.set(ip)
		if mask:
			logger.debug('DHCP Page : Setting the DHCP vlan_mask')
			self.centralized_vlan_mask.set(mask)
		self.click_ok()

	def create_local_new_dhcp_scope(self,name = None, type = None, vlan = None,network= None, netmask = None,exaddress = None, server = None,domain = None,time = None,optype = None, value = None):
		if name:
			logger.debug('DhcpPage :Setting dhcp name')
			self.local_dhcp_name.set(name)
		if type:		
			logger.debug("DhcpPage :Setting dhcp_type to : '%s'"%type)
			self.local_dhcp_type.set(type)
		if vlan:	
			logger.debug("DhcpPage : Entering dhcp vlan value to : '%s'"%vlan)
			self.local_dhcp_vlan.set(vlan)
		if network:	
			logger.debug("DhcpPage : Entering dhcp network value to : '%s'"%network)
			self.local_dhcp_network.set(network)
		if netmask:	
			logger.debug("DhcpPage : Entering dhcp netmask value to : '%s'"%netmask)
			self.local_dhcp_netmask.set(netmask)
		if exaddress:	
			logger.debug("DhcpPage : Entering dhcp excluded_address value to : '%s'"%exaddress)
			self.local_dhcp_excluded_address.set(exaddress)
		if server:	
			logger.debug("DhcpPage : Entering dhcp dns_server value to : '%s'"%server)
			self.local_dhcp_dns_server.set(server)
		if domain:	
			logger.debug("DhcpPage : Entering dhcp domain_name value value to : '%s'"%domain)
			self.local_dhcp_domain_name.set(domain)
		if time:	
			logger.debug("DhcpPage : Entering dhcp lease time value to : '%s'"%time)
			self.local_dhcp_lease_time.set(time)
		if optype:	
			logger.debug("DhcpPage : Entering dhcp option type and value")
			self.local_dhcp_option_type.set(optype)
			self.local_dhcp_option_value.set(value)
		self.save_local_dhcp_settings()
		
	def assert_created_centralized_dhcp(self):
		'''
		Asserts Created Centralized dhcp
		'''
		logger.debug("DhcpPage : Asserting centralized dhcp")
		if not self.created_centralized_dhcp_scope:
			raise AssertionError(" Centralized dhcp is not created .Traceback: %s " %traceback.format_exc())
		time.sleep(2)
		
	def create_distributed_l2_scope(self):
		conf=self.config.config_vars
		logger.debug("DHCP Page : Clicking on  'New' button")
		self.click_on_distributed_dhcp_scopes_new()
		logger.debug("DHCP Page :Write  DHCP name into the text-box")
		self.set_distributed_dhcp_usrname(conf.distributed_dhcp_name)
		logger.debug("DHCP Page :Write  DHCP Vlan  into the text-box")
		self.set_distributed_dhcp_vlan(conf.distributed_dhcp_vlan)
		logger.debug("DHCP Page :Write  DHCP NetMask  into the text-box")
		self.set_distributed_dhcp_netmask(conf.Dhcp_Netmask)
		logger.debug("DHCP Page :Write  DHCP Default Router  into the text-box")
		self.set_distributed_dhcp_default_router(conf.distributed_dhcp_default_router)
		logger.debug("DHCP Page :Write  DHCP Dns Server  into the text-box")
		self.set_distributed_dhcp_dns_server(conf.distributed_dhcp_dns_server)
		logger.debug("DHCP Page :Write  DHCP Domain Name  into the text-box")
		self.set_distributed_dhcp_domain_name(conf.distributed_dhcp_domain_name)
		logger.debug("DHCP Page :Write  DHCP IpAddress Range  into the text-box")
		self.set_distributed_dhcp_ipaddress_range_start(conf.distributed_dhcp_ipaddress_range_start)
		logger.debug("DHCP Page :Write  DHCP IpAddress Range  into the text-box")
		self.set_distributed_dhcp_ipaddress_range_end(conf.distributed_dhcp_ipaddress_range_end)
		logger.debug("DHCP Page : Clicking on '+' button to add new_ip_range...")
		self.click_on_dhcp_distributed_add_new_ip_range()
		logger.debug("DHCP Page :Write  DHCP IpAddress Range  into the text-box")
		self.set_distributed_dhcp_ipaddress_range_start_one(conf.distributed_dhcp_ipaddress_range_start1)
		logger.debug("DHCP Page :Write  DHCP IpAddress Range  into the text-box")
		self.set_distributed_dhcp_ipaddress_range_end_one(conf.distributed_dhcp_ipaddress_range_end1)
		logger.debug("DHCP Page :Write  DHCP Option Type  into the text-box")
		self.set_distributed_dhcp_option_type(conf.Distributed_Option_Type)
		logger.debug("DHCP Page :Write  DHCP Option Value  into the text-box")
		self.set_distributed_dhcp_option_value(conf.Distributed_Option_Value)
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.click_on_next_button()
		logger.debug("DHCP Page :Write  DHCP Client Per Branch  into the text-box")
		self.set_distributed_dhcp_client_per_branch(conf.Client_Per_Branch)
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.click_on_next_button()
		logger.debug("DHCP Page :Write  DHCP Reserve First  into the text-box")
		self.set_distributed_dhcp_reserve_first(conf.Reserve_Last)
		logger.debug("DHCP Page :Write  DHCP Reserve Last  into the text-box")
		self.set_distributed_dhcp_reserve_last(conf.Reserve_First)
		logger.debug("DHCP Page : Clicking on 'FINISH' button...")
		self.click_on_distributed_dhcp_finish_button()
		
	def create_distributed_l3_scope(self):
		conf=self.config.config_vars
		logger.debug("DHCP Page : Clicking on  'New' button")
		self.click_on_distributed_dhcp_scopes_new()
		logger.debug("DhcpPage : Asserting distributed_dhcp_scopes_network_label.")
		self.assert_distributed_dhcp_scopes_network_label()
		logger.debug("DHCP Page :Write  DHCP name into the text-box")
		self.set_distributed_dhcp_usrname(conf.valid_distributed_dhcp_name)
		logger.debug("DHCP Page :Setting DHCP Type into the drop-down")
		self.select_distributed_dhcp_network_type('l3')
		logger.debug("DhcpPage : Asserting distributed_dhcp_netmask_and_default_router.")
		self.assert_distributed_dhcp_netmask_and_default_router()
		logger.debug("DhcpPage : Validating the Distributed Scope fields")
		self.validate_distributed_dhcp_vlan_dns_domain_lease_fields()
		logger.debug("DhcpPage : Validating the ip range and lease time fields")
		self.validate_distributed_dhcp_ip_range_and_lease_time()
		logger.debug("DHCP Page :Write  DHCP Option Type  into the text-box")
		self.set_distributed_dhcp_option_type(conf.Dhcp_Domain_Name_invalid)
		logger.debug("DHCP Page :Write  DHCP Option Value  into the text-box")
		self.set_distributed_dhcp_option_value(conf.invalid_Distributed_Option_Value)
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.click_on_next_button()
		logger.debug("DhcpPage : Asserting distributed_dhcp_Option_type_error.")
		self.assert_distributed_dhcp_option_type_error(True)
		logger.debug("DHCP Page :Write  DHCP Option Type  into the text-box")
		self.set_distributed_dhcp_option_type(conf.centralized_dhcp_name_special_char)
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.click_on_next_button()
		logger.debug("DhcpPage : Asserting distributed_dhcp_Option_type_error.")
		self.assert_distributed_dhcp_option_type_error(True)
		logger.debug("DHCP Page :Write  DHCP Option Value  into the text-box")
		self.set_distributed_dhcp_option_value(conf.Distributed_Option_Value)
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.click_on_next_button()
		logger.debug("DhcpPage : Asserting distributed_dhcp_Option_type_error.")
		self.assert_distributed_dhcp_option_type_error(True)
		logger.debug("DHCP Page :Write  DHCP Option Type  into the text-box")
		self.set_distributed_dhcp_option_type(conf.Distributed_Option_Type)
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.click_on_next_button()
		logger.debug("DhcpPage : Validating the Branch Size and Static ip fields")
		self.validating_branch_size_and_static_ip()
		logger.debug("DHCP Page : Clicking on 'FINISH' button...")
		self.click_on_distributed_dhcp_finish_button()
		
	def delete_distributed_dhcp_if_present(self):
		'''
		deleting Distributed dhcp scope
		'''
		logger.debug("DHCP Page : Deleting Distributed_dhcp if present...")
		if self.delete_dhcp_scope:
			self.buy_time()
			self.delete_dhcp_scope.click()
			self.browser.accept_alert()
			self.buy_time()
			self.browser.refresh()
			self.buy_time()
			
	def asserting_new_button(self):
		logger.debug("DHCPPage: Asserting new button ")
		if self.new_disabled:
			raise AssertionError("DHCPPage: New button is 'Disabled'")
		
		
	def distributed_dhcp_field_validation(self):
		logger.debug("DhcpPage: Clicking on New Button")
		self.click_on_distributed_dhcp_scopes_new()
		logger.debug("DhcpPage : Setting DHCP Name")
		self.network_name.set(self.config.config_vars.centralized_dhcp_name_special_char)
		self.browser.key_press(u'\ue004')
		logger.debug("DhcpPage : Asserting DHCP Name")
		if self.dhcp_name_error:
			raise AssertionError("Field Require error message shown for DHCP Name ")
		if self.centralize_name_max_error:
			raise AssertionError("Maximum Character error message shown for DHCP Name ")
		logger.debug("DhcpPage : Setting Vlad id")
		self.vlan_name.set(self.config.config_vars.zero_preceded_value)
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.next_button.click()
		if not self.vlan_error:
			raise AssertionError(" Vlan range greater than 4093 .Traceback: %s " %traceback.format_exc())
		self.vlan_name.set(self.config.config_vars.vlan_id_3333)
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.next_button.click()
		self.assert_distributed_dhcp_scopes_vlan_error(assert_error=True)
		# self.vlan_name.set(self.config.config_vars.vlan_id)
		
		logger.debug("DhcpPage : Setting netmask adddes")
		self.netmask.set(self.config.config_vars.local_dhcp_netmask)
		logger.debug("DhcpPage : Setting Default Router IP adddes")
		self.default_router.set(self.config.config_vars.router_ip)
		logger.debug("DhcpPage : Setting DNS adddes")
		self.dns_server.set(self.config.config_vars.dns_ip)
		self.browser.key_press(u'\ue004')
		logger.debug("DhcpPage : Asserting netmask adddes")
		if self.netmask_error:
			raise AssertionError(" Valid netmask not accepted.Traceback: %s " %traceback.format_exc())
		logger.debug("DhcpPage : Asserting Default Router IP adddes")
		if self.ip_address_error:
			raise AssertionError(" Valid Ip address not accepted.Traceback: %s " %traceback.format_exc())        
		logger.debug("DhcpPage : Asserting DNS adddes")
		if self.dhcp_dns_server_error:
			raise AssertionError(" Valid dns server not accepted.Traceback: %s " %traceback.format_exc()) 
		
		logger.debug("DhcpPage : Setting Start and End range ip")
		self.set_distributed_dhcp_ipaddress_range_start(self.config.config_vars.ip_start_range)
		self.set_distributed_dhcp_ipaddress_range_end(self.config.config_vars.ip_end_range)
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.next_button.click()
		
		if not self.ip_range_error:
			raise AssertionError("DhcpPage : IP range error not displayed")
		
		logger.debug("DhcpPage : Setting Start and End range ip")
		self.set_distributed_dhcp_ipaddress_range_start(self.config.config_vars.valid_ip_range)
		self.set_distributed_dhcp_ipaddress_range_end(self.config.config_vars.valid_ip_range_2)
		
		logger.debug("DHCP Page : Clicking on '+' button to add new_ip_range...")
		self.click_on_dhcp_distributed_add_new_ip_range()
		
		if not self.distributed_ip_start_one:
			raise AssertionError("DHCPPage : Second IP Address Range text-boxes are not displayed ")
		
		logger.debug("DHCP Page : Clicking on 'Delete' icon to remove new_ip_range...")
		self.remove_ip_range_button.click()
		if self.distributed_ip_start_one:
			raise AssertionError("DHCPPage : Second IP Address Range text-boxes are displayed ")
		
		logger.debug("DHCP Page : Clicking on '+' button to add new option and value.....")
		self.add_new_option.click()
		if not self.option_type_2:
			raise AssertionError("DHCPPage : Second Option-Type text-boxes are not displayed ")
		
		logger.debug("DHCP Page : Clicking on 'Delete' icon to remove new option type...")
		self.remove_option_type.click()
		if self.option_type_2:
			raise AssertionError("DHCPPage : Second Option-Type text-boxes are displayed ")
		
		logger.debug("DHCP Page : Setting Distributed_option_type")
		self.option_type.set(self.config.config_vars.None_option)  
		self.next_button.click()
		if not self.option_type_error:
			raise AssertionError(" option type valid range is 1-254 .Traceback: %s " %traceback.format_exc())
		
		
		logger.debug("DHCP Page : Setting Distributed option_value...")
		self.option_value.set(self.config.config_vars.double_quotes)
		self.browser.key_press(u'\ue004')
		
		# if not self.option_value_quote_error:
			# raise AssertionError("Option value 'Single and Double Quote' not allowed .Traceback: %s " %traceback.format_exc())
		
		logger.debug("DHCP Page : Setting Distributed option_value...")
		self.option_value.set(self.config.config_vars.string_max_len_mac)
		self.browser.key_press(u'\ue004')
		
		if not self.char_255_error:
			raise AssertionError("Option value 'Must be 1-255 chars' .Traceback: %s " %traceback.format_exc())
		
		
		logger.debug("DHCP Page : Setting Distributed option_type and option_value...")
		self.option_type.set(self.config.config_vars.Distributed_Option_Type)
		self.option_value.set(self.config.config_vars.Distributed_Option_Value)
		
		
		logger.debug("DHCPPage : Setting Lease time value")
		self.set_distributed_dhcp_lease_time(self.config.config_vars.vlan_id_5000)
		self.browser.key_press(u'\ue004')
		if not self.lease_time_error:
			raise AssertionError(" Lease time greater time 1440 .Traceback: %s " %traceback.format_exc())
		
		logger.debug("DHCPPage : Setting Lease time value")
		self.set_distributed_dhcp_lease_time(self.config.config_vars.zero_preceded_value)
		self.browser.key_press(u'\ue004')
		if not self.lease_time_error:
			raise AssertionError(" Lease time greater time 1440 .Traceback: %s " %traceback.format_exc())
		
		logger.debug("DHCPPage : Setting Lease time value")
		self.set_distributed_dhcp_lease_time(self.config.config_vars.lease_time_value)
		
		logger.debug("DhcpPage : Setting DHCP Name")
		self.network_name.set(self.config.config_vars.distributed_dhcp_name)
		
		logger.debug("DhcpPage : Setting Vlad id")
		self.vlan_name.set(self.config.config_vars.Dhcp_Vlan)
		
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.next_button.click()
		
		logger.debug("DHCP Page :Write DHCP Client Per Branch into the text-box")
		self.set_distributed_dhcp_client_per_branch(self.config.config_vars.Reserve_First_Exceed)
		self.next_button.click()
		
		
		if not self.client_per_branch_error_2:
			raise AssertionError(" Client per branch is exceeded .Traceback: %s " %traceback.format_exc())
		
		logger.debug("DHCP Page :Write DHCP Client Per Branch into the text-box")
		self.set_distributed_dhcp_client_per_branch(self.config.config_vars.Client_Per_Branch)
		
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.next_button.click()
		
		logger.debug("DHCP Page : Setting dhcp_reserve_field_values...")
		self.reserve_first.set(self.config.config_vars.Reserve_First_Exceed)
		self.reserve_last.set(self.config.config_vars.Reserve_Last_Exceed)
		logger.debug("DHCP Page : Clicking on 'FINISH' button...")
		self.finish_button.click()
		if not self.client_reserve_error:
			raise AssertionError(" Client reserve valid range error message not displayed .Traceback: %s " %traceback.format_exc())
		
		logger.debug("DHCP Page : Setting dhcp_reserve_field_values...")
		self.reserve_first.set(self.config.config_vars.Reserve_First)
		self.reserve_last.set(self.config.config_vars.Reserve_Last)
		
		logger.debug("DHCP Page : Clicking on 'FINISH' button...")
		self.finish_button.click()
		time.sleep(5)
		
	def edit_distributed_dhcp(self):
		logger.debug("DhcpPage: Clicking on 'Edit' button")
		self.dhcp_edit.click()
		
		self.netmask.set(self.config.config_vars.dhcp_netmask_2)
	
		logger.debug("DhcpPage : Setting Start and End range ip")
		self.set_distributed_dhcp_ipaddress_range_start(self.config.config_vars.valid_ip_range_3)
		self.set_distributed_dhcp_ipaddress_range_end(self.config.config_vars.valid_ip_range_4)
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.next_button.click()
		
		logger.debug("DHCP Page :Write DHCP Client Per Branch into the text-box")
		self.set_distributed_dhcp_client_per_branch(self.config.config_vars.client_per_branch_16)
		logger.debug("DHCP Page : Clicking on 'NEXT' button...")
		self.next_button.click()
		
		logger.debug("DHCP Page : Clicking on 'FINISH' button...")
		self.finish_button.click()