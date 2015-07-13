import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.util.WebPage import WebPage
from athenataf.lib.test.TestCase import TestCase
import time
import traceback
from athenataf.config import devices
from Device_Module.ObjectModule import Device

class SystemPage(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "System", test, browser, config)
        self.test.assertPageLoaded(self)
        
    def isPageLoaded(self):
        if self.edit_values_ip:
            return True
        else:
            return False 
            
    def _save_settings(self):
        
        time.sleep(3)
        logger.debug("SystemPage : Click 'Save Settings' button")
        if self.save_settings:
            self.save_settings.click()
        time.sleep(4)
            
    def assert_default_values(self):
        test_case = TestCase(self.config)
        path = self.config.config_vars
        
        time.sleep(3)
        logger.debug("SystemPage : asserting the default value of 'TIMEZONE' drop-down")
        test_case.assertEquals(self.timezone.get_selected() , path.timezone_value , "value of 'TIMEZONE' not set to default")
        
        logger.debug("SystemPage : asserting the default value of 'PREFERRED BAND' drop-down")
        test_case.assertEquals(self.preferred_band.get_selected() , path.preferred_band_value , "value of 'PREFERRED BAND' not set to default")
        
        logger.debug("SystemPage : asserting the default value of 'DYNAMIC CPU UTILIZATION' drop-down")
        test_case.assertEquals(self.dynamic_cpu_utilization.get_selected() , path.dynamic_cpu_utilization_value , "value of 'DYNAMIC CPU UTILIZATION' not set to default")
        
        logger.debug("SystemPage : asserting the default value of 'AUTO JOIN MODE' drop-down")
        test_case.assertEquals(self.auto_join_mode.get_selected() , path.auto_join_mode_value , "value of 'AUTO JOIN MODE' not set to default")
        
        logger.debug("SystemPage : asserting the default value of 'TERMINAL ACCESS' drop-down")
        # test_case.assertEquals(self.terminal_access.get_selected() , path.terminal_access_value , "value of 'TERMINAL ACCESS' not set to default")
        
        logger.debug("SystemPage : asserting the default value of 'TELNET SERVER' drop-down")
        test_case.assertEquals(self.telnet_server.get_selected() , path.telnet_server_value , "value of 'TELNET SERVER' not set to default")
        
        logger.debug("SystemPage : asserting the default value of 'LED DISPLAY' drop-down")
        test_case.assertEquals(self.led_display.get_selected() , path.led_display_value , "value of 'LED DISPLAY' not set to default")
        
        logger.debug("SystemPage : asserting the default value of 'EXTENDED SSID' drop-down")
        test_case.assertEquals(self.extended_ssid.get_selected() , path.extended_ssid_value , "value of 'EXTENDED SSID' not set to default")
        
        logger.debug("SystemPage : asserting the default value of 'DENY INTER USING BRIDGING' drop-down")
        test_case.assertEquals(self.deny_inter_using.get_selected() , path.deny_inter_using_value , "value of 'DENY INTER USING BRIDGING' not set to default")
        
        logger.debug("SystemPage : asserting the default value of 'DENY LOCAL ROUTING' drop-down")
        test_case.assertEquals(self.deny_local_routing.get_selected() , path.deny_local_routing_value , "value of 'DENY LOCAL ROUTING' not set to default")
        
        logger.debug("SystemPage : asserting the default value of 'DYNAMIC RADIUS PROXY' drop-down")
        test_case.assertEquals(self.dynamic_radius_proxy.get_selected() , path.dynamic_radius_proxy_value , "value of 'DYNAMIC RADIUS PROXY' not set to default")
        
        logger.debug("SystemPage : asserting the default value of 'MAS INTEGRATION' drop-down")
        test_case.assertEquals(self.mas_integration.get_selected() , path.mas_integration_value , "value of 'MAS INTEGRATION' not set to default")

    def edit_vc_name(self):
        logger.debug("SystemPage : Click 'Edit Values' button")
        self.edit_values_name.click()
        time.sleep(7)
        logger.debug("SystemPage : Clicking on edit icon ")
        self.vc_name_edit_icon.click()
        logger.debug("SystemPage : Write VC name into the text-box")
        self.vc_name_textbox.set(self.config.config_vars.vc_name)
        self.vc_name_textbox.set(self.config.config_vars.vc_name)
        logger.debug("SystemPage : Click 'Save' button")
        self.save_vc_name_id.click()
        time.sleep(3)
        self.save_name.click()
        time.sleep(7)
        # self._save_settings()
        
    def set_default_vc_name(self):
        self.edit_values_name.click()
        logger.debug("SystemPage : Clicking on edit icon ")
        time.sleep(7)
        logger.debug("SystemPage : Clicking on edit icon ")
        self.vc_name_edit_icon.click()
        logger.debug("SystemPage : Write VC name into the text-box")
        self.vc_name_textbox.set(self.config.config_vars.default_vc_name)
        self.vc_name_textbox.set(self.config.config_vars.default_vc_name)
        logger.debug("SystemPage : Click 'Save' button")
        self.save_vc_name_id.click()
        self.save_name.click()
        # self._save_settings()

    def edit_vc_ip(self):
        logger.debug("SystemPage : Click 'Edit Values' button")
        self.edit_values_ip.click()
        time.sleep(5)
        logger.debug("SystemPage : Clicking on edit icon ")
        self.vc_ip_edit_icon.click()
        if not self.vc_ip_textbox:
            self.vc_ip_edit_icon.click()
        logger.debug("SystemPage : Write VC IP into the text-box")
        self.vc_ip_textbox.set(self.config.config_vars.vc_ip)
        self.vc_ip_textbox.set(self.config.config_vars.vc_ip)
        logger.debug("SystemPage : Click 'Save' button")
        self.save_vc_ip_id.click()
        self.save_ip.click()
        
    def set_nondefault_proxy_and_mas(self):
        
        time.sleep(5)
        logger.debug("SystemPage : Set value in 'MAS INTEGRATION' drop-down")
        self.mas_integration.set(self.config.config_vars.mas_integration_new_value)
        logger.debug("SystemPage : Set value in 'DYNAMIC RADIUS PROXY' drop-down")
        self.dynamic_radius_proxy.set(self.config.config_vars.dynamic_radius_proxy_new_value)
        self._save_settings()
        
    def assert_nondefault_proxy_and_mas(self):
        test_case = TestCase(self.config)
        path = self.config.config_vars
        logger.debug("SystemPage : asserting the non default value of 'DYNAMIC RADIUS PROXY' drop-down")
        test_case.assertEquals(self.dynamic_radius_proxy.get_selected() , path.dynamic_radius_proxy_new_value , "value of 'DYNAMIC RADIUS PROXY' not set to non default")
        
        logger.debug("SystemPage : asserting the non default value of 'MAS INTEGRATION' drop-down")
        test_case.assertEquals(self.mas_integration.get_selected() , path.mas_integration_new_value , "value of 'MAS INTEGRATION' not set to non default")
        
    def set_default_proxy_and_mas(self):
        logger.debug("SystemPage : Set value in 'MAS INTEGRATION' drop-down")
        self.mas_integration.set(self.config.config_vars.mas_integration_value)
        logger.debug("SystemPage : Set value in 'DYNAMIC RADIUS PROXY' drop-down")
        self.dynamic_radius_proxy.set(self.config.config_vars.dynamic_radius_proxy_value)
        self._save_settings()
        
    def set_ntp_server_ip(self , state = None):
        
        time.sleep(8)
        logger.debug("SystemPage : Write IP address in 'NTP SERVER' text-box")
        if state == 'wrong':
            self.ntp_server.set(self.config.config_vars.wrong_ntp_server_ip)
        elif state == 'right':
            self.ntp_server.set(self.config.config_vars.right_ntp_server_ip)
        elif state == None:
            self.ntp_server.set('')
        logger.debug("SystemPage : Click 'Save Settings' button")
        self._save_settings()
        time.sleep(8)
            
    def assert_ntp_server_error_msg(self):
        if not self.ntp_server_error_msg:
            raise AssertionError("Error message not found i.e. Traceback: %s" %traceback.format_exc())
            
    def set_dropdown_value_nondefault(self , drop_box_elem):
        path = self.config.config_vars
        
        time.sleep(5)
        if drop_box_elem == 'timezone':
            logger.debug("SystemPage : Set value in 'TIMEZONE' drop-down")
            self.timezone.set(path.timezone_new_value)
        elif drop_box_elem == 'preferred band':
            logger.debug("SystemPage : Set value in 'PREFERRED BAND' drop-down")
            self.preferred_band.set(path.preferred_band_new_value)
        elif drop_box_elem == 'auto join mode':
            logger.debug("SystemPage : Set value in 'AUTO JOIN MODE' drop-down")
            self.auto_join_mode.set(path.auto_join_mode_new_value)
        elif drop_box_elem == 'terminal access':
            logger.debug("SystemPage : Set value in 'TERMINAL ACCESS' drop-down")
            # self.terminal_access.set(path.terminal_access_new_value)
        elif drop_box_elem == 'led display':
            logger.debug("SystemPage : Set value in 'LED DISPLAY' drop-down")
            self.led_display.set(path.led_display_new_value)
        elif drop_box_elem == 'extended ssid':
            logger.debug("SystemPage : Set value in 'EXTENDED SSID' drop-down")
            self.extended_ssid.set(path.extended_ssid_new_value)
        elif drop_box_elem == 'deny inter':
            logger.debug("SystemPage : Set value in 'DENY INTER USING BRIDGING' drop-down")
            self.deny_inter_using.set(path.deny_inter_using_new_value)
        elif drop_box_elem == 'deny local routing':
            logger.debug("SystemPage : Set value in 'DENY LOCAL ROUTING' drop-down")
            self.deny_local_routing.set(path.deny_local_routing_new_value)
        elif drop_box_elem == 'telnet server':
            logger.debug("SystemPage : Set value in 'TELNET SERVER' drop-down")
            self.telnet_server.set(path.sys_enable)
        elif drop_box_elem == 'dynamic cpu utilization disabled':
            logger.debug("SystemPage : Set value in 'DYNAMIC CPU UTILIZATION' drop-down")
            self.dynamic_cpu_utilization.set(path.dynamic_cpu_utilization_disable)
        elif drop_box_elem == 'dynamic cpu utilization enabled':
            logger.debug("SystemPage : Set value in 'DYNAMIC CPU UTILIZATION' drop-down")
            self.dynamic_cpu_utilization.set(path.dynamic_cpu_utilization_enable)
        logger.debug("SystemPage : Click 'Save Settings' button")
        self._save_settings()
        time.sleep(5)
            
    def assert_dropdown_nondefault_value(self , drop_box_elem): 
        test_case = TestCase(self.config)
        path = self.config.config_vars
        if drop_box_elem == 'timezone':
            logger.debug("SystemPage : asserting the non-default value of 'TIMEZONE' drop-down")
            test_case.assertEquals(self.timezone.get_selected() , path.timezone_new_value , "value of 'TIMEZONE' not set to non-default")
        
        elif drop_box_elem == 'preferred band':
            logger.debug("SystemPage : asserting the non-default value of 'PREFERRED BAND' drop-down")
            test_case.assertEquals(self.preferred_band.get_selected() , path.preferred_band_new_value , "value of 'PREFERRED BAND' not set to non-default")
        
        elif drop_box_elem == 'auto join mode':
            logger.debug("SystemPage : asserting the non-default value of 'AUTO JOIN MODE' drop-down")
            test_case.assertEquals(self.auto_join_mode.get_selected() , path.auto_join_mode_new_value , "value of 'AUTO JOIN MODE' not set to non-default")
        
        elif drop_box_elem == 'terminal access':
            logger.debug("SystemPage : asserting the non-default value of 'TERMINAL ACCESS' drop-down")
            # test_case.assertEquals(self.terminal_access.get_selected() , path.terminal_access_new_value , "value of 'TERMINAL ACCESS' not set to non-default")
        
        elif drop_box_elem == 'led display':
            logger.debug("SystemPage : asserting the non-default value of 'LED DISPLAY' drop-down")
            test_case.assertEquals(self.led_display.get_selected() , path.led_display_new_value , "value of 'LED DISPLAY' not set to non-default")
        
        elif drop_box_elem == 'extended ssid':
            logger.debug("SystemPage : asserting the non-default value of 'EXTENDED SSID' drop-down")
            test_case.assertEquals(self.extended_ssid.get_selected() , path.extended_ssid_new_value , "value of 'EXTENDED SSID' not set to non-default")
        
        elif drop_box_elem == 'deny inter':
            logger.debug("SystemPage : asserting the non-default value of 'DENY INTER USING BRIDGING' drop-down")
            test_case.assertEquals(self.deny_inter_using.get_selected() , path.deny_inter_using_new_value , "value of 'DENY INTER USING BRIDGING' not set to non-default")
        
        elif drop_box_elem == 'deny local routing':
            logger.debug("SystemPage : asserting the non-default value of 'DENY LOCAL ROUTING' drop-down")
            test_case.assertEquals(self.deny_local_routing.get_selected() , path.deny_local_routing_new_value , "value of 'DENY LOCAL ROUTING' not set to non-default")
            
        elif drop_box_elem == 'telnet server':
            logger.debug("SystemPage : asserting the non-default value of 'TELNET SERVER' drop-down")
            test_case.assertEquals(self.telnet_server.get_selected() , path.sys_enable , "value of 'TELNET SERVER' not set to non-default")
            
        elif drop_box_elem == 'dynamic cpu utilization disabled':
            logger.debug("SystemPage : asserting the non-default value of 'DYNAMIC CPU UTILIZATION' drop-down")
            test_case.assertEquals(self.dynamic_cpu_utilization.get_selected() , path.dynamic_cpu_utilization_disable , "value of 'DYNAMIC CPU UTILIZATION' not set to  'Always Disabled in all APs'")
            
        elif drop_box_elem == 'dynamic cpu utilization enabled':
            logger.debug("SystemPage : asserting the non-default value of 'DYNAMIC CPU UTILIZATION' drop-down")
            test_case.assertEquals(self.dynamic_cpu_utilization.get_selected() , path.dynamic_cpu_utilization_enable , "value of 'DYNAMIC CPU UTILIZATION' not set to  'Always Enabled in all APs'")
            
    def set_dropdown_value_default(self , drop_box_elem):
        path = self.config.config_vars
        if drop_box_elem == 'timezone':
            logger.debug("SystemPage : Set value in 'TIMEZONE' drop-down")
            self.timezone.set(path.timezone_value)
        elif drop_box_elem == 'preferred band':
            logger.debug("SystemPage : Set value in 'PREFERRED BAND' drop-down")
            self.preferred_band.set(path.preferred_band_value)
        elif drop_box_elem == 'auto join mode':
            logger.debug("SystemPage : Set value in 'AUTO JOIN MODE' drop-down")
            self.auto_join_mode.set(path.auto_join_mode_value)
        elif drop_box_elem == 'terminal access':
            logger.debug("SystemPage : Set value in 'TERMINAL ACCESS' drop-down")
            # self.terminal_access.set(path.terminal_access_value)
        elif drop_box_elem == 'led display':
            logger.debug("SystemPage : Set value in 'LED DISPLAY' drop-down")
            self.led_display.set(path.led_display_value)
        elif drop_box_elem == 'extended ssid':
            logger.debug("SystemPage : Set value in 'EXTENDED SSID' drop-down")
            self.extended_ssid.set(path.extended_ssid_value)
        elif drop_box_elem == 'deny inter':
            logger.debug("SystemPage : Set value in 'DENY INTER USING BRIDGING' drop-down")
            self.deny_inter_using.set(path.sys_disable)
        elif drop_box_elem == 'deny local routing':
            logger.debug("SystemPage : Set value in 'DENY LOCAL ROUTING' drop-down")
            self.deny_local_routing.set(path.sys_disable)
        elif drop_box_elem == 'telnet server':
            logger.debug("SystemPage : Set value in 'TELNET SERVER' drop-down")
            self.telnet_server.set(path.sys_disable)
        elif drop_box_elem == 'dynamic cpu utilization':
            logger.debug("SystemPage : Set value in 'DYNAMIC CPU UTILIZATION' drop-down")
            self.dynamic_cpu_utilization.set(path.dynamic_cpu_utilization_value)
        self._save_settings()
        
        
    def go_to_admin_tab(self):
        logger.debug("SystemPage : Click 'Admin' bar")
        time.sleep(6)
        self.admin_tab.click()
        if not self.admin_authentication:
            self.admin_tab.click()
        self.browser.key_press(u'\ue00e')
            
    def set_username_and_password(self , validity = None , equality = None):
        if validity is None:
            pass
        if validity == 'valid':
            logger.debug("SystemPage : Write valid user-name")
            self.u_name.set(self.config.config_vars.admin_valid_u_name)
        elif validity == 'invalid':
            logger.debug("SystemPage : Write invalid user-name")
            self.u_name.set(self.config.config_vars.admin_invalid_u_name)
        if equality is None:
            pass
        elif equality == 'match':
            logger.debug("SystemPage : Write password")
            self.p_word.set(self.config.config_vars.admin_password)
            self.retype_p_word.set(self.config.config_vars.admin_password)
        elif equality == 'mismatch':
            logger.debug("SystemPage : Write password")
            self.p_word.set(self.config.config_vars.admin_password)
            self.retype_p_word.set(self.config.config_vars.admin_unmatch_p_word)
            
            time.sleep(3)
        logger.debug("SystemPage : Click 'Save Settings' button")
        self._save_settings()
        time.sleep(8)
            
    def assert_error_message_present(self):
        if not self.uname_pwd_error_msg:
            raise AssertionError("Error message not found i.e. Traceback: %s" %traceback.format_exc())
            
    def create_new_radius_server(self , mode):
        time.sleep(7)
        path = self.config.config_vars
        logger.debug("SystemPage : Set value in 'AUTHENTICATION' drop-down")
        if mode == 'without fallback':
            self.admin_authentication.set(path.authentication_new_value)
        elif mode == 'with fallback':
            self.admin_authentication.set(path.authentication_new_value_fallback)
            self._assert_admin_local_radius_server_fallback_fields()
        logger.debug("SystemPage : Set value in 'AUTH SERVER 1' drop-down")
        if path.new_auth_server_name in self.auth_server_1.get_options():
            self.auth_server_1.set(path.new_auth_server_name)
        else:
            self.auth_server_1.set(path.auth_server_new_value)
            logger.debug("SystemPage : Write authentication server name")
            self.auth_server_name.set(path.new_auth_server_name)
            logger.debug("SystemPage : Write authentication server ip address")
            self.auth_server_ip.set(path.auth_server_ip)
            logger.debug("SystemPage : Write authentication server shared key")
            self.auth_server_shared_key.set(path.system_auth_shared_key)
            logger.debug("SystemPage : Rewrite authentication server shared key")
            self.re_auth_server_shared_key.set(path.system_auth_shared_key)
            logger.debug("SystemPage : Click 'Save Server' button")
            self.save_server.click()
        logger.debug("SystemPage : Click 'Save Settings' button")
        self._save_settings()
        
    def set_admin_authentication_default_value(self):
        logger.debug("SystemPage : Set value in 'AUTHENTICATION' drop-down to default")
        self.admin_authentication.set(self.config.config_vars.authentication_value)
        logger.debug("SystemPage : Click 'Save Settings' button")
        self._save_settings()
            
    def assert_new_auth_server_present(self):   
        test_case = TestCase(self.config)
        path = self.config.config_vars
        logger.debug("SystemPage : asserting the value of 'AUTH SERVER 1' drop-down")
        test_case.assertEquals(self.auth_server_1.get_selected() , path.new_auth_server_name , "value of 'AUTH SERVER 1' not set to 'newserver'")   
            
    def go_to_dhcp_tab(self):
        logger.debug("SystemPage : Click 'DHCP' bar")
        self.dhcp_tab.click()
        if not self.domain_name_dhcp:
            self.dhcp_tab.click()
        self.browser.key_press(u'\ue00e')
        
    def set_dhcp_values(self):
        
        time.sleep(7)
        logger.debug("SystemPage : Write domain name")
        self.domain_name_dhcp.set(self.config.config_vars.domain_name_value)
        logger.debug("SystemPage : Write dns server ip address")
        self.dns_server.set(self.config.config_vars.dns_server_value)
        logger.debug("SystemPage : Write lease time")
        self.lease_time.set(self.config.config_vars.lease_time_value)
        logger.debug("SystemPage : Write network ip address")
        self.network1.set(self.config.config_vars.network_value1)
        logger.debug("SystemPage : Write mask ip address")
        self.mask.set(self.config.config_vars.mask_value)
        logger.debug("SystemPage : Click 'Save Settings' button")
        self._save_settings()

    def click_enterprise_domain(self):
        logger.debug("SystemPage :Click Enterprise Domain.")
        self.enterprise_domain.click()
        if not self.new_domain:
            self.enterprise_domain.click()
        self.buy_time()
        
    def assert_enterprise_domain_page(self):
        if self.new_domain:
            return True
        else:
            raise AssertionError("enterprise domain page did not load i.e . Traceback: %s" % traceback.format_exc())    
            
    def create_domain(self):
        logger.debug("SystemPage :Creating new domain.")
        self.new_domain.click()
        logger.debug("SystemPage : Settings domain name value")
        self.domain_name.set(self.config.config_vars.domain_name)
        self.save_domain.click()
        logger.debug("SystemPage : Click 'Save Settings' button")
        self._save_settings()
        
    def assert_create_domain(self):
        logger.debug("SystemPage :Click Enterprise Domain.")
        self.buy_time()
        self.enterprise_domain.click()
        if self.selected_domain:
            return True
        else:
            raise AssertionError(" Domain name Not Added .i.e Traceback: %s " %traceback.format_exc())
        self.buy_time()
            
    def delete_domain(self):
        logger.debug("SystemPage :Click Enterprise Domain.")
        if self.selected_domain:
            self.selected_domain.click()
            self.buy_time()
            logger.debug("SystemPage :Deleting domain.")
            self.delete.click()
            logger.debug("SystemPage : Click 'Save Settings' button")
            self._save_settings()
        
    def assert_delete_domain(self):
        logger.debug("SystemPage :Click Enterprise Domain.")
        self.enterprise_domain.click()
        if self.no_doamin_present:
            return True
        else:
            raise AssertionError(" Domain values Not Deleted .i.e Traceback: %s " %traceback.format_exc())
            
    def click_logging(self):
        logger.debug("SystemPage :Click Logging.")
        self.logging.click()
        if not self.syslog_server:
            self.logging.click()
        self.buy_time()
        
    def assert_logging_page(self):
        if not self.syslog_server:
            self.syslog_server.click()
                
    def add_syslog_server(self):
        logger.debug("SystemPage : Entering Invalid IP Address...")
        self.syslog_server.set(self.config.config_vars.invalid_syslog_server)
        if self.invalid_ip:
            logger.debug("SystemPage : Invalid IP Address... Entering New IP Address")
            self.syslog_server.set(self.config.config_vars.valid_syslog_server_1)
            logger.debug("SystemPage : Click 'Save Settings' button")
            self._save_settings()
            self.buy_time()
            
    def revert_settings(self):
        logger.debug("SystemPage : Set Syslog server value to default.")
        self.syslog_server.set('')
        logger.debug("SystemPage : Click 'Save Settings' button")
        self._save_settings()
        
    def assert_add_syslog_server(self):
        logger.debug("SystemPage :Click Logging.")
        self.logging.click()
        if not self.invalid_ip: 
            return True
        else:
            raise AssertionError("IP adress not added i.e . Traceback: %s" % traceback.format_exc())
            
    def assert_syslog_facility_levels(self):
        test_case = TestCase(self.config)
        path = self.config.config_vars
        
        logger.debug("SystemPage : Changing the value of SYSLOG LEVEL")
        test_case.assertEquals(self.syslog_level.get_selected() ,  path.Emergency , "value of 'SYSLOG LEVEL' was not changed")
        
        logger.debug("SystemPage : Changing the value of AP-DEBUG")
        test_case.assertEquals(self.ap_debug.get_selected() ,  path.Alert , "value of 'AP-DEBUG' was not changed")
        
        logger.debug("SystemPage : Changing the value of NETWORK")
        test_case.assertEquals(self.network.get_selected() , path.Critical , "value of 'NETWORK' was not  changed")
        
        logger.debug("SystemPage : Changing the value of SECURITY")
        test_case.assertEquals(self.security.get_selected() ,  path.Error , "value of 'SECURITY' was not changed")
        
        logger.debug("SystemPage : Changing the value of SYSTEM")
        test_case.assertEquals(self.system.get_selected() ,  path.Warning , "value of 'SYSTEM' was not  changed")
        
        logger.debug("SystemPage : Changing the value of USER")
        test_case.assertEquals(self.user.get_selected() ,  path.Notice , "value of 'USER' was not changed")
        
        logger.debug("SystemPage : Changing the value of USER-DEBUG")
        test_case.assertEquals(self.user_debug.get_selected() ,  path.Information , "value of 'USER-DEBUG' was not changed")
        
        logger.debug("SystemPage : Changing the value of WIRELESS")
        test_case.assertEquals(self.wireless.get_selected() , path.Debug , "value of 'WIRELESS' was not changed")
        
    def set_non_default_values(self,syslog_level,ap_debug,network,security,system,user,user_debug,wireless):
        logger.debug("SystemPage : Set syslog level.")
        self.syslog_level.set(syslog_level)
        logger.debug("SystemPage : Set ap debug.")
        self.ap_debug.set(ap_debug)
        logger.debug("SystemPage : Set network value.")
        self.network.set(network)
        logger.debug("SystemPage : Set security.")
        self.security.set(security) 
        logger.debug("SystemPage : Set system.")
        self.system.set(system) 
        logger.debug("SystemPage : Set user.")
        self.user.set(user) 
        logger.debug("SystemPage : Set user debug.") 
        self.user_debug.set(user_debug) 
        logger.debug("SystemPage : Set wireless.")
        self.wireless.set(wireless)
        logger.debug("SystemPage : Click 'Save Settings' button")
        self._save_settings()
        self.buy_time()     
        
    def restore_default_values(self):
        path = self.config.config_vars
        logger.debug("SystemPage : Set syslog level to default.")
        self.syslog_level.set(path.default_syslog)
        logger.debug("SystemPage : Set ap debug to default.")
        self.ap_debug.set(path.default_syslog)
        logger.debug("SystemPage : Set network to default.")
        self.network.set(path.default_syslog)   
        logger.debug("SystemPage : Set security to default.")
        self.security.set(path.default_syslog)  
        logger.debug("SystemPage : Set system to default.")
        self.system.set(path.default_syslog)    
        logger.debug("SystemPage : Set user to default.")
        self.user.set(path.default_syslog)      
        logger.debug("SystemPage : Set user debug to default.")
        self.user_debug.set(path.default_syslog)
        logger.debug("SystemPage : Set wireless to default.")
        self.wireless.set(path.default_syslog)
        logger.debug("SystemPage : Click 'Save Settings' button")
        self._save_settings()
            
    def click_l3_mobility(self):
        logger.debug("SystemPage :Click L3 Mobility.")
        self.l3_mobility.click()
        if not self.new_vc_ip_address:
            self.l3_mobility.click()
        self.buy_time()
        
    def assert_l3_mobility_page(self):
        if self.new_vc_ip_address:
            return True
        else:
            raise AssertionError("L3 Mobility page did not load i.e . Traceback: %s" % traceback.format_exc())  
            
    def create_virtual_controller_ip_address(self):
        self.new_vc_ip_address.click()
        logger.debug("SystemPage : Set virtual controller ip address.")
        self.vc_ip_address.set(self.config.config_vars.invalid_vc_ip_address)
        logger.debug("SystemPage : Click Save button")
        self.save_vc.click()
        self.assert_invalid_virtual_controller_ip_address()
        logger.debug("SystemPage : Set virtual controller ip address.")
        self.vc_ip_address.set(self.config.config_vars.vc_ip_address)
        logger.debug("SystemPage : Click Save button")
        self.save_vc.click()
        self.buy_time()
        
    def delete_virtual_controller_ip_address(self): 
        self.buy_time()
        if self.selected_ip_address:
            self.selected_ip_address.click()
            self.buy_time()
            logger.debug("SystemPage : Delete virtual controller ip address.")
            self.delete_vc_ip_address.click()
            self.buy_time()
            logger.debug("SystemPage : Click 'Save Settings' button")
            self._save_settings()
            self.buy_time()
            
    def delete_subnets(self):
        self.buy_time()
        if self.selected_subnets:
            logger.debug("SystemPage : Click subnet mask")
            self.selected_subnets.click()
            self.buy_time()
            logger.debug("SystemPage : Deleting Subnet.")
            self.delete_subnet.click()
            
    def create_subnets(self):
        self.new_subnet.click()
        logger.debug("SystemPage : Set subnet address.")
        self.subnet_address.set(self.config.config_vars.invalid_subnet_address)
        logger.debug("SystemPage : Click Save button")
        self.save_subnet.click()
        if not self.subnet_address_error:
            raise AssertionError("Accepting Invalid Subnet Address. i.e. Traceback: %s" %traceback.format_exc())
        self.buy_time()
        logger.debug("SystemPage : Set subnet address.")
        self.subnet_address.set(self.config.config_vars.subnet_address)
        logger.debug("SystemPage : Set subnet mask.")
        self.subnet_mask.set(self.config.config_vars.invalid_subnet_mask)
        self.save_subnet.click()
        if not self.subnet_mask_error:
            raise AssertionError("Accepting Invalid Subnet Mask. i.e. Traceback: %s" %traceback.format_exc())
        self.buy_time()
        logger.debug("SystemPage : Set subnet address.")
        self.subnet_mask.set(self.config.config_vars.subnet_mask)
        logger.debug("SystemPage : Set vlan id.")
        self.vlan_id.set(self.config.config_vars.invalid_vlan_id)
        self.save_subnet.click()
        if not self.vlan_id_error:
            raise AssertionError("Accepting Invalid vlan id. i.e. Traceback: %s" %traceback.format_exc())
        self.buy_time()
        logger.debug("SystemPage : Setting vlan id")
        self.vlan_id.set(self.config.config_vars.vlan_id)
        logger.debug("SystemPage : Set virtual controller ip address.")
        self.subnet_vc_ip.set(self.config.config_vars.invalid_subnet_vc_ip)
        self.save_subnet.click()
        if not self.subnet_vc_ip_error:
            raise AssertionError("Accepting Invalid subnet vc ip. i.e. Traceback: %s" %traceback.format_exc())
        self.buy_time()
        logger.debug("SystemPage : Setting vc ip address")
        self.subnet_vc_ip.set(self.config.config_vars.subnet_vc_ip)
        self.buy_time()
        logger.debug("SystemPage : Click Save button")
        self.save_subnet.click()
        logger.debug("SystemPage : Click 'Save Settings' button")
        self._save_settings()
        self.buy_time()
        
    def assert_virtual_controller_ip_address(self):
        self.l3_mobility.click()
        if self.selected_ip_address:
            return True
        else:
            raise AssertionError(" Virtual Controller IP Address Not Added .i.e Traceback: %s " %traceback.format_exc())            
            
    def assert_new_wifi_setup(self):
        logger.debug("SystemPage :Click on uplink accordion")   
        # self.uplink_accordion.click()
        self.uplink.click()
        
        time.sleep(6)   
        logger.debug("SystemPage : Set wifi name.")
        self.wifi_name.set(self.config.config_vars.Wifi_Name)
        logger.debug("SystemPage : Set wifi passphrase name.")
        self.wifi_passphrase.set(self.config.config_vars.Wifi_Passphrase)
        if not self.cancel:
            raise AssertionError("Cancel button not found. i.e. Traceback: %s" %traceback.format_exc())
        if not self.save_settings:
            raise AssertionError("Save settings button not found. i.e. Traceback: %s" %traceback.format_exc())  
            
    def create_new_wifi(self):
        self.assert_new_wifi_setup()
        if self.save_settings:
            self._save_settings()
            
    def edit_management_settings(self):
        logger.debug("SystemPage : Set enforce uplink to wifi.")
        self.manage_enforce_uplink.set(self.config.config_vars.Management_Enforce_Uplink)
        if self.cancel_pop_up:
            self.cancel_pop_up.click()      
        logger.debug("SystemPage : Click on wifi-sta .")
        self.wifi_sta.click()
        for i in range(1,10):
            if self.arrow_up_disabled:
                break
            logger.debug("SystemPage : Click on arrow up .")
            self.arrow_up.click()
        logger.debug("SystemPage : Click 'Save Settings' button")
        if self.save_settings:
            self._save_settings()
            
    def assert_new_service_setup(self):
        logger.debug("SystemPage :Click on uplink accordion")   
        # self.uplink_accordion.click()
        self.uplink.click()
        
        time.sleep(6)   
        logger.debug("SystemPage : Set service name.")
        self.pp_service_name.set(self.config.config_vars.Service_Name)
        if not self.cancel:
            raise AssertionError("Cancel button not found. i.e. Traceback: %s" %traceback.format_exc())
        if not self.save_settings:
            raise AssertionError("Save settings button not found. i.e. Traceback: %s" %traceback.format_exc())  
            
    def create_new_ppoe(self):
        logger.debug("SystemPage : Set chap secret.")
        self.pp_chap_secret1.set(self.config.config_vars.Chap_Secret)
        logger.debug("SystemPage : Set retype chap secret.")
        self.pp_chap_secret2.set(self.config.config_vars.Chap_Secret)
        logger.debug("SystemPage : Set retype chap secret.")
        self.pp_chap_secret2.set(self.config.config_vars.Chap_Secret)
        logger.debug("SystemPage : Set user name.")
        self.pp_user.set(self.config.config_vars.User_Name)
        logger.debug("SystemPage : Set password.")
        self.pp_password.set(self.config.config_vars.PPOE_Passphrase)
        logger.debug("SystemPage : Set retype password.")
        self.pp_password_retype.set(self.config.config_vars.PPOE_Passphrase)                    
        logger.debug("SystemPage : Click 'Save Settings' button")
        if self.save_settings:
            self._save_settings()
            
    def select_modem_country_isp(self):
        logger.debug("SystemPage :Click on uplink accordion")   
        self.uplink_accordion.click()
        
        time.sleep(8)
        logger.debug("SystemPage : Set modem country.")
        self.modem_country.set(self.config.config_vars.Modem_Country)           
        logger.debug("SystemPage : Set ISP.")
        self.modem_isp.set(self.config.config_vars.Isp_Name)
        if not self.cancel:
            raise AssertionError("Cancel button not found. i.e. Traceback: %s" %traceback.format_exc())
        if not self.save_settings:
            raise AssertionError("Save settings button not found. i.e. Traceback: %s" %traceback.format_exc())  
        logger.debug("SystemPage : Click 'Save Settings' button")
        if self.save_settings:
            self._save_settings()
            
    def cofigure_3g_settings(self):
        logger.debug("SystemPage :Click on uplink accordion")   
        self.uplink_accordion.click()
        
        time.sleep(15)
        logger.debug("SystemPage : Set 3g usb type.")
        self.cell_usb.set(self.config.config_vars.Cell_Usb)         
        logger.debug("SystemPage : Set 4g type .")
        self.cell_4g_type.set(self.config.config_vars.Cell_4g_Type)     
        logger.debug("SystemPage : Set Usb device.")
        self.cell_usb_dev.set(self.config.config_vars.Cell_Usb_Dev)         
        logger.debug("SystemPage : Set Usb tty.")
        self.cell_usb_tty.set(self.config.config_vars.Cell_Usb_Tty)             
        logger.debug("SystemPage : Set Usb Init.")
        self.cell_usb_init.set(self.config.config_vars.Cell_Usb_Init)           
        logger.debug("SystemPage : Set Usb Dial.")
        self.cell_usb_dial.set(self.config.config_vars.Cell_Usb_Dial)           
        logger.debug("SystemPage : Set Usb mode switch.")
        self.cell_usb_mode_switch.set(self.config.config_vars.Cell_Usb_Mode_Switch)         
        logger.debug("SystemPage : Set Usb user.")
        self.cell_usb_user.set(self.config.config_vars.Cell_Usb_User)               
        logger.debug("SystemPage : Set Usb password.")
        self.cell_usb_password.set(self.config.config_vars.Cell_Usb_Password)
        logger.debug("SystemPage : Click 'Save Settings' button")
        if self.save_settings:
            self._save_settings()
            
    def click_uplink(self):
        logger.debug("SystemPage :Click on uplink")
        self.buy_time()
        if self.uplink_accordion:
            self.uplink_accordion.click()
        self.buy_time()
        if not self.wifi_name:
            self.uplink_accordion.click()
        self.buy_time()
        
    def configure_usb_auth_type(self):
        logger.debug("SystemPage : Set value in 'Usb Auth Type' drop-down")
        path = self.config.config_vars
        self.usb_auth_type.set(path.usb_auth_type_value)
        logger.debug("SystemPage : Click 'Save Settings' button")
        self._save_settings()
        self.buy_time()
        
    def restore_usb_auth_type_default_values(self):
        logger.debug("SystemPage : Changing the value of 'Usb Auth Type' to default")
        path = self.config.config_vars
        self.usb_auth_type.set(path.default_usb_auth_type)
        logger.debug("SystemPage : Click 'Save Settings' button")
        self._save_settings()
        self.buy_time()
        
    def assert_internet_failover_default_values(self):
        test_case = TestCase(self.config)
        path = self.config.config_vars
        test_case.assertEquals(self.manage_internet_failover.get_selected() , path.default_manage_internet_failover, "value of 'INTERNET FAILOVER' is not set to default")
        
    def configure_internet_failover(self):
        logger.debug("SystemPage : Enabling INTERNET FAILOVER")
        path = self.config.config_vars
        self.manage_internet_failover.set(path.manage_internet_failover_value)
        self.buy_time()
        if self.failover_packet_send_frequency and self.failover_packet_lost_count and self.internet_ckeck_timeout :
            logger.debug("INTERNET FAILOVER IS ENABLED")
            self.buy_time()
            logger.debug("SystemPage : Write Failover Packet Send Frequency")
            self.failover_packet_send_frequency.set(self.config.config_vars.invalid_failover_packet_send_frequency)
            logger.debug("SystemPage : Click 'Save Settings' button")
            self._save_settings()
            if not self.packet_send_frequency_error:
                raise AssertionError("Accepting Invalid values for Failover packet send frequency. i.e. Traceback: %s" %traceback.format_exc())
            self.buy_time()
            self.failover_packet_send_frequency.set(self.config.config_vars.failover_packet_send_frequency)
            logger.debug("SystemPage : Write Failover Packet Lost Frequency")
            self.failover_packet_lost_count.set(self.config.config_vars.invalid_failover_packet_lost_count)
            logger.debug("SystemPage : Click 'Save Settings' button")
            self._save_settings()
            if not self.packet_lost_count_error:
                raise AssertionError("Accepting Invalid values for Failover packet lost count. i.e. Traceback: %s" %traceback.format_exc())
            self.buy_time()
            self.failover_packet_lost_count.set(self.config.config_vars.failover_packet_lost_count)
            logger.debug("SystemPage : Write Internet Check Timeout")
            self.internet_ckeck_timeout.set(self.config.config_vars.invalid_internet_ckeck_timeout)
            logger.debug("SystemPage : Click 'Save Settings' button")
            self._save_settings()
            if not self.internet_ckeck_timeout_error:
                raise AssertionError("Accepting Invalid values for Internet check timeout. i.e. Traceback: %s" %traceback.format_exc())
            self.buy_time()
            self.internet_ckeck_timeout.set(self.config.config_vars.internet_ckeck_timeout)
            self.buy_time()
            logger.debug("SystemPage : Click 'Save Settings' button")
            self._save_settings()
            self.buy_time()
        
    def restore_internet_failover_default_values(self):
        logger.debug("SystemPage : Changing the value of 'Manage Internet Failover' to default")
        path = self.config.config_vars
        self.manage_internet_failover.set(path.default_manage_internet_failover)
        logger.debug("SystemPage : Click 'Save Settings' button")
        self._save_settings()
        self.buy_time()

    def buy_time(self):
        
        time.sleep(8)

    def assert_invalid_virtual_controller_ip_address(self):
        if self.vc_ip_address_error: 
            logger.debug("Invalid IP address")
            return True
        else:
            raise AssertionError("VC IP adress  accepting invalid values i.e . Traceback: %s" % traceback.format_exc())
            
    def _assert_admin_local_radius_server_fallback_fields(self):
        if not(self.auth_server_1_label and self.auth_server_2_label and self.username_label and self.password_label and self.retype_password_label):
            raise AssertionError("Radius server with fallback fields not found i.e . Traceback: %s" % traceback.format_exc())
            
    def set_default_uplink_management_settings(self):
        logger.debug('SystemPage: Selecting manage enforce link None')
        self.manage_enforce_uplink.set(self.config.config_vars.manage_enforce_uplink)
        logger.debug('SystemPage: Selecting Pre-emption enabled')
        self.manage_pre_empt.set(self.config.config_vars.pre_emption)
        logger.debug('SystemPage: Writting 180 in vpn fail over time out')
        self.manage_time_txt.set(self.config.config_vars.vpn_failover_timeout)
        logger.debug('SystemPage: Selecting internet failover disabled')
        self.manage_internet_failover.set(self.config.config_vars.internet_failover)
        
    def assert_dhcp_default_values(self):
        logger.debug("SystemPage : asserting the default value of 'DOMAIN NAME' textbox")
        if not self.domain_name_dhcp.get() == '':
            raise AssertionError("DOMAIN NAME textbox is not empty by default. i.e. Traceback: %s" %traceback.format_exc())
        logger.debug("SystemPage : asserting the default value of 'DNS SERVER' textbox")
        if not self.dns_server.get() == '':
            raise AssertionError("DNS SERVER textbox is not empty by default. i.e. Traceback: %s" %traceback.format_exc())
        logger.debug("SystemPage : asserting the default value of 'LEASE TIME' textbox")
        if not self.lease_time.get() == self.config.config_vars.default_least_time:
            raise AssertionError("LEASE TIME textbox  is not zero by default. i.e. Traceback: %s" %traceback.format_exc())
        logger.debug("SystemPage : asserting the default value of 'LEASE TIME' dropdown")
        if not self.least_time_dropdown.get_selected() == self.config.config_vars.least_time_days :
            raise AssertionError(" LEASE TIME dropdown  is not Days by default. i.e. Traceback: %s" %traceback.format_exc())
        logger.debug("SystemPage : asserting the default value of 'NETWORK' textbox")
        if not self.network1.get() == '':
            raise AssertionError(" NETWORK textbox is not empty by default. i.e. Traceback: %s" %traceback.format_exc())
        logger.debug("SystemPage : asserting the default value of 'MASK' textbox")
        if not self.mask.get() == '':
            raise AssertionError(" Mask textbox is not empty by default. i.e. Traceback: %s" %traceback.format_exc())
            
    def configure_virtual_controller_values(self):
        logger.debug("SystemPage : Writting vc netmask'")
        self.gen_vc_netmask.set(self.config.config_vars.gen_vc_netmask)
        logger.debug("SystemPage : Writting vc gateway'")
        self.gen_vc_gateway.set(self.config.config_vars.gen_vc_gateway)
        logger.debug("SystemPage : Writting vc vlan'")
        self.gen_vc_vlan.set(self.config.config_vars.gen_vc_vlan)
        logger.debug("SystemPage : Click 'Save Settings' button")
        self._save_settings()
        self.buy_time()
        
    def restore_virtual_controller_values(self):
        logger.debug("SystemPage : Restoring virtual controller values")
        self.gen_vc_netmask.set('')
        self.gen_vc_gateway.set('')
        self.gen_vc_vlan.set('')
        logger.debug("SystemPage : Click 'Save Settings' button")
        self._save_settings()
        self.buy_time()
        
    def assert_virtual_controller_values(self):
        logger.debug("SystemPage : Asserting virtual controller values")
        self.gen_vc_netmask.set('0')
        self.gen_vc_gateway.set('0')
        self.gen_vc_vlan.set('0')
        logger.debug("SystemPage : Click 'Save Settings' button")
        self._save_settings()
        self.buy_time()
        if not self.vc_netmask_error :
            raise AssertionError("Virtual controller netmask accepting invalid values i.e . Traceback: %s" % traceback.format_exc())
        if not self.vc_gateway_error :
            raise AssertionError("Virtual controller gateway accepting invalid values i.e . Traceback: %s" % traceback.format_exc())
        if not self.vc_vlan_error :
            raise AssertionError("Virtual controller vlan accepting invalid values i.e . Traceback: %s" % traceback.format_exc())
            
    def assert_local_server_default_values(self):
        if not self.admin_authentication.get_selected() == self.config.config_vars.authentication_value:
            raise AssertionError("Authentication dropdown is not set to Internal by default .Traceback: %s " %traceback.format_exc())
        if not self.u_name.get() == self.config.config_vars.admin_username:
            raise AssertionError("Username is not set to admin.Traceback: %s " %traceback.format_exc())
        # password = self.p_word.get()
        # print password
        if not self.p_word.get() == self.config.config_vars.a_password:
            raise AssertionError("Password is not set to ********.Traceback: %s " %traceback.format_exc())
        if not self.retype_p_word.get() == self.config.config_vars.a_password:
            raise AssertionError("Retype Password is not set to ********.Traceback: %s " %traceback.format_exc())
            
    def assert_view_only_default_values(self):
        if not self.usernamereadonly.get() == '':
            raise AssertionError("View Only Username Feild is not Empty.Traceback: %s " %traceback.format_exc())
        if not self.passwordreadonly.get() == '':
            raise AssertionError("View Only Password Feild is not Empty.Traceback: %s " %traceback.format_exc())
        if not self.retypepasswordreadonly.get() == '':
            raise AssertionError("View Only Retype Password Feild is not Empty.Traceback: %s " %traceback.format_exc())
        
    def assert_guest_registration_only_default_values(self):
        if not self.usernameguest.get() == '':
            raise AssertionError("Guest Registration Only Username Feild is not Empty.Traceback: %s " %traceback.format_exc())
        if not self.passwordguest.get() == '':
            raise AssertionError("Guest Registration Only Password Feild is not Empty.Traceback: %s " %traceback.format_exc())
        if not self.retypepasswordguest.get() == '':
            raise AssertionError("Guest Registration Only Retype Password Feild is not Empty.Traceback: %s " %traceback.format_exc())
            
    def guest_registration_only_non_default_values(self,username,password,re_password):
        logger.debug("SystemPage : Writing value in Guest Registration Only Username Feild")
        self.usernameguest.set(username)
        logger.debug("SystemPage : Writing value in Guest Registration Only Password Feild")
        self.passwordguest.set(password)
        logger.debug("SystemPage : Writing value in Guest Registration Only Retype Password Feild")
        self.retypepasswordguest.set(re_password)
        self.buy_time()

    def view_only_non_default_values(self,username,password,re_password):
        logger.debug("SystemPage : Writing value in View Only Username Feild")
        self.usernamereadonly.set(username)
        logger.debug("SystemPage : Writing value in View Only Password Feild")
        self.passwordreadonly.set(password)
        logger.debug("SystemPage : Writing value in View Only Retype Password Feild")
        self.retypepasswordreadonly.set(re_password)
        self.buy_time()

    def restore_guest_registration_only_default_values(self):
        logger.debug("SystemPage : Restoring default values")
        self.usernameguest.clear()
        self.passwordguest.clear()
        self.retypepasswordguest.clear()
        logger.debug("SystemPage : Click 'Save Settings' button")
        self._save_settings()

    def restore_view_only_default_values(self):
        logger.debug("SystemPage : Restoring default values")
        time.sleep(6)
        self.usernamereadonly.clear()
        self.passwordreadonly.clear()
        self.retypepasswordreadonly.clear()
        logger.debug("SystemPage : Click 'Save Settings' button")
        self._save_settings()
        
    def go_to_snmp_tab(self):
        logger.debug("SystemPage : Click 'snmp' bar")
        self.snmp_tab.click()
        if not self.new_snmp_button:
            self.snmp_tab.click()
        self.browser.key_press(u'\ue00e')
        self.buy_time()
            
    def snmp_community_string_validation(self):
        logger.debug("SystemPage : Click new snmp button")
        self.new_snmp_button.click()
        logger.debug("SystemPage : Writing invalid value in snmp community string textbox  Feild")
        self.snmp_community_string_textbox.set(self.config.config_vars.snmp_invalid_string)
        self.snmp_save_new_community.click()
        if not self.snmp_string_error :
            raise AssertionError("Snmp community string textbox  Feild is accepting invalid input.Traceback: %s " %traceback.format_exc())
        self.snmp_community_string_textbox.set(self.config.config_vars.snmp_valid_string)
        self.snmp_save_new_community.click()
        # self.snmp_save_new_community.click()
        time.sleep(2)
        logger.debug("SystemPage : Click delete button to delete SNMP")
        self.delete_snmp_button.click()
        
    
    def page_down(self):
        '''
        scroll down the page
        '''
        self.browser.key_press(u'\ue009')
        self.browser.key_press( u'\ue00f')

    def go_to_proxy_tab(self):
        self.buy_time()
        self.page_down()
        if not self.proxy_tab:
            self.page_down()
        logger.debug("SystemPage : Click 'Proxy' bar")
        self.proxy_tab.click()
        if not self.Proxy_Server:
            self.proxy_tab.click()
        self.buy_time()
        
    def assert_default_proxy_value(self):
        '''
        Asserting Default proxy values
        '''
        test_case = TestCase(self.config)
        path = self.config.config_vars
        
        time.sleep(3)
        logger.debug("SystemPage :ProxyPage - asserting the default value of 'SERVER' textbox")
        test_case.assertEquals(self.Proxy_Server.get() , '' , "value of 'SERVER' textbox not set to default")
        logger.debug("SystemPage :ProxyPage -  asserting the default value of 'PORT' textbox")
        test_case.assertEquals(self.Proxy_Port.get() , '' , "value of 'PORT' textbox not set to default")
        if not self.no_data_to_display_label:
            raise AssertionError("Empty box with 'No data to display' label is not present: %s" %traceback.format_exc())
        self.create_new_proxy.click()
        self.buy_time()
        logger.debug("SystemPage :ProxyPage -  asserting the default value of 'New Exception' textbox")
        test_case.assertEquals(self.new_exception_textbox.get() , '' , "value of 'New Exception' textbox not set to default")
        
    def click_on_proxy_exception_cancel(self):
        '''
        clicking on cancel button
        '''
        self.buy_time()
        logger.debug("SystemPage :ProxyPage - clicking on cancel button")
        self.cancel_proxy.click()
    
    def set_proxy_server_value(self,value):
        '''
        set value for Proxy Server textbox
        '''
        if value == None:
            logger.debug("SystemPage :ProxyPage - set  value for 'SERVER' textbox")
            self.Proxy_Server.set('')
        else:
            logger.debug("SystemPage :ProxyPage - set  value for 'SERVER' textbox")
            self.Proxy_Server.set(value)
            
    def assert_proxy_server_error(self,assert_error):
        '''
        Asserting Proxy Server textbox error message
        '''
        if assert_error == 'true':
            if not self.proxy_server_error:
                raise AssertionError("Proxy Server accepting Invalid Host or IP Address: %s" %traceback.format_exc())
        elif assert_error == 'false':
            if  self.proxy_server_error:
                raise AssertionError(" Invalid Host or IP Address given for Proxy Server  : %s" %traceback.format_exc())
        
    def set_proxy_port_value(self,value):
        '''
        set value for Proxy Server textbox
        '''
        if value == None:
            logger.debug("SystemPage :ProxyPage - set  value for 'SERVER' textbox")
            self.Proxy_Port.set('')
        else:
            logger.debug("SystemPage :ProxyPage - set  value for 'SERVER' textbox")
            self.Proxy_Port.set(value)
            
    def assert_proxy_port_error(self,assert_error):
        '''
        Asserting Proxy Port textbox error message
        '''
        if assert_error == 'true':
            if not self.proxy_port_error:
                raise AssertionError("Proxy Port accepting Invalid range: %s" %traceback.format_exc())
        elif assert_error == 'false':
            if  self.proxy_port_error:
                raise AssertionError(" Proxy Port Valid range is 1-65534   : %s" %traceback.format_exc())       
        
    def click_on_proxy_new_exception(self):
        '''
        click on new exception button
        '''
        self.buy_time()
        logger.debug("SystemPage :ProxyPage - clicking on New button")
        self.create_new_proxy.click()
        if not self.new_exception_textbox:
            self.page_down()
            self.create_new_proxy.click()
        
    def set_proxy_exception_value(self,value):
        '''
        set value for Proxy exception textbox
        '''
        if value == None:
            logger.debug("SystemPage :ProxyPage - set  value for 'SERVER' textbox")
            self.new_exception_textbox.set('')
        else:
            logger.debug("SystemPage :ProxyPage - set  value for 'SERVER' textbox")
            self.new_exception_textbox.set(value)
            
    def assert_proxy_exception_error(self,assert_error):
        '''
        Asserting Proxy exception textbox error message
        '''
        if assert_error == 'true':
            if not self.proxy_exception_error:
                raise AssertionError("Proxy exception accepting Invalid Host or IP Address: %s" %traceback.format_exc())
        elif assert_error == 'false':
            if  self.proxy_exception_error:
                raise AssertionError(" Invalid Host or IP Address given for Proxy exception  : %s" %traceback.format_exc())         
    
    def click_on_proxy_exception_ok(self):
        '''
        clicking on save button
        '''
        self.buy_time()
        logger.debug("SystemPage :ProxyPage - clicking on ok button")
        self.save_proxy_exception.click()   
        
    def click_on_cancel_settings(self):
        '''
        clicking on cancel button
        '''
        self.buy_time()
        logger.debug("SystemPage :ProxyPage - clicking on cancel button")
        self.cancel.click()
    def set_virtual_controller_ip(self,ip):
        '''
        writes given ip in virtual controller ip fields
        '''
        logger.debug("Services: writing vc ip")
        self.vc_ip_textbox.set(ip)
        
    def edit_virtual_controller_ip_values(self):
        '''
        clicks on edit values button
        '''
        logger.debug("SystemPage : Click 'Edit Values' button")
        self.edit_values_ip.click()
        if not self.vc_ip_edit_icon:
            self.edit_values_ip.click()
        time.sleep(5)
        
    def edit_virtual_controller_ip_address(self):
        '''
        clicks on edit icon
        '''
        logger.debug("SystemPage : Clicking on edit icon ")
        self.vc_ip_edit_icon.click()
        if not self.vc_ip_textbox:
            self.vc_ip_edit_icon.click()
        #self.save_vc_ip.click()

    def save_virtual_controller_ip_address(self):
        '''
        clicks on save button
        '''
        self.save_vc_ip.click()
        logger.debug("SystemPage : Click 'Save' button")
        self.save_ip.click()

    def set_timezone(self,timezonevalue):
        '''
        selects given option for time zone
        '''
        logger.debug("SystemPage : selecting timezone")
        self.timezone.set(timezonevalue)
        
    def set_prefered_band(self,preferedband):
        '''
        selects given option for prefered band 
        '''
        logger.debug("SystemPage : selecting prefered band")
        self.preferred_band.set(preferedband)
        
    def set_ntp_server(self,ntp):
        '''
        writes given value into ntp server field 
        '''
        logger.debug("SystemPage : writing ntp server")
        self.ntp_server.set(ntp)
        
    def set_vc_netmask(self,netmask):
        '''
        writes given value into virtual controller netmask
        '''
        logger.debug("SystemPage : writing vc netmask")
        self.gen_vc_netmask.set(netmask)

    def set_vc_gateway(self,gateway):
        '''
        writes given value into virtual controller gateway
        '''
        logger.debug("SystemPage : writing vc gateway")
        self.gen_vc_gateway.set(gateway)
        
    def set_vc_vlan(self,vlan):
        '''
        writes given value into virtual controller vlan
        '''
        logger.debug("SystemPage : writing vc vlan")
        self.gen_vc_vlan.set(vlan)

    def set_dyanamic_cpu_utilization(self,option):
        '''
        writes given value into virtual controller vlan
        '''
        logger.debug("SystemPage : Selecting dynamic cpu utilization")
        self.dynamic_cpu_utilization.set(option)
        
    def assert_vc_vlan(self,option):
        '''
        assert vlan error message
        '''
        if option == 'true':
            if not self.vc_vlan_error:
                raise AssertionError('* Must be number in range 1-4093 message is not displayed')
        if option == 'false':
            if self.vc_vlan_error:
                raise AssertionError('* Must be number in range 1-4093 message is displayed for valid input')
                
    def assert_vc_ip(self, option):         
        '''
        assert vlan ip error message
        '''
        self.save_vc_ip.click()
        if option == 'true':
            if not self.invalid_ip_address_msg:
                raise AssertionError('Invalid Ip address message is not displayed')
        if option == 'false':
            if self.invalid_ip_address_msg:
                raise AssertionError('Invalid Ip address message is displayed for valid input')

    def edit_vc_name_values(self):
        ''''
        clicks on edit values
        '''
        logger.debug("SystemPage : Click 'Edit Values' button")
        self.edit_values_name.click()
        if not self.vc_name_edit_icon:
            self.edit_values_name.click()
        time.sleep(7)
        
    def edit_vc_name_icon(self):    
        '''
        clicks on edit icon
        '''
        logger.debug("SystemPage : Clicking on edit icon ")
        self.vc_name_edit_icon.click()
        if not self.vc_name_textbox:
            self.vc_name_edit_icon.click()
    
    def set_vc_name(self,name):
        '''
        writes vc name 
        '''
        logger.debug("SystemPage : Write VC name into the text-box")
        self.vc_name_textbox.set(name)
        # self.vc_name_textbox.set(self.config.config_vars.vc_name)
        
    def save_vc_name(self):
        '''
        clicks on save button
        '''
        logger.debug("SystemPage : Click 'Save' button")
        self.save_vc_name_id.click()
        self.save_name.click()
        time.sleep(7)

    def save_int_vc_name(self):
        '''
        clicks on save button
        '''
        logger.debug("SystemPage : Click internal 'Save' button")
        self.save_vc_name_id.click()
        time.sleep(7)

    def assert_vc_name(self,option):
        '''
        asserts error message for vc name
        '''
        #due to bug
        if option == 'true':
            if not self.invalid_vc_name_msg:
                raise AssertionError('Invalid VC Name message is not displayed')
        if option == 'false':
            if self.invalid_vc_name_msg:
                raise AssertionError('Invalid VC Name message is displayed for valid input')
                    
    def set_general_dynamic_proxy(self, option):
        '''
        slects given option for dyanamic proxy
        '''
        if option == 'enabled':
            self.dynamic_radius_proxy.set(self.config.config_vars.manage_internet_failover_value)
        if option == 'disabled':
            self.dynamic_radius_proxy.set(self.config.config_vars.auto_join_mode_new_value)

    def enable_help(self):
        '''
        clicks on help button
        '''
        time.sleep(8)
        logger.debug("SystemPage : Clicking help icon")
        self.help_button.click()

    def assert_help_option(self):
        '''
        asserting help content
        '''
        time.sleep(8)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.authentication_label).perform()
        if not self.help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(5)

    def assert_syslog_facility_levels_default_values(self):
        test_case = TestCase(self.config)
        path = self.config.config_vars

        logger.debug("SystemPage : Asserting the DEFAULT value of SYSLOG LEVEL")
        test_case.assertEquals(self.syslog_level.get_selected() ,  path.Warning , "value of 'SYSLOG LEVEL' was not set to Warning")

        logger.debug("SystemPage :  Asserting the DEFAULT value of AP-DEBUG")
        test_case.assertEquals(self.ap_debug.get_selected() ,  path.Warning , "value of 'AP-DEBUG' was not set to Warning")

        logger.debug("SystemPage :  Asserting the DEFAULT value of NETWORK")
        test_case.assertEquals(self.network.get_selected() , path.Warning , "value of 'NETWORK' was not  set to Warning")

        logger.debug("SystemPage :  Asserting the DEFAULT value of SECURITY")
        test_case.assertEquals(self.security.get_selected() ,  path.Warning , "value of 'SECURITY' was not set to Warning")

        logger.debug("SystemPage :  Asserting the DEFAULT value of SYSTEM")
        test_case.assertEquals(self.system.get_selected() ,  path.Warning , "value of 'SYSTEM' was not  set to Warning")

        logger.debug("SystemPage :  Asserting the DEFAULT value of USER")
        test_case.assertEquals(self.user.get_selected() ,  path.Warning , "value of 'USER' was not set to Warning")

        logger.debug("SystemPage :  Asserting the DEFAULT value of USER-DEBUG")
        test_case.assertEquals(self.user_debug.get_selected() ,  path.Warning , "value of 'USER-DEBUG' was not set to Warning")

        logger.debug("SystemPage :  Asserting the DEFAULT value of WIRELESS")
        test_case.assertEquals(self.wireless.get_selected() , path. Warning , "value of 'WIRELESS' was not set to Warning")

    def assert_syslog_server(self):
        '''
        asserting sysylog server
        '''
        logger.debug("SystemPage : Check whether the Syslog server textbox is empty. ")
        if self.syslog_server:
            if not self.syslog_server.get() == '' :
                raise AssertionError("Syslog server textbox is not empty.Traceback: %s " %traceback.format_exc())

    def assert_tftp_dump_server(self):
        '''
        asserting tftp_dump_server
        '''
        logger.debug("SystemPage : Check whether the TFTP Dump Server textbox is empty. ")
        if self.tftp_dump_server:
            if not self.tftp_dump_server.get() == '' :
                raise AssertionError("TFTP Dump Server textbox is not empty.Traceback: %s " %traceback.format_exc())
            
    def assert_help_option_for_general_accordion(self):
        '''
        asserts help text
        '''
        time.sleep(8)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.name_label).perform()
        if not self.help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(5)
            
    def non_default_values_for_proxy_exception(self):
        conf=self.config.config_vars
        self.click_on_proxy_new_exception()
        logger.debug("ProxyPage: Setting pro exception value ")
        self.set_proxy_exception_value(conf.valid_Proxy_exception_value1)
        logger.debug("ProxyPage: Click Ok button")
        self.click_on_proxy_exception_ok()
        
        self.click_on_proxy_new_exception()
        logger.debug("ProxyPage: Setting pro exception value ")
        self.set_proxy_exception_value(conf.valid_Proxy_exception_value2)
        logger.debug("ProxyPage: Click Ok button")
        self.click_on_proxy_exception_ok()
        
        self.click_on_proxy_new_exception()
        logger.debug("ProxyPage: Setting pro exception value ")
        self.set_proxy_exception_value(conf.valid_Proxy_exception_value3)
        logger.debug("ProxyPage: Click Ok button")
        self.click_on_proxy_exception_ok()
        
        self.click_on_proxy_new_exception()
        logger.debug("ProxyPage: Setting pro exception value ")
        self.set_proxy_exception_value(conf.valid_Proxy_exception_value4)
        logger.debug("ProxyPage: Click Ok button")
        self.click_on_proxy_exception_ok()
        
        self.click_on_proxy_new_exception()
        logger.debug("ProxyPage: Setting pro exception value ")
        self.set_proxy_exception_value(conf.valid_Proxy_exception_value5)
        logger.debug("ProxyPage: Click Ok button")
        self.click_on_proxy_exception_ok()
        
        self.click_on_proxy_new_exception()
        logger.debug("ProxyPage: Setting pro exception value ")
        self.set_proxy_exception_value(conf.valid_Proxy_exception_value6)
        logger.debug("ProxyPage: Click Ok button")
        self.click_on_proxy_exception_ok()
    
    def delete_proxy_multiple_exceptions(self,value):
        '''
        Delete Proxy Exception
        '''
        for i in range(1,value):
            self.Proxy_exception0.click()
            self.buy_time()

    def assert_help_option_for_uplink_accordion(self):
        '''
        assert help text
        '''
        time.sleep(8)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.country_label).perform()
        if not self.help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(5)
        
    def set_syslog_server(self, ip):
        '''
        write sysylog server ip
        '''
        logger.debug('SystemPage : Writing sysylog server')
        self.syslog_server.set(ip)

    def set_tftp_dump_server(self, ip):
        '''
        write tftp_dump_server ip
        '''
        logger.debug('SystemPage : Writing session remote end id')
        self.tftp_dump_server.set(ip)

    def assert_help_option_for_logging(self):
        '''
        asserting help content
        '''
        time.sleep(8)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.system_label).perform()
        if not self.syslog_help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(5)   
        
    def wispr_accordion(self):
        '''
            Clicking on WISPR Accordion
        '''
        logger.debug("SystemPage : Clicking WISPR accordion")
        self.wispr.click()
        if not self.iso_code:
            self.wispr.click()
    
    def set_iso_country_code(self,value=None):
        '''
            Setting value in ISO Country Code
        '''
        logger.debug("SystemPage : Setting iso country code value")
        if value:
            self.iso_code.set(value)
        else:
            self.iso_code.set("")
    
    def set_164_area_code(self,value=None):
        '''
            Setting value in E 164 Area Code
        '''
        logger.debug("SystemPage : Setting iso country code value")
        if value:
            self.e164_area_code.set(value)
        else:
            self.e164_area_code.set("") 
    
    def set_operator_name(self,value=None):
        '''
            Setting value in Operator Name
        '''
        logger.debug("SystemPage : Setting iso country code value")
        if value:
            self.operator_name.set(value)
        else:
            self.operator_name.set("")
    
    def set_164_country_code(self,value=None):
        '''
            Setting value in E 164 Country Code
        '''
        logger.debug("SystemPage : Setting iso country code value")
        if value:
            self.e164_country_code.set(value)
        else:
            self.e164_country_code.set("")
    
    def set_ssid_zone(self,value=None):
        '''
            Setting value in SSID/ZONE
        '''
        logger.debug("SystemPage : Setting iso country code value")
        if value:
            self.ssid_zone.set(value)
        else:
            self.ssid_zone.set("")
    
    def set_location_name(self,value=None):
        '''
            Setting value in Location Name
        '''
        logger.debug("SystemPage : Setting iso country code value")
        if value:
            self.location_name.set(value)
        else:
            self.location_name.set("")
    
    def assert_wispr_default_values(self):
        '''
            Asserting the default value of WISPR fields
        '''
        if not self.iso_code.get() == "":
            raise AssertionError("Default value is not set for iso country code")
        if not self.e164_area_code.get() == "":
            raise AssertionError("Default value is not set for E 164 area code")
        if not self.operator_name.get() == "":
            raise AssertionError("Default value is not set for Operation name")
        if not self.e164_country_code.get() == "":
            raise AssertionError("Default value is not set for E 164 country code")
        if not self.ssid_zone.get() == "":
            raise AssertionError("Default value is not set for SSID/ZONE")
        if not self.location_name.get() == "":
            raise AssertionError("Default value is not set for Location name")
    
    def set_wispr_default_value(self):
        '''
            Setting the default value of WISPR fields
        '''
        logger.debug("SystemPage : Setting iso country code default value")
        self.iso_code.clear()
        logger.debug("SystemPage : Setting e 164 area code default value")
        self.e164_area_code.clear()
        logger.debug("SystemPage : Setting operator name default value")
        self.operator_name.clear()
        logger.debug("SystemPage : Setting e 164 country code default value")
        self.e164_country_code.clear()
        logger.debug("SystemPage : Setting iso ssid/zone default value")
        self.ssid_zone.clear()
        logger.debug("SystemPage : Setting location name default value")
        self.location_name.clear()
        
        
    def assert_3g_4g_default_value(self):
        '''
            Asserting the default values under 3G/4G
        '''
        if not self.cell_usb.get() == '':
            raise AssertionError("Default value is not set for  USB type")
        if not self.cell_4g_type.get() == "":
            raise AssertionError("Default value is not set for  4G USB type")
        if not self.cell_usb_dev.get() == '':
            raise AssertionError("Default value is not set for  USB dev")
        if not self.cell_usb_tty.get() == '':
            raise AssertionError("Default value is not set for  USB tty")
        if not self.cell_usb_init.get() == '':
            raise AssertionError("Default value is not set for  USB init")
        if not self.cell_usb_dial.get() == '':
            raise AssertionError("Default value is not set for  USB dial")
        if not self.cell_usb_mode_switch.get() == '':
            raise AssertionError("Default value is not set for  USB mode switch")
        if not self.cell_usb_user.get() == '':
            raise AssertionError("Default value is not set for  USB user")
        if not self.cell_usb_password.get() == '':
            raise AssertionError("Default value is not set for  USB password")
        if not self.modem_country.get_selected() == 'None':
            raise AssertionError("Default value is not set for  Country")
        if not self.modem_isp.get_selected() == 'None':
            raise AssertionError("Default value is not set for  ISP")
        if not self.usb_auth_type.get_selected() == 'NONE':
            raise AssertionError("Default value is not set for  USB auth type")
    
    
    def assert_wi_fi_default_value(self):
        '''
            Asserting the default values under WIFI
        '''
        if not self.wifi_name.get() == '':
            raise AssertionError("Default value is not set for wifi name")
        if not self.wifi_band.get_selected() == '2.4 GHz':
            raise AssertionError("Default value is not set for Band")
        if not self.wifi_management.get_selected() == 'WPA-2 Personal':
            raise AssertionError("Default value is not set for Management")
        if not self.wifi_passphrase_format.get_selected() == '8-63 chars':
            raise AssertionError("Default value is not set for Passphrase format")
        if not self.wifi_passphrase.get() == '':
            raise AssertionError("Default value is not set for Passphrase")
            
    def assert_management_default_value(self):
        '''
            Asserting the default values under Management
        '''
        if not self.manage_enforce_uplink.get_selected() == 'None':
            raise AssertionError("Default value is not set for Enforce Uplink")
        if not self.manage_pre_empt.get_selected() == 'Enabled':
            raise AssertionError("Default value is not set for Pre-emption")
        if not self.manage_time_txt.get() == '180':
            raise AssertionError("Default value is not set for vpn_failover_timeout")
        if not self.manage_internet_failover.get_selected() == 'Disabled':
            raise AssertionError("Default value is not set for inter failover")
        if not self.uplink_priority_default_value.get_label_text() == '3G/4G':
            raise AssertionError("Default value is not set for uplink priority list")   
    
    
    def assert_pppoe_default_value(self):
        '''
            Asserting the default values under PPPOE
        '''
        if not self.pp_service_name.get() == '':
            raise AssertionError("Default value is not set for Service Name")
        if not self.pp_chap_secret1.get() == '':
            raise AssertionError("Default value is not set for Chap secret")
        if not self.pp_local_interafce.get_selected() == 'None':
            raise AssertionError("Default value is not set for Local interface")
        if not self.pp_user.get() == '':
            raise AssertionError("Default value is not set for User")
        if not self.pp_password.get() == '':
            raise AssertionError("Default value is not set for Password")
            
    def set_wifi_name(self,value=None):
        '''
        set WIFI name(ssid) 
        '''
        self.buy_time()
        if value == None:
            logger.debug("SystemPage : set value for wifi Name textbox ")
            self.wifi_name.clear()
        else:
            logger.debug("SystemPage : set value for wifi Name textbox ")
            self.wifi_name.set(value)
            
    def set_wifi_management(self,value=None):
        '''
        select value from WIFI Management Dropdown
        '''
        self.buy_time()
        if value == None:
            logger.debug("SystemPage : set value for wifi Management textbox ")
            self.wifi_management.set(self.config.config_vars.wifi_management2)
        else:
            logger.debug("SystemPage : set value for wifi Management textbox ")
            self.wifi_management.set(value)
            
    def set_wifi_passphrase_text(self,value=None):
        '''
        select value from WIFI Passphrase Textbox
        '''
        self.buy_time()
        if value == None:
            logger.debug("SystemPage : Set wifi passphrase name.")
            self.wifi_passphrase.clear()
        else:
            logger.debug("SystemPage : Set wifi passphrase name.")
            self.wifi_passphrase.set(value)     
            
    def set_wifi_passphrase_format(self,value=None):
        '''
        select value from WIFI Passphrase Textbox
        '''
        self.buy_time()
        if value:
            logger.debug("SystemPage : Set wifi passphrase Dropdown.")
            self.wifi_passphrase_format.set(self.config.config_vars.wifi_passphrase_format2)
        else:
            logger.debug("SystemPage : Set wifi passphrase Dropdown.")
            self.wifi_passphrase_format.set(self.config.config_vars.wifi_passphrase_format1)
            
    def assert_wifi_passphrase_text_error1(self,assert_error):
        '''
        Asserting WIFI Passphrase Textbox error message
        '''
        self.buy_time()
        if assert_error == 'true':
            if not self.wifi_passphrase_text_error1:
                raise AssertionError("WIFI Passphrase accepting Invalid Passphrase : %s" %traceback.format_exc())
        elif assert_error == 'false':
            if  self.wifi_passphrase_text_error1:
                raise AssertionError(" Key must be 8-63 Characters  : %s" %traceback.format_exc())
                
    def assert_wifi_passphrase_text_error2(self,assert_error):
        '''
        Asserting WIFI Passphrase Textbox error message
        '''
        self.buy_time()
        if assert_error == 'true':
            if not self.wifi_passphrase_text_error2:
                raise AssertionError("WIFI Passphrase accepting Invalid Passphrase : %s" %traceback.format_exc())
        elif assert_error == 'false':
            if  self.wifi_passphrase_text_error2:
                raise AssertionError(" Key must be 8-63 Characters  : %s" %traceback.format_exc())
    
    def set_management_enforce_uplink(self,value):
        '''
        select value from MANAGEMENT Enforce Uplink Dropdown
        '''
        self.buy_time()
        if not value:
            logger.debug("SystemPage : Set enforce uplink to wifi.")
            self.manage_enforce_uplink.set(self.config.config_vars.enforce_uplink4)
        else:
            logger.debug("SystemPage : Set enforce uplink to wifi.")
            self.manage_enforce_uplink.set(value)
            
    def set_management_Pre_emption(self,value):
        '''
        select value from MANAGEMENT pre-emption Dropdown
        '''
        self.buy_time()
        if not value:
            logger.debug('SystemPage: Selecting Pre-emption enabled')
            self.manage_pre_empt.set(self.config.config_vars.pre_emption)
        else:
            logger.debug('SystemPage: Selecting Pre-emption enabled')
            self.manage_pre_empt.set(self.config.config_vars.pre_emption1)
        
    def set_management_vpn_failover_timeout(self,value):
        '''
        set value to MANAGEMENT Vpn Failover Timedout Textbox
        '''
        self.buy_time()
        if  value == None:
            logger.debug('SystemPage: Writting default value 180 in vpn fail over time out')
            self.manage_time_txt.set(self.config.config_vars.vpn_failover_timeout)
        else:
            logger.debug('SystemPage: Writting value in vpn fail over time out')
            self.manage_time_txt.set(value)
    
    def assert_management_vpn_failover_timeout_error(self,assert_error):
        '''
        Asserting vpn_failover_timeout Textbox error message
        '''
        self.buy_time()
        if assert_error == 'true':
            if not self.manage_vpn_failover_timeout_error:
                raise AssertionError("management vpn_failover_timeout  accepting Invalid value : %s" %traceback.format_exc())
        elif assert_error == 'false':
            if  self.manage_vpn_failover_timeout_error:
                raise AssertionError("  Valid range is 0-3600 : %s" %traceback.format_exc())

    def set_management_internet_failover(self,value=None):
        '''
        set value from Management Internet Failover DropDown
        '''
        self.buy_time()
        if value:
            logger.debug("SystemPage : Changing the value of 'Manage Internet Failover' to default")
            self.manage_internet_failover.set(self.config.config_vars.manage_internet_failover_value)
        else:
            logger.debug("SystemPage : Changing the value of 'Manage Internet Failover' to default")
            self.manage_internet_failover.set(self.config.config_vars.internet_failover)
    
    def set_management_failover_internet_packet_freq(self,value=None):
        '''
        set value of Management AILOVER INTERNET PACKET SEND FREQUENC Textbox
        '''
        self.buy_time()
        if not value: 
            logger.debug("SystemPage : Write Failover Packet Send Frequency")
            self.failover_packet_send_frequency.set(self.config.config_vars.failover_packet_send_frequency)     
        else:
            logger.debug("SystemPage : Write Failover Packet Send Frequency")
            self.failover_packet_send_frequency.set(value)  
            
    def set_management_failover_packet_lost_count(self,value=None):
        '''
        set value of Management AILOVER INTERNET PACKET SEND FREQUENC Textbox
        ''' 
        self.buy_time()
        if not value: 
            logger.debug("SystemPage : Write Failover Packet Lost Frequency")
            self.failover_packet_lost_count.set(self.config.config_vars.failover_packet_lost_count)
        else:
            logger.debug("SystemPage : Write Failover Packet Lost Frequency")
            self.failover_packet_lost_count.set(value)
            
    def set_management_internet_check_timeout(self,value=None):
        '''
        set value of Management AILOVER INTERNET PACKET SEND FREQUENC Textbox
        ''' 
        self.buy_time()
        if not value: 
            logger.debug("SystemPage : Write Internet Check Timeout")
            self.internet_ckeck_timeout.set(self.config.config_vars.internet_ckeck_timeout)
        else:
            logger.debug("SystemPage : Write Internet Check Timeout")
            self.internet_ckeck_timeout.set(value)      
    
    def assert_management_packet_send_frequency_error(self,assert_error):
        '''
        Asserting packet send frequency Textbox error message
        '''
        self.buy_time()
        if assert_error == 'true':
            if not self.packet_send_frequency_error:
                raise AssertionError("Accepting Invalid values for Failover packet send frequency. i.e. Traceback: %s" %traceback.format_exc())     
        elif assert_error == 'false':
            if  self.packet_send_frequency_error:
                raise AssertionError("Valid range is 1-3600. i.e. Traceback: %s" %traceback.format_exc())       
                
    def assert_management_packet_lost_count_error(self,assert_error):
        '''
        Asserting packet lost count Textbox error message
        '''
        self.buy_time()
        if assert_error == 'true':
            if not self.packet_lost_count_error:
                raise AssertionError("Accepting Invalid values for Failover packet send frequency. i.e. Traceback: %s" %traceback.format_exc())     
        elif assert_error == 'false':
            if  self.packet_lost_count_error:
                raise AssertionError("Valid range is 1-1000. i.e. Traceback: %s" %traceback.format_exc())                   
                
    def assert_management_internet_check_timeout_error(self,assert_error):
        '''
        Asserting internet check timeout  Textbox error message
        '''
        self.buy_time()
        if assert_error == 'true':
            if not self.internet_ckeck_timeout_error:
                raise AssertionError("Accepting Invalid values for Failover packet send frequency. i.e. Traceback: %s" %traceback.format_exc())     
        elif assert_error == 'false':
            if  self.internet_ckeck_timeout_error:
                raise AssertionError("Valid range is 0-3600. i.e. Traceback: %s" %traceback.format_exc())                       
    
    def pppoe_service_name(self,value):
        '''
        write PPPOE Service Name 
        '''
        self.buy_time()
        if value == None:
            logger.debug("SystemPage : Set service name.")
            self.pp_service_name.clear()
        else:
            logger.debug("SystemPage : Set service name.")
            self.pp_service_name.set(value)
    
    def set_pp_chap_secret1(self,value):
        '''
        write PPPOE Chap Secret  
        '''
        self.buy_time()
        if value == None:
            logger.debug("SystemPage : Set chap secret.")
            self.pp_chap_secret1.clear()
        else:
            logger.debug("SystemPage : Set chap secret.")
            self.pp_chap_secret1.set(value)
    
    def set_pp_chap_secret2(self,value):
        '''
        write PPPOE Retype Chap Secret  
        '''
        self.buy_time()
        if value == None:
            logger.debug("SystemPage :  Set retype chap secret.")
            self.pp_chap_secret2.clear()
        else:
            logger.debug("SystemPage : Set retype chap secret.")
            self.pp_chap_secret2.set(value)
            
    def set_pp_password(self,value):
        '''
        write PPPOE pp password 
        '''
        self.buy_time()
        if value == None:
            logger.debug("SystemPage : Set password.")
            self.pp_password.clear()
        else:
            logger.debug("SystemPage : Set password.")
            self.pp_password.set(value)
            self.browser.key_press(u'\ue004')
        
    def set_pp_retype_password(self,value):
        '''
        write PPPOE pp Retype  password 
        '''
        self.buy_time()
        if value == None:
            logger.debug("SystemPage : Set retype password.")
            self.pp_password_retype.clear() 
        else:
            logger.debug("SystemPage : Set retype password.")
            self.pp_password_retype.set(value)
            time.sleep(3)
            self.pp_password_retype.set(value)
        
    def assert_pp_chap_secret_error(self,assert_error):
        '''
        Asserting pp chap secret Textbox error message
        '''
        self.buy_time()
        if assert_error == 'true':
            if not self.pp_chap_secret_error:
                raise AssertionError("Accepting Invalid values . i.e. Traceback: %s" %traceback.format_exc())       
        elif assert_error == 'false':
            if  self.pp_chap_secret_error:
                raise AssertionError("Fields do not match. i.e. Traceback: %s" %traceback.format_exc()) 
                
    def assert_password_error(self,assert_error):
        '''
        Asserting password  Textbox error message
        '''
        self.buy_time()
        if assert_error == 'true':
            if not self.pp_password_error:
                raise AssertionError("Accepting Invalid values . i.e. Traceback: %s" %traceback.format_exc())       
        elif assert_error == 'false':
            if  self.pp_password_error:
                raise AssertionError("Fields do not match. i.e. Traceback: %s" %traceback.format_exc()) 

    def assert_enterprise_domain_names_empty(self):
        '''
        asserting enterprise_domain_names is empty
        '''
        logger.debug("SystemPage : Check whether the enterprise_domains table of enterprise_domain_names is empty. ")
        if not self.enterprise_domains_table_no_data_msg:
            raise AssertionError("enterprise domain table is not empty i.e . Traceback: %s" % traceback.format_exc())   

    def create_new_domain(self):
        '''
        clicks on 'NEW' button for creating new domain in enterprise_domain_names
        '''
        logger.debug("SystemPage : Clicking on 'NEW' button to create new domain. ")
        self.new_domain.click()
        time.sleep(3)
        
    def assert_enter_new_domain_name_popup_textbox_empty(self):
        '''
        asserts popUp-'Enter New domain name' textbox is empty 
        '''
        logger.debug("SystemPage : Check whether the textbox of 'Enter new domain name' popUp is empty. ")
        if not self.domain_name.get()=='':
            raise AssertionError("'Enter new domain name' popUp textbox is not empty i.e . Traceback: %s" % traceback.format_exc())
            
    def assert_invalid_enterprise_domain_name_and_ip(self, domain_name):
        '''
        asserts error message for invalid enterprise domain name/ip address
        '''
        #due to bug
        path = self.config.config_vars
        if domain_name == path.domain_name_invalid:
            self.set_domain_name_value(domain_name)
            self._save_domain()
            logger.debug("SystemPage : Click 'Save Settings' button")
            self._save_settings()
            if not self.invalid_domain_name_msg:
                raise AssertionError('Invalid domain name message is not displayed')
        if domain_name == path.domain_ip_invalid:
            self.set_domain_name_value(domain_name)
            self._save_domain()
            logger.debug("SystemPage : Click 'Save Settings' button")
            self._save_settings()
            if not self.invalid_domain_ip_msg:
                raise AssertionError('Invalid domain Ip address message is not displayed')
                
    def set_domain_name_value(self , domain_name):
        '''
        Enters the domain value in 'Enter new domain name' textbox
        '''
        logger.debug("SystemPage : Entering the domain value : '%s'. "%domain_name)
        self.domain_name.set(domain_name)
        time.sleep(2)
        
    def _save_domain(self):
        '''
        Clicking on 'OK' button to save domain name
        '''
        logger.debug("SystemPage : Clicking on 'OK' button to save domain. ")
        self.save_domain.click()
        time.sleep(3)
        
    def click_new_snmp_button(self):
        '''
        Clicks on 'NEW' button to create new snmp.
        '''
        logger.debug("SystemPage : Clicking on 'New' button to create new SNMP. ")
        self.new_snmp_button.click()
        time.sleep(2)
        
    def click_new_snmpv3_button(self):
        '''
        Clicks on 'NEW' button to create new snmpv3.
        '''
        logger.debug("SystemPage : Clicking on 'New' button to create new SNMPv3. ")
        self.snmpv3_new_button.click()
        time.sleep(2)

    def click_new_snmp_trap_button(self):
        '''
        Clicks on 'NEW' button to create new snmpv3.
        '''
        logger.debug("SystemPage : Clicking on 'New' button to create new SNMPv3. ")
        self.snmp_trap_new_button.click()
        time.sleep(2)

    def set_snmp_value(self, snmp_string):
        '''
        Enters the snmp string.
        '''
        logger.debug("SystemPage : Entering SNMP string to text-box. ")
        self.snmp_community_string_textbox.set(snmp_string)
        self.snmp_save_new_community.click()
        time.sleep(3)
        
    def assert_invalid_snmp_string_error(self):
        '''
        Asserts invalid snmp string error message.
        '''
        #due to bug
        logger.debug("SystemPage : Checking for snmp invalid string error message. ")
        if not self.proxy_port_error:
            raise AssertionError("Invalid snmp error message is not displaced.Traceback: %s " %traceback.format_exc())
            
    def click_snmp_cancel_button(self):
        '''
        Clicks on 'CANCEL' button of SNMP
        '''
        logger.debug("SystemPage : Clicking on 'CANCEL' button of SNMP. ")
        self.snmp_cancel_button.click()
        time.sleep(2)
        
        
    def set_snmpv3_user_value(self, snmpv3_user):
        '''
        Enters the snmpv3 user name.
        '''
        logger.debug("SystemPage : Entering SNMPV3 user name to text-box. ")
        self.snmpv3_user_name.set(snmpv3_user)
        time.sleep(3)
        
    def click_save_snmpv3_user(self):
        '''
        Clicking on 'OK' button to save snmpv3 user
        '''
        logger.debug("SystemPage : Clicking 'OK' button to save snmpv3 user. ")
        self.snmpv3_save_snmp_user_button.click()
        time.sleep(3)

    def assert_snmpv3_empty_password_error(self):
        '''
        Asserting for empty password error.
        '''
        logger.debug("SystemPage : Checking for empty password error. ")
        if not self.snmpv3_pwd_required_error1 and not self.snmpv3_pwd_required_error2:
            raise AssertionError("Empty password error is not displayed .Traceback: %s " %traceback.format_exc())

    def assert_snmpv3_password_mismatch_error(self):
        '''
        Asserting for password mismatch error.
        '''
        logger.debug("SystemPage : Checking for password mismatch error. ")
        if not self.snmpv3_password_mismatch_error1 and not self.snmpv3_password_mismatch_error2:
            raise AssertionError("Password mismatch error is not displayed .Traceback: %s " %traceback.format_exc())
            
    def click_snmpv3_cancel_button(self):
        '''
        Clicking on SNMPV3 cancel button
        '''
        logger.debug("SystemPage : Clicking on snmpv3 'CANCEL' button. ")
        self.snmpv3_cancel_button.click()
        time.sleep(2)
        
    def set_default_uplink_priority_list(self):
        '''
        set default uplink Priority list 
        '''
        for i in range(1,10):
            if not self.uplink_priority_default_value.get_label_text() == '3G/4G':
                self.uplink_priority_3g_4g.click()
                if self.arrow_up_disabled:
                    break
                logger.debug("SystemPage : Click on arrow up .")
                self.arrow_up.click()
        self.buy_time()
    
    def set_uplink_priority_list_wifi_first(self):
        '''
        set  Uplink first Priority list as wifi-sta
        '''
        for i in range(1,2):
            if not  self.uplink_priority_default_value.get_label_text() == 'Wifi-sta':
                self.uplink_priority_Wifi_sta.click()
                if self.arrow_up_disabled:
                    break
                else:
                    logger.debug("SystemPage : Click on arrow up .")
                    self.arrow_up.click()
    
    def set_uplink_priority_list_Eth0_second(self):
        '''
        set  Uplink second Priority list as Eth0
        '''
        logger.debug("SystemPage : Click on 'Eth0' in uplink priority list")
        self.uplink_priority_Eth0.click()
        if self.arrow_up and self.arrow_down :
            pass
        else:
            logger.debug("SystemPage : Click on arrow up .")
            self.arrow_up.click()
    
    def set_pp_user(self,value):
        '''
        write PPPOE pp User 
        '''
        self.buy_time()
        if value == None:
            logger.debug("SystemPage : Set User.")
            self.pp_user.clear()
        else:
            logger.debug("SystemPage : Set User.")
            self.pp_user.set(value)
            
    def assert_syslog_server_ip(self):
        if self.invalid_ip:
            return True
        else:
            raise AssertionError(" Syslog server invalid ip address error msg not shown .i.e Traceback: %s " %traceback.format_exc())
            
    def set_enterprise_domain_non_default_values(self,values):  
        '''
        set values for enterprise Domain 
        '''
        self.create_new_domain()
        logger.debug("SystemPage : Setting domain name value")
        self.set_domain_name_value(values)
        logger.debug("SystemPage : Click 'Save' button")
        self._save_domain()
    
    def delete_created_domains(self):
        for i in range(1,9):
            self.delete.click()
            
    def assert_empty_snmp_community_string_table(self):
        '''
            asserts empty table
        '''
        if not self.community_string_no_data :
            raise AssertionError("SNMP Community string table is not empty")
    
    def assert_empty_user_for_snmpv3_table(self):
        '''
            asserts empty table
        '''
        if not self.snmpv3_no_data :
            raise AssertionError("SNMPV3 table is not empty")


    def assert_empty_snmp_traps_table(self):
        '''
            asserts empty table
        '''
        if not self.snmp_traps_no_data :
            raise AssertionError("SNMP traps table is not empty")
        
    def assert_empty_snmp_community_string(self):
        '''
        asserts empty snmp textbox
        '''
        if not self.snmp_community_string_textbox.get() == '':
            raise AssertionError('SNMP string is not empty')
        
    def assert_snmpv3_deafault_name(self):
        '''
        asserts snmpv3 default name 
        '''
        if not self.snmpv3_user_name.get() == '':
            raise AssertionError('By Deault user name is not empty')

    def assert_snmpv3_default_auth_protocol(self):
        '''
        asserts default auth protocol value
        '''
        if not self.snmpv3_auth_protocol.get_selected() == self.config.config_vars.default_smpv3_auth_protocol :
            raise AssertionError('Auth protocol is not set to default value')
            
    def assert_snmpv3_default_privacy_protocol(self):
        '''
        asserts default privacy protocol
        '''
        if not self.des_privacy_protocol :
            raise AssertionError('Privacy protocol is not set to DES')
            
    def assert_snmpv3_default_password_values(self):
        '''
        asserts empty password fields
        '''
        if not self.snmp_user_auth_password.get() == '':
            raise AssertionError('SNMP auth passoword field is not empty')
        if not self.snmp_user_auth_re_password.get() == '':
            raise AssertionError('SNMP auth retype-passoword field is not empty')
        if not self.snmp_user_privacy_password.get() == '':
            raise AssertionError('SNMP privacy passoword field is not empty')
        if not self.snmp_user_privacy_re_password.get() == '':
            raise AssertionError('SNMP privacy retype-passoword field is not empty')
            
    def assert_default_snmp_trap_ip_address(self):
        '''
        asserts default ip address field
        '''
        if not self.snmp_trap_ip_field.get_attribute_value('placeholder') == self.config.config_vars.default_ip :
            raise AssertionError('IP address is not set to xxx.xxx.xxx.xxx')
    
    def assert_default_version(self):
        '''
        asserts default version
        '''
        if not self.snmp_trap_reciever_trap_version.get_selected() == self.config.config_vars.version:
            raise AssertionError('Version is not set to V2C')

    def assert_default_port(self):
        '''
        assret default port no
        '''
        if not self.snmp_port.get() == '162':
            raise AssertionError('Port is not set to 162')
    
    def assert_default_snmp_inform(self):
        '''
        assret default inform
        '''
        if not self.snmp_inform.get_selected() == self.config.config_vars.default_inform:
            raise AssertionError('Inform is not set to Yes')
    
            
    def assert_community_user_name(self):
        '''
        asserts default commnity user name
        '''
        if not self.snmp_trap_reciever_trap_version.get_selected() == self.config.config_vars.version:
            raise AssertionError('Version is not set to V2C')

    def cancel_trap_settings(self):
        '''
        clicks on cancel button
        '''
        logger.debug('Click cancel button')
        self.cancel_traps.click()

    def assert_snmp_trap_invalid_ip(self):
        '''
        Asserting for SNMP_trap invalid ip address error.
        '''
        logger.debug("SystemPage : Checking for snmp_trap invalid ip adress error. ")
        self.set_snmp_trap_ip_address(self.config.config_vars.snmp_trap_invalid_ip_address)
        self.click_save_traps()
        if not self.snmp_trap_invalid_ip_error:
            raise AssertionError("Invalid IP address message is not dispayed .Traceback: %s " %traceback.format_exc())
        
    def click_save_traps(self):
        '''
        Clicks on snmp_trap 'OK' button
        '''
        logger.debug("SystemPage : Clicking on snmp_trap 'OK' button ")
        self.save_traps.click()
        time.sleep(2)
                
    def set_snmp_trap_ip_address(self,ip_address):
        '''
        Setting values for SNMP_trap ip_address value 
        '''
        logger.debug("SystemPage : Setting value for snmp_trap ip_address field. ")
        self.snmp_trap_ip_field.set(ip_address)
        time.sleep(2)


    def set_snmp_trap_community_name(self,community_name):
        '''
        Setting snmp_trap community name 
        '''
        logger.debug("SystemPage : Setting value for snmp_trap ip_address field. ")
        self.community_name.set(community_name)
        time.sleep(2)

    def set_snmp_trap_port_value(self,port_value):
        '''
        Setting snmp_trap port_value 
        '''
        logger.debug("SystemPage : Setting value for snmp_trap port_value. ")
        self.snmp_port.set(port_value)
        time.sleep(2)
        
    def set_snmp_user_password(self,password,retype_password):
        '''
        Enters the snmp user password.
        '''
        logger.debug("SystemPage : Enters the password in snmp user password fields. ")
        logger.debug("SystemPage : Setting auth password ")
        self.snmp_user_auth_password.set(password)
        logger.debug("SystemPage : Setting auth re password ")
        self.snmp_user_auth_re_password.set(retype_password)
        time.sleep(2)

    def set_snmp_user_privacy_password(self,password,retype_password):
        '''
        Enters the snmp user privacy_password fields.
        '''
        logger.debug("SystemPage : Enters the password in snmp user retype_password field. ")
        self.snmp_user_privacy_password.set(password)
        self.snmp_user_privacy_re_password.set(retype_password)
        time.sleep(2)

    def assert_snmp_trap_invalid_port_value(self):
        '''
        Asserting snmp_traps invalid port number
        '''
        logger.debug("SystemPage : Asserting snmp_traps invalid port number. ")
        self.set_snmp_trap_port_value(self.config.config_vars.snmp_trap_invalid_port_value)
        self.click_save_traps()
        if not self.snmp_trap_invalid_ip_error():
            raise AssertionError("'port no should be in range 0-65535' is not displayed .Traceback: %s " %traceback.format_exc())
    
    def set_version(self, version):
        '''
        selects given option for version
        '''
        logger.debug('SystemPage : selecting version')
        self.snmp_trap_reciever_trap_version.set(version)
        
    def set_inform(self, version):
        '''
        selects given option for version
        '''
        logger.debug('SystemPage : selecting inform')
        self.snmp_inform.set(version)

    def set_auth_protocol(self, protocol):
        '''
        selects given option for version
        '''
        logger.debug('SystemPage : selecting inform')
        self.snmpv3_auth_protocol.set(protocol)
    
    def delete_snmp_community_string_settings(self):
        '''
        Deleting SNMP community string settings.
        '''
        if self.delete_snmp_button:
            logger.debug("SystemPage : Deleting SNMP community string settings. ")
            self.delete_snmp_button.click()
            time.sleep(2)

    def delete_snmpv3_user_settings(self):
        '''
        Deleting SNMPV3 user settings.
        '''
        if self.delete_snmp_user:
            logger.debug("SystemPage : Deleting SNMPV3 user settings. ")
            self.delete_snmp_user.click()
            time.sleep(2)

    def delete_snmp_trap_settings(self):
        '''
        Deleting SNMP_trap user settings.
        '''
        if self.delete_traps:
            logger.debug("SystemPage : Deleting SNMP trap settings. ")  
            self.delete_traps.click()

    def edit_community_string(self):
        '''
        clicks on edit button
        '''
        logger.debug('SystemPage : Clicking on edit button')
        self.edit_comm_string.click()
        
    def edit_snmpv3_user_settings(self):
        '''
        Clicks on Edit icon to edit snmpv3 user settings
        '''
        logger.debug("SystemPage : Clicking on edit icon to edit SNMP user settings. ")
        self.edit_snmp_user.click()
        time.sleep(2)

    def edit_snmpv_traps_settings(self):
        '''
        Clicks on Edit icon to edit snmp traps settings
        '''
        logger.debug("SystemPage : Clicking on edit icon to edit SNMP traps settings. ")
        self.edit_trap.click()
        time.sleep(2)       
        
        
    def click_new_vc_ip_address(self):
        logger.debug("SystemPage : Clicks on new button under VC IP address  .")
        self.new_vc_ip_address.click()
        
    def click_new_subnet(self):
        logger.debug("SystemPage : Clicks on new button under Subnet .")
        self.new_subnet.click()
        
    def click_save_vc(self):
        logger.debug("SystemPage : Clicks on save button under VC IP address .")
        self.save_vc.click()
        self.buy_time()
        
    def click_save_subnet(self):
        logger.debug("SystemPage : Clicks on save button under Subnet .")
        self.save_subnet.click()
        self.buy_time()
            
    def create_virtual_controller(self,ip):
        logger.debug("SystemPage : Set virtual controller ip address.")
        self.vc_ip_address.set(ip)
        
    def create_subnet(self,address,mask,vlanid,vcip):
        logger.debug("SystemPage : Set subnet address.")
        self.subnet_address.set(address)
        logger.debug("SystemPage : Set subnet mask.")
        self.subnet_mask.set(mask)
        logger.debug("SystemPage : Set vlan id.")
        self.vlan_id.set(vlanid)
        logger.debug("SystemPage : Set virtual controller ip address.")
        self.subnet_vc_ip.set(vcip)
        
        
    def set_home_agent_load_balancing(self, option):
        '''
        slects given option for home agent load balancing
        '''
        if option == 'enabled':
            self.home_agent_load_balance.set(self.config.config_vars.sys_enable)
        if option == 'disabled':
            self.home_agent_load_balance.set(self.config.config_vars.sys_disable)
                
    def set_non_default_values_proxy_exception(self,value):
        self.click_on_proxy_new_exception()
        self.set_proxy_exception_value(value)
        self.click_on_proxy_exception_ok()
        
    def delete_domain_name(self,domain_name):
        '''
        Deletes the domain_name
        '''
        logger.debug("SystemPage : Clicking on delete icon to delete domain_name. ")
        domain_name.click()
        time.sleep(2)
        
    def assert_domain_name(self,domain_name):
        '''
        Asserting the domain_name
        '''
        logger.debug("SystemPage : Asserting the domain_name. ")
        if domain_name:
            raise AssertionError("Domain is not deleted . i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(2)
    def discard_ip_address(self):
        '''
        clicks on cancel button
        '''
        logger.debug('SystemPage : L3 Mobility: clicking on cancel button')
        self.vc_ip_cancel_button.click()
        
    def assert_subnet_ip_address(self):
        '''
        asserts for invalid ip address message
        '''
        if not self.subnet_address_error:
            raise AssertionError("Accepting Invalid Subnet Address. i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_subnet_netmask(self):        
        '''
        asserts for invalid netmask message
        '''
        if not self.subnet_mask_error:
            raise AssertionError("Accepting Invalid Subnet Mask. i.e. Traceback: %s" %traceback.format_exc())
    
    def assert_subnet_vlan_id(self):
        '''
        asserts for  Must be number in range 1-4093 message
        '''
        if not self.vlan_id_error:
            raise AssertionError("Accepting Invalid vlan id. i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_subnet_vc_ip(self):
        '''
        asserts for invalid ip address message
        '''
        if not self.subnet_vc_ip_error:
            raise AssertionError("Accepting Invalid subnet vc ip. i.e. Traceback: %s" %traceback.format_exc())
    
    def cancel_subnet_settings(self):
        '''
        clicks on cancel button
        '''
        logger.debug('SystemPage : L3 Mobility : Clicking on cancel button')
        self.subnet_cancel_button.click()
        
    def assert_netmask_support_error(self):
        '''
        asserts for  "Valid subnet but not supported" message
        '''
        if not self.netmask_not_supported_error:
            raise AssertionError("Accepting Invalid subnet vc ip. i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_invalid_ip_adress(self):
        '''
        asserts for invalid ip address message
        '''
        if not self.vc_ip_address_error1:
            raise AssertionError("Accepting Invalid subnet vc ip. i.e. Traceback: %s" %traceback.format_exc())
            
            
    def assert_subnet_fields(self):
        '''
        asserts default subnet field
        '''
        if not self.subnet_address.get_attribute_value('placeholder') == self.config.config_vars.default_ip :
            raise AssertionError('IP address is not set to xxx.xxx.xxx.xxx')
            
        if not self.subnet_mask.get_attribute_value('placeholder') == self.config.config_vars.default_ip :
            raise AssertionError('IP address is not set to xxx.xxx.xxx.xxx')
            
        if not self.vlan_id.get() == '':
            raise AssertionError("Default value is not set for Password")
            
        if not self.subnet_vc_ip.get_attribute_value('placeholder') == self.config.config_vars.default_ip :
            raise AssertionError('IP address is not set to xxx.xxx.xxx.xxx')
            
            
    def assert_home_agent_load_balancing(self,check):
        if check == 'disable':
            if not self.home_agent_load_balance.get_selected() == self.config.config_vars.sys_disable :
                raise AssertionError("Default value of Home Agent Load Balancing is not set to Disabled")
                
        else :
            if not self.home_agent_load_balance.get_selected() == self.config.config_vars.sys_enable :
                raise AssertionError("Value of Home Agent Load Balancing is not set to Enabled")
        
    def set_3g_4g_country_value(self,value=None):
        '''
            Setting 3G 4G Country value
        '''
        logger.debug("SystemPage : Setting Country value")
        self.buy_time()
        if value:
            self.modem_country.set(value)
        else:
            self.modem_country.set(self.config.config_vars.none_default_value)
    
    def set_3g_4g_isp_value(self,value=None):
        '''
            Setting 3G 4G ISP value
        '''
        logger.debug("SystemPage : Setting ISP value")
        self.buy_time()
        if value:
            self.modem_isp.set(value)
        else:
            self.modem_isp.set(self.config.config_vars.none_default_value)
    
    def set_wifi_band_value(self,value=None):
        '''
            Setting WI-FI Band value
        '''
        logger.debug("SystemPage : Setting wifi Band value")
        self.buy_time()
        if value:
            self.wifi_band.set(value)
        else:
            self.wifi_band.set(self.config.config_vars.prefered_band_2_4ghz)
    
    def set_pp_user_name_value(self,value=None):
        '''
            Setting PPPoE User Name value
        '''
        logger.debug("SystemPage : Setting PPPoE User Name value")
        self.buy_time()
        if value:
            self.pp_user.set(value)
        else:
            self.pp_user.clear()
    
    def set_usb_type_value(self,value=None):
        logger.debug("SystemPage:Uplink: Setting the value of USB Type")
        if value:
            self.cell_usb.set(value)
        else:
            self.cell_usb.clear()
    
    def set_cell_4g_type_value(self,value=None):
        logger.debug("SystemPage:Uplink: Setting the value of 4G USB Type")
        if value:
            self.cell_4g_type.set(value)
        else:
            self.cell_4g_type.clear()
            
    def set_cell_usb_dev_value(self,value=None):
        logger.debug("SystemPage:Uplink: Setting the value of USB Dev")
        if value:
            self.cell_usb_dev.set(value)
        else:
            self.cell_usb_dev.clear()
            
    def set_cell_usb_tty_value(self,value=None):
        logger.debug("SystemPage:Uplink: Setting the value of USB Tty")
        if value:
            self.cell_usb_tty.set(value)
        else:
            self.cell_usb_tty.clear()
            
    def set_cell_usb_init_value(self,value=None):
        logger.debug("SystemPage:Uplink: Setting the value of USB int")
        if value:
            self.cell_usb_init.set(value)
        else:
            self.cell_usb_init.clear()
            
    def set_cell_usb_dial_value(self,value=None):
        logger.debug("SystemPage:Uplink: Setting the value of USB Dial")
        if value:
            self.cell_usb_dial.set(value)
        else:
            self.cell_usb_dial.clear()
            
    def set_cell_usb_mode_switch_value(self,value=None):
        logger.debug("SystemPage:Uplink: Setting the value of USB Mode Switch")
        if value:
            self.cell_usb_mode_switch.set(value)
        else:
            self.cell_usb_mode_switch.clear()
            
    def set_cell_usb_user_value(self,value=None):
        logger.debug("SystemPage:Uplink: Setting the value of USB User")
        if value:
            self.cell_usb_user.set(value)
        else:
            self.cell_usb_user.clear()
            
    def set_cell_usb_password_value(self,value=None):
        logger.debug("SystemPage:Uplink: Setting the value of USB Password")
        if value:
            self.cell_usb_password.set(value)
        else:
            self.cell_usb_password.clear()
            
    def set_usb_auth_type_value(self,value=None):
        logger.debug("SystemPage:Uplink: Selecting the value of USB Auth Type")
        self.buy_time()
        if value:
            self.usb_auth_type.set(value)
        else:
            self.usb_auth_type.set(self.config.config_vars.default_value_none)
        self.buy_time()
    

    def set_uplink_priority_list_eth0_first(self):
        '''
        set  Uplink first Priority list as Eth0
        '''
        for i in range(1,3):
            if not  self.uplink_priority_default_value.get_label_text() == 'Eth0':
                self.uplink_priority_Eth0.click()
            if self.up_arrow_enable:
                self.up_arrow_enable.click()

    def set_uplink_priority_list_3G_4G_second(self):
        '''
        set  Uplink second Priority list as 3G/4G
        '''
        self.uplink_priority_3g_4g.click()
        if self.arrow_up and self.arrow_down :
            pass
        else:
            logger.debug("SystemPage : Click on arrow up .")
            self.arrow_up.click()
    
    
    
    def set_default_uplink_3g_4g_setting(self):
        '''
            Setting default values of 3G/4G under Uplink
        '''
        logger.debug("SystemPage : Setting default value for Country")
        self.modem_country.set(self.config.config_vars.none_default_value)
        logger.debug("SystemPage : Setting default value for ISP")
        self.modem_isp.set(self.config.config_vars.none_default_value)
        logger.debug("SystemPage : Setting default value for USB auth type")
        self.usb_auth_type.set(self.config.config_vars.default_value_none)
        logger.debug("SystemPage : Setting default value for USB type")
        self.cell_usb.clear()
        logger.debug("SystemPage : Setting default value for 4G USB Type")
        self.cell_4g_type.clear()
        logger.debug("SystemPage : Setting default value for USB Dev")
        self.cell_usb_dev.clear()
        logger.debug("SystemPage : Setting default value for USB tty")
        self.cell_usb_tty.clear()
        logger.debug("SystemPage : Setting default value for USB init")
        self.cell_usb_init.clear()
        logger.debug("SystemPage : Setting default value for USB dial")
        self.cell_usb_dial.clear()
        logger.debug("SystemPage : Setting default value for USB mode switch")
        self.cell_usb_mode_switch.clear()
        logger.debug("SystemPage : Setting default value for USB user")
        self.cell_usb_user.clear()
        logger.debug("SystemPage : Setting default value for USB password")
        self.cell_usb_password.clear()
    
    def set_default_uplink_wi_fi_setting(self):
        '''
            Setting default values of WIFI under Uplink
        '''
        logger.debug("SystemPage : Setting default value for SSID name")
        self.wifi_name.clear()
        logger.debug("SystemPage : Setting default value for Band")
        self.wifi_band.set(self.config.config_vars.prefered_band_2_4ghz)
        logger.debug("SystemPage : Setting default value for management")
        self.wifi_management.set(self.config.config_vars.wifi_management2)
        logger.debug("SystemPage : Setting default value for Passphrase Format")
        self.wifi_passphrase_format.set(self.config.config_vars.wifi_passphrase_format1)
        logger.debug("SystemPage : Setting default value for Passphrase")
        self.wifi_passphrase.clear()
        
    
    def set_default_uplink_pppoe_setting(self):
        '''
            Setting default values of PPPOE under Uplink
        '''
        logger.debug("SystemPage : Setting default value for Service Name")
        self.pp_service_name.clear()
        logger.debug("SystemPage : Setting default value for Chap Secret")
        self.pp_chap_secret1.clear()
        logger.debug("SystemPage : Setting default value for Retype Chap Secret")
        self.pp_chap_secret2.clear()
        logger.debug("SystemPage : Setting default value for Local Interface")
        self.pp_local_interafce.set(self.config.config_vars.none_default_value)
        logger.debug("SystemPage : Setting default value for User")
        self.pp_user.clear()
        logger.debug("SystemPage : Setting default value for Password")
        self.pp_password.clear()
        logger.debug("SystemPage : Setting default value for Retype Password")
        self.pp_password_retype.clear()
        
    def checking_non_default_value_for_3g_4g(self,country=None,isp=None,u_type=None,c_4g_type=None,u_dev=None,u_tty=None,u_init=None,u_dial=None,switch=None,auth=None,user=None,pwd=None):
        '''
            Checking non default value for 3G/4G
        '''
        logger.debug("SystemPage : Checking non default value for 3G/4G")
        if country or isp :
            self.set_3g_4g_country_value(country)
            self.set_3g_4g_isp_value(isp)
        else:
            self.set_usb_type_value(u_type)
            self.set_cell_4g_type_value(c_4g_type)
            self.set_cell_usb_dev_value(u_dev)
            self.set_cell_usb_tty_value(u_tty)
            self.set_cell_usb_init_value(u_init)
            self.set_cell_usb_dial_value(u_dial)
            self.set_cell_usb_mode_switch_value(switch)
            self.set_usb_auth_type_value(auth)
            self.set_cell_usb_user_value(user)
            self.set_cell_usb_password_value(pwd)   
    
    def checking_non_default_value_for_wifi_field(self,name=None,band=None,management=None,format=None,passphrase=None):
        '''
            Checking non default value for Wi-Fi
        '''
        logger.debug("SystemPage : Checking non default value for Wi-Fi-field")
        self.set_wifi_name(name)
        self.set_wifi_band_value(band)
        self.set_wifi_management(management)
        self.set_wifi_passphrase_format(format)
        self.set_wifi_passphrase_text(passphrase)
    
    def checking_non_default_values_for_management(self,uplink=None,preemption=None,timeout=None,i_failover=None):
        '''
            Checking Non Defaults Values for test case
        '''
        logger.debug("SystemPage : Checking Non Defaults Values for management...")
        self.set_management_enforce_uplink(uplink)
        self.set_management_Pre_emption(preemption)
        self.set_management_vpn_failover_timeout(timeout)
        self.set_management_internet_failover(i_failover)       
        
    def checking_non_default_values_for_wifi(self):
        '''
            Checking non default value for wifi testcase
        '''
        logger.debug("SystemPage : Checking non default value for wifi")
        self.set_wifi_name(self.config.config_vars.wifi_name1)
        self.set_wifi_band_value(self.config.config_vars.preferred_band_new_value)
        self.set_wifi_management(self.config.config_vars.wifi_management3)
        self.set_management_enforce_uplink(self.config.config_vars.enforce_uplink3)
        self.set_management_Pre_emption(self.config.config_vars.pre_emption1)
        self.set_management_vpn_failover_timeout(self.config.config_vars.default_least_time)
        self.set_management_internet_failover(self.config.config_vars.manage_internet_failover_value)
        self.set_management_failover_internet_packet_freq(self.config.config_vars.failover_frequency)
        self.set_management_failover_packet_lost_count(self.config.config_vars.packet_count)
        self.set_management_internet_check_timeout(self.config.config_vars.packet_count)
        
    def checking_non_default_values_for_pppoe(self,service=None,secret=None,retype_secret=None,user=None,pwd=None,retype_pwd=None):
        '''
            Checking non default value for PPPoE
        '''
        logger.debug("SystemPage : Checking non default value for PPPoE")
        self.pppoe_service_name(service)
        self.set_pp_chap_secret1(secret)
        self.set_pp_chap_secret2(retype_secret)
        self.set_pp_user_name_value(user)
        self.set_pp_password(pwd)
        self.set_pp_retype_password(retype_pwd)
        
    def set_dhcp_domain_name(self, name):
        '''
        write given name into domain name field
        '''
        logger.debug('System page: DHCP : Writing domain name')
        self.domain_name_dhcp.set(name)
        
    def set_dhcp_dns_server(self, server):
        '''
        writes given server into dns server field
        '''
        logger.debug('System page: DHCP : Writing dns server')
        self.dns_server.set(server)
        
    def set_dhcp_lease_time(self,time, unit):
        '''
        writes time and selects given unit
        '''
        logger.debug('System page : DHCP : Writing lease time')
        self.lease_time.set(time)
        logger.debug('System page : DHCP : Selecting lease time unit')
        self.least_time_dropdown.set(unit)
        
    def set_dhcp_network(self,ip):
        '''
        writes ip into dhcp network field
        '''
        logger.debug('System page : DHCP :writes given ip into network field')
        self.network1.set(ip)
        
    def set_dhcp_netmask(self,ip):
        '''
        writes ip into dhcp netmask field
        '''
        logger.debug('System page : DHCP :writes given ip into netmask field')
        self.mask.set(ip)
        
    def assert_lease_time_error(self):
        '''
        asserts for lease time valid range
        '''
        if not (self.lease_time_error or self.lease_time_range_error):
            raise AssertionError('System page : DHCP : Lease time range error is not displayed')
            
    def restore_dhcp_default_values(self):
        '''
        restores dhcp default values
        '''
        logger.debug('System page : DHCP : Restores dhcp default values')
        self.set_dhcp_domain_name('')
        self.set_dhcp_dns_server('')
        self.set_dhcp_lease_time('0', self.config.config_vars.least_time_days)
        self.set_dhcp_network('')
        self.set_dhcp_netmask('')
        self._save_settings()
        
    def assert_vc_ip_address(self):
        '''
        asserts vc ip address
        '''
        if not self.vc_ip_address.get_attribute_value('placeholder') == self.config.config_vars.default_ip :
            raise AssertionError('VC IP address is not set to xxx.xxx.xxx.xxx')
            
    def edit_vc_name_icon1(self):   
        '''
        clicks on edit icon
        '''
        logger.debug("SystemPage : Clicking on edit icon ")
        self.vc_name_edit_icon.click()
            
    def set_non_default_values_cpu_util(self,iap):
        '''
        '''
        myDevice = Device.getDeviceObject(iap)
        vlan_id = myDevice.get("vlan")
        self.set_timezone(self.config.config_vars.pacific_time_utc_07)
        self.set_prefered_band(self.config.config_vars.preferred_band_new_value)
        self.set_ntp_server(self.config.config_vars.ntp_server)
        self.set_vc_netmask(self.config.config_vars.vc_netmask)
        self.set_vc_gateway(self.config.config_vars.vc_gateway)
        self.set_vc_vlan(vlan_id)
        self.set_dyanamic_cpu_utilization(self.config.config_vars.dynamic_cpu_utilization_enable)
        
    def set_cpu_util_default_values(self):
        '''
        setting back Default values of Cpu util
        '''
        # self.set_default_vc_name()
        self.set_dropdown_value_default('timezone')
        self.set_dropdown_value_default('preferred band')
        self.set_dropdown_value_default('dynamic cpu utilization')
        self.set_ntp_server_ip()
        self.restore_virtual_controller_values()
        self._save_settings()       
    
    def set_virtual_controller_name(self,name=None):
        logger.debug("SystemPage : Click 'Edit Values' button")
        time.sleep(7)
        self.edit_values_name.click()
        time.sleep(7)
        logger.debug("SystemPage : Clicking on edit icon ")
        self.vc_name_edit_icon.click()
        logger.debug("SystemPage : Write VC name into the text-box")
        self.vc_name_textbox.set(name)
        self.vc_name_textbox.set(name)
        logger.debug("SystemPage : Click 'Save changes' button")
        self.save_vc_name_id.click()
        logger.debug("SystemPage : Click 'Save' button")
        self.save_name.click()
        time.sleep(7)
    
    def set_vc_ip_address(self,ip = None):
        logger.debug("SystemPage : Click 'Edit Values' button")
        self.edit_values_ip.click()
        time.sleep(5)
        logger.debug("SystemPage : Clicking on edit icon ")
        self.vc_ip_edit_icon.click()
        if not self.vc_ip_textbox:
            self.vc_ip_edit_icon.click()
        logger.debug("SystemPage : Write VC IP into the text-box")
        self.vc_ip_textbox.set(ip)
        self.vc_ip_textbox.set(ip)
        logger.debug("SystemPage : Click 'Save changes' button")
        self.save_vc_ip_id .click()
        logger.debug("SystemPage : Click 'Save' button")
        self.save_ip.click()
        logger.debug("SystemPage : Click Close icon button")
        if self.close_pop_up:
            self.close_pop_up.click()
    
    def check_non_default_values_vc_name(self):
        conf = self.config.config_vars
        logger.debug("SystemPage : Edit VC name")
        self.set_virtual_controller_name(conf.vc_name)
        logger.debug("SystemPage : Edit VC IP Address")
        self.set_vc_ip_address(conf.ip_add)
        logger.debug("SystemPage : Edit VC TimeZone")
        self.set_timezone(conf.pacific_time_utc_07)
        logger.debug("SystemPage : Edit VC Preferred Band")
        self.set_prefered_band(conf.prefered_band_2_4ghz)
        logger.debug("SystemPage : Edit NTP Server")
        self.set_ntp_server(conf.enterprise_domain_value5)
        logger.debug("SystemPage : Edit VC Netmask")
        self.set_vc_netmask(conf.vc_netmask)
        logger.debug("SystemPage : Edit VC Gateway")
        self.set_vc_gateway(conf.vc_gateway)
        logger.debug("SystemPage : Edit VC VLAN")
        # self.set_vc_vlan(conf.vc_valid_vlan)
        logger.debug("SystemPage: Scroll Down")
        self.page_down()
        logger.debug("SystemPage : Edit Dynamic CPU Utilization")
        self.set_dyanamic_cpu_utilization(conf.dynamic_cpu_utilization)
        
    def setting_default_values(self):
        vc_name = devices.IAP_1.vc_name
        vc_ip = devices.IAP_1.ip
        conf = self.config.config_vars
        logger.debug("SystemPage : Edit VC name")
        self.set_virtual_controller_name(vc_name)
        logger.debug("SystemPage : Edit VC IP Address")
        self.set_vc_ip_address(vc_ip)
        logger.debug("SystemPage : Edit VC TimeZone")
        self.set_timezone(conf.timezone_value)
        logger.debug("SystemPage : Edit VC Preferred Band")
        self.set_prefered_band(conf.preferred_band_value)
        logger.debug("SystemPage : Edit NTP Server")
        self.ntp_server.clear()
        logger.debug("SystemPage : Edit VC Netmask")
        self.gen_vc_netmask.clear()
        logger.debug("SystemPage : Edit VC Gateway")
        self.gen_vc_gateway.clear()
        logger.debug("SystemPage : Edit VC VLAN")
        # self.gen_vc_vlan.clear()
        logger.debug("SystemPage: Scroll Down")
        self.page_down()
        logger.debug("SystemPage : Edit Dynamic CPU Utilization")
        self.set_dyanamic_cpu_utilization(conf.dynamic_cpu_utilization_value)
        
    def set_dropdown_nondefault_value(self,auto=None,terminal=None,telnet=None,led=None,ssid=None,bridg=None,routing=None,proxy=None,mas=None,timezone1=None,band=None,utilization=None):
        path = self.config.config_vars
        time.sleep(5)
        if timezone1 :
            logger.debug("SystemPage : Set value in 'TIMEZONE' drop-down")
            self.timezone.set(timezone1)
        if band :
            logger.debug("SystemPage : Set value in 'PREFERRED BAND' drop-down")
            self.preferred_band.set(band)
        if utilization :
            logger.debug("SystemPage : Set value in 'DYNAMIC CPU UTILIZATION' drop-down")
            self.dynamic_cpu_utilization.set(utilization)
        if auto :
            logger.debug("SystemPage : Set value in 'AUTO JOIN MODE' drop-down")
            self.auto_join_mode.set(auto)
        if terminal :
            logger.debug("SystemPage : Set value in 'TERMINAL ACCESS' drop-down")
            # self.terminal_access.set(terminal)
        if telnet :
            logger.debug("SystemPage : Set value in 'TELNET SERVER' drop-down")
            self.telnet_server.set(telnet)
        if led :
            logger.debug("SystemPage : Set value in 'LED DISPLAY' drop-down")
            self.led_display.set(led)
        if ssid :
            logger.debug("SystemPage : Set value in 'EXTENDED SSID' drop-down")
            self.extended_ssid.set(ssid)
        if bridg :
            logger.debug("SystemPage : Set value in 'DENY INTER USING BRIDGING' drop-down")
            self.deny_inter_using.set(bridg)
        if routing :
            logger.debug("SystemPage : Set value in 'DENY LOCAL ROUTING' drop-down")
            self.deny_local_routing.set(routing)
        if proxy :
            logger.debug("SystemPage : Set value in 'DYNAMIC RADIUS PROXY' drop-down")
            self.dynamic_radius_proxy.set(proxy)
        if mas :
            logger.debug("SystemPage : Set value in 'MAS INTEGRATION' drop-down")
            self.mas_integration.set(mas)
        logger.debug("SystemPage : Click 'Save Settings' button")
        self._save_settings()
        if self.reboot_ok:
            time.sleep(3)
            self.reboot_ok.click()
        time.sleep(5)
        
    def set_dropdown_default_value(self, timezone1=True,band=True,utilization=True,auto=True,terminal=True,telnet=True,led=True,ssid=True,bridg=True,routing=True,proxy=True,mas=True):
        path = self.config.config_vars
        time.sleep(5)
        if timezone1 :
            logger.debug("SystemPage : Set value in 'TIMEZONE' drop-down")
            self.timezone.set(path.timezone_value)
        if band :
            logger.debug("SystemPage : Set value in 'PREFERRED BAND' drop-down")
            self.preferred_band.set(path.preferred_band_value)
        if utilization :
            logger.debug("SystemPage : Set value in 'DYNAMIC CPU UTILIZATION' drop-down")
            self.dynamic_cpu_utilization.set(path.dynamic_cpu_utilization_value)
        if auto :
            logger.debug("SystemPage : Set value in 'AUTO JOIN MODE' drop-down")
            self.auto_join_mode.set(path.sys_enable)
        if terminal :
            logger.debug("SystemPage : Set value in 'TERMINAL ACCESS' drop-down")
            # self.terminal_access.set(path.sys_enable)
        if telnet :
            logger.debug("SystemPage : Set value in 'TELNET SERVER' drop-down")
            self.telnet_server.set(path.sys_disable)
        if led :
            logger.debug("SystemPage : Set value in 'LED DISPLAY' drop-down")
            self.led_display.set(path.sys_enable)
        if ssid :
            logger.debug("SystemPage : Set value in 'EXTENDED SSID' drop-down")
            self.extended_ssid.set(path.sys_enable)
        if bridg :
            logger.debug("SystemPage : Set value in 'DENY INTER USING BRIDGING' drop-down")
            self.deny_inter_using.set(path.sys_disable)
        if routing :
            logger.debug("SystemPage : Set value in 'DENY LOCAL ROUTING' drop-down")
            self.deny_local_routing.set(path.sys_disable)
        if proxy :
            logger.debug("SystemPage : Set value in 'DYNAMIC RADIUS PROXY' drop-down")
            self.dynamic_radius_proxy.set(path.sys_disable)
        if mas :
            logger.debug("SystemPage : Set value in 'MAS INTEGRATION' drop-down")
            self.mas_integration.set(path.sys_disable)
        logger.debug("SystemPage : Click 'Save Settings' button")
        self._save_settings()
        if self.reboot_ok:
            time.sleep(3)
            self.reboot_ok.click()
        time.sleep(5)

    def set_username_and_password_field(self,user = None,password = None):
        '''
            Setting username and password
        '''
        if user:
            logger.debug("SystemPage : Write valid user-name")
            self.u_name.set(user)
        if password:
            logger.debug("SystemPage : Write password")
            self.p_word.set(password)
            self.retype_p_word.set(password)
    
    def set_admin_authentication_value(self,value=None):
        logger.debug("SystemPage : Set value in 'AUTHENTICATION' drop-down to default")
        self.admin_authentication.set(value)
    

    
    def create_new_radius_server_one(self, name = None, ip = None, key = None):
        logger.debug("SystemPage : Clicking on --New-- Option")
        self.auth_server_1.set(path.auth_server_new_value)
        logger.debug("SystemPage : Write authentication server name")
        self.auth_server_name.set(name)
        logger.debug("SystemPage : Write authentication server ip address")
        self.auth_server_ip.set(ip)
        logger.debug("SystemPage : Write authentication server shared key")
        self.auth_server_shared_key.set(key)
        logger.debug("SystemPage : Rewrite authentication server shared key")
        self.re_auth_server_shared_key.set(key)
        logger.debug("SystemPage : Click 'Save Server' button")
        self.save_server.click()
        
    def create_new_radius_server_two(self, name = None, ip = None, key = None):
        logger.debug("SystemPage : Clicking on --New-- Option")
        self.auth_server_2.set(path.auth_server_new_value)
        logger.debug("SystemPage : Write authentication server name")
        self.auth_server_name.set(name)
        logger.debug("SystemPage : Write authentication server ip address")
        self.auth_server_ip.set(ip)
        logger.debug("SystemPage : Write authentication server shared key")
        self.auth_server_shared_key.set(key)
        logger.debug("SystemPage : Rewrite authentication server shared key")
        self.re_auth_server_shared_key.set(key)
        logger.debug("SystemPage : Click 'Save Server' button")
        self.save_server.click()
        
    def create_new_tacacs_server(self, name = None, ip = None, key = None):
        logger.debug("SystemPage : Clicking on --New-- Option")
        self.auth_server_2.set(path.auth_server_new_value)
        logger.debug("SystemPage : Clicking on 'TACACS' radio button")
        self.tacacs_option.click()
        logger.debug("SystemPage : Write authentication server name")
        self.tacacs_name.set(name)
        logger.debug("SystemPage : Write authentication server ip address")
        self.tacacs_ip.set(ip)
        logger.debug("SystemPage : Write authentication server shared key")
        self.tacacs_shared_key.set(key)
        logger.debug("SystemPage : Rewrite authentication server shared key")
        self.tacacs_retype.set(key)
        logger.debug("SystemPage : Click 'Save Server' button")
        self.save_server.click()
        
    def _assert_admin_local_auth_server_fields(self):
        if not(self.auth_server_1_label and self.auth_server_2_label):
            raise AssertionError("Radius server with fallback fields not found i.e . Traceback: %s" % traceback.format_exc())
        
    def assert_auth_server_1_value(self,value=None):
        logger.debug("SystemPage : asserting the value of 'AUTH SERVER 1' drop-down")
        self.browser.assert_drop_down_value(self.auth_server_1, value, "'AUTH SERVER 1' not set to given value")
        
    def assert_auth_server_2_value(self,value=None):
        logger.debug("SystemPage : asserting the value of 'AUTH SERVER 2' drop-down")
        self.browser.assert_drop_down_value(self.auth_server_2, value, "'AUTH SERVER 2' not set to given value")
        
    def assert_admin_local_username_error_msg(self,assert_msg):
        '''
        Asserts Local Username Error message
        '''
        if assert_msg:
            logger.debug("SystemPage : Asserting  Local Username Error message")
            self.browser.assert_element(self.local_uname_error_msg,' Accepting more than 32 characters')
        else:
            logger.debug("SystemPage : Asserting Local Username Error message")
            self.browser.assert_element(self.local_uname_error_msg,'Username Error message is present',False)
        
    def assert_admin_local_pasword_error_msg(self,assert_msg):
        '''
        Asserts Local Password Error message
        '''
        if assert_msg:
            logger.debug("SystemPage : Asserting  Local Password Error message")
            self.browser.assert_element(self.local_paswd_error_msg,'Accepting more than 32 characters')
        else:
            logger.debug("SystemPage : Asserting Local Password Error message")
            self.browser.assert_element(self.local_paswd_error_msg,'Password Error message is present',False)   
        
    def validate_local_uname_passwd_field(self):
        '''
        Validates Local Username and Password fields
        '''
        self.set_username_and_password(validity = 'invalid', equality = 'mismatch')
        self.assert_admin_local_username_error_msg(assert_msg=True)
        self.assert_admin_local_pasword_error_msg(assert_msg=True)
    
    def set_admin_local_uname_and_pswrd(self,uname=False, pword=False, retype=False):
        '''
        sets Admin UserName and Password
        '''
        if uname:
            logger.debug("SystemPage : Write valid user-name")
            self.u_name.set(uname)
        if  pword:
            logger.debug("SystemPage : Write password")
            self.p_word.set(pword)
        if retype:  
            logger.debug("SystemPage : Click 'Save Settings' button")
            self.retype_p_word.set(retype)
    
    def assert_admin_viewonly_uname_error_msg(self,assert_msg):
        '''
        Asserts Local ViewOnly Error message
        '''
        if assert_msg:
            logger.debug("SystemPage : Asserting  ViewOnly Username Error message")
            self.browser.assert_element(self.viewonly_uname_error,' Accepting more than 32 characters')
        else:
            logger.debug("SystemPage : Asserting ViewOnly Username Error message")
            self.browser.assert_element(self.viewonly_uname_error,'Username Error message is present',False)
        
    def assert_admin_viewonly_pasword_error_msg(self,assert_msg):
        '''
        Asserts Local ViewOnly Error message
        '''
        if assert_msg:
            logger.debug("SystemPage : Asserting  ViewOnly Password Error message")
            self.browser.assert_element(self.viewonly_paswd_error,'Accepting more than 32 characters')
        else:
            logger.debug("SystemPage : Asserting ViewOnly Password Error message")
            self.browser.assert_element(self.viewonly_paswd_error,'Password Error message is present',False)
            
    def validate_admin_viewonly_fields(self):
        '''
        Validates Admin Viewonly Fields
        '''
        conf = self.config.config_vars
        self.view_only_non_default_values(conf.admin_invalid_u_name,conf.admin_password,conf.admin_unmatch_p_word)
        self._save_settings()
        self.assert_admin_viewonly_uname_error_msg(assert_msg=True)
        self.assert_admin_viewonly_pasword_error_msg(assert_msg=True)
    
    def assert_admin_guest_pasword_error_msg(self,assert_msg):
        '''
        Asserts Local Guest Registration Only Error message
        '''
        if assert_msg:
            logger.debug("SystemPage : Asserting  Guest Registration Only Password Error message")
            self.browser.assert_element(self.admin_password_error_mismatch,'Accepting more than 32 characters')
        else:
            logger.debug("SystemPage : Asserting Guest Registration Only Password Error message")
            self.browser.assert_element(self.admin_password_error_mismatch,'Password Error message is present',False)
    
        
    def edit_dhcp_non_default_values(self):
        conf = self.config.config_vars
        logger.debug("SystemPage : Set value in 'AUTO JOIN MODE' drop-down")
        self.auto_join_mode.set(conf.mas_integration_value)
        logger.debug("SystemPage : Set value in 'TERMINAL ACCESS' drop-down")
        # self.terminal_access.set(conf.mas_integration_value)
        logger.debug("SystemPage : Set value in 'TELNET SERVER' drop-down")
        self.telnet_server.set(conf.dynamic_radius_proxy_new_value)
        logger.debug("SystemPage : Set value in 'LED DISPLAY' drop-down")
        self.led_display.set(conf.mas_integration_value)
        logger.debug("SystemPage : Set value in 'EXTENDED SSID' drop-down")
        self.extended_ssid.set(conf.mas_integration_value)
        logger.debug("SystemPage : Set value in 'DENY INTER USING BRIDGING' drop-down")
        self.deny_inter_using.set(conf.dynamic_radius_proxy_new_value)
        logger.debug("SystemPage : Set value in 'DENY LOCAL ROUTING' drop-down")
        self.deny_local_routing.set(conf.dynamic_radius_proxy_new_value)
        logger.debug("SystemPage : Set value in 'dynamic_radius_proxy' drop-down")
        self.dynamic_radius_proxy.set(conf.dynamic_radius_proxy_new_value)
        logger.debug("SystemPage : Set value in 'mas_integration' drop-down")
        self.mas_integration.set(conf.dynamic_radius_proxy_new_value)
        
    def buy_time_2(self):
        import time
        time.sleep(1000)
        
    # def edit_vc_name(self,iap,name=None):
        # myDevice = Device.getDeviceObject(iap)
        # vcname = myDevice.get("vc_name")
        # logger.debug("SystemPage : Click 'Edit Values' button")
        # time.sleep(7)
        # self.edit_values_name.click()
        # self.browser._browser.find_element_by_xpath("//td[@title='%s']/following-sibling::td[1]/div[1]/a" %vcname).click()
        # self.browser._browser.find_element_by_xpath("//td[@title='%s']/span[2]/span[2]/input" %vcname).clear()
        # time.sleep(5)
        # self.browser._browser.find_element_by_xpath("//td[@title='%s']/span[2]/span[2]/input" %vcname).send_keys(name)
        # logger.debug("SystemPage : Click 'Save changes' button")
        # self.browser._browser.find_element_by_xpath("//td[@title='%s']/following-sibling::td[1]/div[2]/a[1]" %vcname).click()
        # logger.debug("SystemPage : Click 'Save' button")
        # self.save_name.click()
        # time.sleep(7)
        
    def set_second_virtual_controller_name(self,name=None):
        logger.debug("SystemPage : Click 'Edit Values' button")
        time.sleep(7)
        self.edit_values_name.click()
        time.sleep(7)
        logger.debug("SystemPage : Clicking on edit icon ")
        self.second_vc_name_edit_icon.click()
        logger.debug("SystemPage : Write VC name into the text-box")
        self.second_vc_name_textbox.set(name)
        self.second_vc_name_textbox.set(name)
        logger.debug("SystemPage : Click 'Save changes' button")
        self.second_save_vc_name_id.click()
        logger.debug("SystemPage : Click 'Save' button")
        self.save_name.click()
        time.sleep(7)
        
    def setting_second_vc_default_name(self):
        vc_name = devices.IAP_2.vc_name
        vc_ip = devices.IAP_2.ip
        conf = self.config.config_vars
        logger.debug("SystemPage : Edit VC name")
        self.set_second_virtual_controller_name(vc_name)
        
    def assert_system_page_vc_field_values(self, ap, command=None, expected=None):
        logger.debug("FirmwarePage : creating object of Device")
        myDevice = Device.getDeviceObject(ap)
        logger.debug("FirmwarePage : waiting to receive prompt")
        myDevice.receive("#")
        logger.debug("FirmwarePage : passing command 'show version' ")
        myDevice.transmit("%s"%command)
        logger.debug("FirmwarePage : waiting to receive prompt")
        output = myDevice.receive("#")
        if not expected in output:
            raise AssertionError("%s configuration is not pushed to Device" %expected)
        
    def set_new_vc_name(self,iap,name=None):
        myDevice = Device.getDeviceObject(iap)
        vcname = myDevice.get("vc_name")
        logger.debug("SystemPage : Click 'Edit Values' button")
        time.sleep(7)
        self.edit_values_name.click()
        logger.debug("SystemPage: Clicking on edit icon")
        self.browser._browser.find_element_by_xpath("//td[@title='%s']/following-sibling::td[1]/div[1]/a" %vcname).click()
        logger.debug("SystemPage: Clearing vc name text box")
        self.browser._browser.find_element_by_xpath("//td[@title='%s']/span[2]/span[2]/input" %vcname).clear()
        time.sleep(5)
        logger.debug("SystemPage: Writing the name of the VC")
        self.browser._browser.find_element_by_xpath("//td[@title='']/span[2]/span[2]/input").send_keys(name)
        logger.debug("SystemPage : Click 'Save changes' button")
        self.browser._browser.find_element_by_xpath("//td[@title='%s']/following-sibling::td[1]/div[2]/a[1]" %name).click()
        logger.debug("SystemPage : Click 'Save' button")
        self.save_name.click()
        time.sleep(7)
        
    def set_new_vc_ip(self,iap,ip_address=None):
        myDevice = Device.getDeviceObject(iap)
        vcip = myDevice.get("ip")
        logger.debug("SystemPage : Click 'Edit Values' button")
        time.sleep(7)
        self.edit_values_ip.click()
        logger.debug("SystemPage: Clicking on edit icon")
        time.sleep(7)
        self.browser._browser.find_element_by_xpath("//td[@title='%s']/following-sibling::td[1]/div[1]/a" %vcip).click()
        logger.debug("SystemPage: Clearing vc ip text box")
        self.browser._browser.find_element_by_xpath("//td[@title='%s']/span[2]/span[2]/input" %vcip).clear()
        time.sleep(5)
        logger.debug("SystemPage: Writing the ip of the VC")
        self.browser._browser.find_element_by_xpath("//td[@title='']/span[2]/span[2]/input").send_keys(ip_address)
        logger.debug("SystemPage : Click 'Save changes' button")
        self.browser._browser.find_element_by_xpath("//td[@title='%s']/following-sibling::td[1]/div[2]/a[1]" %ip_address).click()
        logger.debug("SystemPage : Click 'Save' button")
        self.save_ip.click()
        time.sleep(7)
        
    def setting_original_vc_name(self,iap,name=None):
        myDevice = Device.getDeviceObject(iap)
        vcname = myDevice.get("vc_name")
        logger.debug("SystemPage : Click 'Edit Values' button")
        time.sleep(7)
        self.edit_values_name.click()
        logger.debug("SystemPage: Clicking on edit icon")
        self.browser._browser.find_element_by_xpath("//td[@title='%s']/following-sibling::td[1]/div[1]/a" %name).click()
        logger.debug("SystemPage: Clearing vc name text box")
        self.browser._browser.find_element_by_xpath("//td[@title='%s']/span[2]/span[2]/input" %name).clear()
        time.sleep(5)
        logger.debug("SystemPage: Writing the name of the VC")
        self.browser._browser.find_element_by_xpath("//td[@title='']/span[2]/span[2]/input").send_keys(vcname)
        logger.debug("SystemPage : Click 'Save changes' button")
        self.browser._browser.find_element_by_xpath("//td[@title='%s']/following-sibling::td[1]/div[2]/a[1]" %vcname).click()
        logger.debug("SystemPage : Click 'Save' button")
        self.save_name.click()
        time.sleep(7)
        
    def setting_original_vc_ip(self,iap,ip_address=None):
        myDevice = Device.getDeviceObject(iap)
        vcip = myDevice.get("ip")
        logger.debug("SystemPage : Click 'Edit Values' button")
        time.sleep(7)
        self.edit_values_ip.click()
        logger.debug("SystemPage: Clicking on edit icon")
        self.browser._browser.find_element_by_xpath("//td[@title='%s']/following-sibling::td[1]/div[1]/a" %ip_address).click()
        logger.debug("SystemPage: Clearing vc ip text box")
        self.browser._browser.find_element_by_xpath("//td[@title='%s']/span[2]/span[2]/input" %ip_address).clear()
        time.sleep(5)
        logger.debug("SystemPage: Writing the ip of the VC")
        self.browser._browser.find_element_by_xpath("//td[@title='']/span[2]/span[2]/input").send_keys(vcip)
        logger.debug("SystemPage : Click 'Save changes' button")
        self.browser._browser.find_element_by_xpath("//td[@title='%s']/following-sibling::td[1]/div[2]/a[1]" %vcip).click()
        logger.debug("SystemPage : Click 'Save' button")
        self.save_ip.click()
        time.sleep(7)
        
    def check_non_default_values_vc_name_2(self,iap):
        myDevice = Device.getDeviceObject(iap)
        vlan_id = myDevice.get("vlan")
        conf = self.config.config_vars
        logger.debug("SystemPage : Edit VC TimeZone")
        self.set_timezone(conf.pacific_time_utc_07)
        logger.debug("SystemPage : Edit VC Preferred Band")
        self.set_prefered_band(conf.prefered_band_2_4ghz)
        logger.debug("SystemPage : Edit NTP Server")
        self.set_ntp_server(conf.enterprise_domain_value5)
        logger.debug("SystemPage : Edit VC Netmask")
        self.set_vc_netmask(conf.vc_netmask)
        logger.debug("SystemPage : Edit VC Gateway")
        self.set_vc_gateway(conf.vc_gateway)
        logger.debug("SystemPage : Edit VC VLAN")
        self.set_vc_vlan(vlan_id)
        logger.debug("SystemPage: Scroll Down")
        self.page_down()
        logger.debug("SystemPage : Edit Dynamic CPU Utilization")
        self.set_dyanamic_cpu_utilization(conf.dynamic_cpu_utilization)
        
    def setting_default_values_2(self):
        logger.debug("SystemPage : Edit VC TimeZone")
        self.set_timezone(conf.timezone_value)
        logger.debug("SystemPage : Edit VC Preferred Band")
        self.set_prefered_band(conf.preferred_band_value)
        logger.debug("SystemPage : Edit NTP Server")
        self.ntp_server.clear()
        logger.debug("SystemPage : Edit VC Netmask")
        self.gen_vc_netmask.clear()
        logger.debug("SystemPage : Edit VC Gateway")
        self.gen_vc_gateway.clear()
        logger.debug("SystemPage : Edit VC VLAN")
        self.gen_vc_vlan.clear()
        logger.debug("SystemPage: Scroll Down")
        self.page_down()
        logger.debug("SystemPage : Edit Dynamic CPU Utilization")
        self.set_dyanamic_cpu_utilization(conf.dynamic_cpu_utilization_value)
        
    def click_reboot_ok_button(self):
        logger.debug("SystemPage : Click on 'OK' button")
        if self.reboot_ok:
            time.sleep(3)
            self.reboot_ok.click()
        time.sleep(5)