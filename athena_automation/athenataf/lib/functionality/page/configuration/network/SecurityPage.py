import logging
logger = logging.getLogger('athenataf')
import traceback
from athenataf.lib.util.WebPage import WebPage
from athenataf.lib.functionality.page.configuration.network.AccessPage import AccessPage
import time
class SecurityPage(WebPage):
	def __init__(self, test, browser, config):
		WebPage.__init__(self, "SecurityLevel", test, browser, config)
		self.test.assertPageLoaded(self)
		
	def isPageLoaded(self):
		if self.next:
			return True	
		else:
			return False
		
	def wired_security_defaults(self):
		'''
		Use default security parameters while creating a network.
		'''
		logger.debug("SecurityPage : Disable mac authentication.")
		self.mac_authentication.set(self.config.config_vars.Security_Mac_Authentication)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		return AccessPage(self.test, self.browser, self.config)
		
	def wired_employee_security_defaults(self):
		'''
		Asserting Wired employee security defaults
		'''
		logger.debug('NetworkPage: Security : Checking mac authentication field is selected to :Disabled')
		if not self.mac_authentication.selected=='Disabled':
			raise AssertionError("Mac authentication not Disabled Up by default .Traceback: %s " %traceback.format_exc())
		logger.debug('NetworkPage: Security : Checking 802.1x field is  :Disabled')
		if not self.dot1x.selected=='Disabled':
			raise AssertionError("802.1X AUTHENTICATION not Disabled Up by default .Traceback: %s " %traceback.format_exc())


	def wired_guest_security_defaults(self):
		'''
		Use default guest security parameters while creating a network.
		'''
		if self.mac_authentication:
			logger.debug("SecurityPage : Clicking on next")	
			self.next.click()
			#self.next.click()
		return AccessPage(self.test, self.browser, self.config)

			
	def configure_employee_security(self,both=False):
		'''
		Configure the security parameters for a employee wpa network.
		:param both		:	default : False
		If both = True then select Both(WPA-2 & WPA)
		'''
		# self.assert_passphrase_error_msg()
		if not both:
			logger.debug('SecurityPage : Setting Key Management to WPA-2 Personal')
			self.security_key_management.set(self.config.config_vars.Authentication_wpa2)
		else:
			logger.debug('SecurityPage : Setting Key Management to Both(WPA-2 & WPA)')
			self.security_key_management.set(self.config.config_vars.Authentication_wpa_wpa2)
		logger.debug('SecurityPage: writing passphrase')
		self.passphrase.set(self.config.config_vars.Network_Passphrase)
		logger.debug('SecurityPage: re-writing passphrase')
		self.retype_passphrase.set(self.config.config_vars.Network_Passphrase)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		return AccessPage(self.test, self.browser, self.config)
		
	def configure_guest_security(self,splashpage=False,acknowledged=False,both=False):
		'''
		Configure the security parameters for a guest wpa network.
		'''
		if acknowledged:
			logger.debug("SecurityPage : Selecting Internal - Acknowledged.")
			self.splash_page_type.set(self.config.config_vars.Splash_page_Acknowledged)
			logger.debug("SecurityPage : Clicking on next")	
			self.next.click()
		elif splashpage:
			logger.debug("SecurityPage : Selecting None.")
			self.splash_page_type.set(self.config.config_vars.Splash_page_none)
			logger.debug("SecurityPage : Enable Wireless Encryption.")
			self.wireless_encryption.set(self.config.config_vars.Encryption_Guest)
			logger.debug('SecurityPage : Setting Key Management to WPA-2 Personal')
			self.security_key_management.set(self.config.config_vars.Authentication_wpa2)
			logger.debug('SecurityPage: writing passphrase')
			self.passphrase.set(self.config.config_vars.Network_Passphrase)
			logger.debug('SecurityPage: re-writing passphrase')
			self.retype_passphrase.set(self.config.config_vars.Network_Passphrase)
			logger.debug("SecurityPage : Clicking on next")	
			self.next.click()
		else:
			logger.debug("SecurityPage : Selecting Internal - Authenticated.")
			self.splash_page_type.set(self.config.config_vars.Splash_page_Authenticated)
			logger.debug("SecurityPage : Disable wispr .")
			self.wispr.set(self.config.config_vars.Wispr_status)
			logger.debug("SecurityPage : Disable mac authentication.")
			self.mac_authentication.set(self.config.config_vars.Security_Mac_Authentication)
			logger.debug('SecurityPage: selecting InternalServer')
			self.authentication_server.set(self.config.config_vars.Authentication_server)
			logger.debug("SecurityPage: Writing reauth")
			self.reauth_interval.set(self.config.config_vars.Authentication_interval)
			logger.debug('SecurityPage : Setting blacklisting to enabled')
			self.blacklisting.set(self.config.config_vars.BlackListing_Guest)
			logger.debug("SecurityPage : Enable Wireless Encryption.")
			self.wireless_encryption.set(self.config.config_vars.Encryption_Guest)
			if both:
				logger.debug('SecurityPage : Setting Key Management to Both(WPA-2 & WPA)')
				self.security_key_management.set(self.config.config_vars.Authentication_wpa_wpa2)
			logger.debug('SecurityPage: writing passphrase')
			self.passphrase.set(self.config.config_vars.Network_Passphrase)
			logger.debug('SecurityPage: re-writing passphrase')
			self.retype_passphrase.set(self.config.config_vars.Network_Passphrase)
			logger.debug('SecurityPage: calling  edit_save_splash_page_details method')
			self.edit_save_splash_page_details()
			logger.debug("SecurityPage : Clicking on next")	
			self.next.click()
		return AccessPage(self.test, self.browser, self.config)
		
	def createnetwork_guest_blacklisting_enabled(self):
		'''
		Create a guest network with splash page type : None and blacklisting eenabled. 
		Encryption : Both(WPA-2 & WPA)
		'''
		logger.debug("SecurityPage : Selecting None.")
		self.splash_page_type.set(self.config.config_vars.Splash_page_none)
		logger.debug('SecurityPage : Setting blacklisting to enabled')
		self.blacklisting.set(self.config.config_vars.BlackListing_Guest)
		logger.debug("SecurityPage : Enable Wireless Encryption.")
		self.wireless_encryption.set(self.config.config_vars.Encryption_Guest)
		logger.debug('SecurityPage : Setting Key Management to Both(WPA-2 & WPA)')
		self.security_key_management.set(self.config.config_vars.Authentication_wpa_wpa2)
		logger.debug('SecurityPage: writing passphrase')
		self.passphrase.set(self.config.config_vars.Network_Passphrase)
		logger.debug('SecurityPage: re-writing passphrase')
		self.retype_passphrase.set(self.config.config_vars.Network_Passphrase)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		return AccessPage(self.test, self.browser, self.config)
		
	def set_wpa2_blacklisting_enable(self):
		'''
		Cofigure voice network security parameters.
		'''
		logger.debug('SecurityPage : Setting Key Management to  WPA-2 Personal')
		self.security_key_management.set(self.config.config_vars.Authentication_wpa2)
		logger.debug('SecurityPage : Setting blacklisting to enabled')
		self.blacklisting.set(self.config.config_vars.BlackListing_Guest)
		logger.debug('SecurityPage: writing passphrase')
		self.passphrase.set(self.config.config_vars.Network_Passphrase)
		logger.debug('SecurityPage: re-writing passphrase')
		self.retype_passphrase.set(self.config.config_vars.Network_Passphrase)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		return AccessPage(self.test, self.browser, self.config)
	
	def set_default_captive_role(self,wireless=False):
		if wireless:
			logger.debug("SecurityPage : Selecting External.")
			self.splash_page_type.set(self.config.config_vars.Splash_page_external)
			logger.debug("Entering the captive portal value. ")
			self.wired_captive_portal.set(self.config.config_vars.Wired_Captive_Profile_Default)
			self.next.click()
		else:
			self.splash_page_type.set(self.config.config_vars.Splash_page_external)
			logger.debug("Entering the captive portal value. ")
			self.wired_captive_portal.set(self.config.config_vars.Wired_Captive_Profile_Default)
			logger.debug("SecurityPage : Clicking on next")	
			self.next.click()
		return AccessPage(self.test, self.browser, self.config)
	
	def create_captive_portal_profile(self,text=False,ret = True):
		self.splash_page_type.set(self.config.config_vars.Splash_page_external)
		logger.debug("Entering the captive portal value. ")
		self.wired_captive_portal.set(self.config.config_vars.Wired_Captive_Profile_New)
		if text:
			self.buy_time()
			logger.debug("Entering the captive Type value. ")
			self.captive_type.set(self.config.config_vars.Captive_Role_Text)
			logger.debug("Entering the captive Name value. ")
			self.captive_name.set(self.config.config_vars.Captive_Role_Name)
			logger.debug("Entering the captive Ip value. ")			
			self.captive_ip.set(self.config.config_vars.Captive_Role_Ip)
			logger.debug("Entering the captive Url . ")		
			if self.captive_url:
				logger.debug("Entering the captive Url value. ")	
				self.captive_url.set(self.config.config_vars.domain_name)
			logger.debug("Entering the captive Port value. ")
			self.captive_port.set(self.config.config_vars.Captive_Role_Port)
			logger.debug("Entering the captive Auth text value. ")
			self.captive_auth_text.set(self.config.config_vars.Captive_Role_Name)												
		else:
			logger.debug("Entering the captive Type value. ")
			self.captive_type.set(self.config.config_vars.Captive_Role_Radius_Authentication)
			logger.debug("Entering the captive Name value. ")
			self.captive_name.set(self.config.config_vars.Captive_Role_Name)
			if self.captive_url:
				logger.debug("Entering the captive Url . ")		
				self.captive_url.set(self.config.config_vars.domain_name)			
			logger.debug("Entering the captive Ip value. ")	
			self.captive_ip.set(self.config.config_vars.Captive_Role_Ip)
			logger.debug("Entering the captive Port value. ")										
			self.captive_port.set(self.config.config_vars.Captive_Role_Port)							
		logger.debug("SecurityPage : Clicking on save")	
		self.save.click()
		self.buy_time()
		if ret:
			logger.debug("SecurityPage : Clicking on next")	
			self.next.click()											
			return AccessPage(self.test, self.browser, self.config)	
			
	def configure_enterprise_security(self,both=False):
		'''
		Configure enterprise level security parameters.
		:param both		:	default : False
		If both = True then select Both(WPA-2 & WPA)
		'''
		logger.debug("SecurityPage : Clicking on Entriprise")
		self.enteprise.click()
		if not both:
			logger.debug("SecurityPage : Calling assert_okc_checkbox method")	
			self.assert_okc_checkbox()
			logger.debug('SecurityPage : Setting Key Management to  WPA-2 Enterprise')
			self.security_key_management.set(self.config.config_vars.Authentication_Wpa2_Enterprise)
		else:
			logger.debug('SecurityPage : Setting Key Management to  WPA-2 Enterprise')
			self.security_key_management.set(self.config.config_vars.Authentication_Wpa2_WPA_Enterprise)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		self.buy_time()
		try:
			logger.debug("SecurityPage : Clicking on next")	
			self.next.click()
		except:
			pass
		return AccessPage(self.test, self.browser, self.config)
	
	def assert_okc_options(self):
		'''
		Configure enterprise level security parameters and check if okc checkbox is visible.
		'''
		logger.debug("SecurityPage : Clicking on Entriprise")
		self.enteprise.click()
		logger.debug("SecurityPage : Selecting  InternalServer for Authentication Server feild ")
		self.security_key_management.set(self.config.config_vars.Authentication_Wpa_Enterprise)
		logger.debug('SecurityPage : Asserting okc checkbox : Disabled')
		if self.okc_option:
			raise AssertionError("Okc options visible .Traceback: %s " %traceback.format_exc())
	
	def assert_roaming_defaults(self,personal=False,both=False):
		'''
		Configure enterprise level security parameters and check if okc checkbox is visible.
		'''
		if not personal:
			logger.debug("SecurityPage : Clicking on Entriprise")
			self.enteprise.click()
			if both:
				logger.debug('SecurityPage : Setting Key Management to  WPA-2 Enterprise')
				self.security_key_management.set(self.config.config_vars.Authentication_Wpa2_WPA_Enterprise)
			else:	
				logger.debug("SecurityPage : Set Key Management to WPA-2 Enterprise .")
				self.security_key_management.set(self.config.config_vars.Authentication_Wpa2_Enterprise)
			if self.roaming_open.is_selected():
				raise AssertionError("802.11r romaing checkbox is not disabled by default .Traceback: %s " %traceback.format_exc())
		else:
			if not both:
				logger.debug('SecurityPage : Setting Key Management to  WPA-2 Personal')
				self.security_key_management.set(self.config.config_vars.Authentication_wpa2)
			else:
				logger.debug('SecurityPage : Setting Key Management to Both(WPA-2 & WPA)')
				self.security_key_management.set(self.config.config_vars.Authentication_wpa_wpa2)
			if self.roaming_open.is_selected():
				raise AssertionError("802.11r romaing checkbox is not disabled by default .Traceback: %s " %traceback.format_exc())
			logger.debug('SecurityPage: writing passphrase')
			self.passphrase.set(self.config.config_vars.Network_Passphrase)
			logger.debug('SecurityPage: re-writing passphrase')
			self.retype_passphrase.set(self.config.config_vars.Network_Passphrase)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		self.buy_time()
		try:
			logger.debug("SecurityPage : Clicking on next")	
			self.next.click()
		except:
			pass
		return AccessPage(self.test, self.browser, self.config)
	
	def create_network_mac_authentication_enabled(self,enterprise=False,open_security=False):
		'''
		Create network employee personal,enterprise,open , enable mac auth . Check if Uppercase support is disabled by default.
		'''
		
		if enterprise:
			logger.debug("SecurityPage : Clicking on Entriprise")
			self.enteprise.click()
			logger.debug("SecurityPage :Check the Mac Authentication - Perform MAC authentication before 802.1x.")
			self.enterprise_mac_authentication.click()
			logger.debug("NetworkPage : SecurityPage :Checking personal uppercase support is selected to : Disabled ")
			if not self.personal_uppercase_support.selected=='Disabled':
				raise AssertionError("Uppercase support is not disabled by default .Traceback: %s " %traceback.format_exc())
			logger.debug('SecurityPage : Enabling uppercase support')
			self.personal_uppercase_support.set(self.config.config_vars.Uppercase_Support_Enabled)
			logger.debug("SecurityPage : Set delimiter to  :")
			self.personal_delimeter.set(':')
		elif open_security:
			logger.debug("SecurityPage : Enable open.")
			self.open_security.click()
			logger.debug("SecurityPage : Enable mac authentication.")
			self.mac_authentication.set(self.config.config_vars.Security_Mac_Authentication_Enabled)
			logger.debug("NetworkPage : SecurityPage :Checking personal uppercase support is selected to : Disabled ")
			if not self.personal_uppercase_support.selected=='Disabled':
				raise AssertionError("Uppercase support is not disabled by default .Traceback: %s " %traceback.format_exc())
			logger.debug('SecurityPage : Enabling uppercase support')
			self.personal_uppercase_support.set(self.config.config_vars.Uppercase_Support_Enabled)
			logger.debug("SecurityPage : Set delimiter to  :")
			self.personal_delimeter.set(':')
		else:
			self.mac_authentication.set(self.config.config_vars.Security_Mac_Authentication_Enabled)
			self.assert_mac_delimiter_uppercase_options()
			logger.debug("NetworkPage : SecurityPage :Checking personal uppercase support is selected to : Disabled ")
			if not self.personal_uppercase_support.selected=='Disabled':
				raise AssertionError("Uppercase support is not disabled by default .Traceback: %s " %traceback.format_exc())
			self.assert_delimiter_value_error()
			logger.debug('SecurityPage : Enabling uppercase support')
			self.personal_uppercase_support.set(self.config.config_vars.Uppercase_Support_Enabled)
			logger.debug("SecurityPage : Set delimiter to  :")
			self.personal_delimeter.set(':')
			logger.debug('SecurityPage: writing passphrase')
			self.passphrase.set(self.config.config_vars.Network_Passphrase)
			logger.debug('SecurityPage: re-writing passphrase')
			self.retype_passphrase.set(self.config.config_vars.Network_Passphrase)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		self.buy_time()
		try:
			logger.debug("SecurityPage : Clicking on next")	
			self.next.click()
		except:
			pass
		return AccessPage(self.test, self.browser, self.config)
	
	def check_splash_page_options(self,wireless=False):
		if not wireless:
				options = len(self.splash_page_type.options)
		else:
				options = len(self.splash_page_type.options)
		logger.debug("NetworkPage : SecurityPage :Checking Splash page options  ")
		if options<6:
					raise AssertionError(" All Splash page type options not listed .Traceback: %s " %traceback.format_exc())
		
		
	def create_wireless_guest_captive_portal_profile(self,text=False):
		logger.debug("SecurityPage : Selecting external.")
		self.splash_page_type.set(self.config.config_vars.Splash_page_external)
		logger.debug("Entering the captive portal value. ")
		self.wired_captive_portal.set(self.config.config_vars.Wired_Captive_Profile_New)
		if text:
			logger.debug("Entering the captive Type value. ")
			self.captive_type.set(self.config.config_vars.Captive_Role_Text)
			logger.debug("Entering the captive Name value. ")
			self.captive_name.set(self.config.config_vars.Captive_Role_Name)						
			logger.debug("Entering the captive Ip value. ")	
			self.captive_ip.set(self.config.config_vars.Captive_Role_Ip)
			if self.captive_url:
				logger.debug("Entering the captive Url . ")
				self.captive_url.set(self.config.config_vars.domain_name)			
			logger.debug("Entering the captive Port value. ")
			self.captive_port.set(self.config.config_vars.Captive_Role_Port)							
			logger.debug("Entering the captive Auth text value. ")
			self.captive_auth_text.set(self.config.config_vars.Captive_Role_Name)												
		else:
			logger.debug("Entering the captive Type value. ")
			self.captive_type.set(self.config.config_vars.Captive_Role_Radius_Authentication)
			logger.debug("Entering the captive Name value. ")
			self.captive_name.set(self.config.config_vars.Captive_Role_Name)						
			logger.debug("Entering the captive Ip value. ")	
			self.captive_ip.set(self.config.config_vars.Captive_Role_Ip)
			if self.captive_url:
				logger.debug("Entering the captive Url . ")
				self.captive_url.set(self.config.config_vars.domain_name)			
			logger.debug("Entering the captive Port value. ")
			self.captive_port.set(self.config.config_vars.Captive_Role_Port)							
		logger.debug("SecurityPage : Clicking on Save")	
		self.save.click()
		self.buy_time()
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()	
		return AccessPage(self.test, self.browser, self.config)
		
	def create_wireless_captive_portal(self,text=False):
		logger.debug("NetworkPage : SecurityPage :Writing splash page type : Splash page external ")
		self.splash_page_type.set(self.config.config_vars.Splash_page_external)
		logger.debug("Entering the captive portal value. ")
		self.wired_captive_portal.set(self.config.config_vars.Wired_Captive_Profile_New)
		options = self.wired_captive_portal.get_options()
		for x in options:
			if x == self.config.config_vars.Role_Name:
				raise AssertionError(" Created role is present .Traceback: %s " %traceback.format_exc())
		if text:
			logger.debug("Entering the captive Type value. ")
			self.captive_type.set(self.config.config_vars.Captive_Role_Text)
			logger.debug("Entering the captive Name value. ")
			self.captive_name.set(self.config.config_vars.Captive_Role_Name)						
			logger.debug("Entering the captive Ip value. ")	
			self.captive_ip.set(self.config.config_vars.Captive_Role_Ip)
			if self.captive_url:
				logger.debug("Entering the captive Url . ")
				self.captive_url.set(self.config.config_vars.domain_name)			
			logger.debug("Entering the captive Port value. ")
			self.captive_port.set(self.config.config_vars.Captive_Role_Port)							
			logger.debug("Entering the captive Auth text value. ")
			self.captive_auth_text.set(self.config.config_vars.Captive_Role_Name)												
		else:
			logger.debug("Entering the captive Type value. ")
			self.captive_type.set(self.config.config_vars.Captive_Role_Radius_Authentication)
			logger.debug("Entering the captive Name value. ")
			self.captive_name.set(self.config.config_vars.Captive_Role_Name)						
			logger.debug("Entering the captive Ip value. ")	
			self.captive_ip.set(self.config.config_vars.Captive_Role_Ip)
			if self.captive_url:
				logger.debug("Entering the captive Url . ")
				self.captive_url.set(self.config.config_vars.domain_name)			
			logger.debug("Entering the captive Port value. ")
			self.captive_port.set(self.config.config_vars.Captive_Role_Port)							
		logger.debug("SecurityPage : Clicking on Save")	
		self.save.click()
		self.buy_time()
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()	
		return AccessPage(self.test, self.browser, self.config)
	
	def buy_time(self):
		time.sleep(15)
	
	def	use_security_default(self):
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		self.buy_time()
		if self.next:
			logger.debug("SecurityPage : Clicking on next")	
			self.next.click()											
		return AccessPage(self.test, self.browser, self.config)
		
	def set_security_level_open(self):
		logger.debug("SecurityPage : Enable open.")
		self.open_security.click()
		
	def assert_open_roaming_value(self):
		if not self.roaming_open:
			raise AssertionError("'802.11r ROAMING' checkbox not present.Traceback: %s " %traceback.format_exc())
		elif self.roaming_open.is_selected():
			raise AssertionError("'802.11r ROAMING' checkbox value not enabled.Traceback: %s " %traceback.format_exc())
				
	def set_open_roaming_nondefault(self):
		logger.debug("SecurityPage : Enable 802.11r ROAMING.")
		self.roaming_open.click()

	def set_security_level_and_key_management(self , level):
		if level == 'Personal':
			logger.debug("SecurityPage : Enable personal.")
			self.personal.click()
			logger.debug("NetworkPage : SecurityPage :Asserting key management value ")
			if not self.config.config_vars.personal_key_mgt_value in self.security_key_management.get_options():
				raise AssertionError("'Static WEP' not found in 'KEY MANAGEMENT' drop-down.Traceback: %s " %traceback.format_exc())
			logger.debug("SecurityPage : Set Key Management to Static WEP .")
			self.security_key_management.set(self.config.config_vars.personal_key_mgt_value)
			logger.debug("SecurityPage : Writing Personal Wep key")
			self.personal_wep_key.set(self.config.config_vars.wep_key)
			logger.debug("SecurityPage : re Writing Personal Wep key")
			self.personal_re_wep_key.set(self.config.config_vars.wep_key)
		elif level == 'Enterprise':
			logger.debug("SecurityPage : Clicking on Entriprise")
			self.enteprise.click()
			logger.debug("NetworkPage : SecurityPage :Checking enterprise uppercase support is selected to : Disabled ")
			if not self.config.config_vars.enterprise_key_mgt_value in self.security_key_management.get_options():
				raise AssertionError("'Dynamic WEP' not found in 'KEY MANAGEMENT' drop-down.Traceback: %s " %traceback.format_exc())
			logger.debug('SecurityPage : Setting Key Management to  Dynamic- WEP With 802.1x')
			self.security_key_management.set(self.config.config_vars.enterprise_key_mgt_value)
		
	def assert_roaming_not_present(self):
		if self.roaming_open:
			raise AssertionError("'802.11r ROAMING' option available.Traceback: %s " %traceback.format_exc())
				
	def mac_authentication_configuration(self):
		logger.debug("SecurityPage : Enable mac authentication.")
		self.mac_authentication.set(self.config.config_vars.Security_Mac_Authentication_Enabled)
		if not self.personal_uppercase_support.selected=='Disabled':
			raise AssertionError("Uppercase support is not disabled by default .Traceback: %s " %traceback.format_exc())
		logger.debug('SecurityPage : Enabling uppercase support')
		self.personal_uppercase_support.set(self.config.config_vars.Uppercase_Support_Enabled)
		logger.debug('SecurityPage : Entering delimeter value')
		self.personal_delimeter.set(':')
		self.buy_time()
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		self.buy_time()
		try:
			logger.debug("SecurityPage : Clicking on next")	
			self.next.click()
		except:
			pass
		return AccessPage(self.test, self.browser, self.config)
		
	def assert_passphrase_error_msg(self):
		logger.debug('SecurityPage: writing passphrase')
		self.passphrase.set('111')
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		time.sleep(3)
		if not self.passphrase_mismatch_error_msg:
			raise AssertionError("Passphrase mismatch error message has not been shown .Traceback: %s " %traceback.format_exc())
		if not self.passphrase_length_error_msg:
			raise AssertionError("Passphrase length error message has not been shown .Traceback: %s " %traceback.format_exc())
			
	def click_on_next(self):
		time.sleep(5)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		return AccessPage(self.test, self.browser, self.config)
		
	def assert_mac_delimiter_uppercase_options(self):
		if not self.personal_delimeter:
			raise AssertionError("Delimiter character option is not visible .Traceback: %s " % traceback.format_exc())
		if not self.personal_uppercase_support:
			raise AssertionError("Uppercase support option is not visible .Traceback: %s " % traceback.format_exc())
		
	def assert_delimiter_value_error(self):
		logger.debug('SecurityPage : Entering delimeter value')
		self.personal_delimeter.set('1')
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.delimiter_error_msg:
			raise AssertionError("Delimiter error message is not visible .Traceback: %s " % traceback.format_exc())
	
	def assert_okc_checkbox(self):
		if not self.okc_checkbox.is_selected():
			# raise AssertionError("Opportunistic Key Caching checkbox is not visible: %s " % traceback.format_exc())
			# self.okc_checkbox.click()
			logger.debug("SecurityPage : Clicking on OKC checkbox")	
			self.okc_checkbox.click()
			
	def edit_save_splash_page_details(self):
		logger.debug('SecurityPage : setting "Title Header - Hello" fiend.')
		self.banner_title.set(self.config.config_vars.edit_banner_title_new_value)
		# self.header_color.set(self.config.config_vars.rule_calea_type)
		logger.debug('SecurityPage : Writing Welcome Text.')
		self.welcome_text.set(self.config.config_vars.edit_welcome_text_new_value)
		logger.debug('SecurityPage : Writing Policy Text.')
		self.policy_text.set(self.config.config_vars.edit_policy_text_new_value)
		# self.background_color.set(self.config.config_vars.rule_calea_type)
		logger.debug('SecurityPage : Writing Resirect url.')
		self.redirect_url.set(self.config.config_vars.valid_redirect_url)
		logger.debug('SecurityPage : Clicking on Save button.')
		self.save_button.click()
		
	def create_wireless_guest_with_mac_auth_enabled(self):
		logger.debug("SecurityPage : Selecting internal authenticated  .")
		self.splash_page_type.set(self.config.config_vars.Splash_page_Authenticated)
		logger.debug("SecurityPage : Enable mac authentication.")
		self.mac_authentication.set(self.config.config_vars.Security_Mac_Authentication_Enabled)
		logger.debug("SecurityPage: selecting new from dropdown")
		self.authentication_server.set(self.config.config_vars.new_server)
		self.buy_time()
		logger.debug('SecurityPage : Clicking on Save Server button.')
		self.save_server.click()
		self.buy_time()
		logger.debug("SecurityPage : Write Server name")
		self.auth_server_name.set(self.config.config_vars.invalid_input)
		if not self.name_error:
			raise AssertionError("Server name error. i.e. Traceback: %s" %traceback.format_exc())
		self.buy_time()
		logger.debug("SecurityPage : Write Server name")
		self.auth_server_name.set(self.config.config_vars.auth_server_name)
		logger.debug("SecurityPage : Write Server ip address")
		self.auth_ipaddr.set(self.config.config_vars.invalid_input)
		logger.debug('SecurityPage : Clicking on Save Server button.')
		self.save_server.click()
		if not self.ip_error:
			raise AssertionError("Invalid IP. i.e. Traceback: %s" %traceback.format_exc())
		self.buy_time()
		logger.debug("SecurityPage : Write Server ip address")
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr)
		
		logger.debug("SecurityPage : Write Shared key.")
		self.Auth_Sharedkey.set(self.config.config_vars.invalid_input)
		if not self.shared_key_error:
			raise AssertionError("Length error. i.e. Traceback: %s" %traceback.format_exc())
		self.buy_time()
		logger.debug("SecurityPage : Write Shared key.")
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey)
		
		logger.debug("SecurityPage : Write retype - Shared key.")
		self.Retype_auth_shared_key.set(self.config.config_vars.pswdTxt)
		logger.debug('SecurityPage : Clicking on Save Server button.')
		self.save_server.click()
		if not self.retype_shared_key_error:
			raise AssertionError("Fields do not match error. i.e. Traceback: %s" %traceback.format_exc())
		self.buy_time()
		logger.debug("SecurityPage : Write retype - Shared key.")
		self.Retype_auth_shared_key.set(self.config.config_vars.Retype_auth_shared_key)
		self.buy_time()
		logger.debug("SecuritPage: Write DRP vlan value")
		if not self.drpvlan_disabled:
			self.drpvlan.set(self.config.config_vars.reauth_value)
		logger.debug('SecurityPage : Clicking on Save Server button.')
		self.save_server.click()
		self.buy_time()
		logger.debug('SecurityPage: selecting InternalServer')
		self.authentication_server_2.set(self.config.config_vars.InternalServer)
		logger.debug("SecurityPage: Writing reauth")
		self.reauth_interval.set(self.config.config_vars.reauth_interval)
		logger.debug("SecurityPage: Clicking on internal server user link ")
		self.show_users_link.click()
		self.buy_time()
		logger.debug("SecurityPage: Clicking on add button")
		self.updateButton.click()
		self.buy_time()
		self.assert_new_user_feild_error_msg()
		self.buy_time()
		self.userTxt.set(self.config.config_vars.userTxt)
		self.pswdTxt.set(self.config.config_vars.pswdTxt)
		self.pswdTxt2.set(self.config.config_vars.pswdTxt2)
		self.typeTxt.set(self.config.config_vars.typeTxt)
		self.buy_time()
		logger.debug("SecurityPage: Clicking on add button")
		self.updateButton.click()
		self.buy_time()
		if self.user_name_error:
			logger.debug("SecurityPage: Clicking on Ok button")
			self.ok_button.click()
		logger.debug("SecurityPage: Clicking on Ok button")
		self.okButton.click()
		self.buy_time()
		logger.debug("SecurityPage : Enable Wireless Encryption.")
		self.wireless_encryption.set(self.config.config_vars.wireless_encryption)
		logger.debug('SecurityPage : Setting Key Management to  Both(WPA-2 & WPA)')
		self.security_key_management.set(self.config.config_vars.security_key_management)
		logger.debug('SecurityPage: writing passphrase')
		self.passphrase.set(self.config.config_vars.Network_Passphrase)
		logger.debug('SecurityPage: re writing passphrase')
		self.retype_passphrase.set(self.config.config_vars.Network_Passphrase)
		self.buy_time()
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()	
		return AccessPage(self.test, self.browser, self.config)
		
	def assert_new_user_feild_error_msg(self):
		if (self.name_error1 and self.password_error and self.type_error):
			return True
		else:
			raise AssertionError("Feilds are required i.e . Traceback: %s" % traceback.format_exc())
			
	def enable_mac_authentication(self):
		logger.debug("SecurityPage : Enable mac authentication.")
		self.mac_authentication.set(self.config.config_vars.Security_Mac_Authentication_Enabled)
		if self.passphrase:
			logger.debug("SecurityPage : Write passphrase.")
			self.passphrase.set(self.config.config_vars.Network_Passphrase)
			logger.debug("SecurityPage : Confirm passphrase.")
			self.retype_passphrase.set(self.config.config_vars.Network_Passphrase)
			self.buy_time()
		# self.next.click()	
		# return AccessPage(self.test, self.browser, self.config)
	
	
	def set_splash_page_none(self):
		logger.debug("SecurityPage : Set splash page none.")
		self.splash_page_type.set(self.config.config_vars.Splash_page_none)
		
	def set_802_roaming_dropdown(self):
		logger.debug('SecurityPage : Clicking on open radio button')	
		self.open_radio_button.click()
		time.sleep(6)
		logger.debug('SecurityPage : Enabling mac authentication server')
		self.mac_authentication.set(self.config.config_vars.enable_option)
		time.sleep(6)
		logger.debug("SecurityPage : Setting 802.11r roaming to Enabled")
		self.roaming_open.click()
		self.buy_time()
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()	
		return AccessPage(self.test, self.browser, self.config)
	
	def set_mac_authentication_dropdown(self):
		logger.debug('SecurityPage : Clicking on open radio button')	
		self.open_radio_button.click()
		time.sleep(6)
		logger.debug('SecurityPage : Enabling mac authentication server')
		self.mac_authentication.set(self.config.config_vars.enable_option)
		time.sleep(6)
		# logger.debug("SecurityPage : Setting MAC_Authentication to Disabled")
		# self.mac_authentication.set(self.config.config_vars.disable_option)
		self.buy_time()
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()	
		return AccessPage(self.test, self.browser, self.config)
			
	def set_mac_authentication_auth_server_2_options(self):
		logger.debug('SecurityPage : Clicking on open radio button')	
		self.open_radio_button.click()
		time.sleep(6)
		logger.debug('SecurityPage : Enabling mac authentication server')
		self.mac_authentication.set(self.config.config_vars.enable_option)
		time.sleep(6)
		logger.debug("SecurityPage : Setting MAC_Authentication to Enabled")
		self.mac_authentication.set(self.config.config_vars.mac_authentication_value)
		logger.debug('EditNetworkPage : Setting new external server to Authentication Server 1')
		self.authentication_server.set(self.config.config_vars.new_external_server)
		time.sleep(3)
		logger.debug('EditNetworkPage : Entering details')
		self.auth_server_name.set(self.config.config_vars.auth_server_value)
		logger.debug("SecurityPage : Writing Server ip address")
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr_value)
		logger.debug('SecurityPage : Writing auth Sharedkey value')
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug("SecurityPage : Write retype - Shared key.")
		self.Retype_auth_shared_key.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug("SecuritPage: Write DRP vlan value")
		if not self.drpvlan_disabled:
			self.drpvlan.set(self.config.config_vars.reauth_value)
		logger.debug('EditNetworkPage : Saving external radius server')
		self.save_server.click()
		time.sleep(12)
		logger.debug('EditNetworkPage : Setting new external server to Authentication Server 2')
		self.authentication_server_2.set(self.config.config_vars.new_external_server)
		time.sleep(3)
		logger.debug('EditNetworkPage : Entering details')
		self.auth_server_name.set(self.config.config_vars.auth_server_value_2)
		logger.debug("SecurityPage : Writing Server ip address")
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr_value)
		logger.debug('SecurityPage : Writing auth Sharedkey value')
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug("SecurityPage : Write retype - Shared key.")
		self.Retype_auth_shared_key.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug("SecuritPage: Write DRP vlan value")
		if not self.drpvlan_disabled:
			self.drpvlan.set(self.config.config_vars.reauth_value)
		logger.debug('EditNetworkPage : Saving external radius server')
		self.save_server.click()
		time.sleep(12)
		logger.debug('EditNetworkPage : Editing Accounting dropdown')
		self.accounting.set(self.config.config_vars.accounting_enabled)
		logger.debug('EditNetworkPage : Entering invalid value in Accouting Interval')
		self.accounting_interval.set(self.config.config_vars.invalid_accounting)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.accounting_interval_error_msg:
			raise AssertionError("Invalid accounting message is not visible. i.e . Traceback: %s" % traceback.format_exc())	
		logger.debug('EditNetworkPage : Entering valid value in Accouting Interval')
		self.accounting_interval.set(self.config.config_vars.valid_accounting)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()	
		return AccessPage(self.test, self.browser, self.config)

	def assert_security_level_default_options(self,default=False,open_level=False):
		logger.debug("SecurityPage :Check default security level option.")
		if not default:
			if not self.personal.is_selected():
				raise AssertionError("Security level not personal by default. i.e . Traceback: %s" % traceback.format_exc())
		elif open_level:
			logger.debug("SecurityPage :Click on open.")			
			self.open_security.click()
			if not self.encrytion_text:
				raise AssertionError("SecurityPage : Encryption uneditable text not visible. i.e . Traceback: %s" % traceback.format_exc())			
		else:
			logger.debug("SecurityPage :Click on enterprise.")			
			self.enteprise.click()
			if not self.enteprise.is_selected():
				raise AssertionError("Security level Enterprise not selected. i.e . Traceback: %s" % traceback.format_exc())
	
	def assert_key_management_values(self,personal=False):
		logger.debug("SecurityPage :Assert key management options")
		if not personal:
			if not self.security_key_management.selected == self.config.config_vars.Authentication_wpa2:
				raise AssertionError("Key management not set to wpa2 personal. . i.e . Traceback: %s" % traceback.format_exc())
		else:
			logger.debug("SecurityPage :Check key management when security level is enterprise.")
			if not self.security_key_management.selected == self.config.config_vars.wpa2_enterprise:
				raise AssertionError("Key management not set to wpa2 enterprise. . i.e . Traceback: %s" % traceback.format_exc())

	def set_roaming_to_enable(self):
		logger.debug('SecurityPage : Clicking on open radio button')	
		self.open_radio_button.click()
		time.sleep(6)
		logger.debug('SecurityPage : Enabling mac authentication server')
		self.mac_authentication.set(self.config.config_vars.enable_option)
		time.sleep(6)
		logger.debug('SecurityPage : Setting roaming to Enabled')
		self.roaming_open.click()
		time.sleep(2)
		logger.debug("SecurityPage : Clicking on Next.")
		self.next.click()
		return AccessPage(self.test, self.browser, self.config)
	
	def set_blacklisting_and_max_authentication_failure(self):
		logger.debug('SecurityPage : Clicking on open radio button')	
		self.open_radio_button.click()
		time.sleep(6)
		logger.debug('SecurityPage : Enabling mac authentication server')
		self.mac_authentication.set(self.config.config_vars.enable_option)
		time.sleep(6)
		logger.debug('SecurityPage : Setting roaming to Enabled')
		self.roaming_open.click()
		time.sleep(2)
		logger.debug('SecurityPage : Setting blacklisting to enabled')
		self.blacklisting.set(self.config.config_vars.blacklisting_option)
		time.sleep(2)		
		logger.debug("SecurityPage : Entering in invalid value in max authentication.")
		self.max_auth_failures.set('')
		logger.debug("SecurityPage : Clicking on Next.")
		self.next.click()
		if not self.max_auth_fail_error_msg:
			raise AssertionError("Max authentication error is not visible. i.e. Traceback: %s" %traceback.format_exc())
		logger.debug("SecurityPage : Entering in valid value in max authentication.")
		self.max_auth_failures.set(self.config.config_vars.max_authentication_failure)
		logger.debug("SecurityPage : Clicking on Next.")
		self.next.click()
		return AccessPage(self.test, self.browser, self.config)

	def security_level_enterprise(self):
		logger.debug("SecurityPage :Click on enterprise.")
		self.enteprise.click()

	def configure_80211r_romaing(self,skip_next=False):
		logger.debug("SecurityPage : Enable 802.11r ROAMING.")
		self.roaming_open.click()


	def assert_auth_server_one_defaults(self):
		logger.debug("SecurityPage : Check default value of auth server name .")		
		if not self.authentication_server.selected == self.config.config_vars.InternalServer:
			raise AssertionError("Auth server 1 not set to Internal server . i.e . Traceback: %s" % traceback.format_exc())
		
	def _set_phrase(self):
		logger.debug("SecurityPage : Set passphrase.")
		self.passphrase.set(self.config.config_vars.Network_Passphrase)
		logger.debug("SecurityPage : Set retype passphrase .")
		self.retype_passphrase.set(self.config.config_vars.Network_Passphrase)
		
	def set_auth_interval_time(self,value):
		if value == '180':
			logger.debug("SecurityPage : Set auth interval time.")		
			self.reauth_interval.set(self.config.config_vars.reauth_interval)
		elif value == '10':
			logger.debug("SecurityPage : Set auth interval time to 10.")		
			self.reauth_interval.set(self.config.config_vars.reauth_interval10)
		
	def set_mac_authentication_enabled(self):
		logger.debug("SecurityPage : Enable Mac Authentication Fail-thru.")
		self.auth_failthru_enterprise.click()
		logger.debug("SecurityPage : Enable  Perform MAC authentication before 802.1x.")
		self.mac_authentication_enterprise.click()
		logger.debug("SecurityPage : Enable  okc.")
		self.okc_checkbox.click()
		logger.debug("SecurityPage : Enable  uppercase support.")		
		self.personal_uppercase_support.set(self.config.config_vars.Uppercase_Support_Enabled)
		
	def set_mac_authentication_auth_server_delimeter_uppercase_options(self):
		'''
			setting mac authentication, delimeter, uppercase support options, Creating external radius server
		'''
		logger.debug('SecurityPage : Clicking on open radio button')	
		self.open_radio_button.click()
		time.sleep(6)
		logger.debug('SecurityPage : Enabling mac authentication server')
		self.mac_authentication.set(self.config.config_vars.enable_option)
		logger.debug('SecurityPage : Entering delimeter value')
		self.personal_delimeter.set(self.config.config_vars.delimeter_value)
		logger.debug('SecurityPage : Enabling uppercase support')
		self.personal_uppercase_support.set(self.config.config_vars.Uppercase_Support_Enabled)
		logger.debug('SecurityPage : Setting new external server to Authentication Server 1')
		self.authentication_server.set(self.config.config_vars.new_external_server)
		time.sleep(3)
		logger.debug('SecurityPage : Entering details')
		self.auth_server_name.set(self.config.config_vars.auth_server_value)
		logger.debug("SecurityPage : Writing Server ip address")
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr_value)
		logger.debug('SecurityPage : Writing auth Sharedkey value')
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug("SecurityPage : Write retype - Shared key.")
		self.Retype_auth_shared_key.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug("SecuritPage: Write DRP vlan value")
		if not self.drpvlan_disabled:
			self.drpvlan.set(self.config.config_vars.reauth_value)
		logger.debug('SecurityPage : Saving external radius server')
		self.save_server.click()
		time.sleep(12)
		logger.debug('SecurityPage : Setting new external server to Authentication Server 2')
		self.authentication_server_2.set(self.config.config_vars.new_external_server)
		time.sleep(3)
		logger.debug('SecurityPage : Entering details')
		self.auth_server_name.set(self.config.config_vars.auth_server_value_2)
		logger.debug("SecurityPage : Writing Server ip address")
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr_value)
		logger.debug('SecurityPage : Writing auth Sharedkey value')
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug("SecurityPage : Write retype - Shared key.")
		self.Retype_auth_shared_key.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug("SecuritPage: Write DRP vlan value")
		if not self.drpvlan_disabled:
			self.drpvlan.set(self.config.config_vars.reauth_value)
		logger.debug('SecurityPage : Saving external radius server')
		self.save_server.click()
		time.sleep(12)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()	
		return AccessPage(self.test, self.browser, self.config)
	
	def set_mac_authentication_auth_server_accounting_options(self):
		'''
		setting mac authentication, Creating external radius server
		''' 
		logger.debug('SecurityPage : Clicking on open radio button') 
		self.open_radio_button.click()
		time.sleep(5)
		logger.debug('SecurityPage : Enabling mac authentication server')
		self.mac_authentication.set(self.config.config_vars.enable_option)
		logger.debug('EditNetworkPage : Setting new external server to Authentication Server 1')
		self.create_external_radiuds_server('1')
		time.sleep(20)
		logger.debug('EditNetworkPage : Setting external server to Authentication Server 2')
		self.create_external_radiuds_server('2')
		self.enable_accounting_interval('60')
		logger.debug("SecurityPage : Clicking on next") 
		self.next.click() 
		return AccessPage(self.test, self.browser, self.config)
		
	def configure_security_level(self,enterprise=False,open=False):
		'''
		Configure security level 
		If enterprise true then enable enterprise radio button.
		If open true then enable open radion button.
		default : Personal
		'''
		if enterprise:
			logger.debug("SecurityPage : Enable enterprise.")
			self.enteprise.click()
		elif open:
			logger.debug("SecurityPage : Enable open.")
			self.open_security.click()
		else:
			logger.debug("SecurityPage : Enable personal.")
			self.personal.click()
			
	def assert_default_fields_security_personal(self,wpa_wpa2=False,wpa=False,skip_roaming=False):
		'''
		To verify the default value of other fields if security level is selected as Personal and key management is WPA 2.
		'''
		
		if wpa_wpa2:
			logger.debug("SecurityPage :Set key management to both wpa2 and wpa.")
			self.security_key_management.set(self.config.config_vars.Authentication_Wpa2_WPA_Enterprise)
		if wpa:
			logger.debug("SecurityPage :Set key management to wpa personal.")
			self.security_key_management.set(self.config.config_vars.wpa_personal)

		if skip_roaming:
			if self.invisble_roaming_open :
				logger.debug("SecurityPage :802 roaming options not valid for wpa personal ")
		else:
			logger.debug("SecurityPage :Check default option of  802 roaming. ")
			if  self.roaming_open.is_selected():
				raise AssertionError("Default value is not disabled . i.e . Traceback: %s" % traceback.format_exc())
			logger.debug("since 802.11r roaming field is changed from dropdown to checkbox we can't verify enabled and disabled option")
