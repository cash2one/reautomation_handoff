# Last edited by : Ishan Anand
# On date : 07th Aug 2014

from athenataf.lib.util.WebPage import WebPage
from athenataf.lib.functionality.page.configuration.network.VirtualLanPage import VirtualLanPage
import logging
logger = logging.getLogger('athenataf')
import time
class BasicInfoPage(WebPage):
    def __init__(self, test, browser, config):
        time.sleep(10)
        WebPage.__init__(self, "BasicInfo", test, browser, config)
        self.test.assertPageLoaded(self)
        
        
    def isPageLoaded(self):
        if self.networkname:
            return True 
        else:
            return False 
            
    def employee_network_info(self, network_name="test1"):
        logger.debug('Network : Basic Info Page : Clicking on wireless')
        self.wireless.click()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Writing network name')
        self.networkname.set(network_name)
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on employee radio button')
        self.employee.click()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        import time
        time.sleep(5)
        return VirtualLanPage(self.test, self.browser, self.config)

    def guest_network_info(self):
        logger.debug('Network : Basic Info Page : Clicking on wireless')
        self.wireless.click()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Writing network name')
        self.networkname.set(self.config.config_vars.Network_name)
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on guest radio button')
        self.wired_network_guest.click()
        import time
        time.sleep(5)
        if not self.wired_network_guest.is_selected():
            logger.debug('Network : Basic Info Page : Clicking on guest radio button')
            self.wired_network_guest.click()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
    
    def wired_guest_network_info(self):
        self._click_on_wired()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on guest radio button')
        self.wired_network_guest.click()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on guest radio button')
        self.wired_network_guest.click()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Writing network name')
        self.networkname.set(self.config.config_vars.wired_network_name)
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def voice_network_info(self):
        logger.debug('Network : Basic Info Page : Clicking on wireless')
        self.wireless.click()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        # self.buy_time()
        # self.next.click()
        # self.buy_time()
        # self.assert_network_name_error()
        # self.buy_time()
        logger.debug('Network : Basic Info Page : Writing network name')
        self.networkname.set(self.config.config_vars.Network_name)
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on voice radio button')
        self.voice.click()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def _click_on_wired(self):
        logger.debug('Network : Basic Info Page : Clicking on wired radio button')
        self.wired.click()
        self.wired.click()
        self.buy_time()
    
    def create_wired_network(self):
        '''
        create a wired network with spanning tree settings.
        '''
        self._click_on_wired()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        logger.debug('Network : Basic Info Page : Writing network name')
        self.networkname.set(self.config.config_vars.wired_network_name)
        self.buy_time()
        logger.debug('Network : Basic Info Page : Writing spanning tree status')
        self.spanning_tree.set(self.config.config_vars.Spanning_Tree_Status)
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
    
    def wired_employee_network_info(self):
        self._click_on_wired()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        logger.debug('Network : Basic Info Page : Writing network name')
        self.networkname.set(self.config.config_vars.wired_network_name)
        self.assert_wired_configuration_defaults()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def assert_wired_configuration_defaults(self):
        import traceback
        if not self.employee.is_selected():
            raise AssertionError("'PRIMARY USAGE' radio button is not set to 'Employee': %s " %traceback.format_exc())
        if not self.speed.selected=='Auto':
            raise AssertionError("Speed is not Auto by default .Traceback: %s " %traceback.format_exc())
        if not self.duplex.selected=='Auto':
            raise AssertionError("duplex is not Auto by default .Traceback: %s " %traceback.format_exc())   
        if not self.Wired_POE.selected=='Enabled':
            raise AssertionError("POE not enabled by default by default .Traceback: %s " %traceback.format_exc())
        if not self.admin_status.selected=='Up':
            raise AssertionError("Admin status not Up by default .Traceback: %s " %traceback.format_exc())
        if not self.filtering.selected=='Disabled':
            raise AssertionError("Content filtering not Disabled Up by default .Traceback: %s " %traceback.format_exc())
        if not self.Wired_Uplink.selected=='Disabled':
            raise AssertionError("Wired up link not Disabled Up by default .Traceback: %s " %traceback.format_exc())
        if not self.spanning_tree.selected=='Disabled':
            raise AssertionError("Spanning tree not Disabled Up by default .Traceback: %s " %traceback.format_exc())

    def wired_employee_network_info_2(self):
        self._click_on_wired()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        logger.debug('Network : Basic Info Page : Writing network name')
        self.networkname.set(self.config.config_vars.Network_name2)
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
    
    def set_wired_basic_nondefault(self,poe = False):
        self._click_on_wired()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        logger.debug('Network : Basic Info Page : Writing network name')
        self.networkname.set(self.config.config_vars.wired_network_name)
        self.buy_time()
        logger.debug('Network : Basic Info Page : Show advanced options : Writing speed')
        self.speed.set(self.config.config_vars.basic_speed)
        logger.debug('Network : Basic Info Page : Show advanced options : Writing duplex')
        self.duplex.set(self.config.config_vars.basic_duplex)
        if poe:
            logger.debug('Network : Basic Info Page : Show advanced options : Writing POE status')
            self.Wired_POE.set(self.config.config_vars.poe_disabled)
        logger.debug('Network : Basic Info Page : Show advanced options : Writing admin status')
        self.admin_status.set(self.config.config_vars.basic_admin)
        logger.debug('Network : Basic Info Page : Show advanced options : Writing basic filter')
        self.filtering.set(self.config.config_vars.basic_filter)
        logger.debug('Network : Basic Info Page : Show advanced options : Writing basic uplink')
        self.Wired_Uplink.set(self.config.config_vars.basic_uplink)
        logger.debug('Network : Basic Info Page : Show advanced options : Writing Spanning Tree')
        self.spanning_tree.set(self.config.config_vars.basic_uplink)
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
    
    def buy_time(self):
        import time
        time.sleep(10)
        
    def wired_guest_network_info_changed(self,both=False):
        self._click_on_wired()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        logger.debug('Network : Basic Info Page : Writing network name')
        self.networkname.set(self.config.config_vars.wired_network_name)
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on guest radio button')
        self.wired_network_guest.click()
        self.buy_time()
        # import traceback
        # if not self.speed.selected=='10':
            # raise AssertionError("Speed is not 10 by default .Traceback: %s " %traceback.format_exc())
        # if not self.duplex.selected=='Half':
            # raise AssertionError("duplex is not Half by default .Traceback: %s " %traceback.format_exc()) 
        # if not self.Wired_POE.selected=='Disabled':
            # raise AssertionError("POE not Disabled by default by default .Traceback: %s " %traceback.format_exc())
        # if not self.admin_status.selected=='Down':
            # raise AssertionError("Admin status not Down by default .Traceback: %s " %traceback.format_exc())
        # if not self.filtering.selected=='Enabled':
            # raise AssertionError("Content filtering not Enabled Up by default .Traceback: %s " %traceback.format_exc())
        # if not self.Wired_Uplink.selected=='Enabled':
            # raise AssertionError("Wired up link not Enabled Up by default .Traceback: %s " %traceback.format_exc())
        # if not self.spanning_tree.selected=='Enabled':
            # raise AssertionError("Spanning tree not Enabled Up by default .Traceback: %s " %traceback.format_exc())       
        logger.debug('Network : Basic Info Page : Show advanced options : Writing basic speed ')
        self.speed.set(self.config.config_vars.basic_speed_1000)
        logger.debug('Network : Basic Info Page : Show advanced options : Writing basic admin up ')
        self.admin_status.set(self.config.config_vars.basic_admin_up)
        logger.debug('Network : Basic Info Page : Show advanced options : Selecting wired POE ')
        self.Wired_POE.set(self.config.config_vars.basic_enabled)
        logger.debug('Network : Basic Info Page : Show advanced options : Selecting Filtering')
        self.filtering.set(self.config.config_vars.basic_enabled)
        logger.debug('Network : Basic Info Page : Show advanced options : Selecting wired uplink')
        self.Wired_Uplink.set(self.config.config_vars.basic_enabled)
        logger.debug('Network : Basic Info Page : Show advanced options : Selecting spanning tree')
        self.spanning_tree.set(self.config.config_vars.basic_enabled)
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def assert_network_name_error(self):
        if not self.name_error: 
            import traceback
            raise AssertionError("Procceding without adding network name i.e . Traceback: %s" % traceback.format_exc())
        logger.debug('Network : Basic Info Page : Writing network name')
        self.networkname.set(self.config.config_vars.Network_name)  
            
    def wired_employee_network_info_new(self):
        self._click_on_wired()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        logger.debug('Network : Basic Info Page : Writing network name')
        self.networkname.set(self.config.config_vars.Network_name)
        self.assert_wired_configuration_defaults()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def guest_new_network_info(self):
        logger.debug('Network : Basic Info Page : Clicking on wireless radio button')
        self.wireless.click()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Writing network name')
        self.networkname.set('Aruba')
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on guest radio button')
        self.wired_network_guest.click()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def create_guest_network(self):
        logger.debug('Network : Basic Info Page : Clicking on wireless radio button')
        self.wireless.click()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Writing network name')
        self.networkname.set(self.config.config_vars.guest_network_name)
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on guest radio button')
        self.wired_network_guest.click()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def create_and_assert_employee_network(self):
        import time
        import traceback
        logger.debug('Basic Info Page : Clicking on Wireless')
        self.wireless.click()
        if not self.employee.is_selected():
            raise AssertionError("Employee radio is not selected i.e . Traceback: %s" % traceback.format_exc())         
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')      
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('Basic Info Page : Entering network name') 
        self.networkname.set(self.config.config_vars.Network_name)
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def create_and_assert_voice_network(self):
        import time
        import traceback
        logger.debug('Basic Info Page : Clicking on Wireless')
        self.wireless.click()
        self.voice.click()
        if not self.voice.is_selected():
            raise AssertionError("Voice radio is not selected i.e . Traceback: %s" % traceback.format_exc())            
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')      
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('Basic Info Page : Entering network name') 
        self.networkname.set(self.config.config_vars.Network_name)
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def edit_advance_options(self,uplink=False,max_threshold=False,hide_ssid=False,local_probe=False,inactivity_timeout=False):
        import traceback
        logger.debug('Basic Info Page : Clicking on Wireless.')
        self.wireless.click()
        self.buy_time()
        logger.debug('Basic Info Page : Write network name.')
        self.networkname.set(self.config.config_vars.Network_name)
        self.buy_time()
        logger.debug('Basic Info Page : Clicking employee.')
        self.employee.click()
        self.buy_time()
        logger.debug('Basic Info Page : Click on advanced options.')        
        self.show_advanced_options.click()
        self.buy_time()
        if uplink:
            logger.debug('Basic Info Page: Enable without uplink checkbox .')
            self.without_uplink.click()
        elif max_threshold:
            logger.debug("Basic Info Page: Set max client threshold.")      
            self.max_client_threshold.set(self.config.config_vars.valid_max_client_threshold)
        elif hide_ssid: 
            logger.debug("Basic Info Page: Enable hide ssid.")      
            self.hide_ssid_checkbox.click()
        elif local_probe:
            logger.debug("Basic Info Page: Set LOCAL PROBE REQUEST THRESHOLD.")     
            self.local_probe_req_textbox.set(self.config.config_vars.local_probe_request_threshold)
        elif inactivity_timeout:
            logger.debug('Basic Info Page: Set invalid inactivity timeout.')
            self.inactivity_timeout.set(self.config.config_vars.invalid_inactivity_timeout)
            self.next.click()
            if not self.inactivity_error:
                raise AssertionError("Invalid inactivity error message not displayed .Traceback: %s " %traceback.format_exc())
            logger.debug('Basic Info Page : Set valid inactivity timeout.')
            self.inactivity_timeout.set(self.config.config_vars.valid_inactivity_timeout)
        logger.debug('Basic Info Page: Clicking on Next')   
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)

    def name_field_validation(self, name, validity, type = None):
        logger.debug("BasicInfoPage : writting '%s' into 'NAME(SSID)' field..")
        self.networkname.set(name)
        logger.debug("BasicInfoPage : Clicking 'Next' button..")
        self.next.click()
        if validity == 'valid':
            return VirtualLanPage(self.test, self.browser, self.config)
        elif validity == 'invalid':
            import traceback
            if type == 'spcl_char':
                if not self.spcl_char_error_msg:
                    raise AssertionError("'Quotes are not allowed' error message not found. Traceback: %s " %traceback.format_exc())
            elif type == 'required':
                if not self.name_error:
                    raise AssertionError("'This field is required' error message not found. Traceback: %s " %traceback.format_exc())
            elif type == 'max_length':
                if not self.max_length_error_msg:
                    raise AssertionError("'Maximum 32 character allowed' error message not found. Traceback: %s " %traceback.format_exc())
                    
    def click_on_next(self):
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)

    def click_advanced_settings(self):
        logger.debug('BasicInfoPage : Clicking on SHOW ADVANCED OPTIONS option')
        self.show_advanced_options.click()
        self.buy_time()

    def configure_broadcasefiltering_dtiminterval(self):
        logger.debug('BasicInfoPage : Selecting ARP option from dropdown menu')
        self.broadcasefiltering.set(self.config.config_vars.broadcasefiltering_arp)
        logger.debug('BasicInfoPage : Selecting 3 beacons option from dropdown menu')
        self.dtiminterval.set(self.config.config_vars.dtiminterval_3_beacons)

    def employee_network_info_with_advanced_settings(self):
        logger.debug('Network : Basic Info Page : Clicking on wireless button')
        self.wireless.click()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Writing network name')
        self.networkname.set(self.config.config_vars.Network_name)
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on employee radio button')
        self.employee.click()
        self.buy_time()
        self.click_advanced_settings()

    def employee_network_info_with_advanced_settings_broadcasefiltering_dtiminterval(self):
        self.employee_network_info_with_advanced_settings()
        self.configure_broadcasefiltering_dtiminterval()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)


    def set_broadcasefiltering_dtiminterval(self):
        logger.debug('BasicInfoPage : Selecting ALL option from dropdown menu')
        self.broadcasefiltering.set(self.config.config_vars.broadcasefiltering_all)
        logger.debug('BasicInfoPage : Selecting 7 beacons option from dropdown menu')
        self.dtiminterval.set(self.config.config_vars.dtiminterval_7_beacons)

    def employee_network_with_advanced_settings(self):
        self.employee_network_info_with_advanced_settings()
        self.set_broadcasefiltering_dtiminterval()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)

    def set_besteffort_wmm_share(self,value=None):
        self.buy_time()
        logger.debug("BasicInfoPage : Set Best Effort wmm share value")
        if value:
            self.besteffort_wmm_share.set(value)
        else:
            self.besteffort_wmm_share.set(self.config.config_vars.besteffort)

    def set_video_wmm_share(self,value=None):
        self.buy_time()
        logger.debug("BasicInfoPage : Set video wmm share value")
        if value:
            self.video_wmm_share.set(value)
        else:
            self.video_wmm_share.set(self.config.config_vars.video_wmm_share)

    def employee_network_with_advanced_settings_besteffort_wmm_share(self):
        self.employee_network_info_with_advanced_settings()
        self.set_besteffort_wmm_share()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)

    def employee_network_with_advanced_settings_video_wmm_share(self):
        self.employee_network_info_with_advanced_settings()
        self.set_video_wmm_share()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)

    def set_voice_wmm_share(self,value=None):
        self.buy_time()
        logger.debug("BasicInfoPage : Set voice wmm share value")
        if value:
            self.voice_wmm_share.set(value)
        else:
            self.voice_wmm_share.set(self.config.config_vars.voice_wmm_share)

    def employee_network_with_advanced_settings_voice_wmm_share(self):
        self.employee_network_info_with_advanced_settings()
        self.set_voice_wmm_share()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def set_background_wmm(self,value=None):
        self.buy_time()
        logger.debug("BasicInfoPage : Set background_wmm value")
        if value:
            self.background_wmm.set(value)
        else:
            self.background_wmm.set(self.config.config_vars.background_wmm)
        
    def employee_network_with_advanced_settings_background_wmm(self):
        self.employee_network_info_with_advanced_settings()
        self.set_background_wmm()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def enable_content_filtering(self):
        self.buy_time()
        logger.debug("BasicInfoPage : Enable content_filtering")
        self.content_filtering_dropdown.set(self.config.config_vars.basic_enabled)
        
    def employee_network_with_advanced_settings_enable_content_filtering(self):
        self.employee_network_info_with_advanced_settings()
        self.enable_content_filtering()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def set_5ghz_band(self):
        self.buy_time()
        logger.debug("BasicInfoPage : Set band to 5 GHZ ")
        self.band.set(self.config.config_vars.band)
        
    def employee_network_with_advanced_settings_5ghz_band(self):
        self.employee_network_info_with_advanced_settings()
        self.set_5ghz_band()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def enable_disable_ssid(self):
        self.buy_time()
        if self.disable_ssid:
            logger.debug('BasicInfoPage : Enable disable ssid.')
            self.disable_ssid.click()
            
    def employee_network_with_advanced_settings_enable_disable_ssid(self):
        self.employee_network_info_with_advanced_settings()
        self.enable_disable_ssid()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def create_and_assert_employee_network_with_content_filtering(self):
        '''
            Clicking on show advanced options and enabling Content Filtering
        '''
        import time
        import traceback
        logger.debug('Basic Info Page : Clicking on Wireless')
        self.wireless.click()
        if not self.employee.is_selected():
            raise AssertionError("Employee radio is not selected i.e . Traceback: %s" % traceback.format_exc())         
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')      
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('Basic Info Page : Entering network name') 
        self.networkname.set(self.config.config_vars.Network_name)
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Show Advanced Options')
        self.show_advanced_options.click()
        self.buy_time()
        logger.debug('Basic Info Page : Enabling Content Filtering')
        self.content_filtering_dropdown.set(self.config.config_vars.content_filtering_value)
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
    
    def create_and_assert_employee_network_with_disable_ssid(self):
        '''
            Clicking on show advanced options and checking disable ssid
        '''
        import time
        import traceback
        logger.debug('Basic Info Page : Clicking on Wireless')
        self.wireless.click()
        if not self.employee.is_selected():
            raise AssertionError("Employee radio is not selected i.e . Traceback: %s" % traceback.format_exc())         
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')      
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('Basic Info Page : Entering network name') 
        self.networkname.set(self.config.config_vars.Network_name)
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Show Advanced Options')
        self.show_advanced_options.click()
        self.buy_time()
        if not self.inactivity_timeout:
            self.show_advanced_options.click()
        logger.debug('Basic Info Page : Enabling disabled ssid')
        self.disable_ssid.click()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def create_and_assert_voice_network_with_disable_ssid(self):
        '''
            Clicking on show advanced options and checking disable ssid
        '''
        import time
        import traceback
        logger.debug('Basic Info Page : Clicking on Wireless')
        self.wireless.click()
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on voice ')
        self.voice.click()
        if not self.voice.is_selected():
            raise AssertionError("Voice radio is not selected i.e . Traceback: %s" % traceback.format_exc())            
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')      
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('Basic Info Page : Entering network name') 
        self.networkname.set(self.config.config_vars.Network_name)
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Show Advanced Options')
        self.show_advanced_options.click()
        self.buy_time()
        if not self.inactivity_timeout:
            self.show_advanced_options.click()      
        logger.debug('Basic Info Page : Enabling disabled ssid')
        self.disable_ssid.click()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
    
    def employee_network_info_with_can_be_used_without_uplink(self):
        '''
            Clicking on show advanced options and checking can_be_used_without_uplink
        '''
        import time
        import traceback
        logger.debug('Basic Info Page : Clicking on Wireless')
        self.wireless.click()
        if not self.employee.is_selected():
            raise AssertionError("Employee radio is not selected i.e . Traceback: %s" % traceback.format_exc())         
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')      
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('Basic Info Page : Entering network name') 
        self.networkname.set(self.config.config_vars.Network_name)
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Show Advanced Options')
        self.show_advanced_options.click()
        self.buy_time()
        if not self.inactivity_timeout:
            self.show_advanced_options.click()
        logger.debug('Basic Info Page : Enabling CAN BE USED WITHOUT UPLINK')
        self.without_uplink.click()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def voice_network_info_with_can_be_used_without_uplink(self):
        '''
            Clicking on show advanced options and checking can_be_used_without_uplink
        '''
        import time
        import traceback
        logger.debug('Basic Info Page : Clicking on Wireless')
        self.wireless.click()
        logger.debug('Basic Info Page : Clicking on voice')
        self.voice.click()
        if not self.voice.is_selected():
            raise AssertionError("Voice radio is not selected i.e . Traceback: %s" % traceback.format_exc())            
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')      
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('Basic Info Page : Entering network name') 
        self.networkname.set(self.config.config_vars.Network_name)
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Show Advanced Options')
        self.show_advanced_options.click()
        self.buy_time()
        if not self.inactivity_timeout:
            self.show_advanced_options.click()
        logger.debug('Basic Info Page : Enabling CAN BE USED WITHOUT UPLINK')
        self.without_uplink.click()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
    
    def employee_network_info_with_max_client_threshold(self):
        '''
            Clicking on show advanced options and edit max client threshold
        '''
        import time
        import traceback
        logger.debug('Basic Info Page : Clicking on Wireless')
        self.wireless.click()
        if not self.employee.is_selected():
            raise AssertionError("Employee radio is not selected i.e . Traceback: %s" % traceback.format_exc())         
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')      
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('Basic Info Page : Entering network name') 
        self.networkname.set(self.config.config_vars.Network_name)
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Show Advanced Options')
        self.show_advanced_options.click()
        self.buy_time()
        if not self.inactivity_timeout:
            self.show_advanced_options.click()
        logger.debug('Basic Info Page : Entering valid value in MAX Client Threashold ')
        self.max_client_threshold.set(self.config.config_vars.valid_max_client_threshold)
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def voice_network_info_with_max_client_threshold(self):
        '''
            Clicking on show advanced options and edit max client threshold
        '''
        import time
        import traceback
        logger.debug('Basic Info Page : Clicking on Wireless')
        self.wireless.click()
        if not self.employee.is_selected():
            raise AssertionError("Employee radio is not selected i.e . Traceback: %s" % traceback.format_exc())         
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')      
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('Basic Info Page : Entering network name') 
        self.networkname.set(self.config.config_vars.Network_name)
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Show Advanced Options')
        self.show_advanced_options.click()
        self.buy_time()
        if not self.inactivity_timeout:
            self.show_advanced_options.click()
        logger.debug('Basic Info Page : Entering valid value in MAX Client Threashold ')
        self.max_client_threshold.set(self.config.config_vars.valid_max_client_threshold)
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
    
    def employee_network_info_with_local_probe_request_threshold(self,value):
        '''
            Clicking on show advanced options and edit local probe request threshold
        '''
        import time
        import traceback
        logger.debug('Basic Info Page : Clicking on Wireless')
        self.wireless.click()
        if not self.employee.is_selected():
            raise AssertionError("Employee radio is not selected i.e . Traceback: %s" % traceback.format_exc())         
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')      
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('Basic Info Page : Entering network name') 
        self.networkname.set(self.config.config_vars.Network_name)
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Show Advanced Options')
        self.show_advanced_options.click()
        self.buy_time()
        logger.debug('Basic Info Page : Entering valid value in Local Probe Request Threashold ')
        self.local_probe_req_textbox.set(value)
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
    
    
    def employee_network_info_with_inactive_timeout(self,value):
        '''
            Clicking on show advanced options and edit inactive timeout
        '''
        import time
        import traceback
        logger.debug('Basic Info Page : Clicking on Wireless')
        self.wireless.click()
        if not self.employee.is_selected():
            raise AssertionError("Employee radio is not selected i.e . Traceback: %s" % traceback.format_exc())         
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')      
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('Basic Info Page : Entering network name') 
        self.networkname.set(self.config.config_vars.Network_name)
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Show Advanced Options')
        self.show_advanced_options.click()
        self.buy_time()
        if not self.inactivity_timeout:
            self.show_advanced_options.click()
        logger.debug('Basic Info Page : Entering invalid value in Local Probe Request Threashold ')
        self.inactivity_timeout.set('1')
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        if not self.inactivity_timeout_error:
            raise AssertionError("Inactivity timeout error is not visible i.e . Traceback: %s" % traceback.format_exc())
        logger.debug('Basic Info Page : Entering valid value in Local Probe Request Threashold ')
        self.inactivity_timeout.set(value)
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def voice_network_info_with_inactive_timeout(self,value):
        '''
            Clicking on show advanced options and edit inactive timeout
        '''
        import time
        import traceback
        logger.debug('Basic Info Page : Clicking on Wireless')
        self.wireless.click()
        self.voice.click()
        if not self.voice.is_selected():
            raise AssertionError("Voice radio is not selected i.e . Traceback: %s" % traceback.format_exc())            
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')      
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('Basic Info Page : Entering network name') 
        self.networkname.set(self.config.config_vars.Network_name)
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Show Advanced Options')
        self.show_advanced_options.click()
        self.buy_time()
        if not self.inactivity_timeout:
            self.show_advanced_options.click()
        logger.debug('Basic Info Page : Entering invalid value in Local Probe Request Threashold ')
        self.inactivity_timeout.set('1')
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        if not self.inactivity_timeout_error:
            raise AssertionError("Inactivity timeout error is not visible i.e . Traceback: %s" % traceback.format_exc())
        logger.debug('Basic Info Page : Entering valid value in Local Probe Request Threashold ')
        self.inactivity_timeout.set(value)
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
    
    def employee_network_info_with_hide_ssid(self):
        '''
            Clicking on show advanced options and click on hide ssid        
        '''
        import time
        import traceback
        logger.debug('Basic Info Page : Clicking on Wireless')
        self.wireless.click()
        if not self.employee.is_selected():
            raise AssertionError("Employee radio is not selected i.e . Traceback: %s" % traceback.format_exc())         
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')      
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('Basic Info Page : Entering network name') 
        self.networkname.set(self.config.config_vars.Network_name)
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Show Advanced Options')
        self.show_advanced_options.click()
        self.buy_time()
        if not self.inactivity_timeout:
            self.show_advanced_options.click()
        logger.debug('Basic Info Page : Clicking on hide ssid')
        self.hide_ssid_checkbox.click()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def voice_network_info_with_hide_ssid(self):
        '''
            Clicking on show advanced options and click on hide ssid        
        '''
        import time
        import traceback
        logger.debug('Basic Info Page : Clicking on Wireless')
        self.wireless.click()
        if not self.employee.is_selected():
            raise AssertionError("Employee radio is not selected i.e . Traceback: %s" % traceback.format_exc())         
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')      
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('Basic Info Page : Entering network name') 
        self.networkname.set(self.config.config_vars.Network_name)
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Show Advanced Options')
        self.show_advanced_options.click()
        self.buy_time()
        if not self.inactivity_timeout:
            self.show_advanced_options.click()
        logger.debug('Basic Info Page : Clicking on hide ssid')
        self.hide_ssid_checkbox.click()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def enable_hide_ssid(self):
        self.buy_time()
        if self.hide_ssid_checkbox:
            logger.debug('BasicInfoPage : Enable hide ssid.')
            self.hide_ssid_checkbox.click()
            
    def employee_network_with_advanced_settings_enable_hide_ssid(self):
        self.employee_network_info_with_advanced_settings()
        self.enable_hide_ssid()
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def voice_network_info_with_advanced_settings(self):
        logger.debug('Basic Info Page : Clicking on Wireless radio button') 
        self.wireless.click()
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('Basic Info Page : Entering network name') 
        self.networkname.set(self.config.config_vars.Network_name)
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on voice ')    
        self.voice.click()
        self.buy_time()
        self.click_advanced_settings()
        
    def voice_network_info_with_advanced_settings_broadcasefiltering_dtiminterval(self):
        self.voice_network_info_with_advanced_settings()
        self.configure_broadcasefiltering_dtiminterval()
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def voice_network_with_advanced_settings(self):
        self.voice_network_info_with_advanced_settings()
        self.set_broadcasefiltering_dtiminterval()
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    
    def voice_network_with_advanced_settings_background_wmm(self):
        self.voice_network_info_with_advanced_settings()
        self.set_background_wmm()
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def voice_network_with_advanced_settings_besteffort_wmm_share(self):
        self.voice_network_info_with_advanced_settings()
        self.set_besteffort_wmm_share()
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def voice_network_with_advanced_settings_video_wmm_share(self):
        self.voice_network_info_with_advanced_settings()
        self.set_video_wmm_share('0')
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def voice_network_with_advanced_settings_voice_wmm_share(self):
        self.voice_network_info_with_advanced_settings()
        self.set_voice_wmm_share()
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def voice_network_with_advanced_settings_enable_content_filtering(self):
        self.voice_network_info_with_advanced_settings()
        self.enable_content_filtering()
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def voice_network_with_advanced_settings_5ghz_band(self):
        self.voice_network_info_with_advanced_settings()
        self.set_5ghz_band()
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def voice_network_with_advanced_settings_enable_disable_ssid(self):
        self.voice_network_info_with_advanced_settings()
        self.enable_disable_ssid()
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def voice_network_with_advanced_settings_enable_hide_ssid(self):
        self.voice_network_info_with_advanced_settings()
        self.enable_hide_ssid()
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def set_advance_options(self,uplink=False,max_threshold=False,inactivity_timeout=False,hide_ssid=False,local_probe=False,disable_ssid=False):
        import traceback
        self.voice_network_info_with_advanced_settings()
        self.buy_time()
        if uplink:
            logger.debug('Basic Info Page: Enable without uplink checkbox .')
            self.without_uplink.click()
            self.buy_time()
        if max_threshold:
            logger.debug("Basic Info Page: Set max client threshold.")      
            self.max_client_threshold.set(self.config.config_vars.max_client_threshold)
        if hide_ssid:   
            logger.debug("Basic Info Page: Enable hide ssid.")      
            self.hide_ssid_checkbox.click()
        if local_probe:
            logger.debug("Basic Info Page: Set LOCAL PROBE REQUEST THRESHOLD.")     
            self.local_probe_req_textbox.set(self.config.config_vars.local_probe_request_threshold)
        if inactivity_timeout :
            logger.debug('Basic Info Page: Set invalid inactivity timeout.')
            self.inactivity_timeout.set(self.config.config_vars.invalid_inactivity_timeout)
            logger.debug('Basic Info Page : Clicking on Next')  
            self.next.click()
            if not self.inactivity_error:
                raise AssertionError("Invalid inactivity error message not displayed .Traceback: %s " %traceback.format_exc())
            logger.debug('Basic Info Page : Set valid inactivity timeout.')
            self.inactivity_timeout.set(self.config.config_vars.valid_inactivity_timeout)
            
        if disable_ssid:
            logger.debug('BasicInfoPage : Enable disable ssid.')
            self.disable_ssid.click()
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def employee_network_info_with_specific_name(self,name,flag):
        logger.debug('Basic Info Page : Clicking on wireless radio button') 
        self.wireless.click()
        logger.debug('Basic Info Page : writting network name') 
        self.networkname.set(name)
        self.buy_time()
