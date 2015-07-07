from athenataf.lib.util.WebPage import WebPage
import traceback
import logging
logger = logging.getLogger('athenataf')
import time
class SwitchDhcpPage(WebPage):
	def __init__(self, test, browser, config):
		WebPage.__init__(self, "SwitchesDhcp", test, browser, config)
		self.test.assertPageLoaded(self)

	def isPageLoaded(self):
		if self.dhcp_scopes_new:
			return True    
		else:
			return False 
	
	def create_new(self):
		logger.debug('DhcpPool: Clicking on New button')
		time.sleep(3)
		self.dhcp_scopes_new.click()
		time.sleep(3)
	
	def create_new_dhcp_pool(self , name , network , netmask , option_type, dns_server =None , wins_server =None ,exclude_start_range = None,exclude_end_range = None):
		'''
		creates new dhcp pool
		'''
		self.create_new()
		logger.debug('DhcpPool: Writting Dhcp name')
		self.dhcp_name.set(name)
		logger.debug('DhcpPool: Writting Dhcp netork')
		self.dhcp_network.set(network)
		logger.debug('DhcpPool: Writting Dhcp netmask')
		self.dhcp_netmask.set(netmask)
		if not dns_server == 'None' :
			logger.debug('DhcpPool: Writting dns server')
			self.dhcp_dns_server.set(dns_server)
		if not wins_server == 'None' :
			logger.debug('DhcpPool: Writting wins server')
			self.dhcp_wins_server.set(wins_server)
		if not exclude_start_range == 'None' and not exclude_end_range == 'None':
			logger.debug("DhcpPoolpage: Writing exclude address range start ")
			self.exclude_address_start.set(exclude_start_range)
			logger.debug("DhcpPoolpage: Writing exclude address range end")
			self.exclude_address_end.set(exclude_end_range)
		logger.debug('DhcpPool: Selecting Dhcp option type as IP')
		self.dhcppool_option_type.set(option_type)
		logger.debug('Dhcp_pool: Clicking on Add button')
		self.dhcp_add.click()
		
	def delete_dhcp(self):
		'''
		deletes newly created dhcp pool
		'''
		if self.dhcp_delete :
			logger.debug('DhcpPool: Clicking on Delete button')
			self.dhcp_delete.click()
			time.sleep(3)
			self.delete_dhcp_pool.click()
			# self.browser.accept_alert()
		time.sleep(3)		
		
	def assert_dhcp_duplicate_creation(self):
		self.create_new()
		logger.debug('DhcpPool: Writting Dhcp name')
		self.dhcp_name.set(self.config.config_vars.dhcp_name1)
		self.dhcp_add.click()
		if not self.dhcp_duplicate_error :
			raise AssertionError("DhcpPool : Duplicate dhcp name accepted")
			
	
	def assert_ui_elements_existing_on_dhcp_pools_page(self):
		logger.debug("DhcpPools: Checking for DHCP Pools label")
		if not self.dhcp_pools_label :
			raise AssertionError("DhcpPoolsPage : Dhcp pool label is not visible")
		logger.debug("DhcpPoolsPage: Checking for Dhcp Pool table ")
		if not self.dhcp_pool_table:
			raise AssertionError("DhcpPoolsPage : Dhcp pool tabel is not visible")
		if not self.enable_dhcp_service:
			raise AssertionError("DhcpPoolPage enable dhcp service checkbox  is not visible")
			
	def create_dhcp_pool_without_profile_name(self):
		'''
		clicks on add button without entering profile name and 
		asserts for the error message
		'''
		self.create_new()
		logger.debug("DHCPPage: Click on Add Button")
		self.dhcp_add.click()
		if not self.dhcp_name_required_field_msg :
			raise AssertionError("Dhcp pool profile name required field error message is not visible")
			
	def set_enable_dhcp_services(self,value = None):
		'''
		enable /disables enable dhcp service checkbox 
		'''
		logger.debug("DHCPPage: Click on DHCP service checkbox")
		if value == 'enable':
			if not self.enable_dhcp_service.is_selected () :
				self.enable_dhcp_service.click()
		else:
			if self.enable_dhcp_service.is_selected () :
				self.enable_dhcp_service.click()

	def save_setting(self):
		'''
		Clicks on save setting button
		'''
		logger.debug('DhcpPoolPage: Clicking on save setting button')
		self.save_settings.click()
		
	def cancel_button_functionality(self):
		logger.debug('DhcpPool: Clicking on New button')
		self.dhcp_scopes_new.click()
		logger.debug('DhcpPool: Writting Dhcp name')
		self.dhcp_name.set(self.config.config_vars.dhcp_name)
		logger.debug('DhcpPool: Writting Dhcp netork')
		self.dhcp_network.set(self.config.config_vars.dhcp_network)
		logger.debug('DhcpPool: Clicking on cancel button')
		self.dhcp_cancel.click()
		
	def select_test2_edit_icon(self):
		self.test2_edit.click()
			
	def edit_dhcp_pool(self,network,netmask):
		logger.debug('DhcpPool: Writting Dhcp netork')
		self.dhcp_network.set(network)
		logger.debug('DhcpPool: Writting Dhcp netmask')
		self.dhcp_netmask.set(netmask)
		logger.debug('DhcpPool: Clicking on save button')
		self.dhcp_add.click()
		if self.dhcp_add:
			self.dhcp_add.click
			
	def check_test2_exist(self):
		if not self.test2:
			self.create_new_dhcp_pool('test2','10.10.10.20','255.255.255.0','IP','None','None','None','None')
	
	def create_dhcp_pool_with_multiple_exclude_ip(self , name , network , netmask):
		'''
		creates new dhcp pool with multiple exclude ip address
		'''
		self.create_new()
		logger.debug('DhcpPool: Writting Dhcp name')
		self.dhcp_name.set(name)
		logger.debug('DhcpPool: Writting Dhcp netork')
		self.dhcp_network.set(network)
		logger.debug('DhcpPool: Writting Dhcp netmask')
		self.dhcp_netmask.set(netmask)
		logger.debug("DhcpPoolpage: Writing exclude address range start 1")
		self.exclude_address_start.set(self.config.config_vars.dhcp_network)
		logger.debug("DhcpPoolpage: Writing exclude address range end 1")
		self.exclude_address_end.set(self.config.config_vars.address_range)
		self.exclude_address_add_button_1.click()
		logger.debug("DhcpPoolpage: Writing exclude address range start 2")
		self.exclude_address_start_1.set(self.config.config_vars.exclude_address_start_1)
		logger.debug("DhcpPoolpage: Writing exclude address range end 2")
		self.exclude_address_end_1.set(self.config.config_vars.exclude_address_end_1)	
		self.exclude_address_add_button_2.click()
		logger.debug("DhcpPoolpage: Writing exclude address range start 3")
		self.exclude_address_start_2.set(self.config.config_vars.exclude_address_start_2)
		logger.debug("DhcpPoolpage: Writing exclude address range end 3")
		self.exclude_address_end_2.set(self.config.config_vars.exclude_address_end_2)
		logger.debug('DhcpPool: Clicking on add button')	
		self.dhcp_add.click()
		if self.dhcp_add:
			self.dhcp_add.click		
		
	def set_profile_name(self, name):
		logger.debug('DhcpPool: Writting Dhcp name')
		self.dhcp_name.set(name)
		
	def crate_dhcp_with_multiple_dns_server(self):
		logger.debug("DhcpPoolPage : Writing first dns server")
		self.dhcp_dns_server.set(self.config.config_vars.dns_server1)
		logger.debug("DhcpPoolPage: Clicking on add button")
		self.add_dns_server1.click()
		logger.debug("DhcpPoolPage : Writing second dns server")
		self.dhcp_dns_server1.set(self.config.config_vars.dns_server2)
		logger.debug("DhcpPoolPage: Clicking on add button")
		self.add_dns_server2.click()
		logger.debug("DhcpPoolPage : Writing second dns server")
		self.dhcp_dns_server2.set(self.config.config_vars.dns_server3)
		logger.debug("DhcpPoolPage: Clicking on add button")
		self.add_dns_server3.click()
		logger.debug("DhcpPoolPage : Writing second dns server")
		self.dhcp_dns_server3.set(self.config.config_vars.dns_server4)
		logger.debug("DhcpPoolPage: Clicking on add button")
		self.add_dns_server4.click()
		logger.debug("DhcpPoolPage : Writing second dns server")
		self.dhcp_dns_server4.set(self.config.config_vars.dns_server5)
		logger.debug("DhcpPoolPage: Clicking on add button")
		self.add_dns_server5.click()
		logger.debug("DhcpPoolPage : Writing second dns server")
		self.dhcp_dns_server5.set(self.config.config_vars.dns_server6)
		logger.debug("DhcpPoolPage: Clicking on add button")
		self.add_dns_server6.click()
		logger.debug("DhcpPoolPage : Writing second dns server")
		self.dhcp_dns_server6.set(self.config.config_vars.dns_server7)
		logger.debug("DhcpPoolPage: Clicking on add button")
		self.add_dns_server7.click()
		logger.debug("DhcpPoolPage : Writing second dns server")
		self.dhcp_dns_server7.set(self.config.config_vars.dns_server8)
		logger.debug("DhcpPoolPage: Clicking on add button")
		self.add_dns_server8.click()
		logger.debug("DhcpPoolPage : Writing second dns server")
		self.dhcp_dns_server8.set(self.config.config_vars.dns_server9)
		
	def save_dhcp_pool(self):
		'''
		clicks on save button
		'''
		logger.debug('DhcpPoolPage : Clicking on save button')
		self.dhcp_add.click()
		
	def crate_dhcp_with_multiple_wins_server(self):
		logger.debug("DhcpPoolPage : Writing first wins server")
		self.dhcp_wins_server.set(self.config.config_vars.wins_server1)
		logger.debug("DhcpPoolPage: Clicking on add button")
		self.add_wins_server1.click()
		logger.debug("DhcpPoolPage : Writing second wins server")
		self.dhcp_wins_server1.set(self.config.config_vars.wins_server2)
		logger.debug("DhcpPoolPage: Clicking on add button")
		self.add_wins_server2.click()
		logger.debug("DhcpPoolPage : Writing second wins server")
		self.dhcp_wins_server2.set(self.config.config_vars.wins_server3)
		logger.debug("DhcpPoolPage: Clicking on add button")
		self.add_wins_server3.click()
		logger.debug("DhcpPoolPage : Writing second wins server")
		self.dhcp_wins_server3.set(self.config.config_vars.wins_server4)
		logger.debug("DhcpPoolPage: Clicking on add button")
		self.add_wins_server4.click()
		logger.debug("DhcpPoolPage : Writing second wins server")
		self.dhcp_wins_server4.set(self.config.config_vars.wins_server5)
		logger.debug("DhcpPoolPage: Clicking on add button")
		self.add_wins_server5.click()
		logger.debug("DhcpPoolPage : Writing second wins server")
		self.dhcp_wins_server5.set(self.config.config_vars.wins_server6)
		logger.debug("DhcpPoolPage: Clicking on add button")
		self.add_wins_server6.click()
		logger.debug("DhcpPoolPage : Writing second wins server")
		self.dhcp_wins_server6.set(self.config.config_vars.wins_server7)
		logger.debug("DhcpPoolPage: Clicking on add button")
		self.add_wins_server7.click()
		logger.debug("DhcpPoolPage : Writing second wins server")
		self.dhcp_wins_server7.set(self.config.config_vars.wins_server8)
		logger.debug("DhcpPoolPage: Clicking on add button")
		self.add_wins_server8.click()
		logger.debug("DhcpPoolPage : Writing second wins server")
		self.dhcp_wins_server8.set(self.config.config_vars.wins_server9)
		
	def validate_all_elememt_of_dhcp_page(self):
		self.create_new()
		logger.debug("DhcpPoolPage : Writing invalid dhcp name")
		self.dhcp_name.set(self.config.config_vars.dhcp_name_invalid)
		logger.debug('DhcpPool: Writting invalid Dhcp netork')
		self.dhcp_network.set(self.config.config_vars.dhcp_network_invalid)		
		logger.debug('DhcpPool: Writting invalid Dhcp netmask')
		self.dhcp_netmask.set(self.config.config_vars.dhcp_netmask_invalid)
		logger.debug('DhcpPool: Writting invalid  default router')
		self.dhcp_router.set(self.config.config_vars.dhcp_router_invalid)
		logger.debug('DhcpPool: Writting invalid dns server')
		self.dhcp_dns_server.set(self.config.config_vars.dns_server_invalid)
		logger.debug('DhcpPool: Writting invalid wins server')
		self.dhcp_wins_server.set(self.config.config_vars.wins_server_invalid)
		logger.debug("DhcpPoolpage: Writing invalid exclude address start range")
		self.exclude_address_start.set(self.config.config_vars.exclude_address_start_invalid)
		logger.debug("DhcpPoolpage: Writing invalid exclude address end range")
		self.exclude_address_end.set(self.config.config_vars.exclude_address_end_invalid)
		logger.debug('DhcpPool: Selecting Dhcp option type as IP')
		self.dhcppool_option_type.set(self.config.config_vars.option_type_ip)	
		logger.debug("DhcpPoolpage: Writing invalid Dhcp option code ")
		self.dhcppool_option_code.set(self.config.config_vars.dhcp_option_code_invalid)
		logger.debug("DhcpPoolpage: Writing invalid Dhcp option value ")
		self.dhcppool_option_value.set(self.config.config_vars.dhcp_option_value_invalid)
		self.dhcp_add.click()
		
	def asssert_all_element_of_dhcp_page(self):
		logger.debug("DHCPPage: Asserting the DHCP page elements")
		if not self.name_error_msg:
			raise AssertionError("Dhcp profile name max length error message is not visible")
		if not self.network_error_msg:
			raise AssertionError("Dhcp network invalid ip address error message is not visible")
		if not self.netmask_error_msg:
			raise AssertionError("Dhcp netmask invalid ip address error message is not visible")
		if not self.default_router_error_msg:
			raise AssertionError("Dhcp default invalid ip address router error message is not visible")
		if not self.dns_server_error_msg:
			raise AssertionError("Dhcp dns server invalid ip address error message is not visible")
		if not self.wins_server_error_msg:
			raise AssertionError("Dhcp wins server invalid ip address error message is not visible")
		if not self.exclude_address_error_msg:
			raise AssertionError("Dhcp exclude address invalid ip address error message is not visible")
		if not self.option_code_error_msg:
			raise AssertionError("Dhcp option code valid range error message is not visible")
		if not self.option_value_error_msg:
			raise AssertionError("Dhcp option value invalid ip address error message is not visible")
		
	def cancel_button(self):
		logger.debug('Clicking on cancel button')
		self.dhcp_cancel.click()