# 			logger.debug("SecurityPage :Check 802 roaming options enable option")
# 			if not self.roaming_open.options[1] ==  self.config.config_vars.enable_option:
# 				raise AssertionError("Enabled option missing . i.e . Traceback: %s" % traceback.format_exc())
# 			logger.debug("SecurityPage :Check 802 roaming  disabled option")		
# 			if not self.roaming_open.options[0] ==  self.config.config_vars.disable_option:
# 				raise AssertionError("Disabled option missing . i.e . Traceback: %s" % traceback.format_exc())

		logger.debug("SecurityPage :Check Pass phrase Format 8-63 Chars.")
		if not self.wpa_passphrase_format.options[0] ==  self.config.config_vars.pass_phrase_format_8_63_chars:
			raise AssertionError("Enabled option missing . i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage :Check 802 roaming  disabled option")		
		if not self.wpa_passphrase_format.options[1] ==  self.config.config_vars.pass_phrase_format_64_hexa_chars:
			raise AssertionError("Disabled option missing . i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage :Check default option of  802 roaming ")
		if not self.wpa_passphrase_format.selected == self.config.config_vars.pass_phrase_format_8_63_chars:
			raise AssertionError("Default value is not disabled . i.e . Traceback: %s" % traceback.format_exc())
		
		logger.debug("SecurityPage :Check if default pass phrase is empty.")
		default_value = self.passphrase.get()
		if not default_value == '':
			raise AssertionError(" pass phrase is not empty. i.e . Traceback: %s" % traceback.format_exc())

		logger.debug("SecurityPage :Check if default retype pass phrase is empty.")
		default_value = self.retype_passphrase.get()
		if not default_value == '':
			raise AssertionError(" re type pass phrase is not empty. i.e . Traceback: %s" % traceback.format_exc())
		
		self.assert_mac_authentication_parameterlist_and_defaults()
		self.assert_blacklisting_parameterlist_and_defaults()
		
	def assert_default_fields_security_enterprise(self,wpa_wpa2=False,wpa=False,skip_roaming_okc=False,dynamic_wep=False,assert_session_key=False):
		'''
		To verify the default value in security form while creation if Security level is selected as Enterprise and Key Management is Both (WPA & WPA2)
		'''
		
		if wpa_wpa2:
			logger.debug("SecurityPage :Set key management to both wpa2 and wpa.")
			self.security_key_management.set(self.config.config_vars.Authentication_Wpa2_WPA_Enterprise)
		if wpa:
			logger.debug("SecurityPage :Set key management to wpa enterprise.")
			self.security_key_management.set(self.config.config_vars.Authentication_Wpa_Enterprise)
		if dynamic_wep:
			logger.debug("SecurityPage :Set key management to dynamic wep.")
			self.security_key_management.set(self.config.config_vars.enterprise_key_mgt_value)
			
		if skip_roaming_okc:
			logger.debug("SecurityPage :802 roaming options and okc opions not valid for wpa enterprise ")
		else:
			logger.debug("SecurityPage :Check okc option default checkbox.")
			if self.okc_checkbox.is_selected():
				raise AssertionError("Okc option is Enabled . i.e . Traceback: %s" % traceback.format_exc())
			
			logger.debug("SecurityPage :Check default option of  802 roaming. ")
			if  self.roaming_open.is_selected():
				raise AssertionError("Default value is not disabled . i.e . Traceback: %s" % traceback.format_exc())
			logger.debug("since 802.11r roaming field is changed from dropdown to checkbox we can't verify enabled and disabled option")
# 			logger.debug("SecurityPage :Check 802 roaming options enable option")
# 			if not self.roaming_open.options[1] ==  self.config.config_vars.enable_option:
# 				raise AssertionError("Enabled option missing . i.e . Traceback: %s" % traceback.format_exc())
# 			logger.debug("SecurityPage :Check 802 roaming  disabled option")		
# 			if not self.roaming_open.options[0] ==  self.config.config_vars.disable_option:
# 				raise AssertionError("Disabled option missing . i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage :Check default option of  termination. ")
		if not self.termination.selected == self.config.config_vars.disable_option:
			raise AssertionError("Default value is not disabled . i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage :Check termination options enable option")
		if not self.termination.options[1] ==  self.config.config_vars.enable_option:
			raise AssertionError("Enabled option missing . i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage :Check termination  disabled option")		
		if not self.termination.options[0] ==  self.config.config_vars.disable_option:
			raise AssertionError("Disabled option missing . i.e . Traceback: %s" % traceback.format_exc())
		
		logger.debug("SecurityPage :Check default value of reauth interval.")
		default_value = self.reauth_interval.get()
		if not default_value == self.config.config_vars.reauth_interval_default_value:
			raise AssertionError(" Default value of reauth interval is not 0. i.e . Traceback: %s" % traceback.format_exc())
		
		logger.debug("SecurityPage : Check default value of auth server 1.")
		if not self.authentication_server.selected==self.config.config_vars.InternalServer:
			raise AssertionError("default value is not InternalServer .Traceback: %s " %traceback.format_exc())
		logger.debug("SecurityPage : Check for new option in auth server 1.")
		# if not self.authentication_server.options[1]== '-- New --':
			# raise AssertionError("default value is not InternalServer .Traceback: %s " %traceback.format_exc())
	
		logger.debug("SecurityPage :Check Perform MAC authentication before 802.1x default option.")		
		if self.mac_authentication_enterprise.is_selected():
			raise AssertionError("Perform MAC authentication before 802.1x is enabled . i.e . Traceback: %s" % traceback.format_exc())
		
		logger.debug("SecurityPage :Check Mac Authentication Fail-thru default option.")		
		if self.auth_failthru_enterprise.is_selected():
			raise AssertionError("Mac Authentication Fail-thru is enabled . i.e . Traceback: %s" % traceback.format_exc())

		self.assert_blacklisting_parameterlist_and_defaults()
		
		if assert_session_key:
			logger.debug("SecurityPage :Check leap use session key default option.")		
			if self.leap_use_session_key.is_selected():
				raise AssertionError("Mac Authentication Fail-thru is enabled . i.e . Traceback: %s" % traceback.format_exc())
			
	def assert_default_feilds_security_enterprise_mac_enabled(self):
		'''
		To verify the default value of Employee network in Enterprise security level with MAC enabled.
		'''
		logger.debug("SecurityPage :Check the Mac Authentication - Perform MAC authentication before 802.1x.")		
		self.enterprise_mac_authentication.click()