#       self.voice.click()
#       self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        if flag:
            return VirtualLanPage(self.test, self.browser, self.config)
    
    def assert_duplicate_network_error_message(self):
        '''
            Asserting duplicate network error message
        '''
        import traceback
        if not self.duplicate_network_name_error_msg:
            raise AssertionError("Duplicate network error message is not visible: %s " %traceback.format_exc())
        logger.debug('BasicInfoPage : Clicking on OK button')
        self.message_dialog_ok_button.click()
        logger.debug('BasicInfoPage : Clicking on Cancel button')
        self.basic_info_cancel_button.click()
        self.buy_time()
        
    def validate_network_name(self):
        '''
        validating the field "name"
        in BasicInfoPage
        '''
        self.buy_time()
        self.set_invalid_network_name(self.config.config_vars.ntwrk_name_spcl_char_invalid)
        self.buy_time()
        self.set_invalid_network_name(self.config.config_vars.ntwrk_name_blank)
        self.buy_time()
        self.set_invalid_network_name(self.config.config_vars.ntwrk_name_max)
    
    def set_invalid_network_name(self,netwrk_name):
        logger.debug('BasicInfoPage: writing network name in textbox "Name" ')
        self.networkname.set(netwrk_name)
        logger.debug('BasicInfoPage: clicking "Next" button ')
        self.next.click()
        if netwrk_name == 'ntwrk_name_spcl_char_invalid':
            if not self.spcl_char_error_msg:
                raise AssertionError("'Quotes are not allowed' error message not found. Traceback: %s " %traceback.format_exc())
            
        if netwrk_name == 'ntwrk_name_blank':
            if not self.name_error:
                raise AssertionError("'This field is required' error message not found. Traceback: %s " %traceback.format_exc())
        
        if netwrk_name == 'ntwrk_name_max':
            if not self.max_length_error_msg:
                raise AssertionError("'This field is required' error message not found. Traceback: %s " %traceback.format_exc())

    
    def assert_employee_radio_button(self):
        import traceback
        if not self.employee.is_selected():
            raise AssertionError("Basic Info Page: Employee radio is not selected by default . i.e. Traceback: %s" %traceback.format_exc())
        
        
    def assert_broadcasefiltering(self, broad):
        logger.debug("Basic Info Page : Assert 'Broadcasefiltering' drop down value...")
        if not self.broadcasefiltering.get_selected() == broad:
            raise AssertionError("'Broadcasefiltering' drop down not set to '%s'.Traceback: %s " %(broad,traceback.format_exc()))
            
    def assert_dtiminterval(self, dtim):
        logger.debug("Basic Info Page : Assert 'Dtiminterval' drop down value...")
        if not self.dtiminterval.get_selected() == dtim:
            raise AssertionError("'Dtiminterval' drop down not set to '%s'.Traceback: %s " %(dtim,traceback.format_exc()))
            
    def assert_multicastratetransmissionl(self, multicast):
        logger.debug("Basic Info Page : Assert 'MULTICAST TRANSMISSION OPTIMIZATION' drop down value...")
        if not self.multicastratetransmission.get_selected() == multicast:
            raise AssertionError("'MULTICAST TRANSMISSION OPTIMIZATION' drop down not set to '%s'.Traceback: %s " %(multicast,traceback.format_exc()))
            
    def assert_dynamicmulticast(self, dynamic):
        logger.debug("Basic Info Page : Assert 'Dynamic Multicast Optimization ' drop down value...")
        if not self.dynamicmulticast.get_selected() == dynamic:
            raise AssertionError("'Dynamic Multicast Optimization ' drop down not set to '%s'.Traceback: %s " %(dynamic,traceback.format_exc()))
            
    def assert_transmit_rates_2_Ghz_defaults(self):
        '''
            Validate the transmit rates 2.4GHz default values
        '''
        import traceback
        logger.debug("Clicking the Hide Advanced Option. ")
        self.show_advanced_options.click()
        logger.debug("Validating the default values ")
        if not self.band_24ghzmin.get_selected()== self.config.config_vars.band_24ghzmin_default:
            raise AssertionError("2.4GHz min value is not set to default. Traceback: %s " %traceback.format_exc())
            
        if not self.band_24ghzmax.get_selected()== self.config.config_vars.band_24ghzmax_default:
            raise AssertionError("2.4GHz min value is not set to default. Traceback: %s " %traceback.format_exc())
        
        time.sleep(4)
        logger.debug('Basic Info Page : Clicking on Cancel button') 
        self.basic_info_cancel_button.click()
        
    def assert_transmit_rates_5_Ghz_defaults(self):
        '''
            Validate the transmit rates 5GHz default values
        '''
        import traceback
        logger.debug("Clicking the Hide Advanced Option. ")
        self.show_advanced_options.click()
        logger.debug("Validating the default values ")
        if not self.band_5ghzmin.get_selected()== self.config.config_vars.band_5ghzmin_default:
            raise AssertionError("5GHz min value is not set to default. Traceback: %s " %traceback.format_exc())
            
        if not self.band_5ghzmax.get_selected()== self.config.config_vars.band_5ghzmax_default:
            raise AssertionError("5GHz min value is not set to default. Traceback: %s " %traceback.format_exc())
        time.sleep(4)
        logger.debug('Basic Info Page : Clicking on Cancel button') 
        self.basic_info_cancel_button.click()
        
    def assert_content_filtering_defaults(self):
        '''
            Validate the content filtering default values
        '''
        import traceback
        logger.debug("Clicking the Hide Advanced Option. ")
        self.show_advanced_options.click()
        logger.debug("Validating the default values ")
        if not self.content_filtering_dropdown.get_selected() == self.config.config_vars.content_filtering_default:
            raise AssertionError("Default value for content filtering is not selected  Traceback: %s " %traceback.format_exc())
        
        time.sleep(4)
        logger.debug('Basic Info Page : Clicking on Cancel button') 
        self.basic_info_cancel_button.click()
        
        
    def assert_band_field_defaults(self):
        '''
            Validate the band field default values
        '''
        import traceback
        logger.debug("Clicking the Hide Advanced Option. ")
        self.show_advanced_options.click()
        logger.debug("Validating the default values ")
        if not self.band.get_selected() == self.config.config_vars.band_default:
            raise AssertionError("Default value for Band field is not selected Traceback: %s " %traceback.format_exc())
        
        time.sleep(4)
        logger.debug('Basic Info Page : Clicking on Cancel button') 
        self.basic_info_cancel_button.click()       
        
    def assert_inactivity_timeout_defaults(self):
        '''
            Validate the inactivity timeout default values
        '''
        import traceback
        logger.debug("Clicking the Hide Advanced Option. ")
        self.show_advanced_options.click()
        logger.debug("Validating the default values ")
        if not self.inactivity_timeout.get() == self.config.config_vars.inactivity_timeout_default:
            raise AssertionError("Default value is not selected for inactivity timeout field Traceback: %s " %traceback.format_exc())
        
        time.sleep(4)
        logger.debug('Basic Info Page : Clicking on Cancel button') 
        self.basic_info_cancel_button.click()
        
    def create_wired_guest_network(self):
        logger.debug('BasicInfoPage: Clicking on wired radio button')
        self._click_on_wired()
        logger.debug('BasicInfoPage: Writing network name-Test1949')
        self.networkname.set(self.config.config_vars.valid_network_name)
        logger.debug('BasicInfoPage: Clicking on guest radio button')
        self.wired_network_guest.click()
        logger.debug('BasicInfoPage: Setting speed 100 and duplex: Full')
        self.set_speed_duplex(self.config.config_vars.basic_speed, self.config.config_vars.full_duplex)
        logger.debug('BasicInfoPage: POE is set to Enabled')
        self.set_POE(self.config.config_vars.poe_disabled)
        logger.debug('BasicInfoPage: Admin Status is set to Up')
        self.set_admin_status(self.config.config_vars.admin_status_up)
        logger.debug('BasicInfoPage: Content filtering - Enabled')
        self.set_content_filtering(self.config.config_vars.basic_filter)
        logger.debug('BasicInfoPage: Uplink - Enabled')
        self.set_uplink(self.config.config_vars.basic_uplink)
        logger.debug('BasicInfoPage: Spanning tree - Enabled')
        self.spanning_tree.set(self.config.config_vars.Spanning_Tree_Status)
        logger.debug('BasicInfoPage: Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def set_speed_duplex(self, speed, duplex):  
        if speed == '100' :
            logger.debug('BasicInfoPage: Show Advanced options: Selecting basic speed')
            self.speed.set(self.config.config_vars.basic_speed)
        elif speed == '10' :
            logger.debug('BasicInfoPage: Show Advanced options: Selecting speed 10')
            self.speed.set(self.config.config_vars.speed_10)
        elif speed == '1000' :
            logger.debug('BasicInfoPage: Show Advanced options: Selecting basic speed 100')
            self.speed.set(self.config.config_vars.speed_1000)
        
        if duplex == 'Half' :
            logger.debug('BasicInfoPage: Show Advanced options: Selecting duplex half')
            self.duplex.set(self.config.config_vars.basic_duplex)
        elif duplex == 'Full' :
            logger.debug('BasicInfoPage: Show Advanced options: Selecting duplex Full')
            self.duplex.set(self.config.config_vars.full_duplex)
    
    def set_POE(self, value ='None'):
        if value == 'Disabled' :
            logger.debug('BasicInfoPage: Show Advanced options: Selecting POE disabled')
            self.Wired_POE.set(self.config.config_vars.poe_disabled)
        else :
            logger.debug('BasicInfoPage: Show Advanced options: Selecting POE enabled')
            self.Wired_POE.set(self.config.config_vars.poe_enabled)
    
    def set_admin_status(self,value):
        if value == 'Down':
            logger.debug('BasicInfoPage: Show Advanced options: Selecting admin status down')
            self.admin_status.set(self.config.config_vars.basic_admin)
        elif value == 'Up' :
            logger.debug('BasicInfoPage: Show Advanced options: Selecting admin status up')
            self.admin_status.set(self.config.config_vars.admin_status_up)
    
    def set_content_filtering(self,value):
        if value == 'Enabled' :
            logger.debug('BasicInfoPage: Show Advanced options: Selecting basic filtering enabled')
            self.filtering.set(self.config.config_vars.basic_filter)
        else:
            logger.debug('BasicInfoPage: Show Advanced options: Selecting basic filtering disabled')
            self.filtering.set(self.config.config_vars.content_filtering_default)
    
    def set_uplink(self,value): 
        if value == 'Disabled':
            logger.debug('BasicInfoPage: Show Advanced options: Selecting wired uplink disabled')
            self.Wired_Uplink.set(self.config.config_vars.uplink_disabled)
        else :
            logger.debug('BasicInfoPage: Show Advanced options: Selecting wired uplink enabled')
            self.Wired_Uplink.set(self.config.config_vars.basic_uplink)
            
    def wired_employee_network_info_with_specific_name(self,name):
        self._click_on_wired()
        self.buy_time()
        logger.debug('BasicInfoPage: Clicking on next button')
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        logger.debug('BasicInfoPage: writing network name')
        self.networkname.set(name)
        self.assert_wired_configuration_defaults()
        self.buy_time()
        logger.debug('BasicInfoPage: Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def wired_guest_network_info_with_specific_name(self,name):
        self._click_on_wired()
        self.buy_time()
        logger.debug('BasicInfoPage: Clicking on next button')
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('BasicInfoPage: Clicking wired guest radio button')
        self.wired_network_guest.click()
        self.buy_time()
        logger.debug('BasicInfoPage: Clicking wired guest radio button')
        self.wired_network_guest.click()
        self.buy_time()
        logger.debug('BasicInfoPage: writing network name')
        self.networkname.set(name)
        self.buy_time()
        logger.debug('BasicInfoPage: Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def specific_wired_guest_network_info_changed(self,name):
        self._click_on_wired()
        self.buy_time()
        logger.debug('BasicInfoPage: Clicking on next button')
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        logger.debug('BasicInfoPage: writing network name')
        self.networkname.set(name)
        self.buy_time()
        logger.debug('BasicInfoPage:Clicking on guest radio button')
        self.wired_network_guest.click()
        self.buy_time()
        # import traceback
        # if not self.speed.selected=='10':
            # raise AssertionError("Speed is not 10 by default .Traceback: %s " %traceback.format_exc())
        # if not self.duplex.selected=='Half':
            # raise AssertionError("duplex is not Half by default .Traceback: %s " %traceback.format_exc()) 
        # if not self.Wired_POE.selected=='Disabled':
            # raise AssertionError("POE not Disabled by default by default .Traceback: %s " %traceback.format_exc())
        # if not self.admin_status.selected=='Down':
            # raise AssertionError("Admin status not Down by default .Traceback: %s " %traceback.format_exc())
        # if not self.filtering.selected=='Enabled':
            # raise AssertionError("Content filtering not Enabled Up by default .Traceback: %s " %traceback.format_exc())
        # if not self.Wired_Uplink.selected=='Enabled':
            # raise AssertionError("Wired up link not Enabled Up by default .Traceback: %s " %traceback.format_exc())
        # if not self.spanning_tree.selected=='Enabled':
            # raise AssertionError("Spanning tree not Enabled Up by default .Traceback: %s " %traceback.format_exc())       
        logger.debug('Network page :BasicInfoPage:Show advanced options : Writing  speed')
        self.speed.set('1000')
        logger.debug('Network page :BasicInfoPage:Show advanced options : Selecting admin status up ')
        self.admin_status.set('Up')
        logger.debug('Network page :BasicInfoPage:Show advanced options : Selecting wired POE : Enabled ')
        self.Wired_POE.set(self.config.config_vars.basic_enabled)
        logger.debug('Network page :BasicInfoPage:Show advanced options : Selecting Filtering : Enabled ')
        self.filtering.set(self.config.config_vars.basic_enabled)
        logger.debug('Network page :BasicInfoPage:Show advanced options : Selecting Uplink : Enabled ')
        self.Wired_Uplink.set(self.config.config_vars.basic_enabled)
        logger.debug('Network page :BasicInfoPage:Show advanced options : Selecting Spanning tree: Enabled ')
        self.spanning_tree.set(self.config.config_vars.basic_enabled)
        self.buy_time()
        logger.debug('BasicInfoPage: Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)

        
    def set_dynamic_multicast_optimization(self,value=None):
        '''
        selects given value to dynamic multicast optimization
        '''
        if value:
            logger.debug('Network page :BasicInfoPage:Show advanced options : writing dynamic multicast ')
            self.dynamicmulticast.set(value)
        else:
            logger.debug('Network page :BasicInfoPage:Show advanced options : writing dynamic multicast default value ')
            self.dynamicmulticast.set(self.config.config_vars.dynamicmulticast_default)
            
    def set_inactivity_timeout_value(self,value=None):
        '''
        sets given value to inactivity time out
        '''
        if value:
            logger.debug('Network page :BasicInfoPage:Show advanced options : writing inactivity time out ')
            self.inactivity_timeout.set(value)
        else:
            logger.debug('Network page :BasicInfoPage:Show advanced options : writing inactivity time out: default value ')
            self.inactivity_timeout.set(self.config.config_vars.inactivity_timeout_default)
        
    def set_local_probe_req_textbox_value(self,value=None):
        '''
        sets given value to local probe request textbox 
        '''
        if value:
            logger.debug('Network page :BasicInfoPage:Show advanced options : writing local probe request ')
            self.local_probe_req_textbox.set(value)
        else:
            logger.debug('Network page :BasicInfoPage:Show advanced options : writing local probe request ')
            self.local_probe_req_textbox.set(self.config.config_vars.local_probe_default)
        
    
    def setting_hide_advance_option_value(self):
        import time
        self.set_dynamic_multicast_optimization(self.config.config_vars.dynamicmulticast_value)
        self.enable_content_filtering()
        self.set_inactivity_timeout_value(self.config.config_vars.valid_inactivity_timeout)
        self.enable_hide_ssid()
        self.set_local_probe_req_textbox_value(self.config.config_vars.local_probe_value)
        logger.debug('Network page :BasicInfoPage:Show advanced options : clicking air time checkbox')
        self.airtime_check_box.click()
        time.sleep(3)
        logger.debug('Network page :BasicInfoPage:Show advanced options : writing air time')
        self.airtime.set(self.config.config_vars.airtime_value)
        self.set_background_wmm(self.config.config_vars.background_wmm_value)
        self.set_besteffort_wmm_share(self.config.config_vars.besteffort_wmm_value)
        self.set_video_wmm_share(self.config.config_vars.video_wmm_share_value)
        self.set_voice_wmm_share(self.config.config_vars.voice_wmm_share_value)
        self.buy_time()
        logger.debug('Network page :BasicInfoPage:clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)     
        
    def set_name_field(self):
        logger.debug("BasicInfoPage : writting '%s' into 'NAME(SSID)' field..")
        self.networkname.set(self.config.config_vars.Network_name)
        logger.debug("BasicInfoPage : Clicking 'Next' button..")
        self.next.click()
        
    def wired_test_1934_info(self):
        self._click_on_wired()
        self.buy_time()
        logger.debug('Network page :BasicInfoPage:clicking on next button')
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.networkname.set(self.config.config_vars.new_test_1934)
        self.assert_wired_configuration_defaults()
        self.buy_time()
        logger.debug('Network page :BasicInfoPage:clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def click_wired_network(self):
        logger.debug('Network page :BasicInfoPage:clicking on wired radio button')
        self.wired.click()
        self.buy_time()
        
        
    def assert_broadcasefiltering_dropdown_values(self):
        logger.debug('BasicInfoPage : Getting all options from Broadcast Filtering')
        options = self.broadcasefiltering.get_options()
        if not options[2] == self.config.config_vars.broadcasefiltering_all:
            raise AssertionError("Broadcast Filtering ALL element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[1] == self.config.config_vars.broadcasefiltering_arp:
            raise AssertionError("Broadcast Filtering ARP element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[0] == self.config.config_vars.basic_disabled:
            raise AssertionError("Broadcast Filtering Disabled element not matched i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_multicastratetransmission_dropdown_values(self):
        logger.debug('BasicInfoPage : Getting all options from multicast transmission optimization')
        options = self.multicastratetransmission.get_options()
        if not options[1] == self.config.config_vars.basic_enabled:
            raise AssertionError("multicast transmission optimization Enabled element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[0] == self.config.config_vars.basic_disabled:
            raise AssertionError("multicast transmission optimization Disabled element not matched i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_dynamicmulticast_dropdown_values(self):
        logger.debug('BasicInfoPage : Getting all options from dynamic multicast optimization')
        options = self.dynamicmulticast.get_options()
        if not options[1] == self.config.config_vars.basic_enabled:
            raise AssertionError("Dynamic multicast optimization Enabled element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[0] == self.config.config_vars.basic_disabled:
            raise AssertionError("Dynamic multicast optimization Disabled element not matched i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_content_filtering_dropdown(self):
        logger.debug('BasicInfoPage : Getting all options from content filtering')
        options = self.content_filtering_dropdown.get_options()
        if not options[1] == self.config.config_vars.basic_enabled:
            raise AssertionError("content filtering Enabled element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[0] == self.config.config_vars.basic_disabled:
            raise AssertionError("content filtering Disabled element not matched i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_band_dropdown(self):
        logger.debug('BasicInfoPage : Getting all options from Band')
        options = self.band.get_options()
        if not options[2] == self.config.config_vars.band:
            raise AssertionError("Band 5 Ghz element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[1] == self.config.config_vars.band24:
            raise AssertionError("Band 2.4 Ghz element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[0] == self.config.config_vars.band_default:
            raise AssertionError("Band All element not matched i.e. Traceback: %s" %traceback.format_exc())
            
            
    def assert_dropdown_default_values(self,broadcasefiltering=False,dtiminterval=False,multicastratetransmission=False,dynamicmulticast=False,content_filtering=False,band=False ):
        conf = self.config.config_vars
        if broadcasefiltering :
            self.browser.assert_drop_down_value(self.broadcasefiltering,conf.basic_disabled,'BROADCAST FILTERING is not set to Disabled')
        if dtiminterval :
            self.browser.assert_drop_down_value(self.dtiminterval,conf.dtiminterval_1_beacon,'DTIMINTERVAL is not set to 1 beacon')
        if multicastratetransmission :
            self.browser.assert_drop_down_value(self.multicastratetransmission,conf.basic_disabled,'MULTICASTRATETRANSMISSION is not set to Disabled')
        if dynamicmulticast :
            self.browser.assert_drop_down_value(self.dynamicmulticast,conf.basic_disabled,'DYNAMICMULTI CAST is not set to Disabled')
        if content_filtering :
            self.browser.assert_drop_down_value(self.content_filtering,conf.basic_disabled,'CONTENT FILTERING is not set to Disabled')
        if band :
            self.browser.assert_drop_down_value(self.band,conf.band_default,'Band is not set to All')
        
            
    def assert_local_probe_request_threshold(self):
        logger.debug("BasicInfoPage: Asserting Local Probe Request Threshold default value")
        if not self.local_probe_req_textbox.get() == self.config.config_vars.local_probe_default:
            raise AssertionError("BasicInfoPage: Local Probe Request Threshold not set to default")

    def assert_max_client_threshold(self):
        logger.debug("BasicInfoPage: Asserting Max Client Threshold default value")
        if not self.max_client_threshold.get() == self.config.config_vars.max_client_default:
            raise AssertionError("BasicInfoPage: Max Client Threshold not set to default")

    def assert_can_be_used_without_uplink(self):
        logger.debug("BasicInfoPage: Asserting Can Be Used Without Uplink default value")
        if self.without_uplink.is_selected:
            raise AssertionError("BasicInfoPage: Can Be Used Without Uplink is enable")

    def assert_disable_ssid(self):
        logger.debug("BasicInfoPage: Asserting Disable SSID default value")
        if self.disable_ssid.is_selected:
            raise AssertionError("BasicInfoPage: Disable SSID is enable")

    def assert_hide_ssid(self):
        logger.debug("BasicInfoPage: Asserting HIDE SSID default value")
        if self.hide_ssid_checkbox.is_selected:
            raise AssertionError("BasicInfoPage: HIDE SSID is enable")

    def assert_inactivity_timeout(self):
        logger.debug("BasicInfoPage: Asserting Inactivity Timeout value")
        if not self.inactivity_timeout.get() == self.config.config_vars.inactivity_timeout_default:
            raise AssertionError("BasicInfoPage: Inactivity Timeout not set to default")

    def assert_dmo_channel_utilization_threshold(self):
        logger.debug("BasicInfoPage: Asserting DMO Channel Utilization Threshold value")
        if not self.dmo_channel_utilization_threshold.get() == self.config.config_vars.background_wmm:
            raise AssertionError("BasicInfoPage: DMO Channel Utilization Threshold not set to default")

    def assert_wmm_share_value(self):
        '''
        assert background wmm share
        assert best effort wmm share
        assert video wmm share
        assert voice wmm share
        '''
        conf = self.config.config_vars
        self.browser.assert_text(self.background_wmm,conf.invalid_airtime,'background wmm value not set to default','value')
        self.browser.assert_text(self.besteffort_wmm_share,conf.invalid_airtime,'best effort wmm value not set to default','value')
        self.browser.assert_text(self.video_wmm_share,conf.invalid_airtime,'video wmm value not set to default','value')
        self.browser.assert_text(self.voice_wmm_share,conf.invalid_airtime,'voice wmm value not set to default','value')
        
    def assert_2_Ghz_dropdown_options(self,min_max,option_list):
        '''
        Asserting 2.4Ghz dropdown options
        '''
        logger.debug('Network page :BasicInfoPage:Checking for 2.4Ghz min or max dropdown options')
        if min_max == 'min':
            options = self.band_24ghzmin.get_options()
            if not (options == option_list):
                raise AssertionError(" Options are missing or new option/options found Traceback: %s " %traceback.format_exc())
        elif min_max == 'max':
            options = self.band_24ghzmax.get_options()
            if not (options == option_list):
                raise AssertionError(" Options are missing or new option/options found Traceback: %s " %traceback.format_exc())

    def assert_5_Ghz_dropdown_options(self,min_max,option_list):
        '''
        Asserting 5Ghz dropdown options
        '''
        logger.debug('Network page :BasicInfoPage:Checking for 5Ghz min or max dropdown options')
        if min_max == 'min':
            options = self.band_5ghzmin.get_options()
            if not (options == option_list):
                raise AssertionError(" Options are missing or new option/options found Traceback: %s " %traceback.format_exc())
        elif min_max == 'max':
            options = self.band_5ghzmax.get_options()
            if not (options == option_list):
                raise AssertionError(" Options are missing or new option/options found Traceback: %s " %traceback.format_exc())

    def assert_bandwidth_limits_airtime_checkbox(self):
        '''
        Asserting whether the airtime checkbox is disabled
        '''
        logger.debug('Network page :BasicInfoPage:Checking AIRTIME checkbox disabled')
        if self.airtime_check_box.is_selected() : 
            raise AssertionError("AIRTIME checkbox is selected Traceback: %s " %traceback.format_exc())

    def assert_bandwidth_limits_each_radio_checkbox(self):
        '''
        Asserting whether the EachRadio checkbox is disabled
        '''
        logger.debug('Network page :BasicInfoPage:Checking EACHRADIO checkbox disabled')
        if self.each_radio_check_box.is_selected() : 
            raise AssertionError("EACHRADIO checkbox is selected Traceback: %s " %traceback.format_exc())

    def click_airtime_checkbox(self):
        '''
        Clicking Airtime checkbox
        '''
        logger.debug('Network page :BasicInfoPage:Clicking Airtime checkbox')
        if self.airtime_check_box:
            self.airtime_check_box.click()
            time.sleep(2)

    def click_each_radio_checkbox(self):
        '''
        Clicking EachRadio checkbox
        '''
        logger.debug('Network page :BasicInfoPage:Clicking EachRadio checkbox')
        if self.each_radio_check_box:
            self.each_radio_check_box.click()
            time.sleep(2)

    def assert_airtime_textbox_empty(self):
        '''
        Asserting Airtime textbox
        '''
        logger.debug('Network page :BasicInfoPage:Asserting Airtime empty textkbox')
        if not self.airtime.get() == '' :
            raise AssertionError("Airtime textbox is not empty Traceback: %s " %traceback.format_exc())

    def assert_each_radio_textbox_empty(self):
        '''
        Asserting EachRadio textbox
        '''
        logger.debug('Network page :BasicInfoPage:Asserting EachRadio empty textkbox')
        if not self.each_radio.get() == '' :
            raise AssertionError("EachRadio textbox is not empty Traceback: %s " %traceback.format_exc())
            
    def assert_transmit_rates_dropdown_default_values(self,ghz24_min=False,ghz24_max=False,ghz5_min=False,ghz5_max=False):
        conf = self.config.config_vars
        if ghz24_min :
            self.browser.assert_drop_down_value(self.band_24ghzmin,conf.band_24ghzmin_default,'2.4GHz min default value is not set to 1')
        if ghz24_max :
            self.browser.assert_drop_down_value(self.band_24ghzmax,conf.band_24ghzmax_default,'2.4GHz max default value is not set to 54')
        if ghz5_min :
            self.browser.assert_drop_down_value(self.band_5ghzmin,conf.band_5ghzmin_default,'5 GHz default min value is not set to 6')
        if ghz5_max :
            self.browser.assert_drop_down_value(self.band_5ghzmax,conf.band_24ghzmax_default,'5 GHz default max value is not set to 54')
            
            
    def assert_dtiminterval_dropdown_options(self,option_list):
        logger.debug('BasicInfoPage : Checking for dtiminterval dropdown options')
        options = self.dtiminterval.get_options()
        if not (options == option_list):
            raise AssertionError(" Options are missing . Traceback: %s " %traceback.format_exc())
            
    def set_24ghz_band(self):
        self.buy_time()
        logger.debug("BasicInfoPage : Set band to 2.4 GHZ ")
        self.band.set(self.config.config_vars.band_24ghz)
            
    def voice_network_dmo_channel_utilization_and_multicast_transmission(self,network=None,channel=None,value=None):
        if network == 'Employee':
            self.employee_network_info_with_advanced_settings()
        if network == 'Voice':
            self.voice_network_info_with_advanced_settings()
        logger.debug("BasicInfoPage: Setting the value of DMO channel Utilization")
        if channel:
            self.dmo_channel_utilization_threshold.set(channel)
        if value == 'Enabled':
            self.multicastratetransmission.set(self.config.config_vars.basic_enabled)
        else:
            self.multicastratetransmission.set(self.config.config_vars.basic_disabled)
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def setting_airtime_value(self,airtime=None,value=None):    
        logger.debug("EditNetworkPage: Setting the value of Airtime field")
        if airtime == 'Enable':
            if not self.airtime_check_box.is_selected():
                self.airtime_check_box.click()
                logger.debug("EditNetworkPage: Setting Air time value")
                self.airtime.set(value)
        else:
            if self.airtime_check_box.is_selected():
                self.airtime_check_box.click()
        
    def setting_each_radio_value(self,radio=None,value=None):   
        logger.debug("EditNetworkPage: Setting the value of Each Radio field")
        if radio == 'Enable':
            if not self.each_radio_check_box.is_selected():
                self.each_radio_check_box.click()
                logger.debug("EditNetworkPage: Setting Air time value")
                self.each_radio.set(value)
        else:
            if self.each_radio_check_box.is_selected():
                self.each_radio_check_box.click()
    
    def voice_network_dmo_channel_dynamic_optimization_radio_airtime(self,value=None,channel=None):
        if value == 'Employee':
            self.employee_network_info_with_advanced_settings()
        if value == 'Voice':
            self.voice_network_info_with_advanced_settings()
        logger.debug("BasicInfoPage: Setting the value of DMO channel Utilization")
        if channel:
            self.dmo_channel_utilization_threshold.set(channel)
        self.set_dynamic_multicast_optimization(self.config.config_vars.dynamicmulticast_value)
        self.setting_airtime_value('Enable',self.config.config_vars.edit_localprobe)
        #self.setting_each_radio_value('Enable',self.config.config_vars.value_65535)
        self.buy_time()
        logger.debug('Basic Info Page : Clicking on Next')  
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def assert_broadcasefiltering_dropdown_values(self):
        logger.debug('BasicInfoPage : Getting all options from Broadcast Filtering')
        options = self.broadcasefiltering.get_options()
        if not options[2] == self.config.config_vars.broadcasefiltering_all:
            raise AssertionError("Broadcast Filtering ALL element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[1] == self.config.config_vars.broadcasefiltering_arp:
            raise AssertionError("Broadcast Filtering ARP element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[0] == self.config.config_vars.basic_disabled:
            raise AssertionError("Broadcast Filtering Disabled element not matched i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_multicastratetransmission_dropdown_values(self):
        logger.debug('BasicInfoPage : Getting all options from multicast transmission optimization')
        options = self.multicastratetransmission.get_options()
        if not options[1] == self.config.config_vars.basic_enabled:
            raise AssertionError("multicast transmission optimization Enabled element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[0] == self.config.config_vars.basic_disabled:
            raise AssertionError("multicast transmission optimization Disabled element not matched i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_dynamicmulticast_dropdown_values(self):
        logger.debug('BasicInfoPage : Getting all options from dynamic multicast optimization')
        options = self.dynamicmulticast.get_options()
        if not options[1] == self.config.config_vars.basic_enabled:
            raise AssertionError("Dynamic multicast optimization Enabled element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[0] == self.config.config_vars.basic_disabled:
            raise AssertionError("Dynamic multicast optimization Disabled element not matched i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_content_filtering_dropdown(self):
        logger.debug('BasicInfoPage : Getting all options from content filtering')
        options = self.content_filtering_dropdown.get_options()
        if not options[1] == self.config.config_vars.basic_enabled:
            raise AssertionError("content filtering Enabled element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[0] == self.config.config_vars.basic_disabled:
            raise AssertionError("content filtering Disabled element not matched i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_band_dropdown(self):
        logger.debug('BasicInfoPage : Getting all options from Band')
        options = self.band.get_options()
        if not options[2] == self.config.config_vars.band:
            raise AssertionError("Band 5 Ghz element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[1] == self.config.config_vars.band24:
            raise AssertionError("Band 2.4 Ghz element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[0] == self.config.config_vars.band_default:
            raise AssertionError("Band All element not matched i.e. Traceback: %s" %traceback.format_exc())
            
            
    def assert_dropdown_default_values(self,broadcasefiltering=False,dtiminterval=False,multicastratetransmission=False,dynamicmulticast=False,content_filtering=False,band=False):
        conf = self.config.config_vars
        logger.debug("BasicInfoPage: Asserting BROADCAST FILTERING default value")
        if broadcasefiltering :
            self.browser.assert_drop_down_value(self.broadcasefiltering,conf.basic_disabled,'BROADCAST FILTERING is not set to Disabled')
        logger.debug("BasicInfoPage: Asserting DTIMINTERVAL  default value")
        if dtiminterval :
            self.browser.assert_drop_down_value(self.dtiminterval,conf.dtiminterval_1_beacon,'DTIMINTERVAL is not set to 1 beacon')
        logger.debug("BasicInfoPage: Asserting MULTICASTRATETRANSMISSION default value")
        if multicastratetransmission :
            self.browser.assert_drop_down_value(self.multicastratetransmission,conf.basic_disabled,'MULTICASTRATETRANSMISSION is not set to Disabled')
        logger.debug("BasicInfoPage: Asserting DYNAMICMULTI default value")
        if dynamicmulticast :
            self.browser.assert_drop_down_value(self.dynamicmulticast,conf.basic_disabled,'DYNAMICMULTI CAST is not set to Disabled')
        logger.debug("BasicInfoPage: Asserting CONTENT FILTERING default value")
        if content_filtering :
            self.browser.assert_drop_down_value(self.content_filtering_dropdown,conf.basic_disabled,'CONTENT FILTERING is not set to Disabled')
        logger.debug("BasicInfoPage: Asserting Band default value")
        if band :
            self.browser.assert_drop_down_value(self.band,conf.band_default,'Band is not set to All')
        
            
    def assert_local_probe_request_threshold(self):
        logger.debug("BasicInfoPage: Asserting Local Probe Request Threshold default value")
        if not self.local_probe_req_textbox.get() == self.config.config_vars.local_probe_default:
            raise AssertionError("BasicInfoPage: Local Probe Request Threshold not set to default")

    def assert_max_client_threshold(self):
        logger.debug("BasicInfoPage: Asserting Max Client Threshold default value")
        if not self.max_client_threshold.get() == self.config.config_vars.max_client_default:
            raise AssertionError("BasicInfoPage: Max Client Threshold not set to default")

    def assert_can_be_used_without_uplink(self):
        logger.debug("BasicInfoPage: Asserting Can Be Used Without Uplink default value")
        if self.without_uplink.is_selected():
            raise AssertionError("BasicInfoPage: Can Be Used Without Uplink is enable")

    def assert_disable_ssid(self):
        logger.debug("BasicInfoPage: Asserting Disable SSID default value")
        if self.disable_ssid.is_selected():
            raise AssertionError("BasicInfoPage: Disable SSID is enable")

    def assert_hide_ssid(self):
        logger.debug("BasicInfoPage: Asserting HIDE SSID default value")
        if self.hide_ssid_checkbox.is_selected():
            raise AssertionError("BasicInfoPage: HIDE SSID is enable")

    def assert_inactivity_timeout(self):
        logger.debug("BasicInfoPage: Asserting Inactivity Timeout value")
        if not self.inactivity_timeout.get() == self.config.config_vars.inactivity_timeout_default:
            raise AssertionError("BasicInfoPage: Inactivity Timeout not set to default")

    def assert_dmo_channel_utilization_threshold(self):
        logger.debug("BasicInfoPage: Asserting DMO Channel Utilization Threshold value")
        if not self.dmo_channel_utilization_threshold.get() == self.config.config_vars.background_wmm:
            raise AssertionError("BasicInfoPage: DMO Channel Utilization Threshold not set to default")

    def assert_wmm_share_value(self):
        '''
        assert background wmm share
        assert best effort wmm share
        assert video wmm share
        assert voice wmm share
        '''
        conf = self.config.config_vars
        logger.debug('BasicInfoPage:Asserting background wmm value')
        self.browser.assert_text(self.background_wmm,conf.invalid_airtime,'background wmm value not set to default','value')
        logger.debug('BasicInfoPage:Asserting best effort wmm value')
        self.browser.assert_text(self.besteffort_wmm_share,conf.invalid_airtime,'best effort wmm value not set to default','value')
        logger.debug('BasicInfoPage:Asserting video wmm value')
        self.browser.assert_text(self.video_wmm_share,conf.invalid_airtime,'video wmm value not set to default','value')
        logger.debug('BasicInfoPage:Asserting voice wmm value')
        self.browser.assert_text(self.voice_wmm_share,conf.invalid_airtime,'voice wmm value not set to default','value')
        
    def assert_2_Ghz_dropdown_options(self,min_max):
        '''
        Asserting 2.4Ghz dropdown options
        '''
        logger.debug('BasicInfoPage:Checking for 2.4Ghz min or max dropdown options')
        list = [1, 2, 5, 11, 6, 9, 12, 18, 24, 36, 48, 54]
        if min_max == 'min':
            options1 = self.band_24ghzmin.get_options()
            options = [int(str(x)) for x in options1]
            for x in range(0,11):
                if not options[x] == list[x]:
                    raise AssertionError("2.4 Ghz options are missing : %s " %traceback.format_exc())

        elif min_max == 'max':
            options1 = self.band_24ghzmax.get_options()
            options = [int(str(x)) for x in options1]
            for x in range(0,11):
                if not options[x] == list[x]:
                    raise AssertionError("2.4 Ghz options are missing : %s " %traceback.format_exc())

    def assert_5_Ghz_dropdown_options(self,min_max):
        '''
        Asserting 5Ghz dropdown options
        '''
        logger.debug('BasicInfoPage:Checking for 2.4Ghz min or max dropdown options')
        list = [6,9,12,18,24,36,48,54]
        if min_max == 'min':
            options1 = self.band_5ghzmin.get_options()
            options = [int(str(x)) for x in options1]
            for x in range(0,7):
                if not options[x] == list[x]:
                    raise AssertionError("5 Ghz options are missing : %s " %traceback.format_exc())

        elif min_max == 'max':
            options1 = self.band_5ghzmax.get_options()
            options = [int(str(x)) for x in options1]
            for x in range(0,7):
                if not options[x] == list[x]:
                    raise AssertionError("5 Ghz options are missing : %s " %traceback.format_exc())

    def assert_bandwidth_limits_airtime_checkbox(self):
        '''
        Asserting whether the airtime checkbox is disabled
        '''
        logger.debug('BasicInfoPage:Checking AIRTIME checkbox disabled')
        if self.airtime_check_box.is_selected() : 
            raise AssertionError("AIRTIME checkbox is selected Traceback: %s " %traceback.format_exc())

    def assert_bandwidth_limits_each_radio_checkbox(self):
        '''
        Asserting whether the EachRadio checkbox is disabled
        '''
        logger.debug('BasicInfoPage:Checking EACHRADIO checkbox disabled')
        if self.each_radio_check_box.is_selected() : 
            raise AssertionError("EACHRADIO checkbox is selected Traceback: %s " %traceback.format_exc())

    def click_airtime_checkbox(self):
        '''
        Clicking Airtime checkbox
        '''
        logger.debug('BasicInfoPage:Clicking Airtime checkbox')
        if self.airtime_check_box:
            self.airtime_check_box.click()
            time.sleep(2)

    def click_each_radio_checkbox(self):
        '''
        Clicking EachRadio checkbox
        '''
        logger.debug('BasicInfoPage:Clicking EachRadio checkbox')
        if self.each_radio_check_box:
            self.each_radio_check_box.click()
            time.sleep(2)

    def assert_airtime_textbox_empty(self):
        '''
        Asserting Airtime textbox
        '''
        logger.debug('BasicInfoPage:Asserting Airtime empty textkbox')
        if not self.airtime.get() == '' :
            raise AssertionError("Airtime textbox is not empty Traceback: %s " %traceback.format_exc())

    def assert_each_radio_textbox_empty(self):
        '''
        Asserting EachRadio textbox
        '''
        logger.debug('BasicInfoPage:Asserting EachRadio empty textkbox')
        if not self.each_radio.get() == '' :
            raise AssertionError("EachRadio textbox is not empty Traceback: %s " %traceback.format_exc())
            
    def assert_transmit_rates_dropdown_default_values(self,ghz24_min=False,ghz24_max=False,ghz5_min=False,ghz5_max=False):
        conf = self.config.config_vars
        logger.debug('BasicInfoPage:Asserting 2.4GHz min default value')
        if ghz24_min :
            self.browser.assert_drop_down_value(self.band_24ghzmin,conf.band_24ghzmin_default,'2.4GHz min default value is not set to 1')
        logger.debug('BasicInfoPage:Asserting 2.4GHz max default value')
        if ghz24_max :
            self.browser.assert_drop_down_value(self.band_24ghzmax,conf.band_24ghzmax_default,'2.4GHz max default value is not set to 54')
        logger.debug('BasicInfoPage:Asserting 5 GHz min default value')
        if ghz5_min :
            self.browser.assert_drop_down_value(self.band_5ghzmin,conf.band_5ghzmin_default,'5 GHz default min value is not set to 6')
        logger.debug('BasicInfoPage:Asserting 5 GHz max default value')
        if ghz5_max :
            self.browser.assert_drop_down_value(self.band_5ghzmax,conf.band_24ghzmax_default,'5 GHz default max value is not set to 54')
            
            
    def assert_dtiminterval_dropdown_options(self):
        import traceback
        logger.debug('BasicInfoPage:Checking for DTIM options')
        list = ['1 beacon','2 beacons','3 beacons','4 beacons','5 beacons','6 beacons','7 beacons','8 beacons','9 beacons','10 beacons']
        options1 = self.dtiminterval.get_options()
        # print options1
        # options = [int(str(x)) for x in options1]
        for x in range(0,9):
            if not options1[x] == list[x]:
                raise AssertionError("DTIM interval options are missing : %s " %traceback.format_exc()) 

    def set_miscellaneous_band(self,value):
        self.buy_time()
        logger.debug("BasicInfoPage : Set band to 5 GHZ ")
        self.band.set(value)
                
                
    def create_wired_guest_network_1948(self):
        '''
        Creates Wired Guest Network
        '''
        logger.debug('BasicInfoPage: Clicking on wired radio button')
        self._click_on_wired()
        logger.debug('BasicInfoPage: Writing network name-Test1949')
        self.networkname.set(self.config.config_vars.new_test_1948)
        logger.debug('BasicInfoPage: Clicking on guest radio button')
        self.wired_network_guest.click()
        logger.debug('BasicInfoPage: Setting speed 100 and duplex: Half')
        self.set_speed_duplex(self.config.config_vars.basic_speed, self.config.config_vars.basic_duplex)
        
    def assert_wired_guest_network_1948(self):
        '''
        Name : Test1948
        Primary Usage : Guest
        Speed/Duplex : 100/half
        POE : Enabled
        Admin Status : UP
        Content Filtering :disabled
        Uplink : disabled
        Spanning Tree : disabled
        ''' 
        conf = self.config.config_vars
        logger.debug('BasicInfoPage: Checking the default value of text-box "Name"')
        self.browser.assert_text(self.networkname, conf.new_test_1948,'"Name" not set to "Test1948"','value')   
        logger.debug('Network : Basic Info Page : Checking Primary Usage Guest')        
        if not self.wired_network_guest.is_selected():
            raise AssertionError("Primary Usage is not selected as Guest: %s " %traceback.format_exc())     
        logger.debug('BasicInfoPage: Checking speed 100 and duplex: Half')
        self.browser.assert_drop_down_value(self.speed,conf.basic_speed,'Speed is not set to 100')      
        self.browser.assert_drop_down_value(self.duplex,conf.basic_duplex,'Speed  is not set to Half')      
        logger.debug("BasicInfoPage: Asserting POE default value")
        self.browser.assert_drop_down_value(self.Wired_POE,conf.poe_enabled,' POE is not set to Enabled')       
        logger.debug("BasicInfoPage: Asserting Admin Status default value")
        self.browser.assert_drop_down_value(self.admin_status,conf.admin_status_up,' Admin Status  is not set to UP')   
        logger.debug("BasicInfoPage: Asserting Content Filtering default value")
        self.browser.assert_drop_down_value(self.filtering,conf.content_filtering_default,'Content Filtering is not set Disabled')      
        logger.debug("BasicInfoPage: Asserting Uplink default value")
        self.browser.assert_drop_down_value(self.Wired_Uplink,conf.uplink_disabled,'Uplink is not set Disabled')        
        logger.debug("BasicInfoPage: Asserting Spanning Tree default value")
        self.browser.assert_drop_down_value(self.spanning_tree,conf.basic_disabled,'Spanning Tree is not set Disabled')
        
    def create_wired_guest_network_assert_defaults(self):
        '''
        Creates new wired 'GUEST' network and asserts defaults values of basicInfo page.
        '''
        self._click_on_wired()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Checking for empty name error message')
        self.assert_network_name_error()
        self.buy_time()
        self.assert_network_name_max_error()
        logger.debug('Network : Basic Info Page : Clicking on guest radio button')
        self.wired_network_guest.click()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Writing network name')
        self.networkname.set(self.config.config_vars.wired_network_name)
        self.assert_wired_configuration_defaults_guest_network()        
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def assert_network_name_max_error(self):
        '''
        Asserts Maximum characters error message for network name.
        '''
        logger.debug("Network : Basic Info Page : Writing network name")
        self.networkname.set(self.config.config_vars.ntwrk_name_max)
        logger.debug("Network : Basic Info Page :Clicking on 'next' button")
        self.next.click()
        logger.debug("Network : Basic Info Page :Checking for maximum character error message")
        self.buy_time()
        if not self.max_length_error_msg:
            raise AssertionError("'* Maximum 32 character allowed' error message not displayed. Traceback: %s " %traceback.format_exc())
            
    def assert_wired_configuration_defaults_guest_network(self,):
        import traceback
        if not self.wired_network_guest.is_selected():
            raise AssertionError("'PRIMARY USAGE' radio button is not set to 'Employee': %s " %traceback.format_exc())
        if not self.speed.selected=='Auto':
            raise AssertionError("Speed is not Auto by default .Traceback: %s " %traceback.format_exc())
        if not self.duplex.selected=='Auto':
            raise AssertionError("duplex is not Auto by default .Traceback: %s " %traceback.format_exc())   
        if not self.Wired_POE.selected=='Enabled':
            raise AssertionError("POE not enabled by default by default .Traceback: %s " %traceback.format_exc())
        if not self.admin_status.selected=='Up':
            raise AssertionError("Admin status not Up by default .Traceback: %s " %traceback.format_exc())
        if not self.filtering.selected=='Disabled':
            raise AssertionError("Content filtering not Disabled Up by default .Traceback: %s " %traceback.format_exc())
        if not self.Wired_Uplink.selected=='Disabled':
            raise AssertionError("Wired up link not Disabled Up by default .Traceback: %s " %traceback.format_exc())
        if not self.spanning_tree.selected=='Disabled':
            raise AssertionError("Spanning tree not Disabled Up by default .Traceback: %s " %traceback.format_exc())
            
    def assert_basic_info_page_all_fields_and_default_values(self):
        '''
        Asserts all fields of 'BASIC INFO' page.
        Asserts defaults value set to all fields.
        '''
        logger.debug("Basic Info Page :Checking for 'Type' text.")
        if not self.basic_info_text_label:
            raise AssertionError("BasicInfo Page : 'TEXT' label not found .Traceback: %s " %traceback.format_exc())
        
        logger.debug("Basic Info Page :Checking for 'NAME(SSID)' text.")
        if not self.basic_info_name_label:
            raise AssertionError("BasicInfo Page : 'NAME(SSID)' label not found .Traceback: %s " %traceback.format_exc())
        
        logger.debug("Basic Info Page :Checking for 'PRIMARY USAGE' text.")
        if not self.basic_info_primary_usage_label:
            raise AssertionError("BasicInfo Page : 'PRIMARY USAGE' label not found .Traceback: %s " %traceback.format_exc())
    
        logger.debug("Basic Info Page :Checking for 'Wireless' radio button.")
        if not self.wireless:
            raise AssertionError("BasicInfo Page : 'Wireless' radio button not found .Traceback: %s " %traceback.format_exc())
        
        logger.debug("Basic Info Page :Checking for 'Wired' radio button.")
        if not self.wired:
            raise AssertionError("BasicInfo Page : 'Wired' radio button not found .Traceback: %s " %traceback.format_exc())
        
        logger.debug("Basic Info Page :Checking for 'NAME' text box.")
        if not self.networkname:
            raise AssertionError("BasicInfo Page : 'NAME' text box not found .Traceback: %s " %traceback.format_exc())
            
        logger.debug("Basic Info Page :Checking for 'Employee' radio button.")
        if not self.employee:
            raise AssertionError("BasicInfo Page : 'Employee' radio button not found .Traceback: %s " %traceback.format_exc())
            
        logger.debug("Basic Info Page :Checking for 'Voice' radio button.")
        if not self.voice:
            raise AssertionError("BasicInfo Page : 'Voice' radio button not found .Traceback: %s " %traceback.format_exc())
            
        logger.debug("Basic Info Page :Checking for 'Guest' radio button.")
        if not self.wired_network_guest:
            raise AssertionError("BasicInfo Page : 'Guest' radio button text box not found .Traceback: %s " %traceback.format_exc())
            
        logger.debug("Basic Info Page :Checking for 'SHOW ADVANCED SETTINGS' link.")
        if not self.show_advanced_options:
            raise AssertionError("BasicInfo Page : 'SHOW ADVANCED SETTINGS' link not found .Traceback: %s " %traceback.format_exc())
            
        logger.debug("Basic Info Page :Checking for 'Wireless' radio button selected.")
        if not self.wireless.is_selected():
            raise AssertionError("BasicInfo Page : 'Wireless' radio button not selected .Traceback: %s " %traceback.format_exc())
            
        logger.debug("Basic Info Page :Checking for 'Name' empty textbox.")
        if not self.networkname.get() == '':
            raise AssertionError("BasicInfo Page : 'Name' textbox is not empty .Traceback: %s " %traceback.format_exc())
        
        logger.debug("Basic Info Page :Checking for 'Employee' radio button selected.")
        if not self.employee.is_selected():
            raise AssertionError("BasicInfo Page : 'Employee' radio button not selected .Traceback: %s " %traceback.format_exc())
            
    def create_new_network(self,type,networkname,primary_usage):
        logger.debug('Network : Basic Info Page : Clicking on wireless')
        type.click()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        self.buy_time()
        self.assert_network_name_error()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Writing network name')
        self.networkname.set(networkname)
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on employee radio button')
        primary_usage.click()
        self.buy_time()
        logger.debug('Network : Basic Info Page : Clicking on next button')
        self.next.click()
        import time
        time.sleep(5)
        return VirtualLanPage(self.test, self.browser, self.config)
        
    def check_spanning_multversion_text_availablility(self):
        time.sleep(10)
        self.browser.key_press(u'\ue009')
        self.browser.key_press( u'\ue00f')
        actions = self.browser.get_action_chain()
        actions.move_to_element(self.spanning_text_msg).perform()
        time.sleep(20)
        if not self.spanning_text_msg:
            raise AssertionError(" 'Supported in 6.3.1.2-4.0.0 and above' message is not visible i.e. Traceback: %s" %traceback.format_exc())
        
    