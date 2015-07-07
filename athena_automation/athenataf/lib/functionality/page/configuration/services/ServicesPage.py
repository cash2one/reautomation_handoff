from athenataf.lib.util.WebPage import WebPage
import logging
from athenataf.lib.test.TestCase import TestCase
import traceback
logger = logging.getLogger('athenataf')
import time 
class ServicesPage(WebPage):
	def __init__(self, test, browser, config):
		WebPage.__init__(self, "Services", test, browser, config)
		self.test.assertPageLoaded(self)

	def isPageLoaded(self):
		self.browser._browser.implicitly_wait(120)
		self.browser._browser.set_page_load_timeout(120)
		if self.enable_air_group_text:
			return True    
		else:
			return False

	def airgroup_options(self):
		logger.debug("ServicesPage : Clicks on Enable Air group button ")
		self.enable_air_group.click()
		logger.debug("ServicesPage : Enabling Bonjour Multicast ")
		self.guest_bonjour.click()
		logger.debug("ServicesPage : Clicks on save button ")
		self.save_setting.click()
		self.buy_time()
		logger.debug("ServicesPage : Calling  restore_defaults method")
		self.restore_defaults()

	def assert_airgroup_checkbox(self):
		check_box=0
		if self.enable_air_group:
			check_box=check_box+1
		if self.guest_bonjour:
			check_box=check_box+1
		if check_box>2:
			raise AssertionError(" Default checkbox greater than two .Traceback: %s " %traceback.format_exc())
		elif check_box<2:
			raise AssertionError(" Default checkbox less than two .Traceback: %s " %traceback.format_exc())
			
	def assert_airgroup_checkbox_disabled(self):
		self.buy_time()
		if self.enable_air_group.is_selected():
			# self.enable_air_group.click()
			raise AssertionError(" Enable air group checkbox is enabled by default .Traceback: %s " %traceback.format_exc())
		elif self.guest_bonjour.is_selected():
			# self.guest_bonjour.click()
			raise AssertionError(" Enable guest bonjour checkbox is enabled by default .Traceback: %s " %traceback.format_exc())

	def assert_rtls_aeroscout_checkbox(self):
		logger.debug("ServicesPage : Click rtls accordion ")
		self.rtls_menu.click()
		if self.aruba_rtls.is_selected():
			raise AssertionError(" Aruba rtls checkbox enabled by default .Traceback: %s " %traceback.format_exc())
		elif self.location_engine.is_selected():
			raise AssertionError(" Analytics & location engine checkbox is enabled by default .Traceback: %s " %traceback.format_exc())
		elif self.aero_scout.is_selected():
			raise AssertionError(" Aeroscout checkbox is enabled by default .Traceback: %s " %traceback.format_exc())
	
	def enable_rtls(self):
		logger.debug("ServicesPage : Click rtls accordion ")
		self.rtls_menu.click()
		if not self.rtls_ip_address:
			logger.debug("Services: Clicking on Aruba RTLS checkbox")
			self.aruba_rtls.click()
		logger.debug("Services: Entering Rtls ip address")
		self.rtls_ip_address.set(self.config.config_vars.Ip_Address)
		logger.debug("Services: Entering Rtls port")
		self.rtls_port.set(self.config.config_vars.Port)
		logger.debug("Services: Entering Rtls passphrase")
		self.rtls_passphrase.set(self.config.config_vars.Network_Passphrase)
		logger.debug("Services: Entering Rtls retype passphrase")	
		self.rtls_re_passphrase.set(self.config.config_vars.Network_Passphrase)
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()

	def save_settings(self):
		self.buy_time()
		logger.debug("ServicesPage : Clicks on save button ")
		self.save_setting.click()
		self.buy_time()

	def buy_time(self):
		time.sleep(12)

	def enable_aero_scout(self):
		logger.debug("ServicesPage : Click rtls accordion ")
		self.rtls_menu.click()
		if not self.scout_ip_address:
			logger.debug("ServicesPage : Clicking on aero scout. ")
			self.aero_scout.click()
		logger.debug("Services: Entering aeroscout ip  address ")
		self.scout_ip_address.set(self.config.config_vars.Ip_Address)
		logger.debug("Services: Entering aeroscout port ")
		self.scout_port.set(self.config.config_vars.Port)
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()

	def enable_airgroup_clearpass(self):
		if not self.cppm_server_select:
			self.enable_air_group.click()
		if not self.cppm_server_select.selected == self.config.config_vars.Cppm_server:
			raise AssertionError(" Cppm server1 is not set to default.Traceback: %s " %traceback.format_exc())
		if self.enable_clear_pass.is_selected():
			raise AssertionError(" Enable clear pass is not enabled.Traceback: %s " %traceback.format_exc())

	def enable_airgroup(self):
		if not self.itunes:
			logger.debug("Service: Clicking on AirGroup checkbox")
			self.enable_air_group.click()
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()

	def restore_defaults(self):
		if self.enable_air_group.is_selected():
			logger.debug("Service: Clicking on AirGroup checkbox")
			self.enable_air_group.click()
		if self.guest_bonjour.is_selected():
			logger.debug("ServicesPage : Enabling Bonjour Multicast ")
			self.guest_bonjour.click()
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()

	def assert_custom_role(self):
		time.sleep(10)
		if not self.enable_air_group.is_selected():
			logger.debug("Service: Clicking on AirGroup checkbox")
			self.enable_air_group.click()
		if not self.enable_air_print.is_selected():
			logger.debug('ServicesPage : Enabling air print')
			self.enable_air_print.click()
			time.sleep(6)
		logger.debug("Service: Clicks on Airprint editrole ")
		self.airprint_editrole.click()
		if not self.close_Roles_popUp:
			logger.debug("Service: Clicks on Airprint editrole ")
			self.airprint_editrole.click()
		if not self.new_role:
			raise AssertionError("New role setup failed i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		logger.debug("Service: Clicks on Roles popup close button ")
		self.close_Roles_popUp.click()
		logger.debug('ServicesPage : Enabling air print')
		self.enable_air_print.click()
		logger.debug("Service: Clicking on AirGroup checkbox")
		self.enable_air_group.click()
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
			
	def enable_analytics_location_engine(self):
		logger.debug("ServicesPage : calling rtls_click method ")
		self.rtls_click()
		# self.rtls_menu.click()
		if not self.location_engine:
			logger.debug("ServicesPage : calling rtls_click method ")
			self.rtls_click()
		if not self.location_engine.is_selected():
			logger.debug("ServicesPage : Enable location engine checkbox .")
			self.location_engine.click()
		logger.debug("ServicesPage : Set service server. ")
		self.service_server.set(self.config.config_vars.service_server)
		logger.debug("ServicesPage : Set report interval.")        
		self.report_interval_location.set(self.config.config_vars.report_interval_location)
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()

	def restore_location_engine_defaults(self):
		if self.location_engine.is_selected():
			logger.debug("ServicesPage : Disable location engine checkbox .")
			self.location_engine.click()
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()        


	def open_dns_credentials(self):
		self.open_dns_accordion.click()
		logger.debug("ServicesPage : Set Dns Username. ")
		self.dns_username.set(self.config.config_vars.User_Name)
		logger.debug("ServicesPage : Set Dns password.")
		self.dns_password.set(self.config.config_vars.dns_password)
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()

	def clear_dns_credenrials(self):
		logger.debug("ServicesPage : Set  Dns Username null. ")
		self.dns_username.set('')
		logger.debug("ServicesPage : Set Dns password null.")
		self.dns_password.set('')
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()

	def conifgure_calea_settings(self):
		self.calea_accordion.click()
		logger.debug("ServicesPage : Set Calea ip address. ")
		self.calea_ip_address.set(self.config.config_vars.calea_ip_address)
		logger.debug("ServicesPage : Set Encapsulation type.")
		self.calea_encapsulation_type.set(self.config.config_vars.calea_encapsulation_type)
		logger.debug("ServicesPage : Set Calea gre type. ")
		self.calea_gre_type.set(self.config.config_vars.calea_gre_type)
		logger.debug("ServicesPage : Set Calea mtu. ")
		self.calea_mtu.set(self.config.config_vars.calea_mtu)                
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()

	def clear_calea_settings(self):
		logger.debug("ServicesPage : Set Calea ip address null. ")
		self.calea_ip_address.set('')
		logger.debug("ServicesPage : Set Encapsulation type null.")
		self.calea_encapsulation_type.set(self.config.config_vars.calea_encapsulation_type)
		logger.debug("ServicesPage : Set Calea gre type null. ")
		self.calea_gre_type.set('')
		logger.debug("ServicesPage : Set Calea mtu null. ")
		self.calea_mtu.set('')                
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()

	def assert_calea_support_settings(self):
		self.calea_accordion.click()
		logger.debug("ServicesPage : Set invalid ip address. ")
		self.calea_ip_address.set(self.config.config_vars.calea_invalid_ip_address)
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
		if not self.ip_addess_error:
			raise AssertionError(" Invalid ip address accepted .Traceback: %s " %traceback.format_exc())
		logger.debug("ServicesPage : asserting options of 'Encapsulation type' drop-down")
		options = self.calea_encapsulation_type.options
		if not 'GRE' in options:
			raise AssertionError(" Encapsulation type has more than one option: GRE  .Traceback: %s " %traceback.format_exc())     
		logger.debug("ServicesPage : Set MTU > 1500. ")
		self.calea_mtu.set(self.config.config_vars.calea_invalid_mtu)
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
		if not self.calea_mtu_error:
			raise AssertionError(" Mtu range greater than 1500  .Traceback: %s " %traceback.format_exc())
		self.calea_cancel_button.click()

	def edit_calea_configuration(self):
		self.calea_accordion.click()                                 
		logger.debug("ServicesPage : Set ip address. ")
		self.calea_ip_address.set(self.config.config_vars.Ip_Address1)
		logger.debug("ServicesPage : Set encapsulation type to GRE. ")
		self.calea_encapsulation_type.set(self.config.config_vars.calea_encapsulation_type)
		logger.debug("ServicesPage : Set mtu .  ")                
		self.calea_mtu.set(self.config.config_vars.calea_mtu)        
		logger.debug("ServicesPage : Set Gre type .  ")                
		self.calea_gre_type.set(self.config.config_vars.calea_gre_type1)        
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()

	def reset_calea_fields(self):
		logger.debug("ServicesPage : Set ip address none . ")
		self.calea_ip_address.set('')
		logger.debug("ServicesPage : Set encapsulation type to GRE  . ")
		self.calea_encapsulation_type.set(self.config.config_vars.calea_encapsulation_type)
		logger.debug("ServicesPage : Set mtu to default.  ")                
		self.calea_mtu.set(self.config.config_vars.calea_mtu_default)        
		logger.debug("ServicesPage : Set Gre type .  ")                
		self.calea_gre_type.set('')        
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()                 

	def assert_rtls_analytics_location_engine(self):
		logger.debug("ServicesPage : Click rtls accordion ")
		self.rtls_menu.click()
		if not self.location_engine.is_selected():
			logger.debug("ServicesPage : click location engine checkbox. ")
			self.location_engine.click()
		logger.debug("ServicesPage : Check for the server textbox . ")
		if not self.service_server:
			raise AssertionError(" Service server textbox not visible.Traceback: %s " %traceback.format_exc())
		logger.debug("ServicesPage : Check for the report interval location textbox . ")
		if not self.report_interval_location:
			raise AssertionError(" Report interval location not visible.Traceback: %s " %traceback.format_exc())
		logger.debug("ServicesPage : clicks on calea cancel button. ")
		self.calea_cancel_button.click()
		self.buy_time()

	def disable_analytics_location_engine(self):
		logger.debug("ServicesPage : Click rtls accordion ")
		self.rtls_menu.click()
		if self.location_engine.is_selected():
			logger.debug("ServicesPage : click location engine checkbox. ")
			self.location_engine.click()
			logger.debug("ServicesPage : calling save_settings method ")
			self.save_settings() 

	def restore_aero_scout_defaults(self):
		if self.aero_scout.is_selected():
			logger.debug("ServicesPage : Clicking on aero scout. ")
			self.aero_scout.click()
			logger.debug("ServicesPage : Clicking on save button ")
			self.save_settings()

	def restore_rtls_default(self):
		logger.debug("ServicesPage : Clicking on aruba rtls. ")
		self.aruba_rtls.click()
		logger.debug("ServicesPage : Clicking on save button ")
		self.save_settings()

	def rtls_click(self):
		self.buy_time()
		logger.debug("ServicesPage : Clicking on rtls menu ")
		self.rtls_menu.click()

	def assert_air_group_settings(self):
		if self.enable_air_mobile_chk.is_selected():
			raise AssertionError("ENABLE AirGroup ACROSS MOBILITY DOMAINS is checked.Traceback: %s " %traceback.format_exc())
		if self.enable_air_print.is_selected():
			raise AssertionError("ENABLE AIR PRINT is checked.Traceback: %s " %traceback.format_exc())
		if self.enable_air_play.is_selected():
			raise AssertionError("ENABLE AIR PLAY is checked.Traceback: %s " %traceback.format_exc())
		if self.itunes.is_selected():
			raise AssertionError("ITUNES is checked.Traceback: %s " %traceback.format_exc())
		if self.enable_remote_mgemt.is_selected():
			raise AssertionError("ENABLE REMOTE MANAGEMENT is checked.Traceback: %s " %traceback.format_exc())
		if self.enable_sharing.is_selected():
			raise AssertionError("SHARING is checked.Traceback: %s " %traceback.format_exc())
		if self.enable_chat.is_selected():
			raise AssertionError("CHAT is checked.Traceback: %s " %traceback.format_exc())
		if self.enable_allowall.is_selected():
			raise AssertionError("ALLOWALL is checked.Traceback: %s " %traceback.format_exc())

	def click_all_air_group_options(self):
		logger.debug('ServicesPage : Enabling air mobile check')
		self.enable_air_mobile_chk.click()
		logger.debug('ServicesPage : Enabling air print')
		self.enable_air_print.click()
		if not self.edit_air_print_disallowed_roles:
			raise AssertionError("Edit Air Print Disallowed Roles not visible.Traceback: %s " %traceback.format_exc())
		if not self.edit_air_print_disallowed_vlans:
			raise AssertionError("Edit Air Print Disallowed vlans not visible.Traceback: %s " %traceback.format_exc())
		logger.debug('ServicesPage : Enabling air play')
		self.enable_air_play.click()
		if not self.edit_air_play_disallowed_roles:
			raise AssertionError("Edit Air Play Disallowed Roles not visible.Traceback: %s " %traceback.format_exc())
		if not self.edit_air_play_disallowed_vlans:
			raise AssertionError("Edit Air Play Disallowed vlans not visible.Traceback: %s " %traceback.format_exc())
		logger.debug('ServicesPage : Enabling air itunes')
		self.itunes.click()
		if not self.itunes_disallowed_roles:
			raise AssertionError("Edit itunes Disallowed Roles not visible.Traceback: %s " %traceback.format_exc())
		if not self.itunes_disallowed_vlans:
			raise AssertionError("Edit itunes Disallowed vlans not visible.Traceback: %s " %traceback.format_exc())
		logger.debug('ServicesPage : Enabling remote management')
		self.enable_remote_mgemt.click()
		if not self.remote_management_disallowed_roles:
			raise AssertionError("Edit Remote Management Disallowed Roles not visible.Traceback: %s " %traceback.format_exc())
		if not self.remote_management_disallowed_vlans:
			raise AssertionError("Edit Remote Management Disallowed vlans not visible.Traceback: %s " %traceback.format_exc())
		self.enable_sharing.click()
		if not self.sharing_disallowed_roles:
			raise AssertionError("Edit Sharing Disallowed Roles not visible.Traceback: %s " %traceback.format_exc())
		if not self.sharing_disallowed_vlans:
			raise AssertionError("Edit Sharing Disallowed vlans not visible.Traceback: %s " %traceback.format_exc())
		self.enable_chat.click()
		if not self.chat_disallowed_roles:
			raise AssertionError("Edit Chat Disallowed Roles not visible.Traceback: %s " %traceback.format_exc())
		if not self.chat_disallowed_vlans:
			raise AssertionError("Edit Chat Disallowed vlans not visible.Traceback: %s " %traceback.format_exc())
		self.enable_allowall.click()
		if not self.allowall_disallowed_roles:
			raise AssertionError("Edit allowall Disallowed Roles not visible.Traceback: %s " %traceback.format_exc())
		if not self.allowall_disallowed_vlans:
			raise AssertionError("Edit Allowall Disallowed vlans not visible.Traceback: %s " %traceback.format_exc())
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()

	def air_group_restore_defaults(self):
		logger.debug('ServicesPage : Enabling air mobile check')
		self.enable_air_mobile_chk.click()
		logger.debug('ServicesPage : Enabling air print')
		self.enable_air_print.click()
		logger.debug('ServicesPage : Enabling air play')
		self.enable_air_play.click()
		logger.debug('ServicesPage : Enabling air itunes')
		self.itunes.click()
		logger.debug('ServicesPage : Enabling remote management')
		self.enable_remote_mgemt.click()
		logger.debug('ServicesPage : Enabling sharing')
		self.enable_sharing.click()
		logger.debug('ServicesPage : Enabling chat')
		self.enable_chat.click()
		logger.debug('ServicesPage : Enabling allowall')
		self.enable_allowall.click()
		logger.debug('ServicesPage : Enabling air group')
		self.enable_air_group.click()
		logger.debug('ServicesPage : Clicking on save button')
		self.save_settings()

	def creat_new_cppm_server(self):
		logger.debug('ServicesPage : Entering authentication server name')
		self.auth_server_name.set(self.config.config_vars.cppm_server_name)
		logger.debug('ServicesPage : Entering ip address')
		self.auth_ipaddr.set(self.config.config_vars.cppm_server_ip)
		logger.debug('ServicesPage : Entering sharedkey')
		self.auth_sharedkey.set(self.config.config_vars.auth_sharedkey_value)
		logger.debug('ServicesPage : Re-entering sharedkey')
		self.retype_auth_shared_key.set(self.config.config_vars.retype_auth_sharedkey_value)
		logger.debug('ServicesPage : Entering airgroup port')
		self.airgroup_port.set(self.config.config_vars.coa_port)
		logger.debug('ServicesPage : Saving settings')
		self.cppm_save_button.click()
		self.buy_time()

	# def assert_new_cppm_server(self):
		# self.cppm_server_select.set(self.config.config_vars.new_cppm_server_name)
		# self.auth_coa_only.click()
		# self.auth_server_name.set(self.config.config_vars.invalid_cppm_server_name)
		# self.auth_ipaddr.set(self.config.config_vars.invalid_cppm_server_ip)
		# self.auth_sharedkey.set(self.config.config_vars.invalid_auth_sharedkey_value)
		# self.retype_auth_shared_key.set(self.config.config_vars.invalid_retype_auth_sharedkey_value)
		# self.airgroup_port.set(self.config.config_vars.invalid_coa_port)
		# self.cppm_save_button.click()	
		# if not self.auth_server_name_error:
			# raise AssertionError("No special characters allowed, only - and _ allowed.Traceback: %s " %traceback.format_exc())
		# if not self.auth_ipaddr_error:
			# raise AssertionError("Invalid IP Address.Traceback: %s " %traceback.format_exc())

		# if not self.auth_Sharedkey_error:
			# raise AssertionError("Length must be 2-64 characters.Traceback: %s " %traceback.format_exc())

		# if not self.retype_auth_shared_key_error:
			# raise AssertionError("Fields do not match.Traceback: %s " %traceback.format_exc())

		# if not self.airgroup_port_error:
			# raise AssertionError("Must be a number in range 1-65534: %s " %traceback.format_exc())

	def assert_cppm_server_feilds(self):
		self.cppm_server_select.set(self.config.config_vars.cppm_server_name)
		if not self.cppm_server2_select.selected == self.config.config_vars.Cppm_server:
			raise AssertionError(" Cppm server2 is not set to default.Traceback: %s " %traceback.format_exc())
		if not self.coa_server_select.selected == self.config.config_vars.Cppm_server:
			raise AssertionError(" CoA server is not set to default.Traceback: %s " %traceback.format_exc())
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
			
	def assert_rtls_enable(self):
		if self.rtls_unassociated_chk.is_selected():
			raise AssertionError("INCLUDE UNASSOCIATED STATIONS is checked.Traceback: %s " %traceback.format_exc())

	def assert_rtls_3rd_party_aeroscout(self):
		if self.scout_unassociated_chk.is_selected():
			raise AssertionError("INCLUDE UNASSOCIATED STATIONS is checked.Traceback: %s " %traceback.format_exc())
			
	def enable_airgroup_enable_air_print_box(self):
		if not self.enable_air_group.is_selected():
			logger.debug('ServicesPage : Enabling enable air group option')
			self.enable_air_group.click()
		if not self.enable_air_print.is_selected():
			logger.debug('ServicesPage : Enabling enable air print option')
			self.enable_air_print.click()
		if not self.edit_air_print_disallowed_roles:
			raise AssertionError("Edit Air Print Disallowed Roles not visible.Traceback: %s " %traceback.format_exc())
		logger.debug('ServicesPage : Editing air print disallowed roles')
		self.edit_air_print_disallowed_roles.click()
		if self.config.config_vars.Role_Name:
			logger.debug('ServicesPage : Saving roles')
			self.save_roles_popup.click()
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()

	def restore_enable_airgroup_enable_air_print_box(self):
		if self.enable_air_print.is_selected():
			logger.debug('ServicesPage : Restoring enable air print option')
			self.enable_air_print.click()
		if self.enable_air_group.is_selected():
			logger.debug('ServicesPage : Restoring enable air group option')
			self.enable_air_group.click()
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()

	def assert_airgroup_role(self):
		time.sleep(10)
		if not self.enable_air_group.is_selected():
			logger.debug('ServicesPage : Click air group.')
			self.enable_air_group.click()
		if not self.enable_air_play.is_selected():
			logger.debug('ServicesPage : Click air print.')
			self.enable_air_play.click()
			time.sleep(6)
		logger.debug('ServicesPage : Click air play disallowed roles.')
		self.airplay_editrole.click()
		if not self.confirm_save_close_roles:
			self.airplay_editrole.click()
		if not self.role1:
			raise AssertionError("Role 1 setup failed i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		if not self.role2:
			raise AssertionError("Role 2 setup failed i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		if not self.role3:
			raise AssertionError("Role 3 setup failed i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		self.confirm_save_close_roles.click()
		logger.debug('ServicesPage : Enabling air print')
		self.enable_air_print.click()
		logger.debug("Service: Clicking on AirGroup checkbox")
		self.enable_air_group.click()
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()

	def assert_new_cppm_server(self):
		self.cppm_server_select.set(self.config.config_vars.new_cppm_server_name)
		self.auth_coa_only.click()
		self.auth_server_name.set(self.config.config_vars.invalid_cppm_server_name)
		self.auth_ipaddr.set(self.config.config_vars.invalid_cppm_server_ip)
		self.auth_sharedkey.set(self.config.config_vars.invalid_auth_sharedkey_value)
		self.retype_auth_shared_key.set(self.config.config_vars.invalid_retype_auth_sharedkey_value)
		self.airgroup_port.set(self.config.config_vars.invalid_coa_port)
		self.cppm_save_button.click()	
		if not self.auth_server_name_error:
			raise AssertionError("No special characters allowed, only - and _ allowed.Traceback: %s " %traceback.format_exc())
		if not self.auth_ipaddr_error:
			raise AssertionError("Invalid IP Address.Traceback: %s " %traceback.format_exc())

		if not self.auth_Sharedkey_error:
			raise AssertionError("Length must be 2-64 characters.Traceback: %s " %traceback.format_exc())

		if not self.retype_auth_shared_key_error:
			raise AssertionError("Fields do not match.Traceback: %s " %traceback.format_exc())

		if not self.airgroup_port_error:
			raise AssertionError("Must be a number in range 1-65534: %s " %traceback.format_exc())

	def assert_calea_configuration_default(self):
		logger.debug("ServicesPage : Clicking on Calea Accordion. ")
		self.calea_accordion.click()
		if self.calea_ip_address:
			logger.debug('ServicesPage :Checking calea ip address feild is Empty.')
			if not self.calea_ip_address.get() == '':
				raise AssertionError("Calea ip address feild is not empty.Traceback: %s " %traceback.format_exc())

		if self.calea_encapsulation_type:
			logger.debug('ServicesPage :Checking whether encapsulation type is set to GRE.')
			if not self.calea_encapsulation_type.get_selected() == self.config.config_vars.calea_encapsulation_type :
				raise AssertionError("encapsulation type is not set to GRE.Traceback: %s " %traceback.format_exc())

		if self.calea_mtu:
			logger.debug('ServicesPage :Checking whether calea mtu is set to 1500.')
			if not self.calea_mtu.get() == self.config.config_vars.calea_mtu_default :
				raise AssertionError("calea mtu is set not to 1500.Traceback: %s " %traceback.format_exc())

		if self.calea_gre_type:
			logger.debug('ServicesPage :Checking whether calea gre type is set to 25944.')
			if not self.calea_gre_type.get() == self.config.config_vars.calea_gre_type :
				raise AssertionError("Checking whether calea gre type is set to 25944.Traceback: %s " %traceback.format_exc())

	def assert_open_dns_feilds(self):
		logger.debug("ServicesPage : Clicking on Open dns Accordion. ")
		self.open_dns_accordion.click()
		if self.dns_username:
			logger.debug('ServicesPage :Checking whether Username feild is Empty.')
			if not self.dns_username.get() == '' :
				raise AssertionError("Username feild is not Empty.Traceback: %s " %traceback.format_exc())
		if self.dns_password:
			logger.debug('ServicesPage :Checking whether password feild is Empty.')
			if not self.dns_password.get() == ''  :
				raise AssertionError("password feild is not Empty.Traceback: %s " %traceback.format_exc())
	

	def assert_rtls_analytics_and_location_engine(self):
		logger.debug("ServicesPage : Click rtls accordion ")
		self.rtls_menu.click()
		if not self.location_engine.is_selected():
			logger.debug("ServicesPage : click location engine checkbox. ")
			self.location_engine.click()
		logger.debug("ServicesPage : Check whether the server textbox is empty. ")
		if self.service_server:
			if not self.service_server.get() == '' :
				raise AssertionError("  Server textbox not empty.Traceback: %s " %traceback.format_exc())

		logger.debug("ServicesPage : Check for the report interval is set to 30 sec . ")
		if self.report_interval_location:
			if not self.report_interval_location.get() == self.config.config_vars.report_interval_location :
				raise AssertionError(" Report interval is not set to 30 sec.Traceback: %s " %traceback.format_exc())

		self.save_setting.click()
		self.buy_time()


	def set_rtls_analytics_location_engine_non_default_values(self):
		logger.debug("ServicesPage : Click rtls accordion ")
		self.rtls_menu.click()
		if not self.location_engine.is_selected():
			logger.debug("ServicesPage : click location engine checkbox. ")
			self.location_engine.click()
			logger.debug("ServicesPage : Setting Invalid IP in Server textbox ")
			self.service_server.set(self.config.config_vars.invalid_value)
			self.save_setting.click()
			if not self.service_server_error:
				raise AssertionError("'Invalid IP Address' error message not found i.e. Traceback: %s" %traceback.format_exc())
			logger.debug("ServicesPage : Setting IP in Server textbox ")
			self.service_server.set(self.config.config_vars.service_server)

			logger.debug("ServicesPage : Setting invalid report interval value . ")
			self.report_interval_location.set(self.config.config_vars.invalid_value)
			self.save_setting.click()
			if not self.report_interval_location_error:
				raise AssertionError("'Must be a number in range 6-60' error message not found. i.e. Traceback: %s" %traceback.format_exc())
			self.report_interval_location.set(self.config.config_vars.report_interval_location_new)
			self.save_setting.click()
			self.buy_time()

	def airgroup_bonjour_enable(self):
		logger.debug("ServicesPage : Enabling Bonjour Multicast ")
		self.guest_bonjour.click()
		self.save_setting.click()
		self.buy_time()

	def restore_bonjour_defaults(self):
		logger.debug("ServicesPage : Disabling Bonjour Multicast ")
		if self.guest_bonjour.is_selected():
			logger.debug("ServicesPage : Enabling Bonjour Multicast ")
			self.guest_bonjour.click()
			logger.debug("ServicesPage : calling save_settings method ")
			self.save_settings()
			self.buy_time()

	def assert_network_integration_default(self):
		logger.debug("ServicesPage : Clicking on Network Integration Accordion. ")
		self.network_integration_accordion.click()
		logger.debug('ServicesPage :Enable Feild is Unchecked.')
		if self.alto_enable.is_selected():
			raise AssertionError("Enable Feild is Checked.Traceback: %s " %traceback.format_exc())

		if self.alto_username:
			logger.debug('ServicesPage :Checking whether Username feild is Empty.')
			if not self.alto_username.get() == '' :
				raise AssertionError(" Username feild is not Empty.Traceback: %s " %traceback.format_exc())

		if self.alto_password:
			logger.debug('ServicesPage :Checking whether Password feild is Empty.')
			if not self.alto_password.get() == '':
				raise AssertionError("Password feild is not Empty.Traceback: %s " %traceback.format_exc())

		if self.alto_retype_password:
			logger.debug('ServicesPage :Checking whether Retype Password feild is Empty.')
			if not self.alto_retype_password.get() == '' :
				raise AssertionError("Retype Password feild is not Empty.Traceback: %s " %traceback.format_exc())

		if self.alto_ip_address:
			logger.debug('ServicesPage :Checking whether IP Address feild is Empty.')
			if not self.alto_ip_address.get() == '' :
				raise AssertionError("IP Address feild is not Empty.Traceback: %s " %traceback.format_exc())

		if self.alto_port:
			logger.debug('ServicesPage :Checking whether port is set to 443.')
			if not self.alto_port.get() == self.config.config_vars.alto_port :
				raise AssertionError("Port is not set to 443.Traceback: %s " %traceback.format_exc())


	def set_network_integration_non_default_values(self):
		logger.debug("ServicesPage : Clicking on Network Integration Accordion. ")
		self.network_integration_accordion.click()
		logger.debug('ServicesPage :Check Enable Feild.')
		self.alto_enable.click()
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
		self.alto_retype_password.set(self.config.config_vars.invalid_value)
		self.alto_port.set(self.config.config_vars.invalid_alto_port)
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
		if not self.alto_username_error:
			raise AssertionError("Username error message not found i.e. Traceback: %s" %traceback.format_exc())
		if not self.alto_password_error:
			raise AssertionError("Password error message not found i.e. Traceback: %s" %traceback.format_exc())
		if not self.alto_retype_password_error:
			raise AssertionError("Retype Password error message not found i.e. Traceback: %s" %traceback.format_exc())
		if not self.alto_ip_address_error:
			raise AssertionError("IP Addresss error message not found i.e. Traceback: %s" %traceback.format_exc())
		if not self.alto_error:
			raise AssertionError("Port error message not found i.e. Traceback: %s" %traceback.format_exc())
	
		logger.debug("ServicesPage : Set Username value . ")		
		self.alto_username.set(self.config.config_vars.User_Name)
		logger.debug("ServicesPage : Set Password value . ")
		self.alto_password.set(self.config.config_vars.Network_Passphrase)
		logger.debug("ServicesPage : Set Retype Password value . ")
		self.alto_retype_password.set(self.config.config_vars.Network_Passphrase)
		logger.debug("ServicesPage : Set IP Addresss value . ")
		self.alto_ip_address.set(self.config.config_vars.Ip_Address)
		logger.debug("ServicesPage : Set Port value. ")
		self.alto_port.set(self.config.config_vars.Port)
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()

	def reset_network_integration_fields(self):
		logger.debug('ServicesPage :Uncheck Enable Feild.')
		if self.alto_enable.is_selected():
			self.alto_enable.click()
		logger.debug("ServicesPage : Set Username to none . ")
		self.alto_username.set('')
		logger.debug("ServicesPage : Set Password to none . ")
		self.alto_password.set('')
		logger.debug("ServicesPage : Set Retype Password to none . ")
		self.alto_retype_password.set('')
		logger.debug("ServicesPage : Set IP Addresss to none . ")
		self.alto_ip_address.set('')
		logger.debug("ServicesPage : Set Port to 443 . ")
		self.alto_port.set(self.config.config_vars.alto_port)
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()

	def click_on_enable_air_group(self):
		'''
		Clicking on Air Group checkbox
		'''
		logger.debug("Service: Clicking on AirGroup checkbox")
		self.enable_air_group.click()

	def click_on_enable_air_print_checkbox(self):
		'''
		Clicking on Enable Air Print checkbox
		'''
		logger.debug("Service: Clicking on Air Print checkbox")
		self.enable_air_print.click()
		if not self.enable_air_print.is_selected():
			logger.debug('ServicesPage : Enabling air print')
			self.enable_air_print.click()

	def click_on_itunes_checkbox(self):
		'''
		Clicking on Enable Itunes checkbox
		'''
		logger.debug("Service: Clicking on Itunes checkbox")
		self.itunes.click()
		if not self.itunes.is_selected():
			logger.debug('ServicesPage : Enabling air itunes')
			self.itunes.click()

	def click_on_remote_management(self):
		'''
		Clicking on Remote Management checkbox
		'''
		logger.debug("Services: Clicking on Remote Management checkbox")
		self.enable_remote_mgemt.click()
		if not self.enable_remote_mgemt.is_selected():
			logger.debug('ServicesPage : Enabling remote management')
			self.enable_remote_mgemt.click()

	def click_on_sharing_checkbox(self):
		'''
			Clicking on Sharing checkbox
		'''
		logger.debug("Services: Clicking on Sharing checkbox")
		self.enable_sharing.click()
		if not self.enable_sharing.is_selected():
			self.enable_sharing.click()

	def click_on_chat_checkbox(self):
		'''
		Clicking on chat checkbox
		'''
		logger.debug("Services: Clicking on Chat checkbox")
		self.enable_chat.click()	
		if not self.enable_chat.is_selected():		
			self.enable_chat.click()	

	def click_on_allowall_checkbox(self):
		'''
		Clicking on allowall checkbox
		'''
		logger.debug("Services: Clicking on Allowall checkbox")
		self.enable_allowall.click()
		if not self.enable_allowall.is_selected():
			self.enable_allowall.click()
		
	def click_on_rtls_accordion(self):
		'''
		Opening rtls accordion
		'''
		logger.debug("Services: Clicking on RTLS Accordion")
		self.rtls_menu.click()
		self.buy_time()

	def click_on_aruba_rtls(self):
		'''
		Clicking on aruba rtls
		'''
		logger.debug("Services: Clicking on Aruba RTLS checkbox")
		self.aruba_rtls.click()

	def edit_air_print_disallowed_role(self):
		'''
		Editing Air Print Disallowed role
		'''
		logger.debug("Service: Clicking on Air Print Disallowed Roles Edit button")
		self.edit_air_print_disallowed_roles.click()
		logger.debug("Services: Adding role in selected list")
		self.default_role_option.click()
		logger.debug("Services: Clicking on Move button")
		self.move_role_button.click()
		logger.debug("Services: Clicking on OK button")
		self.save_roles_popup.click()
		if not self.created_default_role_text:
			raise AssertionError("Newly selected rule is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))

	def edit_itunes_disallowed_role(self):
		'''
		Editing Itunes Disallowed role
		'''
		logger.debug("Service: Clicking on Itunes Disallowed Roles Edit button")
		self.itunes_disallowed_roles.click()
		logger.debug("Services: Adding role in selected list")
		self.default_role_option.click()
		logger.debug("Services: Clicking on Move button")
		self.move_role_button.click()
		logger.debug("Services: Clicking on OK button")
		self.save_roles_popup.click()
		if not self.created_default_role_text:
			raise AssertionError("Newly selected rule is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))

	def edit_remote_management_disallowed_role(self):
		'''
		Editing Remote Management Disallowed role
		'''
		logger.debug("Service: Clicking on Remote Management Disallowed Roles Edit button")
		self.remote_management_disallowed_roles.click()
		logger.debug("Services: Adding role in selected list")
		self.default_role_option.click()
		logger.debug("Services: Clicking on Move button")
		self.move_role_button.click()
		logger.debug("Services: Clicking on OK button")
		self.save_roles_popup.click()
		if not self.created_default_role_text:
			raise AssertionError("Newly selected rule is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))               
		
	def edit_sharing_disallowed_role(self):
		'''
		Editing Sharing Disallowed role
		'''
		logger.debug("Service: Clicking on Sharing Disallowed Roles Edit button")
		self.sharing_disallowed_roles.click()
		logger.debug("Services: Adding role in selected list")
		self.default_role_option.click()
		logger.debug("Services: Clicking on Move button")
		self.move_role_button.click()
		logger.debug("Services: Clicking on OK button")
		self.save_roles_popup.click()
		if not self.created_default_role_text:
			raise AssertionError("Newly selected rule is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))

	def edit_chat_disallowed_role(self):
		'''
		Editing Chat Disallowed role
		'''
		logger.debug("Service: Clicking on Chat Disallowed Roles Edit button")
		self.chat_disallowed_roles.click()
		logger.debug("Services: Adding role in selected list")
		self.default_role_option.click()
		logger.debug("Services: Clicking on Move button")
		self.move_role_button.click()
		logger.debug("Services: Clicking on OK button")
		self.save_roles_popup.click()
		if not self.created_default_role_text:
			raise AssertionError("Newly selected rule is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))

	def edit_allowall_disallowed_role(self):
		'''
		Editing Chat Disallowed role
		'''
		logger.debug("Service: Clicking on Allowall Disallowed Roles Edit button")
		self.allowall_disallowed_roles.click()
		logger.debug("Services: Adding role in selected list")
		self.default_role_option.click()
		logger.debug("Services: Clicking on Move button")
		self.move_role_button.click()
		logger.debug("Services: Clicking on OK button")
		self.save_roles_popup.click()
		if not self.created_default_role_text:
			raise AssertionError("Newly selected rule is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))               
		 

	def edit_air_print_disallowed_vlans_id(self):
		'''
		Editing Air Print Disallowed vlans
		'''
		logger.debug("Service: Clicking on Air Print Disallowed Vlans Edit button")
		self.edit_air_print_disallowed_vlans.click()
		logger.debug("Services: Entering invalid value in vlan id textbox")
		self.air_print_disallowed_vlan_id_textbox.set('0')
		logger.debug("Services: Clicking on OK button")
		self.air_print_disallowed_vlan_OK_button.click()
		if not self.vlans_list_error:
			raise AssertionError("Invalid input message is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))               
		logger.debug("Services: Entering valid value in vlan id")
		self.air_print_disallowed_vlan_id_textbox.set('1,2')
		logger.debug("Services: Clicking on OK button")
		self.air_print_disallowed_vlan_OK_button.click()
		if not self.created_vlans_text_1:
			raise AssertionError("Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		if not self.created_vlans_text_2:
			raise AssertionError("Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))

	def edit_itunes_disallowed_vlans_id(self):
		'''
		Editing Itunes Disallowed vlans
		'''
		logger.debug("Service: Clicking on Itunes Disallowed Vlans Edit button")
		self.itunes_disallowed_vlans.click()
		logger.debug("Services: Entering invalid value in vlan id textbox")
		self.air_print_disallowed_vlan_id_textbox.set('0')
		logger.debug("Services: Clicking on OK button")
		self.air_print_disallowed_vlan_OK_button.click()
		if not self.vlans_list_error:
			raise AssertionError("Invalid input message is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))               
		logger.debug("Services: Entering valid value in vlan id")
		self.air_print_disallowed_vlan_id_textbox.set('1,2')
		logger.debug("Services: Clicking on OK button")
		self.air_print_disallowed_vlan_OK_button.click()
		if not self.created_vlans_text_1:
			raise AssertionError("Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		if not self.created_vlans_text_2:
			raise AssertionError("Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))  

	def edit_remote_management_disallowed_vlans_id(self):
		'''
		Editing Remote Management Disallowed vlans
		'''
		logger.debug("Service: Clicking on Remote Management Disallowed Vlans Edit button")
		self.remote_management_disallowed_vlans.click()
		logger.debug("Services: Entering invalid value in vlan id textbox")
		self.air_print_disallowed_vlan_id_textbox.set('0')
		logger.debug("Services: Clicking on OK button")
		self.air_print_disallowed_vlan_OK_button.click()
		if not self.vlans_list_error:
			raise AssertionError("Invalid input message is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))               
		logger.debug("Services: Entering valid value in vlan id")
		self.air_print_disallowed_vlan_id_textbox.set('1,2')
		logger.debug("Services: Clicking on OK button")
		self.air_print_disallowed_vlan_OK_button.click()
		if not self.created_vlans_text_1:
			raise AssertionError("Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		if not self.created_vlans_text_2:
			raise AssertionError("Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))

	def edit_sharing_disallowed_vlans_id(self):
		'''
		Editing Sharing Disallowed vlans
		'''
		logger.debug("Service: Clicking on Sharing Disallowed Vlans Edit button")
		self.sharing_disallowed_vlans.click()
		logger.debug("Services: Entering invalid value in vlan id textbox")
		self.air_print_disallowed_vlan_id_textbox.set('0')
		logger.debug("Services: Clicking on OK button")
		self.air_print_disallowed_vlan_OK_button.click()
		if not self.vlans_list_error:
			raise AssertionError("Invalid input message is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))               
		logger.debug("Services: Entering valid value in vlan id")
		self.air_print_disallowed_vlan_id_textbox.set('1,2')
		logger.debug("Services: Clicking on OK button")
		self.air_print_disallowed_vlan_OK_button.click()
		if not self.created_vlans_text_1:
			raise AssertionError("Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		if not self.created_vlans_text_2:
			raise AssertionError("Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))                 

	def edit_chat_disallowed_vlans_id(self):
		'''
		Editing Chat Disallowed vlans
		'''
		logger.debug("Service: Clicking on Chat Disallowed Vlans Edit button")
		self.chat_disallowed_vlans.click()
		logger.debug("Services: Entering invalid value in vlan id textbox")
		self.air_print_disallowed_vlan_id_textbox.set('0')
		logger.debug("Services: Clicking on OK button")
		self.air_print_disallowed_vlan_OK_button.click()
		if not self.vlans_list_error:
			raise AssertionError("Invalid input message is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))               
		logger.debug("Services: Entering valid value in vlan id")
		self.air_print_disallowed_vlan_id_textbox.set('1,2')
		logger.debug("Services: Clicking on OK button")
		self.air_print_disallowed_vlan_OK_button.click()
		if not self.created_vlans_text_1:
			raise AssertionError("Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		if not self.created_vlans_text_2:
			raise AssertionError("Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))                 

	def edit_allowall_disallowed_vlans_id(self):
		'''
		Editing allowall Disallowed vlans
		'''
		logger.debug("Service: Clicking on Allowall Disallowed Vlans Edit button")
		self.allowall_disallowed_vlans.click()
		logger.debug("Services: Entering invalid value in vlan id textbox")
		self.air_print_disallowed_vlan_id_textbox.set('0')
		logger.debug("Services: Clicking on OK button")
		self.air_print_disallowed_vlan_OK_button.click()
		if not self.vlans_list_error:
			raise AssertionError("Invalid input message is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))               
		logger.debug("Services: Entering valid value in vlan id")
		self.air_print_disallowed_vlan_id_textbox.set('1,2')
		logger.debug("Services: Clicking on OK button")
		self.air_print_disallowed_vlan_OK_button.click()
		if not self.created_vlans_text_1:
			raise AssertionError("Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		if not self.created_vlans_text_2:
			raise AssertionError("Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))                 

	def enable_include_unassociated_stations(self):
		'''
		Entering all required values in ARUBA RTLS and enabling include_unassociated_stations checkbox
		'''
		logger.debug("Services: Clicking on Aruba RTLS checkbox")
		self.aruba_rtls.click()
		logger.debug("Services: Entering invalid values in all the fields")
		self.rtls_ip_address.set('-1')
		logger.debug("Services: Entering Rtls port")
		self.rtls_port.set('0')
		logger.debug("Services: Entering Rtls passphrase")
		self.rtls_passphrase.set('1')
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
		if not self.invalid_ip_address_msg:
			raise AssertionError("Invalid IP message is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		if not self.invalid_port_error_msg:
			raise AssertionError("Invalid Port message is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		if not self.invalid_passphrase_error_msg:
			raise AssertionError("Invalid Passphrase message is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		if not self.invalid_re_passphrase_error_msg:
			raise AssertionError("Invalid Re-Passphrase message is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		logger.debug("Services: Entering valid values in all the fields")
		self.rtls_ip_address.set('10.10.10.10')
		logger.debug("Services: Entering Rtls port")
		self.rtls_port.set('2')
		logger.debug("Services: Entering Rtls passphrase")
		self.rtls_passphrase.set('123456789')        
		self.rtls_re_passphrase.set('123456789')
		logger.debug("Services: Clicking on Include Unassociated Stations")
		self.rtls_unassociated_chk.click()
		logger.debug("Services: Clicking on Save Settings")
		self.save_settings()

	def click_on_enable_air_group_checkbox(self):
		'''
		Clicking on Air Group checkbox
		'''
		logger.debug("Service: Clicking on AirGroup checkbox")
		self.enable_air_group.click()

	def assert_open_dns_empty_password(self):
		self.buy_time()
		logger.debug("ServicesPage : clicking on Open Dns accordion")
		self.open_dns_accordion.click()
		logger.debug("ServicesPage : Set Dns Username. ")
		self.dns_username.set(self.config.config_vars.User_Name)
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
		if not self.open_dns_passwd_error:
			raise AssertionError("'Field is required' message is not present  i.e %s " %traceback.format_exc())
		

	def assert_open_dns_passwrd_with_blanks_inbetween(self):
		self.buy_time()
		logger.debug("ServicesPage : Set Dns Username. ")
		self.dns_username.set(self.config.config_vars.User_Name)
		logger.debug("ServicesPage : Set Dns password. ")
		self.dns_password.set(self.config.config_vars.open_dns_passwrd)
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
		if not self.open_dns_passwd_error1:
			raise AssertionError("'No Space Allowed' message is not present  i.e %s " %traceback.format_exc())

	def enable_airgroup_options(self):
		logger.debug("Service: Clicking on AirGroup checkbox")
		self.enable_air_group.click()
		logger.debug("ServicesPage : Enabling Bonjour Multicast ")
		self.guest_bonjour.click()
		logger.debug("Service: Clicking on Save Settings button")
		self.save_setting.click()
		self.buy_time()
		
	def click_on_network_integration_accordion(self):
		logger.debug("ServicesPage : Clicking on Network Integration Accordion. ")
		self.network_integration_accordion.click()
		self.buy_time()
		
	def edit_network_integration(self):
		'''
		edit non default values for Network Integration
		'''
		logger.debug('ServicesPage :Check Enable Feild.')
		self.alto_enable.click()
		logger.debug("ServicesPage : Set Username value . ")		
		self.alto_username.set(self.config.config_vars.User_Name1)
		logger.debug("ServicesPage : Set Password value . ")
		self.alto_password.set(self.config.config_vars.Network_Passphrase1)
		logger.debug("ServicesPage : Set Retype Password value . ")
		self.alto_retype_password.set(self.config.config_vars.Network_Passphrase1)
		logger.debug("ServicesPage : Set IP Addresss value . ")
		self.alto_ip_address.set(self.config.config_vars.Ip_Address1)
		logger.debug("ServicesPage : Set Port value. ")
		self.alto_port.set(self.config.config_vars.Port1)
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
		
	def set_calea_non_default_values(self):
		'''
		set non default values for CALEA Integration
		'''
		self.calea_accordion.click()
		logger.debug("ServicesPage : Set Calea ip address. ")
		self.calea_ip_address.set(self.config.config_vars.calea_ip_address)
		logger.debug("ServicesPage : Set Encapsulation type.")
		self.calea_encapsulation_type.set(self.config.config_vars.calea_encapsulation_type)
		logger.debug("ServicesPage : Set Calea gre type. ")
		self.calea_gre_type.set(self.config.config_vars.calea_gre_type1)
		logger.debug("ServicesPage : Set Calea mtu. ")
		self.calea_mtu.set(self.config.config_vars.calea_mtu1)                
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
		
	def conifgure_calea_ip_address_with_preceding_zeros(self):
		'''
		Setting Calea ip address with preceding zeros
		'''
		self.calea_accordion.click()
		logger.debug("ServicesPage : Set Calea ip address with preceding zeros.")
		self.calea_ip_address.set(self.config.config_vars.calea_ip_address_with_preceding_zeros)
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
		
	def assert_calea_ip_address_with_preceding_zeros(self):
		'''
		Checking whether calea ip address has ignored the zeros while considering the IPaddr.
		'''
		logger.debug("ServicesPage : Clicking on Calea Accordion. ")
		self.calea_accordion.click()
		if self.calea_ip_address:
			logger.debug('ServicesPage :Checking whether calea ip address has ignored the zeros while considering the IPaddr.')
			if not self.calea_ip_address.get() == self.config.config_vars.calea_ip_address_without_preceding_zeros:
				raise AssertionError("Calea ip address has not ignored the zeros while considering the IPaddr..Traceback: %s " %traceback.format_exc())
				
	def assert_rtls_fields(self):
		logger.debug("ServicesPage : Check whether the Rtls ip  address textbox is empty. ")
		if self.rtls_ip_address:
			if not self.rtls_ip_address.get() == '' :
				raise AssertionError("Rtls ip address textbox is not empty.Traceback: %s " %traceback.format_exc())

		logger.debug("ServicesPage : Check whether the Rtls port textbox is empty. ")
		if self.rtls_port:
			if not self.rtls_port.get() == '' :
				raise AssertionError("Rtls port textbox is not empty.Traceback: %s " %traceback.format_exc())

		logger.debug("ServicesPage : Check whether the Rtls passphrase textbox is empty. ")
		if self.rtls_passphrase:
			if not self.rtls_passphrase.get() == '' :
				raise AssertionError("Rtls passphrase textbox is not empty.Traceback: %s " %traceback.format_exc())

		logger.debug("ServicesPage : Check whether the Rtls Retype passphrase textbox is empty. ")
		if self.rtls_re_passphrase:
			if not self.rtls_re_passphrase.get() == '' :
				raise AssertionError("Rtls  Retype passphrase textbox  is not empty.Traceback: %s " %traceback.format_exc())

		logger.debug("ServicesPage : Check whether the INCLUDE UNASSOCIATED STATIONS is unchecked. ")		
		if self.rtls_unassociated_chk.is_selected():
			raise AssertionError("INCLUDE UNASSOCIATED STATIONS is checked.Traceback: %s " %traceback.format_exc())
			
	def click_analytics_location_engine_checkbox(self):
		logger.debug("ServicesPage : click on  analytics location engine checkbox. ")
		self.location_engine.click()
		
	def assert_rtls_analytics_location_engine_fields(self):
		logger.debug("ServicesPage : Check whether the server textbox is empty. ")
		if self.service_server:
			if not self.service_server.get() == '' :
				raise AssertionError("  Server textbox not empty.Traceback: %s " %traceback.format_exc())

		logger.debug("ServicesPage : Check for the report interval is set to 30 sec . ")
		if self.report_interval_location:
			if not self.report_interval_location.get() == self.config.config_vars.report_interval_location :
				raise AssertionError(" Report interval is not set to 30 sec.Traceback: %s " %traceback.format_exc())
				
	def click_aeroscout_checkbox(self):
		logger.debug("ServicesPage : Clicking on aeroscout checkbox. ")
		self.aero_scout.click()
		
	def assert_aeroscout_fields(self):
		logger.debug("ServicesPage : Check whether the aeroscout ip  address textbox is empty. ")
		if self.scout_ip_address:
			if not self.scout_ip_address.get() == '' :
				raise AssertionError("  Aeroscout ip address textbox not empty.Traceback: %s " %traceback.format_exc())

		logger.debug("ServicesPage : Check whether the aeroscout port textbox is empty. ")
		if self.scout_port:
			if not self.scout_port.get() == '' :
				raise AssertionError("  Aeroscout port textbox not empty.Traceback: %s " %traceback.format_exc())

		logger.debug("ServicesPage : Check whether the INCLUDE UNASSOCIATED STATIONS is unchecked. ")
		if self.scout_unassociated_chk.is_selected():
			raise AssertionError("INCLUDE UNASSOCIATED STATIONS is checked.Traceback: %s " %traceback.format_exc())
		
	
	def assert_entire_rtls_fields(self):
		self.assert_rtls_aeroscout_checkbox()
		logger.debug("ServicesPage : Clicking on aruba rtls. ")
		self.click_on_aruba_rtls()
		self.assert_rtls_fields()
		self.click_analytics_location_engine_checkbox()
		self.assert_rtls_analytics_location_engine_fields()
		self.click_aeroscout_checkbox()
		self.assert_aeroscout_fields()
		self.click_aeroscout_checkbox()
		self.click_analytics_location_engine_checkbox()
		self.click_on_aruba_rtls()
		# self.save_settings()
		
	def clear_calea_ip_address(self):
		logger.debug("ServicesPage : Set Calea ip address to null. ")
		self.calea_ip_address.set('')               
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
		
	def assert_airprint_disallowed_roles_and_vlans(self):
		'''
		Asserting Enable Airprint options 
		'''
		self.buy_time()
		if not self.enable_air_group.is_selected():
			logger.debug("Service: Clicking on AirGroup checkbox")
			self.enable_air_group.click()
		self.buy_time()
		self.page_down()
		if not self.enable_air_print.is_selected():
			logger.debug('ServicesPage : Enabling air print')
			self.enable_air_print.click()
		self.edit_air_print_disallowed_roles.click()
		if not self.close_Roles_popUp:
			self.edit_air_print_disallowed_roles.click()
		self._assert_dissallowed_roles()
		self.close_Roles_popUp.click()
		self.buy_time()
		self.edit_air_print_disallowed_vlans.click()
		if not self.close_vlans_popup:
			self.edit_air_print_disallowed_vlans.click()
		self._assert_dissallowed_vlans()
		self.close_vlans_popup.click()
		logger.debug('ServicesPage : Enabling air print')
		self.enable_air_print.click()
		logger.debug("Service: Clicking on AirGroup checkbox")
		self.enable_air_group.click()
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
		
		
	def assert_air_play_disallowed_roles_and_vlans(self):
		'''
		Asserting Enable Airplay options 
		'''
		self.buy_time()
		if not self.enable_air_group.is_selected():
			logger.debug("Service: Clicking on AirGroup checkbox")
			self.enable_air_group.click()
		self.buy_time()
		if not self.enable_air_play.is_selected():
			logger.debug('ServicesPage : Enabling air play')
			self.enable_air_play.click()
		self.buy_time()
		self.edit_air_play_disallowed_roles.click()
		self.buy_time()
		if not self.close_Roles_popUp:
			self.edit_air_play_disallowed_roles.click()
		self._assert_dissallowed_roles()
		self.close_Roles_popUp.click()
		self.buy_time()
		self.edit_air_play_disallowed_vlans.click()
		if not self.close_vlans_popup:
			self.edit_air_play_disallowed_vlans.click()
		self._assert_dissallowed_vlans()
		self.close_vlans_popup.click()
		logger.debug('ServicesPage : Enabling air play')
		self.enable_air_play.click()
		logger.debug("Service: Clicking on AirGroup checkbox")
		self.enable_air_group.click()
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
		self.buy_time()
		
	def _assert_dissallowed_roles(self):
		if not self.default_role_option:
			raise AssertionError("Default Wired Port Profile Role is not present .Traceback: %s " %traceback.format_exc()) 
		if not self.new_test_role:
			raise AssertionError("New role setup failed .Traceback: %s " %traceback.format_exc()) 
		if not self.wired_instant_role:
			raise AssertionError("Instant Wired  Role is not present .Traceback: %s " %traceback.format_exc()) 
	
	def _assert_dissallowed_vlans(self):
		if not self.air_print_disallowed_vlan_id_textbox.get() == '':
			raise AssertionError("there is no empty textbox in Air Print Disallowed Vlans ")

	def assert_itunes_disallowed_roles_and_vlans(self):
		'''
		Asserting Enable Itunes options 
		'''
		self.buy_time()
		if not self.enable_air_group.is_selected():
			logger.debug("Service: Clicking on AirGroup checkbox")
			self.enable_air_group.click()
		self.buy_time()
		self.page_down()
		if not self.itunes.is_selected():
			logger.debug('ServicesPage : Enabling air itunes')
			self.itunes.click()
		self.buy_time()
		self.itunes_disallowed_roles.click()
		self.buy_time()
		if not self.close_Roles_popUp:
			self.itunes_disallowed_roles.click()
		self._assert_dissallowed_roles()
		self.close_Roles_popUp.click()
		self.buy_time()
		self.itunes_disallowed_vlans.click()
		if not self.close_vlans_popup:
			self.itunes_disallowed_vlans.click()
		self._assert_dissallowed_vlans()
		self.close_vlans_popup.click()
		logger.debug('ServicesPage : Enabling air itunes')
		self.itunes.click()
		logger.debug("Service: Clicking on AirGroup checkbox")
		self.enable_air_group.click()
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
		self.buy_time()
	
	def assert_remote_management_disallowed_roles_and_vlans(self):
		'''
		Asserting Enable RemoteManagement options 
		'''
		self.buy_time()
		if not self.enable_air_group.is_selected():
			logger.debug("Service: Clicking on AirGroup checkbox")
			self.enable_air_group.click()
		self.buy_time()
		self.page_down()
		if not self.enable_remote_mgemt.is_selected():
			logger.debug('ServicesPage : Enabling remote management')
			self.enable_remote_mgemt.click()
		self.buy_time()
		self.remote_management_disallowed_roles.click()
		self.buy_time()
		if not self.close_Roles_popUp:
			self.remote_management_disallowed_roles.click()
		self._assert_dissallowed_roles()
		self.close_Roles_popUp.click()
		self.buy_time()
		self.remote_management_disallowed_vlans.click()
		if not self.close_vlans_popup:
			self.remote_management_disallowed_vlans.click()
		self._assert_dissallowed_vlans()
		self.close_vlans_popup.click()
		logger.debug('ServicesPage : Enabling remote management')
		self.enable_remote_mgemt.click()
		logger.debug("Service: Clicking on AirGroup checkbox")
		self.enable_air_group.click()
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
		self.buy_time()
		
	
	def assert_sharing_disallowed_roles_and_vlans(self):
		'''
		Asserting Enable Sharing options 
		'''
		self.buy_time()
		if not self.enable_air_group.is_selected():
			logger.debug("Service: Clicking on AirGroup checkbox")
			self.enable_air_group.click()
		self.buy_time()
		self.page_down()
		if not self.enable_sharing.is_selected():
			self.enable_sharing.click()
		self.buy_time()
		self.sharing_disallowed_roles.click()
		self.buy_time()
		if not self.close_Roles_popUp:
			self.sharing_disallowed_roles.click()
		self._assert_dissallowed_roles()
		self.close_Roles_popUp.click()
		self.buy_time()
		self.sharing_disallowed_vlans.click()
		if not self.close_vlans_popup:
			self.sharing_disallowed_vlans.click()
		self._assert_dissallowed_vlans()
		self.close_vlans_popup.click()
		self.enable_sharing.click()
		logger.debug("Service: Clicking on AirGroup checkbox")
		self.enable_air_group.click()
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
		self.buy_time()

	def assert_chat_disallowed_roles_and_vlans(self):
		'''
		Asserting Enable Chat options 
		'''
		self.buy_time()
		if not self.enable_air_group.is_selected():
			logger.debug("Service: Clicking on AirGroup checkbox")
			self.enable_air_group.click()
		self.buy_time()
		self.page_down()
		if not self.enable_chat.is_selected():
			self.enable_chat.click()
		self.buy_time()
		self.chat_disallowed_roles.click()
		self.buy_time()
		if not self.close_Roles_popUp:
			self.chat_disallowed_roles.click()
		self._assert_dissallowed_roles()
		self.close_Roles_popUp.click()
		self.buy_time()
		self.chat_disallowed_vlans.click()
		if not self.close_vlans_popup:
			self.chat_disallowed_vlans.click()
		self._assert_dissallowed_vlans()
		self.close_vlans_popup.click()
		self.enable_chat.click()
		logger.debug("Service: Clicking on AirGroup checkbox")
		self.enable_air_group.click()
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
		self.buy_time()
		
	def assert_allow_all_disallowed_roles_and_vlans(self):
		'''
		Asserting Enable AllowAll options 
		'''
		self.buy_time()
		if not self.enable_air_group.is_selected():
			logger.debug("Service: Clicking on AirGroup checkbox")
			self.enable_air_group.click()
		self.buy_time()
		self.page_down()
		if not self.enable_allowall.is_selected():
			self.enable_allowall.click()
		self.buy_time()
		self.allowall_disallowed_roles.click()
		self.buy_time()
		if not self.close_Roles_popUp:
			self.allowall_disallowed_roles.click()
		self._assert_dissallowed_roles()
		self.close_Roles_popUp.click()
		self.buy_time()
		self.allowall_disallowed_vlans.click()
		if not self.close_vlans_popup:
			self.allowall_disallowed_vlans.click()
		self._assert_dissallowed_vlans()
		self.close_vlans_popup.click()
		self.enable_allowall.click()
		logger.debug("Service: Clicking on AirGroup checkbox")
		self.enable_air_group.click()
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
		self.buy_time()
		
	def click_on_enable_air_play_checkbox(self):
		'''
		Clicking on Enable Air Play checkbox
		'''
		logger.debug("Service: Clicking on Air Play checkbox")
		self.enable_air_play.click()
		if not self.enable_air_play.is_selected():
			logger.debug('ServicesPage : Enabling air play')
			self.enable_air_play.click()

	def edit_air_group_setting_and_services_disallowed_role(self):
		'''
		Editing Air Group Disallowed role
		'''
		self._assert_dissallowed_roles()
		self.buy_time()
		logger.debug("Services: Adding role in selected list")
		self.default_role_option.click()
		self.buy_time()
		logger.debug("Services: Clicking on Move button")
		self.move_role_button.click()
		logger.debug("Services: Clicking on OK button")
		self.save_roles_popup.click()
		
		
	def click_on_edit_air_play_disallowed_roles(self):
		'''
		clicking on Edit button of Air Play Dissallowed role 
		'''
		self.edit_air_play_disallowed_roles.click()
		if not self.close_Roles_popUp:
			self.edit_air_play_disallowed_roles.click()
	
	def click_on_edit_air_play_disallowed_vlans(self):
		'''
		clicking on Edit button of Air Play Dissallowed vlans 
		'''
		self.edit_air_play_disallowed_vlans.click()
		if not self.close_vlans_popup:
			self.edit_air_play_disallowed_vlans.click()
	
	def edit_air_group_setting_and_services_disallowed_vlans(self):
		'''
		Editing Air Group Disallowed  vlans
		'''     
		self._assert_dissallowed_vlans()
		logger.debug("Services: Entering valid value in vlan id")
		self.air_print_disallowed_vlan_id_textbox.set('1,2')
		logger.debug("Services: Clicking on OK button")
		self.air_print_disallowed_vlan_OK_button.click()
		self.buy_time()
		
	def page_down(self):
		'''
		scroll down the page
		'''
		self.browser.key_press(u'\ue009')
		self.browser.key_press( u'\ue00f')
	
	def click_on_edit_air_print_disallowed_roles(self):
		'''
		clicking on Edit button of Air Print Dissallowed Roles
		'''
		self.edit_air_print_disallowed_roles.click()
		if not self.close_Roles_popUp:
			self.edit_air_print_disallowed_roles.click()
	
	def click_on_edit_air_print_disallowed_vlans(self):
		'''
		clicking on Edit button of Air Print Dissallowed vlans 
		'''
		self.edit_air_print_disallowed_vlans.click()
		if not self.close_vlans_popup:
			self.edit_air_print_disallowed_vlans.click()
			
	def click_on_edit_itunes_disallowed_roles(self):
		'''
		clicking on Edit button of Air Print Dissallowed Roles
		'''
		self.itunes_disallowed_roles.click()
		if not self.close_Roles_popUp:
			self.itunes_disallowed_roles.click()

	def click_on_edit_itunes_disallowed_vlans(self):
		'''
		clicking on Edit button of Air Print Dissallowed vlans 
		'''
		self.itunes_disallowed_vlans.click()
		if not self.close_vlans_popup:
			self.itunes_disallowed_vlans.click()
	
	def click_on_edit_remote_management_disallowed_roles(self):
		'''
		clicking on Edit button of Remote Management Dissallowed Roles
		'''
		self.remote_management_disallowed_roles.click()
		if not self.close_Roles_popUp:
			self.remote_management_disallowed_roles.click()

	def click_on_edit_remote_management_disallowed_vlans(self):
		'''
		clicking on Edit button of Remote Management Dissallowed vlans 
		'''
		self.remote_management_disallowed_vlans.click()
		if not self.close_vlans_popup:
			self.remote_management_disallowed_vlans.click()
			
	def click_on_edit_sharing_disallowed_roles(self):
		'''
		clicking on Edit button of Sharing Dissallowed Roles
		'''
		self.sharing_disallowed_roles.click()
		if not self.close_Roles_popUp:
			self.sharing_disallowed_roles.click()

	def click_on_edit_sharing_disallowed_vlans(self):
		'''
		clicking on Edit button of Sharing  Dissallowed vlans 
		'''
		self.sharing_disallowed_vlans.click()
		if not self.close_vlans_popup:
			self.sharing_disallowed_vlans.click()
	
	def click_on_edit_chat_disallowed_roles(self):
		'''
		clicking on Edit button of Chat Dissallowed Roles
		'''
		self.chat_disallowed_roles.click()
		if not self.close_Roles_popUp:
			self.chat_disallowed_roles.click()

	def click_on_edit_chat_disallowed_vlans(self):
		'''
		clicking on Edit button of Chat  Dissallowed vlans 
		'''
		self.chat_disallowed_vlans.click()
		if not self.close_vlans_popup:
			self.chat_disallowed_vlans.click()
			
	def click_on_edit_allow_all_disallowed_roles(self):
		'''
		clicking on Edit button of Allow All Dissallowed Roles
		'''
		self.allowall_disallowed_roles.click()
		if not self.close_Roles_popUp:
			self.allowall_disallowed_roles.click()

	def click_on_edit_allow_all_disallowed_vlans(self):
		'''
		clicking on Edit button of Allow All  Dissallowed vlans 
		'''
		self.allowall_disallowed_vlans.click()
		if not self.close_vlans_popup:
			self.allowall_disallowed_vlans.click()
	
	def assert_air_play_default_wired_port_profile(self):
		if not self.air_play_default_role:
			raise AssertionError("ServicesPage :Newly selected rule is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
			
	def assert_air_play_created_vlan_text(self):
		if not self.air_play_vlan_text1:
			raise AssertionError("ServicesPage :Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		self.buy_time()
		if not self.air_play_vlan_text2:
			raise AssertionError("ServicesPage :Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		self.buy_time()
		
	def assert_itunes_default_wired_port_profile(self):
		if not self.itunes_default_role:
			raise AssertionError("ServicesPage :Newly selected rule is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
			
	def assert_itunes_created_vlan_text(self):
		if not self.itunes_vlan_text1:
			raise AssertionError("ServicesPage :Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		self.buy_time()
		if not self.itunes_vlan_text2:
			raise AssertionError("ServicesPage :Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		self.buy_time()
		
	def assert_remote_management_wired_port_profile(self):
		if not self.remote_management_default_role:
			raise AssertionError("ServicesPage :Newly selected rule is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
			
	def assert_remote_management_created_vlan_text(self):
		if not self.remote_management_vlan_text1:
			raise AssertionError("ServicesPage :Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		self.buy_time()
		if not self.remote_management_vlan_text2:
			raise AssertionError("ServicesPage :Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		self.buy_time()
		
	def assert_sharing_wired_port_profile(self):
		if not self.sharing_default_role:
			raise AssertionError("ServicesPage :Newly selected rule is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
			
	def assert_sharing_created_vlan_text(self):
		if not self.sharing_vlan_text1:
			raise AssertionError("ServicesPage :Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		self.buy_time()
		if not self.sharing_vlan_text2:
			raise AssertionError("ServicesPage :Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		self.buy_time()
		
	def assert_chat_wired_port_profile(self):
		if not self.chat_default_role:
			raise AssertionError("ServicesPage :Newly selected rule is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
			
	def assert_chat_created_vlan_text(self):
		if not self.chat_vlan_text1:
			raise AssertionError("ServicesPage :Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		self.buy_time()
		if not self.chat_vlan_text2:
			raise AssertionError("ServicesPage :Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		self.buy_time()
		
	def assert_allow_all_wired_port_profile(self):
		if not self.allow_all_default_role:
			raise AssertionError("ServicesPage :Newly selected rule is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
			
	def assert_allow_all_created_vlan_text(self):
		if not self.allow_all_vlan_text1:
			raise AssertionError("ServicesPage : Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		self.buy_time()
		if not self.allow_all_vlan_text2:
			raise AssertionError("ServicesPage : Newly created vlan is not present  i.e %s. Traceback: %s" % (self.management_subnet, traceback.format_exc()))
		self.buy_time()
		
	def click_on_app_rf_accordion(self):
		'''
		Clicking on APP RF Accordion
		'''
		logger.debug("ServicesPage : Clicking on APP RF Accordion. ")
		self.app_rf_accordion.click()
		self.buy_time()
			
			
	def assert_enable_dpi(self, check):
		'''
		asserts enable dpi checkbox
		'''
		if check == 'true':
			if not self.enable_dpi.is_selected() :
				raise AssertionError('ServicesPage : Enable dpi checkbox is Disabled')
				
		else :
			if self.enable_dpi.is_selected() :
				raise AssertionError('ServicesPage : Enable dpi checkbox is Enabled')
				
	def set_enable_dpi(self,check):
		'''
		clicks on enable app rf checkbox
		'''
		if check == 'true':
			if not self.enable_dpi.is_selected() :
				logger.debug('Services: Clicking on Enable dpi checkbox')
				try:
					self.enable_dpi.click()
				except:
					pass
		else :
			if self.enable_dpi.is_selected() :
				logger.debug('Services: Clicking on Enable dpi checkbox')
				try:
					self.enable_dpi.click()
				except:
					pass
				
	def set_cppm_server1(self, option):
		'''
		selects given value for CPPM Server1
		'''
		logger.debug('Services: Selecting CPPM server')
		self.cppm_server_select.set(option)
		
	def set_new_server_name(self,name):
		'''
		writes given name in name field
		'''
		logger.debug('Services: Writing server name')
		self.auth_server_name.set(name)
		
	def set_new_server_ip(self,ip):
		'''
		writes given ip in IP Address field
		'''
		logger.debug('Services: Writing ip address')
		self.auth_ipaddr.set(ip)
		
	def set_new_server_shared_key(self,key):
		'''
		writes given key in Shared key field
		'''
		logger.debug('Services: Writing shared key')
		self.auth_sharedkey.set(key)

	def set_new_server_retype_shared_key(self,key):
		'''
		writes given key in Shared key field
		'''
		logger.debug('Services: Writing retype shared key')
		self.retype_auth_shared_key.set(key)
		
	def set_rfc_3576(self,option):
		'''
		Enables or disables depending on the option
		'''
		if option == 'enable' :
			if not self.rfc_3576.is_selected() :
				logger.debug('Services: Clicking on rfc 3576')
				self.rfc_3576.click()
		if option == 'disable' :
			if self.rfc_3576.is_selected() :
				logger.debug('Services: Clicking on rfc 3576')
				self.rfc_3576.click()
			
	def set_accounting_port(self, port):
		'''
		writing given port in accounting port field
		'''
		logger.debug('Services: Writing Accounting port')
		self.accounting_port.set(port)
		
	def set_deadtime(self, time):
		'''
		writing given time in Deadtime field
		'''
		logger.debug('Services: Writing dead time')
		self.deadtime.set(time)
		
	def set_timeout(self, time):
		'''
		writing given time in Timeout field
		'''
		logger.debug('Services: Writing time out')
		self.timeout.set(time)
		
	def set_retrycount(self, count):
		'''
		writing given count in Retry count field
		'''
		logger.debug('Services: Writing Retry count')
		self.retrycount.set(count)
		
	def set_nas_ip_address(self, ip):
		'''
		writing given count in Retry count field
		'''
		logger.debug('Services: Writing NAS IP address')
		self.nas_ip_address.set(ip)
		
	def set_nas_identifier(self, value):
		'''
		writing given count in Retry count field
		'''
		logger.debug('Services: Writing NAS identifier')
		self.nas_identifier.set(value)
		
	def set_auth_port(self,value):
		'''
		writes given value into auth port field
		'''
		logger.debug('Services: Writing auth port')
		self.authport.set(value)
		
	def save_auth_server(self):
		'''
		clicks on save server button
		'''
		logger.debug('Services: clicking on save button')
		self.cppm_save_button.click()
		self.buy_time()
		
		
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
		
	def set_tacacs_auth_port(self,value):
		'''
		writes given value into auth port field
		'''
		logger.debug('Services: Writing auth port')
		self.Auth_Tacacs_Port.set(value)
		
	def set_tacacs_timeout(self, time):
		'''
		writing given time in Timeout field
		'''
		logger.debug('Services: Writing time out')
		self.auth_tacacs_timeout.set(time)
		
	def set_new_server_tacacs_ip(self,ip):
		'''
		writes given ip in IP Address field
		'''
		logger.debug('Services: Writing ip address')
		self.auth_tacacs_ipaddr.set(ip)
		
	def set_tacacs_retrycount(self, count):
		'''
		writing given count in Retry count field
		'''
		logger.debug('Services: Writing Retry count')
		self.auth_tacacs_retry_count.set(count)
		
	def set_airgroup_port(self, port):
		'''
		writes given value into airgroup port field
		'''
		logger.debug('Services: Writing auth port')
		self.airgroup_port.set(port)
		
	def set_rtls_fields(self,ipaddr,port,passphrase,repassphrase,update):
		'''
		Sets rtls fields
		'''
		logger.debug("Services: Entering Rtls ip address")
		self.rtls_ip_address.set(ipaddr)
		logger.debug("Services: Entering Rtls port")
		self.rtls_port.set(port)
		logger.debug("Services: Entering Rtls passphrase")
		self.rtls_passphrase.set(passphrase) 
		logger.debug("Services: Entering Rtls retype passphrase")		
		self.rtls_re_passphrase.set(repassphrase)
		logger.debug("Services: Entering Rtls Update every ")
		self.rtls_update.set(update)
		
	def click_rtls_unassociated_chk(self):
		'''
		Clicking on RTLS INCLUDE UNASSOCIATED STATIONS
		'''
		logger.debug("ServicesPage : Click INCLUDE UNASSOCIATED STATIONS . ")		
		self.rtls_unassociated_chk.click()
	
	def set_rtls_analytics_location_engine_fields(self,server,interval):
		'''
		Sets rtls analytics location engine fields
		'''
		logger.debug("ServicesPage : Entering service server. ")
		self.service_server.set(server)
		logger.debug("ServicesPage : Entering report interval.")        
		self.report_interval_location.set(interval)
		
	def set_aeroscout_fields(self,ipaddr,port):
		'''
		Sets aeroscout fields
		'''
		logger.debug("Services: Entering aeroscout ip  address ")
		self.scout_ip_address.set(ipaddr)
		logger.debug("Services: Entering aeroscout port ")
		self.scout_port.set(port)
	
	def click_scout_unassociated_chk(self):
		'''
		Clicking on SCOUT INCLUDE UNASSOCIATED STATIONS
		'''
		logger.debug("ServicesPage : Click INCLUDE UNASSOCIATED STATIONS . ")		
		self.scout_unassociated_chk.click()
		
	def clear_entire_rtls_fields(self,aruba_rtls=False,location_engine=False,aero_scout=False):
		'''
		Clears entire Rtls fields
		'''
		if aruba_rtls :
			logger.debug("Services: Entering Rtls ip address")
			self.rtls_ip_address.set('')
			logger.debug("Services: Entering Rtls port")
			self.rtls_port.set('')
			logger.debug("Services: Entering Rtls passphrase")
			self.rtls_passphrase.set('') 
			logger.debug("Services: Entering Rtls retype passphrase")		
			self.rtls_re_passphrase.set('')
			logger.debug("Services: Entering Rtls Update every ")
			self.rtls_update.set('30')
			logger.debug("Services: Clicking on Aruba RTLS checkbox")
			self.aruba_rtls.click()

		if location_engine :
			logger.debug("ServicesPage : Entering service server. ")
			self.service_server.set('')
			logger.debug("ServicesPage : Entering report interval.")        
			self.report_interval_location.set('30')
			logger.debug("ServicesPage : click on  analytics location engine checkbox. ")
			self.location_engine.click()

		if aero_scout :
			logger.debug("Services: Entering aeroscout ip  address ")
			self.scout_ip_address.set('')
			logger.debug("Services: Entering aeroscout port ")
			self.scout_port.set('')
			logger.debug("ServicesPage : Clicking on aeroscout checkbox. ")
			self.aero_scout.click()
		
	def assert_auth_server_name(self):
		logger.debug("ServicesPage : Check whether the Auth Server Name  textbox is empty. ")
		if self.auth_server_name:
			if not self.auth_server_name.get() == '' :
				raise AssertionError("Auth Server Name textbox is not empty.Traceback: %s " %traceback.format_exc())
				
	def assert_auth_ipaddr(self):
		logger.debug("ServicesPage : Check whether the Auth IP Address textbox is empty. ")
		if self.auth_ipaddr:
			if not self.auth_ipaddr.get() == '' :
				raise AssertionError("Auth IP Address textbox is not empty.Traceback: %s " %traceback.format_exc())
				
	def assert_auth_sharedkey(self):
		logger.debug("ServicesPage : Check whether the Auth Shared Key textbox is empty. ")
		if self.auth_sharedkey:
			if not self.auth_sharedkey.get() == '' :
				raise AssertionError("Shared Key textbox is not empty.Traceback: %s " %traceback.format_exc())
				
	def assert_retype_auth_shared_key(self):
		logger.debug("ServicesPage : Check whether the Auth Retype-Shared Key textbox is empty. ")
		if self.retype_auth_shared_key:
			if not self.retype_auth_shared_key.get() == '' :
				raise AssertionError("Retype-Shared Key textbox is not empty.Traceback: %s " %traceback.format_exc())
				
				
	def assert_airGroup_port(self):
		logger.debug("ServicesPage : Check whether the AirGroup Port textbox is set to 5999. ")
		if self.airgroup_port:
			if not self.airgroup_port.get() == self.config.config_vars.coa_port :
				raise AssertionError(" AirGroup Port textbox is not set to 5999 .Traceback: %s " %traceback.format_exc())
				
	def assert_auth_account_port(self):
		logger.debug("ServicesPage : Check whether the Auth Account Port textbox is set to 1813. ")
		if self.accounting_port:
			if not self.accounting_port.get() == self.config.config_vars.act_port_default :
				raise AssertionError(" Auth Account Port textbox is not set to 1813 .Traceback: %s " %traceback.format_exc())
				
	def assert_dead_time(self):
		logger.debug("ServicesPage : Check whether the Dead Time textbox is set to 5. ")
		if self.deadtime:
			if not self.deadtime.get() == self.config.config_vars.dead_time_default :
				raise AssertionError(" Dead Time textbox is not set to 5 .Traceback: %s " %traceback.format_exc())
				
	def assert_timeout(self):
		logger.debug("ServicesPage : Check whether the Timeout textbox is set to 5. ")
		if self.timeout:
			if not self.timeout.get() == self.config.config_vars.dead_time_default :
				raise AssertionError(" Timeout textbox is not set to 5 .Traceback: %s " %traceback.format_exc())
				
				
	def assert_retry_count(self):
		logger.debug("ServicesPage : Check whether the retry count textbox is set to 3")
		if self.retrycount:
			if not self.retrycount.get() == self.config.config_vars.retry_count_default :
				raise AssertionError(" Retry Count textbox is not set to 3 .Traceback: %s " %traceback.format_exc())
				
	def assert_auth_port(self):
		logger.debug("ServicesPage : Check whether the Auth Account Port textbox is set to 1812. ")
		if self.authport:
			if not self.authport.get() == self.config.config_vars.auth_port_default :
				raise AssertionError(" Auth Account Port textbox is not set to 1812 .Traceback: %s " %traceback.format_exc())
				
	
	
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
				
	def assert_radius_radio(self, enable):
		'''
		asserts radius radio button
		'''
		if enable == 'true':
			if not self.radius.is_selected() :
				raise AssertionError('Radius Radio button is Disabled')
				
		else :
			if self.radius.is_selected() :
				raise AssertionError('Radius Radio button is Enabled')
		
	def assert_rfc_3576(self, enable):
		'''
		asserts rfc 3576 checkbox
		'''
		if enable == 'true':
			if not self.rfc_3576.is_selected() :
				raise AssertionError('Radius Radio button is Disabled')
				
		else :
			if self.rfc_3576.is_selected() :
				raise AssertionError('Radius Radio button is Enabled')

	def select_default_role(self):
		'''
		selects default wired port profile
		'''
		logger.debug("Services: Clicking on Default port profile")
		self.default_role_option.click()


	def move_back_selected_role(self):
		'''
		clicks on move button
		'''
		logger.debug("Services: Clicking on Move button")
		self.move_role_back_button.click()
		
	def save_roles(self):
		'''
		clicks on ok button
		'''
		logger.debug("Services: Clicking on OK button")
		self.save_roles_popup.click()
	
	def select_wired_instant_role(self):
		''''
		selects wired instant role
		'''
		logger.debug("Services: Clicking on wired instant ")
		self.wired_instant_role.click()

	def move_selected_role(self):
		'''
		clicks on move button
		'''
		logger.debug("Services: Clicking on Move button")
		self.move_role_button.click()
	
	def set_vlans(self, vlan):
		'''
		writes given vlan into vlan field
		'''
		logger.debug("Services: writing vlan")
		self.air_print_disallowed_vlan_id_textbox.set(vlan)
		
	def save_vlan_pop_up(self):
		'''
		clicks on ok button
		'''
		logger.debug("Services: Clicking on OK button")
		self.air_print_disallowed_vlan_OK_button.click()
		
	def edit_cppm_server1(self):
		'''
		clicks on cppm server1 edit button
		'''
		logger.debug('ServicesPage : clicking on cppm server1 edit button')
		self.edit_cppm_server1.click()
		
	def asserting_aruba_rtls_fields_value(self,ip=None,port=None,passphrase=None,repassphrase=None,range=None):
		logger.debug("ServicePage: Asserting the Aruba RTLS fields")
		if ip:
			if not self.invalid_ip_address_msg:
				raise AssertionError("Invalid IP message is not present")
		else:
			if self.invalid_ip_address_msg:
				raise AssertionError("Invalid IP message is present")
		if port:
			if not self.invalid_port_error_msg:
				raise AssertionError("Number range Port message is not present ")
		else:
			if self.invalid_port_error_msg:
				raise AssertionError("Number range Port message is present ")
		if passphrase:
			if not self.invalid_passphrase_error_msg:
				raise AssertionError("Passphrase Length error message is not present ")
		else:
			if self.invalid_passphrase_error_msg:
				raise AssertionError("Passphrase Length error message is present ")		
		if repassphrase:
			if not self.invalid_re_passphrase_error_msg:
				raise AssertionError("Field mis-match error message is not present ")
		else:
			if self.invalid_re_passphrase_error_msg:
				raise AssertionError("Field mis-match error message is present ")		
		if range:
			if not self.number_range_error_msg:
				raise AssertionError("Number range error message is not present")
		else:
			if self.number_range_error_msg:
				raise AssertionError("Number range error message is present")
	
	def asserting_location_engine_fields(self,server=None,interval=None):
		logger.debug("ServicePage: Asserting the Analytics and Location Engine fields")
		if server:
			if not self.service_server_error:
				raise AssertionError("Invalid IP message is not present")
		else:
			if self.service_server_error:
				raise AssertionError("Invalid IP message is present")
		if interval:
			if not self.report_interval_location_error:
				raise AssertionError("Number range message is not present")
		else:
			if self.report_interval_location_error:
				raise AssertionError("Number range message is present")			
	
	def asserting_aeroscout_fields(self,ip=None,port=None):
		logger.debug("ServicePage: Asserting the Aeroscout fields")
		if ip:
			if not self.aeroscout_ip_error_msg:
				raise AssertionError("Invalid IP message is not present")
		else:
			if self.aeroscout_ip_error_msg:
				raise AssertionError("Invalid IP message is present")
		if port:
			if not self.aeroscout_port_error_msg:
				raise AssertionError("Number range error message is not present")
		else:
			if self.aeroscout_port_error_msg:
				raise AssertionError("Number range error message is present")
	
	def rtls_field_validation(self):
		conf = self.config.config_vars
		logger.debug('RTLS: Clicking on RTLS accordion ')
		self.rtls_click()
		logger.debug('RTLS: Clicking on Aruba RTLS checkbox ')
		self.click_on_aruba_rtls()
		logger.debug('RTLS: Seeting values in Aruba RTLS fields ')
		self.set_rtls_fields(conf.calea_invalid_ip_address,conf.invalid_alto_port,conf.invalid_value_2,conf.dns_password,conf.rtls_update_value)
		logger.debug('RTLS: Clicking on Analytics and Location Engine checkbox ')
		if not self.location_engine.is_selected():
			self.click_analytics_location_engine_checkbox()
		self.set_rtls_analytics_location_engine_fields(conf.calea_invalid_ip_address,conf.invalid_value)
		logger.debug('RTLS: Clicking on Aeroscout checkbox ')
		if not self.aero_scout.is_selected():
			self.click_aeroscout_checkbox()
		self.set_aeroscout_fields(conf.calea_invalid_ip_address,conf.invalid_alto_port)
		logger.debug('RTLS: Clicking on Save Setting button ')
		self.save_setting.click()
		logger.debug('RTLS: Asserting fields')
		self.asserting_aruba_rtls_fields_value(True,True,True,True,True)
		self.asserting_location_engine_fields(True,True)
		self.asserting_aeroscout_fields(True,True)
		logger.debug('RTLS: Settings the values')
		self.set_rtls_fields(conf.Ip_Address,conf.act_port,conf.dns_password,conf.dns_password,conf.rtls_update)
		self.set_rtls_analytics_location_engine_fields(conf.Ip_Address,conf.report_interval_location)
		self.set_aeroscout_fields(conf.Ip_Address,conf.act_port)
		
		self.click_rtls_unassociated_chk()
		self.click_rtls_unassociated_chk()
		self.save_setting.click()
		logger.debug('RTLS: Asserting fields')
		self.asserting_aruba_rtls_fields_value(False,False,False,False,False)
		self.asserting_location_engine_fields(False,False)
		self.asserting_aeroscout_fields(False,False)
	
	def assert_auth_server_name_maxlength_error(self,assert_error=None):
		'''
		Asserts Auth Server Name Maxlength Error
		'''
		if assert_error == None:
			if self.auth_server_name_maxlength_error:
				raise AssertionError("Maximum 32 characters allowed.Traceback: %s " %traceback.format_exc())
		if assert_error == True:
			if not self.auth_server_name_maxlength_error:
				raise AssertionError("Auth Server Name textbox is Accepting more than 32 characters allowed.Traceback: %s " %traceback.format_exc())
				
	def assert_auth_ipaddr_error(self,assert_error=None):
		'''
		Asserts Auth Server IP address Error
		'''	
		if assert_error == None:
			if  self.auth_ipaddr_error:
				raise AssertionError("Invalid IP Address.Traceback: %s " %traceback.format_exc())
		if assert_error == True:		
			if not self.auth_ipaddr_error:
				raise AssertionError("Accepting Invalid IP Address.Traceback: %s " %traceback.format_exc())	
				
	def assert_auth_Sharedkey_error(self,assert_error=None):
		'''
		Asserts Auth Server SharedKey  Error
		'''	
		if assert_error == None:
			if  self.auth_Sharedkey_error:
				raise AssertionError("Length must be 2-64 characters.Traceback: %s " %traceback.format_exc())
		if assert_error == True:		
			if not self.auth_Sharedkey_error:
				raise AssertionError("Accepting Invalid value for SharedKey.Traceback: %s " %traceback.format_exc())				
	
	def assert_auth_account_port_error(self,assert_error=None):
		'''
		Asserts Auth Server Auth Account port Error
		'''	
		if assert_error == None:
			if  self.auth_account_port_error:
				raise AssertionError("Must be a number in range 1-65534.Traceback: %s " %traceback.format_exc())
		if assert_error == True:		
			if not self.auth_account_port_error:
				raise AssertionError("Accepting Invalid value range.Traceback: %s " %traceback.format_exc())
	
	def set_drpmask(self, netmask):
		'''
		writing given netmask in drpmask field
		'''
		logger.debug('Services: Writing drpmask')
		self.drpmask.set(netmask)

	def assert_deadtime_error(self,assert_error=None):
		'''
		Asserts Auth Server DeadTime error
		'''	
		if assert_error == None:
			if self.deadtime_error:
				raise AssertionError("Must be a number in range 1-1440.Traceback: %s " %traceback.format_exc())
		if assert_error == True:		
			if not self.deadtime_error:
				raise AssertionError("Accepting Invalid value range.Traceback: %s " %traceback.format_exc())
	
	def assert_drpmask_error(self,assert_error=None):
		'''
		Asserts Auth Server DrpMask error  
		'''	
		if assert_error == None:
			if  self.drpmask_error:
				raise AssertionError("Invalid Net Mask.Traceback: %s " %traceback.format_exc())
		if assert_error == True:		
			if not self.drpmask_error:
				raise AssertionError("Accepting Invalid Net Mask.Traceback: %s " %traceback.format_exc())
	
	def set_drp_gateway(self, gateway):
		'''
		writing given netmask in Drp Gateway field
		'''
		logger.debug('Services: Writing Drp Gateway')
		self.drpgateway.set(gateway)
	
	def assert_auth_timeout_error(self,assert_error=None):
		'''
		Asserts Auth Server Timeout error  
		'''	
		if assert_error == None:
			if  self.auth_timeout_error:
				raise AssertionError("Must be a number in range 1-30: %s " %traceback.format_exc())
		if assert_error == True:		
			if not self.auth_timeout_error:
				raise AssertionError("Accepting Invalid Timeout .Traceback: %s " %traceback.format_exc())
	
	def assert_auth_retry_count_error(self,assert_error=None):
		'''
		Asserts Auth Server Retry Count error  
		'''	
		if assert_error == None:
			if  self.auth_retry_count_error:
				raise AssertionError("Must be a number in range 1-5: %s " %traceback.format_exc())
		if assert_error == True:		
			if not self.auth_retry_count_error:
				raise AssertionError("Accepting Invalid Retry Count .Traceback: %s " %traceback.format_exc())
	
	def assert_auth_nas_ip_addr_error(self,assert_error=None):
		'''
		Asserts Auth Server NAS Ip Address error  
		'''	
		if assert_error == None:
			if  self.auth_nas_ip_addr_error:
				raise AssertionError("Invalid IP Address %s " %traceback.format_exc())
		if assert_error == True:		
			if not self.auth_nas_ip_addr_error:
				raise AssertionError("Accepting Invalid IP Address .Traceback: %s " %traceback.format_exc())
	
	def assert_auth_port_error(self,assert_error=None):
		'''
		Asserts Auth Server auth port error  
		'''	
		if assert_error == None:
			if  self.auth_port_error:
				raise AssertionError("Must be a number in range 1-65534 %s " %traceback.format_exc())
		if assert_error == True:		
			if not self.auth_port_error:
				raise AssertionError("Accepting Invalid range .Traceback: %s " %traceback.format_exc())
	
	def set_drp_ip(self, ip):
		'''
		writing given ip in Drp Ip field
		'''
		logger.debug('Services: Writing Drp ip')
		self.drp_ip.set(ip)
	
	def set_drp_vlan(self, id):
		'''
		writing given id in Drp Vlan field
		'''
		logger.debug('Services: Writing Drp id')
		self.drp_vlan.set(id)
	
	def assert_auth_drp_vlan_error(self,assert_error=None):
		'''
		Asserts Auth Server auth Drp Vlan error  
		'''	
		if assert_error == None:
			if  self.drp_vlan_error:
				raise AssertionError("Must be a number in range 1-4093 %s " %traceback.format_exc())
		if assert_error == True:		
			if not self.drp_vlan_error:
				raise AssertionError("Accepting Invalid range .Traceback: %s " %traceback.format_exc())
	
	def select_tacacs_radio(self):
		'''
		selects default tacacs radio button
		'''
		logger.debug("Services: Clicking on tacacs radio button")
		self.tacacs_radio.click()
	
	def assert_tacacs_name_maxlength_error(self,assert_error=None):
		'''
		Asserts tacacs Name  Maxlength Error
		'''
		if assert_error == None:
			if self.tacacs_name_maxlength_error:
				raise AssertionError("Maximum 32 characters allowed.Traceback: %s " %traceback.format_exc())
		if assert_error == True:
			if not self.tacacs_name_maxlength_error:
				raise AssertionError("Auth tacacs Name textbox is Accepting more than 32 characters allowed.Traceback: %s " %traceback.format_exc())
	
	def assert_tacacs_Sharedkey_error(self,assert_error=None):
		'''
		Asserts Auth Server tacacs SharedKey  Error
		'''	
		if assert_error == None:
			if  self.tacacs_Sharedkey_error:
				raise AssertionError("Length must be 2-64 characters.Traceback: %s " %traceback.format_exc())
		if assert_error == True:		
			if not self.tacacs_Sharedkey_error:
				raise AssertionError("Accepting Invalid value for SharedKey.Traceback: %s " %traceback.format_exc())
	
	def assert_tacacs_auth_port_error(self,assert_error=None):
		'''
		Asserts tacacs Auth port Error
		'''	
		if assert_error == None:
			if  self.tacacs_auth_port_error:
				raise AssertionError("Must be a number in range 1-65534 %s " %traceback.format_exc())
		if assert_error == True:		
			if not self.tacacs_auth_port_error:
				raise AssertionError("Accepting Invalid range .Traceback: %s " %traceback.format_exc())
	
	def assert_tacacs_timeout_error(self,assert_error=None):
		'''
		Asserts Server tacacs Timeout error  
		'''	
		if assert_error == None:
			if  self.auth_tacacs_timeout_error:
				raise AssertionError("Must be a number in range 1-30: %s " %traceback.format_exc())
		if assert_error == True:		
			if not self.auth_tacacs_timeout_error:
				raise AssertionError("Accepting Invalid Timeout .Traceback: %s " %traceback.format_exc())
	
	def assert_auth_ipaddr_tacacs_error(self,assert_error=None):
		'''
		Asserts Auth Server tacacs Ip Address error  
		'''	
		if assert_error == None:
			if  self.auth_ipaddr_tacacs_error:
				raise AssertionError("Invalid IP Address %s " %traceback.format_exc())
		if assert_error == True:		
			if not self.auth_ipaddr_tacacs_error:
				raise AssertionError("Accepting Invalid IP Address .Traceback: %s " %traceback.format_exc())
	
	def assert_tacacs_retry_count_error(self,assert_error=None):
		'''
		Asserts Auth Server tacacs Retry Count error  
		'''	
		if assert_error == None:
			if  self.tacacs_retry_count_error:
				raise AssertionError("Must be a number in range 1-5: %s " %traceback.format_exc())
		if assert_error == True:		
			if not self.tacacs_retry_count_error:
				raise AssertionError("Accepting Invalid Retry Count .Traceback: %s " %traceback.format_exc())
	
	def validate_server_radio_fields(self):
		conf=self.config.config_vars
		self.set_new_server_name(conf.invalid_value_2)
		self.set_new_server_ip(conf.invalid_cppm_server_ip)
		self.set_new_server_shared_key(conf.invalid_value_3)
		self.set_new_server_retype_shared_key(conf.invalid_value_3)
		self.set_timeout(conf.invalid_timeout)
		self.set_retrycount(conf.invalid_retry_count)
		self.set_auth_port(conf.invalid_coa_port)
		self.set_nas_ip_address(conf.invalid_nas_ip)

		self.assert_rfc_3576(False)
		self.set_rfc_3576('enable')
		self.save_auth_server()
		self.assert_auth_server_name_maxlength_error(True)
		self.assert_auth_ipaddr_error(True)
		self.assert_auth_Sharedkey_error(True)
		self.assert_auth_timeout_error(True)
		self.assert_auth_retry_count_error(True)
		self.assert_auth_nas_ip_addr_error(True)
		self.assert_auth_port_error(True)

		self.set_accounting_port(conf.invalid_coa_port)
		self.set_new_server_name(conf.cppm_server_name)
		self.set_new_server_ip(conf.Ip_Address)
		self.set_new_server_shared_key(conf.auth_sharedkey_value)
		self.set_new_server_retype_shared_key(conf.auth_sharedkey_value)
		self.set_timeout(conf.dead_time_default)
		self.set_retrycount(conf.dead_time_default)
		self.set_auth_port(conf.auth_port_default)
		self.set_nas_ip_address(conf.Ip_Address1)


		self.save_auth_server()
		self.assert_auth_server_name_maxlength_error()
		self.assert_auth_ipaddr_error()
		self.assert_auth_Sharedkey_error()
		self.assert_auth_timeout_error()
		self.assert_auth_retry_count_error()
		self.assert_auth_nas_ip_addr_error()
		self.assert_auth_port_error()

		self.assert_auth_account_port_error(True)
		self.set_deadtime(conf.calea_mtu_default)
		self.set_drpmask(conf.invalid_aut_netmask)
		self.set_accounting_port(conf.auth_port_default)
		self.save_auth_server()
		self.buy_time()
		self.assert_auth_account_port_error()
		self.assert_deadtime_error(True)
		self.assert_drpmask_error(True)

		self.buy_time()
		self.set_deadtime(conf.dead_time_default)
		self.set_drpmask(conf.valid_netmask)
		self.set_drp_vlan(conf.invalid_auth_vlan_id)
		self.save_auth_server()
		self.assert_deadtime_error()
		self.assert_drpmask_error()
		self.assert_auth_drp_vlan_error(True)
		self.buy_time()
		self.set_drp_vlan(conf.valid_auth_vlan_id)
		self.set_drpmask(conf.invalid_aut_netmask)
		self.buy_time()
		self.save_auth_server()
		self.assert_auth_drp_vlan_error()
		
	def validate_server_tacacs_radio_fields(self):
		conf=self.config.config_vars
		self.select_tacacs_radio()
		self.set_new_server_tacacs_name(conf.invalid_value_2)
		self.set_new_server_tacacs_shared_key(conf.invalid_value_3)
		self.set_new_server_tacacs_retype_shared_key(conf.invalid_value_3)
		self.set_tacacs_auth_port(conf.invalid_coa_port)
		self.set_tacacs_timeout(conf.invalid_timeout)
		self.set_new_server_tacacs_ip(conf.invalid_cppm_server_ip)
		
		self.save_auth_server()
		self.assert_tacacs_name_maxlength_error(True)
		self.assert_tacacs_Sharedkey_error(True)
		self.assert_tacacs_auth_port_error(True)
		self.assert_tacacs_timeout_error(True)
		self.assert_auth_ipaddr_tacacs_error(True)
		
		self.set_new_server_tacacs_name(conf.User_Name_1)
		self.set_new_server_tacacs_shared_key(conf.invalid_value_2)
		self.set_new_server_tacacs_retype_shared_key(conf.invalid_value_2)
		self.set_tacacs_auth_port(conf.Auth_Tacacs_Port_default)
		self.set_tacacs_timeout(conf.dead_time_default)
		self.set_new_server_tacacs_ip(conf.cppm_server_ip)
		self.set_tacacs_retrycount(conf.invalid_retry_count)
		
		self.save_auth_server()
		self.assert_tacacs_name_maxlength_error()
		self.assert_tacacs_Sharedkey_error()
		self.assert_tacacs_auth_port_error()
		self.assert_tacacs_timeout_error()
		self.assert_auth_ipaddr_tacacs_error()
		self.assert_tacacs_retry_count_error(True)
		
		self.set_tacacs_retrycount(conf.retry_count_default)
		self.set_new_server_tacacs_ip(conf.invalid_cppm_server_ip)
		self.buy_time()
		self.save_auth_server()
		self.assert_tacacs_retry_count_error()
	
	def select_auth_coa_only(self):
		'''
		checks the auth coa only
		'''
		logger.debug("Services: Clicking on auth coa only Check box")
		self.auth_coa_only.click()
		
	def assert_airgroup_port_error(self,assert_error=None):
		'''
		Asserts Air Group Port error  
		'''	
		if assert_error == None:
			if  self.airgroup_port_error:
				raise AssertionError("Must be a number in range 1-65534: %s " %traceback.format_exc())
		if assert_error == True:		
			if not self.airgroup_port_error:
				raise AssertionError("Accepting Invalid range .Traceback: %s " %traceback.format_exc())
				
	def validate_server_coa_only_fields(self):
		conf=self.config.config_vars
		self.select_auth_coa_only()
		self.set_new_server_name(conf.invalid_value_2)
		self.set_new_server_ip(conf.invalid_cppm_server_ip)
		self.set_new_server_shared_key(conf.invalid_value_3)
		self.set_new_server_retype_shared_key(conf.invalid_value_3)
		
		self.save_auth_server()
		self.assert_auth_server_name_maxlength_error(True)
		self.assert_auth_ipaddr_error(True)
		self.assert_auth_Sharedkey_error(True)
		
		self.set_new_server_name(conf.User_Name_1)
		self.set_new_server_ip(conf.Ip_Address)
		self.set_new_server_shared_key(conf.invalid_value_2)
		self.set_new_server_retype_shared_key(conf.invalid_value_2)
		self.set_airgroup_port(conf.invalid_coa_port)
		
		self.save_auth_server()
		self.assert_auth_server_name_maxlength_error()
		self.assert_auth_ipaddr_error()
		self.assert_auth_Sharedkey_error()
		self.assert_airgroup_port_error(True)
		
		self.set_airgroup_port(conf.coa_port)
		self.set_new_server_name(conf.invalid_value_2)
		self.save_auth_server()
		self.assert_airgroup_port_error()
		self.cppm_cancel()
		
	def cppm_cancel(self):
		'''
		clicks on Cancel server button
		'''
		logger.debug('Services: clicking on Cancel button')
		self.cppm_cancel_button.click()
		self.buy_time()
		
	def assert_air_group_fields(self):
		logger.debug("Services : checking 'ENABLE AirGroup ACROSS MOBILITY DOMAINS' checkbox...")
		self.browser.assert_element(self.enable_air_mobile_chk, "ENABLE AirGroup ACROSS MOBILITY DOMAINS checkbox is not present")
		logger.debug("Services : checking 'ENABLE AIR PRINT' checkbox...")
		self.browser.assert_element(self.enable_air_print, "ENABLE AIR PRINT checkbox is not present")
		logger.debug("Services : checking 'ENABLE AIR PLAYT' checkbox...")
		self.browser.assert_element(self.enable_air_play, "ENABLE AIR PRINT checkbox is not present")
		logger.debug("Services : checking 'ITUNES' checkbox...")
		self.browser.assert_element(self.itunes, "ITUNES checkbox is not present")
		logger.debug("Services : checking 'ENABLE REMOTE MANAGEMENT' checkbox...")
		self.browser.assert_element(self.enable_remote_mgemt, "ENABLE REMOTE MANAGEMENT checkbox is not present")
		logger.debug("Services : checking 'SHARING' checkbox...")
		self.browser.assert_element(self.enable_sharing, "SHARING checkbox is not present")
		logger.debug("Services : checking 'CHAT' checkbox...")
		self.browser.assert_element(self.enable_chat, "CHAT checkbox is not present")
		logger.debug("Services : checking 'ALLOWALL' checkbox...")
		self.browser.assert_element(self.enable_allowall, "ALLOWALL checkbox is not present")
		
	def assert_analytics_and_location_engine_fields(self):
		'''
		Asserts Fields of analytics and location engine.
		'''
		self.browser.assert_element(self.service_server, "'SERVER' element not found.")
		self.browser.assert_element(self.report_interval_location, "'REPORT INTERNAL' element not found.")
		
	def validate_network_integration_fields(self):
		logger.debug('ServicesPage :Check Enable Feild.')
		self.alto_enable.click()
		self.alto_retype_password.set(self.config.config_vars.invalid_value)
		self.alto_port.set(self.config.config_vars.invalid_alto_port)
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
		if not self.alto_username_error:
			raise AssertionError("Username error message not found i.e. Traceback: %s" %traceback.format_exc())
		if not self.alto_password_error:
			raise AssertionError("Password error message not found i.e. Traceback: %s" %traceback.format_exc())
		if not self.alto_retype_password_error:
			raise AssertionError("Retype Password error message not found i.e. Traceback: %s" %traceback.format_exc())
		if not self.alto_ip_address_error:
			raise AssertionError("IP Addresss error message not found i.e. Traceback: %s" %traceback.format_exc())
		if not self.alto_error:
			raise AssertionError("Port error message not found i.e. Traceback: %s" %traceback.format_exc())
		
	def click_on_cancel(self):
		'''
		Clicks on Cancel button
		'''
		logger.debug("ServicesPage : clicks on calea cancel button. ")
		self.calea_cancel_button.click()
		self.buy_time()

	def set_opendns_username_password(self,user = None,passwd = None):
		'''
		writes user name and password
		'''
		if user:
			logger.debug("ServicesPage : Set Dns Username. ")
			self.dns_username.set(user)
		if passwd:	
			logger.debug("ServicesPage : Set Dns password.")
			self.dns_password.set(passwd)
		logger.debug("ServicesPage : calling save_settings method ")
		self.save_settings()
				
	def assert_override_flag_button(self,check):
		'''
		Asserts Override flag Button
		'''
		if check == 'True':
			self.browser.assert_element(self.override_flag_button_new, 'Ovveride flag button is not present')
		if check == 'False':	
			self.browser.assert_element(self.override_flag_button_new, 'Ovveride flag button is not present', False)	