# 		if not self.personal_uppercase_support.selected=='Disabled':
# 			raise AssertionError("Uppercase support is not disabled by default .Traceback: %s " %traceback.format_exc())
# 		self.personal_uppercase_support.set(self.config.config_vars.Uppercase_Support_Enabled)

		logger.debug("SecurityPage :Check if delimeter character is empty.")
		default_value = self.personal_delimeter.get()
		if not default_value == '':
			raise AssertionError(" Delimeter is not empty. i.e . Traceback: %s" % traceback.format_exc())
		
		logger.debug("SecurityPage :Check default option of  uppercase support. ")
		if not self.personal_uppercase_support.selected == self.config.config_vars.disable_option:
			raise AssertionError("Default value is not disabled . i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage :Check uppercase support options enable option")
		if not self.personal_uppercase_support.options[1] ==  self.config.config_vars.enable_option:
			raise AssertionError("Enabled option missing . i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage :Check uppercase support  disabled option")		
		if not self.personal_uppercase_support.options[0] ==  self.config.config_vars.disable_option:
			raise AssertionError("Disabled option missing . i.e . Traceback: %s" % traceback.format_exc())
		
	def assert_default_feilds_security_mac_enabled(self):
		'''
		To verify the default value of Employee network in Personal security level with MAC enabled.
		'''
		logger.debug("SecurityPage :Enable mac authentication.")
		self.mac_authentication.set(self.config.config_vars.enable_option)

		logger.debug("SecurityPage :Check if delimeter character is empty.")
		default_value = self.personal_delimeter.get()
		if not default_value == '':
			raise AssertionError(" Delimeter is not empty. i.e . Traceback: %s" % traceback.format_exc())

		logger.debug("SecurityPage :Check default option of  uppercase support. ")
		if not self.personal_uppercase_support.selected == self.config.config_vars.disable_option:
			raise AssertionError("Default value is not disabled . i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage :Check uppercase support options enable option")
		if not self.personal_uppercase_support.options[1] ==  self.config.config_vars.enable_option:
			raise AssertionError("Enabled option missing . i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage :Check uppercase support  disabled option")		
		if not self.personal_uppercase_support.options[0] ==  self.config.config_vars.disable_option:
			raise AssertionError("Disabled option missing . i.e . Traceback: %s" % traceback.format_exc())

		logger.debug("SecurityPage : Check default value of auth server 1.")
		if not self.authentication_server.selected==self.config.config_vars.InternalServer:
			raise AssertionError("default value is not InternalServer .Traceback: %s " %traceback.format_exc())
		logger.debug("SecurityPage : Check for new option in auth server 1.")
		if not self.authentication_server.options[1]== '-- New --':
			raise AssertionError("default value is not InternalServer .Traceback: %s " %traceback.format_exc())
		
		logger.debug("SecurityPage :Check default value of reauth interval.")
		default_value = self.reauth_interval.get()
		if not default_value == self.config.config_vars.reauth_interval_default_value:
			raise AssertionError(" Default value of reauth interval is not 0. i.e . Traceback: %s" % traceback.format_exc())
		
	def assert_default_feilds_security_blacklisting_enabled(self):
		logger.debug('SecurityPage : Setting blacklisting to enabled')
		self.blacklisting.set(self.config.config_vars.blacklisting_option)
		
		logger.debug("SecurityPage :Check default value of max authentication failure.")
		default_value = self.max_auth_failures.get()
		if not default_value == self.config.config_vars.max_authentication_default_value:
			raise AssertionError(" Default value of max authentication failure is not 0. i.e . Traceback: %s" % traceback.format_exc())
		
	def create_external_radius_server_in_auth_server_one(self):
		'''
		Create new external radius in auth server 1 
		'''
		logger.debug('SecurityPage : Setting new external server to Authentication Server 1')
		self.authentication_server.set(self.config.config_vars.new_external_server)
		logger.debug('SecurityPage : Writing details')
		self.auth_server_name.set(self.config.config_vars.auth_server_value)
		logger.debug('SecurityPage : Writing auth ipaddr value')
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr_value)
		logger.debug('SecurityPage : Writing auth Sharedkey value')
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug('SecurityPage : re Writing auth Sharedkey value')
		self.Retype_auth_shared_key.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug("SecuritPage: Write DRP vlan value")
		if not self.drpvlan_disabled:
			self.drpvlan.set(self.config.config_vars.reauth_value)
		logger.debug('SecurityPage : Saving external radius server')
		self.save_server.click()
		self.buy_time()
		if self.drpvlan_error:
			self.drpvlan.set(self.config.config_vars.reauth_2)
			self.save_server.click()
		
	def assert_default_feilds_security_termination_enabled(self):		
		logger.debug("SecurityPage :Enable termination. ")
		self.termination.set(self.config.config_vars.enable_option)
		if self.config.config_vars.InternalServer in self.authentication_server.options:
			raise AssertionError("Internal server visible in auth server 1 options . i.e . Traceback: %s" % traceback.format_exc())
		self.create_external_radius_server_in_auth_server_one()
		logger.debug("SecurityPage :Check if Accounting option is visible to user for Termination enabled.")		
		if self.accounting:
			raise AssertionError("Accounting option visible for user  . i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage :Check if Auth server 2 option is visible and configurable if auth server is 1 .")
		if self.authentication_server_2:
			raise AssertionError("Auth server 2 is visible and configurable. i.e . Traceback: %s" % traceback.format_exc())
		

	def assert_default_feilds_security_static_wep(self):
		'''
		To verify the default value of other fields if security level is selected as Personal and key management is Static WEP
		'''
		logger.debug("SecurityPage :Set key management to Static wep.")		
		self.security_key_management.set(self.config.config_vars.personal_key_mgt_value)
		
		logger.debug("SecurityPage :Check default option of  wep key. ")
		if not self.wep_key_size.selected == self.config.config_vars.wep_key_option_1:
			raise AssertionError("Default value is not 128 bit . i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage :Check 64 bit option in Wep key dropdown.")
		if not self.wep_key_size.options[1] ==  self.config.config_vars.wep_key_option_2:
			raise AssertionError("64 bit option is missing . i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage :Check 128 bit option in Wep key dropdown")		
		if not self.wep_key_size.options[0] ==  self.config.config_vars.wep_key_option_1:
			raise AssertionError("128 bit option is missing . i.e . Traceback: %s" % traceback.format_exc())
		
		logger.debug("SecurityPage :Check Tx Key Dropdown parameter list")		
		options = self.wep_key_index.get_options()
		for x in range(0,4):
			if not options[x] == str(x+1):
				raise AssertionError("Transit power not visible: %s " %traceback.format_exc())
			
		logger.debug("SecurityPage :Check if wep key is empty.")
		default_value = self.personal_wep_key.get()
		if not default_value == '':
			raise AssertionError("wep key is not empty. i.e . Traceback: %s" % traceback.format_exc())
			
		logger.debug("SecurityPage :Check if retype wep key is empty.")
		default_value = self.personal_re_wep_key.get()
		if not default_value == '':
			raise AssertionError(" re type wep key is not empty. i.e . Traceback: %s" % traceback.format_exc())
		self.assert_mac_authentication_parameterlist_and_defaults()
		self.assert_blacklisting_parameterlist_and_defaults()
		
	
	def assert_mac_authentication_parameterlist_and_defaults(self):
		'''
		Check parameter list of mac authentication and default value.
		'''
		logger.debug("SecurityPage :Check default option of mac authentication.")
		if not self.mac_authentication.selected ==  self.config.config_vars.disable_option:
			raise AssertionError("Default option is not disabled . i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage :Check mac authentication options enable option")
		if not self.mac_authentication.options[1] ==  self.config.config_vars.enable_option:
			raise AssertionError("Enabled option missing . i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage :Check mac authentication  disabled option")		
		if not self.mac_authentication.options[0] ==  self.config.config_vars.disable_option:
			raise AssertionError("Disabled option missing . i.e . Traceback: %s" % traceback.format_exc())
		
	def assert_blacklisting_parameterlist_and_defaults(self):
		'''
		Check parameter list of blacklisting and default value.
		'''		
		logger.debug("SecurityPage :Check default option of blacklisitng")		
		if not self.blacklisting.selected ==  self.config.config_vars.disable_option:
			raise AssertionError("Blacklist default not set to Disabled . i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage :Check blacklisiting options enable option")
		if not self.blacklisting.options[1] ==  self.config.config_vars.enable_option:
			raise AssertionError("Enabled option missing . i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage :Check blacklisiting  disabled option")		
		if not self.blacklisting.options[0] ==  self.config.config_vars.disable_option:
			raise AssertionError("Disabled option missing . i.e . Traceback: %s" % traceback.format_exc())

	def _set_security_level(self, level):
		logger.debug("SecurityPage : Clicking '%s' radio button..." %level)
		if level == 'enterprise':
			self.enteprise.click()
		elif level == 'personal':
			self.personal.click()
		elif level == 'open':
			self.open_security.click()
			
	def validate_reauth_interval(self, level, unit):
		logger.debug("SecurityPage : Calling _set_security_level method  .")
		self._set_security_level(level)
		if level == 'personal':
			logger.debug("SecurityPage : Setting 'MAC AUTHENTICATION' to 'Enabled'...")
			self.mac_authentication.set(self.config.config_vars.Security_Mac_Authentication_Enabled)
			logger.debug("SecurityPage : Writing passphrase...")
			self.passphrase.set(self.config.config_vars.Auth_Sharedkey)
			logger.debug("SecurityPage : rewriting passphrase...")
			self.retype_passphrase.set(self.config.config_vars.Auth_Sharedkey)
		self.validate_reauth_interval_field(unit)
		logger.debug("SecurityPage : Writing valid numbers in reauth interval text-box...")
		self.reauth_interval.set(self.config.config_vars.reauth_intrvl_num_valid)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if (self.reauth_interval_error_msg_mins or self.reauth_interval_error_msg_hrs):
			raise AssertionError("'Must be a number' error message found. i.e . Traceback: %s" % traceback.format_exc())
			
	def validate_cache_timeout(self):
		logger.debug("SecurityPage : Calling _set_security_level method  .")
		self._set_security_level('enterprise')
		logger.debug("SecurityPage : Calling create_external_radiuds_server method  .")
		self.create_external_radiuds_server('1')
		logger.debug("SecurityPage : Setting authentication survivability to 'Enabled'.")
		self.auth_survivability.set(self.config.config_vars.auth_survivability_enable)
		logger.debug("SecurityPage : Writing alphabet in 'Cache Timeout' text-box.")
		self.cache_timeout.set(self.config.config_vars.reauth_intrvl_alpha)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.cache_timeout_field_error:
			raise AssertionError("'Must be a number' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing invalid number in 'Cache Timeout' text-box.")
		self.cache_timeout.set(self.config.config_vars.cache_timeout_invalid_num)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.cache_timeout_field_error:
			raise AssertionError("'Must be a number' error message not found. i.e. Traceback: %s" %traceback.format_exc())
		
		logger.debug("SecurityPage : Writing special character in 'Cache Timeout' text-box.")
		self.cache_timeout.set(self.config.config_vars.reauth_intrvl_spcl_char)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.cache_timeout_field_error:
			raise AssertionError("'Must be a number' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing null character in 'Cache Timeout' text-box.")
		self.cache_timeout.set('')
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.cache_timeout_field_error:
			raise AssertionError("'Must be a number' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing valid number in 'Cache Timeout' text-box.")
		self.cache_timeout.set(self.config.config_vars.accounting_intrvl_valid)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if self.cache_timeout_field_error:
			raise AssertionError("'Must be a number' error message found. i.e. Traceback: %s" %traceback.format_exc())
			
	def validate_enterprise_delimeter(self, level):
		logger.debug("SecurityPage : Calling _set_security_level method  .")
		self._set_security_level(level)
		if level == 'enterprise':
			logger.debug("SecurityPage : Checking 'Perform MAC authentication before 802.1X' check box.")
			self.mac_authentication_enterprise.click()
		elif level == 'personal':
			logger.debug("SecurityPage : Setting 'MAC AUTHENTICATION' to 'Enabled'...")
			self.mac_authentication.set(self.config.config_vars.Security_Mac_Authentication_Enabled)
			logger.debug("SecurityPage : Writing passphrase...")
			self.passphrase.set(self.config.config_vars.Auth_Sharedkey)
			logger.debug("SecurityPage : rewriting passphrase...")
			self.retype_passphrase.set(self.config.config_vars.Auth_Sharedkey)
		logger.debug("SecurityPage : Writing alphabet in 'Delimiter character' text box.")
		self.personal_delimeter.set(self.config.config_vars.reauth_intrvl_alpha)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.delimiter_char_error:
			raise AssertionError("'it should accept only : / , - space' error message present. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing numbers in 'Delimiter character' text box.")
		self.personal_delimeter.set(self.config.config_vars.reauth_intrvl_num_valid)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.delimiter_char_error:
			raise AssertionError("'it should accept only : / , - space' error message present. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing special chars in 'Delimiter character' text box.")
		self.personal_delimeter.set(self.config.config_vars.reauth_intrvl_spcl_char)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.delimiter_char_error:
			raise AssertionError("'it should accept only : / , - space' error message present. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing two special chars in 'Delimiter character' text box.")
		self.personal_delimeter.set(self.config.config_vars.delimiter_char_two)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.delimiter_char_error:
			raise AssertionError("more than one character is being accepted. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing null chars in 'Delimiter character' text box.")
		self.personal_delimeter.set('')
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if self.delimiter_char_error:
			raise AssertionError("this field is not optinal. i.e. Traceback: %s" %traceback.format_exc())
		self.back.click()
			
		logger.debug("SecurityPage : Writing valid special chars in 'Delimiter character' text box.")
		self.personal_delimeter.set(self.config.config_vars.delimiter_char_valid)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if self.delimiter_char_error:
			raise AssertionError("'it should accept only : / , - space' error message present. i.e. Traceback: %s" %traceback.format_exc())
			
	def validate_accounting_interval(self, level):
		logger.debug("SecurityPage : Calling _set_security_level method  .")
		self._set_security_level(level)
		if level == 'personal':
			logger.debug("SecurityPage : Setting 'MAC AUTHENTICATION' to 'Enabled'...")
			self.mac_authentication.set(self.config.config_vars.Security_Mac_Authentication_Enabled)
			logger.debug("SecurityPage : Writing passphrase...")
			self.passphrase.set(self.config.config_vars.Auth_Sharedkey)
			logger.debug("SecurityPage : rewriting passphrase...")
			self.retype_passphrase.set(self.config.config_vars.Auth_Sharedkey)
		logger.debug("SecurityPage : Calling create_external_radiuds_server method  .")
		self.create_external_radiuds_server('1')
		if level == 'enterprise':
			logger.debug("SecurityPage : Setting 'TERMINATION' to disabled.")
			self.termination.set(self.config.config_vars.termination_disabled)
		logger.debug("SecurityPage : Setting 'ACCOUNTING' to enabled.")
		self.accounting.set(self.config.config_vars.accounting_enabled)
		logger.debug("SecurityPage : Writing alphabet in 'ACCOUNTING INTERVAL' text box.")
		self.accounting_interval.set(self.config.config_vars.reauth_intrvl_alpha)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.accounting_interval_error_msg:
			raise AssertionError("'Must be a number in range 0-60' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing invalid numbers in 'ACCOUNTING INTERVAL' text box.")
		self.accounting_interval.set(self.config.config_vars.accounting_intrvl_invalid)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.accounting_interval_error_msg:
			raise AssertionError("'Must be a number in range 0-60' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing special characters in 'ACCOUNTING INTERVAL' text box.")
		self.accounting_interval.set(self.config.config_vars.reauth_intrvl_spcl_char)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.accounting_interval_error_msg:
			raise AssertionError("'Must be a number in range 0-60' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing 3 digit number in 'ACCOUNTING INTERVAL' text box.")
		self.accounting_interval.set(self.config.config_vars.reauth_intrvl_num_invalid_hrs)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.accounting_interval_error_msg:
			raise AssertionError("'Must be a number in range 0-60' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing null character in 'ACCOUNTING INTERVAL' text box.")
		self.accounting_interval.set('')
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if self.accounting_interval_error_msg:
			raise AssertionError("'Must be a number in range 0-60' error message found. i.e. Traceback: %s" %traceback.format_exc())
		self.back.click()
			
		logger.debug("SecurityPage : Writing valid number in 'ACCOUNTING INTERVAL' text box.")
		self.accounting_interval.set(self.config.config_vars.accounting_intrvl_valid)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if self.accounting_interval_error_msg:
			raise AssertionError("'Must be a number in range 0-60' error message found. i.e. Traceback: %s" %traceback.format_exc())
			
	def validate_max_authentication_failure(self, level):
		logger.debug("SecurityPage : Calling _set_security_level method  .")
		self._set_security_level(level)
		logger.debug("SecurityPage : Setting 'BLACKLISTING' to enabled.")
		self.blacklisting.set(self.config.config_vars.blacklisting_enabled)
		logger.debug("SecurityPage : Writing alphabets in 'MAX AUTHENTICATION FAILURES' textbox.")
		self.max_auth_failures.set(self.config.config_vars.reauth_intrvl_alpha)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.max_auth_fail_error_msg:
			raise AssertionError("'Must be a number in range 0-10' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing special characters in 'MAX AUTHENTICATION FAILURES' textbox.")
		self.max_auth_failures.set(self.config.config_vars.reauth_intrvl_spcl_char)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.max_auth_fail_error_msg:
			raise AssertionError("'Must be a number in range 0-10' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing invalid numbers in 'MAX AUTHENTICATION FAILURES' textbox.")
		self.max_auth_failures.set(self.config.config_vars.max_auth_failure_invalid_num)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.max_auth_fail_error_msg:
			raise AssertionError("'Must be a number in range 0-10' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing null character in 'MAX AUTHENTICATION FAILURES' textbox.")
		self.max_auth_failures.set('')
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.max_auth_fail_error_msg:
			raise AssertionError("'Must be a number in range 0-10' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing valid value in 'MAX AUTHENTICATION FAILURES' textbox.")
		self.max_auth_failures.set(self.config.config_vars.max_auth_failure_valid_num)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if self.max_auth_fail_error_msg:
			raise AssertionError("'Must be a number in range 0-10' error message found. i.e. Traceback: %s" %traceback.format_exc())
			
	def validate_passphrase_8_to_63_chars(self):
		conf = self.config.config_vars
		# logger.debug("SecurityPage : Calling _set_security_level method  .")
		# self._set_security_level('personal')
		logger.debug("SecurityPage : Setting 'KEY MANAGEMENT' drop down to 'wpa personal'")
		self.security_key_management.set(conf.key_management_wpa)
		logger.debug("SecurityPage : Setting 'PASSPHRASE FORMAT' drop down to '8-63 chars'")
		self.wpa_passphrase_format.set(conf.passphrase_frmt_8_63_char)
		logger.debug("SecurityPage : Writing alphabet in 'PASSPHRASE' text box")
		self.passphrase.set(conf.passphrase_alpha)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if self.passphrase_length_error_msg or self.passphrase_req_error:
			raise AssertionError("alphabet was not accepted. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing numbers in 'PASSPHRASE' text box")
		self.passphrase.set(conf.Retype_auth_shared_key)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if self.passphrase_length_error_msg or self.passphrase_req_error:
			raise AssertionError("number was not accepted. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing special characters in 'PASSPHRASE' text box")
		self.passphrase.set(conf.passphrase_spcl_char)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if self.passphrase_length_error_msg or self.passphrase_req_error:
			raise AssertionError("special character was not accepted. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing invalid passphrase in 'PASSPHRASE' text box")
		self.passphrase.set(conf.reauth_intrvl_num_invalid)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.passphrase_length_error_msg:
			raise AssertionError("'Must be 8-63 characters' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing invalid passphrase in 'PASSPHRASE' text box")
		self.passphrase.set(conf.passphrase_invalid)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.passphrase_length_error_msg:
			raise AssertionError("'Must be 8-63 characters' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing null character in 'PASSPHRASE' text box")
		self.passphrase.set('')
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.passphrase_req_error:
			raise AssertionError("null character was accepted. i.e. Traceback: %s" %traceback.format_exc())
			
	def validate_passphrase_64_hex_chars(self):
		conf = self.config.config_vars
		logger.debug("SecurityPage : Setting 'KEY MANAGEMENT' drop down to 'wpa personal'")
		self.security_key_management.set(conf.key_management_wpa)
		logger.debug("SecurityPage : Setting 'PASSPHRASE FORMAT' drop down to '8-63 chars'")
		self.wpa_passphrase_format.set(conf.passphrase_frmt_64_hex)
		logger.debug("SecurityPage : Writing valid alphabet in 'PASSPHRASE' text box")
		self.passphrase.set(conf.passphrase_hex_alpha_valid)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if self.passphrase_hex_length_err or self.passphrase_req_error:
			raise AssertionError("valid alphabet was not accepted. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing invalid alphabet in 'PASSPHRASE' text box")
		self.passphrase.set(conf.passphrase_hex_alpha_invalid)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.passphrase_hex_length_err:
			raise AssertionError("invalid alphabet was accepted. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing valid numbers in 'PASSPHRASE' text box")
		self.passphrase.set(conf.passphrase_hex_num_valid)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if self.passphrase_hex_length_err or self.passphrase_req_error:
			raise AssertionError("valid number was not accepted. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing special characters in 'PASSPHRASE' text box")
		self.passphrase.set(conf.passphrase_hex_spcl_char)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.passphrase_hex_length_err:
			raise AssertionError("special character was accepted. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing invalid passphrase in 'PASSPHRASE' text box")
		self.passphrase.set(conf.reauth_intrvl_alpha)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.passphrase_hex_length_err:
			raise AssertionError("'Must be 64 hexadecimal characters' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing invalid passphrase in 'PASSPHRASE' text box")
		self.passphrase.set(conf.passphrase_hex_num_invalid)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.passphrase_hex_length_err:
			raise AssertionError("'Must be 64 hexadecimal characters' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing null character in 'PASSPHRASE' text box")
		self.passphrase.set('')
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.passphrase_req_error:
			raise AssertionError("null character was accepted. i.e. Traceback: %s" %traceback.format_exc())
			
	def validate_wep_key_128_bit(self):
		conf = self.config.config_vars
		logger.debug("SecurityPage : Calling _set_security_level method  .")
		self._set_security_level('personal')
		logger.debug("SecurityPage : Setting 'KEY MANAGEMENT' drop down to 'static wep'")
		self.security_key_management.set(conf.key_mngmt_static)
		logger.debug("SecurityPage : Setting 'WEP KEY SIZE' drop down to '128-bit'")
		self.wep_key_size.set(conf.wep_key_size_128)
		logger.debug("SecurityPage : Writing valid alphabet in 'WEP KEY' text box")
		self.personal_wep_key.set(conf.wep_key_alpha_valid)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if self.wep_key_len_error or self.wep_key_req_error:
			raise AssertionError("valid alphabet was not accepted. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing invalid alphabet in 'WEP KEY' text box")
		self.personal_wep_key.set(conf.wep_key_alpha_invalid)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.wep_key_len_error:
			raise AssertionError("invalid alphabet was accepted. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing valid numbers in 'WEP KEY' text box")
		self.personal_wep_key.set(conf.wep_key_num_valid)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if self.wep_key_len_error or self.wep_key_req_error:
			raise AssertionError("valid number was not accepted. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing special characters in 'WEP KEY' text box")
		self.personal_wep_key.set(conf.wep_key_chars)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.wep_key_len_error:
			raise AssertionError("special character was accepted. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing invalid passphrase in 'WEP KEY' text box")
		self.personal_wep_key.set(conf.reauth_intrvl_alpha)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.wep_key_len_error:
			raise AssertionError("'Must be 26 hexadecimal characters' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing invalid passphrase in 'WEP KEY' text box")
		self.personal_wep_key.set(conf.passphrase_hex_num_invalid)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.wep_key_len_error:
			raise AssertionError("'Must be 26 hexadecimal characters' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing null character in 'WEP KEY' text box")
		self.personal_wep_key.set('')
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.wep_key_req_error:
			raise AssertionError("null character was accepted. i.e. Traceback: %s" %traceback.format_exc())
			
	def validate_wep_key_64_bit(self):
		conf = self.config.config_vars
		logger.debug("SecurityPage : Calling _set_security_level method  .")
		self._set_security_level('personal')
		logger.debug("SecurityPage : Setting 'KEY MANAGEMENT' drop down to 'static wep'")
		self.security_key_management.set(conf.key_mngmt_static)
		logger.debug("SecurityPage : Setting 'WEP KEY SIZE' drop down to '64-bit'")
		self.wep_key_size.set(conf.wep_key_size_64)
		logger.debug("SecurityPage : Writing invalid alphabet in 'WEP KEY' text box")
		self.personal_wep_key.set(conf.wep_key_64_alpha_invalid)
		time.sleep(3)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.wep_key_64_len_error:
			raise AssertionError("invalid alphabet was accepted. i.e. Traceback: %s" %traceback.format_exc())
		
		logger.debug("SecurityPage : Writing valid alphabet in 'WEP KEY' text box")
		self.personal_wep_key.set(conf.wep_key_64_alpha)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if self.wep_key_64_len_error or self.wep_key_req_error:
			raise AssertionError("valid alphabet was not accepted. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing valid numbers in 'WEP KEY' text box")
		self.personal_wep_key.set(conf.wep_key_64_num_valid)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if self.wep_key_64_len_error or self.wep_key_req_error:
			raise AssertionError("valid number was not accepted. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing special characters in 'WEP KEY' text box")
		self.personal_wep_key.set(conf.wep_key_64_spcl_char)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.wep_key_64_len_error:
			raise AssertionError("special character was accepted. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing invalid passphrase in 'WEP KEY' text box")
		self.personal_wep_key.set(conf.reauth_intrvl_alpha)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.wep_key_64_len_error:
			raise AssertionError("'Must be 10 hexadecimal characters' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing invalid passphrase in 'WEP KEY' text box")
		self.personal_wep_key.set(conf.passphrase_hex_num_invalid)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.wep_key_64_len_error:
			raise AssertionError("'Must be 10 hexadecimal characters' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			
		logger.debug("SecurityPage : Writing null character in 'WEP KEY' text box")
		self.personal_wep_key.set('')
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.wep_key_req_error:
			raise AssertionError("null character was accepted. i.e. Traceback: %s" %traceback.format_exc())
			
	def enable_80211r_roaming(self):
		logger.debug("SecurityPage : Enable 802.11r ROAMING.")
		self.roaming_open.click()
		logger.debug("SecurityPage : Set passphrase.")
		self.passphrase.set(self.config.config_vars.Network_Passphrase)
		logger.debug("SecurityPage : Set retype passphrase .")
		self.retype_passphrase.set(self.config.config_vars.Network_Passphrase)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		return AccessPage(self.test, self.browser, self.config)
		
	def _select_new_authentication_server(self, number): 
		logger.debug("SecurityPage : Select new for authentucation server %s." %number)
		if number == '1':
			self.buy_time()
			self.buy_time()
			logger.debug('SecurityPage : Setting new external server to -- New --')
			self.authentication_server.set(self.config.config_vars.new_server)
			self.buy_time()
			logger.debug("SecurityPage : Clicking on save server")	
			self.save_server.click()
			self.buy_time()
			logger.debug("SecurityPage : Writing Server name")
			self.auth_server_name.set(self.config.config_vars.invalid_input)
			if not self.name_error:
				raise AssertionError("Server name error. i.e. Traceback: %s" %traceback.format_exc())
			self.buy_time()
			logger.debug("SecurityPage : Writing Server name")
			self.auth_server_name.set(self.config.config_vars.auth_server_name)
		elif number == '2':
			self.buy_time()
			self.buy_time()
			logger.debug('SecurityPage : Setting new external server to -- New --')
			self.authentication_server_2.set(self.config.config_vars.new_server)
			self.buy_time()
			logger.debug("SecurityPage : Clicking on save server")	
			self.save_server.click()
			self.buy_time()
			logger.debug("SecurityPage : Writing Server name")
			self.auth_server_name.set(self.config.config_vars.invalid_input)
			if not self.name_error:
				raise AssertionError("Server name error. i.e. Traceback: %s" %traceback.format_exc())
			self.buy_time()
			logger.debug("SecurityPage : Writing Server name")
			self.auth_server_name.set(self.config.config_vars.auth_server_name2)
		
	def create_external_radiuds_server(self, number):
		logger.debug("SecurityPage : Calling  _select_new_authentication_server method ")
		self._select_new_authentication_server(number)
		logger.debug("SecurityPage : Writing Server ip address")
		self.auth_ipaddr.set(self.config.config_vars.invalid_input)
		logger.debug("SecurityPage : Clicking on save server")
		self.save_server.click()
		self.page_up()
		if not self.ip_error:
			raise AssertionError("Invalid IP. i.e. Traceback: %s" %traceback.format_exc())
		self.buy_time()
		logger.debug("SecurityPage : Writing Server ip address")
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr)
		logger.debug("SecurityPage : Writing Shared key.")
		self.Auth_Sharedkey.set(self.config.config_vars.invalid_input)
		if not self.shared_key_error:
			raise AssertionError("Length error. i.e. Traceback: %s" %traceback.format_exc())
		self.buy_time()
		logger.debug("SecurityPage : Writing Shared key.")
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey)
		
		logger.debug("SecurityPage : re Writing retype - Shared key.")
		self.Retype_auth_shared_key.set(self.config.config_vars.pswdTxt)
		logger.debug("SecurityPage : Clicking on save server")
		self.save_server.click()
		if not self.retype_shared_key_error:
			raise AssertionError("Fields do not match error. i.e. Traceback: %s" %traceback.format_exc())
		self.buy_time()
		logger.debug("SecurityPage : re Writing retype - Shared key.")
		self.Retype_auth_shared_key.set(self.config.config_vars.Retype_auth_shared_key)
		if self.drpvlan_error:
			self.drpvlan.set(self.config.config_vars.reauth_2)
		self.buy_time()
		logger.debug("SecurityPage : Clicking on save server")
		self.save_server.click()
		self.buy_time()
		
	def set_both_wpa_2_wpa_64passphrase_format(self):
		logger.debug("SecurityPage : Set Key Management to Both(WPA-2 & WPA) .")
		self.security_key_management.set(self.config.config_vars.Authentication_Wpa2_WPA_Enterprise)
		logger.debug("SecurityPage : Enable mac authentication.")
		self.mac_authentication.set(self.config.config_vars.Security_Mac_Authentication_Enabled)
		logger.debug("SecurityPage : Setting  Passphrase.")
		self.passphrase.set(self.config.config_vars.hexadecimal_64_char)
		logger.debug("SecurityPage : Setting  Retype Passphrase.")
		self.retype_passphrase.set(self.config.config_vars.hexadecimal_64_char)
		logger.debug("SecurityPage : Set passphrase format to 64 hexadecimal chars.")
		self.wpa_passphrase_format.set(self.config.config_vars.passphrase_format_64)
		self.buy_time()
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()	
		return AccessPage(self.test, self.browser, self.config)
		
	def set_static_wep_Tx_key(self):
		logger.debug("SecurityPage : Set Key Management to Static WEP .")
		self.security_key_management.set(self.config.config_vars.personal_key_mgt_value)
		logger.debug("SecurityPage : Enable mac authentication.")
		self.mac_authentication.set(self.config.config_vars.Security_Mac_Authentication_Enabled)
		logger.debug("SecurityPage : Set value of Tx Key to 1.")
		self.wep_key_index.set(self.config.config_vars.wep_key_index)
		logger.debug("SecurityPage : Setting  WEP Key to 26 hexadecimal char.")
		self.personal_wep_key.set(self.config.config_vars.wep_key)
		logger.debug("SecurityPage : Setting  Retype WEP Key to 26 hexadecimal char.")
		self.personal_re_wep_key.set(self.config.config_vars.wep_key)
		logger.debug("SecurityPage : Set value of WEP Key Size to 128-bit.")
		self.wep_key_size.set(self.config.config_vars.wep_key_size)
		self.buy_time()
		# self.next.click()	
		# return AccessPage(self.test, self.browser, self.config)
			
	def set_wpa_blacklisting_enable(self):
		logger.debug("SecurityPage : Set Key Management to WPA Personal .")
		self.security_key_management.set(self.config.config_vars.wpa_personal)
		logger.debug("SecurityPage : Enable blacklisting.")
		self.blacklisting.set(self.config.config_vars.BlackListing_Guest)
		logger.debug("SecurityPage : Setting  max_auth_failure value to 10.")
		self.max_auth_failures.set(self.config.config_vars.max_auth_failure)
		logger.debug("SecurityPage : Set passphrase format to 8-63 chars.")
		self.wpa_passphrase_format.set(self.config.config_vars.passphrase_format_8)
		logger.debug("SecurityPage : Setting  Passphrase.")
		self.passphrase.set(self.config.config_vars.Network_Passphrase)
		logger.debug("SecurityPage : Setting  Retype Passphrase.")
		self.retype_passphrase.set(self.config.config_vars.Network_Passphrase)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		return AccessPage(self.test, self.browser, self.config)
		
	def set_both_wpa_2_wpa_passphrase_format_64_hexadecimal_chars(self):
		logger.debug("SecurityPage : Set Key Management to Both(WPA-2 & WPA) .")
		self.security_key_management.set(self.config.config_vars.Authentication_Wpa2_WPA_Enterprise)
		logger.debug("SecurityPage : Enable 802.11r ROAMING.")
		self.roaming_open.click()
		logger.debug("SecurityPage : Enable mac authentication.")
		self.mac_authentication.set(self.config.config_vars.Security_Mac_Authentication_Enabled)
		logger.debug("SecurityPage : Set passphrase format to 64 hexadecimal chars.")
		self.wpa_passphrase_format.set(self.config.config_vars.passphrase_format_64)
		logger.debug("SecurityPage : Setting  Passphrase.")
		self.passphrase.set(self.config.config_vars.security_passphrase)
		logger.debug("SecurityPage : Setting  Retype Passphrase.")
		self.retype_passphrase.set(self.config.config_vars.security_passphrase)
		self.buy_time()
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()	
		return AccessPage(self.test, self.browser, self.config)
		
	def configure_auth_server_settings(self,accounting_enable=False,acc_interval=False,balancing=False,auth_survivability=False,roaming=False,okc=False,blacklisting=False,mac_authentication=False,uppercase_support=False,termination=False):
		if accounting_enable:
			logger.debug("SecurityPage :Enable accounting")
			self.accounting.set(self.config.config_vars.enable_option)
			if acc_interval:
				logger.debug('EditNetworkPage :Set Accouting Interval.')
				self.accounting_interval.set(self.config.config_vars.accounting_interval_value)

		if balancing:
			logger.debug("SecurityPage :Enable load balancing.")
			self.load_balancing.set(self.config.config_vars.enable_option)
			
		if auth_survivability:
			logger.debug("SecurityPage :Enable auth survivability.")
			self.auth_survivability.set(self.config.config_vars.enable_option)
			
		if roaming:
			logger.debug("SecurityPage : Enable 802.11r ROAMING.")
			self.roaming_open.click()
			
		if okc:
			logger.debug("SecurityPage : Disable OKC .")
			if self.okc_checkbox.is_selected():
				self.okc_checkbox.click()
			
		if 	blacklisting:
			logger.debug("SecurityPage :Enable blacklisting.")
			self.blacklisting.set(self.config.config_vars.enable_option)
			
		if 	mac_authentication:
			logger.debug("SecurityPage :Enable mac authenttication.")
			self.mac_authentication.set(self.config.config_vars.enable_option)
			
		if uppercase_support:
			logger.debug("SecurityPage :Enable uppercase support.")
			self.personal_uppercase_support.set(self.config.config_vars.enable_option)
		
		if termination:
			logger.debug("SecurityPage :Enable Termination.")
			self.termination.set(self.config.config_vars.enable_option)

			
	def create_external_radius_server_in_auth_server_two(self):
		'''
		Create external radius in auth server two.
		'''
		logger.debug('EditNetworkPage : Setting new external server to Authentication Server 2')
		self.authentication_server_2.set(self.config.config_vars.new_external_server)
		time.sleep(3)
		logger.debug('EditNetworkPage : Entering details')
		self.auth_server_name.set(self.config.config_vars.auth_server_value_2)
		logger.debug("SecurityPage : Writing Server ip address")
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr_value)
		logger.debug('SecurityPage : Writing auth Sharedkey value')
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug("SecurityPage : Write retype - Shared key.")
		self.Retype_auth_shared_key.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug('EditNetworkPage : Saving external radius server')
		self.save_server.click()
		time.sleep(12)
		if self.drpvlan_error:
			self.drpvlan.set(self.config.config_vars.reauth_2)
			self.save_server.click()
		
	def set_delimiter(self):
		logger.debug("SecurityPage : Set delimiter to  :")
		self.personal_delimeter.set(self.config.config_vars.personal_delimeter)
		
	def set_security_enterprise_dropdown(self,wpa_wpa2=False,wpa=False,dynamic_wep=False):
		'''
		Setting key management drop down to wpa_wpa2 or wpa or dynamicWEP
		'''
		if wpa_wpa2:
			logger.debug("SecurityPage :Set key management to both wpa2 and wpa.")
			self.security_key_management.set(self.config.config_vars.Authentication_Wpa2_WPA_Enterprise)
		if wpa:
			logger.debug("SecurityPage :Set key management to wpa enterprise.")
			self.security_key_management.set(self.config.config_vars.Authentication_Wpa_Enterprise)
		if dynamic_wep:
			logger.debug("SecurityPage :Set key management to dynamic wep.")
			self.security_key_management.set(self.config.config_vars.enterprise_key_mgt_value)
			
	def set_default_settings(self):
		'''
			To set default settings. Key Management : WPA-2 Personal
		'''
		logger.debug('SecurityPage : Entering passphrase')
		self.passphrase.set(self.config.config_vars.Network_Passphrase)
		self.retype_passphrase.set(self.config.config_vars.Network_Passphrase)
		logger.debug('SecurityPage : Clicking on next')
		self.next.click()
		return AccessPage(self.test, self.browser, self.config)
	
	def set_key_management_wpa_personal(self):
		'''
			To set Key Management WPA Personal
		'''
		logger.debug('SecurityPage : Setting key management value to WPA Personal')
		self.security_key_management.set(self.config.config_vars.key_management)
		logger.debug('SecurityPage : Entering passphrase')
		self.passphrase.set(self.config.config_vars.Network_Passphrase)
		self.retype_passphrase.set(self.config.config_vars.Network_Passphrase)
		logger.debug('SecurityPage : Clicking on next')
		self.next.click()
		return AccessPage(self.test, self.browser, self.config)
	
	def set_key_management_auth_server_termination_accounting(self):
		'''
			Setting auth server 1, auth survivability, accounting dropdown, accounting interval
		'''
		logger.debug('SecurityPage : Clicking on Enterprise radio button')
		self.enterprise_radio_button.click()
		logger.debug('SecurityPage : Setting Key Management to Dynamic WEP')
		self.security_key_management.set(self.config.config_vars.keymanagement_value)
		logger.debug('SecurityPage : Setting new external server to Authentication Server 1')
		self.authentication_server.set(self.config.config_vars.new_external_server)
		time.sleep(3)
		logger.debug('SecurityPage : Entering details')
		self.auth_server_name.set(self.config.config_vars.auth_server_value)
		logger.debug("SecurityPage : Writing Server ip address")
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr_value)
		logger.debug('SecurityPage : Writing auth Sharedkey value')
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug("SecurityPage : Write retype - Shared key.")
		self.Retype_auth_shared_key.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug("SecuritPage: Write DRP vlan value")
		if not self.drpvlan_disabled:
			self.drpvlan.set(self.config.config_vars.reauth_value)
		logger.debug('SecurityPage : Saving external radius server')
		self.save_server.click()
		time.sleep(12)
		logger.debug('SecurityPage : Enabling authentication survivability')
		self.auth_survivability.set(self.config.config_vars.auth_survivability)
		logger.debug('SecurityPage : Disabling termination option')
		if self.termination.get_selected() == self.config.config_vars.enable_option:
			self.termination.set(self.config.config_vars.disable_option)
		logger.debug('SecurityPage : Editing Accounting dropdown')
		self.accounting.set(self.config.config_vars.accounting_enabled)
		logger.debug('SecurityPage : Entering invalid value in Accouting Interval')
		self.accounting_interval.set(self.config.config_vars.invalid_accounting)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.accounting_interval_error_msg:
			raise AssertionError("Invalid accounting message is not visible. i.e . Traceback: %s" % traceback.format_exc())	
		logger.debug('SecurityPage : Entering valid value in Accouting Interval')
		self.accounting_interval.set(self.config.config_vars.valid_accounting)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()	
		return AccessPage(self.test, self.browser, self.config)
	
	def set_key_management_reauth_interval_leap_use_session_key(self):
		'''
			Setting key management, reauth interval, use session key
		'''		
		logger.debug('SecurityPage : Clicking on Enterprise radio button')
		self.enterprise_radio_button.click()
		logger.debug('SecurityPage : Setting Key Management to Dynamic WEP')
		self.security_key_management.set(self.config.config_vars.keymanagement_value)
		time.sleep(3)
		logger.debug('SecurityPage : Setting reauth interval')
		self.reauth_interval.set(self.config.config_vars.reauth_value)
		logger.debug('SecurityPage : Clicking on Use session key for LEAP')
		self.leap_use_session_key.click()
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()	
		return AccessPage(self.test, self.browser, self.config)
	
	def set_key_management_dynamic_wep(self):
		'''
			Setting key management Dynamic WEP
		'''
		logger.debug('SecurityPage : Clicking on Enterprise radio button')
		self.enterprise_radio_button.click()
		logger.debug('SecurityPage : Setting Key Management to Dynamic WEP')
		self.security_key_management.set(self.config.config_vars.keymanagement_value)
		time.sleep(3)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()	
		return AccessPage(self.test, self.browser, self.config)
	
	def set_key_management_dynamic_wep_with_uppercase_support_enabled(self):
		'''
			Setting key management Dynamic WEP and uppercase support enabled
		'''	
		logger.debug('SecurityPage : Clicking on Enterprise radio button')
		self.enterprise_radio_button.click()
		logger.debug('SecurityPage : Setting Key Management to Dynamic WEP')
		self.security_key_management.set(self.config.config_vars.keymanagement_value)
		time.sleep(3)
		logger.debug('EditNetworkPage : Enabling mac authentication options')		
		self.mac_authentication_enterprise.click()
		logger.debug('SecurityPage : Enabling uppercase support')
		self.personal_uppercase_support.set(self.config.config_vars.Uppercase_Support_Enabled)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()	
		return AccessPage(self.test, self.browser, self.config)
	
	def click_on_enterprise_radio_button(self):
		'''
			Clicking on enterprise radio button 
		'''
		logger.debug('SecurityPage : Clicking on Enterprise radio button')
		self.enterprise_radio_button.click()
		time.sleep(5)
		
	def set_key_management_dynamic_wep_option(self):
		'''
			Setting key management Dynamic WEP
		'''
		logger.debug('SecurityPage : Setting Key Management to Dynamic WEP')
		self.security_key_management.set(self.config.config_vars.keymanagement_value)
		time.sleep(3)
		
	def set_key_management_wpa_2_enterprise_option(self):
		'''
			Setting key management wpa 2 enterprise
		'''
		logger.debug('SecurityPage : Setting Key Management to WPA 2 option')
		self.security_key_management.set(self.config.config_vars.Authentication_Wpa2_Enterprise)
		time.sleep(3)
		
	def set_key_management_both_wpa2_and_wpa_enterprise_option(self):
		'''
			Setting key management to Both WPA 2 and WPA Enterprise
		'''
		logger.debug('SecurityPage : Setting Key Management to Both WPA 2 and WPA Enterprise')
		self.security_key_management.set(self.config.config_vars.Authentication_Wpa2_WPA_Enterprise)
		time.sleep(3)
		
	def set_key_management_wpa_enterprise(self):
		'''
			Setting key management to Both WPA enterprise
		'''
		logger.debug('SecurityPage : Setting Key Management to WPA Enterprise')
		self.security_key_management.set(self.config.config_vars.Authentication_Wpa_Enterprise)
		time.sleep(3)		
		
	def set_mac_authentication_options(self):
		'''
			Enabling mac authentication options
		'''
		logger.debug('EditNetworkPage : Enabling mac authentication options')		
		self.mac_authentication_enterprise.click()
		self.auth_failthru_enterprise.click()
		time.sleep(3)
		
	def set_uppercase_support_dropdown(self):
		'''
		Enabling uppercase support dropdown
		'''
		logger.debug('SecurityPage : Enabling uppercase support')
		self.personal_uppercase_support.set(self.config.config_vars.Uppercase_Support_Enabled)
		time.sleep(3)

	def enable_blacklisting(self):
		'''
		Enabling blacklisting 
		'''
		logger.debug('SecurityPage : Setting blacklisting to enabled')
		self.blacklisting.set(self.config.config_vars.blacklisting_option)
		time.sleep(3)
		
	def edit_max_auth_failure(self,value):
		'''
		Editing max authentication failure
		'''
		logger.debug('SecurityPage : Editing max authentication failure')
		self.max_auth_failure_textbox.set(value)
		
	def set_reauth_interval(self):
		'''
		Setting reauth interval to 3 Hrs
		'''
		logger.debug('SecurityPage : Editing reauth interval')
		self.reauth_interval.set(self.config.config_vars.new_reauth_value)
		self.reauth_intrvl_unit.set('hrs.')

	def set_reauth_interval_options(self,value):
		'''
		Setting reauth interval to 3 Hrs
		'''
		logger.debug('SecurityPage : Editing reauth interval')
		self.reauth_interval.set(value)


	def set_external_radius_server_1(self):
		'''
		Setting external radius server
		'''
		logger.debug('SecurityPage : Setting new external server to Authentication Server 1')
		self.authentication_server.set(self.config.config_vars.new_external_server)
		time.sleep(3)
		logger.debug('SecurityPage : Entering details')
		self.auth_server_name.set(self.config.config_vars.auth_server_value)
		logger.debug("SecurityPage : Writing Server ip address")
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr_value)
		logger.debug('SecurityPage : Writing auth Sharedkey value')
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug("SecurityPage : Write retype - Shared key.")
		self.Retype_auth_shared_key.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug("SecuritPage: Write DRP vlan value")
		if not self.drpvlan_disabled:
			self.drpvlan.set(self.config.config_vars.reauth_value)
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
		logger.debug("SecurityPage : Writing Server ip address")
		self.auth_ipaddr.set(self.config.config_vars.auth_ipaddr_value)
		logger.debug('SecurityPage : Writing auth Sharedkey value')
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug("SecurityPage : Write retype - Shared key.")
		self.Retype_auth_shared_key.set(self.config.config_vars.Auth_Sharedkey_value)
		logger.debug("SecuritPage: Write DRP vlan value")
		if not self.drpvlan_disabled:
			self.drpvlan.set(self.config.config_vars.reauth_value)
		logger.debug('SecurityPage : Saving external radius server')
		self.save_server.click()
		time.sleep(12)
		
	def setting_termination_option(self,flag):
		'''
		setting terminal option
		'''
		if flag:
			logger.debug('SecurityPage : Enabling terminal option')
			self.termination.set(self.config.config_vars.enable_option)
		else:
			logger.debug('SecurityPage : Disabling terminal option')
			self.termination.set(self.config.config_vars.disable_option)
			
	def assert_auth_server_internal_server_option(self):
		'''
		Asserting authentication server to InternalServer
		'''
		time.sleep(5)
		if not self.authentication_server.get_selected() == self.config.config_vars.InternalServer:
			raise AssertionError("Authentication server 1 is not set to InternalServer. i.e . Traceback: %s" % traceback.format_exc())	
		
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
		
	def set_roaming_option(self,value):
		'''
			Setting roaming option
		'''
		if value == 'Enabled':
			logger.debug('SecurityPage : Enabling roaming option')
			self.roaming_enterprise.set(self.config.config_vars.enable_option)
		else:
			logger.debug('SecurityPage : Disabling roaming option')
			self.roaming_enterprise.set(self.config.config_vars.disable_option)
			
			
	def select_auth_server_internalserver(self,value):
		'''
			Setting internal server
		'''		
		if value == '1':
			logger.debug("EditNetworkPage : Selecting  InternalServer for Authentication Server feild ")
			self.authentication_server.set(self.config.config_vars.InternalServer)
			self.buy_time()
		if value == '2':
			logger.debug("EditNetworkPage : Selecting  InternalServer for Authentication Server feild ")
			self.authentication_server_2.set(self.config.config_vars.InternalServer)
			self.buy_time()
			
			
	def enable_accounting_interval(self,value):
		'''
			Setting Accounting dropdown and interval
		'''
		logger.debug('SecurityPage : Editing Accounting dropdown')
		self.accounting.set(self.config.config_vars.accounting_enabled)
		time.sleep(4)
		logger.debug('SecurityPage : Entering valid value in Accouting Interval')
		self.accounting_interval.set(value)
		time.sleep(3)
		
		
	def enable_authentication_survivability(self):
		'''
			Enabling authentication survivability
		'''
		logger.debug('SecurityPage : Enabling authentication survivability')
		self.auth_survivability.set(self.config.config_vars.auth_survivability)
		time.sleep(3)
		
		
	def move_to_next_page(self):
		'''
			Moving to next page
		'''
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()	
		return AccessPage(self.test, self.browser, self.config)
		
	def set_authentication_server_to_internalserver(self):				
		logger.debug('SecurityPage : Changing Authentication Server  to InternalServer')
		self.authentication_server.set(self.config.config_vars.InternalServer)
		
	def enable_mac_authentication_enterprise(self):
		logger.debug('SecurityPage : Clicking Perform MAC authentication before 802.1X.')
		self.mac_authentication_enterprise.click()

	def configure_security_radio_fields(self,okc=False,mac_authentication=False,mac_authentication_fail_thru=False):
		'''
		Configure radio button fields on security page , eg: Okc , Perform mac authentication , mac authentication fail thru.
		'''
		if okc:
			logger.debug("SecurityPage : Disable OKC .")
			self.okc_checkbox.click()

		if mac_authentication:
			logger.debug("SecurityPage : Enable mac_authentication .")
			self.mac_authentication_enterprise.click()

		if mac_authentication_fail_thru:
			logger.debug("SecurityPage : Enable mac_authentication_fail_thru .")
			self.auth_failthru_enterprise.click()
			
	def validate_authentication_server_feilds(self):
		logger.debug("SecurityPage : Select new for authentucation server" )
		self.buy_time()
		logger.debug('SecurityPage : Changing Authentication Server  to InternalServer')
		self.authentication_server.set(self.config.config_vars.new_server)
		self.buy_time()
		logger.debug("SecurityPage : Write Server name")
		self.auth_server_name.set(self.config.config_vars.invalid_input)
		logger.debug("SecurityPage : Write Server IP address")
		self.auth_ipaddr.set(self.config.config_vars.invalid_input)
		logger.debug("SecurityPage : Write Shared key.")
		self.Auth_Sharedkey.set(self.config.config_vars.invalid_input)
		logger.debug("SecurityPage : Write retype - Shared key.")
		self.Retype_auth_shared_key.set(self.config.config_vars.invalid_zero_input)
		logger.debug("SecurityPage : Write  Accounting Port value.")
		self.Auth_Account_Port.set(self.config.config_vars.invalid_zero_input)
		logger.debug("SecurityPage : Write Dead Time.")
		self.deadtime.set(self.config.config_vars.invalid_zero_input)
		logger.debug("SecurityPage : Write Time Out value.")
		self.auth_timeout.set(self.config.config_vars.invalid_zero_input)
		logger.debug("SecurityPage : Write Retry Count value.")
		self.retry_count.set(self.config.config_vars.invalid_zero_input)
		logger.debug("SecurityPage : Write Auth Port value.")
		self.AuthPort.set(self.config.config_vars.invalid_zero_input)
		logger.debug("SecuritPage: Write DRP vlan value")
		if not self.drpvlan_disabled:
			self.drpvlan.set(self.config.config_vars.reauth_value)
		self.buy_time()
		logger.debug('SecurityPage : Saving external radius server')
		self.save_server.click()
		self.buy_time()

		if not self.name_error:
			raise AssertionError("Server name error. i.e. Traceback: %s" %traceback.format_exc())

		if not self.ip_error:
			raise AssertionError("Invalid IP. i.e. Traceback: %s" %traceback.format_exc())

		if not self.shared_key_error:
			raise AssertionError("Length error. i.e. Traceback: %s" %traceback.format_exc())

		if not self.retype_shared_key_error:
			raise AssertionError("Fields do not match error. i.e. Traceback: %s" %traceback.format_exc())

		if not self.Auth_Account_Port_error:
			raise AssertionError("Server name error. i.e. Traceback: %s" %traceback.format_exc())

		if not self.deadtime_error:
			raise AssertionError("'Must be a number in range 1-1440' error msg not present. i.e. Traceback: %s" %traceback.format_exc())

		if not self.auth_timeout_error:
			raise AssertionError("'Must be a number in range 1-30' error msg not present. i.e. Traceback: %s" %traceback.format_exc())

		if not self.Auth_Retry_Count_error:
			raise AssertionError("'Must be a number in range 1-5' error msg not present. i.e. Traceback: %s" %traceback.format_exc())

		if not self.AuthPort_error:
			raise AssertionError("'Must be a number in range 1-65534' error msg not present. i.e. Traceback: %s" %traceback.format_exc())

		self.confirm_save_close_server.click()
		
	def validate_authentication_server_required_feilds(self):
		logger.debug("SecurityPage : Select new for authentucation server" )
		self.buy_time()
		logger.debug("SecurityPage: selecting -- New --  from dropdown")
		self.authentication_server.set(self.config.config_vars.new_server)
		self.buy_time()
		logger.debug('SecurityPage : Saving external radius server')
		self.save_server.click()
		self.buy_time()
		if not self.name_error:
			raise AssertionError("Server name error. i.e. Traceback: %s" %traceback.format_exc())
		if not self.shared_key_error:
			raise AssertionError("Length error. i.e. Traceback: %s" %traceback.format_exc())
		logger.debug("SecurityPage : Write Server name")
		self.auth_server_name.set(self.config.config_vars.auth_server_name)
		logger.debug("SecurityPage : Write Shared key.")
		self.Auth_Sharedkey.set(self.config.config_vars.Auth_Sharedkey)
		logger.debug('SecurityPage : Saving external radius server')
		self.save_server.click()
		self.buy_time()
		if not self.retype_shared_key_error:
			raise AssertionError("Fields do not match error. i.e. Traceback: %s" %traceback.format_exc())
		
		logger.debug('SecurityPage : clicking on  confirm save close server button')
		self.confirm_save_close_server.click()
		
		
	def authentication_feild_with_select(self):
		logger.debug("SecurityPage : Select new for authentucation server" )
		self.buy_time()
		logger.debug("SecurityPage: selecting -- New --  from dropdown")
		self.authentication_server.set(self.config.config_vars.new_server)
		self.buy_time()
		logger.debug('SecurityPage : clicking on  confirm save close server button')
		self.confirm_save_close_server.click()
		if not self.authentication_server.get_selected() == self.config.config_vars.select:
			raise AssertionError("Authentication server 1 is not set to --Select--. i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		self.buy_time()
		if not self.auth_server1_error_required:
			raise AssertionError("'* This field is mandatory' error not found. i.e. Traceback: %s" %traceback.format_exc())
			
			
	def checking_for_authentication_servers_visibility(self):
		logger.debug("EditNetworkPage : Checking whether authentication_server1 feild is visible")
		if not self.authentication_server:
			raise AssertionError("authentication_server1 feild is not visible .Traceback: %s " %traceback.format_exc())
		
		logger.debug("EditNetworkPage : Checking whether authentication_server2 feild is visible")
		if self.authentication_server_2:
			raise AssertionError("authentication_server2 feild is visible .Traceback: %s " %traceback.format_exc())
		
	def checking_for_authentication_server2_visibility(self):
		logger.debug("EditNetworkPage : Checking whether authentication_server2 feild is visible")
		if not self.authentication_server_2:
			raise AssertionError("authentication_server2 feild is not visible .Traceback: %s " %traceback.format_exc())
			
	def assert_invalid_passphrase(self):
		logger.debug('SecurityPage : writing valid passphrase')
		self.passphrase.set(self.config.config_vars.passphrase_invalid_hex_value)
		time.sleep(10)
		logger.debug("SecurityPage :Check Pass phrase Format 64 hexadecimal chars.")
		self.wpa_passphrase_format.set(self.config.config_vars.passphrase_format_64)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		if not self.passphrase_hex_length_err:
			raise AssertionError("Invalid input warning is not shown.Traceback: %s " %traceback.format_exc())
			
	def set_authentication_server_next(self):
		self.enterprise_radio_button.click()
		logger.debug("SecurityPage: selecting -- Select -- from dropdown")
		self.authentication_server.set(self.config.config_vars.select)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()
		
	def assert_exist_name_error(self):
		self.enterprise_radio_button.click()
		logger.debug("SecurityPage: Clicking on internal server user link ")
		self.show_users_link.click()
		time.sleep(7)
		if self.select_user_name:
			logger.debug("SecurityPage : Clicking on Select user name ")	
			self.select_user_name.click()
			logger.debug("SecurityPage : Clicking on Delete button")	
			self.delete_button.click()
			self.browser.accept_alert()
		logger.debug('SecurityPage : writing userTxt  value')
		self.userTxt.set(self.config.config_vars.rule_calea_type)
		logger.debug('SecurityPage : writing pswdTxt  value')
		self.pswdTxt.set(self.config.config_vars.rule_calea_type)
		logger.debug('SecurityPage : writing pswdTxt2  value')
		self.pswdTxt2.set(self.config.config_vars.rule_calea_type)
		logger.debug('SecurityPage : writing typeTxt  value')
		self.typeTxt.set(self.config.config_vars.user_type_value)
		logger.debug('SecurityPage : Clicking add button')
		self.updateButton.click()
		time.sleep(7)
		logger.debug('SecurityPage : writing userTxt  value')
		self.userTxt.set(self.config.config_vars.rule_calea_type)
		logger.debug('SecurityPage : writing pswdTxt  value')
		self.pswdTxt.set(self.config.config_vars.rule_calea_type)
		logger.debug('SecurityPage : writing pswdTxt2  value')
		self.pswdTxt2.set(self.config.config_vars.rule_calea_type)
		logger.debug('SecurityPage : writing typeTxt  value')
		self.typeTxt.set(self.config.config_vars.user_type_value)
		logger.debug('SecurityPage : Clicking add button')
		self.updateButton.click()
		if not self.duplicate_user_exist_error:
			raise AssertionError("Error message is not shown.Traceback: %s " %traceback.format_exc())
			
	def validate_splash_page(self):
		'''
			Validate the port value in External Captive portal
		'''
		logger.debug("Entering the splash page type value. ")
		self.set_splash_page_type_value("External")
		logger.debug("Entering the captive portal value. ")
		self.set_wired_captive_portal_value("-- New --")
		logger.debug("Setting the invalid port value. ")
		self.set_captive_port_value(self.config.config_vars.captive_port_invalid)
		logger.debug("Setting the legal value in port. ")
		self.set_captive_port_value()
		logger.debug('SecurityPage :  Clicking on Save button')
		self.save.click()
		logger.debug('SecurityPage :  Clicking on Cancel button')
		self.cap_cancel.click()
		logger.debug('SecurityPage :  Clicking on Cancel button of network creation')
		self.network_create_cancel.click()
		
	
	def set_captive_port_value(self,value=None):
		if value >=1 and value <= 65535:
			logger.debug("Entering the valid value in captive port")
			self.captive_port.set(value)
		elif value:
			logger.debug("Entering the valid value in captive port")
			self.captive_port.set(value)
			logger.debug('SecurityPage :  Clicking on Save button')
			self.save.click()
			if self.port_validate_error:
				raise AssertionError(" Must be a number in range 1-65535. i.e . Traceback: %s" % traceback.format_exc())
		else:
			logger.debug("Entering the valid value in captive port")
			self.captive_port.set(self.config.config_vars.captive_port_default)
		
		
		
	def set_splash_page_type_value(self,value=None):
		'''
		selecting value from splash page type Drop down
		'''
		if value == "None":
			logger.debug("SecurityPage : Selecting None .")
			self.splash_page_type.set(self.config.config_vars.Splash_page_none)
		elif value == "Internal - Acknowledged":
			logger.debug("SecurityPage : Selecting internal authenticated  .")
			self.splash_page_type.set(self.config.config_vars.Splash_page_Acknowledged)
		elif value =="External":
			logger.debug("SecurityPage : Selecting External  .")
			self.splash_page_type.set(self.config.config_vars.Splash_page_external)
		else:
			logger.debug("SecurityPage : Selecting internal authenticated  .")
			self.splash_page_type.set(self.config.config_vars.Splash_page_Authenticated)
	
	
	def set_wired_captive_portal_value(self,value=None):
		'''
		selecting value from wired captive portal Drop down
		'''
		if value == "-- New --":
			logger.debug("SecurityPage : Selecting wired captive portal as -- New -- .")
			self.wired_captive_portal.set(self.config.config_vars.Wired_Captive_Profile_New)
		else: 
			logger.debug("SecurityPage : Selecting wired captive portal as default.")
			self.wired_captive_portal.set(self.config.config_vars.Wired_Captive_Profile_Default)
	
	def validate_backlist_field(self):
		'''
		Validate the Blacklist field in security section
		'''
		logger.debug("SecurityPage : Entering the splash page type value. ")
		self.set_splash_page_type_value("External")
		logger.debug("SecurityPage : Selecting the Blacklist field. ")
		self.blacklist_whitelist.click()
		logger.debug("SecurityPage : clicking on new button to create a new blacklist. ")
		self.blacklist_new.click()
		logger.debug("SecurityPage : Entering the invalid value in the text field.")
		self.new_regex.set(self.config.config_vars.new_regex_error)
		logger.debug("SecurityPage : Clicking on the save button. ")
		self._walled_new_save_button()
		if not self.black_list_error:
			raise AssertionError("Maximum 64 charactersa are allowed. i.e . Traceback: %s" % traceback.format_exc())
		
		logger.debug("SecurityPage : Entering the Valid value in the text field.")
		self.new_regex.set(self.config.config_vars.new_regex_valid)
		logger.debug("SecurityPage : Clicking on the save button. ")
		self._walled_new_save_button()
		logger.debug("SecurityPage : Selecting the existing blacklist.")
		self.buy_time()
		self.select_blacklist.click()
		logger.debug("SecurityPage : Clicking on the edit button. ")
		self.blacklist_edit.click()
		logger.debug("SecurityPage : Entering the invalid value in the text field. ")		
		self.new_regex.set(self.config.config_vars.new_regex_error)
		logger.debug("SecurityPage : Clicking on the save button .")
		self._walled_new_save_button()
		if not self.black_list_error:
			raise AssertionError("Maximum 64 charactersa are allowed. i.e . Traceback: %s" % traceback.format_exc())
		logger.debug("SecurityPage : Entering the valid value in the text field. ")
		self.new_regex.set(self.config.config_vars.new_regex_valid)
		logger.debug("SecurityPage : Clicking on the save button .")
		self._walled_new_save_button()
		logger.debug("SecurityPage : Selecting the existing blacklist.")
		self.select_blacklist.click()
		logger.debug("Deleting the exixting blacklist to make it default. ")
		self.blacklist_delete.click()
		
		logger.debug("SecurityPage : Clicking on the Cancel button .")
		self.walled_cancel.click()
		logger.debug('SecurityPage :  Clicking on Cancel button of network creation')
		self.network_create_cancel.click()
		
		
		
	def validate_whitelist_field(self):
		'''
		Validate the WhiteList field in security section
		'''
		logger.debug("SecurityPage : Entering the splash page type value. ")
		self.set_splash_page_type_value("External")
		logger.debug("SecurityPage : Selecting the Whitelist field. ")
		self.blacklist_whitelist.click()
		logger.debug("SecurityPage : clicking on new button to create a new whitelist. ")
		self.whitelist_new.click()
		logger.debug("SecurityPage : Entering the exceeded value in the text field.")
		self.new_regex.set(self.config.config_vars.new_regex_error)
		logger.debug("SecurityPage : Clicking on the save button. ")
		self._walled_new_save_button()
		if not self.black_list_error:
			raise AssertionError("Maximum 64 charactersa are allowed. i.e . Traceback: %s" % traceback.format_exc())
		
		logger.debug("SecurityPage : Entering the correct value in the text field.")
		self.new_regex.set(self.config.config_vars.new_regex_valid)
		self._walled_new_save_button()
		logger.debug("SecurityPage : Selecting the existing whitelist.")
		self.buy_time()
		if self.walled_new_save:
			logger.debug("SecurityPage : Clicking on the save button. ")
			self._walled_new_save_button()
		logger.debug("SecurityPage : Selecting the existing blacklist.")
		self.select_blacklist.click()
		logger.debug("SecurityPage : Clicking on the edit button. ")
		self.blacklist_edit.click()
		logger.debug("SecurityPage : Entering the invalid value in the text field.")
		self.new_regex.set(self.config.config_vars.new_regex_error)
		logger.debug("SecurityPage : Clicking on the save button. ")
		self._walled_new_save_button()
		if not self.black_list_error:
			raise AssertionError("Maximum 64 charactersa are allowed. i.e . Traceback: %s" % traceback.format_exc())
		
		logger.debug("SecurityPage : Entering the valid value in the text field.")
		self.new_regex.set(self.config.config_vars.new_regex_valid)
		logger.debug("SecurityPage : Clicking on the save button. ")
		self._walled_new_save_button()
		if self.walled_new_save:
			logger.debug("SecurityPage : Clicking on the save button. ")
			self._walled_new_save_button()
		logger.debug("SecurityPage : Selecting the existing blacklist.")
		self.select_blacklist.click()
		logger.debug("SecurityPage : Deleting the exixting whitelist to make it default. ")
		self.blacklist_delete.click()
		
		logger.debug("SecurityPage : Clicking on the Cancel button .")
		self.walled_cancel.click()
		logger.debug('SecurityPage :  Clicking on Cancel button of network creation')
		self.network_create_cancel.click()
		
	
	def _walled_new_save_button(self):
		'''
		Clicking on Walled new save button
		'''
		time.sleep(3)
		logger.debug("SecurityPage : Clicking on the walled new save button. ")
		self.walled_new_save.click()

	def validate_security_section_field(self):
		'''
		Validating Security Section Field
		'''
		logger.debug("SecurityPage : Entering the splash page type value. ")
		self.set_splash_page_type_value("External")
		logger.debug("SecurityPage : Entering the captive portal value. ")
		self.set_wired_captive_portal_value("New")
		logger.debug("SecurityPage : calling set_wispr_value method. ")
		self.set_wispr_value()
		logger.debug("SecurityPage : SecurityPage : Enable Wireless Encryption.")
		self.wireless_encryption.set(self.config.config_vars.wireless_encryption)
		logger.debug("SecurityPage : SecurityPage : Clicking on next")	
		self.next.click()
		
		if not self.passphrase_error_required:
			raise AssertionError("PassPhrase field id required can't lest blank. ")
		self.create_external_radius_server_in_auth_server_one()

	def assert_radius_radio_button(self):
		if not self.radius.is_selected():
			raise AssertionError("radius radio button is not selected. i.e. Traceback: %s" %traceback.format_exc())
			
			
	def set_authentication_server1(self, value):
		'''
		select new or internalserver from dropdown
		'''
		if value == 'New':
			logger.debug("SecurityPage: selecting new from dropdown")
			self.authentication_server.set(self.config.config_vars.new_server)
		elif value == 'InternalServer':
			logger.debug("SecurityPage: selecting new from dropdown")
			self.authentication_server.set(self.config.config_vars.InternalServer)
		
		
	def assert_auth_port(self):
		if not self.AuthPort.get() == self.config.config_vars.default_AuthPort:
			raise AssertionError("the default value of auth port is not set to 1812 . i.e. Traceback: %s" %traceback.format_exc())
			
	def assert_auth_account_port(self):
		if not self.Auth_Account_Port.get() == self.config.config_vars.default_Auth_Account_Port:
			raise AssertionError("the default value of auth account port is not set to 1813 . i.e. Traceback: %s" %traceback.format_exc())
		
	
	def assert_dead_time(self):
		if not self.deadtime.get() == self.config.config_vars.default_dead_time:
			raise AssertionError("the default value of dead time is not set to 5 . i.e. Traceback: %s" %traceback.format_exc())
			
	def set_ldap_radio_button(self):
		'''
			Click on new server ldap radio button 
		'''
		logger.debug('SecurityPage : Clicking on new server ldap radio button')
		self.ldap.click()
		time.sleep(5)
	
	def assert_ldap_auth_port(self):
		if not self.ldap_auth_port.get() == self.config.config_vars.default_ldap_auth_port:
			raise AssertionError("the default value of ldap auth port is not set to 5 . i.e. Traceback: %s" %traceback.format_exc())
		
	def set_new_server_radius_radio_button(self):
		'''
		click on new server radius button
		'''
		logger.debug('SecurityPage : Clicking on new server radius radio button')
		self.radius.click()
		self.buy_time()
	
	
	def set_new_server_coa_only_check_box(self):
		'''
		click on new server 'Coa Only' chekbox
		'''
		logger.debug('SecurityPage : Clicking on Coa Only chekbox')
		self.auth_coa_only_check_box.click()
		self.buy_time()
	
	def assert_air_group_coa_port(self):
		if not self.air_group_coa_port.get() == self.config.config_vars.default_air_group_coa_port_value:
			raise AssertionError("the default value of air group coa port is not set to its default value 5999 . i.e. Traceback: %s" %traceback.format_exc())
			
	def set_valid_paasphrase_retype(self):
		'''
		write valid passphrase and
		retype it to match
		'''
		logger.debug('SecurityPage : writing valid passphrase')
		self.passphrase.set(self.config.config_vars.wep_key_alpha_valid)
		logger.debug('SecurityPage : re writing valid passphrase in retype textbox')
		self.retype_passphrase.set(self.config.config_vars.wep_key_alpha_valid)
		self.buy_time()
		
		
	def set_wireless_security_defaults(self):
		logger.debug("SecurityPage : Calling _set_security_level method  .")
		self._set_security_level('personal')
		logger.debug('SecurityPage : write valid passphrase and retype it to match')
		self.set_valid_paasphrase_retype()
		logger.debug('SecurityPage : clicking on next')
		self.click_on_next()
		self.buy_time()
		return AccessPage(self.test, self.browser, self.config)
		
	def assert_security_level_default(self):
		'''
		Checking for default value of SECURITY LEVEL...
		'''
		logger.debug("SecurityPage : Checking security level default .")
		if not self.personal.is_selected(): 
			raise AssertionError("'Personal' radio button is not selected by default. i.e . Traceback: %s" % traceback.format_exc())
	
	def assert_personal_key_management_default_value(self):
		'''
		Checking for default value of KEY MANAGEMENT in Personal...
		'''	
		logger.debug("SecurityPage : Checking Personal-key management default")
		if not self.security_key_management.get_selected() == self.config.config_vars.Authentication_wpa2: 
			raise AssertionError("'KEY MANAGEMENT' dropdown is not set to default. i.e . Traceback: %s" % traceback.format_exc())
	
	def assert_personal_security_dot11r_roaming_default(self):
		'''
		Checking for default value of 802.11r ROAMING in Personal...
		'''	
		logger.debug("SecurityPage : Checking Personal-security_dot11r default")
		if  self.roaming_open.is_selected(): 
			raise AssertionError("'802.11r ROAMING' checkbox is enabled by default. i.e . Traceback: %s" % traceback.format_exc())
		
	def assert_personal_passphrase_format_default(self):
		'''
		Checking for default value of PASSPHRASE in Personal...
		'''
		logger.debug("SecurityPage : Checking Personal-passphrase_format default")
		if not self.wpa_passphrase_format.get_selected() == self.config.config_vars.pass_phrase_format_8_63_chars: 
			raise AssertionError("'PASSPHRASE FORMAT' dropdown is not set to default. i.e . Traceback: %s" % traceback.format_exc())
			
	def assert_personal_mac_authentication_default(self):
		'''
		Checking for default value of MAC AUTHENTICATION in Personal...
		'''	
		logger.debug("SecurityPage : Checking Personal-mac_authentication default")
		if not self.mac_authentication.get_selected() == self.config.config_vars.disable_option: 
			raise AssertionError("'MAC AUTHENTICATION' dropdown is not set to default. i.e . Traceback: %s" % traceback.format_exc())
	
	def assert_personal_blacklisting_default(self):
		'''
		Checking for default value of MAC AUTHENTICATION in Personal...
		'''
		logger.debug("SecurityPage : Checking Personal-blacklisting default")
		if not self.blacklisting.get_selected() == self.config.config_vars.disable_option: 
			raise AssertionError("'BLACKLISTING' dropdown is not set to default. i.e . Traceback: %s" % traceback.format_exc())
	
	def assert_enterprise_termination_default(self):
		'''
		Checking for default value of TERMINATION in Enterprise...
		'''
		self.security_level_enterprise()
		logger.debug("SecurityPage : Checking enterprise_termination default")
		if not self.termination.get_selected() == self.config.config_vars.disable_option: 
			raise AssertionError("'TERMINATION' dropdown is not set to default. i.e . Traceback: %s" % traceback.format_exc())
		
	def assert_enterprise_authentication_server1_default(self):
		'''
		Checking for default value of AUTHENTICATION SERVER 1 in Enterprise...
		'''	
		self.security_level_enterprise()
		logger.debug("SecurityPage : Checking enterprise_authentication_server1 default")
		if not self.authentication_server.get_selected() == self.config.config_vars.InternalServer: 
			raise AssertionError("'AUTHENTICATION SERVER 1' dropdown is not set to default. i.e . Traceback: %s" % traceback.format_exc())
	
	def assert_enterprise_perform_mac_authentication_uppercase(self):
		'''
		Checking for default value of UPPERCASE SUPPORT of perform_mac_authentication 802.1x 
		in MAC AUTHENTICATION in Enterprise...
		'''
		self.security_level_enterprise()
		logger.debug("SecurityPage : selecting perform_mac_authentication 802.1x")
		self.mac_authentication_enterprise.click()
		if not self.personal_uppercase_support.get_selected() == self.config.config_vars.disable_option: 
			raise AssertionError("'UPPERCASE SUPPORT' dropdown is not set to default. i.e . Traceback: %s" % traceback.format_exc())
			
	def set_authentication_server(self, value):
		'''
			selects new or InternalServer option from drop-down
		'''
		if value == 'new':
			logger.debug('SecurityPage : selecting new..')
			self.authentication_server.set(self.config.config_vars.new_server)
		elif value == 'InternalServer':
			logger.debug('SecurityPage: selecting InternalServer')
			self.authentication_server.set(self.config.config_vars.internal_server)
		

	def assert_timeout(self):
		if not self.auth_timeout.get() == self.config.config_vars.default_time_out:
			raise AssertionError("time out value is not set to 5.i.e . Traceback: %s" % traceback.format_exc())
	
	def assert_splash_page_required_fields(self):
		'''
			set Splash page type to External
			selects new captive portal
			asserts required fields
		'''
		logger.debug("SecurityPage : Selecting External .")
		self.set_splash_page_type(self.config.config_vars.Splash_page_external)
		logger.debug("SecurityPage : setting  captive portal profile -- New -- .")
		self.set_captive_portal_profile(self.config.config_vars.Wired_Captive_Profile_New)
		logger.debug("SecurityPage : setting  captive portal Auth text Authentication text .")
		self.set_captive_type(self.config.config_vars.captive_portal_auth_text)
		logger.debug("SecurityPage : clicking onj save button")
		self.save.click()
		if not self.captive_name_required_error:
			raise AssertionError("Field is Required.i.e . Traceback: %s" % traceback.format_exc())
		if not self.captive_ip_req_error:
			raise AssertionError("Field is Required.i.e . Traceback: %s" % traceback.format_exc())
		if not self.captive_url_req_error:
			raise AssertionError("Field is Required.i.e . Traceback: %s" % traceback.format_exc())
		if not self.captive_port_error:
			raise AssertionError("Must be a number range in range1-65534.i.e . Traceback: %s" % traceback.format_exc())
		if not self.captive_authtext_req_error:
			raise AssertionError("Field is Required.i.e . Traceback: %s" % traceback.format_exc())

	def assert_splash_page_visuals(self):
		'''
		validates redirect url field on security page
		'''
		logger.debug("SecurityPage : Selecting internal authenticated  .")
		self.set_splash_page_type(self.config.config_vars.Splash_page_Authenticated)
		logger.debug("SecurityPage : Setting invalid redirect url...")
		self.redirect_url.set(self.config.config_vars.invalid_redirect_url)
		logger.debug('SecurityPage : Clicking save button..')
		self._save_settings()
		if not self.redirect_url_error_message:
			raise AssertionError("SecurityPage : Required error message is not displayed .Traceback: %s " %traceback.format_exc())
		logger.debug('SecurityPage : Setting valid redirect url...')
		self.redirect_url.set(self.config.config_vars.valid_redirect_url)
		logger.debug('SecurityPage : Clicking save button..')
		self._save_settings()
		if not self.changes_saved:
			raise AssertionError("SecurityPage :  Valid URL not accepted .Traceback: %s " %traceback.format_exc())
	
	def set_splash_page_type(self, value = None):
		'''
			selects internal-authenticated or external-radius authenticated or 
			external- authentication text or external or internal-acknwledged 
		'''
		if value == 'Internal - Authenticated':
			logger.debug("SecurityPage : Selecting internal Authenticated  .")
			self.splash_page_type.set(self.config.config_vars.Splash_page_Authenticated)
		elif value == 'External - RADIUS Authentication':
			logger.debug("SecurityPage : Selecting external -radius authentication.")
			self.splash_page_type.set(self.config.config_vars.splash_page_external_radius_auth)
		elif value == 'External - Authentication Text':
			logger.debug("SecurityPage : Selecting external -authentication text.")
			self.splash_page_type.set(self.config.config_vars.splash_page_external_auth_text)
		elif value == 'External':
			logger.debug("SecurityPage : Selecting external.")
			self.splash_page_type.set(self.config.config_vars.Splash_page_external)
		else :
			logger.debug("SecurityPage : Selecting internal-authentication.")
			self.splash_page_type.set(self.config.config_vars.Splash_page_Acknowledged)
			
	def _save_settings(self):
		'''
			clicks on save button
		'''
		logger.debug('SecurityPage : Clicking save button..')
		self.save_button.click()
	
	def set_captive_portal_profile(self, value):
		'''
			selects new or default
		'''
		if value == '-- New --' :
			logger.debug("SecurityPage : Setting  captive portal value as -- New --. ")
			self.wired_captive_portal.set(self.config.config_vars.Wired_Captive_Profile_New)
		elif value == 'default' :
			logger.debug("SecurityPage :Setting captive portal value as default. ")
			self.wired_captive_portal.set(self.config.config_vars.Wired_Captive_Profile_Default)
			
			
	def set_captive_type(self, value = None):
		'''
			selects authentication text or radius authentication
		'''
		if value == 'Authentication text':
			logger.debug("SecurityPage :Setting captive Type Authentication text. ")
			self.captive_type.set(self.config.config_vars.captive_portal_auth_text)
		else :
			logger.debug("SecurityPage :Setting captive Type value. ")
			self.captive_type.set(self.config.config_vars.Captive_Role_Radius_Authentication)			
			
	def set_key_management_reauth_interval_use_session_key(self):
		'''
			Setting key management, reauth interval, use session key
		'''		
		logger.debug('SecurityPage : Clicking on Enterprise radio button')
		self.enterprise_radio_button.click()
		logger.debug('SecurityPage : Setting Key Management to Dynamic WEP')
		self.security_key_management.set(self.config.config_vars.keymanagement_value)
		time.sleep(3)
		logger.debug('SecurityPage : Setting reauth interval')
		self.reauth_interval.set(self.config.config_vars.reauth_value)
		logger.debug('SecurityPage : Clicking on Use session key for LEAP')
		self.leap_use_session_key.click()
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()	
		return AccessPage(self.test, self.browser, self.config)

	def set_splash_page_visuals_field_values(self):
		conf = self.config.config_vars
		logger.debug('SecurityPage : setting "BATTLE TITLE" fiend.')
		self.banner_title.set(conf.banner_title_new_value)
# 		logger.debug('SecurityPage : setting "HEADER COLOR" fiend.')
# 		self.header_color.set(conf.header_color_default)
		logger.debug('SecurityPage : setting "WELCOME TEXT" fiend.')
		self.welcome_text.set(conf.welcome_text_new_value)
		logger.debug('SecurityPage : setting "POLICY TEXT" fiend.')
		self.policy_text.set(conf.policy_text_new_value)
# 		logger.debug('SecurityPage : setting "BACKGROUND COLOR" fiend.')
# 		self.background_color.set(conf.background_color_default)
		logger.debug('SecurityPage : setting "REDIRECT URL" fiend.')
		self.redirect_url.set(conf.valid_redirect_url)
		
	def enable_mac_authentication1(self):
		logger.debug("SecurityPage : Enable mac authentication.")
		self.mac_authentication.set(self.config.config_vars.Security_Mac_Authentication_Enabled)
		
	def create_security_internal_server_new_user(self):
		conf = self.config.config_vars
		logger.debug('SecurityPage : Clicking on internal server link')
		self.user_count0.click()
		logger.debug('SecurityPage : setting username value')
		self.userTxt.set(conf.userTxt)
		logger.debug('SecurityPage : setting password value')
		self.pswdTxt.set(conf.pswdTxt)
		logger.debug('SecurityPage : setting retype value')
		self.pswdTxt2.set(conf.pswdTxt2)
		logger.debug('SecurityPage : setting type value')
		self.typeTxt.set(conf.typeTxt)
		self.buy_time()
		logger.debug('SecurityPage : Clicking add button')
		self.updateButton.click()
		logger.debug('SecurityPage : Clicking add button')
		self.okButton.click()
		if self.save_server1:
			self.save_server1.click()
		self.buy_time()
		if self.okButton:
			logger.debug("SecurityPage: Clicking on ok button")
			self.okButton.click()

	def set_encryption(self, value):
		if value == 'Enabled':
			logger.debug("SecurityPage : Enable Wireless Encryption.")
			self.wireless_encryption.set(self.config.config_vars.wireless_encryption)
		else:
			logger.debug("SecurityPage : disable Wireless Encryption.")
			self.wireless_encryption.set(self.config.config_vars.disable_option)
	
	def set_security_key_management(self, value):
		'''
		selecting value from Security Key Management  Drop down
		'''
		if value == 'WPA-2 Personal':
			logger.debug('SecurityPage : Setting Key Management to  WPA-2 Personal')
			self.security_key_management.set(self.config.config_vars.Authentication_wpa2)
		elif value == 'WPA Personal':
			logger.debug('SecurityPage : Setting Key Management to  WPA Personal')
			self.security_key_management.set(self.config.config_vars.key_management)
		elif value == 'Both(WPA-2 & WPA)':
			logger.debug('SecurityPage : Setting Key Management to  Both(WPA-2 & WPA)')
			self.security_key_management.set(self.config.config_vars.Authentication_Wpa2_WPA_Enterprise)
		elif value == 'Static WEP':
			logger.debug('SecurityPage : Setting Key Management to  Static WEP')
			self.security_key_management.set(self.config.config_vars.personal_key_mgt_value)

	def set_pass_phrase_format(self, value):
		'''
		selecting value from Paas Phrase format  Drop down
		'''
		if value == '8-63 chars':
			self.wpa_passphrase_format.set(self.config.config_vars.passphrase_format_8)
		elif value == '64 hexadecimal chars':
			self.wpa_passphrase_format.set(self.config.config_vars.passphrase_format_64)
	
	def set_passphrase_retype(self, passphrase=None, retype=None):
		'''
		Entering Passphrase and Retype passphrase textbox
		'''
		time.sleep(5)
		logger.debug('SecurityPage: writing passphrase')
		self.passphrase.set(passphrase)
		logger.debug('SecurityPage: re-writing passphrase')
		self.retype_passphrase.set(retype)
		
	def set_mac_authentication_value(self,value):
		'''
		setting set mac authentication value from Drop down
		'''
		if value == 'Enabled':
			self.mac_authentication.set(self.config.config_vars.enable_option)
		elif value == 'Disabled':
			self.mac_authentication.set(self.config.config_vars.disable_option)
	
	def configure_reauth_interval(self, time, unit):
		'''
		configuring reauth interval
		'''
		logger.debug("SecurityPage: Writing reauth")
		self.reauth_interval.set(time)
		logger.debug("securityPage: Selecting time unit-min/hr")
		self.reauth_intrvl_unit.set(unit)
	
	def set_wispr(self, value):
		'''
		sets wispr option to enable or disable
		'''
		if value == 'Enabled' :
			self.wispr.set(self.config.config_vars.enable_option)
		elif value == 'Disabled':
			self.wispr.set(self.config.config_vars.disable_option)
	
	def add_internal_sever_user(self):
		'''
		creates internal server user
		'''
		logger.debug("SecurityPage: Clicking on internal server user link ")
		self.show_users_link.click()
		logger.debug("SecurityPage: Writing user name")
		self.userTxt.set(self.config.config_vars.userTxt)
		logger.debug("SecurityPage: Writing password")
		self.buy_time()
		self.pswdTxt.set(self.config.config_vars.pswdTxt)
		logger.debug("SecurityPage: Re-writing password")
		self.pswdTxt2.set(self.config.config_vars.pswdTxt2)
		logger.debug("SecurityPage: selecting type as guest")
		self.buy_time()
		self.typeTxt.set(self.config.config_vars.typeTxt)
		self.buy_time()
		logger.debug("SecurityPage: Clicking on add button")
		self.updateButton.click()
		logger.debug("SecurityPage: Clicking on ok button")
		self.okButton.click()
		if self.okButton:
			logger.debug("SecurityPage: Clicking on ok button")
			self.okButton.click()
		self.buy_time()
		if self.save_server1:
			self.save_server1.click()
		self.buy_time()
		if self.okButton:
			logger.debug("SecurityPage: Clicking on ok button")
			self.okButton.click()
		
	def reset_disable_if_uplink_type_is(self):
		'''
		restores default values of 3G/4g, Wifi, ethernet
		'''
		if self.threeg_or_fourg.is_selected():
			self.threeg_or_fourg.click()
		if self.wifi.is_selected():
			self.wifi.click()
		if self.ethernet.is_selected():
			self.ethernet.click()
	
	def return_acces_page(self):
		'''
		returns to AccessPage
		'''
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()	
		return AccessPage(self.test, self.browser, self.config)
	
	def set_splash_page_visulas(self):
		'''
		sets non default values to splash page visuals
		'''
		logger.debug("SecurityPage: Writing banner title")
		self.banner_title.set(self.config.config_vars.banner_title_new_value)
		logger.debug("SecurityPage: Writing welcome text")
		self.welcome_text.set(self.config.config_vars.welcome_text)
		logger.debug("SecurityPage: Writing policy text")
		self.policy_text.set(self.config.config_vars.policy_text_new_value)
		logger.debug("SecurityPage: Clicking on save button")
		self.save_button.click()
		logger.debug("SecurityPage: clicking on preview splash page")
		self.buy_time()
		self.preview_splash_page.click()
		self.buy_time()
		logger.debug("SecurityPage: clicking on preview splash page close button")
		self.preview_splash_page_close.click()
		
	def set_personal_uppercase_support(self,value=None):
		'''
		sets personal uppercase support
		'''
		if value:
			logger.debug('SecurityPage : Setting  uppercase support')
			self.personal_uppercase_support.set(value)
		else:
			logger.debug('SecurityPage : Setting uppercase support to its default')
			self.personal_uppercase_support.set(self.config.config_vars.Uppercase_Support_default)
			
	def set_authentication_server_2_value(self,value=None):
		'''
		selects authentication server2  
		'''
		if value:
			logger.debug('EditNetworkPage : Setting new external server Value')
			self.authentication_server_2.set(value)
	
	def set_load_balancing_field(self,value=None):
		'''
		sets given value to load balancing field
		'''
		if value:
			logger.debug("SecurityPage :Setting load balancing.")
			self.load_balancing.set(value)
		else:
			logger.debug("SecurityPage :Setting load balancing to its default.")
			self.load_balancing.set(self.config.config_vars.disable_option)
	
	def set_reauth_interval_value(self,value=None):
		'''
		sets reauth interval
		'''
		logger.debug('SecurityPage : Setting reauth_interval value')
		if value:
			self.reauth_interval.set(value)
		else:
			self.reauth_interval.set(self.config.config_vars.reauth_interval_default_value)
	
	def create_internal_server_employee_user(self):
		'''
		creates internal server employee user
		'''
		conf = self.config.config_vars
		logger.debug('SecurityPage : Clicking on internal server link')
		self.user_count0.click()
		logger.debug("Validating the configuration dialog box ")
		if not self.search_user:
			raise AssertionError("New user configuration dialog box is not open .Traceback: %s " %traceback.format_exc())		
		logger.debug('SecurityPage : setting username value')
		self.userTxt.set(conf.userTxt)
		logger.debug('SecurityPage : setting password value')
		self.pswdTxt.set(conf.pswdTxt)
		logger.debug('SecurityPage : setting retype value')
		self.pswdTxt2.set(conf.pswdTxt2)
		logger.debug('SecurityPage : setting type value')
		self.typeTxt.set(conf.typeTxt_employee)
		logger.debug('SecurityPage : Clicking add button')
		self.updateButton.click()
		time.sleep(3)
		logger.debug('SecurityPage : Clicking add button')
		self.okButton.click()	
	
	def set_max_auth_failures_value(self,value=None):
		'''
		sets max auth failures
		'''
		if value:
			logger.debug("SecurityPage: Writing reauth")
			self.max_auth_failures.set(value)
		else:
			logger.debug("SecurityPage: Writing reauth")
			self.max_auth_failures.set(self.config.config_vars.max_authentication_default_value)
	
	
	def set_security_page_value(self):
		logger.debug("SecurityPage: Calling  security_level_enterprise")
		self.security_level_enterprise()
		logger.debug("SecurityPage: Calling  set_key_management_wpa_2_enterprise_option")
		self.set_key_management_wpa_2_enterprise_option()
		logger.debug('SecurityPage : Clicking on Roaming open button')
		self.roaming_open.click()
		logger.debug("SecurityPage: Calling  enable_mac_authentication_enterprise")
		self.enable_mac_authentication_enterprise()
		if not self.personal_delimeter:
			raise AssertionError("Delimiter Character option is not visible .Traceback: %s " %traceback.format_exc())
		if not self.personal_uppercase_support:
			raise AssertionError("Uppercase Support option is not visible .Traceback: %s " %traceback.format_exc())
		logger.debug('SecurityPage : Entering delimeter value')
		self.personal_delimeter.set(self.config.config_vars.delimeter_value)
		logger.debug("SecurityPage : Enable  uppercase support.")	
		self.set_personal_uppercase_support(self.config.config_vars.Uppercase_Support_Enabled)
		logger.debug("SecurityPage: Calling  set_external_radius_server_1")
		self.set_external_radius_server_1()
		
		if not self.authentication_server.get_selected()== self.config.config_vars.auth_server_value:
			raise AssertionError("Authentication Server1 list box is not selected with coufigured value .Traceback: %s " %traceback.format_exc())
		time.sleep(4)
		self.checking_for_authentication_server2_visibility()
		logger.debug('EditNetworkPage : Setting new external server to InternalServer')
		self.set_authentication_server_2_value(self.config.config_vars.internal_server)
		if not self.load_balancing:
			raise AssertionError("Load balancing option is not visible .Traceback: %s " %traceback.format_exc())
		
		logger.debug("SecurityPage: Calling  set_load_balancing_field")
		self.set_load_balancing_field(self.config.config_vars.enable_option)
		logger.debug("SecurityPage: Calling  set_reauth_interval_value")
		self.set_reauth_interval_value(self.config.config_vars.reauth_interval)
		logger.debug("SecurityPage: Calling  create_internal_server_employee_user")
		self.create_internal_server_employee_user()
		
		time.sleep(3)
		if not self.user_count1:
			raise AssertionError("Internal server user count not increment to 1  .Traceback: %s " %traceback.format_exc())
		time.sleep(4)
		logger.debug('SecurityPage : Setting blacklisting to enabled')
		self.blacklisting.set(self.config.config_vars.blacklisting_option)
		logger.debug("SecurityPage: Calling  set_max_auth_failures_value")
		self.set_max_auth_failures_value(self.config.config_vars.max_authentication_failure)
		logger.debug("SecurityPage : Clicking on next")	
		self.next.click()											
		return AccessPage(self.test, self.browser, self.config)

	def configure_splash_page_type(self, value):
		'''
		sets splash page type
		'''
		logger.debug("SecurityPage : Selecting value from splash page type  drop-down.")
		self.splash_page_type.set(value)

	def configure_blacklisting(self, option, value=None):
		'''
		sets Blacklisting 
		'''
		if option == 'Enable':
			logger.debug('SecurityPage : Setting blacklisting to enabled')
			self.blacklisting.set('Enabled')
			logger.debug("SecurityPage: Calling  set_max_auth_failures_value")
			self.set_max_auth_failures_value(value)
		else:
			logger.debug('SecurityPage : Setting blacklisting to Disabled')
			self.blacklisting.set('Disabled')
			
	def configure_encryption(self,encrytion_option,key_management_option,value):
		'''
		sets Encryption Values
		'''
		if encrytion_option == 'Enabled':
			logger.debug("SecurityPage : Enable Wireless Encryption.")
			self.wireless_encryption.set('Enabled')
			if key_management_option == 'Static WEP':
				logger.debug('SecurityPage : Setting Key Management to  Static WEP')
				self.security_key_management.set(self.config.config_vars.key_mngmt_static)
				logger.debug("SecurityPage : Writing Personal Wep key")
				self.personal_wep_key.set(self.config.config_vars.wep_key)
				logger.debug("SecurityPage : re Writing Personal Wep key")
				self.personal_re_wep_key.set(self.config.config_vars.wep_key)
			else:
				logger.debug('SecurityPage : Setting Key Management Value')
				self.security_key_management.set(value)
				logger.debug('SecurityPage: writing passphrase')
				self.passphrase.set(self.config.config_vars.Network_Passphrase)
				logger.debug('SecurityPage: re writing passphrase')
				self.retype_passphrase.set(self.config.config_vars.Network_Passphrase)
				time.sleep(5)
		else:
			logger.debug("SecurityPage : Disable Wireless Encryption.")
			self.wireless_encryption.set('Disabled')			

	def configure_wired_802_1x_authentication(self, value):
		'''
		Selecting value from Wired 802.1x Drop down
		'''
		logger.debug("SecurityPage :Selecting value from Wired 802.1x Drop down.")
		self.dot1x.set(value)
		
	def assert_default_users(self):
		if not self.user_count0:
			raise AssertionError("Default user count is not set to 0 .Traceback: %s " %traceback.format_exc())

	def assert_reauth_interval_unit(self, value, unit):
		if not self.reauth_interval.get() == value:
			raise AssertionError(" Default value of reauth interval is not 0. i.e . Traceback: %s" % traceback.format_exc())
		if not self.reauth_intrvl_unit.get_selected() == unit:
			raise AssertionError(" Default unit is not set to min. i.e . Traceback: %s" % traceback.format_exc())
			
	def set_disable_if_uplink_type_is(self,threeG_fourG,wifi,ethernet):
		'''
		sets 3g/4g, wifi and Ethernet
		'''
		if threeG_fourG:
			if not self.threeg_or_fourg.is_selected():
				logger.debug("SecurityPage : Clicking on 3g/4g")	
				self.threeg_or_fourg.click()
		if wifi:
			if not self.wifi.is_selected():
				logger.debug("SecurityPage : Clicking on wifi")	
				self.wifi.click()
		if ethernet:
			if not self.ethernet.is_selected():
				logger.debug("SecurityPage : Clicking on Ethernet")	
				self.ethernet.click()
				
	def assert_external_spalsh_page_type_default_values(self):
		'''
		Asserting the default values
		wired_captive_portal : --select--
		Wispr_status : Disabled
		wireless_encryption : Disabled
		mac_authentication : Disabled
		authentication_server : InternalServer
		blacklisting : Disabled
		reauth_interval : 0
		show_users_link : 0 users
		blacklist_whitelist : 0 blacklist 0 whitelist
		DISABLE IF UPLINK TYPE IS: 3G/4G, wifi, ethernet unchecked
		'''
		conf = self.config.config_vars
		self.browser.assert_drop_down_value(self.wired_captive_portal, conf.select, "capitive profile  not set to default value")
		self.browser.assert_drop_down_value(self.wispr, conf.Wispr_status, "wispr  not set to default value")
		self.browser.assert_drop_down_value(self.wireless_encryption, conf.disable_option, "encryption  not set to default value")
		self.browser.assert_drop_down_value(self.mac_authentication, conf.Security_Mac_Authentication, "Mac Authentication not set to default value")
		self.browser.assert_drop_down_value(self.authentication_server, conf.internal_server, "authentication server1 not set to default value")
		self.browser.assert_drop_down_value(self.blacklisting, conf.disable_option, "blacklisting not set to default value")
		self.browser.assert_text(self.reauth_interval, conf.reauth_interval_default_value, "blacklisting not set to default value", "value")
		self.browser.assert_element(self.show_users_link, "show users link not present")
		self.browser.assert_element(self.blacklist_whitelist, "blacklisting not set to default value")
		self.browser.assert_check_box_value(self.threeg_or_fourg, "3G/4G checkbox is not unchecked by default", check=True)
		self.browser.assert_check_box_value(self.wifi, "wifi checkbox is not unchecked by default", check=True)
		self.browser.assert_check_box_value(self.ethernet, "ethernet checkbox is not unchecked by default", check=True)
		
	def assert_none_spalsh_page_type_default_values(self):	
		'''
		wireless_encryption : Disabled
		blacklisting : Disabled
		Wispr_status : Disabled
		'''
		conf = self.config.config_vars
		self.browser.assert_drop_down_value(self.wireless_encryption, conf.disable_option, "encryption  not set to default value")
		self.browser.assert_drop_down_value(self.blacklisting, conf.disable_option, "blacklisting not set to default value")
		self.browser.assert_drop_down_value(self.wispr, conf.Wispr_status, "wispr  not set to default value")
		
	def assert_default_wireless_guest_fields(self):
		'''
		asserts default values of security page for wireless guest network
		splash page type : Internal Acknowledged
		mac authentication : Disabled 
		blacklisting : Disabled
		Disable if uplink type is : 3g/4g, Wifi,Ethernet : Unchecked
		Encryption : Disabled
		'''
		conf = self.config.config_vars
		self.browser.assert_drop_down_value(self.splash_page_type, conf.Splash_page_Acknowledged,'Splash page type is not set to default')
		self.browser.assert_drop_down_value(self.mac_authentication, conf.open_roaming_value,'mac authentication is not set to default value')
		self.browser.assert_drop_down_value(self.blacklisting, conf.open_roaming_value,'Blacklisting is not set to default value')
		self.browser.assert_drop_down_value(self.wireless_encryption, conf.open_roaming_value,'wireless encryption is not set to default value')
		self.browser.assert_check_box_value(self.threeg_or_fourg, '3g/4g is not unchecked', check = True)
		self.browser.assert_check_box_value(self.wifi, 'wifi is not unchecked', check = True)
		self.browser.assert_check_box_value(self.ethernet, 'ethernet is not unchecked', check = True)	
	
	def assert_splash_page_internal_auth_fields(self):
		'''
		WISPr : disabled
		MAC Authentication : disabled
		Auth server 1 : Internal Server
		Reauth Interval : 0
		internal server : zero user link
		blacklisting : Disabled
		disable if uplink type is : 3g/4g, Wifi,Ethernet : Unchecked
		Encryption : Disabled
		'''
		conf = self.config.config_vars
		self.browser.assert_drop_down_value(self.mac_authentication, conf.open_roaming_value,'mac authentication is not set to default value')
		self.browser.assert_drop_down_value(self.blacklisting, conf.open_roaming_value,'Blacklisting is not set to default value')
		self.browser.assert_drop_down_value(self.wireless_encryption, conf.open_roaming_value,'wireless encryption is not set to default value')
		self.browser.assert_drop_down_value(self.wispr,conf.open_roaming_value,'Wispr is not set to Disabled')
			
	def assert_splash_page_internal_acknowledged_mac_enabled_field(self):
		'''
		delimiter char : empty
		uppercase support : disabled
		auth server 1: internal server
		reauth interval : 0
		interval server user link : zero show user link
		'''
		conf = self.config.config_vars
		self.browser.assert_drop_down_value(self.authentication_server,conf.Authentication_server,'Auth server1 is not set to InternalServer')
		self.browser.assert_text(self.reauth_interval,conf.invalid_zero_input,'reauth interval is not set to zero','value')
		self.browser.assert_element(self.show_users_link,'zero show users link is not displayed')
		self.browser.assert_text(self.personal_delimeter,'','delimiter is not empty','value')
		
		
	def setting_dynamic_wep_voice_network_value(self,key = None):
		logger.debug("SecurityPage : Selecting SecurityLevel field")
		self.configure_security_level(enterprise=True)
		logger.debug("SecurityPage : Selecting Key Management field")
		if key == 'Dynamic- WEP With 802.1x':
			self.set_key_management_dynamic_wep_option()
		if key == 'WPA-2 Enterprise':
			self.set_key_management_wpa_2_enterprise_option()
		logger.debug("SecurityPage : Creating Authentication_server 1")
		self.create_external_radius_server_in_auth_server_one()
		logger.debug("SecurityPage : Creating Authentication_server 2")
		self.create_external_radius_server_in_auth_server_two()
		logger.debug("SecurityPage : Setting Blacklist and Max Authentication  Failures value")
		self.configure_blacklisting('Enable',self.config.config_vars.max_auth_failure)
		logger.debug("SecurityPage : Setting Reauth interval")
		self.set_reauth_interval()
		logger.debug("SecurityPage : Selecting Load Balancing value")
		self.configure_auth_server_settings(balancing = True)
		
		
	def assert_splash_page_internal_authenticated_mac_enabled_field(self):
		'''
		delimiter char : empty
		uppercase support : disabled
		'''
		conf = self.config.config_vars
		logger.debug("SecurityPage: Asserting Disabled from Uppercase Support dropdown")
		self.browser.assert_drop_down_value(self.personal_uppercase_support,conf.disable_option,'Uppercase Support is not set to Disabled')
		logger.debug("SecurityPage: Asserting whether delimiter field is empty")
		self.browser.assert_text(self.personal_delimeter,'','delimiter is not empty','value')
		
	def assert_auth_server2_and_accounting(self):
		'''
		Auth server2: --select--
		Accounting  : Disabled
		'''
		logger.debug("SecurityPage :checking  By default Auth server2 is set to --select-- or not")
		self.browser.assert_drop_down_value(self.authentication_server_2,self.config.config_vars.select,'By default Auth server2 is not set to --select--')
		logger.debug("SecurityPage :checking  By default Accounting is set to Disabled or not")
		self.browser.assert_drop_down_value(self.accounting,self.config.config_vars.disable_option,'By default Accounting  is not set to Disabled')
		
	def assert_load_balancing(self):
		'''
		Load Balancing  : Disabled
		'''
		logger.debug("SecurityPage :checking  By default Load Balancing is set to Disabled or not")
		self.browser.assert_drop_down_value(self.load_balancing,self.config.config_vars.disable_option,'By default Load Balancing is not set to Disabled')
			
	def assert_accounting_and_user_link(self):
		logger.debug("SecurityPage : Asserting the Accounting field")
		if self.accounting:
			raise AssertionError("SecurityPage : Accounting field is visible")
		logger.debug("SecurityPage : Asserting the User Link field")
		if not self.show_users_link:
			raise AssertionError("SecurityPage : User Link field is not present")
		
	def assert_accounting_mode_and_interval(self):
		'''
		Accounting mode: Authentication
		Accounting Internal: Empty
		'''
		self.browser.assert_drop_down_value(self.accounting_mode,'Authentication','Accounting mode is not set to "Authentication"')
		self.browser.assert_text(self.accounting_interval,'','Accounting Internal is not empty','value')
		
	def assert_internal_server_link(self,visibility=True):
		'''
		Internal server link : Default Visible
		'''
		if not visibility:
			if self.show_users_link:
				raise AssertionError(" Internal server link is visible. i.e . Traceback: %s" % traceback.format_exc())
		else:
			if not self.show_users_link:
				raise AssertionError(" Internal server link is not visible. i.e . Traceback: %s" % traceback.format_exc())
				
	def assert_default_value_security_sp_iternal_auth_as_1_external_as2_internal(self):
		'''
		asserts following fields
		accounting : not visible
		load balancing : disabled 
		interval server user link : zero show user link
		'''
		conf = self.config.config_vars
		logger.debug('SecurityPage : asserting for accounting field')
		if self.accounting:
			raise AssertionError("Accounting option visible for user  . i.e . Traceback: %s" % traceback.format_exc())
		logger.debug('SecurityPage : asserting show user link')	
		self.browser.assert_element(self.show_users_link,'zero show users link is not displayed')
		logger.debug('SecurityPage : asserting load balancing : disabled')	
		self.browser.assert_drop_down_value(self.load_balancing,conf.open_roaming_value,'load balancing field is not set to disabled')

	def set_authentication_server_1_value(self,value=None):
		'''
		selects authentication server1  
		'''
		if value:
			logger.debug('EditNetworkPage : Setting new external server Value')
			self.authentication_server.set(value)

	def edit_network_with_mac_authentication_accounting_accounting_interval(self,enterprise=False,open=False):
		'''
		Sets following fields:
		mac_authentication : Enabled
		Creates Auth_server1 and Auth_server2
		Accounting_interval : 60 
		Load balancing : Enabled
		Reauth interval : 
		'''
		conf = self.config.config_vars
		self.configure_security_level(enterprise,open)
		# self.set_passphrase_retype(conf.Auth_Sharedkey,conf.Auth_Sharedkey)
		self.set_mac_authentication_value('Enabled')
		self.create_external_radiuds_server('1')
		self.create_external_radiuds_server('2')
		self.enable_accounting_interval('60')
		self.set_load_balancing_field(conf.blacklisting_option)
		self.configure_reauth_interval(conf.max_authentication_failure,conf.reauth_intrvl_unit_min)		


	def assert_authentication_server2(self, value):
		'''
		Asserting vales from authentication server2 dropdown
		'''
		conf = self.config.config_vars
		if value == 'New':
			logger.debug("SecurityPage: Asserting --New-- from dropdown")
			self.browser.assert_drop_down_value(self.authentication_server_2,conf.new_server,'Authentication server 2 is not set to --New--')
		if value == 'InternalServer':
			logger.debug("SecurityPage: Asserting InternalServer from dropdown")
			self.browser.assert_drop_down_value(self.authentication_server_2,conf.InternalServer,'Authentication server 2 is not set to InternalServer')
		if value == 'Select':
			logger.debug("SecurityPage: Asserting --Select-- from dropdown")
			self.browser.assert_drop_down_value(self.authentication_server_2,conf.select,'Authentication server 2 is not set to --Select--')
			
	def assert_authentication_server2_dropdown(self):
		conf = self.config.config_vars
		logger.debug('SecurityPage : Asserting Default value of Authentication Server 2 dropdown')
		self.browser.assert_drop_down_value(self.authentication_server_2,conf.select,'Authentication Server 2 is not set to --Select--')
		logger.debug('SecurityPage : Getting  options from Authentication Server 2')
		options = self.authentication_server_2.get_options()
		if not options[1] == self.config.config_vars.new_server:
			raise AssertionError("Authentication Server 2 --New-- element not matched i.e. Traceback: %s" %traceback.format_exc())
		if not options[2] == conf.InternalServer:
			raise AssertionError("'InternalServer' element not found i.e. Traceback: %s" %traceback.format_exc())
		if not options[0] == self.config.config_vars.select:
			raise AssertionError("Authentication Server 2 --Select-- element not matched i.e. Traceback: %s" %traceback.format_exc())	
			
	def assert_auth_survivability_dropdown(self):
		conf = self.config.config_vars
		logger.debug('SecurityPage : Asserting Default value of Auth survivability dropdown')
		self.browser.assert_drop_down_value(self.auth_survivability,conf.disable_option,'Auth survivability is not set to Disabled')
		logger.debug('SecurityPage : Getting all options from Auth survivability')
		options = self.auth_survivability.get_options()
		if not options[1] == self.config.config_vars.enable_option:
			raise AssertionError("Auth survivability Enabled element not matched i.e. Traceback: %s" %traceback.format_exc())
		if not options[0] == self.config.config_vars.disable_option:
			raise AssertionError("Auth survivability Disabled element not matched i.e. Traceback: %s" %traceback.format_exc())
			
	def assert_accounting_dropdown(self):
		conf = self.config.config_vars
		logger.debug('SecurityPage : Asserting Default value of Accounting dropdown')
		self.browser.assert_drop_down_value(self.accounting,conf.disable_option,'Accounting is not set to Disabled')
		logger.debug('SecurityPage : Getting all options from Accounting')
		options = self.accounting.get_options()
		if not options[1] == self.config.config_vars.enable_option:
			raise AssertionError("Accounting Enabled element not matched i.e. Traceback: %s" %traceback.format_exc())
		if not options[0] == self.config.config_vars.disable_option:
			raise AssertionError("Accounting Disabled element not matched i.e. Traceback: %s" %traceback.format_exc())
			
	def set_authentication_server_1_value(self,value=None):
		'''
		selects authentication server1  
		'''
		if value:
			logger.debug('SecurityPage : Setting new external server Value')
			self.authentication_server.set(value)
			
	def get_and_assert_load_balancing_dropdown_elements(self):
		'''
		get and assert Load Balancing options
		'''
		conf = self.config.config_vars
		self.buy_time()
		logger.debug('SecurityPage : getting Load Balancing options')	
		options = self.load_balancing.get_options()
		logger.debug('SecurityPage : Checking for Load Balancing options')	
		if not options[0] == conf.disable_option:
			raise AssertionError("'Disabled' element not found i.e. Traceback: %s" %traceback.format_exc())
		if not options[1] == conf.enable_option:
			raise AssertionError("'Enabled' element not found i.e. Traceback: %s" %traceback.format_exc())
			
	def assert_authentication_server2_survivability_accounting(self):
		'''
		Authentication Server2 : --Select--
		Auth Survivability : Disabled
		Accounting : Disabled
		'''
		conf=self.config.config_vars
		self.browser.assert_drop_down_value(self.authentication_server_2,conf.select,'Authentication Server2 is not selected as --Select-- by default')
		self.browser.assert_drop_down_value(self.auth_survivability,conf.disable_option,'Auth Survivability is not selected as Disabled by default')
		self.browser.assert_drop_down_value(self.accounting,conf.disable_option,'Accounting is not selected as Disabled by default')

	def get_and_assert_accounting_dropdown_elements(self):
		'''
		Asserting accounting dropdown elements and its default value
		'''
		conf = self.config.config_vars
		self.buy_time()
		logger.debug('SecurityPage : getting Accounting options') 
		options = self.accounting.get_options()
		logger.debug('SecurityPage : Checking for Accounting options') 
		if not options[0] == conf.disable_option:
			raise AssertionError("'Disabled' element not found i.e. Traceback: %s" %traceback.format_exc())
		if not options[1] == conf.enable_option:
			raise AssertionError("'Enabled' element not found i.e. Traceback: %s" %traceback.format_exc())
		
	def get_and_assert_auth_survivability_dropdown_elements(self):
		'''
		Asserting Auth Survivability dropdown elements and its default value
		'''
		conf = self.config.config_vars
		self.buy_time()
		logger.debug('SecurityPage : getting Auth Survivability options') 
		options = self.auth_survivability.get_options()
		logger.debug('SecurityPage : Checking for Auth Survivability options') 
		if not options[0] == conf.enable_option:
			raise AssertionError("'Enabled' element not found i.e. Traceback: %s" %traceback.format_exc())
		if not options[1] == conf.disable_option:
			raise AssertionError("'Disabled' element not found i.e. Traceback: %s" %traceback.format_exc())	
		
	def get_and_assert_authentication_server2_dropdown_elements(self):
		'''
		Asserting Auth Server2 dropdown elements and its default value
		'''
		conf = self.config.config_vars
		self.buy_time()
		logger.debug('SecurityPage : getting Auth Server2 options') 
		options = self.authentication_server_2.get_options()
		logger.debug('SecurityPage : Checking for Auth Server2 options') 
		if not options[0] == conf.select:
			raise AssertionError("'--Select--' element not found i.e. Traceback: %s" %traceback.format_exc())
		if not options[1] == conf.new_server:
			raise AssertionError("'--New--' element not found i.e. Traceback: %s" %traceback.format_exc())	
		if not options[2] == conf.InternalServer:
			raise AssertionError("'InternalServer' element not found i.e. Traceback: %s" %traceback.format_exc())
		if not options[3] == conf.auth_server_value_2:
			raise AssertionError("'testradius_2' element not found i.e. Traceback: %s" %traceback.format_exc())		
			
	def assert_accounting_accounting_interval(self,visibile=True):
		'''
		Asserts accounting and accounting interval fields visibility
		'''
		if visibile:
			logger.debug('SecurityPage : checking Accounting dropdown and accounting interval visible')
			if not self.accounting:
				raise AssertionError("Accounting dropdown is not visible i.e. Traceback: %s" %traceback.format_exc())
				self.buy_time()
			else:
				self.accounting.set('Enable')
				if not self.accounting_interval:
					raise AssertionError("Accounting interval is not visible i.e. Traceback: %s" %traceback.format_exc())
					self.buy_time()
		else:
			logger.debug('SecurityPage : checking Accounting dropdown and accounting interval visible')
			if self.accounting:
				raise AssertionError("Accounting dropdown is visible i.e. Traceback: %s" %traceback.format_exc())
				self.buy_time()		
				
				
	def open_voice_network_with_accounting_interval_uppercase_supported(self,enterprise=False,open=False):
		'''
		Sets following fields:
		mac_authentication : Enabled
		Creates Auth_server1 and Auth_server1
		'''
		conf = self.config.config_vars
		self.configure_security_level(enterprise,open)
		self.set_mac_authentication_value('Enabled')
		self.create_external_radiuds_server('1')
		logger.debug('EditNetworkPage : Setting new external server to InternalServer')
		self.set_authentication_server_2_value(self.config.config_vars.internal_server)
			
	def get_and_assert_authentication_server1_dropdown_elements(self):
		'''
		Asserting Auth Server 1 dropdown elements and its default value
		'''

		conf = self.config.config_vars
		self.buy_time()
		logger.debug('SecurityPage : getting Auth Server options') 
		options = self.authentication_server.get_options()
		logger.debug('SecurityPage : Checking for Auth Server options')
		if not options[2] == conf.InternalServer:
			raise AssertionError("'InternalServer' element not found i.e. Traceback: %s" %traceback.format_exc())
		if not options[0] == conf.select:
			raise AssertionError(" '--Select--' element not found i.e. Traceback: %s" %traceback.format_exc()) 
		if not options[1] == conf.new_server:
			raise AssertionError("'--New--' element not found i.e. Traceback: %s" %traceback.format_exc())

	def assert_auth_server1_selected_option(self,option):
		'''
		asserts auth server1 selected option with param: option
		'''
		logger.debug('Network : SecuritPage : Checking authe server1 selected option')
		self.browser.assert_drop_down_value(self.authentication_server, option, 'Authentication server is not set to %s' %option)

	def validate_authentication_server_name(self):
		'''
		validates auth server name 
		auth server name should not accept any special charecter except hypen and underscore
		'''
		conf = self.config.config_vars
		logger.debug("SecurityPage : Write Server name")
		self.auth_server_name.set(conf.passphrase_spcl_char)
		logger.debug('SecurityPage : Saving external radius server')
		self.save_server.click()
		self.buy_time()
		if not self.name_error:
			raise AssertionError("NetworkPage :SecuritPage :auth server name is accepting special characters i.e. Traceback: %s" %traceback.format_exc())
		logger.debug("SecurityPage : Write Server name")
		self.auth_server_name.set(conf.hypen_underscore)
		logger.debug('SecurityPage : Saving external radius server')
		self.save_server.click()
		if self.name_error:
			raise AssertionError("NetworkPage :SecuritPage :auth server is not accepting valid characters i.e. Traceback: %s" %traceback.format_exc())
		logger.debug("SecurityPage : Write Server name")
		self.auth_server_name.set(conf.auth_server_name)
		logger.debug("SecurityPage : Write Shared key.")
		self.Auth_Sharedkey.set(conf.blacklisting_option)
		logger.debug('NetworkPage: SecurityPage : Auth server1 : Clicking save server button')
		logger.debug("SecurityPage : Write retype - Shared key.")
		self.Retype_auth_shared_key.set(conf.blacklisting_option)
		logger.debug("SecuritPage: Write DRP vlan value")
		if not self.drpvlan_disabled:
			self.drpvlan.set(self.config.config_vars.reauth_value)
		self.save_server.click()


	def assert_auth_server2_internal_server_count_warning(self):
		'''
		authentication_server2 : -- Select --
		internal server cunt : not visible
		warning message : not visible
		'''
		conf = self.config.config_vars
		self.browser.assert_element(self.show_users_link,'zero show users link is displayed',False)
		self.browser.assert_element(self.zero_users_warning,'Only registered users of type "Employee" will be able to access this networks is displayed',False)
		self.browser.assert_drop_down_value(self.authentication_server_2,conf.select,'Auth server to is not set to -- Select --')

	def validate_reauth_interval_field(self,unit):
		'''
		validates reauth interval
		'''
		logger.debug("SecurityPage : Selecting '%s'..." %unit)
		self.reauth_intrvl_unit.set(unit)
		logger.debug("SecurityPage : Writing alphabet in reauth interval text-box...")
		self.reauth_interval.set(self.config.config_vars.reauth_intrvl_alpha)
		logger.debug("SecurityPage : Clicking on next") 
		self.next.click()
		if not (self.reauth_interval_error_msg_mins or self.reauth_interval_error_msg_hrs):
			raise AssertionError("'Must be a number' error message not found. i.e . Traceback: %s" % traceback.format_exc())

		logger.debug("SecurityPage : Writing special chars in reauth interval text-box...")
		self.reauth_interval.set(self.config.config_vars.reauth_intrvl_spcl_char)
		logger.debug("SecurityPage : Clicking on next") 
		self.next.click()
		if not (self.reauth_interval_error_msg_mins or self.reauth_interval_error_msg_hrs):
			raise AssertionError("'Must be a number' error message not found. i.e . Traceback: %s" % traceback.format_exc())

		logger.debug("SecurityPage : Writing invalid numbers in reauth interval text-box...")
		if unit == self.config.config_vars.reauth_intrvl_unit_min:
			self.reauth_interval.set(self.config.config_vars.reauth_intrvl_num_invalid)
		else:
			self.reauth_interval.set(self.config.config_vars.reauth_intrvl_num_invalid_hrs)
		logger.debug("SecurityPage : Clicking on next") 
		self.next.click()
		if not (self.reauth_interval_error_msg_mins or self.reauth_interval_error_msg_hrs):
			raise AssertionError("'Must be a number' error message not found. i.e . Traceback: %s" % traceback.format_exc())

		logger.debug("SecurityPage : Writing null character in reauth interval text-box...")
		self.reauth_interval.set('')
		logger.debug("SecurityPage : Clicking on next") 
		self.next.click()
		if not (self.reauth_interval_error_msg_mins or self.reauth_interval_error_msg_hrs):
			raise AssertionError("'Must be a number' error message not found. i.e . Traceback: %s" % traceback.format_exc())
			
			
	def assert_splash_page_type_and_mac_authentication(self):
		'''
		splash page type : Internal Authenticated
		mac_authentication : Disabled
		'''
		conf = self.config.config_vars
		self.browser.assert_drop_down_value(self.splash_page_type, conf.Splash_page_Authenticated,'Splash page type is not set to default')
		self.browser.assert_drop_down_value(self.mac_authentication, conf.Security_Mac_Authentication, "Mac Authentication not set to default value")
			
	def assert_internal_authenticated_fields(self):
		'''
		Authentication server1 : InternalServer
		auth server 1: internal server
		reauth interval : 0
		'''
		conf = self.config.config_vars
		self.assert_auth_server_internal_server_option()
		self.browser.assert_text(self.reauth_interval,conf.invalid_zero_input,'reauth interval is not set to zero','value')
		self.browser.assert_element(self.show_users_link,'zero show users link is not displayed')	
		self.browser.assert_element(self.zero_users_warning,'zero users warning link is not displayed')	
			
	def create_authenticate_server(self):
		'''
		Creates New Authenticate Server1
		'''
		logger.debug("SecurityPage : set Authentication Server as new")
		self.set_authentication_server('new')
		logger.debug("SecurityPage : Write Server name")
		self.auth_server_name.set(self.config.config_vars.userTxt)
		logger.debug("SecurityPage : Writing Server ip address")
		self.auth_ipaddr.set(self.config.config_vars.valid_auth_server_ip)
		logger.debug('SecurityPage : Writing auth Sharedkey value')
		self.Auth_Sharedkey.set(self.config.config_vars.auth_shared_key)
		logger.debug("SecurityPage : Write retype - Shared key.")
		self.Retype_auth_shared_key.set(self.config.config_vars.auth_shared_key)
		logger.debug("SecuritPage: Write DRP vlan value")
		if not self.drpvlan_disabled:
			self.drpvlan.set(self.config.config_vars.reauth_value)
		logger.debug('EditNetworkPage : Saving external radius server')
		self.save_server.click()
		self.buy_time()
		
	def assert_security_sp_internal_auth_wispr_enabled_fields(self,captive=False):
		'''
		Accounting Mode : Authentication
		Accounting Interval :
		Auth server1: --select--
		Auth server2: --select--		
		'''
		logger.debug("SecurityPage :checking  By defaultAccounting Mode is set to Authentication or not")
		self.browser.assert_drop_down_value(self.accounting_mode,self.config.config_vars.accounting_mode,'By default Accounting Mode is not set to Authentication')
		logger.debug("SecurityPage :checking  By default Accounting Interval is empty or not")
		self.browser.assert_text(self.accounting_interval,'','Accounting Interval is not empty','value')
		# logger.debug("SecurityPage :checking  By default Auth server1 is set to --select-- or not")
		# self.browser.assert_drop_down_value(self.authentication_server,self.config.config_vars.select,'By default Auth server1 is not set to --select--')
		self.create_external_radius_server_in_auth_server_one()
		logger.debug("SecurityPage :checking  By default Auth server2 is set to --select-- or not")
		self.browser.assert_drop_down_value(self.authentication_server_2,self.config.config_vars.select,'By default Auth server2 is not set to --select--')
		logger.debug("SecurityPage :checking Show User is present or not")
		if self.show_users_link:
			raise AssertionError("Show User is present .Traceback: %s " %traceback.format_exc())
		logger.debug("SecurityPage :checking MAC Authentication is present or not")
		if self.mac_authentication:
			raise AssertionError("MAC Authentication is present .Traceback: %s " %traceback.format_exc())
		if captive:
			logger.debug("SecurityPage :checking  By default Captive Portal is set to --select-- or not")
			self.browser.assert_drop_down_value(self.wired_captive_portal,self.config.config_vars.select,'By default Captive Portal is not set to --select--')
			
	def assert_external_splash_page_type_fields(self):
		'''
		wired_captive_portal : --select--
		mac_authentication : Disabled
		authentication_server : InternalServer
		blacklisting : Disabled
		reauth_interval : 0
		show_users_link : 0 users
		blacklist_whitelist : 0 blacklist 0 whitelist
		'''
		conf = self.config.config_vars
		logger.debug('Network : SecuritPage : Checking Wired Captive Portal selected as  --select-- by default')
		self.browser.assert_drop_down_value(self.wired_captive_portal, conf.select, "capitive profile  not set to default value")
		self.browser.assert_drop_down_value(self.mac_authentication, conf.Security_Mac_Authentication, "Mac Authentication not set to default value")
		self.browser.assert_drop_down_value(self.authentication_server, conf.internal_server, "authentication server1 not set to default value")
		self.browser.assert_text(self.reauth_interval, conf.reauth_interval_default_value, "blacklisting not set to default value", "value")
		self.browser.assert_element(self.show_users_link, "show users link not present")
		self.browser.assert_element(self.zero_users_warning,'zero users warning link is not displayed')	
		self.browser.assert_element(self.blacklist_whitelist, "blacklisting not set to default value")
		
	def click_on_edit_captive_portal(self):
		'''
		Clicks on Captive Portal
		'''
		logger.debug('SecurityPage : clicking on Edit button')
		self.edit_captive_portal.click()
		if not self.captive_type:
			self.edit_captive_portal.click()
		self.buy_time()
		
	def assert_external_captive_portal_default(self):
		'''
		Capitive Type : Authentiation text
		Capitive Ip : 10.30.40.50
		Capitive Url : /
		Capitive Port : 80
		Capitive Portal Failure : Deny Internet
		Url Whitelisting : checked
		Auth Text : Authenticated
		Redirect Url : 
		'''
		conf = self.config.config_vars
		logger.debug('Network : SecuritPage : Asserting Captive Profile name ')
		if not self.disabled_default:
			raise AssertionError("Captive profile name field not disabled and it Editable i.e. Traceback: %s" %traceback.format_exc())
		logger.debug('Network : SecuritPage : Checking Captive Type selected as Authentiation text by default')
		self.browser.assert_drop_down_value(self.captive_type, conf.captive_portal_auth_text, "capitive Type  not set to Authentiation text by default")
		# logger.debug('Network : SecuritPage : Checking Captive Ip selected as 10.30.40.50 by default')
		# self.browser.assert_text(self.captive_ip, conf.external_captive_ip, "capitive Ip  not set to 10.30.40.50  by default", "value")
		logger.debug('Network : SecuritPage : Checking Captive Url selected as / by default')
		self.browser.assert_text(self.captive_url, conf.external_captive_url, "capitive Url  not set to /  by default", "value")
		logger.debug('Network : SecuritPage : Checking Captive Port selected as 80 by default')
		self.browser.assert_text(self.captive_port, conf.external_captive_port, "capitive Url  not set to 80 by default", "value")
		# logger.debug('Network : SecuritPage : Checking Captive Portal Failure selected as Deny Internet by default')
		# self.browser.assert_drop_down_value(self.Security_CaptivePortalFailure, conf.external_captive_portal_failure, "capitive Portal Failure  not set to Deny Internet by default")
		logger.debug('Network : SecuritPage : Checking Url Whitelisting is checked  by default')
		self.browser.assert_check_box_value(self.Secuirty_auto_url_whitelisting, "Url Whitelisting checkbox is not checked by default", uncheck=True)
		logger.debug('Network : SecuritPage : Checking Captive Auth Text selected as  by default')
		self.browser.assert_text(self.captive_auth_text, conf.external_captive_auth_text, "capitive Auth Text not set to Authenticated by default", "value")
		logger.debug('Network : SecuritPage : Checking Captive Redirect Url selected as  by default')
		self.browser.assert_text(self.Secuirty_redirect_url, '', "capitive Redirect Url textbox not Empty by default", "value")	
		
	def create_walled_garden_white_and_blacklist(self):
		'''
		Creates Whitelist and Blacklist
		'''
		logger.debug("SecurityPage : Selecting the Blacklist field. ")
		self.blacklist_whitelist.click()
		logger.debug("SecurityPage : clicking on new button to create a new blacklist. ")
		self.blacklist_new.click()
		logger.debug("SecurityPage : Entering the blacklist_name in the text field.")
		self.new_regex.set(self.config.config_vars.blacklist_name)
		self.walled_new_save.click()
		logger.debug("SecurityPage : clicking on new button to create a new whitelist. ")
		self.whitelist_new.click()
		logger.debug("SecurityPage : Entering the whitelist_name in the text field.")
		self.new_regex.set(self.config.config_vars.whitelist_name)
		logger.debug("SecurityPage : Clicking on the save button. ")
		self.walled_new_save.click()
		time.sleep(3)
		self.walled_save.click()
		time.sleep(3)
			
			
			
	def assert_wired_mac_authentication_fail_through(self):
		'''
		Mac Authentication fail through : Disabled
		'''
		conf = self.config.config_vars
		logger.debug('Network : SecuritPage : Checking Wired Mac Authentication fail through selected as Disabled by default')
		self.browser.assert_drop_down_value(self.mac_authentication_fail_through, conf.disable_option, "Mac Authentication fail through  not set to default value")
			
	def configure_wired_mac_authentication_fail_through(self,value):
		'''
		configure Mac Authentication fail through 
		'''	
		logger.debug("SecurityPage : Sets Mac Authentication fail through . ")		
		self.mac_authentication_fail_through.set(value)			

	def assert_wired_guest_network_security_level_defaults(self):
		'''
		Asserts all security level default values for wired guest network. 
		'''
		logger.debug('SecurityPage : checking default splash page type value')
		self.browser.assert_drop_down_value(self.splash_page_type, self.config.config_vars.Splash_page_Acknowledged,'Splash page type is not set to default')
		logger.debug('SecurityPage : checking default mac authentication value')
		self.browser.assert_drop_down_value(self.mac_authentication, self.config.config_vars.open_roaming_value,'mac authentication is not set to default value')
		# logger.debug('SecurityPage : asserting 3g/4g checkbox')
		# self.browser.assert_check_box_value(self.threeg_or_fourg, '3g/4g is not unchecked', check = True)
		# logger.debug('SecurityPage : asserting wifi checkbox')
		# self.browser.assert_check_box_value(self.wifi, 'wifi is not unchecked', check = True)
		# logger.debug('SecurityPage : asserting ethernet checkbox')
		# self.browser.assert_check_box_value(self.ethernet, 'ethernet is not unchecked', check = True)
		
	def assert_wired_guest_network_security_level_Splash_page_visuals_defaults(self):
		'''
		Asserts all splash page visuals default values.
		'''
		logger.debug("SecurityPage : Asserting banner title default text")
		self.browser.assert_text(self.banner_title, self.config.config_vars.banner_title_guest_network_default,'Banner title is not set to default value','value')
		# logger.debug("SecurityPage : Asserting headercolor default text")
		# self.browser.assert_text(self.header_color, self.config.config_vars.header_color_default,'Header color is not set to default value','value')
		logger.debug("SecurityPage : Asserting  default welcome_text")
		self.browser.assert_text(self.welcome_text, self.config.config_vars.welcome_text_default,'Welcome text is not set to default value','value')
		logger.debug("SecurityPage : Asserting  default policy_text")
		self.browser.assert_text(self.policy_text, self.config.config_vars.policy_text_default,'policy text is not set to default value','value')
		# logger.debug("SecurityPage : Asserting  default background_color text")
		# self.browser.assert_text(self.background_color, self.config.config_vars.background_color_default,'background color is not set to default value','value')
		logger.debug("SecurityPage : Asserting  default redirect url text")
		self.browser.assert_text(self.redirect_url, self.config.config_vars.redirect_url_default,'redirect url is not set to default value','value')
		
		
	def assert_wired_network_redirected_url(self):
		'''
		Asserts invalid redirected url error message 
		'''
		logger.debug("SecurityPage : Setting invalid redirect url...")
		self.redirect_url.set(self.config.config_vars.invalid_redirect_url)
		logger.debug('SecurityPage : Clicking save button..')
		self._save_settings()
		if not self.redirect_url_error_message:
			raise AssertionError("SecurityPage : Required error message is not displayed .Traceback: %s " %traceback.format_exc())
		
	def set_default_redirect_url(self):
		'''
		Sets redirected url to empty value/default value.
		'''
		logger.debug('SecurityPage : Setting empty redirect url...')
		self.redirect_url.set(self.config.config_vars.redirect_url_default)
		logger.debug('SecurityPage : Clicking save button..')
		self._save_settings()
		
	def set_leap_use_session_key(self,enable=False):
		'''
		Enables or Disables the 'leap use session key' checkbox.
		'''
		if enable:
			if self.leap_use_session_key:
				if not self.leap_use_session_key.is_selected():
					logger.debug('SecurityPage : Clicking on Use session key for LEAP')
					self.leap_use_session_key.click()
			else:
				raise AssertionError("SecurityPage : element 'Leap use session key' not found.Traceback: %s " %traceback.format_exc())
		else:
			if self.leap_use_session_key:
				if self.leap_use_session_key.is_selected():
					logger.debug('SecurityPage : Clicking on Use session key for LEAP')
					self.leap_use_session_key.click()
					
					
	
	
	def assert_splash_page_fields(self):
		'''
		Asserts splash page fields
		'''
		logger.debug('SecurityPage : checking Splash page Username textbox...')
		self.browser.assert_text(self.splash_page_user_name,'','Splash page Username textbox is not empty','value')
		logger.debug('SecurityPage : checking Splash page password textbox...')
		self.browser.assert_text(self.splash_page_password,'','Splash page password textbox is not empty','value')
		logger.debug('SecurityPage : checking Splash page Login button...')
		self.browser.assert_element(self.splash_page_login, "splash page Login button is not present")
		
		
	def assert_splash_page_type_disabled_option(self):
		'''
		Checking Splash page type option disabled or not
		'''
		logger.debug('SecurityPage : checking External - RADIUS Authentication is disabled or not...')
		self.browser.assert_element(self.external_radius_authentication, "External - RADIUS Authentication is not disabled")	
		logger.debug('SecurityPage : checking External - Authentication Text is disabled or not...')
		self.browser.assert_element(self.external_authentication_text, "External - Authentication Text is not disabled")
		logger.debug('SecurityPage : checking Splash page type External is disabled or not...')		
		self.browser.assert_element(self.splash_page_type_external, "Splash page type External is  disabled")	
			
	def set_wep_key_size(self,wep_key):
		'''
		Sets Wep Key size
		'''
		logger.debug("SecurityPage : Set value of WEP Key Size to 128-bit.")
		self.wep_key_size.set(wep_key)

	def create_blacklist_whitelist_walled_garden(self, blacklist = True, whitelist = True):
		'''
		creates blacklist and whitelist
		'''
		logger.debug("SecurityPage : Selecting the Blacklist field. ")
		self.blacklist_whitelist.click()
		if blacklist == True :
			logger.debug("SecurityPage : clicking on new button to create a new blacklist. ")
			self.blacklist_new.click()
			logger.debug("SecurityPage : Entering the invalid value in the text field.")
			self.new_regex.set(self.config.config_vars.blacklist_name)
			logger.debug("SecurityPage : Clicking on the save button. ")
			self._walled_new_save_button()
		if whitelist == True :
			logger.debug("SecurityPage : clicking on new button to create a new whitelist. ")
			self.whitelist_new.click()
			logger.debug("SecurityPage : Entering the exceeded value in the text field.")
			self.new_regex.set(self.config.config_vars.new_regex_valid)
			logger.debug("SecurityPage : Clicking on the save button. ")
			self._walled_new_save_button()
			self.walled_save.click()

	def create_security_captive_portal_profile(self):
		self.splash_page_type.set(self.config.config_vars.Splash_page_external)
		logger.debug("Entering the captive portal value. ")
		self.wired_captive_portal.set(self.config.config_vars.Wired_Captive_Profile_New)
		self.buy_time()
		logger.debug("Entering the captive Type value. ")
		self.captive_type.set(self.config.config_vars.Captive_Role_Text)
		logger.debug("Entering the captive Name value. ")
		self.captive_name.set(self.config.config_vars.Captive_Role_Name)
		logger.debug("Entering the captive Ip value. ")			
		self.captive_ip.set(self.config.config_vars.Captive_Role_Ip)
		logger.debug("Entering the captive Url . ")		
		if self.captive_url:
			logger.debug("Entering the captive Url value. ")	
			self.captive_url.set(self.config.config_vars.domain_name)
		logger.debug("Entering the captive Port value. ")
		self.captive_port.set(self.config.config_vars.Captive_Role_Port)
		logger.debug("Entering the captive Auth text value. ")
		self.captive_auth_text.set(self.config.config_vars.Captive_Role_Name)
		logger.debug("SecurityPage : Clicking on save")	
		self.save.click()
		self.buy_time()	
	
	def edit_captive_portal_profile(self):
		self.splash_page_type.set(self.config.config_vars.Splash_page_external)
		logger.debug("Entering the captive portal value. ")
		self.wired_captive_portal.set(self.config.config_vars.captive_text_1)
		self.buy_time()
		logger.debug("Clicking on Edit Button ")
		self.click_on_edit_captive_portal()
		logger.debug("Entering the captive Ip value. ")			
		self.captive_ip.set(self.config.config_vars.auth_ipaddr)
		logger.debug("Entering the captive Url . ")		
		if self.captive_url:
			logger.debug("Entering the captive Url value. ")	
			self.captive_url.set(self.config.config_vars.domain_name_value)
		logger.debug("Entering the captive Port value. ")
		self.captive_port.set(self.config.config_vars.captive_port_default)
		logger.debug("SecurityPage : Clicking on save")	
		self.save.click()
		self.buy_time()
		if self.save:
			self.save.click()

	def save_captive_profile_button(self):
		'''
		clicks 'Save' button.
		'''
		logger.debug("EditNetworkPage: Clicking on 'SAVE' button")
		if self.save:
			self.save.click()
			self.buy_time()
	
	def assert_default_captive_portal_profile_error(self):
		'''
		Asserts Captive portal profile error.
		'''
		logger.debug("EditNetworkPage: Asserting Captive portal profile error")
		if not self.captive_portal_error_msg:
			raise AssertionError("SecurityPage : Captive portal profile error message not found.Traceback: %s " %traceback.format_exc())
		
	def click_captive_profile_cancel_button(self):
		'''
		Clicks on 'Cancel' button
		'''
		if self.cap_cancel:
			logger.debug('SecurityPage :  Clicking on Cancel button')
			self.cap_cancel.click()
			
	def click_on_next_button(self):
		'''
		Clicks on 'NEXT' button.
		'''
		logger.debug("SecurityPage : Clicking on next")
		if self.next:
			self.next.click()
			self.buy_time()
		if not self.role_radio:
			self.next.click()
		
	def assert_default_captive_portal_type(self):
		'''
		Asserts Captive portal type 'Default' option's type.
		'''
		logger.debug('Network : SecuritPage : Checking Captive Type selected as Authentiation text by default')
		self.browser.assert_drop_down_value(self.captive_type, self.config.config_vars.captive_portal_auth_text, "capitive Type  not set to Authentiation text by default")

	def assert_default_captive_portal_auth_text(self):
		'''
		Asserts Captive portal type 'Default' option's auth text.
		'''
		logger.debug('Network : SecuritPage : Checking Captive Auth Text selected as  by default')
		self.browser.assert_text(self.captive_auth_text, self.config.config_vars.external_captive_auth_text, "capitive Auth Text not set to Authenticated by default", "value")
		
	def set_accounting_mode(self,value=True):
		'''
		Sets accounting mode dropdown value.
		'''
		conf = self.config.config_vars
		if value:
			logger.debug('Network : SecuritPage : Setting accounting mode to Authentication')
			self.accounting_mode.set(conf.accounting_mode)
		else:
			logger.debug('Network : SecuritPage : Setting accounting mode to Association')
			self.accounting_mode.set(conf.accounting_mode_association)
			
			
	def set_captive_name(self,name):
		'''
		Sets Captive Name
		'''
		logger.debug("Entering the captive Name value. ")
		self.captive_name.set(name)
		
	def set_captive_ip(self,ip):
		'''
		Sets Captive Ip
		'''
		logger.debug("Entering the captive Ip value. ")			
		self.captive_ip.set(ip)	
	
	def set_use_https(self,value):
		'''
		sets USE HTTPS
		'''
		if value == 'check':
			if not self.use_https.is_selected():
				self.use_https.click()
		if value == 'uncheck':
			if self.use_https.is_selected():
				self.use_https.click()

	def set_secuirty_auto_url_whitelisting(self,value):
		'''
		sets secuirty auto url whitelisting
		'''
		if value == 'check':
			if not self.Secuirty_auto_url_whitelisting.is_selected():
				self.Secuirty_auto_url_whitelisting.click()
		if value == 'uncheck':
			if self.Secuirty_auto_url_whitelisting.is_selected():
				self.Secuirty_auto_url_whitelisting.click()

	def set_captive_url(self,url):
		'''
		Sets Captive url
		'''
		logger.debug("Entering the captive Url value. ")	
		self.captive_url.set(url)

	def set_captive_port(self,port):
		'''
		sets Capitive Port
		'''
		logger.debug("Entering the captive Port value. ")
		self.captive_port.set(port)

	def click_on_captive_portal_profile_save(self):
		'''
		Clicking on save button
		'''
		logger.debug("SecurityPage : Clicking on save")	
		self.save.click()
		self.buy_time()	
		
	def create_captive_portal_profile_with_whitelisting_enabled(self):
		'''
		creates Captive Portal Profile
		'''
		conf = self.config.config_vars
		self.wired_captive_portal.set(conf.Wired_Captive_Profile_New)
		logger.debug("Entering the captive Name value. ")
		self.set_captive_name(conf.Captive_Role_Name)
		self.captive_ip.set(conf.Captive_Role_Ip)
		self.set_use_https('uncheck')
		self.set_captive_url(conf.domain_name)
		self.set_captive_port(conf.Captive_Role_Port)
		self.set_secuirty_auto_url_whitelisting('check')
		self.click_on_captive_portal_profile_save()
	
	def set_accounting_mode(self,value=True):
		conf = self.config.config_vars
		if value:
			logger.debug('Network : SecuritPage : Setting accounting mode to Authentication')
			self.accounting_mode.set(conf.accounting_mode)
		else:
			logger.debug('Network : SecuritPage : Setting accounting mode to Association')
			self.accounting_mode.set(conf.accounting_mode_association)
					
	def set_security_captive_portal_failure(self,value):
		'''
		sets Security Captive Portal Failure
		'''
		logger.debug('Network : SecuritPage : Setting Security Captive Portal Failure')
		self.Security_CaptivePortalFailure.set(value)
		
		
	def creating_two_external_auth_server_with_mac_auth(self):
		logger.debug('EditNetworkPage: Creating Captive Portal')
		self.create_captive_portal_profile_with_whitelisting_enabled()
		logger.debug('EditNetworkPage :Setting MAC Authentication')
		self.configure_auth_server_settings(mac_authentication = True)
		logger.debug('EditNetworkPage :Creating Auth Server1')
		self.create_external_radius_server_in_auth_server_one()
		logger.debug('EditNetworkPage :Creating Auth Server2')
		self.create_external_radius_server_in_auth_server_two()
		self.configure_auth_server_settings(balancing = True)
		logger.debug('EditNetworkPage :Set Accouting field.')
		self.accounting.set(self.config.config_vars.enable_option)
		logger.debug('EditNetworkPage :Set Accouting Mode')
		self.accounting_mode.set(self.config.config_vars.accounting_mode)
		logger.debug('EditNetworkPage :Set Accouting Interval.')
		self.accounting_interval.set(self.config.config_vars.accounting_interval_value_20)

	def create_external_captive_portal_1(self,redirect_url='',type=True,https=True,portal_failure=True,whitelisting=True):
		conf = self.config.config_vars
		self.wired_captive_portal.set(conf.Wired_Captive_Profile_New)
		logger.debug("Entering the captive Name value. ")
		self.captive_name.set(conf.Captive_Role_Name)
		logger.debug("Entering the captive Type value. ")
		if type:
			self.captive_type.set(conf.Captive_Role_Radius_Authentication)
		else:
			self.captive_type.set(conf.Captive_Role_Text)
		logger.debug("Entering the captive Ip value. ")	
		self.captive_ip.set(conf.Captive_Role_Ip)
		if self.captive_url:
			logger.debug("Entering the captive Url. ")		
			self.captive_url.set(conf.domain_name)			
		logger.debug("Entering the captive Port value. ")										
		self.captive_port.set(conf.Captive_Role_Port)
		
		if https:
			logger.debug("Enabling the use-https checkbox.")
			if not self.use_https.is_selected():
				self.use_https.click()
		else:
			logger.debug("Disabling the use-https checkbox.")
			if self.use_https.is_selected():
				self.use_https.click()
				
		if portal_failure:
			logger.debug("Setting the captive Portal Failure as 'Deny Internet'. ")
			self.Security_CaptivePortalFailure.set(conf.external_captive_portal_failure)
		else:
			logger.debug("Setting the captive Portal Failure as 'Allow Internet'. ")
			self.Security_CaptivePortalFailure.set(conf.captive_portal_failure_allow)
			
		if whitelisting:
			logger.debug("Disabling the Auto URL Whitelisting checkbox.")
			if self.Secuirty_auto_url_whitelisting.is_selected():
				self.Secuirty_auto_url_whitelisting.click()
		else:
			logger.debug("Enabling the Auto URL Whitelisting checkbox.")
			if not self.Secuirty_auto_url_whitelisting.is_selected():
				self.Secuirty_auto_url_whitelisting.click()
		
		logger.debug("Setting redirect_url value.")
		self.Secuirty_redirect_url.set(redirect_url)
		logger.debug("SecurityPage : Clicking on save")	
		self.save.click()
		self.buy_time()
		
	def create_external_captive_portal_2(self):
		conf = self.config.config_vars
		self.wired_captive_portal.set(conf.Wired_Captive_Profile_New)
		logger.debug("Entering the captive Name value. ")
		self.captive_name.set(conf.Captive_Role_Name)
		logger.debug("Setting captive portal type. ")
		self.captive_type.set(conf.Captive_Role_Text)
		self.set_captive_ip(conf.captive_portal_ip)
		self.set_captive_url(conf.captive_portal_url)
		self.set_captive_port(conf.external_captive_port)
		self.set_secuirty_auto_url_whitelisting('check')
		self.captive_auth_text.set(conf.external_captive_auth_text)
		self.save_captive_profile_button()		
		
	def set_captive_portal_failure(self,value):
		'''
		sets captive portal failure 
		'''
		logger.debug("SecurityPage : Setting portal failure") 
		self.Security_CaptivePortalFailure.set(value)
		
	def set_redirect_url(self,url):
		'''
		sets captive portal failure 
		'''
		logger.debug("SecurityPage : Clicking on save") 
		self.Secuirty_redirect_url.set(url)
			
	def assert_splas_page_visuals_fields(self):
		'''
		Asserts Logo upload, Delete and logo Image button
		'''
		logger.debug('SecurityPage : checking Image is uplloaded or not...')
		self.browser.assert_element(self.no_logo_image, "Image is uploaded in Splash Page visuals ")	
		logger.debug('SecurityPage : checking logo upload button is enable or not...')
		self.browser.assert_element(self.logo_upload, "logo upload button is not Enabled")
		logger.debug('SecurityPage : checking Delete button is Disabled or not...')		
		self.browser.assert_element(self.logo_disabled_delete_button, "Delete button is not disabled")

	# def create_external_captive_portal(self,flag):
		# logger.debug("SecurityPage : Selecting external.")
		# self.splash_page_type.set(self.config.config_vars.Splash_page_external)
		# logger.debug("Entering the captive portal value. ")
		# self.wired_captive_portal.set(self.config.config_vars.Wired_Captive_Profile_New)
		# time.sleep(9)
		# logger.debug("Entering the captive Type value. ")
		# self.captive_type.set(self.config.config_vars.Captive_Role_Radius_Authentication)
		# time.sleep(20)
		# raw_input('waste')
		# logger.debug("Entering the captive Name value. ")
		# self.captive_name.set(self.config.config_vars.Captive_Role_Name)      
		# logger.debug("Entering the captive Ip value. ") 
		# self.captive_ip.set(self.config.config_vars.Captive_Role_Ip)
		# logger.debug("Entering the captive Url . ")
		# self.captive_url.set(self.config.config_vars.domain_name)   
		# logger.debug("Entering the captive Port value. ")
		# self.captive_port.set(self.config.config_vars.Captive_Role_Port)
		# if flag == 'check' :
		# raw_input('out')
		# if not self.CaptiveUseHttps.is_selected():
		# logger.debug("Enabling Use Https checkbox. ")
		# self.CaptiveUseHttps.click()
		# elif flag == 'uncheck': 
		# if self.CaptiveUseHttps.is_selected():
		# logger.debug("Disabling Use Https checkbox. ")
		# self.CaptiveUseHttps.click()
		# logger.debug("SecurityPage : Clicking on Save") 
		# self.save.click()
		# self.buy_time()


	def assert_captive_external_splash_page_type_fields(self):
		'''
		mac_authentication : Disabled
		authentication_server : InternalServer
		blacklisting : Disabled
		blacklist_whitelist : 0 blacklist 0 whitelist
		Wispr : Disabled
		'''
		conf = self.config.config_vars
		self.browser.assert_drop_down_value(self.mac_authentication, conf.disable_option, "Mac Authentication not set to default value")
		self.browser.assert_drop_down_value(self.authentication_server, conf.internal_server, "authentication server1 not set to default value")
		self.browser.assert_drop_down_value(self.wireless_encryption, conf.disable_option, "encryption  not set to default value")
		self.browser.assert_drop_down_value(self.blacklisting, conf.disable_option, "blacklisting not set to default value")
		self.browser.assert_element(self.blacklist_whitelist, "blacklisting not set to default value")
		self.browser.assert_drop_down_value(self.wispr,conf.disable_option,'Wispr is not set to Disabled')

	def set_delimiter_characrter(self,value):
		logger.debug("SecurityPage : Set delimiter")
		self.personal_delimeter.set(value)
		
	def assert_upload_logo_button(self):
		logger.debug("Asserting upload button ")
		if not self.disable_upload_button:
			raise AssertionError("Upload button for upload logo is enable")
	
	def configure_wpa_personal_two_external_server(self):
		conf = self.config.config_vars
		self.configure_splash_page_type(self.config.config_vars.Splash_page_Authenticated)
		self.set_mac_authentication_value('Enabled')
		self.set_delimiter()
		self.set_uppercase_support_dropdown()
		
		self.create_external_radius_server_in_auth_server_one()
		self.create_external_radius_server_in_auth_server_two()
		
		self.set_reauth_interval_options(self.config.config_vars.reauth_interval_1440)
		self.configure_auth_server_settings(accounting_enable=True,balancing=True)
		self.set_accounting_mode('Authentication')
		self.accounting_interval.set(self.config.config_vars.valid_accounting)
		
		self.configure_blacklisting('Enable',self.config.config_vars.max_authentication_2)
		
		self.set_encryption("Enabled")
		self.set_security_key_management("WPA Personal")
		self.set_pass_phrase_format('64 hexadecimal chars')
		self.set_passphrase_retype(conf.hexadecimal_64_char,conf.hexadecimal_64_char)
		
		logger.debug('SecurityPage: calling  edit_save_splash_page_details method')
		self.edit_save_splash_page_details()
		
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
		self.auth_server_name.set(value)

	def set_auth_server_ip_address(self,value=''):
		'''
		Sets auth server IP address.
		'''
		logger.debug("SecurityPage : Writing Server ip address")
		self.auth_ipaddr.set(value)
		
	def set_auth_shared_key_retype(self,shared_key='',retype=''):
		'''
		Sets auth server Auth shared key and retype value.
		'''
		logger.debug('SecurityPage : Writing auth Sharedkey value')
		self.Auth_Sharedkey.set(shared_key)
		logger.debug("SecurityPage : Write retype - Shared key.")
		self.Retype_auth_shared_key.set(retype)

	def set_auth_server_accounting_port(self,value='1813'):
		'''
		Sets auth server accounting count.
		'''
		logger.debug("SecurityPage : Write  Accounting Port value.")
		self.Auth_Account_Port.set(value)

	def set_auth_server_dead_time(self,value='5'):
		'''
		Sets auth server Dead Time.
		'''
		logger.debug("SecurityPage : Write  Dead Time value.")
		self.Auth_Account_Port.set(value)
		
	def set_auth_server_time_out(self,value='5'):
		'''
		Sets authentication server time out.
		'''
		logger.debug("SecurityPage : Write  Time out value.")
		self.auth_timeout.set(value)
		
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
		self.AuthPort.set(value)

	def assert_auth_server_name_error(self):
		'''
		Asserts authentication server name error message.
		'''
		logger.debug("SecurityPage : Checking for Auth server name error.")
		if not self.name_error:
			raise AssertionError("SecurityPage : Server name error. i.e. Traceback: %s" %traceback.format_exc())

	def assert_auth_server_ip_address_error(self):
		'''
		Asserts authentication server IP address error message.
		'''
		logger.debug("SecurityPage : Checking for Auth server IP address error.")
		if not self.ip_error:
			raise AssertionError("SecurityPage : Invalid IP. i.e. Traceback: %s" %traceback.format_exc())

	def assert_auth_server_shared_key_error(self,value=True):
		'''
		Asserts authentication server shared key length error message.
		'''
		if value:
			logger.debug("SecurityPage : Checking for Auth server shared key space error.")
			if not self.auth_shared_key_space_error:
				raise AssertionError("SecurityPage : Auth server shared key space error message not found. i.e. Traceback: %s" %traceback.format_exc())
		else:
			logger.debug("SecurityPage : Checking for Auth server shared key length error.")
			if not self.shared_key_error:
				raise AssertionError("SecurityPage : Auth server shared key length error message not found. i.e. Traceback: %s" %traceback.format_exc())

	def assert_auth_server_accounting_port_error(self):
		'''
		Asserts authentication server Accounting port error message.
		'''
		logger.debug("SecurityPage : Checking for Auth server Accounting port error.")
		if not self.Auth_Account_Port_error:
			raise AssertionError("SecurityPage : Auth server Accounting port error message not found. i.e. Traceback: %s" %traceback.format_exc())

	def assert_auth_server_deadtime_error(self):
		'''
		Asserts authentication server Deadtime error message.
		'''
		logger.debug("SecurityPage : Checking for Auth server Dead Time error.")
		if not self.deadtime_error:
			raise AssertionError("SecurityPage : 'Must be a number in range 1-1440' error msg not present. i.e. Traceback: %s" %traceback.format_exc())

	def assert_auth_server_time_out_error(self):
		'''
		Asserts authentication server Time out error message.
		'''
		logger.debug("SecurityPage : Checking for Auth server Timeout error.")
		if not self.auth_timeout_error:
			raise AssertionError("SecurityPage : 'Must be a number in range 1-30' error msg not present. i.e. Traceback: %s" %traceback.format_exc())

	def assert_auth_server_retry_count_error(self):
		'''
		Asserts authentication server Retry count error message.
		'''
		logger.debug("SecurityPage : Checking for Auth server Retry count error.")
		if not self.Auth_Retry_Count_error:
			raise AssertionError("SecurityPage : 'Must be a number in range 1-5' error msg not present. i.e. Traceback: %s" %traceback.format_exc())

	def assert_auth_server_auth_port_error(self):
		'''
		Asserts authentication server Auth port error message.
		'''
		logger.debug("SecurityPage : Checking for Auth server Auth port error.")
		if not self.AuthPort_error:
			raise AssertionError("SecurityPage : 'Must be a number in range 1-65534' error msg not present. i.e. Traceback: %s" %traceback.format_exc())
			
	def assert_retry_count_default_value(self):
		'''
		asserts default value of retry count
		'''
		conf = self.config.config_vars
		logger.debug('SecurityPage : Auth Server : Checking retry count default value')
		self.browser.assert_text(self.retry_count,conf.max_auth_failure_valid_num,'Retry Count is not set to 5','value')

	def assert_auth_rfc_default(self):
		'''
		Asserts auth rfc checkbox
		'''
		logger.debug('SecurityPage : Auth server : checking is rfc checkbox selected')
		self.browser.assert_check_box_value(conf.auth_rfc,'Auth rfc is selected by default',check = True)
		
	def assert_authentication_server1_error(self):
		'''
		Asserts Authentication server1 '* This field is mandatory' error message
		'''
		if not self.auth_server1_error_required:
			raise AssertionError("'* This field is mandatory' error not found. i.e. Traceback: %s" %traceback.format_exc())
			
	def click_save_server(self):
		'''
		Clicks on 'SAVE' button.
		'''			
		logger.debug('SecurityPage : Clicking on Save Server button.')
		self.save_server.click()
		self.buy_time()
		
	def set_drp_vlan_value(self,value):
		logger.debug('SecurityPage: Writing drpvlan')
		time.sleep(3)
		if not self.drpvlan_disabled:
			self.drpvlan.set(value)
			self.buy_time()
		
	def assert_authentication_server_1_and_2_dropdown_values(self,server,name=None):
		'''
		Asserts athentication server 1 and 2 values.
		'''
		if server == '1':
			if self.authentication_server.get_selected() == name:
				raise AssertionError("Athentication server 1 is set to 'New' %s" %traceback.format_exc())
		elif server == '2':
		    if self.authentication_server_2.get_selected() == name:
				raise AssertionError("Athentication server 2 is set to 'New' %s" %traceback.format_exc())
		
	def click_on_preview_splash_page(self):
		'''
		Clicks on Preview Splash Page
		'''
		logger.debug("SecurityPage: clicking on preview splash page")
		self.preview_splash_page.click()
		self.buy_time()
	
	def click_on_delete_logo(self):
		'''
		Clicks on Delete button
		'''
		logger.debug("SecurityPage: clicking on Delete button")
		self.delete_logo.click()
		self.buy_time()
		
	def assert_splash_banner_logo(self):
		'''
		Asserts splash Banner logo is not present
		'''
		logger.debug("SecurityPage: Checking splash Banner logo is not present or not")
		self.browser.assert_element(self.splash_banner_logo,'splash banner logo is Present', False)	
	
	def assert_splash_logo_preview_change_delete_options(self):
		'''
		Asserts logo preview image, Change and Delete options
		'''	
		logger.debug('SecurityPage : Asserting logo preview image')
		self.browser.assert_element(self.logo_preview,'Logo preview image is not displayed')
		logger.debug('SecurityPage : Asserting logo change button')
		self.browser.assert_element(self.change_logo,'Logo change button is not displayed')
		logger.debug('SecurityPage : Asserting logo delete button')
		self.browser.assert_element(self.delete_logo,'Logo delete button is not displayed')
		
	def click_on_preview_splash_page_close(self):
		'''
		clicks on Preview Splash Page Close button
		'''
		logger.debug("SecurityPage: clicking on preview splash page close button")
		self.preview_splash_page_close.click()
		self.buy_time()
		
	def check_captive_portal_logo_text_availablility(self):
		time.sleep(10)
		actions = self.browser.get_action_chain()
		actions.move_to_element(self.logo_preview_msg).perform()
		time.sleep(8)
		if not self.logo_text_msg:
			raise AssertionError(" text message is not visible for captive portal logo i.e. Traceback: %s" %traceback.format_exc())
		time.sleep(5)
		
	def setting_wpa_personal_internal_server(self,format=None):
		conf = self.config.config_vars
		logger.debug("SecurityPage : Selecting value from splash page type  drop-down.")
		self.configure_splash_page_type(conf.Splash_page_Authenticated)
		logger.debug("SecurityPage : Enable mac authentication.")
		self.enable_mac_authentication1()
		logger.debug('SecurityPage : Enabling uppercase support')
		self.set_uppercase_support_dropdown()
		logger.debug("SecurityPage : Set delimiter to  :")
		self.set_delimiter()
		logger.debug("SecurityPage : Setting Blacklisting and max_auth_failure")
		self.configure_blacklisting('Enable',conf.new_reauth_value)
		logger.debug("SecurityPage : Enable Wireless Encryption.")
		self.set_encryption('Enabled')
		logger.debug('SecurityPage : Setting Key Management to  WPA Personal')
		self.set_security_key_management('WPA Personal')
		if format == '8-63':
			logger.debug("SecurityPage : Setting 'PASSPHRASE FORMAT' drop down to '64 Hexadecimal chars'")
			self.wpa_passphrase_format.set(conf.passphrase_frmt_8_63_char)
			logger.debug('SecurityPage: writing passphrase')
			self.passphrase.set('111')
			logger.debug("SecurityPage : Clicking on next")	
			self.next.click()
			if not self.passphrase_length_error_msg:
				raise AssertionError("Passphrase length error message has not been shown .Traceback: %s " %traceback.format_exc())
			logger.debug('SecurityPage: writing passphrase')
			self.passphrase.set(self.config.config_vars.wep_key_alpha_valid)
			logger.debug('SecurityPage: re-writing passphrase')
			self.retype_passphrase.set(self.config.config_vars.wep_key_alpha_valid)
			
		if format == '64':
			logger.debug("SecurityPage : Setting 'PASSPHRASE FORMAT' drop down to '64 Hexadecimal chars'")
			self.wpa_passphrase_format.set(conf.passphrase_frmt_64_hex)
			logger.debug('SecurityPage: writing passphrase')
			self.passphrase.set('111')
			logger.debug("SecurityPage : Clicking on next")	
			self.next.click()
			if not self.passphrase_hex_length_err:
				raise AssertionError("'Must be 64 hexadecimal characters' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			logger.debug('SecurityPage: writing passphrase')
			self.passphrase.set(self.config.config_vars.passphrase_hex_alpha_valid)
			logger.debug('SecurityPage: re-writing passphrase')
			self.retype_passphrase.set(self.config.config_vars.passphrase_hex_alpha_valid)
		
	def setting_static_wep_with_password(self,format=None):
		conf = self.config.config_vars
		logger.debug("SecurityPage : Enable Wireless Encryption.")
		self.set_encryption('Enabled')
		logger.debug('SecurityPage : Setting Key Management to Static WEP')
		self.set_security_key_management('Static WEP')
		if format == '128':
			logger.debug("SecurityPage : Setting 'WEP KEY SIZE' drop down to '128-bit'")
			self.wep_key_size.set(conf.wep_key_size_128)
			logger.debug("SecurityPage : Writing valid alphabet in 'WEP KEY' text box")
			self.personal_wep_key.set(conf.wep_key_alpha_invalid)
			logger.debug("SecurityPage : Clicking on next")	
			self.next.click()
			if not self.wep_key_len_error:
				raise AssertionError("Must be 26 characters or more. i.e. Traceback: %s" %traceback.format_exc())
			logger.debug("SecurityPage : Writing Personal Wep key")
			self.personal_wep_key.set(self.config.config_vars.wep_key)
			logger.debug("SecurityPage : re Writing Personal Wep key")
			self.personal_re_wep_key.set(self.config.config_vars.wep_key)
			
		if format == '64':
			logger.debug("SecurityPage : Setting 'WEP KEY SIZE' drop down to '128-bit'")
			self.wep_key_size.set(conf.wep_key_size_64)
			logger.debug("SecurityPage : Writing valid alphabet in 'WEP KEY' text box")
			self.personal_wep_key.set(conf.wep_key_64_alpha_invalid)
			logger.debug("SecurityPage : Clicking on next")	
			self.next.click()
			if not self.wep_key_64_len_error:
				raise AssertionError("'Must be 10 hexadecimal characters' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			logger.debug("SecurityPage : Writing Personal Wep key")
			self.personal_wep_key.set(self.config.config_vars.ten_hexa_decimal_chars)
			logger.debug("SecurityPage : re Writing Personal Wep key")
			self.personal_re_wep_key.set(self.config.config_vars.ten_hexa_decimal_chars)
		
		
	def setting_wpa_2_personal_two_authserver_internal_and_external(self,format=None,authserver=True):
		conf = self.config.config_vars
		time.sleep(25)
		logger.debug("SecurityPage : Selecting value from splash page type  drop-down.")
		self.configure_splash_page_type(conf.Splash_page_Acknowledged)
		logger.debug("SecurityPage : Enable mac authentication.")
		time.sleep(20)
		self.enable_mac_authentication1()
		logger.debug('SecurityPage : Enabling uppercase support')
		self.set_uppercase_support_dropdown()
		logger.debug("SecurityPage : Set delimiter to  :")
		self.set_delimiter()
		time.sleep(5)
		if authserver:
			self.create_external_radius_server_in_auth_server_one()
			self.create_external_radius_server_in_auth_server_two()
		logger.debug("SecurityPage : Setting Blacklisting and max_auth_failure")
		self.configure_blacklisting('Enable',conf.new_reauth_value)
		logger.debug("SecurityPage : Enable Wireless Encryption.")
		self.set_encryption('Enabled')
		logger.debug('SecurityPage : Setting Key Management to  WPA Personal')
		self.set_security_key_management('WPA-2 Personal')
		if format == '8-63':
			logger.debug("SecurityPage : Setting 'PASSPHRASE FORMAT' drop down to '64 Hexadecimal chars'")
			self.wpa_passphrase_format.set(conf.passphrase_frmt_8_63_char)
			logger.debug('SecurityPage: writing passphrase')
			self.passphrase.set('111')
			logger.debug("SecurityPage : Clicking on next")	
			self.next.click()
			if not self.passphrase_length_error_msg:
				raise AssertionError("Passphrase length error message has not been shown .Traceback: %s " %traceback.format_exc())
			logger.debug('SecurityPage: writing passphrase')
			self.passphrase.set(self.config.config_vars.wep_key_alpha_valid)
			logger.debug('SecurityPage: re-writing passphrase')
			self.retype_passphrase.set(self.config.config_vars.wep_key_alpha_valid)
			
		if format == '64':
			logger.debug("SecurityPage : Setting 'PASSPHRASE FORMAT' drop down to '64 Hexadecimal chars'")
			self.wpa_passphrase_format.set(conf.passphrase_frmt_64_hex)
			logger.debug('SecurityPage: writing passphrase')
			self.passphrase.set('111')
			logger.debug("SecurityPage : Clicking on next")	
			self.next.click()
			if not self.passphrase_hex_length_err:
				raise AssertionError("'Must be 64 hexadecimal characters' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			logger.debug('SecurityPage: writing passphrase')
			self.passphrase.set(self.config.config_vars.passphrase_hex_alpha_valid)
			logger.debug('SecurityPage: re-writing passphrase')
			self.retype_passphrase.set(self.config.config_vars.passphrase_hex_alpha_valid)
	
	def enable_fast_roaming_option(self, roaming):
		'''
		Enable 802.11r, 802.11k, 802.11v
		'''
		if roaming == '802.11r':
			if not self.roaming_open.is_selected():
				logger.debug('SecurityPage : Clicking on Roaming open 802.11r button')
				self.roaming_open.click()
		if roaming == '802.11v':	
			if not self.roaming_open_v.is_selected():
				logger.debug('SecurityPage : Clicking on Roaming open 802.11v button')
				self.roaming_open_v.click()
		if roaming == '802.11k':	
			if not self.roaming_open_k.is_selected():
				logger.debug('SecurityPage : Clicking on Roaming open 802.11k button')
				self.roaming_open_k.click()
				
	def create_authentication_server(self,name=None, ip=None, sharedkey=None,retypekey=None,rfc=False,actport=None,time=None,timeout=None,retrycount= None,authport = None,mask = None,dip = None,gateway = None,vlan = None,nas_ip=None,nas_identifier_value=None,coa_port=None):
		'''
		creates authentication server
		'''
		if name:
			logger.debug('SecurityPage: Writing server name')
			self.auth_server_name.set(name)
		if ip: 
			logger.debug('SecurityPage: Writing ip')
			self.auth_ipaddr.set(ip)
		if sharedkey:
			logger.debug('SecurityPage: Writing SharedKey')
			self.Auth_Sharedkey.set(sharedkey)
		if retypekey: 
			logger.debug('SecurityPage: Writing Retype SharedKey')
			self.Retype_auth_shared_key.set(retypekey)
		if rfc :
			logger.debug('SecurityPage: Selecting rfc checkbox')
			self.auth_rfc.click()
		if actport:	
			logger.debug('SecurityPage: Writing actport')
			self.Auth_Account_Port.set(actport)
		if time:	
			logger.debug('SecurityPage: Writing deadtime')
			self.deadtime.set(time)
		if timeout:	
			logger.debug('SecurityPage: Writing timeout')
			self.auth_timeout.set(timeout)
		if retrycount:	
			logger.debug('SecurityPage: Writing retry count')
			self.retry_count.set(retrycount)
		if authport:	
			logger.debug('SecurityPage: Writing authport')
			self.AuthPort.set(authport)
		self.page_down()	
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
			self.nas_ip.set(nas_ip)
		if nas_identifier_value:
			logger.debug('SecurityPage : Setting NAS Identifier. ')
			self.nas_identifier.set(nas_identifier_value)
		logger.debug('SecurityPage:External Auth Server : Clicking on save button')	
		self.save_server.click()
		if self.drpvlan_error:
			self.drpvlan.set(self.config.config_vars.reauth_2)
			self.save_server.click()	
		
	def set_captive_portal_failure1(self, allow = True):
		'''
		sets captive portal failure
		'''
		if allow:
			logger.debug('SecurityPage: Selecting Allow option as Captive portal failure')
			self.external_captive_portal_failure.set(self.config.config_vars.allow_internet)
		else :
			logger.debug('SecurityPage: Selecting Deny option as Captive portal failure')
			self.external_captive_portal_failure.set(self.config.config_vars.deny_internet)
	
	def set_automatic_url_whitelisting(self, url = True):
		'''
		sets automatic url whitelisting
		'''
		if url:
			logger.debug('SecurityPage: Selecting automatic url whitelisting as Enable')
			self.external_automatic_url_whitelisting.set(self.config.config_vars.wispr_enable)
		else :
			logger.debug('SecurityPage: Selecting automatic url whitelisting as disable')
			self.external_automatic_url_whitelisting.set(self.config.config_vars.termination_disabled)	
				
	def assert_splash_page_visuals_disabled(self):
		'''
		Asserts Upload, Delete,  no logo image label, preview splash page 
		'''
		logger.debug('SecurityPage: checking Upload button is Disabled or not...')
		self.browser.assert_element(self.disable_upload_button, 'Upload button is not Disabled')
		logger.debug('SecurityPage : checking Delete button is Disabled or not...')		
		self.browser.assert_element(self.logo_disabled_delete_button, "Delete button is not disabled")
		logger.debug('SecurityPage : checking no logo image label is present or not...')
		self.browser.assert_element(self.no_logo_image, "logo image label is not present")	
		logger.debug('SecurityPage : checking preview splash page is present or not ...')
		self.browser.assert_element(self.preview_splash_page, "checking preview splash page is not present ")
		
	def page_down(self):
		'''
		scroll down the page
		'''
		self.browser.key_press(u'\ue009')
		self.browser.key_press( u'\ue00f')
		
	def page_up(self):
		'''
		scroll up the page
		'''
		self.browser.key_press(u'\ue009')
		self.browser.key_press(u'\ue00e')