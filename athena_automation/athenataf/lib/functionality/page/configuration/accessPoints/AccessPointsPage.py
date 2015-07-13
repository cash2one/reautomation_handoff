# Developed by : Ishan Anand
# On date : 30th Jun 2014

from athenataf.lib.util.WebPage import WebPage
import time
import logging
logger = logging.getLogger('athenataf')
import traceback
from athenataf.config import devices
from Device_Module.ObjectModule import Device
class AccessPointsPage(WebPage):
    def __init__(self, test, browser, config):
        time.sleep(5)
        WebPage.__init__(self, "AccessPoint", test, browser, config)
        self.test.assertPageLoaded(self)
        
        
    def isPageLoaded(self):
        if self.access_label:
            return True 
        else:
            return False 
        
    def click_access_point(self):
        logger.debug("AccessPointsPage : click accesspoint")
        
        time.sleep(5)
        # self.access_point.click()
        time.sleep(5)
        
        
    def edit_access_point(self):
        # logger.debug("AccessPointsPage : click accesspoint")
        # self.access_point.click()
        logger.debug("AccessPointsPage : click 'Edit' button")
        self.ap_edit_button.click()
        
        time.sleep(20)
            
    def click_radio(self):
        logger.debug("AccessPointsPage : click 'Radio' accordion")
        self.radio.click()
        
        time.sleep(8)
        
    def set_mode_to_monitor(self):
        if not self.mode_picklist.get_selected() == 'Access':
            logger.debug("AccessPointsPage: Mode not set to access by default.Traceback: %s " %traceback.format_exc())  
        logger.debug("AccessPointsPage :set mode to Monitor")
        self.mode_picklist.set(self.config.config_vars.monitor_wifi_mode)
        if not self.message:
            raise AssertionError("Reboot AP for changes to take effect. message is not found.Traceback: %s " %traceback.format_exc())
        self.click_save_settings()
        
    def click_save_settings(self):
        logger.debug("AccessPointsPage : click 'Save' button")
        time.sleep(5)
        if self.save_button:
            self.save_button.click()
            logger.debug("AccessPointsPage : click 'Continue' button")
            time.sleep(8)
            if self.reboot_popup_ok:
                self.reboot_popup_ok.click()
            time.sleep(5)
        
    def assert_arm_assigned(self):
        if not self.arm_radio_24g.is_selected():
            raise AssertionError(" default ap is not ARM assigned :%s " %traceback.format_exc())

    def set_mode_to_spectrum(self):
        logger.debug("AccessPointsPage :set value in 'SPECTRUM' drop down")
        self.mode_picklist.set(self.config.config_vars.spectrum_wifi_mode)
        self.click_save_settings()
        
    def set_mode_to_access(self):
        logger.debug("AccessPointsPage :set value in 'ACCESS' drop down")
        self.mode_picklist.set(self.config.config_vars.access_wifi_mode)
        self.click_save_settings()

        
    def set_radio_Administrator_assigned(self):
        logger.debug("AccessPointsPage : set Admin Assigned")
        self.aa_radio_24g.click()
        logger.debug("AccessPointsPage : click 'Save' button")
        self.assert_radio_administrator_assigned_fields()
        self.click_save_settings()
        
    def assert_radio_administrator_assigned_fields(self):
        logger.debug("AccessPointsPage : Searching Channel dropdown.")
        if not self.channel:
            raise AssertionError("Channel drop down not present: %s " %traceback.format_exc())
        logger.debug("AccessPointsPage : Searching transmit_power textbox.")
        if not self.transmit_power:
            raise AssertionError("Transit power not visible: %s " %traceback.format_exc())
        options = self.channel.get_options()
        for x in range(0,11):
            if not options[x] == str(x+1):
                raise AssertionError("Transit power not visible: %s " %traceback.format_exc())
        k = 1
        for i in range(11,18):
            if not options[i] == str(k)+ '+' :
                raise AssertionError("Transit power not visible: %s " %traceback.format_exc())
            k+=1

    def go_to_uplink(self):
        logger.debug("AccessPointsPage : click 'Uplink' accordion")
        self.uplink.click()
        
    def assert_default_values_of_uplink(self):
        if not self.eth0_bridging.get_selected() == self.config.config_vars.etho_bridging_disabled:
            raise AssertionError(" etho bridging is not set to Disabled")
            
    def set_nondefault_values_of_uplink(self):
        logger.debug("AccessPointsPage :set etho bridging to Enabled")
        self.eth0_bridging.set(self.config.config_vars.etho_bridging_enabled)
        if not self.etho_bridging_msg:  
            raise AssertionError(" Etho bridging message is not present ")
        self.uplink_vlan.set(self.config.config_vars.uplink_mgt_vlan_valid_value)
        self.click_save_settings()
        time.sleep(3)
        # self.alert_continue.click()
        
    def set_default_value_of_etho_bridging(self):
        logger.debug("AccessPointsPage :set etho bridging to Disabled")
        self.eth0_bridging.set(self.config.config_vars.etho_bridging_disabled)
        logger.debug("AccessPointsPage : click 'Save' button")
        self.click_save_settings()
        
    def set_radio_adaptive_assigned(self):
        logger.debug("AccessPointsPage : set Adaptive Assigned")
        self.arm_radio_24g.click()
        self.click_save_settings()
        
    def click_edit_iap(self):
        logger.debug("AccessPointsPage : Clicking on 'access' under 'MODE' column...")
        self.iap_mode_value.click()
        logger.debug("AccessPointsPage : Clicking 'Edit' button...")
        self.ap_edit_button.click()
        
    def assert_table_headers(self):
        logger.debug("AccessPointsPage : Asserting table column attributes...")
        if not (self.name and self.status and self.ip_address and self.ip_assignment and self.mode_label and self.type and self.ghz_24_channel and self.ghz_5_channel):
            raise AssertionError("Table headers not matched. Traceback: %s" % traceback.format_exc())
            
    def assert_edit_button(self):
        # logger.debug("AccessPointsPage : Clicking on 'access' under 'MODE' column...")
        # self.iap_mode_value.click()
        logger.debug("AccessPointsPage : Asserting 'Edit' button...")
        if not self.ap_edit_button:
            raise AssertionError("Edit button not found. Traceback: %s" % traceback.format_exc())
            
    def assert_basic_info_accordion_open(self):
        logger.debug("AccessPointsPage : Asserting Basic Info Accordion open...")
        if not self.basic_info_section:
            raise AssertionError("Basic Info accordion not open. Traceback: %s" % traceback.format_exc())
    
    def assert_basic_info_fields(self):
        logger.debug("AccessPointsPage : Asserting Basic Info field...")
        if not (self.basic_info_name_field and self.prefered_master and self.ip_address_for_ap):
            raise AssertionError("Basic Info field did not match. Traceback: %s" % traceback.format_exc())
            
    def assert_basic_info_default_values(self):
        logger.debug("AccessPointsPage : Asserting Basic Info field values...")
        if not self.prefered_master.get_selected() == 'Disabled':
            raise AssertionError("'Prefered Master' not set to default. Traceback: %s" % traceback.format_exc())
        # if not self.get_ip_from_dhcp.is_selected():
            # raise AssertionError("'IP Address for Access Point' not set to default. Traceback: %s" % traceback.format_exc())
    
    def click_radio_accordion(self):
        logger.debug("AccessPointsPage : Clicking on Radio accordion...")
        self.radio_accordion.click()
        
        time.sleep(7)
        if not self.radio_section:
            self.radio_accordion.click()
            
    def click_uplink_accordion(self):
        logger.debug("AccessPointsPage : Clicking on Uplink accordion...")
        self.uplink_accordion.click()
        
        time.sleep(7)
        if not self.uplink_section:
            self.uplink_accordion.click()
        
    def assert_radio_default_values(self):
        logger.debug("AccessPointsPage : Asserting 'MODE' values...")
        if not self.mode_picklist.get_selected() == 'Access':
            raise AssertionError("'MODE' not set to 'Access'. Traceback: %s" % traceback.format_exc())
        logger.debug("AccessPointsPage : Asserting '2.4 GHz BAND' values...")
        if not self.arm_radio_24g.is_selected():
            raise AssertionError("'2.4 GHz Band' not set to default. Traceback: %s" % traceback.format_exc())
        logger.debug("AccessPointsPage : Asserting '5 GHz BAND' values...")
        if not self.adaptive_radio_mgmt_5.is_selected():
            raise AssertionError("'5 GHz Band' not set to default. Traceback: %s" % traceback.format_exc())
        
    def assert_uplink_default_values(self):
        logger.debug("AccessPointsPage : Asserting 'ETH0 BRIDGING' values...")
        if not self.eth0_bridging.get_selected() == 'Disabled':
            raise AssertionError("'ETH0 BRIDGING' not set to 'Disabled'. Traceback: %s" % traceback.format_exc())
            
    def assert_name_error(self):
        name_str = '5'
        for x in range(1,39):
            name_str = name_str + '5'
        logger.debug('AccessPointPage : Editing in name field')
        self.access_point_name.set(name_str)
        time.sleep(5)
        logger.debug('AccessPointPage : Clicking on save button')
        self.save_button.click()
        if not self.access_point_name_error_msg:
            raise AssertionError("Invalid name input is not visible. Traceback: %s" % traceback.format_exc())
    
    def set_access_point_name(self, name):
        logger.debug('AccessPointPage : Clicking on Edit button')
        try:
            self.edit_access_point()
        except:
            logger.debug('AccessPointPage : Editing in name field')
            self.access_point_name.set(name)
            time.sleep(5)
            logger.debug('AccessPointPage : Clicking on save button')
            self.save_button.click()
            time.sleep(5)
        
    def assert_new_access_name(self):
        logger.debug('AccessPointPage : Clicking on Edit button')
        self.edit_access_point()
        if not self.access_point_name.get() == self.config.config_vars.new_access_point_name:
            raise AssertionError("Access point name has not been changed input is not visible. Traceback: %s" % traceback.format_exc())
    
    def assert_config_single_radio(self):
        logger.debug('AccessPointPage : Clicking on Edit button')
        self.edit_access_point()
        self.go_to_radio_section()
        if not self.access_point_24Ghz_label:
            raise AssertionError("2.4 GHz option is not visible. Traceback: %s" % traceback.format_exc())
        if not self.access_point_5Ghz_label:
            raise AssertionError("5 GHz option is not visible. Traceback: %s" % traceback.format_exc())
        
    def assign_radio_band(self, band, assignment):
        if band == '2.4GHz' and assignment == 'Adaptive':
            self.arm_radio_24g.click()
        elif band == '2.4GHz' and assignment == 'Administrator':
            self.aa_radio_24g.click()
        elif band == '5GHz' and assignment == 'Adaptive':
            self.adaptive_radio_mgmt_5.click()  
        elif band == '5GHz' and assignment == 'Administrator':
            self.aa_radio_5g.click()
        if self.save_button:
            self.save_button.click()
        
    def go_to_radio_section(self):
        logger.debug('AccessPointPage : Clicking on Radio accordion')
        self.click_radio()
        
    def configure_preffered_master(self,enable=False):
        if enable:
            logger.debug('AccessPointPage :Enable preffered master.')
            self.prefered_master.set(self.config.config_vars.preffered_master_enable)
        else:
            logger.debug('AccessPointPage :Disable preffered master.')
            self.prefered_master.set(self.config.config_vars.preffered_master_disable)
        logger.debug('AccessPointPage :Click save.')            
        if self.save_button:
            self.save_button.click()
            self.reboot_popup_ok.click()
        
    def get_ap_default_name(self):
        logger.debug('AccessPointPage : Clicking on Edit button')
        self.edit_access_point()
        return self.access_point_name.get()
        
    def assert_uplink_management_vlan(self):
        self.uplink_vlan.set(self.config.config_vars.uplink_mgt_vlan_reserved_value)
        self.save_button.click()
        if not self.vlan_mgt_3333_reserved_error:
            raise AssertionError("'* VLAN 3333 is reserved' error message not found. i.e. Traceback: %s" % traceback.format_exc())
        time.sleep(5)
        
        self.uplink_vlan.set(self.config.config_vars.uplink_mgt_vlan_0_preceed)
        self.save_button.click()
        if not self.ap_uplink_mgt_vlan_error:
            raise AssertionError("'* Must be number in range is 1-4093' error message not found. i.e. Traceback: %s" % traceback.format_exc())
        time.sleep(5)
        
        self.uplink_vlan.set(self.config.config_vars.uplink_mgt_vlan_invalid_value)
        self.save_button.click()
        if not self.ap_uplink_mgt_vlan_error:
            raise AssertionError("'* Must be number in range is 1-4093' error message not found. i.e. Traceback: %s" % traceback.format_exc())
        time.sleep(5)
        
        # self.uplink_vlan.set(self.config.config_vars.uplink_mgt_vlan_0_value)
        # self.save_button.click()
        # if not self.ap_uplink_mgt_vlan_error:
            # raise AssertionError("'* Must be number in range is 1-4093' error message not found. i.e. Traceback: %s" % traceback.format_exc())
        # time.sleep(5)
        
        self.uplink_vlan.set(self.config.config_vars.uplink_mgt_vlan_string_value)
        self.save_button.click()
        if not self.ap_uplink_mgt_vlan_error:
            raise AssertionError("'* Must be number in range is 1-4093' error message not found. i.e. Traceback: %s" % traceback.format_exc())
        time.sleep(5)
        
        self.uplink_vlan.set(self.config.config_vars.uplink_mgt_vlan_comma)
        self.save_button.click()
        if not self.ap_uplink_mgt_vlan_error:
            raise AssertionError("Comma seperated values  accepted'. i.e. Traceback: %s" % traceback.format_exc())
        time.sleep(5)
        
        self.uplink_vlan.set(self.config.config_vars.uplink_mgt_vlan_in_range_value)
        self.save_button.click()
        if not self.ap_uplink_mgt_vlan_error:
            raise AssertionError("'Range not accepted'. i.e. Traceback: %s" % traceback.format_exc())
        time.sleep(5)
        
        self.uplink_vlan.set(self.config.config_vars.uplink_mgt_vlan_valid_value)
        self.save_button.click()
        if not self.reboot_popup_ok :
            raise AssertionError("'Valid value not accepted'. i.e. Traceback: %s" % traceback.format_exc())
        self.reboot_popup_ok.click()
        time.sleep(5)
        self.edit_access_point()
        self.click_uplink_accordion()
        self.uplink_vlan.set(self.config.config_vars.uplink_mgt_vlan_0_value)
        self.save_button.click()
        self.reboot_popup_ok.click()
            
    def edit_radio_custom_channel_and_power(self):
        self.buy_time()
        logger.debug('AccessPointPage :clicking on AccessPoint and edit button of AccessPoints')
        self.click_access_point_edit_go_to_radio()
        logger.debug('AccessPointPage :clicking on Administrator assigned radio button of 2.4GHz BAND')
        self.aa_radio_24g.click()
        logger.debug('AccessPointPage :clicking on Administrator assigned radio button of 5GHz BAND')
        self.page_down()
        self.set_5ghz_radio_Administrator_assigned()
        
        logger.debug('AccessPointPage :selecting value from 2.4GHz Channel Drop=down')
        self.channel.set(self.config.config_vars.channel_24g_value)
        logger.debug('AccessPointPage :writing  value in 2.4GHz Transmit power textbox')
        self.transmit_power.set(self.config.config_vars.transmit_power_24g_value1)
        
        logger.debug('AccessPointPage :selecting value from 5GHz Channel Drop=down')
        self.channel_5ghz.set(self.config.config_vars.channel_5ghz_value)
        self.browser.key_press(u'\ue007')
        logger.debug('AccessPointPage :writing  value in 5GHz Transmit power textbox')
        self.transmit_power_5g.set(self.config.config_vars.transmit_power_5g_value1)
        logger.debug('AccessPointPage :clicking on SaveSettings button')
        self.save_button.click()
        
        self.buy_time()
        logger.debug('AccessPointPage :clicking on AccessPoint and edit button of AccessPoints')
        # self.click_access_point_edit_go_to_radio()
        logger.debug('AccessPointPage :writing  value in 2.4GHz Transmit power textbox')
        self.transmit_power.set(self.config.config_vars.transmit_power_24g_value2)
        logger.debug('AccessPointPage :writing  value in 5GHz Transmit power textbox')
        self.transmit_power_5g.set(self.config.config_vars.transmit_power_5g_value2)
        logger.debug('AccessPointPage :clicking on SaveSettings button')
        self.save_button.click()
        self.buy_time()
        
    def buy_time(self):
        time.sleep(5)
        
    def set_radio_defaults(self):
        '''
        clicking on Adaptive radio management assigned radio button
        and clicking on SaveSetting button
        '''
        logger.debug('AccessPointPage : Setting radio default values')
        self.click_access_point_edit_go_to_radio()
        
        logger.debug('AccessPointPage :writing  value in 2.4GHz Transmit power textbox')
        self.transmit_power.set(self.config.config_vars.transmit_power_24g_default_value)
        logger.debug('AccessPointPage :selecting value from 2.4GHz Channel Drop=down')
        self.channel.set(self.config.config_vars.channel_24g_value_default)
        
        logger.debug('AccessPointPage :writing  value in 5GHz Transmit power textbox')
        self.transmit_power_5g.set(self.config.config_vars.transmit_power_24g_default_value)
        logger.debug('AccessPointPage :selecting value from 5GHz Channel Drop=down')
        self.channel_5ghz.set(self.config.config_vars.channel_5ghz_value_default)
        
        self.arm_radio_24g.click()
        self.adaptive_radio_mgmt_5.click()
        self.save_button.click()
        
    def click_access_point_edit_go_to_radio(self):
        self.edit_access_point()
        self.click_radio_accordion()
        
    def validate_access_points_radio_custom_channel_and_power(self):
        self.buy_time()
        logger.debug('AccessPointPage :clicking on AccessPoint and edit button of AccessPoints')
        self.click_access_point_edit_go_to_radio()
        logger.debug('AccessPointPage :clicking on Administrator assigned radio button of 2.4GHz BAND')
        self.aa_radio_24g.click()
        self.assert_24ghz_band_channel_drop_down()
        logger.debug('AccessPointPage :writing  value in 2.4GHz Transmit power textbox')
        self.transmit_power.set(self.config.config_vars.invalid_transmit_power_24g_value)
        logger.debug('AccessPointPage :clicking on SaveSettings button')
        self.save_button.click()
        if not self.transmit_power_error_msg_24ghz:
            raise AssertionError("Accepting Transmit power value more than 127: %s " %traceback.format_exc())
        self.buy_time()
        logger.debug('AccessPointPage :writing  value in 2.4GHz Transmit power textbox')
        self.transmit_power.set(self.config.config_vars.alpha_transmit_power_24g_value)
        logger.debug('AccessPointPage :clicking on SaveSettings button')
        self.save_button.click()
        if not self.transmit_power_error_msg_24ghz:
            raise AssertionError("Accepting alphanumeric value for  Transmit power  : %s " %traceback.format_exc())
        self.buy_time()
        self.page_down()
        logger.debug('AccessPointPage :clicking on Administrator assigned radio button of 5GHz BAND')
        self.set_5ghz_radio_Administrator_assigned()
        self.page_down()
        self.assert_5ghz_band_channel_drop_down()
        logger.debug('AccessPointPage :writing  value in 5GHz Transmit power textbox')
        self.transmit_power_5g.set(self.config.config_vars.invalid_transmit_power_5g_value)
        logger.debug('AccessPointPage :clicking on SaveSettings button')
        self.save_button.click()
        if not self.transmit_power_error_msg_5ghz:
            raise AssertionError("Accepting Transmit power value more than 127: %s " %traceback.format_exc())
        self.buy_time()
        logger.debug('AccessPointPage :writing  value in 5GHz Transmit power textbox')
        self.transmit_power_5g.set(self.config.config_vars.alpha_transmit_power_5g_value)
        logger.debug('AccessPointPage :clicking on SaveSettings button')
        self.save_button.click()
        if not self.transmit_power_error_msg_5ghz:
            raise AssertionError("Accepting alphanumeric value for  Transmit power  : %s " %traceback.format_exc())
        self.buy_time() 
        
    def assert_24ghz_band_channel_drop_down(self):
        logger.debug('AccessPointPage :Checking Regulatory domain value of 2.4GHZ Band Channel')
        options = self.channel.get_options()
        for x in range(0,11):
            if not options[x] == str(x+1):
                raise AssertionError("2.4GHZ Band Channel list are not in range i,e not from 1 to 11: %s " %traceback.format_exc())
        k = 1
        for i in range(11,18):
            if not options[i] == str(k)+ '+' :
                raise AssertionError("2.4GHZ Band Channel list are not in range i,e not from 1+ to 7+ %s " %traceback.format_exc())
            k+=1
    def assert_5ghz_band_channel_drop_down(self):
        logger.debug('AccessPointPage :Checking Regulatory domain value of 5GHZ Band Channel')
        channel_options = self.channel_5ghz.get_options()
        n=36
        for a in range(0,8):
            if not channel_options[a] == str(n):
                raise AssertionError("5GHZ Band Channel list are not in range i,e not from 36 to 64: %s " %traceback.format_exc())
            n+=4
        n=100
        for a in range(8,13):
            if not channel_options[a] == str(n):
                raise AssertionError("5GHZ Band Channel list are not in range i,e not from 100 to 116: %s " %traceback.format_exc())
            n+=4
        n=132
        for a in range(13,17):
            if not channel_options[a] == str(n):
                raise AssertionError("5GHZ Band Channel list are not in range i,e not from 100 to 116: %s " %traceback.format_exc())
            n+=4
            
        j=149
        for b in range(17,22):
            if not channel_options[b] == str(j):
                raise AssertionError("5GHZ Band Channel list are not in range i,e not from 149 to 165: %s " %traceback.format_exc())
            j+=4
        m=36
        for c in range(22,26): 
            if not channel_options[c] == str(m)+ '+' :
                raise AssertionError("5GHZ Band Channel list are not in range i,e not from 36+ to 149+: %s " %traceback.format_exc())
            m+=8
        m=100
        for c in range(26,28): 
            if not channel_options[c] == str(m)+ '+' :
                raise AssertionError("5GHZ Band Channel list are not in range i,e not from 100+ to 108+: %s " %traceback.format_exc())
            m+=8    
        m=132
        for c in range(28,30): 
            if not channel_options[c] == str(m)+ '+' :
                raise AssertionError("5GHZ Band Channel list are not in range i,e not from 36+ to 149+: %s " %traceback.format_exc())
            m+=8
        m=149
        for c in range(30,32): 
            if not channel_options[c] == str(m)+ '+' :
                raise AssertionError("5GHZ Band Channel list are not in range i,e not from 36+ to 149+: %s " %traceback.format_exc())
            m+=8
        c = 32
        m = 36
        if not channel_options[c] == str(m)+ 'E' :
            raise AssertionError("5GHZ Band Channel list are not in range i,e not from 36+ to 149+: %s " %traceback.format_exc())
        c = c + 1   
        m = 52
        if not channel_options[c] == str(m)+ 'E' :
            raise AssertionError("5GHZ Band Channel list are not in range i,e not from 36+ to 149+: %s " %traceback.format_exc())
        c = c + 1   
        m = 100
        if not channel_options[c] == str(m)+ 'E' :
            raise AssertionError("5GHZ Band Channel list are not in range i,e not from 36+ to 149+: %s " %traceback.format_exc())
        c = c + 1   
        m = 132
        if not channel_options[c] == str(m)+ 'E' :
            raise AssertionError("5GHZ Band Channel list are not in range i,e not from 36+ to 149+: %s " %traceback.format_exc())
        c = c + 1   
        m = 149
        if not channel_options[c] == str(m)+ 'E' :
            raise AssertionError("5GHZ Band Channel list are not in range i,e not from 36+ to 149+: %s " %traceback.format_exc())
            
    def assert_pagination_option(self):
        if not self.page_dropdown:
            raise AssertionError("Page number drop down option is not available")
        if not self.page_label:
            raise AssertionError("Page label is not present")
        if not self.page_no_text:
            raise AssertionError("Page number text is not present")
        if not self.go_button:
            raise AssertionError("GO button is not present")
        if not self.page_navigation_arrow:
            raise AssertionError("Page navigation arrow is not available")
            
    def set_24ghz_radio_Administrator_assigned(self):
        logger.debug("AccessPointsPage : set Admin Assigned")
        self.aa_radio_24g.click()
        
    def set_radio_24ghz_band_admn_assgnd_channel(self,value):
        self.buy_time()
        logger.debug('AccessPointPage :selecting value from 2.4GHz Channel Drop=down')
        self.channel.set(value)
        
    def set_radio_24ghz_transmit_power(self,value):
        '''
        set radio 2.4ghz TRANSMIT POWER value and assert the  error message
        '''
        if value == None:
            logger.debug('AccessPointPage :writing  value in 2.4GHz Transmit power textbox')
            self.transmit_power.set(self.config.config_vars.transmit_power_24g_default_value)
        else:
            logger.debug('AccessPointPage :writing  value in 2.4GHz Transmit power textbox')
            self.transmit_power.set(value)
        
    def assert_radio_24ghz_transmit_power_error(self,assert_error): 
        '''
        Asserting radio 5ghz TRANSMIT POWER Error message
        '''
        self.buy_time()
        if assert_error == 'true':
            if not self.transmit_power_error_msg_24ghz:
                raise AssertionError("Accepting Transmit power value more than 127: %s " %traceback.format_exc())
        elif assert_error == 'false':
            if self.transmit_power_error_msg_24ghz:
                raise AssertionError(" * Must be number in range is 0-127: %s " %traceback.format_exc())
                
    
    def click_on_cancel(self):
        '''
        clicking on Cancel button
        '''
        logger.debug("AccessPointPage : Clicking on 'CANCEL' button...")
        self.buy_time()
        self.cancel_button.click()
    
    def set_radio_5ghz_transmit_power(self,value):
        '''
        set radio 5ghz TRANSMIT POWER value and assert the  error message
        '''
        self.buy_time()
        if value == None: 
            logger.debug('AccessPointPage :writing  value in 5GHz Transmit power textbox')
            self.transmit_power_5g.set(self.config.config_vars.transmit_power_24g_default_value)
        else:
            logger.debug('AccessPointPage :writing  value in 5GHz Transmit power textbox')
            self.transmit_power_5g.set(value)
        
    def assert_radio_5ghz_transmit_power_error(self,assert_error):  
        '''
        Asserting radio 5ghz TRANSMIT POWER Error message
        '''
        self.buy_time()
        if assert_error == 'true':
            if not self.transmit_power_error_msg_5ghz:
                raise AssertionError("Accepting Transmit power value more than 127: %s " %traceback.format_exc())
        elif assert_error == 'false':
            if self.transmit_power_error_msg_5ghz:
                raise AssertionError(" * Must be number in range is 0-127: %s " %traceback.format_exc())
                    
    def validating_radio_24ghz_transmit_power(self):
        conf=self.config.config_vars
        self.set_radio_24ghz_transmit_power(conf.invalid_transmit_power_24g_value)
        self.save_settings()
        self.assert_radio_24ghz_transmit_power_error('true')
        self.set_radio_24ghz_transmit_power(conf.alpha_transmit_power_24g_value)
        self.save_settings()
        self.assert_radio_24ghz_transmit_power_error('true')
        self.set_radio_24ghz_transmit_power(conf.valid_transmit_power_24g_zero_preceded_value)
        self.save_settings()
        self.assert_radio_24ghz_transmit_power_error('true')
        self.set_radio_24ghz_transmit_power(conf.no_value)
        self.save_settings()
        self.assert_radio_24ghz_transmit_power_error('true')
        
    def set_5ghz_radio_Administrator_assigned(self):
        self.buy_time()
        logger.debug("AccessPointsPage : Setting Admin Assigned")
        self.aa_radio_5g.click()
        if not self.channel_5ghz:
            self.aa_radio_5g.click()
        
        
    def validating_radio_5ghz_transmit_power(self):
        conf=self.config.config_vars
        self.set_radio_5ghz_transmit_power(conf.invalid_transmit_power_5g_value)
        self.save_settings()
        self.assert_radio_5ghz_transmit_power_error('true')
        self.set_radio_5ghz_transmit_power(conf.alpha_transmit_power_5g_value)
        self.save_settings()
        self.assert_radio_5ghz_transmit_power_error('true')
        self.set_radio_5ghz_transmit_power(conf.valid_transmit_power_5g_zero_preceded_value)
        self.save_settings()
        self.assert_radio_5ghz_transmit_power_error('true')
        self.set_radio_5ghz_transmit_power(conf.no_value)
        self.save_settings()
        self.assert_radio_5ghz_transmit_power_error('true')
        
    def save_settings(self):
        '''
        clicking on save settings button
        '''
        logger.debug("AccessPointsPage : click 'Save' button")
        self.buy_time()
        self.save_button.click()
        self.buy_time()
        if self.save_button:
            self.save_button.click()
            
    def page_down(self):
        '''
        scroll down the page
        '''
        self.browser.key_press(u'\ue009')
        self.browser.key_press( u'\ue00f')
        
    def select_static_radio_button(self):
        time.sleep(10)
        logger.debug("Clicking on static radio button")
        self.static_radio.click()
        time.sleep(10)
    
    def assert_ip_netmask_gateway(self,value):
        logger.debug("Asserting the default value of netmask and gateway")
        if not self.netmask_textbox.get() == value:
            raise AssertionError("Netmask value is not set to default")
        if not self.default_gateway.get() == value:
            raise AssertionError("Gateway value is not set to default")
        
    def set_ip_address_value(self,value=None):
        logger.debug("Setting ip address field")
        if value:
            self.ip_address_textbox.set(value)
        else:
            self.ip_address_textbox.set("")
            
    def set_netmask_value(self,value=None):
        logger.debug("Setting netmask address field")
        if value:
            self.netmask_textbox.set(value)
        else:
            self.netmask_textbox.set("")
    
    def set_gateway_value(self,value=None):
        logger.debug("Setting default gateway field")
        if value:
            self.default_gateway.set(value)
        else:
            self.default_gateway.set("")
    
    def set_dns_server_value(self,value=None):
        logger.debug("Setting dns server field")
        if value:
            self.dns_server.set(value)
        else:
            self.dns_server.set("")
    
    def set_domain_name_value(self,value=None):
        logger.debug("Setting domain name field")
        if value:
            self.domain_name.set(value)
        else:
            self.domain_name.set("")
    
    def save_setting_button(self):
        logger.debug("Clicking on save setting button")
        self.save_button.click()
        
    def assert_reboot_ap_warning(self):
        if not self.reboot_ap_warning:
            raise AssertionError("Reboot AP warning message not shown")
    
    def asserting_ip_netmask_gateway_dns_domain_error(self,ip=False,netmask=False,gateway=False,ip_gateway=False,dns=False,domain=False):
        if ip:
            if not self.ip_invalid_error:
                raise AssertionError("Error message is not shown for ip address")
        if netmask:
            if not self.netmask_invalid_error:
                raise AssertionError("Error message is not shown for netmask")
        if gateway:
            if not self.gateway_invalid_error:
                raise AssertionError("Error message is not shown for default gateway")
        if ip_gateway:
            if not self.gateway_ip_error:
                raise AssertionError("Error message is not shown for default gateway and ip address")
        if dns:
            if not self.dns_invalid_error:
                raise AssertionError("Error message is not shown for dns server")
        if domain:
            if not self.domain_invalid_error:
                raise AssertionError("Error message is not shown for domain name")
        
    def asserting_ip_netmask_gateway_dns_domain(self,ip=True,netmask=True,gateway=True,ip_gateway=True,dns=True,domain=True):
        if ip:
            if self.ip_invalid_error:
                raise AssertionError("Error message is shown for ip address")
        if netmask:
            if self.netmask_invalid_error:
                raise AssertionError("Error message is shown for netmask")
        if gateway:
            if self.gateway_invalid_error:
                raise AssertionError("Error message is shown for default gateway")
        if ip_gateway:
            if self.gateway_ip_error:
                raise AssertionError("Error message is shown for default gateway and ip address")
        if dns:
            if self.dns_invalid_error:
                raise AssertionError("Error message is shown for dns server")
        if domain:
            if self.domain_invalid_error:
                raise AssertionError("Error message is shown for domain name")
    
    def clicking_reboot_ap_warning(self):
        logger.debug('AccessPointPage : Clicking reboot_ap_warning...')
        self.reboot_ap_warning.click()
        
    def assert_nondefault_values_of_uplink(self):
        conf=self.config.config_vars
        logger.debug("AccessPointsPage :Assert etho bridging to Enabled")
        self.browser.assert_drop_down_value(self.eth0_bridging, conf.etho_bridging_enabled, "etho bridging not set to given value")
        logger.debug("AccessPointsPage :Assert Uplink Management VLAN to Enabled")
        self.browser.assert_text(self.uplink_vlan, conf.uplink_mgt_vlan_valid_value, "Uplink Management VLAN not set to given value", "value")
        
    def set_default_value_of_uplink_management_vlan(self):
        logger.debug("AccessPointsPage :setting Uplink Management VLAN")
        self.uplink_vlan.set(self.config.config_vars.uplink_mgt_vlan_0_value)
        
    def assert_basic_info_ip_address_static_fields(self):
        '''
        Asserts Basic Info Ip Address Static Fields
        '''
        logger.debug("AccessPointPage: Checking Ip Address textbox is not present or not")
        self.browser.assert_element(self.ip_address_textbox,'Ip Address textbox is not Present')
        logger.debug("AccessPointPage: Checking Netmask textbox is not present or not")
        self.browser.assert_element(self.netmask_textbox,'Netmask textbox is not Present')  
        logger.debug("AccessPointPage: Checking Default Gateway textbox is not present or not")
        self.browser.assert_element(self.default_gateway,'Default Gateway textbox is not Present')
        logger.debug("AccessPointPage: Checking Dns Server textbox is not present or not")
        self.browser.assert_element(self.dns_server,'Dns Server textbox is not Present')
        logger.debug("AccessPointPage: Checking domain Name textbox is not present or not")
        self.browser.assert_element(self.domain_name,'domain Name textbox is not Present')      
        
    def get_current_server_ip_and_set(self):
        '''
        Get Current Server Ip 
        '''
        dev_ip = devices.IAP_1.ip
        logger.debug("AccessPointsPage :set Ip Address Textbox")
        self.ip_address_textbox.set(dev_ip)
    
    def set_radio_mode(self,mode):
        logger.debug("AccessPointsPage :set value in 'SPECTRUM' drop down")
        self.mode_picklist.set(mode)
        
    def set_mode_to_default(self):
        if not self.mode_picklist.get_selected() == 'Access':
            logger.debug("AccessPointsPage :set value in 'ACCESS' drop down")
            self.mode_picklist.set(self.config.config_vars.access_wifi_mode)
            self.click_save_settings()


    def click_134_edit_iap(self):
        logger.debug("AccessPointsPage : Clicking 134 IAP 'Edit' button...")
        self.type_134_iap_edit.click()
        
    def click_135_edit_iap(self):
        logger.debug("AccessPointsPage : Clicking 135 IAP 'Edit' button...")
        self.type_135_iap_edit.click()
        
    def click_external_antenna_accordion(self):
        logger.debug("AccessPointsPage : Clicking on EXTERNAL ANTENNA  Accordion...")
        self.external_antenna_accordion.click()
        time.sleep(10)
        
    def assert_24ghz_and_5ghz_antenna_gain(self):
        conf = self.config.config_vars
        if self.antenna_gain_24ghz :
            logger.debug('AccessPointsPage : Asserting 2.4GHz Antenna Gain textbox')
            self.browser.assert_text(self.antenna_gain_24ghz,conf.zero_dbi,'2.4GHz Antenna Gain textbox is  not set to zero dbi','value')
            
        if self.antenna_gain_5ghz :
            logger.debug('AccessPointsPage : Asserting 5GHz Antenna Gain textbox')
            self.browser.assert_text(self.antenna_gain_5ghz,conf.zero_dbi,'5GHz Antenna Gain textbox is  not set to zero dbi','value')
            
    def asserting_external_antenna_accordion(self):
        '''
        '''
        try:
            if self.external_antenna_accordion:
                self.external_antenna_accordion.click()
                raise AssertionError("EXTERNAL ANTENNA  Accordion is present")              
        except:
            pass
            

    def set_24_ghz_antenna_gain(self,value=None):
        '''
        Sets 2.4Ghz Antenna Gain
        '''
        if value == None:
            logger.debug("AccessPointsPage :set value in '2.4Ghz Antenna Gain' TextBox")
            self.antenna_gain_24ghz.set(self.config.config_vars.transmit_power_24g_default_value)
        else:
            logger.debug("AccessPointsPage :set value in '2.4Ghz Antenna Gain' TextBox")
            self.antenna_gain_24ghz.set(value)

    def set_5_ghz_antenna_gain(self,value=None):
        '''
        Sets 5Ghz Antenna Gain
        '''
        if value == None:
            logger.debug("AccessPointsPage :set value in '5Ghz Antenna Gain' TextBox")
            self.antenna_gain_5ghz.set(self.config.config_vars.transmit_power_24g_default_value)
        else:
            logger.debug("AccessPointsPage :set value in '5Ghz Antenna Gain' TextBox")
            self.antenna_gain_5ghz.set(value)
    
    def assert_antenna_24GHz_gain_error(self,error_msg):
        '''
        Asserts 2.4Ghz Antenna Gain error 
        '''
        if error_msg:
            self.browser.assert_element(self.antenna_2GHz_gain_error, 'Must be number in range is 0-99 error message is not present')
        else:
            self.browser.assert_element(self.antenna_2GHz_gain_error, 'Must be number in range is 0-99 error message is not present',False)
    
    def assert_antenna_5GHz_gain_error(self,error_msg):
        '''
        Asserts 5Ghz Antenna Gain error 
        '''
        if error_msg:
            self.browser.assert_element(self.antenna_5GHz_gain_error, 'Must be number in range is 0-99 error message is not present')
        else:
            self.browser.assert_element(self.antenna_5GHz_gain_error, 'Must be number in range is 0-99 error message is not present',False)
    
    def validate_antenna_gain_fields(self, value, error_msg):
        self.set_24_ghz_antenna_gain(value)
        self.set_5_ghz_antenna_gain(value)
        self.save_setting_button()
        self.assert_antenna_24GHz_gain_error(error_msg)
        self.assert_antenna_5GHz_gain_error(error_msg)
        
    def setting_defaults_24_channel(self):
        logger.debug('AccessPointPage :selecting value from 2.4GHz Channel Drop=down')
        self.channel.set(self.config.config_vars.channel_24g_value_default)
        logger.debug('AccessPointPage :writing  value in 2.4GHz Transmit power textbox')
        self.transmit_power.set(self.config.config_vars.transmit_power_24g_default_value)
        
    def setting_defaults_5_channel(self):
        logger.debug('AccessPointPage :selecting value from 5GHz Channel Drop=down')
        self.channel_5ghz.set(self.config.config_vars.channel_5ghz_value_default)
        logger.debug('AccessPointPage :writing  value in 2.4GHz Transmit power textbox')
        self.transmit_power_5g.set(self.config.config_vars.transmit_power_24g_default_value)
        
    def assert_spl_char_name_error(self):
        logger.debug('AccessPointPage : Editing in name field')
        self.access_point_name.set(self.config.config_vars.special_chars_hostname)
        time.sleep(5)
        logger.debug('AccessPointPage : Clicking on save button')
        self.save_button.click()
        if self.access_point_spl_char:
            raise AssertionError("Invalid access point name accepted. Traceback: %s" % traceback.format_exc())
            
    def get_set_current_mac_address(self):
        '''
        Get Current mac address 
        '''
        mac_address = devices.IAP_1.mac_address
        logger.debug("AccessPointsPage :set Ip Address Textbox")
        self.access_point_name.set(mac_address)
        time.sleep(5)
        
            
            
    def get_and_set_current_server_ip_netmask_dns_ip_gateway(self):
        '''
        Get Current Server Ip , dns ip, netmask and Gateway
        '''
        dev_ip = devices.IAP_1.ip
        dev_dns_ip = devices.IAP_1.dns_ip
        dev_netmask = devices.IAP_1.netmask
        dev_gateway = devices.IAP_1.gateway_ip
        
        
        logger.debug("AccessPointsPage :set Ip Address Textbox")
        self.ip_address_textbox.set(dev_ip)
        
        logger.debug("AccessPointsPage :set Ip Address Textbox")
        self.netmask_textbox.set(dev_netmask)
        
        logger.debug("AccessPointsPage :set Ip Address Textbox")
        self.default_gateway.set(dev_gateway)
        
        logger.debug("AccessPointsPage :set Ip Address Textbox")
        self.dns_server.set(dev_dns_ip)
        
    def set_adaptive_radio_defaults(self):
        '''
        clicking on Adaptive radio management assigned radio button
        and clicking on SaveSetting button
        '''
        logger.debug('AccessPointPage : Setting radio default values')
        self.click_access_point_edit_go_to_radio()
        self.mode_picklist.set(self.config.config_vars.access_wifi_mode)
        self.arm_radio_24g.click()
        self.adaptive_radio_mgmt_5.click()
        self.click_save_settings()
        
    def select_particular_vc(self,iap):
        myDevice = Device.getDeviceObject(iap)
        ip = myDevice.get("ip")
        self.browser._browser.find_element_by_xpath("//td[@title='%s']/following-sibling::td[6]" %ip).click()

    def select_particular_iap_type(self,iap):
        myDevice = Device.getDeviceObject(iap)
        aptype = myDevice.get("ap_type")
        self.browser._browser.find_element_by_xpath("//td[@title='%s']/following-sibling::td[3]" %aptype).click()
        
    def get_and_set_slave_iap_details(self):
        '''
        Get Current Server Ip , dns ip, netmask and Gateway
        '''
        dev_ip = devices.IAP_2.ip
        dev_dns_ip = devices.IAP_2.dns_ip
        dev_netmask = devices.IAP_2.netmask
        dev_gateway = devices.IAP_2.gateway_ip
        
        
        logger.debug("AccessPointsPage :set Ip Address Textbox")
        self.ip_address_textbox.set(dev_ip)
        
        logger.debug("AccessPointsPage :set Ip Address Textbox")
        self.netmask_textbox.set(dev_netmask)
        
        logger.debug("AccessPointsPage :set Ip Address Textbox")
        self.default_gateway.set(dev_gateway)
        
        logger.debug("AccessPointsPage :set Ip Address Textbox")
        self.dns_server.set(dev_dns_ip)
        
        
    def assert_backend(device,command=None,expected=None):
        '''
        Device : IAP or switch to used for backend validation.
        command : cli command
        expected : expected result in cli o/partition
        '''
        myDevice = Device.getDeviceObject(ap)
        # version = firmware_version.split('_')[0]
        myDevice.receive("#")
        myDevice.transmit("%s"%command)
        output = myDevice.receive("#")
        if not expected in output:
            raise AssertionError("%s not found in config." %expected)
        
        
        
        
        

    
  
    
