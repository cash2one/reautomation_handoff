from athenataf.lib.util.WebPage import WebPage
import traceback
import logging
import time
logger = logging.getLogger('athenataf')

class SwitchesPage(WebPage):
	def __init__(self, test, browser, config):
		WebPage.__init__(self, "Switches", test, browser, config)
		self.test.assertPageLoaded(self)

	def isPageLoaded(self):
		if self.switch_count:
			return True    
		else:
			return False 

	def set_host_name(self,value=None):
		logger.debug("SwitchPage: Setting the host name")
		time.sleep(4)
		if value:
			self.hostname.set(value)
		else:
			self.hostname.set(self.config.config_vars.host_name)

	def save_setting(self):
		logger.debug("SwitchPage: Click save button")
		self.save_settings.click()

	def assert_switch_page(self):
		if not self.switch_page:
			raise AssertionError("Switch page is not loaded .Traceback: %s " %(traceback.format_exc()))

	def assert_switch_group(self):
		if not self.assert_switch:
			import traceback
			raise AssertionError("switch is available in group i.e. Traceback: %s" %traceback.format_exc())
			
	def assert_switch_1(self):
		if not self.switch_1:
			import traceback
			raise AssertionError("switch is not available in group i.e. Traceback: %s" %traceback.format_exc())

	def edit_switch(self):
		'''
		clicks on edit button
		'''
		time.sleep(4)
		logger.debug("SwitchPage : Clicking on edit button ")
		self.edit.click()
		time.sleep(4)
	
	def set_ip_assignment(self, value):
		'''
		sets ip assignment drop down to given value
		'''
		logger.debug("SwitchesPage : Click on ip assignment")
		# self.ip_assignment.click()
		if value == 'Static' :
			logger.debug("SwitchesPage : Setting IP Assignment to Switch type")
			self.ip_assignment_dropdown.set(self.config.config_vars.static)
		elif value == 'DHCP' :
			logger.debug("SwitchesPage : Setting IP Assignment to DHCP type")
			self.ip_assignment_dropdown.set(self.config.config_vars.dhcp)
			
	def save_switch_settings(self):
		'''
		clicks on save settings
		'''
		logger.debug("SwitchPage : Clicking on Save Settings")
		self.save.click()
		time.sleep(4)
		
	def set_static_ipaddress_netmask_gateway(self,ip=None,subnet_mask=None,gateway1=None):
		'''
		sets
		IP ADDRESS :ipaddress
		NETMASK	   : netmask
		GATEWAY	   : gatwway
		'''
		logger.debug("SwitchPage : Writing ip address")
		self.ip_address.set(ip)
		logger.debug("SwitchPage : Writing Netmask")
		self.netmask.set(subnet_mask)
		logger.debug("SwitchPage : Writing default Gateway")
		self.gateway.set(gateway1)
		self.save_switch_settings()
		
	def assert_default_switch_configuration(self):
		'''
			Asserting the default switch fields
		'''
		if not self.mac_address_1:
			raise AssertionError("MAC Address field is not set to default")
		if not self.host_name:
			raise AssertionError("Host Name field is not set to default")
		if not self.ip_assign_dhcp:
			raise AssertionError("IP Assignment field not set to DHCP ")
		if not self.default_ip_address:
			raise AssertionError("IP Address field is not set to - ")
		if not self.default_netmask:
			raise AssertionError("Subnet mask field is not set to - ")
		if not self.default_gateway:
			raise AssertionError("Default gateway field is not set to - ")
		
	def assert_ip_netmask(self):
		if not self.ip_netmask_error:
			raise AssertionError("Invalid ip address and subnet mask combination")
		logger.debug("Clicking OK button on error page")
		self.ok_error_msg.click()
	
	def assert_hostname(self, valid = True):
		if valid :
			if self.host_name_error :
				raise AssertionError('SwitchPage : Valid Hostname is not accepted')
		else :
			if not self.host_name_error :
				raise AssertionError('SwitchPage : Invalid Hostname is accepted')
			self.ok_error_msg_2.click()
			
	def assert_max_string_hostname(self, hst_name):
		'''
		Asserting hostname inputs
		'''
		current_host_name = self.hostname.get()
		if not current_host_name == hst_name :
			raise AssertionError("SwitchPage : Valid Hostname not Accepted")
			
	def verify_mac_address(self, mac_addr = None):
		'''
			Asserting mac address field
		'''
		mac_address = self.mac_address_1.get_label_text()
		if not mac_address == mac_addr:
			raise AssertionError("SwitchPage : MAC address are not matching ")
	
	def assert_ip_or_netmask(self,error=None):
		if error == 'ip':
			if not self.ip_error:
				raise AssertionError("Invalid IP address ")
		if error == 'netmask':
			if not self.netmask_error:
				raise AssertionError("Invalid subnet mask address ")
		logger.debug("Clicking OK button on error page")
		self.ip_netmask_error_ok.click()
		
	def assert_invalid_hostname(self,value=None):
		'''
			Asserting invalid host name
		'''
		if value == 'maxlength':
			if not self.invalid_hostname_error:
				raise AssertionError('SwitchPage : InValid Hostname accepted')
		if value == 'blank':
			if not self.blank_hostname_error:
				raise AssertionError('SwitchPage : Blank/Null Hostname accepted')
		
		