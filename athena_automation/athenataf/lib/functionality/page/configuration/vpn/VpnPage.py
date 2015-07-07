import logging
logger = logging.getLogger('athenataf')
import traceback
from athenataf.lib.util.WebPage import WebPage
import time

class VpnPage(WebPage):
	def __init__(self, test, browser, config):
		time.sleep(5)
		WebPage.__init__(self, "Vpn", test, browser, config)
		self.test.assertPageLoaded(self)
		
		
	def isPageLoaded(self):
		if self.protocol:
			return True	
		else:
			return False 
			
	def write_in_primary(self):
		logger.debug("VpnPage : Setting Primary text values")
		self.primary_host_textbox.set(self.config.config_vars.primary_text) 

	def write_in_backup(self):
		logger.debug("VpnPage : Setting Backup host values")
		self.backup_host_textbox.set(self.config.config_vars.backup_text)
		
	def revert_settings(self):
		logger.debug("VpnPage : Setting Backup host values to default")
		self.backup_host_textbox.set('')
		logger.debug("VpnPage : Setting Primary text values to default")
		self.primary_host_textbox.set('') 

	def setting_nondefault_values(self):
		logger.debug("VpnPage : Clicking on Preemption ")
		self.preemption.click()
		self.buy_time()
		if not self.preemption.is_selected():
			logger.debug("VpnPage : Clicking on Preemption ")
			self.preemption.click()
		self.browser.key_press(u'\ue00f')
		logger.debug("VpnPage : Setting Hold Time values")
		self.hold_time.set(self.config.config_vars.holdTime)
		logger.debug("VpnPage : Clicking on Fast failover ")
		self.fast_failover.click()
		logger.debug("VpnPage : Setting  secs test packet values")
		self.secs_bet_packet.set(self.config.config_vars.secs_test_packets)
		logger.debug("VpnPage : Setting Max text packet values")
		self.max_text_packet.set(self.config.config_vars.max_text_packet)

	def assert_default_fields(self):
		if self.secs_bet_packet and self.max_text_packet:
			return True
		else:
			raise AssertionError("Exception occured in default fields identification i.e %s and %s. Traceback: %s" % (self.secs_bet_packet, self.max_text_packet, traceback.format_exc()))
			
	def assert_gre_default(self):
		if self.gre_host and self.gre_type and self.gre_tunnel:
			return True
		else:
			raise AssertionError("Exception occured in default fields identification i.e %s and %s and %s. Traceback: %s" % (self.gre_host, self.gre_type, self.gre_tunnel, traceback.format_exc()))
	
	def create_tunnel(self):
		logger.debug("VpnPage :Clicking on create tunnel button")
		self.Create_tunnel.click()

	def setting_tunnel_values(self):
		logger.debug("VpnPage : Writing tunnel name")
		self.profile_name.set(self.config.config_vars.tunnel_name)
		logger.debug("VpnPage : Writing primary adress")
		self.primary_adress.set(self.config.config_vars.primary_add)
		logger.debug("VpnPage : Writing backup address")
		self.backup_address.set(self.config.config_vars.backup_add)
		logger.debug("VpnPage : Writing udp port value")
		self.udp_port.set(self.config.config_vars.local_port)
		logger.debug("VpnPage : Writing local port value")
		self.local_port.set(self.config.config_vars.local_port)
		logger.debug("VpnPage : Writing interval value")
		self.hello_interval.set(self.config.config_vars.interval)
		logger.debug("VpnPage : Setting msg type")
		self.msg_digest.set(self.config.config_vars.msg_type)
		logger.debug("VpnPage : Writing shared key value")
		self.key.set(self.config.config_vars.shared_key)
		logger.debug("VpnPage : Clicking on checksum checkbox")
		self.checksum_checkbox.click()
		self.checksum_checkbox.click()
		logger.debug("VpnPage : Setting vpn failover mode")
		self.failover_mode.set(self.config.config_vars.vpn_failover_mode)
		logger.debug("VpnPage : Writing retry interval value")
		self.failover_retry.set(self.config.config_vars.retry_interval)	
		logger.debug("VpnPage : Writing fail count value")
		self.failover_count.set(self.config.config_vars.fail_count)
		logger.debug("VpnPage : Writing tunnel mtu value")
		self.failover_mtu.set(self.config.config_vars.tunnel_mtu)
		logger.debug("VpnPage : Clicking on save")
		time.sleep(5)
		# self.save_internal.click()
		self.save_internal.click()
		if self.save_internal:
			self.save_internal.click()
		time.sleep(15)
	def assert_tunnel(self):
		if self.tunnel_created :
			return True
		else:
			raise AssertionError("Exception occured in tunnel identification i.e %s . Traceback: %s" % (self.tunnel_created, traceback.format_exc()))
			
	def setting_gre_values(self):
		logger.debug("VpnPage : Writing gre_host value")
		self.gre_host.set(self.config.config_vars.host_gre)
		logger.debug("VpnPage : Writing gre_type value")
		self.gre_type.set(self.config.config_vars.gre_type)	
		logger.debug("VpnPage : Clicking on gre tunnel checkbox")
		self.gre_tunnel.click()
		
	def got_to_vpn_routing(self):
		logger.debug("VpnPage : Clicking on Routing")
		self.routing.click()

	def click_new_route(self):
		logger.debug("VpnPage :Clicking on new Button")
		self.new.click()		

	def add_route(self):
		# if not self.vpn_destination:	
			# self.new.click()
		# self._assert_edit_field_error()
		logger.debug("VpnPage : Writing route destination value")
		self.vpn_destination.set(self.config.config_vars.route_destination)
		logger.debug("VpnPage : Writing route mask value")
		self.vpn_netmask.set(self.config.config_vars.route_mask)
		logger.debug("VpnPage : Writing route gateway value")
		self.vpn_gateway.set(self.config.config_vars.route_gateway)
		logger.debug("VpnPage : Clicking on Routing")
		self.routing.click()		
		logger.debug("VpnPage : Clicking on ok")
		self.ok.click()
		
	def edit_route(self):
		logger.debug("VpnPage : Editing route destination value")
		self.vpn_destination.set(self.config.config_vars.edit_route_destination)
		logger.debug("VpnPage : Writing route mask value")
		self.vpn_netmask.set(self.config.config_vars.route_mask)
		logger.debug("VpnPage : Writing route gateway value")
		self.vpn_gateway.set(self.config.config_vars.edit_route_gateway)	
		logger.debug("VpnPage : Clicking on ok")
		self.ok.click()
		
	def clicking_edit_route(self):
		logger.debug("VpnPage : Editing Route")
		self.netmask.click()
		self.edit.click()	
		
	def delete_route(self):
		logger.debug("VpnPage : Deleting Route")
		self.netmask.click()
		self.delete.click()
		
	def assert_route(self):
		if self.netmask:
			return True
		else:
			raise AssertionError("Exception occured in route identification i.e %s . Traceback: %s" % (self.netmask, traceback.format_exc()))
			
	def assert_edited_route(self):
		if self.edited_gateway:
			return True
		else:
			raise AssertionError("Exception occured in route identification i.e %s . Traceback: %s" % (self.edited_gateway, traceback.format_exc()))
			
	def setting_arubaGre_values(self):
		self.assert_primary_host_test_packets()
		logger.debug("VpnPage : Clicking on Preemption")
		self.preemption.click()
		self.buy_time()
		if not self.preemption.is_selected():
			self.preemption.click()
		self.browser.key_press(u'\ue00f')
		logger.debug("VpnPage : Setting  Hold time values")
		self.hold_time.set(self.config.config_vars.holdTime)
		logger.debug("VpnPage : Clicking on Fast failover ")
		self.fast_failover.click()
		logger.debug("VpnPage : Clicking on Reconnect User on Failover")
		self.reconnect.click()
		logger.debug("VpnPage : Setting  vpn failover time values")
		if not self.vpn_failover:
			self.reconnect.click()
		self.vpn_failover.set(self.config.config_vars.vpn_failover_time)
		logger.debug("VpnPage : Setting  secs test packet values")
		self.secs_bet_packet.set(self.config.config_vars.secs_test_packets)
		logger.debug("VpnPage : Setting  max text packet values")
		self.max_text_packet.set(self.config.config_vars.max_text_packet)
		logger.debug("VpnPage : Clicking on Pre up tunnel")
		self.gre_tunnel.click()
			
	def assert_arubaGre_default(self):
	
		if not self.gre_tunnel.is_selected():
	
			return True
		else:
			raise AssertionError("Exception occured in route identification i.e %s . Traceback: %s" % (self.backup_host_textbox, traceback.format_exc()))	
			
	def save_settings(self):
		logger.debug("VpnPage : Click 'Save Settings' button")
		self.buy_time()
		self.save.click()
		self.buy_time()
		
	def revert_gre_settings(self):
		logger.debug("VpnPage : Clicking on Preemption")
		self.preemption.click()
		self.buy_time()
		if not self.preemption.is_selected():
			self.preemption.click()
		logger.debug("VpnPage : Clicking on Pre up tunnel")
		self.gre_tunnel.click()
		logger.debug("VpnPage : Clicking on Reconnect User on Failover")
		self.reconnect.click()
		logger.debug("VpnPage : Clicking on Fast failover ")
		self.fast_failover.click()
		logger.debug("VpnPage : Setting Backup host values to default")
		self.backup_host_textbox.set('')
		logger.debug("VpnPage : Setting Primary host values to default")
		self.primary_host_textbox.set('')

	def buy_time(self):
		import time
		time.sleep(5) 
		
	def handle_save_alert(self):
		if self.save_pop_up:
			logger.debug("VpnPage : clicking on save button")
			self.save_pop_up.click()
			self.LeftPanel.go_to_vpn()
			
	
	def assert_fields(self):
		import traceback
		if self.preemption.is_selected():
			raise AssertionError("VPN :Preemption is checked . Traceback: %s" % traceback.format_exc())
		if self.fast_failover.is_selected():
			raise AssertionError("VPN :Fast Failover is checked . Traceback: %s" % traceback.format_exc()) 
		if self.reconnect.is_selected():
			raise AssertionError("VPN :Reconnect User on Failover is checked . Traceback: %s" % traceback.format_exc())
		
	def set_primary_backup_host_default_values(self):
		logger.debug("VpnPage : Setting Backup host values to default")
		self.backup_host_textbox.set('')
		logger.debug("VpnPage : Setting Primary host values to default")
		self.primary_host_textbox.set('')
		
	def set_vpn_controller_default_values(self): # not used
		self.gre_host.set(self.config.config_vars.host_gre)
		self.gre_type.set(self.config.config_vars.gre_type)	
		logger.debug("VpnPage : clicking gre tunnel")
		self.gre_tunnel.click()
		
	def assert_edit_route_fields(self):
		import traceback
		if not self.edit_route_label:
			raise AssertionError("VPN :Edit route label is not visible . Traceback: %s" % traceback.format_exc())
		if not self.vpn_destination:
			raise AssertionError("VPN :Destination textbox is not visible . Traceback: %s" % traceback.format_exc())
		if not self.vpn_netmask:
			raise AssertionError("VPN :Netmask textbox is not visible . Traceback: %s" % traceback.format_exc())
		if not self.vpn_gateway:
			raise AssertionError("VPN :Gateway textbox is not visible . Traceback: %s" % traceback.format_exc())
		
	def assert_primary_host_test_packets(self):
		import traceback
		self.write_in_primary()
		logger.debug("VpnPage : Setting secs between packets field to zero")
		self.secs_bet_packet.set('0')
		self.save_settings()
		if not self.secs_bet_packet_error:
			raise AssertionError("VPN :Test packet error is not visible . Traceback: %s" % traceback.format_exc())
		logger.debug("VpnPage : Setting max text packets to zero")
		self.max_text_packet.set('0')
		self.save_settings()
		if not self.max_text_packet_error:
			raise AssertionError("VPN :Max allowed test packet error is not visible . Traceback: %s" % traceback.format_exc())
	
	def set_checkbox_default_values(self):
		logger.debug("VpnPage : Clicking on Pre-emption checkbox")
		if self.preemption.is_selected():
			self.preemption.click()
		logger.debug("VpnPage : Clicking on Reconnect User on Failover")
		if self.fast_failover.is_selected():
			self.fast_failover.click()
		logger.debug("VpnPage : Clicking on Fast failover ")
		if self.reconnect.is_selected():
			self.reconnect.click()
	
	# def _assert_edit_field_error(self):
		# import traceback
		# self.vpn_destination.set('0')
		# logger.debug('VpnPage : Clicking on new route label')
		# self.new_route.click()		
		# if not self.destination_error_msg:
			# raise AssertionError("VPN :Invalid destination error is not visible . Traceback: %s" % traceback.format_exc())
		# self.vpn_netmask.set('0')
		# logger.debug('VpnPage : Clicking on new route label')
		# self.new_route.click()
		# if not self.netmask_error_msg:
			# raise AssertionError("VPN :Invalid netmask error is not visible . Traceback: %s" % traceback.format_exc())
		# self.vpn_gateway.set('0')
		# logger.debug('VpnPage : Clicking on new route label')
		# self.new_route.click()
		# if not self.gateway_error_msg:
			# raise AssertionError("VPN :Invalid gateway error is not visible . Traceback: %s" % traceback.format_exc())
		# self.cancel_button.click()
		
	def _assert_edit_field_error(self):
		import traceback
		logger.debug("VpnPage : Writing destination ip ")
		self.vpn_destination.set('1.1.1')
		logger.debug("VpnPage : Writing netmask")
		self.vpn_netmask.set('2.2.2')
		logger.debug("VpnPage : Writing gateway")
		self.vpn_gateway.set('0')
		logger.debug("VpnPage : Writing destination ip ")
		self.vpn_destination.set('1.1.1')		
		if not self.destination_error_msg:
			raise AssertionError("VPN :Invalid destination error is not visible . Traceback: %s" % traceback.format_exc())
		
		if not self.netmask_error_msg:
			raise AssertionError("VPN :Invalid netmask error is not visible . Traceback: %s" % traceback.format_exc())
		
		if not self.gateway_error_msg:
			raise AssertionError("VPN :Invalid gateway error is not visible . Traceback: %s" % traceback.format_exc())
		# self.cancel_button.click()
	
	def assert_tunnel_config_error(self):
		import traceback
		logger.debug("VpnPage : Writing primary address ")
		self.primary_adress.set('0')
		logger.debug("VpnPage : Writing backup address ")
		self.backup_address.set('0')
		logger.debug("VpnPage : Writing udp port ")
		self.udp_port.set('0')
		logger.debug("VpnPage : Writing local port ")
		self.local_port.set('0')
		logger.debug("VpnPage : Writing hello interval ")
		self.hello_interval.set('0')
		logger.debug("VpnPage : Writing failover retry  ")
		self.failover_retry.set('0')
		logger.debug("VpnPage : Writing failover retry count ")
		self.failover_count.set('6')
		logger.debug("VpnPage : Writing failover mtu ")
		self.failover_mtu.set('0')
		logger.debug("VpnPage : Clicking save button ")
		self.save_internal.click()	
		import time
		time.sleep(8)
		if not self.primary_peer_error_msg:
			raise AssertionError("VPN :Primary peer address accepting invalid values . Traceback: %s" % traceback.format_exc())
		
		if not self.backup_peer_error_msg:
			raise AssertionError("VPN :Backup peer address accepting invalid values. Traceback: %s" % traceback.format_exc())
		
		if not self.peer_udp_port_error_msg:
			raise AssertionError("VPN :peer udp port accepting invalid values . Traceback: %s" % traceback.format_exc())
		
		if not self.local_udp_port_error_msg:
			raise AssertionError("VPN :local udp port accepting invalid values. Traceback: %s" % traceback.format_exc())
		
		if not self.hello_interval_error_msg:
			raise AssertionError("VPN :hello interval accepting invalid values. Traceback: %s" % traceback.format_exc())
		
		if not self.failover_interval_error_msg:
			raise AssertionError("VPN :failover interval accepting invalid values. Traceback: %s" % traceback.format_exc())		
		
		if not self.failover_count_error_msg:
			raise AssertionError("VPN :failover count accepting invalid values. Traceback: %s" % traceback.format_exc())
		
		if not self.mtu_error_msg:
			raise AssertionError("VPN :mtu accepting invalid values. Traceback: %s" % traceback.format_exc())
		
	def create_assert_session(self):
		import traceback
		logger.debug("VpnPage : Clicking on new session button ")
		self.create_new_session_button.click()
		logger.debug("VpnPage : Clicking save button ")
		self.session_save_button.click()
		logger.debug("VpnPage : Writing session name")
		self.session_profile_name.set(self.config.config_vars.session_name)
		logger.debug("VpnPage : Writing session ip")
		self.session_tunnel_ip_addr.set('0')
		logger.debug("VpnPage : Session : Clicking save button ")
		self.session_save_button.click()
		if not self.session_tunnel_ip_error:
			raise AssertionError("VPN :Invalid IP address format message is not visible . Traceback: %s" % traceback.format_exc())
		logger.debug("VpnPage : Writing session ip")
		self.session_tunnel_ip_addr.set(self.config.config_vars.valid_session_ip_adress)
		
		logger.debug("VpnPage : Writing session netmask")
		self.session_tunnel_netmask.set('0')
		self.buy_time()
		logger.debug("VpnPage : Clicking save button ")
		self.session_save_button.click()
		self.buy_time()
		if self.session_save_button:
			self.session_save_button.click()
		self.buy_time()
		if not self.session_tunnel_netmask_error:
			raise AssertionError("VPN :Invalid netmask format message is not visible . Traceback: %s" % traceback.format_exc())
		logger.debug("VpnPage : Writing session netmask")
		self.session_tunnel_netmask.set(self.config.config_vars.valid_session_netmask)
		
		logger.debug("VpnPage : Writing session tunnel vlan")
		self.session_tunnel_vlan.set('1')
		logger.debug("VpnPage : Clicking save button ")
		self.session_save_button.click()
		if not self.session_tunnel_val_error:
			raise AssertionError("VPN : Tunnel vlan value is out of range . Traceback: %s" % traceback.format_exc())
		logger.debug("VpnPage : Writing session tunnel vlan")
		self.session_tunnel_vlan.set(self.config.config_vars.valid_session_vlan)
		
		# self.session_cookie_lenght.set('0')
		# if not self.disabled_cookie :
			# raise AssertionError("Cookie is enabled .Traceback: %s " %traceback.format_exc())
		
		logger.debug("VpnPage : Writing session cookie length")
		self.session_cookie_lenght.set('4')
		logger.debug("VpnPage : Clicking save button ")
		self.session_save_button.click()
		logger.debug("VpnPage : Writing session cookie ")
		self.session_cookie.set('1')
		if not self.session_cookie_error:
			raise AssertionError("VPN : Cookie is without 8 hex char . Traceback: %s" % traceback.format_exc())
		logger.debug("VpnPage : Writing session cookie ")
		self.session_cookie.set(self.config.config_vars.cookie_field_4)
		
		logger.debug("VpnPage : Writing session cookie length")
		self.session_cookie_lenght.set('8')
		logger.debug("VpnPage : Writing session cookie ")
		self.session_cookie.set('1')
		logger.debug("VpnPage : Clicking save button ")
		self.session_save_button.click()
		if not self.session_cookie_error:
			raise AssertionError("VPN : Cookie is without 8 hex char . Traceback: %s" % traceback.format_exc())
		logger.debug("VpnPage : Writing session cookie ")
		self.session_cookie.set(self.config.config_vars.cookie_field_8)
		
		logger.debug("VpnPage : Writing session remote end id ")
		self.session_remote_end_id.set('c')
		logger.debug("VpnPage : Clicking save button ")
		self.session_save_button.click()
		# self.session_save_button.click()
		if not self.session_remote_id_end_error:
			raise AssertionError("VPN : Remote end id is taking charecter . Traceback: %s" % traceback.format_exc())
		self.session_remote_end_id.set(self.config.config_vars.valid_session_remote_end_id)
		
		# self.session_save_button.click()
		# self.save.click()
		# import time
		# time.sleep(8)
		
	def delete_session(self):
		logger.debug("VpnPage : Deleting Session ")
		self.session_profile_list_name.click()
		logger.debug("VpnPage : Clicking on delete button ")
		self.session_name_delete_button.click()
		logger.debug("VpnPage : Clicking save button ")
		self.save.click()
		import time
		time.sleep(8)
		
	def restore_Ipsec_default(self):
		logger.debug("VpnPage : Selecting Aruba IPSec ")
		self.protocol.set(self.config.config_vars.vpn_def_protocol)
		self.buy_time()
		self.save_settings()
		
	def restore_manual_GRE_default(self):
		logger.debug("VpnPage : Resetting  gre-host values")
		self.gre_host.set('')
		logger.debug("VpnPage : Resetting  gre-type values")
		self.gre_type.set('')
		logger.debug("VpnPage : Clicking on Pre up tunnel")
		if self.gre_tunnel.is_selected():
			self.gre_tunnel.click()
		self.restore_Ipsec_default()
		
			
	def assert_Ipsec_default(self):
		logger.debug("VpnPage : Selecting Aruba IPSec ")
		self.protocol.set(self.config.config_vars.vpn_def_protocol)
		self.buy_time()
		if self.primary_host1 and self.backup_host:
			return True
		else:
			raise AssertionError("Primary host and backup host feilds not found  .Traceback: %s " %traceback.format_exc())

	def assert_aruba_gre_default(self):
		if not (self.primary_host1 and self.backup_host and self.gre_tunnel1):
			raise AssertionError("Primary host and backup host and gre tunnel feilds not found .Traceback: %s " %traceback.format_exc())
		if self.gre_tunnel.is_selected():
			raise AssertionError("per-ap-tunnel is enabled .Traceback: %s " %traceback.format_exc())
		
	def assert_L2TPv3_default(self):
		self.buy_time()
		if self.create_tunnel1 and self.create_session:
			return True
		else:
			raise AssertionError("new tunnel button is not enabled or new session button is not disabled.Traceback: %s " %traceback.format_exc())

	def assert_manual_gre_default(self):
		if self.gre_host and self.gre_type and self.gre_tunnel:
			return True
		else:
			raise AssertionError(" gre host and gre type and gre tunnel feilds not found.Traceback: %s " %traceback.format_exc())
			

	def cancel_click(self):
		logger.debug("VpnPage : Clicking on Session Cancel button ")
		self.session_cancel_button.click()
		import time
		time.sleep(8)
		
	def save_session_click(self):
		logger.debug("VpnPage : Clicking on Session Save button ")
		self.session_save_button.click()
		if self.session_save_button:
			self.session_save_button.click()
		logger.debug("VpnPage : Clicking on Session Save button ")
		self.save.click()
		import time
		time.sleep(8)

	def configure_IPSec_default(self):
		logger.debug("VpnPage : Clicking on Pre up tunnel")
		if not self.preemption.is_selected():
			self.preemption.click()
		self.buy_time()
		if not self.preemption.is_selected():
			self.preemption.click()
		logger.debug("VpnPage : Clicking on Fast failover ")
		self.fast_failover.click()
		if not self.fast_failover.is_selected():
			self.fast_failover.click()
		self.browser.key_press(u'\ue00f')
		logger.debug("VpnPage : Setting Hold Time values")
		self.hold_time.set(self.config.config_vars.holdTime)
		logger.debug("VpnPage : Clicking on Reconnect User on Failover")
		self.reconnect.click()
		self.buy_time()
		if not self.reconnect.is_selected():
			self.reconnect.click()
		logger.debug("VpnPage : Setting  vpn failover time values")
		self.vpn_failover.set(self.config.config_vars.vpn_failover_time)
		logger.debug("VpnPage : Setting  secs test packet values")
		self.secs_bet_packet.set(self.config.config_vars.secs_test_packets)
		logger.debug("VpnPage : Setting Max text packet values")
		self.max_text_packet.set(self.config.config_vars.max_text_packet)
		
	def assert_IPSec_fields(self):
		import traceback
		if not self.preemption.is_selected():
			raise AssertionError("VPN :Preemption is unchecked . Traceback: %s" % traceback.format_exc())
		if not self.fast_failover.is_selected():
			raise AssertionError("VPN :Fast Failover is unchecked . Traceback: %s" % traceback.format_exc()) 
		if not self.reconnect.is_selected():
			raise AssertionError("VPN :Reconnect User on Failover is unchecked . Traceback: %s" % traceback.format_exc())
			
	def	enable_preup_tunnel(self):
		logger.debug("VpnPage : Enabling Pre-tunnel ")
		self.gre_tunnel.click()
		
	def	assert_primary_backup_address(self):
		import traceback
		logger.debug("VpnPage : Writing primary host  ")
		self.primary_host_textbox.set('abc123.*')
		self.save_settings()
		if not self.primary_add_error:
			raise AssertionError("VPN :Primary address feild accepting invalid values. Traceback: %s" % traceback.format_exc())
		self.backup_host_textbox.set('abc123.*')
		self.save_settings()
		if not self.backup_add_error:
			raise AssertionError("VPN :Backup address feild accepting invalid values . Traceback: %s" % traceback.format_exc())
		
	def assert_IPsec_parameters_fields(self):
		import traceback
		logger.debug("VpnPage : Writing primary host  ")
		self.primary_host_textbox.set('abc123.*')
		logger.debug("VpnPage : Writing backup host  ")
		self.backup_host_textbox.set('abc123.*')
		self.save_settings()
		if not self.primary_add_error:
			raise AssertionError("VPN :Primary address feild accepting invalid values. Traceback: %s" % traceback.format_exc())
		self.save_settings()
		if not self.backup_add_error:
			raise AssertionError("VPN :Backup address feild accepting invalid values . Traceback: %s" % traceback.format_exc())
		logger.debug("VpnPage : clicking preemption checkbox")
		self.preemption.click()
		self.buy_time()
		if not self.preemption.is_selected():
			self.preemption.click()
		self.browser.key_press(u'\ue00f')
		logger.debug("VpnPage : clicking fast failover")
		self.fast_failover.click()
		logger.debug("VpnPage : Writing hold time  ")
		self.hold_time.set('abv')
		self.save_settings()
		if not self.hold_time_error:
			raise AssertionError("VPN :Hold Time feild accepting values beyond specified range. Traceback: %s" % traceback.format_exc())
		logger.debug("VpnPage : Writing secs betwen packet  ")
		self.secs_bet_packet.set('3601')
		self.save_settings()
		if not self.secs_bet_packet_error:
			raise AssertionError("VPN :Secs between test packets feild accepting values beyond specified range. Traceback: %s" % traceback.format_exc())
		logger.debug("VpnPage : Writing max text packet  ")
		self.max_text_packet.set('0')
		self.save_settings()
		if not self.max_text_packet_error:
			raise AssertionError("VPN :Max allowed test packet loss feild accepting values beyond specified range . Traceback: %s" % traceback.format_exc())
		logger.debug("VpnPage : clicking preemption checkbox")
		self.preemption.click()
		self.buy_time()
		if not self.preemption.is_selected():
			self.preemption.click()
		logger.debug("VpnPage : clicking fast failover checkbox")
		self.fast_failover.click()
		# self.reconnect.click()
			
	def assert_manual_gre_parameters_fields(self):
		import traceback
		logger.debug("VpnPage : Writing gre host")
		self.gre_host.set('abc123.*')
		logger.debug("VpnPage : Writing gre host")
		self.gre_type.set('abc')
		if self.gre_tunnel.is_selected():
			raise AssertionError("VPN :Per ap tunnel is enabled. Traceback: %s" % traceback.format_exc())
		self.save_settings()
		if not self.gre_type_error:
			raise AssertionError("VPN :Gre type feild accepting invalid values . Traceback: %s" % traceback.format_exc())
				
	def assert_default_manual_gre(self):
		logger.debug("VpnPage : Writing protocol")
		self.protocol.set(self.config.config_vars.vpn_gre_protocol)
		self.buy_time()
		if not self.gre_host.get() == '':
			raise AssertionError("VPN : HOST Value is not set to Default. Traceback: %s" % traceback.format_exc())
		if not self.gre_type.get() == self.config.config_vars.default_gre_type:
			raise AssertionError("VPN : GRE TYPE Value is not set to its Default value 1. Traceback: %s" % traceback.format_exc())
		if self.gre_tunnel.is_selected():
			raise AssertionError("VPN : PER-AP-TUNNEL checkbox is checked. Traceback: %s" % traceback.format_exc())
			
	def assert_secs_between_test_packets(self):
		'''
		asserts the default value of secs between test packets is set to 5
		'''
		if not self.secs_bet_packet.get() == '5' :
			raise AssertionError('VPNPage : Secs between packet is not set to default value')
		else:
			pass

	def assert_max_text_packet_loss(self):
		'''
		checks whether max text packet loss is set to default value
		'''
		if not self.max_text_packet.get() == '2':
			raise AssertionError('VPNPage :  max text packet loss is not set to default value')
		else:
			pass
	
	def set_primary_host_field(self, value, correct):
		'''
		writes given value into primary host fields and asserts if its invalid input
		'''
		logger.debug("VPNPage : Writting primary host field")
		self.primary_host_textbox.set(value)
		# self.browser.key_press(u'\ue004')
		self.save_settings()
		if correct == 'true':
			if not self.primary_add_error : 
				raise AssertionError('VPNPage: Inavlid ip address message is not displayed ')
		else :
			if self.primary_add_error :
				raise AssertionError('VPNPage: Inavlid ip address message is displayed for valid ip address')

	def set_secs_between_test_packets(self,value,correct):
		'''
		writes given value into secs between test packets field and asserts for invalid value
		'''
		logger.debug("VPNPage : Writting primary host field")
		self.secs_bet_packet.set(value)
		self.save_settings()
		if correct == 'true':
			if not self.secs_bet_packet_error:
				raise AssertionError('VPNPage : Must be a number in range 1 - 3600 error is not displayed')
		else :
			if self.secs_bet_packet_error :
				raise AssertionError('VPNPage: Must be a number in range 1 - 3600 error is displayed')
				
	def set_max_allowed_test_packets_loss(self,value,correct):
		'''
		writes given value into max allowed test packets loss field and asserts for invalid value
		'''
		logger.debug("VPNPage : Writting primary host field")
		if value == '':
			self.max_text_packet.set(value)
			self.save_settings()
			if not self.max_text_packet.get() == '0' :
				raise AssertionError("VPNPage : max allowed test packets loss field is not set to zero ")
		else :		
			logger.debug("VPNPage : Writting primary host field")
			self.max_text_packet.set(value)
			self.save_settings()
			if correct == 'true':
				if not self.max_text_packet_error:
					raise AssertionError('VPNPage : Must be a number in range 1 - 3600 error is not displayed')
			else :
				if self.max_text_packet_error :
					raise AssertionError('VPNPage: Must be a number in range 1 - 3600 error is displayed')
					
	def set_backup_host(self, value, correct):
		'''
		writes given value into primary host fields and asserts if its invalid input
		'''
		logger.debug("VPNPage : Writing primary host field")
		self.backup_host_textbox.set(value)
		self.save_settings()
		if correct == 'true':
			if not self.backup_add_error : 
				raise AssertionError('VPNPage: Inavlid ip address message is not displayed ')
		else :
			if self.backup_add_error :
				raise AssertionError('VPNPage: Inavlid ip address message is displayed for valid ip address')
	
	def assert_backhost_fields(self):
		'''
		checks whether preemption , fast failover ,reconnect user on fail over check box
		'''
		if not self.preemption and not self.fast_failover and not self.reconnect :
			raise AssertionError("VPNPage : Preemption , Fast fail over and Reconnect user on fail over  is not displayed")
			
	def set_premption(self, check):
		'''
		checks or unchecks the preemption checkbox
		'''
		if check == 'true':
			if not self.preemption.is_selected() :
				logger.debug('Clicking on preemption checkbox')
				self.preemption.click()
		else :
			if self.preemption.is_selected() :
				logger.debug('Clicking on preemption checkbox')
				self.preemption.click()
	
	def set_hold_time(self,time):
		'''
		writes given time into hold time field
		'''
		logger.debug('Writing into hold time field')
		self.hold_time.set(time)
	
	def assert_hold_time_field_default_value(self):
		'''
		asserts hold time field default value
		'''
		if not self.hold_time.get() == self.config.config_vars.hold_time_default_value :
			raise AssertionError("VPNPage : Hold time is not set to default  value")
		

	def assert_hold_time_field(self,value):
		'''
		asserts fr hold time field error message
		'''
		if value == 'true':
			if not self.hold_time_error:
				raise AssertionError("VPNPage : Inavalid error message is not displayed")
		else :
			if self.hold_time_error:
				raise AssertionError("VPNPage : Valid hold time is not accepted")

	def set_reconnect_user_on_failover(self,check):
		'''
		clicks on reconnect user on failover checkbox
		'''
		if check == 'true':
			if not self.reconnect.is_selected() :
				logger.debug('Clicking on preemption checkbox')
				self.reconnect.click()
		else :
			if self.reconnect.is_selected() :
				logger.debug('Clicking on preemption checkbox')
				self.reconnect.click()

	def assert_reconnect_time_on_failover_field_default_value(self):
		'''
		asserts hold time field default value
		'''
		if not self.vpn_failover.get() == self.config.config_vars.recnnect_default_value :
			raise AssertionError("VPNPage : Hold time is not set to default  value")
	
	def set_reconnect_time_on_failover(self,value):
		'''
		writes into reconnect time on fail over field
		'''
		logger.debug('writing into reconnect time on fail over field')
		self.vpn_failover.set(value)
		
	def assert_reconnect_time_on_failover_field(self, value):
		'''
		asserts for reconnect time on fail over field error message
		'''
		if value == 'true':
			if not self.reconnect_time_failover_error:
				raise AssertionError("VPNPage : Inavalid error message is not displayed")
		else :
			if self.reconnect_time_failover_error:
				raise AssertionError("VPNPage : Valid hold time is not accepted")
	
	def set_protocol(self,value):
		'''
		sets given value to Protocol field
		'''
		logger.debug("selecting given value for protocol field")
		self.protocol.set(value)
		
	def set_failover(self,check):
		'''
		clicks on failover checkbox
		'''
		if check == 'true':
			if not self.fast_failover.is_selected() :
				logger.debug('Clicking on preemption checkbox')
				self.fast_failover.click()
		else :
			if self.fast_failover.is_selected() :
				logger.debug('Clicking on preemption checkbox')
				self.fast_failover.click()
	
	def set_manual_gre_host(self,value):
		'''
		writes given value into host field
		'''
		logger.debug('writing into host field')
		self.gre_host.set(value)
		
	def assert_manual_gre_host(self,value):	
		'''
		asserts error message of gre host field
		'''
		if value == 'true':
			if not self.gre_host_error:
				raise AssertionError('Invalid IP or hostname message is not displayed')
		else :
			if self.gre_host_error:
				raise AssertionError('Invalid IP or Hostname message displayed for valid input')

	def set_gre_type(self,value):
		'''
		writes given value into GRE Type field
		'''
		logger.debug('writing into GRE Type field')
		self.gre_type.set(value)
		
	def assert_gre_type_field(self, value):
		'''
		asserts gre type error message
		'''
		if value == 'true':
			if not self.gre_type_error:
				raise AssertionError('Invalid IP or hostname message is not displayed')
		else :
			if self.gre_type_error:
				raise AssertionError('Invalid IP or Hostname message displayed for valid input')
		
	def set_per_ap_tunnel(self,check):
		'''
		clicks on Per-AP-Tunnel checkbox
		'''
		if check == 'true':
			if not self.gre_tunnel.is_selected() :
				logger.debug('Clicking on preemption checkbox')
				self.gre_tunnel.click()
		else :
			if self.gre_tunnel.is_selected() :
				logger.debug('Clicking on preemption checkbox')
				self.gre_tunnel.click()
	
	def assert_per_ap_tunnel(self, check):
		'''
		asserts per ap tunnel checkbox
		'''
		if check == 'true':
			if not self.gre_tunnel.is_selected() :
				raise AssertionError('Per Ap Tunnel checkbox is not selected')
				
		else :
			if self.gre_tunnel.is_selected() :
				raise AssertionError('Per Ap Tunnel checkbox is selected')
	def create_new_session(self):
		'''
		clicks on new session button
		'''
		logger.debug('VPNPage : Clicking on new button')
		self.create_new_session_button.click()
	
	def set_profile_name(self,name):
		'''
		writes given name into profile name field''
		'''
		logger.debug('VpnPage: writing profile name')
		self.session_profile_name.set(name)
		
	def set_tunnel_ip_address(self,ip):
		'''
		writes given tunnel ip address into tunnel ip field
		'''
		logger.debug('VPNPage: Writing tunnel ip address')
		self.session_tunnel_ip_addr.set(ip)
		
	def set_tunnel_netmask(self, netmask):
		'''
		writes given netmask into tunnel netmask field
		'''
		logger.debug('VPNPage: Writing tunnel netmask ')
		self.session_tunnel_netmask.set(netmask)
		
	def set_cookie_length(self, length):
		'''
		writes given netmask into tunnel netmask field
		'''
		if length == '0':
			logger.debug('VPNPage: Setting cookie length 0 ')
			self.session_cookie_lenght.set(self.config.config_vars.zero_cookie_length)
		if length == '4':
			logger.debug('VPNPage: Setting cookie length 4')
			self.session_cookie_lenght.set(self.config.config_vars.four_cookie_length)
		if length == '8':
			logger.debug('VPNPage: Setting cookie length 8')
			self.session_cookie_lenght.set(self.config.config_vars.eight_cookie_length)
			
	def set_cookie(self, cookie):
		'''
		writes cokie length
		'''
		logger.debug('VPNPage: Writing cookie length')
		self.session_cookie.set(cookie)
		
	def set_tunnel_vlan(self, vlan):
		'''
		writes tunnel vlan
		'''
		logger.debug('VPNPage: Writing tunnel vlan')
		self.session_tunnel_vlan.set(vlan)
		
	def delete_created_tunnel(self):
		'''
		deletes newly created tunnel
		'''
		logger.debug('VPNPage: clicking in tunnel')
		self.tunnel_created.click()
		logger.debug('VPNPage: Clicking on delete button')
		self.delete_tunnel.click()
		
	def select_tunnel(self):
		'''
		clicks on created tunnel
		'''
		logger.debug('VPNPage: clicking on created tunnel')
		self.tunnel_created.click()
		
	def set_backup_address(self, ip):
		'''
		writes given ip address into backup address
		'''
		logger.debug('VPNPage : writing backup ip address ')
		self.backup_address.set(ip)
		
	def set_message_digest_type(self,option):
		'''
		sets message digest type
		'''
		logger.debug('VPNPage : selecting message digest type ')
		self.msg_digest.set(option)
		
	def set_shared_key(self, shared_key):
		'''
		sets shared key
		'''
		logger.debug('VPNPage : writing shared key ')
		self.key.set(shared_key)
		
	def save_tunnel_settings(self):
		'''
		clicks on save button
		'''
		logger.debug('VPNPage : clicking on save button')
		self.save_internal.click()
		
	def assert_failover_retry_count(self):
		'''
		asserts for failover retry count error message
		'''
		if not self.failover_retry_count_error_msg :
			raise AssertionError('Must be a number in range 1 - 5 message is not displayed')
			
	def set_failover_retry_count(self, count):
		'''
		writes fail over retry count
		'''
		logger.debug('VPNPage : writing failover retry count ')
		self.failover_count.set(count)
		
	def select_session_profile(self):
		'''
		selects created session
		'''
		logger.debug('Clicking on created session profile')
		self.session_profile_list_name.click()
	
	def set_session_remote_end_id(self, id):
		'''
		writes session remote end id
		'''
		logger.debug('Writing session remote end id')
		self.session_remote_end_id.set(id)
	
	def assert_profile_name_validation_error_message(self,value):
		'''
		asserts profile name error message
		'''
		if value =='invalid':  
			if not self.tunnel_name_req_error:
				raise AssertionError("VPN : L2TPV3 : Profile name validation error is not displayed")
		else :
			if self.tunnel_name_req_error:
				raise AssertionError("VPN : L2TPV3 : Profile name validation error is displayed for valid input")

	def assert_primary_peer_validation_error_message(self,value):
		'''
		asserts Primary peer address error message
		'''
		if value =='invalid':  
			if not self.invalid_primary_peer_ip_error:
				raise AssertionError("VPN : L2TPV3 : Primary peer validation error is not displayed")
		else :
			if self.invalid_primary_peer_ip_error:
				raise AssertionError("VPN : L2TPV3 : Primary peer validation error is displayed for valid input")

	def assert_shared_key_validation_error_message(self,value):
		'''
		asserts shared_key error message
		'''
		if value =='invalid':  
			if not self.shared_key_req_error:
				raise AssertionError("VPN : L2TPV3 : Shared key validation error is not displayed")
		else :
			if self.shared_key_req_error:
				raise AssertionError("VPN : L2TPV3 : shared key validation error is displayed for valid input")
				
				
	def set_tunnel_profile_name(self, name):
		'''
		writes tunnel profile name
		'''
		logger.debug('VpnPage: writing profile name')
		self.profile_name.set(name)
		
	def set_tunnel_primary_adress(self,ip):
		'''
		writes tunnel primary peer ip
		'''
		logger.debug('VpnPage: L2TPV3 :writing primary peer address')
		self.primary_adress.set(ip)
				
	def set_local_udp_port(self,port):
		'''
		writes local udp port
		'''
		logger.debug('VpnPage: L2TPV3 :writing local udp port')
		self.local_port.set(port)
		
	def set_peer_udp_port(self,port):
		'''
		writes peer udp port
		'''
		logger.debug('VpnPage: L2TPV3 :writing peer udp port')
		self.udp_port.set(port)
		
	def set_hello_interval(self,interval):
		'''
		writes hello interval
		'''
		logger.debug('VpnPage: L2TPV3 :writing hello interval')
		self.hello_interval.set(interval)

	def assert_required_fields_of_tunnel(self):
		'''
		asserts error message of required fields of tunnel creation
		'''
		self.assert_profile_name_validation_error_message('invalid')
		self.assert_primary_peer_validation_error_message('invalid')
		self.assert_shared_key_validation_error_message('invalid')
		
	def assert_invalid_backup_peer_ip_address_message(self, value):
		'''
		asserts for invalid ip format error message 
		'''
		if value == 'invalid':
			if not self.backup_peer_error_msg:
				raise AssertionError("VPN :Backup peer address accepting invalid values. Traceback: %s" % traceback.format_exc())
		else:
			if  self.backup_peer_error_msg:
				raise AssertionError("VPN :Backup peer address not accepting valid values. Traceback: %s" % traceback.format_exc())

	def assert_invalid_peer_udp_message(self, value):
		'''
		asserts for 'Must be a number in range 1 - 65534' error message 
		'''
		if value == 'invalid':
			if not self.peer_udp_port_error_msg:
				raise AssertionError("VPN : peer udp port accepting invalid values. Traceback: %s" % traceback.format_exc())
		else:
			if  self.peer_udp_port_error_msg:
				raise AssertionError("VPN :peer udp port not accepting valid values. Traceback: %s" % traceback.format_exc())

	def assert_invalid_local_udp_message(self, value):
		'''
		asserts for 'Must be a number in range 1 - 65534' error message 
		'''
		if value == 'invalid':
			if not self.local_udp_port_error_msg:
				raise AssertionError("VPN : local udp port accepting invalid values. Traceback: %s" % traceback.format_exc())
		else:
			if  self.local_udp_port_error_msg:
				raise AssertionError("VPN :local udp port not accepting valid values. Traceback: %s" % traceback.format_exc())

	def assert_hello_interval_error_message(self, value):
		'''
		asserts for 'Must be a number in range 5 - 300' error message 
		'''
		if value == 'invalid':
			if not self.hello_interval_error_msg:
				raise AssertionError("VPN : hello interval accepting invalid values. Traceback: %s" % traceback.format_exc())
		else:
			if  self.hello_interval_error_msg:
				raise AssertionError("VPN :hello interval not accepting valid values. Traceback: %s" % traceback.format_exc())
				
	def validate_hello_interval_field(self):
		'''
		validates hello interval field
		'''
		conf = self.config.config_vars
		self.set_hello_interval(conf.invalid_zero_input)
		self.save_tunnel_settings()
		self.assert_hello_interval_error_message('invalid')
		self.set_hello_interval(conf.hold_time_default_value)
		self.save_tunnel_settings()
		self.assert_hello_interval_error_message('invalid')	
		self.set_hello_interval(conf.zero_preceding_value)
		self.save_tunnel_settings()
		self.assert_hello_interval_error_message('invalid')
		self.set_hello_interval(conf.alphanumeric)
		self.save_tunnel_settings()
		self.assert_hello_interval_error_message('invalid')
		self.set_hello_interval(conf.valid_gre_type)
		self.save_tunnel_settings()
		self.assert_hello_interval_error_message('valid')

	def assert_shared_key_field(self,visible):
		'''
		asserts for visibility of shared key field
		'''
		if visible == 'True':
			if not self.hello_interval :
				raise AssertionError('VPNPage: Shared key field is not visible')
		else :
			if not self.hello_interval_invisible :
				raise AssertionError('VPNPage: Shared key field is  visible')

	def set_mtu_value(self,value):
		'''
		writes mtu value
		'''
		logger.debug('VpnPage: L2TPV3 :writing mtu value')
		self.failover_mtu.set(value)  

 
	def set_failover_count(self,count_value):
		'''
		writes failover count value
		'''
		logger.debug('VpnPage: L2TPV3 :writing failover_count value')
		self.failover_count.set(count_value) 

	def set_failover_retry(self,retry_value):
		'''
		writes failover retry value
		'''
		logger.debug('VpnPage: L2TPV3 :writing failover_retry value')
		self.failover_retry.set(retry_value)
  
	def set_failover_mode(self,failover_mode):
		'''
		writes failover_mode value
		'''
		logger.debug('VpnPage: L2TPV3 :writing failover_mode value')
		self.failover_mode.set(failover_mode)
  
	def set_checksum(self,value):
		'''
		selecting or deselecting checksum checkbox
		'''
		if value == 'enable':
			if not self.checksum_checkbox.is_selected():
				logger.debug("VpnPage: L2TPV3 :Clicking checksum to Enable ")
				self.checksum_checkbox.click()
		else:
			if self.checksum_checkbox.is_selected():
				logger.debug("VpnPage: L2TPV3 :Clicking checksum to Disable ")
				self.checksum_checkbox.click()
  
	def assert_mtu_error_message(self):
		'''
		Asserting mtu field error message...
		'''
		logger.debug('VpnPage: L2TPV3 : Asserting for mtu error message ')
		if not self.mtu_error_msg : 
			raise AssertionError("VPN : L2TPV3 : MTU error message is not displayed")

	def assert_failover_interval_error_message(self):
		'''
		Asserting failover interval error message...
		'''
		logger.debug('VpnPage: L2TPV3 : Asserting failover interval error message...')
		if not self.failover_interval_error_msg : 
			raise AssertionError("VPN : L2TPV3 : Failover interval error message is not displayed")
				
	def assert_checksum_default_value(self):
		'''
		validates default value of checksum
		'''
		if not self.checksum_checkbox.is_selected():
			raise AssertionError('VPNPage: Checksum checkbox is not enabled by default')

	def assert_failover_mode_default_value(self):
		'''
		validates default value of failover mode
		'''
		if not self.failover_mode.get_selected() == 'Preemptive' :
			raise AssertionError('VPNPage: Failover mode is not set to Preemptive mode by default')
	
	def validate_fail_over_retry_interval(self):
		'''
		validates fail over retry interval
		'''
		conf = self.config.config_vars
		self.set_failover_retry('')
		self.save_tunnel_settings()
		self.assert_failover_interval_error_message()
		self.set_failover_retry(conf.secs_test_packets)		
		self.save_tunnel_settings()
		self.assert_failover_interval_error_message()
		self.set_failover_retry(conf.hold_time_default_value)		
		self.save_tunnel_settings()
		self.assert_failover_interval_error_message()					
		self.set_failover_retry(conf.zero_preceding_value)		
		self.save_tunnel_settings()
		self.assert_failover_interval_error_message()
		self.set_failover_retry(conf.alphanumeric)		
		self.save_tunnel_settings()
		self.assert_failover_interval_error_message()
		self.set_failover_retry(conf.interval)		
		self.save_tunnel_settings()

	def validate_fail_over_retry_count(self):
		'''
		validates fail over retry count
		'''
		self.set_failover_retry('')
		self.save_tunnel_settings()
		self.assert_failover_retry_count()	
		self.set_failover_retry(conf.zero_preceding_value)
		self.save_tunnel_settings()
		self.assert_failover_retry_count()	
		self.set_failover_retry(conf.invalid_coa_port)
		self.save_tunnel_settings()
		self.assert_failover_retry_count()	
		self.set_failover_retry(conf.alphanumeric)
		self.save_tunnel_settings()
		self.assert_failover_retry_count()	
		self.set_failover_retry(conf.valid_session_vlan)
		self.save_tunnel_settings()

	def validate_mtu_field(self):
		'''
		validates mtu field
		'''
		self.set_mtu_value('')
		self.save_tunnel_settings()
		self.assert_mtu_error_message()
		self.set_mtu_value(conf.zero_cookie_length)
		self.save_tunnel_settings()
		self.assert_mtu_error_message()
		self.set_mtu_value(conf.zero_preceding_value)
		self.save_tunnel_settings()
		self.assert_mtu_error_message()
		self.set_mtu_value(conf.alphanumeric)
		self.save_tunnel_settings()
		self.assert_mtu_error_message()
		self.set_mtu_value(conf.invalid_coa_port)
		self.save_tunnel_settings()
		self.assert_mtu_error_message()
		self.set_mtu_value(conf.hold_time_default_value)
		self.save_tunnel_settings()
		
	def configure_l2_specific_sublayer(self,flag=False):
		'''
		check or uncheck default l2 specific sublayer checkbox.
		'''
		if self.l2_sublayer:
			if flag:
				if not self.l2_sublayer.is_selected():
					logger.debug('VpnPage: L2TPV3 : Selecting session l2 sublayer checkbox.  ')
					self.l2_sublayer.click()
			else:
				if self.l2_sublayer.is_selected():
					logger.debug('VpnPage: L2TPV3 : Unchecking session l2 sublayer checkbox.  ')
					self.l2_sublayer.click()
					
					
	def check_multiversion_text_availablility(self):
		logger.debug('VpnPage: L2TPV3 :Checking for multiversion flag msg  ')
		time.sleep(10)
		self.browser.key_press(u'\ue009')
		self.browser.key_press( u'\ue00f')
		actions = self.browser.get_action_chain()
		actions.move_to_element(self.multiversion_msg).perform()
		time.sleep(20)
		if not self.multiversion_msg:
			raise AssertionError(" 'Supported in 6.3.1.2-4.0.0 and above' message is not visible i.e. Traceback: %s" %traceback.format_exc())
			
			
	def assert_multiversion_flag_unavailablility(self):
		time.sleep(20)
		logger.debug('VpnPage: L2TPV3 :Checking for multiversion flag msg  ')
		if self.multiversion_msg:
			raise AssertionError(" 'Supported in 6.3.1.2-4.0.0 and above' message is visible i.e. Traceback: %s" %traceback.format_exc())
			
	def assert_disabled_l2_sublayer(self):
		logger.debug('VpnPage: L2TPV3 :Asserting disabled l2_sublayer  ')
		if not self.disabled_l2_sublayer:
			raise AssertionError(" l2_sublayer field is not disabled  i.e. Traceback: %s" %traceback.format_exc())
			
			
	def assert_session(self):
		logger.debug('VpnPage: L2TPV3 :Asserting session  ')
		if self.created_session :
			return True
		else:
			raise AssertionError("Exception occured in tunnel identification i.e %s . Traceback: %s" % (self.tunnel_created, traceback.format_exc()))
		
	def select_session(self):
		logger.debug('VpnPage: L2TPV3 :Selecting session  ')
		if self.created_session :
			self.created_session.click()

	def assert_multiversion_flag_availablility(self):
		time.sleep(20)
		logger.debug('VpnPage: Checking for multiversion flag ')
		if self.multiversion_msg1:
			raise AssertionError(" 'Supported from 4.0 and above' image is not found i.e. Traceback: %s" %traceback.format_exc())			
			
	def assert_create_new_session_button(self):
		'''
		checking whether the new session Create button is enable or not
		'''
		self.buy_time()
		if not self.create_new_session_button:
			raise AssertionError('New button for the session profile is not enabled')
	
	def assert_session_profile_name_error(self):
		'''
		assert for profile name error
		'''
		self.buy_time()
		if not self.vpn_sp_profile_name_error:
			raise AssertionError('Creating Seesion profile without profile name')
			
	def assert_session_profile_tunnel_ip_error(self,assert_error):
		'''
		assert for session profile IP address invalid format error
		'''
		self.buy_time()
		if assert_error == True:
			if not self.vpn_sp_tp_ip_error:
				raise AssertionError('Accepting invalid IP Address format')		
		if assert_error == False:
			if self.vpn_sp_tp_ip_error:
				raise AssertionError('nvalid IP Address format')	
		
	def assert_session_profile_tunnel_netmask_error(self,assert_error):
		'''
		assert for session profile Netmask  invalid format error
		'''
		self.buy_time()
		if assert_error == True:
			if not self.vpn_sp_tp_ip_error:
				raise AssertionError('Accepting invalid Netmask Address format')	
		if assert_error == False:
			if not self.vpn_sp_tp_ip_error:
				raise AssertionError(' invalid Netmask Address format')	
		
	def get_session_tunnel_name(self,name):
		'''
		get value from textbox Tunnel Profile Name and compare 
		'''
		self.buy_time()
		if not self.session_tunnel_name.get() == name:
			raise AssertionError('Tunnel Profile name is not listed created tunnel profile')	
			
	def assert_session_tunnel_vlan_error(self,assert_error):
		'''
		assert for session profile Netmask  invalid format error
		'''
		self.buy_time()
		if assert_error == True:
			if not self.session_tunnel_vlan_error:
				raise AssertionError('Accepting invalid Tunnel vlan value')	
		if assert_error == False:
			if not self.session_tunnel_vlan_error:
				raise AssertionError(' Must be a number in range 2 - 4094 except 3333')
				
	def validate_session_tunnel_vlan_id(self,vlan,assert_error):
		self.buy_time()
		self.set_tunnel_vlan(vlan)
		self.session_save_button()
		self.assert_session_tunnel_vlan_error(assert_error)
		
	def assert_session_cookie_error_8x(self):
		'''
		Asserts session cookie error
		'''
		if not self.session_cookie_error:
			raise AssertionError('Accepting invalid chars for cookie length 4')
		
	def assert_session_cookie_error_16x(self):
		'''
		Asserts session cookie error
		'''
		if not self.session_cookie_error_16:
			raise AssertionError('Accepting invalid chars for cookie length 8')
			
	def get_session_cookie_length(self,name):
		'''
		get value from Drop-down  cookie length
		'''
		self.buy_time()
		if not self.session_cookie_lenght.get_selected() == name:
			raise AssertionError('Default cookie length "0" is not get selected')			
			
	def assert_session_remote_id_end_error(self,assert_error):
		'''
		assert for session end id error
		'''
		self.buy_time()
		if assert_error == True:
			if not self.session_remote_id_end_error:
				raise AssertionError('Accepting invalid values')	
		if assert_error == False:
			if not self.session_remote_id_end_error:
				raise AssertionError(' Must be in range 1-2147483647')		
	
	def validate_session_remote_end_id(self,id,assert_error):
		self.set_session_remote_end_id(id)
		self.session_save_button()
		self.assert_session_remote_id_end_error(assert_error)	