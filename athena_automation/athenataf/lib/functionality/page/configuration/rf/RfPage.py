from athenataf.lib.util.WebPage import WebPage
from Device_Module.ObjectModule import Device
import logging
logger = logging.getLogger('athenatef')
import time
import traceback

class RfPage(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "Rf", test, browser, config)
        self.test.assertPageLoaded(self)
        
    def isPageLoaded(self):
        if self.page_header:
            return True
        else:
            return False 
            
    def _buy_time(self):
        time.sleep(20)
            
    def _let_page_load(self):
        for i in range(2):
            time.sleep(4)
            logger.debug('RfPage : Clicking radio accodion')
            self.radio_section.click()
            time.sleep(4)
            logger.debug('RfPage : Clicking arm accodion')
            self.arm_section.click()
            self._buy_time()
            
    def _let_page_load1(self):
        # for i in range(2):
        time.sleep(4)
        logger.debug('RfPage : Clicking radio accodion')
        self.radio_section.click()
        time.sleep(4)
        logger.debug('RfPage : Clicking arm accodion')
        self.arm_section.click()
        time.sleep(4)
        logger.debug('RfPage : Clicking radio accodion')
        self.radio_section.click()
        time.sleep(8)
            
    def assert_values(self):
        try:
            self._let_page_load()
            logger.debug('RfPage : Asserting band steering mode default values')    
            if not self.band_steering_mode.get_selected() == self.config.config_vars.band_steering_mode_value:
                raise Exception("Value of 'Band Steering Mode' is not set to default")
                
            logger.debug('RfPage : Asserting airtime fairness mode default values')    
            if not self.airtime_fairness_mode.get_selected() == self.config.config_vars.airtime_fairness_mode_value:
                raise Exception("Value of 'Airtime Fairness Mode' is not set to default")
            
            logger.debug('RfPage : Asserting client match default values')                
            if not self.client_match.get_selected() == self.config.config_vars.client_match_value:
                raise Exception("Value of 'Client Match' is not set to default")
                
            logger.debug('RfPage : Asserting slb mode default values')        
            if not self.slb_mode.get_selected() == self.config.config_vars.slb_mode_value:
                raise Exception("Value of 'SLB Mode' is not set to default")
            
            logger.debug('RfPage : Asserting min transmit_power default values')    
            if not self.min_transmit_power.get_selected() == self.config.config_vars.min_transmit_power_value:
                raise Exception("Value of 'Min Transmit Power' is not set to default")
                
            logger.debug('RfPage : Asserting max_transmit power default values')        
            if not self.max_transmit_power.get_selected() == self.config.config_vars.max_transmit_power_value:
                raise Exception("Value of 'Max Transmit Mode' is not set to default")
                
            logger.debug('RfPage : Asserting client aware default values')        
            if not self.client_aware.get_selected() == self.config.config_vars.client_aware_value:
                raise Exception("Value of 'Client Aware' is not set to default")
                
            logger.debug('RfPage : Asserting scanning default values')        
            if not self.scanning.get_selected() == self.config.config_vars.scanning_value:
                raise Exception("Value of 'Scanning' is not set to default")
                
            logger.debug('RfPage : Asserting wide channel bands default values')        
            if not self.wide_channel_bands.get_selected() == self.config.config_vars.wide_channel_bands_value:
                raise Exception("Value of 'Wide Channel Bands' is not set to default")
            
            logger.debug('RfPage : Asserting mhz support default values')    
            if not self.mhz_support.get_selected() == self.config.config_vars.mhz_support_value:
                raise Exception("Value of '80 MHz Support' is not set to default")
            
            logger.debug('RfPage : Asserting customize valid channel default values')
            if self.customize_valid_channels.is_selected():
                raise Exception("Customize valid channel' is not set to default")
            
            
        except Exception as e:
            
            raise AssertionError("Asserted value not matched. Traceback: %s" % traceback.format_exc())
            
    def set_client_control_values(self):
        self._let_page_load()
        logger.debug('RfPage : Setting band steering mode values')
        self.band_steering_mode.set(self.config.config_vars.new_band_steering_mode_value)
        logger.debug('RfPage : Setting airtime fairness mode values')
        self.airtime_fairness_mode.set(self.config.config_vars.new_airtime_fairness_mode_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
        
    def assert_client_control_values(self):
        try:
            logger.debug('RfPage : Asserting band steering mode  new values')
            if not self.band_steering_mode.get_selected() == self.config.config_vars.new_band_steering_mode_value:
                raise Exception("Value of 'Band Steering Mode' is not set to new value")
                
            logger.debug('RfPage : Assering airtime fairness mode new values')    
            if not self.airtime_fairness_mode.get_selected() == self.config.config_vars.new_airtime_fairness_mode_value:
                raise Exception("Value of 'Airtime Fairness Mode' is not set to new value")
        except Exception as e:
            
            raise AssertionError("Asserted value not matched. Traceback: %s" % traceback.format_exc())
            
            
    def set_client_control_values_to_default(self):
        logger.debug('RfPage : Setting band steering mode to default values')
        self.band_steering_mode.set(self.config.config_vars.band_steering_mode_value)
        logger.debug('RfPage : Setting airtime fairness mode to default values')
        self.airtime_fairness_mode.set(self.config.config_vars.airtime_fairness_mode_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
            
    def set_access_point_control_values(self):
        self._let_page_load()
        logger.debug('RfPage : Setting min transmit power values')
        self.min_transmit_power.set(self.config.config_vars.new_min_transmit_power_value)
        logger.debug('RfPage : Setting max transmit power values')
        self.max_transmit_power.set(self.config.config_vars.new_max_transmit_power_value)
        logger.debug('RfPage : Setting client aware values')
        self.client_aware.set(self.config.config_vars.new_client_aware_value)
        logger.debug('RfPage : Setting scanning values')
        self.scanning.set(self.config.config_vars.new_scanning_value)
        logger.debug('RfPage : Setting wide channel bands values')
        self.wide_channel_bands.set(self.config.config_vars.new_wide_channel_bands_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
            
    def assert_access_point_control_values(self):
        try:
            logger.debug('RfPage : Asserting min transmit power  new values')
            if not self.min_transmit_power.get_selected() == self.config.config_vars.new_min_transmit_power_value:
                raise Exception("Value of 'Min Transmit Power' is not set to new value")
            
            logger.debug('RfPage : Asserting max transmit power new values')
            if not self.max_transmit_power.get_selected() == self.config.config_vars.new_max_transmit_power_value:
                raise Exception("Value of 'Max Transmit Power' is not set to new value")
                
            logger.debug('RfPage : Asserting client aware new values')    
            if not self.client_aware.get_selected() == self.config.config_vars.new_client_aware_value:
                raise Exception("Value of 'Client Aware' is not set to new value")
                
            logger.debug('RfPage : Asserting scanning  new values')    
            if not self.scanning.get_selected() == self.config.config_vars.new_scanning_value:
                raise Exception("Value of 'Scanning' is not set to new value")
                
            logger.debug('RfPage : Asserting wide channel bands  new values')    
            if not self.wide_channel_bands.get_selected() == self.config.config_vars.new_wide_channel_bands_value:
                raise Exception("Value of 'Wide Channel Bands' is not set to new value")
        except Exception as e:
            
            raise AssertionError("Asserted value not matched. Traceback: %s" % traceback.format_exc())    
            
    def set_access_point_control_values_to_default(self):
        logger.debug('RfPage : Setting max transmit power to default values')
        self.max_transmit_power.set(self.config.config_vars.max_transmit_power_value)
        logger.debug('RfPage : Setting min transmit power to default values')
        self.min_transmit_power.set(self.config.config_vars.min_transmit_power_value)
        logger.debug('RfPage : Setting client aware to default values')
        self.client_aware.set(self.config.config_vars.client_aware_value)
        logger.debug('RfPage : Setting scanning to default values')
        self.scanning.set(self.config.config_vars.scanning_value)
        logger.debug('RfPage : Setting wide channel bands to default values')
        self.wide_channel_bands.set(self.config.config_vars.wide_channel_bands_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
            
    def customize_channels(self):
        self._let_page_load()
        logger.debug('RfPage : Clicking on customize valid channels checkbox')
        self.customize_valid_channels.click()
        time.sleep(4)
        if not self.edit_24_ghz:
            self.customize_valid_channels.click()
        logger.debug('RfPage : Clicking on 2.4 GHz Edit')
        self.edit_24_ghz.click()
        logger.debug('RfPage : Clicking on values of 2.4  GHz')
        self.ghz_24_1.click()
        self.ghz_24_2.click()
        self.ghz_24_3.click()
        time.sleep(4)
        logger.debug('RfPage : Clicking on 5 GHz Edit')
        self.edit_5_ghz.click()
        logger.debug('RfPage : Clicking on values of 5  GHz')
        self.ghz_5_36.click()
        self.ghz_5_40.click()
        self.ghz_5_44.click()
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
        
    def assert_valid_channels(self):
        try:
            if not self.customize_valid_channels.is_selected():
                self.customize_valid_channels.click()
            self.edit_24_ghz.click()
            logger.debug('RFPage : Asserting whethr the following fields are enabled ')
            if not self.ghz_24_1.is_selected() and self.ghz_24_2.is_selected() and self.ghz_24_3.is_selected() :
                raise Exception("2.4 GHz channels are not customized")
            self.edit_5_ghz.click()
            logger.debug('RFPage : Asserting whethr the following fields are enabled ')
            if not self.ghz_5_36.is_selected() and self.ghz_5_40.is_selected() and self.ghz_5_44.is_selected() :
                raise Exception("5 GHz channels are not customized")
        except Exception as e:
            
            raise AssertionError("Asserted value not matched. Traceback: %s" % traceback.format_exc())
            
    def assert_radio_values_24_ghz(self):
        try:
            self._let_page_load1()
            logger.debug('RFPage : Asserting Default Value of Legacy Only')
            if not self.legacy_only_24ghz.get_selected() == self.config.config_vars.legacy_only_24ghz_value:
                raise Exception("Value of 'Legacy Only' is not set to default")
            
            logger.debug('RFPage : Asserting Default Value of 802.11d/802.11h')
            if not self.dropdown_11d_11h_24ghz.get_selected() == self.config.config_vars.dropdown_11d_11h_24ghz_value:
                raise Exception("Value of '802.11d/802.11h' is not set to default")
                
            logger.debug('RFPage : Asserting Default Value of Interface Immunity Level')    
            if not self.interface_immunity_24ghz.get_selected() == self.config.config_vars.interface_immunity_24ghz_value:
                raise Exception("Value of 'Interface Immunity Level' is not set to default")
                
            logger.debug('RFPage : Asserting Default Value of Channel Switch Announcement Count is not set to default')    
            if not self.channel_switch_announce_24ghz.get_selected() == self.config.config_vars.channel_switch_announce_24ghz_value:
                raise Exception("Value of 'Channel Switch Announcement Count' is not set to default")
                
            logger.debug('RFPage : Asserting Default Value of Background spectrum Monitoring')
            if not self.background_spectrum_24ghz.get_selected() == self.config.config_vars.background_spectrum_24ghz_value:
                raise Exception("Value of 'Background spectrum Monitoring' is not set to default")
        except Exception as e:
            
            raise AssertionError("Asserted value not matched. Traceback: %s" % traceback.format_exc())
            
    def assert_radio_values_5_ghz(self):
        try:
            self._let_page_load1()
            logger.debug('RFPage : Asserting Default Value of Legacy Only ')
            if not self.legacy_only_5ghz.get_selected() == self.config.config_vars.legacy_only_5ghz_value:
                raise Exception("Value of 'Legacy Only' is not set to default")
                
            logger.debug('RFPage : Asserting Default Value of 802.11d/802.11h')    
            if not self.dropdown_11d_11h_5ghz.get_selected() == self.config.config_vars.dropdown_11d_11h_5ghz_value:
                raise Exception("Value of '802.11d/802.11h' is not set to default")
                
            logger.debug('RFPage : Asserting Default Value of Interface Immunity Level')    
            if not self.interface_immunity_5ghz.get_selected() == self.config.config_vars.interface_immunity_5ghz_value:
                raise Exception("Value of 'Interface Immunity Level' is not set to default")
            
            logger.debug('RFPage : Asserting Default Value of Channel Switch Announcement Count')
            if not self.channel_switch_announce_5ghz.get_selected() == self.config.config_vars.channel_switch_announce_5ghz_value:
                raise Exception("Value of 'Channel Switch Announcement Count' is not set to default")
                
            logger.debug('RFPage : Asserting Default Value of Background spectrum Monitoring')    
            if not self.background_spectrum_5ghz.get_selected() == self.config.config_vars.background_spectrum_5ghz_value:
                raise Exception("Value of 'Background spectrum Monitoring' is not set to default")
        except Exception as e:
            
            raise AssertionError("Asserted value not matched. Traceback: %s" % traceback.format_exc())
            
    def set_2ghz_band_values(self):
        self._let_page_load1()
        logger.debug('RfPage : Setting Legacy Only values')
        self.legacy_only_24ghz.set(self.config.config_vars.new_legacy_only_24ghz_value)
        logger.debug('RfPage : Setting 802.11d/802.11h values')
        self.dropdown_11d_11h_24ghz.set(self.config.config_vars.new_dropdown_11d_11h_24ghz_value)
        logger.debug('RfPage : Setting Interface Immunity Level values')
        self.interface_immunity_24ghz.set(self.config.config_vars.new_interface_immunity_24ghz_value)
        logger.debug('RfPage : Setting Channel Switch Announcement Count values')
        self.channel_switch_announce_24ghz.set(self.config.config_vars.new_channel_switch_announce_24ghz_value)
        logger.debug('RfPage : Setting Background spectrum Monitoring values')
        self.background_spectrum_24ghz.set(self.config.config_vars.new_background_spectrum_24ghz_value)
        logger.debug('RfPage : Setting beacon interval values')
        self.beacon_interval_24ghz.set(self.config.config_vars.new_beacon_interval_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
        
    def assert_new_2ghz_band_values(self):
        try:
            logger.debug('RFPage : Asserting Default Value of Legacy Only')
            if not self.legacy_only_24ghz.get_selected() == self.config.config_vars.new_legacy_only_24ghz_value:
                raise Exception("Value of 'Legacy Only' is not set to new value")
                
            logger.debug('RFPage : Asserting Default Value of 802.11d/802.11d')    
            if not self.dropdown_11d_11h_24ghz.get_selected() == self.config.config_vars.new_dropdown_11d_11h_24ghz_value:
                raise Exception("Value of '802.11d/802.11d' is not set to new value")
                
            logger.debug('RFPage : Asserting Default Value of Interface Immunity Level')    
            if not self.interface_immunity_24ghz.get_selected() == self.config.config_vars.new_interface_immunity_24ghz_value:
                raise Exception("Value of 'Interface Immunity Level' is not set to new value")
            
            logger.debug('RFPage : Asserting Default Value of channel_switch_announce_24ghz')
            if not self.channel_switch_announce_24ghz.get_selected() == self.config.config_vars.new_channel_switch_announce_24ghz_value:
                raise Exception("Value of 'Channel Switch Announcement Count' is not set to new value")
                
            logger.debug('RFPage : Asserting Default Value of Background Spectrum Monitoring')    
            if not self.background_spectrum_24ghz.get_selected() == self.config.config_vars.new_background_spectrum_24ghz_value:
                raise Exception("Value of 'Background Spectrum Monitoring' is not set to new value")
        except Exception as e:
            
            raise AssertionError("Asserted value not matched. Traceback: %s" % traceback.format_exc())
            
    def set_2ghz_band_values_to_default(self):
        logger.debug('RFPage : Value of Legacy Only  is not set to default')
        self.legacy_only_24ghz.set(self.config.config_vars.legacy_only_24ghz_value)
        logger.debug('RFPage : Value of 802.11d/802.11d  is not set to default')
        self.dropdown_11d_11h_24ghz.set(self.config.config_vars.dropdown_11d_11h_24ghz_value)
        logger.debug('RFPage : Value of Interface Immunity Level  is not set to default')
        self.interface_immunity_24ghz.set(self.config.config_vars.interface_immunity_24ghz_value)
        logger.debug('RFPage : Value of channel_switch_announce_24ghz is not set to default')
        self.channel_switch_announce_24ghz.set(self.config.config_vars.channel_switch_announce_24ghz_value)
        logger.debug('RFPage : Value of Background Spectrum Monitoring  is not set to default')    
        self.background_spectrum_24ghz.set(self.config.config_vars.background_spectrum_24ghz_value)
        logger.debug('RFPage : Value of Beacon_interval  is not set to default')
        self.beacon_interval_24ghz.set(self.config.config_vars.beacon_interval_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
        
    def set_5ghz_band_values(self):
        self._let_page_load1()
        logger.debug('RFPage : Value of Legacy Only  is not set to default')
        self.legacy_only_5ghz.set(self.config.config_vars.new_legacy_only_5ghz_value)
        logger.debug('RFPage : Value of 802.11d/802.11d  is not set to default')
        self.dropdown_11d_11h_5ghz.set(self.config.config_vars.new_dropdown_11d_11h_5ghz_value)
        logger.debug('RFPage : Value of channelswitch announce  is not set to default')
        self.channel_switch_announce_5ghz.set(self.config.config_vars.new_channel_switch_announce_5ghz_value)
        logger.debug('RFPage : Value of background spectrum  is not set to default')
        self.background_spectrum_5ghz.set(self.config.config_vars.new_background_spectrum_5ghz_value)
        logger.debug('RFPage : Value of Beacon_interval  is not set to default')
        self.beacon_interval_5ghz.set(self.config.config_vars.new_beacon_interval_value)
        logger.debug('RFPage : Value of Interface Immunity Level  is not set to default')
        self.interface_immunity_5ghz.set(self.config.config_vars.new_interface_immunity_5ghz_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
        
    def assert_new_5ghz_band_values(self):
        try:
            logger.debug('RFPage : Asserting new Value of Legacy Only')
            if not self.legacy_only_5ghz.get_selected() == self.config.config_vars.new_legacy_only_5ghz_value:
                raise Exception("Value of 'Legacy Only' is not set to new value")
            
            logger.debug('RFPage : Asserting new Value of 802.11d/802.11d')
            if not self.dropdown_11d_11h_5ghz.get_selected() == self.config.config_vars.new_dropdown_11d_11h_5ghz_value:
                raise Exception("Value of '802.11d/802.11d' is not set to new value")
                
            logger.debug('RFPage : Asserting new Value of Interface Immunity Level')    
            if not self.interface_immunity_5ghz.get_selected() == self.config.config_vars.new_interface_immunity_5ghz_value:
                raise Exception("Value of 'Interface Immunity Level' is not set to new value")
                
            logger.debug('RFPage : Asserting Default Value of channel switch announce')    
            if not self.channel_switch_announce_5ghz.get_selected() == self.config.config_vars.new_channel_switch_announce_5ghz_value:
                raise Exception("Value of 'Channel Switch Announcement Count' is not set to new value")
                
            logger.debug('RFPage : Asserting Default Value of Background Spectrum Monitoring')    
            if not self.background_spectrum_5ghz.get_selected() == self.config.config_vars.new_background_spectrum_5ghz_value:
                raise Exception("Value of 'Background Spectrum Monitoring' is not set to new value")
                
        except Exception as e:
            
            raise AssertionError("Asserted value not matched. Traceback: %s" % traceback.format_exc())
        
    def set_5ghz_band_values_to_default(self):
        logger.debug('RFPage : Value of Legacy Only  is not set to default')
        self.legacy_only_5ghz.set(self.config.config_vars.legacy_only_5ghz_value)
        logger.debug('RFPage : Value of 802.11d/802.11d  is not set to default')
        self.dropdown_11d_11h_5ghz.set(self.config.config_vars.dropdown_11d_11h_5ghz_value)
        logger.debug('RFPage : Value of Interface Immunity Level  is not set to default')
        self.interface_immunity_5ghz.set(self.config.config_vars.interface_immunity_5ghz_value)
        logger.debug('RFPage : Value of channel switch announce  is not set to default')
        self.channel_switch_announce_5ghz.set(self.config.config_vars.channel_switch_announce_5ghz_value)
        logger.debug('RFPage : Value of Background Spectrum Monitoring  is not set to default')
        self.background_spectrum_5ghz.set(self.config.config_vars.background_spectrum_5ghz_value)
        logger.debug('RFPage : Value of Beacon  is not set to default')
        self.beacon_interval_5ghz.set(self.config.config_vars.beacon_interval_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
        
    def set_out_of_range_cm_values(self):
        self._let_page_load()
        logger.debug('RfPage : Setting vale of cm calculating interval')
        self.cm_calculating_interval.set(self.config.config_vars.new_cm_calculating_interval_value)
        logger.debug('RfPage : Setting vale of cm neighbour matching')
        self.cm_neighbour_matching.set(self.config.config_vars.new_cm_neighbour_matching_value)
        logger.debug('RfPage : Setting vale of cm threshold')
        self.cm_threshold.set(self.config.config_vars.new_cm_threshold_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
        
    def assert_cm_error_msg(self):
        
        logger.debug('RfPage : Asserting Error msg for cm calculating interval')
        if not self.error_message_calc_intr:
            raise AssertionError("'cm calculating interval' error message not found i.e. Traceback: %s" %traceback.format_exc())
        logger.debug('RfPage : Asserting Error msg for cm neighbour matching')
        if not self.error_mssg_neigh_match:
            raise AssertionError("'cm neighbour matching' error message not found i.e. Traceback: %s" %traceback.format_exc())
        logger.debug('RfPage : Asserting Error msg for cm threshold')
        if not self.error_mssg_threshold:
            raise AssertionError("'cm threshold' error message not found i.e. Traceback: %s" %traceback.format_exc())
        
    def set_cm_values_to_boundary(self):
        logger.debug('RfPage : Setting vale of cm interval boundry value')
        self.cm_calculating_interval.set(self.config.config_vars.cm_calculating_interval_boundry_value)
        logger.debug('RfPage : Setting vale of cm threshold neighbour matching boundry value')
        self.cm_neighbour_matching.set(self.config.config_vars.cm_neighbour_matching_boundry_value)
        logger.debug('RfPage : Setting vale of cm threshold')
        self.cm_threshold.set(self.config.config_vars.cm_threshold_boundry_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
        
    def set_cm_values_to_default(self):
        logger.debug('RfPage : Setting vale of cm interval boundry to default value')
        self.cm_calculating_interval.set(self.config.config_vars.cm_calculating_interval_value)
        logger.debug('RfPage : Setting vale of cm neighbour matching boundry to default value')
        self.cm_neighbour_matching.set(self.config.config_vars.cm_neighbour_matching_value)
        logger.debug('RfPage : Setting vale of cm interval threshold to default value')
        self.cm_threshold.set(self.config.config_vars.cm_threshold_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
        
    def assert_no_cm_error_msg(self):
        logger.debug('RfPage : Asserting cm errror messages')
        if self.error_message_calc_intr and self.error_mssg_neigh_match and self.error_mssg_threshold:
            
            raise AssertionError("error messages found while setting to boundary value i.e. Traceback: %s" %traceback.format_exc())
            
    def set_beacon_interval_outside_range(self):
        self._let_page_load1()
        logger.debug('RfPage : Setting beacon interval outside range')
        self.beacon_interval_24ghz.set(self.config.config_vars.beacon_interval_value_outside_range)
        logger.debug('RfPage : Setting beacon interval outside range')
        self.beacon_interval_5ghz.set(self.config.config_vars.beacon_interval_value_outside_range)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
        
    def assert_beacon_interval_error_msg(self):
        
        logger.debug('RfPage : Asserting beacon interval error msg')
        if not self.beacon_interval_24ghz_error:
            raise AssertionError("'Beacon Interval 2.4 GHz' error message not found i.e. Traceback: %s" %traceback.format_exc())
        if not self.beacon_interval_5ghz_error:
            raise AssertionError("'Beacon Interval 5 GHz' error message not found i.e. Traceback: %s" %traceback.format_exc())
        
    def set_beacon_interval_to_dafault(self):
        logger.debug('RfPage : Setting beacon interval')
        self.beacon_interval_24ghz.set(self.config.config_vars.beacon_interval_value)
        logger.debug('RfPage : Setting beacon interval')
        self.beacon_interval_5ghz.set(self.config.config_vars.beacon_interval_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
        
    def assert_slb_mode_value(self):
        self._let_page_load()
        logger.debug('RfPage : Asserting slb mode value')
        path = self.config.config_vars
        values_list = self.slb_mode.get_options()
        for value in values_list:
            if not (value == path.slb_mode_value or path.slb_mode_value_2nd or path.slb_mode_value_3rd):
                
                raise AssertionError("'SLB MODE' drop-down values not found i.e. Traceback: %s" %traceback.format_exc())
        
    def set_slb_mode_value(self):
        
        logger.debug('RfPage : Settng slb mode value')
        self.slb_mode.set(self.config.config_vars.slb_mode_value_2nd)
        if not self.slb_mode.get_selected() == self.config.config_vars.slb_mode_value_2nd:
            raise AssertionError("'SLB MODE' drop-down values not set to 'Radio' i.e. Traceback: %s" %traceback.format_exc())
        self.slb_mode.set(self.config.config_vars.slb_mode_value_3rd)
        if not self.slb_mode.get_selected() == self.config.config_vars.slb_mode_value_3rd:
            raise AssertionError("'SLB MODE' drop-down values not set to 'channel+Radio' i.e. Traceback: %s" %traceback.format_exc())
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
        
    def set_slb_mode_value_to_default(self):
        
        logger.debug('RfPage : Setting slb mode value')
        self.slb_mode.set(self.config.config_vars.slb_mode_value)
        if not self.slb_mode.get_selected() == self.config.config_vars.slb_mode_value:
            raise AssertionError("'SLB MODE' drop-down values not set to 'channel' i.e. Traceback: %s" %traceback.format_exc())
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
        
    def assert_client_match_parameters(self):
        self._let_page_load()
        
        logger.debug('RfPage : Asserting cm values ')
        if not self.client_match_text:
            raise AssertionError("'CLIENT MATCH' parameter not found i.e. Traceback: %s" %traceback.format_exc())
        if not self.cm_calculating_int_text:
            raise AssertionError("'CM CALCULATING INTERVAL' parameter not found i.e. Traceback: %s" %traceback.format_exc())
        if not self.cm_neighbour_matching_text:
            raise AssertionError("'CM NEIGHBOUR MATCHING' parameter not found i.e. Traceback: %s" %traceback.format_exc())
        if not self.cm_threshold_text:
            raise AssertionError("'CM THRESHOLD' parameter not found i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_80_mhz_support_field_and_default_value(self):
        self._let_page_load()
        logger.debug('RfPage : Asserting 80 mhz support field and default value ')
        
        if not self.mhz_support:
            raise AssertionError("'80 MHz Support' parameter not found i.e. Traceback: %s" %traceback.format_exc())
        if not self.mhz_support.get_selected() == self.config.config_vars.mhz_support_value:
            raise AssertionError("'80 MHz SUPPORT' value not set to default i.e. Traceback: %s" %traceback.format_exc())
            
    def set_80_mhz_support_value(self , state):
        
        logger.debug('RfPage : Enabling 80 mhz support field')
        if state == 'enable':
            self.mhz_support.set(self.config.config_vars.new_mhz_support_value)
            logger.debug('RfPage : Clicking on save settings')
            self.save_settings.click()
            self._buy_time()
            if not self.mhz_support.get_selected() == self.config.config_vars.new_mhz_support_value:
                raise AssertionError("'80 MHz SUPPORT' value not set to 'Enabled' i.e. Traceback: %s" %traceback.format_exc())
        elif state == 'disable':
            self.mhz_support.set(self.config.config_vars.mhz_support_value)
            logger.debug('RfPage : Clicking on save settings')
            self.save_settings.click()
            self._buy_time()
            if not self.mhz_support.get_selected() == self.config.config_vars.mhz_support_value:
                raise AssertionError("'80 MHz SUPPORT' value not set to 'Disabled' i.e. Traceback: %s" %traceback.format_exc())
            
    
    def assert_string_beacon_interval(self):
        
        logger.debug('RfPage : Asserting beacon values' )
        self.beacon_interval_24ghz.set(self.config.config_vars.network_value)
        if not self.beacon_interval_24ghz_error:
            raise AssertionError("Error message has not been shown' i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_beacon_error_msg(self):
        
        self._let_page_load1()
        logger.debug('RF Radio : Setting Beacon Interval 2.4 GHz to 50')
        self.beacon_interval_24ghz.set(self.config.config_vars.beacon_interval_value_outside_range)
        logger.debug('RF Radio : Setting Beacon Interval 5 GHz to 50')
        self.beacon_interval_5ghz.set(self.config.config_vars.beacon_interval_value_outside_range)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        if not self.beacon_interval_24ghz_error:
            raise AssertionError("'Beacon Interval 2.4 GHz' error message not found i.e. Traceback: %s" %traceback.format_exc())
        if not self.beacon_interval_5ghz_error:
            raise AssertionError("'Beacon Interval 5 GHz' error message not found i.e. Traceback: %s" %traceback.format_exc())
        logger.debug('RF Radio : Clicking on Cancel button')
        self.rf_cancel_button.click()
        
    def set_5ghz_band_field(self):
        logger.debug('RF Radio : Setting 5 GHz band values')
        self.legacy_only_5ghz.set(self.config.config_vars.new_legacy_only_5ghz_value)
        self.dropdown_11d_11h_5ghz.set(self.config.config_vars.new_dropdown_11d_11h_5ghz_value)
        self.channel_switch_announce_5ghz.set(self.config.config_vars.new_channel_switch_announce_5ghz_value)
        self.background_spectrum_5ghz.set(self.config.config_vars.new_background_spectrum_5ghz_value)
        self.beacon_interval_5ghz.set(self.config.config_vars.new_beacon_interval_value)
        self.interface_immunity_5ghz.set(self.config.config_vars.new_interface_immunity_5ghz_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
        
    def set_2ghz_band_field(self):
        logger.debug('RF Radio : Setting 2.4 GHz band values')
        self.legacy_only_24ghz.set(self.config.config_vars.new_legacy_only_24ghz_value)
        self.dropdown_11d_11h_24ghz.set(self.config.config_vars.new_dropdown_11d_11h_24ghz_value)
        self.interface_immunity_24ghz.set(self.config.config_vars.new_interface_immunity_24ghz_value)
        self.channel_switch_announce_24ghz.set(self.config.config_vars.new_channel_switch_announce_24ghz_value)
        self.background_spectrum_24ghz.set(self.config.config_vars.new_background_spectrum_24ghz_value)
        self.beacon_interval_24ghz.set(self.config.config_vars.new_beacon_interval_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
        
    def check_calculation_interval(self):
        
        time.sleep(7)
        logger.debug('RfPage : Setting cm calculating interval')
        self.cm_calculating_interval.set(self.config.config_vars.invalid_cm_calculating_interval_value)
        time.sleep(3)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        if not self.error_message_calc_intr:
            raise AssertionError("Invalid value error message not found i.e. Traceback: %s" %traceback.format_exc())
            
        logger.debug('RfPage : Setting cm calculating interval')
        self.cm_calculating_interval.set(self.config.config_vars.char_cm_calculating_interval_value)
        time.sleep(3)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()        
        if not self.error_message_calc_intr:
            raise AssertionError("Invalid value error message not found i.e. Traceback: %s" %traceback.format_exc())
            
        logger.debug('RfPage : Setting cm calculating interval')
        self.cm_calculating_interval.set(self.config.config_vars.cm_calculating_interval_value)
        time.sleep(3)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()

    def set_default_calculation_interval(self):
        logger.debug('RfPage : Setting cm calculating interval')
        self.cm_calculating_interval.set(self.config.config_vars.cm_calculating_interval_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        time.sleep(8)
        
    def check_neighbour_interval(self):
         
        time.sleep(8)
        logger.debug('RfPage : Setting cm neighbour matching')
        self.cm_neighbour_matching.set(self.config.config_vars.cm_neighbour_matching_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        if self.error_mssg_neigh_match:
            raise AssertionError(" Error message displayed for valid value. i.e. Traceback: %s" %traceback.format_exc())
            
        logger.debug('RfPage : Setting cm neighbour matching')
        self.cm_neighbour_matching.set(self.config.config_vars.invalid_cm_calculating_interval_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()        
        if not self.error_mssg_neigh_match:
            raise AssertionError("Invalid value set to cm neighbour i.e. Traceback: %s" %traceback.format_exc())
        
        logger.debug('RfPage : Setting cm neighbour matching')
        self.cm_neighbour_matching.set(self.config.config_vars.char_cm_calculating_interval_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()        
        if not self.error_mssg_neigh_match:
            raise AssertionError("Invalid value set to cm neighbour i.e. Traceback: %s" %traceback.format_exc())
        
    def set_default_neighbour_interval(self):
        logger.debug('RfPage : Setting default neighbouring ')
        self.cm_neighbour_matching.set(self.config.config_vars.cm_neighbour_matching_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        time.sleep(20)
        
    def set_config_to_default(self):
        time.sleep(15)
        logger.debug('RfPage : Setting  band_steering_mode_value ')
        self.band_steering_mode.set(self.config.config_vars.band_steering_mode_value)
        logger.debug('RfPage : Setting  airtime_fairness_mode_value ')
        self.airtime_fairness_mode.set(self.config.config_vars.airtime_fairness_mode_value)
        logger.debug('RfPage : Setting client_match_value ')
        self.client_match.set(self.config.config_vars.client_match_value)    
        logger.debug('RfPage : Setting  cm_calculating_interval_value ')
        self.cm_calculating_interval.set(self.config.config_vars.cm_calculating_interval_value)    
        logger.debug('RfPage : Setting  scanning_value ')
        self.scanning.set(self.config.config_vars.scanning_value)
        logger.debug('RfPage : Setting mhz_support_value ')
        self.mhz_support.set(self.config.config_vars.mhz_support_value)
        logger.debug('RfPage : Setting  cm_threshold_value ')
        self.cm_threshold.set(self.config.config_vars.cm_threshold_value)
        if self.customize_valid_channels.is_selected():
            self.customize_valid_channels.click()
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        time.sleep(20)
        
    def change_config(self):
        time.sleep(15)
        logger.debug('RfPage : Setting  band_steering_mode ')
        self.band_steering_mode.set(self.config.config_vars.new_band_steering_mode_value)
        logger.debug('RfPage : Setting  airtime_fairness_mode ')
        self.airtime_fairness_mode.set(self.config.config_vars.new_airtime_fairness_mode_value)
        logger.debug('RfPage : Setting  client_match ')
        self.client_match.set(self.config.config_vars.new_client_match_value)    
        logger.debug('RfPage : Setting  cm_calculating_interval ')
        self.cm_calculating_interval.set(self.config.config_vars.cm_calculating_interval_boundry_value)    
        logger.debug('RfPage : Setting  scanning ')
        self.scanning.set(self.config.config_vars.new_scanning_value)
        logger.debug('RfPage : Setting  mhz_support ')
        self.mhz_support.set(self.config.config_vars.enable_mhz_support_value)
        logger.debug('RfPage : Setting  cm_threshold_value ')
        self.cm_threshold.set(self.config.config_vars.cm_threshold_boundry_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        time.sleep(20)
        
    def assert_rf_values(self):
        
        logger.debug('RfPage : Asserting Default values')
        if not self.arm_client_control_span:
            raise AssertionError("Band steering is not set to prefer 5GHz i.e. Traceback: %s" %traceback.format_exc())
        if self.radio_ghz_band_span:
            raise AssertionError("Radio accordion is opened i.e. Traceback: %s" %traceback.format_exc())
        if not self.config.config_vars.Default_band_steering_mode == self.band_steering_mode.get_selected():
            raise AssertionError("Band streeting mode is not set to Prefer 5GHz i.e. Traceback: %s" %traceback.format_exc())
        if not self.config.config_vars.airtime_fairness_mode_value == self.airtime_fairness_mode.get_selected():
            raise AssertionError("Airtime fairness mode is not set to Fair Access i.e. Traceback: %s" %traceback.format_exc())
        if not self.config.config_vars.client_match_value == self.client_match.get_selected():
            raise AssertionError("Client match is not set to Disabled i.e. Traceback: %s" %traceback.format_exc())
        if not self.config.config_vars.slb_mode_value == self.slb_mode.get_selected():
            raise AssertionError("slb Mode is not set to channel i.e. Traceback: %s" %traceback.format_exc())
        if self.customize_valid_channels.is_selected():
            raise AssertionError("Customised Channel is Selected i.e. Traceback: %s" %traceback.format_exc())
        if not self.config.config_vars.min_transmit_power_value == self.min_transmit_power.get_selected():
            raise AssertionError("Min TRansmit power is not set to 18 i.e. Traceback: %s" %traceback.format_exc())
        if not self.config.config_vars.max_transmit_power_value == self.max_transmit_power.get_selected():
            raise AssertionError("Max TRansmit power is not set to Max i.e. Traceback: %s" %traceback.format_exc())
        if not self.config.config_vars.client_aware_value == self.client_aware.get_selected():
            raise AssertionError("Client aware is not set to Enabled i.e. Traceback: %s" %traceback.format_exc())
        if not self.config.config_vars.scanning_value == self.scanning.get_selected():
            raise AssertionError("Scanning value is not set to Enabled i.e. Traceback: %s" %traceback.format_exc())
        if not self.config.config_vars.wide_channel_bands_value == self.wide_channel_bands.get_selected():
            raise AssertionError("Wide channel is not set to 5Ghz i.e. Traceback: %s" %traceback.format_exc())
        if not self.config.config_vars.mhz_support_value == self.mhz_support.get_selected():
            raise AssertionError("Mhz Support Value is not set to Disabled i.e. Traceback: %s" %traceback.format_exc())
            
    def enable_disable_help_link(self):
        logger.debug('RfPage : Clicking on Help button')
        self.help_button.click()
        time.sleep(8)
        self.help_button.click()
        
    def save_alert(self):
        time.sleep(8)
        logger.debug('RfPage : Setting band steering mode value')
        self.band_steering_mode.set(self.config.config_vars.new_band_steering_mode_value)
        time.sleep(8)
        logger.debug('RfPage : Clicking access point button')
        self.access_point_button.click()
        logger.debug('RfPage : Clicking confirm save ok')
        self.confirm_save_ok.click()
        time.sleep(8)
        
    def assert_changed_setting(self):
        
        logger.debug('RfPage : Asserting whether  band steering mode value is set to new value ')
        if not self.config.config_vars.new_band_steering_mode_value == self.band_steering_mode.get_selected():
            raise AssertionError("Band streeting mode is not set to Balanced Bands i.e. Traceback: %s" %traceback.format_exc())
            
    def set_default_setting(self):
        logger.debug('RfPage : Setting band steering mode to default value')
        self.band_steering_mode.set(self.config.config_vars.band_steering_mode_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click() 
    
    def deselect_few_channels(self):
        self._let_page_load()
        logger.debug('RfPage : Deselecting customize valid channels')
        if not self.edit_24_ghz:
            logger.debug('RfPage : Deselecting customize valid channels')
            self.customize_valid_channels.click()
        logger.debug('RfPage : Clicking 2.4 ghHZ edit button')
        self.edit_24_ghz.click()
        logger.debug('RfPage : Clicking 2.4 ghHZ : 1')
        self.ghz_24_1.click()
        logger.debug('RfPage : Clicking 2.4 ghHZ : 2')
        self.ghz_24_2.click()
        logger.debug('RfPage : Clicking 2.4 ghHZ : 5')
        self.edit_5_ghz.click()
        logger.debug('RfPage : Clicking 2.4 ghHZ : 36')
        self.ghz_5_36.click()
        logger.debug('RfPage : Clicking 2.4 ghHZ : 40')
        self.ghz_5_40.click()
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
        
    def clear_channels(self):
        self._let_page_load()
        if not self.edit_24_ghz:
            logger.debug('RfPage : radio : clicking customize valid channels')
            self.customize_valid_channels.click()
        logger.debug('RfPage : Clicking edit button')
        self.edit_24_ghz.click()
        logger.debug('RfPage : Clicking 2.4 GHZ : edit : 3')
        self.ghz_24_3.click()
        logger.debug('RfPage : Clicking edit : 5ghz')
        self.edit_5_ghz.click()
        logger.debug('RfPage : Clicking 5GHZ : edit : 44')
        self.ghz_5_44.click()
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
        
    def assert_few_valid_channels(self):
        try:
            if not self.selected_few_channels_24_ghz:
                raise Exception("2.4 GHz channels are not customized")
            if not self.selected_few_channels_5_ghz:
                raise Exception("5 GHz channels are not customized")
        except Exception as e:
            
            raise AssertionError("Asserted value not matched. Traceback: %s" % traceback.format_exc())    
            
    def set_min_max_transmit_power(self):
        logger.debug('RF : Writing min transmit power')
        self.min_transmit_power.set(self.config.config_vars.change_min_transmit_power_value)
        logger.debug('RF : Writing max transmit power')
        self.max_transmit_power.set(self.config.config_vars.change_max_transmit_power_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
        
    def set_default_min_max_transmit_power(self):
        '''
        setting default min and max transmit values
        '''
        logger.debug('RF : Setting min transmit power to default')
        self.min_transmit_power.set(self.config.config_vars.min_transmit_power_value)
        logger.debug('RF : Setting max transmit power to default')
        self.max_transmit_power.set(self.config.config_vars.max_transmit_power_value)
        logger.debug('RfPage : Clicking on save settings')
        self.save_settings.click()
        self._buy_time()
        
    def click_to_customize_valid(self):
        '''
        clicks on customize valid channels
        '''
        if not self.edit_24_ghz:
            logger.debug('RfPage : radio : clicking customize valid channels')
            self.customize_valid_channels.click()
    
    def open_radio_accordion(self):
        '''
        clicks on radio accordion
        '''
        time.sleep(10)
        logger.debug('RF : Clicking radio accordion')
        self.radio_section.click()
            
    def assert_radio_default_values(self):
        '''
        asserts radio accordion default values
        '''
        logger.debug('RF Page : Asserting rf radio field for default values')
        if not self.legacy_only_24ghz.get_selected() == self.config.config_vars.legacy_only_24ghz_value:
            raise AssertionError("2.4 GHz LEGACY ONLY is not disabled i.e. Traceback: %s" %traceback.format_exc())
        if not self.legacy_only_5ghz.get_selected() == self.config.config_vars.legacy_only_24ghz_value:
            raise AssertionError("5 GHz LEGACY ONLY is not disabled i.e. Traceback: %s" %traceback.format_exc())
        if not self.dropdown_11d_11h_24ghz.get_selected() == self.config.config_vars.legacy_only_24ghz_value:
            raise AssertionError("For 2.4 GHz 802.11d / 802.11h is not disabled i.e. Traceback: %s" %traceback.format_exc())
        if not self.dropdown_11d_11h_5ghz.get_selected() == self.config.config_vars.legacy_only_24ghz_value:
            raise AssertionError("For 5 GHz 802.11d / 802.11h is not disabled i.e. Traceback: %s" %traceback.format_exc())
        if not self.interface_immunity_24ghz.get_selected() == self.config.config_vars.interface_immunity_24ghz_value:
            raise AssertionError("For 2.4 GHz INTERFACE IMMUNITY LEVEL is not set to 2 i.e. Traceback: %s" %traceback.format_exc())
        if not self.interface_immunity_5ghz.get_selected() == self.config.config_vars.interface_immunity_24ghz_value:
            raise AssertionError("For 5 GHz INTERFACE IMMUNITY LEVEL is not set to 2 i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_switch_announce_24ghz.get_selected() == self.config.config_vars.channel_switch_announce_24ghz_value:
            raise AssertionError("For 2.4 GHz CHANNEL SWITCH ANNOUNCEMENT COUNT is not set to 0 i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_switch_announce_5ghz.get_selected() == self.config.config_vars.channel_switch_announce_24ghz_value:
            raise AssertionError("For 5 GHz CHANNEL SWITCH ANNOUNCEMENT COUNT is not set to 0 i.e. Traceback: %s" %traceback.format_exc())
        if not self.background_spectrum_24ghz.get_selected() == self.config.config_vars.background_spectrum_24ghz_value:
            raise AssertionError("For 2.4 GHz BACKGROUND SPECTRUM MONITORING is not disabled i.e. Traceback: %s" %traceback.format_exc())
        if not self.background_spectrum_5ghz.get_selected() == self.config.config_vars.background_spectrum_24ghz_value:
            raise AssertionError("For 5 GHz BACKGROUND SPECTRUM MONITORING is not disabled i.e. Traceback: %s" %traceback.format_exc())
            
    def enable_help(self):
        '''
        clicks on help button
        '''
        time.sleep(8)
        logger.debug('RF : Clicking on help button')
        self.help_button.click()

    def assert_help_option(self):
        '''
        asserts help text labels
        '''
        time.sleep(8)
        action_chain = self.browser.get_action_chain()
        action_chain.move_to_element(self.band_streering_mode_help_link).perform()
        if not self.help_content:
            raise AssertionError("Help content is not opened i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(5)
        
    def assert_band_streering_options(self):
        '''
        asserts band steering options
        '''
        time.sleep(5)
        logger.debug('RfPage : Getting all options from Band Streering dropdown')
        options = self.band_steering_mode.get_options()
        if not options[0] == self.config.config_vars.band_streering_disable:
            raise AssertionError("Band streering Disable element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[1] == self.config.config_vars.band_streering_prefer_5ghz:
            raise AssertionError("Band streering Prefer 5GHz element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[2] == self.config.config_vars.band_streering_force_5ghz:
            raise AssertionError("Band streering Force 5GHz element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[3] == self.config.config_vars.band_streering_balance_band:
            raise AssertionError("Band streering Balance Bands element not matched i.e. Traceback: %s" %traceback.format_exc())
            
    def set_different_band_streering_options(self):
        '''
        sets band steering mode
        '''
        logger.debug('RfPage : Setting Band Streering dropdown to Force 5GHz')
        self.band_steering_mode.set(self.config.config_vars.band_streering_force_5ghz)
        logger.debug('RfPage : Clicking on Save button')
        self.save_button.click()
        time.sleep(15)
        logger.debug('RfPage : Setting Band Streering dropdown to Balance Band')
        self.band_steering_mode.set(self.config.config_vars.band_streering_balance_band)
        logger.debug('RfPage : Clicking on Save button')
        self.save_button.click()
        time.sleep(15)
        
    def set_band_streering_default(self):
        '''
        sets default value of band steering
        '''
        logger.debug('RfPage : Setting Band Streering dropdown to Prefer 5GHz')
        self.band_steering_mode.set(self.config.config_vars.band_streering_prefer_5ghz)
        logger.debug('RfPage : Clicking on Save button')
        self.save_button.click()
        time.sleep(15)
        
    def assert_air_fairness_mode_options(self):
        '''
        asserts air fairness mode options
        '''
        time.sleep(5)
        logger.debug('RfPage : Getting all options from Air Fairness Mode dropdown')
        options = self.airtime_fairness_mode.get_options()
        if not options[0] == self.config.config_vars.airtime_fairness_mode_default_access:
            raise AssertionError("Air Fairness Mode Disable element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[1] == self.config.config_vars.airtime_fairness_mode_fair_access:
            raise AssertionError("Air Fairness Mode Fair Access element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[2] == self.config.config_vars.airtime_fairness_mode_preferred_access:
            raise AssertionError("Air Fairness Mode Preferred Access element not matched i.e. Traceback: %s" %traceback.format_exc())
    
    def set_different_air_fairness_mode_options(self):
        '''
        sets air fairness mode to different options
        '''
        self.airtime_fairness_mode.set(self.config.config_vars.airtime_fairness_mode_default_access)
        logger.debug('RfPage : Clicking on Save button')
        self.save_button.click()
        time.sleep(15)
        logger.debug('RfPage : Setting Air Fairness Mode dropdown to Balance Preferred Access')
        self.airtime_fairness_mode.set(self.config.config_vars.airtime_fairness_mode_preferred_access)
        logger.debug('RfPage : Clicking on Save button')
        self.save_button.click()
        time.sleep(15)
        
    def set_air_fairness_mode_default(self):
        '''
        sets default value of air fairness mode
        '''
        logger.debug('RfPage : Setting Air Fairness Mode dropdown to Fair Access')
        self.airtime_fairness_mode.set(self.config.config_vars.airtime_fairness_mode_fair_access)
        logger.debug('RfPage : Clicking on Save button')
        self.save_button.click()
        
        time.sleep(15)
        
    def assert_client_match_options(self):
         
        time.sleep(5)
        logger.debug('RfPage : Getting all options from Client Match dropdown')
        options = self.client_match.get_options()
        if not options[0] == self.config.config_vars.client_match_disabled:
            raise AssertionError("Client Match Enabled element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[1] == self.config.config_vars.client_match_enabled:
            raise AssertionError("Client Match Disabled element not matched i.e. Traceback: %s" %traceback.format_exc())
        
    def set_different_client_match_options(self):
        '''
        sets client match to different options
        '''
        logger.debug('RfPage : Setting Client Match dropdown to Enabled')
        self.client_match.set(self.config.config_vars.client_match_enabled)
        logger.debug('RfPage : Clicking on Save button')
        try:
            logger.debug('RfPage : Clicking on Save button')
            self.save_button.click()
        except:
            logger.debug('Save button not present')
        
    def set_client_match_default(self):
        '''
        sets client match default values
        '''
        logger.debug('RfPage : Setting Client Match dropdown to Disabled')
        self.client_match.set(self.config.config_vars.client_match_disabled)
        logger.debug('RfPage : Clicking on Save button')
        try:
            logger.debug('RfPage : Clicking on Save button')
            self.save_button.click()
        except:
            logger.debug('Save button not present')
        time.sleep(15)
        
    def assert_cm_threshold_value(self):    
        
        logger.debug('RfPage : Entering invalid value in CM Threshold field')
        time.sleep(5)
        logger.debug('RFPage : Writing cm threshold ')
        self.cm_threshold.set(self.config.config_vars.change_min_transmit_power_value)
        logger.debug('RfPage : Clicking on Save button')
        self.save_button.click()
        if not self.error_mssg_threshold:
            raise AssertionError("CM Threshold error message is not visible i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(5)
        logger.debug('RFPage : Writing cm threshold ')
        self.cm_threshold.set(self.config.config_vars.char_cm_calculating_interval_value)
        logger.debug('RfPage : Clicking on Save button')
        self.save_button.click()
        if not self.error_mssg_threshold:
            raise AssertionError("CM Threshold error message is not visible i.e. Traceback: %s" %traceback.format_exc())
        logger.debug('RfPage : Entering valid value in CM Calculating Interval field')
        time.sleep(5)
        logger.debug('RFPage : Writing cm threshold ')
        self.cm_threshold.set(self.config.config_vars.cm_threshold_boundry_value)
        logger.debug('RfPage : Clicking on Save button')
        self.save_button.click()
        time.sleep(18)
        
    def set_cm_threshold_default_value(self):
        '''
        sets default value of cm threshold 
        '''
        logger.debug('RfPage : Entering default value in CM Threshold field')
        self.cm_threshold.set(self.config.config_vars.cm_threshold_value)
        logger.debug('RfPage : Clicking on Save button')
        self.save_button.click()
        time.sleep(15)
        
    def assert_client_aware_options(self):
         
        time.sleep(8)
        logger.debug('RfPage : Getting all options from Client Aware dropdown')
        options = self.client_aware.get_options()
        if not options[0] == self.config.config_vars.client_match_disabled:
            raise AssertionError("Client Aware Enabled element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[1] == self.config.config_vars.client_match_enabled:
            raise AssertionError("Client Aware Disabled element not matched i.e. Traceback: %s" %traceback.format_exc())
        
    
    def set_different_client_aware_options(self):
        '''
        sets client aware options
        '''
        logger.debug('RfPage : Setting Client Aware dropdown to Enabled')
        self.client_aware.set(self.config.config_vars.client_match_enabled)
        logger.debug('RfPage : Clicking on Save button')
        try:
            logger.debug('RfPage : Clicking on Save button')
            self.save_button.click()
        except:
            logger.debug('Save button not present')
        time.sleep(18)
            
    def set_client_aware_default(self):
        '''
        sets default value to client aware
        '''
        logger.debug('RfPage : Setting Client Aware dropdown to Enabled')
        self.client_aware.set(self.config.config_vars.client_match_enabled)
        logger.debug('RfPage : Clicking on Save button')
        try:
            logger.debug('RfPage : Clicking on Save button')
            self.save_button.click()
        except:
            logger.debug('Save button not present')
        time.sleep(15)
        
    def assert_scanning_options(self):
         
        time.sleep(8)
        logger.debug('RfPage : Getting all options from Scanning dropdown')
        options = self.scanning.get_options()
        if not options[0] == self.config.config_vars.client_match_disabled:
            raise AssertionError("Scanning Enabled element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[1] == self.config.config_vars.client_match_enabled:
            raise AssertionError("Scanning Disabled element not matched i.e. Traceback: %s" %traceback.format_exc())
    
    def set_different_scanning_options(self):
        logger.debug('RfPage : Setting Client Aware dropdown to Enabled')
        self.scanning.set(self.config.config_vars.client_match_enabled)
        logger.debug('RfPage : Clicking on Save button')
        try:
            logger.debug('RfPage : Clicking on Save button')
            self.save_button.click()
        except:
            logger.debug('Save button not present')
            
    def set_scanning_default(self):
        logger.debug('RfPage : Setting Client Aware dropdown to Enabled')
        self.scanning.set(self.config.config_vars.client_match_enabled)
        logger.debug('RfPage : Clicking on Save button')
        try:
            logger.debug('RfPage : Clicking on Save button')
            self.save_button.click()
        except:
            logger.debug('Save button not present')
        time.sleep(15)
        
    def assert_wide_channel_bands_options(self):
         
        time.sleep(8)
        logger.debug('RfPage : Getting all options from Wide Channel Bands dropdown')
        options = self.wide_channel_bands.get_options()
        if not options[0] == self.config.config_vars.wide_channel_bands_none:
            raise AssertionError("Wide Channel Bands None element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[1] == self.config.config_vars.wide_channel_bands_all:
            raise AssertionError("Wide Channel Bands All element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[2] == self.config.config_vars.wide_channel_bands_5ghz:
            raise AssertionError("Wide Channel Bands 5 GHz element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[3] == self.config.config_vars.wide_channel_bands_24ghz:
            raise AssertionError("Wide Channel Bands 2.4 GHz element not matched i.e. Traceback: %s" %traceback.format_exc())
    
    def set_different_wide_channel_bands_options(self):
        logger.debug('RfPage : Setting Wide Channel Bands dropdown to None')
        self.wide_channel_bands.set(self.config.config_vars.wide_channel_bands_none)
        self.save_changes()
        logger.debug('RfPage : Setting Wide Channel Bands to 5GHz')
        self.wide_channel_bands.set(self.config.config_vars.wide_channel_bands_5ghz)
        self.save_changes()
        logger.debug('RfPage : Setting Wide Channel Bands to 2.4GHz')
        self.wide_channel_bands.set(self.config.config_vars.wide_channel_bands_24ghz)
        self.save_changes()
        
    def set_wide_channel_bands_default(self):
        logger.debug('RfPage : Setting Wide Channel Bands to 5GHz')
        self.wide_channel_bands.set(self.config.config_vars.wide_channel_bands_5ghz)
        self.save_changes()
        
    def assert_80_mhz_options(self):
         
        time.sleep(8)
        logger.debug('RfPage : Getting all options from 80 GHz Support dropdown')
        options = self.mhz_support.get_options()
        if not options[0] == self.config.config_vars.client_match_disabled:
            raise AssertionError("80 GHz Support Disabled element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[1] == self.config.config_vars.client_match_enabled:
            raise AssertionError("80 GHz Support Enabled element not matched i.e. Traceback: %s" %traceback.format_exc())
        
    def set_different_80_mhz_options(self):
        logger.debug('RfPage : Setting 80 GHz Support dropdown to Enabled')
        self.mhz_support.set(self.config.config_vars.client_match_enabled)
        self.save_changes()
        
    def set_80_mhz_default(self):
        logger.debug('RfPage : Setting 80 GHz Support dropdown to Disabled')
        self.mhz_support.set(self.config.config_vars.mhz_support_value)
        self.save_changes()
    

    def save_changes(self):
         try:
            logger.debug('RfPage : Clicking on Save button')
            self.save_button.click()
         except:
            logger.debug('Save button not present')
         time.sleep(15)
        
    def check_rf_accordions(self):
        logger.debug('RF Page : Checking whether rf arm accordion is opened by default')
        time.sleep(8)
        if not self.client_control_label:
            raise AssertionError("RF Arm accordion is not opened by default i.e. Traceback: %s" %traceback.format_exc())
        if self.legacy_only_24ghz:
            raise AssertionError("RF Radio accordion is opened by default i.e. Traceback: %s" %traceback.format_exc())
                
        
    def assert_rf_options(self):
        logger.debug('RF Page : Asserting on rf field options')
        time.sleep(8)
        if not self.band_steering_mode.get_selected() == self.config.config_vars.band_steering_mode_value:
            raise AssertionError("Band Streeing Mode is not set to Prefer 5Ghz i.e. Traceback: %s" %traceback.format_exc())
        if not self.airtime_fairness_mode.get_selected() == self.config.config_vars.airtime_fairness_mode_value:
            raise AssertionError("Airtime Fairness Mode is not set to Fair Access i.e. Traceback: %s" %traceback.format_exc())
        if not self.slb_mode.get_selected() == self.config.config_vars.slb_mode_value:
            raise AssertionError("SLB Mode is not set to Channel i.e. Traceback: %s" %traceback.format_exc())
        if self.customize_valid_channels.is_selected():
            raise AssertionError("Customize Valid Channel is Checked i.e. Traceback: %s" %traceback.format_exc())
        if not self.min_transmit_power.get_selected() == self.config.config_vars.min_transmit_power_value:
            raise AssertionError("Min Transmit Power is not set to 18 i.e. Traceback: %s" %traceback.format_exc())
        if not self.max_transmit_power.get_selected() == self.config.config_vars.max_transmit_power_value:
            raise AssertionError("Max Transmit Power is not set to 18 i.e. Traceback: %s" %traceback.format_exc())
        if not self.client_aware.get_selected() == self.config.config_vars.client_aware_value:
            raise AssertionError("Client Aware is not set to Enabled i.e. Traceback: %s" %traceback.format_exc())
        if not self.scanning.get_selected() == self.config.config_vars.scanning_value:
            raise AssertionError("Scanning is not set to Enabled i.e. Traceback: %s" %traceback.format_exc())
        if not self.wide_channel_bands.get_selected() == self.config.config_vars.wide_channel_bands_value:
            raise AssertionError("Wide Channels Bands is not set to 5 GHz i.e. Traceback: %s" %traceback.format_exc())
        if not self.mhz_support.get_selected() == self.config.config_vars.mhz_support_value:
            raise AssertionError("80 MHz Support is not set to Disabled i.e. Traceback: %s" %traceback.format_exc())
        
    def check_rf_help(self):
        
        time.sleep(8)
        logger.debug('RF Page : Clicking Help button')
        self.help_button.click()
        time.sleep(8)
        actions = self.browser.get_action_chain()
        actions.move_to_element(self.band_streering_mode_help_link).perform()
        time.sleep(5)
        if not self.help_content:
            raise AssertionError("Band Streering Mode help content is not visible i.e. Traceback: %s" %traceback.format_exc())
        
    def modify_rf_arm_config(self):
        self._let_page_load()
        logger.debug('RfPage : Set airtime fairness mode to Preferred Access. ')
        self.airtime_fairness_mode.set(self.config.config_vars.new_airtime_fairness_mode_value)
        
    def assert_save_alert_pop_up(self,visible=False):
        logger.debug('RfPage : Checking whether the save alert pop up visible')
        if visible:
            if not self.confirm_save_ok :
                raise AssertionError("Save alert pop up not visible . i.e. Traceback: %s" %traceback.format_exc())
            if  self.confirm_save_cancel:
                raise AssertionError("Cancel button not visible . i.e. Traceback: %s" %traceback.format_exc())
            #logger.debug('RfPage : Click on save. ')
            #self.confirm_save_ok.click()
            time.sleep(8)
        else:
            if self.confirm_save_ok :
                raise AssertionError("Save alert pop up visible i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_transmit_power_dropdown_values(self,maximum=False):
        self._let_page_load()
        time.sleep(10)
        
        logger.debug('RfPage : Get all options from Max transmit power dropdown. ')
        if maximum:
            self.min_transmit_power.set('3')
            options = self.max_transmit_power.get_options()
        else:
            options = self.min_transmit_power.get_options()
        s = 0
        for x in range(0,6):
            s = s+3
            if not options[x] == str(s):
                
                raise AssertionError(" option %s is missing.  i.e. Traceback: %s " %(options[x],traceback.format_exc()))
        if maximum:
            if not options[11] == 'Max':
                raise AssertionError("Max option not present in max transmit power dropdown .i.e. Traceback: %s" %traceback.format_exc())
        else:
            if not options[11] == 'Max':
                raise AssertionError("Max option not present in min transmit power dropdown .i.e. Traceback: %s" %traceback.format_exc())
            

    def modify_transit_power(self,maximum=False,value='18'):
        if maximum:
            logger.debug('RfPage : Set max transmit power to %s .' %value)
            self.max_transmit_power.set(value)
        else:
            if value == '18':
                value = self.config.config_vars.minimum_transmit_power_value
            logger.debug('RfPage : Set max transmit power to %s .' %value)
            self.min_transmit_power.set(value)
        if self.save_settings:
            logger.debug('RfPage : Clicking on Save button')
            self.save_settings.click()
        self._buy_time()
        
    def check_all_values(self):
         
        self._let_page_load1()
        time.sleep(5)
        logger.debug('RfPage : Getting all options from Legacy Only dropdown of 2.4 GHz Band')
        options = self.legacy_only_24ghz.get_options()
        if not options[1] == self.config.config_vars.legacy_only_enabled:
            raise AssertionError("Legacy Only Enabled element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[0] == self.config.config_vars.legacy_only_disabled:
            raise AssertionError("Legacy Only Disabled element not matched i.e. Traceback: %s" %traceback.format_exc())
         
        logger.debug('RfPage : Getting all options from Legacy Only dropdown of 5 GHz Band')
        options = self.legacy_only_5ghz.get_options()
        if not options[1] == self.config.config_vars.legacy_only_enabled:
            raise AssertionError("Legacy Only Enabled element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[0] == self.config.config_vars.legacy_only_disabled:
            raise AssertionError("Legacy Only Disabled element not matched i.e. Traceback: %s" %traceback.format_exc())
         
        logger.debug('RfPage : Getting all options from 802.11d / 802.11h dropdown of 2.4 GHz Band')
        options = self.dropdown_11d_11h_24ghz.get_options()
        if not options[1] == self.config.config_vars.band_802_enabled:
            raise AssertionError("802.11d / 802.11h Enabled element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[0] == self.config.config_vars.band_802_disabled:
            raise AssertionError("802.11d / 802.11h Disabled element not matched i.e. Traceback: %s" %traceback.format_exc())
         
        logger.debug('RfPage : Getting all options from 802.11d / 802.11h dropdown of 5 GHz Band')
        options = self.dropdown_11d_11h_5ghz.get_options()
        if not options[1] == self.config.config_vars.band_802_enabled:
            raise AssertionError("802.11d / 802.11h Enabled element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[0] == self.config.config_vars.band_802_disabled:
            raise AssertionError("802.11d / 802.11h Disabled element not matched i.e. Traceback: %s" %traceback.format_exc())
         
        logger.debug('RfPage : Getting all options from Background Spectrum Monitoring dropdown of 2.4 GHz Band')
        time.sleep(5)
        options = self.background_spectrum_24ghz.get_options()
        if not options[1] == self.config.config_vars.spectrum_monitoring_enabled:
            raise AssertionError("Background Spectrum Monitoring Enabled element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[0] == self.config.config_vars.spectrum_monitoring_disabled:
            raise AssertionError("Background Spectrum Monitoring Disabled element not matched i.e. Traceback: %s" %traceback.format_exc())
         
        logger.debug('RfPage : Getting all options from Background Spectrum Monitoring dropdown of 5 GHz Band')
        time.sleep(5)
        options = self.background_spectrum_5ghz.get_options()
        if not options[1] == self.config.config_vars.spectrum_monitoring_enabled:
            raise AssertionError("Background Spectrum Monitoring Enabled element not matched i.e. Traceback: %s" %traceback.format_exc())
        if not options[0] == self.config.config_vars.spectrum_monitoring_disabled:
            raise AssertionError("Background Spectrum Monitoring Disabled element not matched i.e. Traceback: %s" %traceback.format_exc())
          
        logger.debug('RfPage : Getting all options from Interference Immunity Level dropdown of 2.4 GHz Band')
        options = self.interface_immunity_24ghz.get_options()
        for x in range(0,5):
            if not options[x] == str(x):
                raise AssertionError("Background Spectrum Monitoring element not matched i.e. Traceback: %s" %traceback.format_exc())
             
        logger.debug('RfPage : Getting all options from Interference Immunity Level dropdown of 5 GHz Band')
        options = self.interface_immunity_5ghz.get_options()
        for x in range(0,5):
            if not options[x] == str(x):
                raise AssertionError("Background Spectrum Monitoring element not matched i.e. Traceback: %s" %traceback.format_exc())
        
        logger.debug('RfPage : Getting all options from Channel switch announcement count of 2.4 GHz band')
        options = self.channel_switch_announce_24ghz.get_options()
        for x in range(0,10):
            if not options[x] == str(x):
                raise AssertionError("Channel switch announcement count element not matched i.e. Traceback: %s" %traceback.format_exc())
            
        logger.debug('RfPage : Getting all options from Channel switch announcement count of 5 GHz band')
        options = self.channel_switch_announce_5ghz.get_options()
        for x in range(0,10):
            if not options[x] == str(x):
                raise AssertionError("Channel switch announcement count element not matched i.e. Traceback: %s" %traceback.format_exc())
    
    def select_default_instant(self):
        '''
        selects default group : instant
        '''
        time.sleep(5)
        logger.debug('Rf Page : Expanding All Groups')
        self.all_group_button.click()
        logger.debug('Rf Page : Expanding default group')
        self.default_expand_button.click()
        logger.debug('Rf Page : Select Instant')
        self.default_group_instant_option.click()
        time.sleep(5)
    
    def set_legacy_radio_parameter(self):
         
        logger.debug('Rf Page : Clicking on radio accordion')
        self.radio_section.click()
        time.sleep(5)
        logger.debug('Rf Page : Setting Legacy Only to Enabled')
        self.legacy_only_24ghz.set(self.config.config_vars.new_legacy_only_24ghz_value)
        time.sleep(5)
        self.save_changes()
        time.sleep(180)
        
    def assert_detection_resolve_override_flag(self):
        
        if not self.override_flag_button:
            raise AssertionError("Override flag is not visible i.e. Traceback: %s" %traceback.format_exc())
        logger.debug('Rf Page : Clicking on override flag')
        self.override_flag_button.click()
        time.sleep(5)
        if not self.rf_radio_override_flag_options:
            raise AssertionError("Legacy mode is not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.rf_radio_override_flag_vc_name:
            raise AssertionError("VC name is not present i.e. Traceback: %s" %traceback.format_exc())
        logger.debug('Rf Page : Clicking Resolve All')
        self.override_resolv_button.click()
        time.sleep(8)
        
    def set_legacy_radio_parameter_default(self):
         
        time.sleep(5)
        logger.debug('Rf Page : Setting Legacy Only to Disabled')
        self.legacy_only_24ghz.set(self.config.config_vars.legacy_only_24ghz_value)
        time.sleep(5)
        self.save_changes()
        time.sleep(5)
        
    def set_arm_parameters(self):
         
        time.sleep(5)
        logger.debug('Rf Page : Setting CM Threshold')
        self.cm_threshold.set(self.config.config_vars.cm_threshold_boundry_value)
        logger.debug('Rf Page : Setting CM Neighbour Matching')
        self.cm_neighbour_matching.set(self.config.config_vars.cm_neighbour_matching_boundry_value)
        logger.debug('Rf Page : Setting Scanning')
        self.scanning.set(self.config.config_vars.new_scanning_value)
        logger.debug('Rf Page : Setting Client Aware')
        self.client_aware.set(self.config.config_vars.new_client_aware_value)
        time.sleep(5)
        self.save_changes()
        time.sleep(180)
        
    def assert_resolve_rf_arm_override_flag(self):
        
        if not self.override_flag_button:
            raise AssertionError("Override flag is not visible i.e. Traceback: %s" %traceback.format_exc())
        logger.debug('RFPage : Clicking on override flag')
        self.override_flag_button.click()
        time.sleep(5)
        if not self.override_flag_client_aware:
            raise AssertionError("Client aware is not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.override_flag_scanning:
            raise AssertionError("Scanning is not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.override_flag_nb_matching:
            raise AssertionError("Client match is not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.override_flag_calc_threshold:
            raise AssertionError("CM threshold is not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.rf_radio_override_flag_vc_name:
            raise AssertionError("VC name is not present i.e. Traceback: %s" %traceback.format_exc())
        logger.debug('WidsPage : Clicking Resolve All')
        self.override_resolv_button.click()
        time.sleep(8)
        
    def set_arm_parameters_default(self):
         
        time.sleep(5)
        logger.debug('Rf Page : Setting default CM Threshold')
        self.cm_threshold.set(self.config.config_vars.cm_threshold_value)
        logger.debug('Rf Page : Setting default CM Neighbour Matching')
        self.cm_neighbour_matching.set(self.config.config_vars.cm_neighbour_matching_value)
        logger.debug('Rf Page : Setting default Scanning')
        self.scanning.set(self.config.config_vars.scanning_value)
        logger.debug('Rf Page : Setting default Client Aware')
        self.client_aware.set(self.config.config_vars.client_aware_value)
        time.sleep(5)
        self.save_changes()
        
    def assert_24ghz_checkbox_values(self):
        
        logger.debug('RfPage : Checking whether the following checkboxes for 2.4 Ghz are visible')
        if not self.channel_24ghz_1:
            raise AssertionError("channel 24 checkbox_1 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_24ghz_2:
            raise AssertionError("channel 24 checkbox_2 not visible i.e. Traceback: %s" %traceback.format_exc())    
        if not self.channel_24ghz_3:
            raise AssertionError("channel 24 checkbox_3 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_24ghz_4:
            raise AssertionError("channel 24 checkbox_4 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_24ghz_5:
            raise AssertionError("channel 24 checkbox_5 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_24ghz_6:
            raise AssertionError("channel 24 checkbox_6 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_24ghz_7:
            raise AssertionError("channel 24 checkbox_7 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_24ghz_8:
            raise AssertionError("channel 24 checkbox_8 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_24ghz_9:
            raise AssertionError("channel 24 checkbox_9 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_24ghz_10:
            raise AssertionError("channel 24 checkbox_10 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_24ghz_11:
            raise AssertionError("channel 24 checkbox_11 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_24ghz_12:
            raise AssertionError("channel 24 checkbox_12 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_24ghz_13:
            raise AssertionError("channel 24 checkbox_13 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_24ghz_1plus:
            raise AssertionError("channel 24 checkbox_1+ not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_24ghz_2plus:
            raise AssertionError("channel 24 checkbox_2+ not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_24ghz_3plus:
            raise AssertionError("channel 24 checkbox_3+ not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_24ghz_4plus:
            raise AssertionError("channel 24 checkbox_4+ not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_24ghz_5plus:
            raise AssertionError("channel 24 checkbox_5+ not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_24ghz_6plus:
            raise AssertionError("channel 24 checkbox_6+ not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_24ghz_7plus:
            raise AssertionError("channel 24 checkbox_7+ not visible i.e. Traceback: %s" %traceback.format_exc())
        
            
    def assert_5ghz_checkbox_values(self):
        
        logger.debug('RfPage : Checking whether the following checkboxes for 5Ghz are visible')
        if not self.channel_5ghz_36:
            raise AssertionError("channel 5 checkbox_36 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_40:
            raise AssertionError("channel 5 checkbox_40 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_44:
            raise AssertionError("channel 5 checkbox_44 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_48:
            raise AssertionError("channel 5 checkbox_48 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_52:
            raise AssertionError("channel 5 checkbox_52 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_56:
            raise AssertionError("channel 5 checkbox_56 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_60:
            raise AssertionError("channel 5 checkbox_60 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_64:
            raise AssertionError("channel 5 checkbox_64 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_100:
            raise AssertionError("channel 5 checkbox_100 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_104:
            raise AssertionError("channel 5 checkbox_104 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_108:
            raise AssertionError("channel 5 checkbox_108 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_112:
            raise AssertionError("channel 5 checkbox_112 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_116:
            raise AssertionError("channel 5 checkbox_116 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_120:
            raise AssertionError("channel 5 checkbox_120 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_124:
            raise AssertionError("channel 5 checkbox_124 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_128:
            raise AssertionError("channel 5 checkbox_128 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_132:
            raise AssertionError("channel 5 checkbox_132 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_136:
            raise AssertionError("channel 5 checkbox_136 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_140:
            raise AssertionError("channel 5 checkbox_140 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_149:
            raise AssertionError("channel 5 checkbox_149 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_153:
            raise AssertionError("channel 5 checkbox_153 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_157:
            raise AssertionError("channel 5 checkbox_157 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_161:
            raise AssertionError("channel 5 checkbox_161 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_165:
            raise AssertionError("channel 5 checkbox_165 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_36plus:
            raise AssertionError("channel 5 checkbox_36+ not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_44plus:
            raise AssertionError("channel 5 checkbox_44+ not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_52plus:
            raise AssertionError("channel 5 checkbox_52+ not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_60plus:
            raise AssertionError("channel 5 checkbox_60+ not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_100plus:
            raise AssertionError("channel 5 checkbox_100+ not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_108plus:
            raise AssertionError("channel 5 checkbox_108+ not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_132plus:
            raise AssertionError("channel 5 checkbox_132+ not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_149plus:
            raise AssertionError("channel 5 checkbox_149+ not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_157plus:
            raise AssertionError("channel 5 checkbox_157+ not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_36E:
            raise AssertionError("channel 5 checkbox_36E not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_52E:
            raise AssertionError("channel 5 checkbox_52E not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_100E:
            raise AssertionError("channel 5 checkbox_100E not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_116E:
            raise AssertionError("channel 5 checkbox_116E not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_132E:
            raise AssertionError("channel 5 checkbox_132E not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_149E:
            raise AssertionError("channel 5 checkbox_149E not visible i.e. Traceback: %s" %traceback.format_exc())
            
    def custom_channel_defaults(self):
        self._buy_time()
        logger.debug('RFPage : Clicking customize valid channels')
        self.customize_valid_channels.click()
        logger.debug('RFPage :clicking 2.4 ghz edit button')
        self.edit_24_ghz.click()
        self._buy_time()
        self.assert_24ghz_checkbox_values()
        logger.debug('RFPage :Clicking 2.4ghz : 3')
        self.channel_24ghz_3.click()
        logger.debug('RFPage :Clicking 5+')
        self.channel_24ghz_5plus.click()
        self._buy_time()
        logger.debug('RFPage :clicking 5ghz ghz edit button')
        self.edit_5_ghz.click()
        self._buy_time()
        if not self.mhz_support.get_selected() == self.config.config_vars.mhz_support_value:
            raise Exception("Value of '80 MHz Support' is not Disabled")
        self.assert_5ghz_checkbox_for_few_values()
        self.assert_5ghz_checkbox_values()
        logger.debug('RFPage :Clicking 5ghz : 36')
        self.channel_5ghz_36.click()
        logger.debug('RFPage :Clicking 5ghz : 44+')
        self.channel_5ghz_44plus.click()
        logger.debug('RFPage :Clicking 5ghz : 52E')
        self.channel_5ghz_52E.click()
        self._buy_time()
        logger.debug('RfPage : Clicking on Save button')
        self.save_settings.click()
        
    def revert_custom_channel_values(self):
        logger.debug('RFPage: deselecting 2.4Ghz : 3')
        self.channel_24ghz_3.click()
        logger.debug('RFPage: deselecting 2.4Ghz : 5+')
        self.channel_24ghz_5plus.click()
        logger.debug('RFPage: clicking on close 2.4ghz button ')
        self.close_24ghz_channels.click()
        self._buy_time()
        logger.debug('RFPage: deselecting 5Ghz : 36')
        self.channel_5ghz_36.click()
        logger.debug('RFPage: deselecting 5Ghz : 44')
        self.channel_5ghz_44plus.click()
        logger.debug('RFPage: deselecting 5Ghz : 52E')
        self.channel_5ghz_52E.click()
        logger.debug('RFPage: clicking on close 5ghz button ')
        self.hide_5ghz_channels.click()
        self._buy_time()
        logger.debug('RFPage: clicking on customize valid channels ')
        self.customize_valid_channels.click()
        logger.debug('RfPage : Clicking on Save button')
        self.save_settings.click()
        
    def assert_5ghz_checkbox_for_few_values(self):
        logger.debug('RfPage : Checking whether the following checkboxes for 5Ghz are visible')
        if not self.channel_5ghz_36E:
            raise AssertionError("channel 5 checkbox_36E visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_52E:
            raise AssertionError("channel 5 checkbox_52E visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_100E:
            raise AssertionError("channel 5 checkbox_100E visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_116E:
            raise AssertionError("channel 5 checkbox_116E visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_132E:
            raise AssertionError("channel 5 checkbox_132E  visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_149E:
            raise AssertionError("channel 5 checkbox_149E visible i.e. Traceback: %s" %traceback.format_exc())

    def open_arm_accordion(self):
        time.sleep(10)
        logger.debug('RFPage : Clicking on RF ARm Accordion')
        self.arm_section.click()
    
    def set_legacy_only_24ghz(self,value=None):
        '''
        sets legacy only 2.4ghz
        '''
        if value:
            logger.debug('RFPage: Wriiting legacy only 2.4ghz')
            self.legacy_only_24ghz.set(value)
        else:
            logger.debug('RFPage: Wriiting legacy only 2.4ghz')
            self.legacy_only_24ghz.set(self.config.config_vars.legacy_only_24ghz_value)
    
    def set_dropdown_11d_11h_24ghz(self,value=None):
        '''
        sets given value to 11d 11h 2.4ghz
        '''
        if value:
            logger.debug('RFPage: Wriiting 11d 11h 2.4ghz')
            self.dropdown_11d_11h_24ghz.set(value)
        else:
            self.dropdown_11d_11h_24ghz.set(self.config.config_vars.band_802_disabled)
            
    def set_beacon_interval_24ghz(self,value=None):
        '''
        sets given value to beacon interval
        '''
        if value:
            logger.debug('RFPage: Wriiting beacon interval')
            self.beacon_interval_24ghz.set(value)
        else:
            logger.debug('RFPage: Wriiting beacon interval')
            self.beacon_interval_24ghz.set(self.config.config_vars.beacon_interval_value)
    
    def set_interface_immunity_24ghz(self,value=None):
        '''
        sets given value to interface immunity 2.4ghz
        '''
        if value:
            logger.debug('RFPage: Wriiting interface immunity 2.4ghz')
            self.interface_immunity_24ghz.set(value)
        else:
            logger.debug('RFPage: Wriiting interface immunity 2.4ghz')
            self.interface_immunity_24ghz.set(self.config.config_vars.interface_immunity_24ghz_value)
    
    def set_channel_switch_announce_24ghz(self,value=None):
        '''
        sets given value to channel switch announce 2,4ghz
        '''
        if value:
            logger.debug('RFPage: Wriiting channel switch announce')
            self.channel_switch_announce_24ghz.set(value)
        else:
            logger.debug('RFPage: Wriiting channel switch announce')
            self.channel_switch_announce_24ghz.set(self.config.config_vars.channel_switch_announce_24ghz_value)
    
    def set_background_spectrum_24ghz(self,value=None):
        '''
                sets given value to background spectrum
        '''
        if value:
            logger.debug('RFPage: Wriiting background spectrum')
            self.background_spectrum_24ghz.set(value)
        else:
            logger.debug('RFPage: Wriiting background spectrum')
            self.background_spectrum_24ghz.set(self.config.config_vars.background_spectrum_24ghz_value)
    
    def set_legacy_only_5ghz(self,value=None):
        '''
                sets given value to legacy only 5ghz
        '''
        if value:
            logger.debug('RFPage: Wriiting legacy only 5ghz')
            self.legacy_only_5ghz.set(value)
        else:
            logger.debug('RFPage: Wriiting legacy only 5ghz')
            self.legacy_only_5ghz.set(self.config.config_vars.legacy_only_5ghz_value)
    
    def set_dropdown_11d_11h_5ghz(self,value=None):
        '''
                sets given value to 11d 11h 5ghz
        '''
        if value:
            logger.debug('RFPage: Wriiting 11d 11h 5ghz')
            self.dropdown_11d_11h_5ghz.set(value)
        else:
            logger.debug('RFPage: Wriiting 11d 11h 5ghz')
            self.dropdown_11d_11h_5ghz.set(self.config.config_vars.band_802_disabled)
            
    def set_beacon_interval_5ghz(self,value=None):
        '''
                sets given value to beacon interval 5ghz
        '''
        if value:
            logger.debug('RFPage: Wriiting beacon interval 5ghz')
            self.beacon_interval_5ghz.set(value)
        else:
            logger.debug('RFPage: Wriiting beacon interval 5ghz')
            self.beacon_interval_5ghz.set(self.config.config_vars.beacon_interval_value)
    
    def set_interface_immunity_5ghz(self,value=None):
        '''
                sets given value to interface immunity 5ghz
        '''
        if value:
            logger.debug('RFPage: Wriiting interface immunity 5ghz')
            self.interface_immunity_5ghz.set(value)
        else:
            logger.debug('RFPage: Wriiting interface immunity 5ghz')
            self.interface_immunity_5ghz.set(self.config.config_vars.interface_immunity_5ghz_value)
    
    def set_channel_switch_announce_5ghz(self,value=None):
        '''
                sets given value to switch announce 5ghz
        '''
        if value:
            logger.debug('RFPage: Wriiting switch announce 5ghz')
            self.channel_switch_announce_5ghz.set(value)
        else:
            logger.debug('RFPage: Wriiting switch announce 5ghz')
            self.channel_switch_announce_5ghz.set(self.config.config_vars.channel_switch_announce_5ghz_value)
    
    def set_background_spectrum_5ghz(self,value=None):
        '''
                sets given value to background spectrum 5ghz
        '''
        if value:
            logger.debug('RFPage: Wriiting background spectrum 5ghz')
            self.background_spectrum_5ghz.set(value)
        else:
            logger.debug('RFPage: Wriiting background spectrum 5ghz')
            self.background_spectrum_5ghz.set(self.config.config_vars.background_spectrum_5ghz_value)
    
    def set_rf_arm_client_control_band_sterring_mode(self,value):
        '''
        set non default value for Radio ARM Client Control BandSteering Mode
        '''
        time.sleep(15)
        if value == None:
            logger.debug('RfPage : Setting Band Streering dropdown to value')
            self.band_steering_mode.set(self.config.config_vars.band_steering_mode_value)
        else:
            logger.debug('RfPage : Setting Band Streering dropdown to value')
            self.band_steering_mode.set(value)
        
    def set_rf_arm_client_control_airtime_fairness_mode(self,value):
        '''
        set non default value for Radio ARM Client Control AIRTIME FAIRNESS MODE
        '''
        if value == None:
            logger.debug('RfPage : Setting AIRTIME FAIRNESS MODE to value')
            self.airtime_fairness_mode.set(self.config.config_vars.airtime_fairness_mode_value)
        else:
            logger.debug('RfPage : Setting AIRTIME FAIRNESS MODE to value')
            self.airtime_fairness_mode.set(value)
    def set_rf_arm_client_control_client_match(self,value):
        '''
        set Radio ARM Client Control Client Match value
        '''
        if value == None:
            logger.debug('RfPage : Setting  Client Match to value')
            self.client_match.set(self.config.config_vars.client_match_disabled)    
        else:
            logger.debug('RfPage : Setting  Client Match to value')
            self.client_match.set(value)    
        
            
    def set_rf_arm_client_control_cm_calculating_interval(self,value):
        '''
        set Radio ARM Client Control CM CALCULATING INTERVAL value
        '''        
        if value == None:
            logger.debug('RfPage : Setting  CM CALCULATING INTERVAL value')
            self.cm_calculating_interval.set(self.config.config_vars.cm_calculating_interval_value)    
        else:
            logger.debug('RfPage : Setting  CM CALCULATING INTERVAL value')
            self.cm_calculating_interval.set(value)    
        
            
    def set_rf_arm_client_control_cm_neighbor_matching(self,value):
        '''
        set Radio ARM Client Control CM NEIGHBOR MATCHING value
        '''        
        if value == None:
            logger.debug('RfPage : Setting CM NEIGHBOR MATCHING  value')
            self.cm_neighbour_matching.set(self.config.config_vars.cm_neighbour_matching_value)    
        else:
            logger.debug('RfPage : Setting CM NEIGHBOR MATCHING value')
            self.cm_neighbour_matching.set(value)
        
    def set_rf_arm_client_control_cm_threshold(self,value):
        '''
        set Radio ARM Client Control CM THRESHOLD value
        '''        
        if value == None:
            logger.debug('RfPage : Setting CM THRESHOLD  value')
            self.cm_threshold.set(self.config.config_vars.cm_threshold_value)
        else:
            logger.debug('RfPage : Setting CM THRESHOLD value')
            self.cm_threshold.set(value)
        
    def set_rf_arm_client_control_slb_mode(self,value):
        '''
        set Radio ARM Client Control SLB MODE value
        '''        
        if value == None:
            logger.debug('RfPage : Setting SLB MODE  value')
            self.slb_mode.set(self.config.config_vars.slb_mode_value)

        else:
            logger.debug('RfPage : Setting SLB MODE value')
            self.slb_mode.set(value)
    def set_rf_arm_access_point_control_customized_valid_channel(self,check):
        '''
        set Radio ARM Access point Control  CUSTOMIZE VALID CHANNELS value
        '''        
        if check == 'true':
            logger.debug('RfPage : Setting CUSTOMIZE VALID CHANNELSvalue value')
            self.customize_valid_channels.click()
            if not self.customize_valid_channels.is_selected():
                self.customize_valid_channels.click()
        else:
            logger.debug('RfPage : Setting CUSTOMIZE VALID CHANNELSvalue  value')
            if self.customize_valid_channels.is_selected():
                self.customize_valid_channels.click()
                
    def set_rf_arm_access_point_control_min_transmit_power(self,value):
        '''
        set Radio ARM Access point Control  MIN TRANSMIT POWER value
        '''        
        if value == None:
            logger.debug('RfPage : Setting MIN TRANSMIT POWER value')
            self.min_transmit_power.set(self.config.config_vars.min_transmit_power_value)

        else:
            logger.debug('RfPage : Setting MIN TRANSMIT POWER value')
            self.min_transmit_power.set(value)
                
    def set_rf_arm_access_point_control_max_transmit_power(self,value):
        '''
        set Radio ARM Access point Control  MAX TRANSMIT POWER value
        '''        
        if value == None:
            logger.debug('RfPage : Setting MAX TRANSMIT POWER value')
            self.max_transmit_power.set(self.config.config_vars.max_transmit_power_value)

        else:
            logger.debug('RfPage : Setting MAX TRANSMIT POWER value')
            self.max_transmit_power.set(value)    
            
    def set_rf_arm_access_point_control_client_aware(self,value):
        '''
        set Radio ARM Access point Control  CLIENT AWARE value
        '''        
        if value == None:
            logger.debug('RfPage : Setting CLIENT AWARE value')
            self.client_aware.set(self.config.config_vars.client_aware_value)

        else:
            logger.debug('RfPage : Setting CLIENT AWARE value')
            self.client_aware.set(value)    
    
    def set_rf_arm_access_point_control_scanning(self,value):
        '''
        set Radio ARM Access point Control SCANNING value
        '''        
        if value == None:
            logger.debug('RfPage : Setting SCANNING value')
            self.scanning.set(self.config.config_vars.scanning_value)

        else:
            logger.debug('RfPage : Setting SCANNING value')
            self.scanning.set(value)
            
    def set_rf_arm_access_point_control_wide_channel_bands(self,value):
        '''
        set Radio ARM Access point Control WIDE CHANNEL BANDS value
        '''        
        if value == None:
            logger.debug('RfPage : Setting WIDE CHANNEL BANDS value')
            self.wide_channel_bands.set(self.config.config_vars.wide_channel_bands_value)

        else:
            logger.debug('RfPage : Setting WIDE CHANNEL BANDS value')
            self.wide_channel_bands.set(value)
        
    def set_rf_arm_access_point_control_mhz_support(self,value):
        '''
        set Radio ARM Access point Control80 MHZ SUPPORT value
        '''        
        if value == None:
            logger.debug('RfPage : Setting 80 MHZ SUPPORT value')
            self.mhz_support.set(self.config.config_vars.mhz_support_value)

        else:
            logger.debug('RfPage : Setting 80 MHZ SUPPORT value')
            self.mhz_support.set(value)
            
    def assert_save_settings_button(self):
        '''
        asserting save settings button
        '''
        self._buy_time()
        logger.debug('RfPage :asserting save settings button')
        if not self.save_button:
            raise AssertionError("Save Settings button is not present i.e. Traceback: %s" %traceback.format_exc())
            
    def click_on_rf_cancel_button(self):
        '''
        clicking on CANCEL button
        '''
        self._buy_time()
        logger.debug('RfPage : Clicking on Cancel Button')
        self.rf_cancel_button.click()
            
    def assert_edited_rf_arm_values(self):
        '''
        asserting edited fields
        '''
        self._buy_time()
        logger.debug('RfPage :Asserting on the edited vales of rf arm feilds ')
        if not self.slb_mode.get_selected() == self.config.config_vars.slb_mode_value_3rd:
            raise Exception("Edited Value of 'SLB Mode' is changed")
        if not self.cm_calculating_interval.get() == self.config.config_vars.cm_calculating_interval_boundry_value1:
            raise Exception("Edited Value of 'CM CALCULATING INTERVAL' is changed")
        if not self.cm_neighbour_matching.get() == self.config.config_vars.cm_neighbour_matching_value1:
            raise AssertionError("Edited Value of 'CM NEIGHBOUR MATCHING' is changed")    
        if not self.cm_threshold.get() == self.config.config_vars.cm_threshold_value1:
            raise AssertionError("Edited Value of 'CM THRESHOLD' is changed")    

    def assert_cm_calculating_interval(self):
        logger.debug('RfPage :Checking for cm calculating interval error msg ')
        if not self.cm_calculating_interval.get() == self.config.config_vars.cm_calculating_interval_value:
            raise AssertionError("default value of 'CM CALCULATING INTERVAL' is not 30 i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_cm_calulating_error(self):
        logger.debug('RfPage :Checking for cm calculating error msg ')
        if not self.error_message_calc_intr:
            raise AssertionError("Invalid value error message not found i.e. Traceback: %s" %traceback.format_exc())

    def assert_cm_neighbour_matching(self):
        logger.debug('RfPage :Checking for cm neighbour matching error msg ')
        if not self.error_mssg_neigh_match:
            raise AssertionError("'cm neighbour matching' error message not found i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_cm_threshold(self):
        logger.debug('RfPage :Checking for cm threshold error msg ')
        if not self.error_mssg_threshold:
            raise AssertionError("CM Threshold error message is not visible i.e. Traceback: %s" %traceback.format_exc())
        
    def assert_cm_calulating_error(self,assert_error):
        logger.debug('RfPage :Checking for error msg ')
        self._buy_time()
        if assert_error == 'true':
            if not self.error_message_calc_intr:
                raise AssertionError("Invalid value error message not found i.e. Traceback: %s" %traceback.format_exc())
        elif assert_error == 'false':
            if self.error_message_calc_intr:
                raise AssertionError("Must be a number in range 20-100 i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_cm_neighbour_matching(self,assert_error):
        logger.debug('RfPage :Checking for error msg ')
        if assert_error == 'true':
            if not self.error_mssg_neigh_match:
                raise AssertionError("'cm neighbour matching' error message not found i.e. Traceback: %s" %traceback.format_exc())
        elif assert_error == 'false':        
            if  self.error_mssg_neigh_match:
                raise AssertionError("Must be a number in range 1-100 i.e. Traceback: %s" %traceback.format_exc())    
                
    def assert_cm_threshold(self,assert_error):
        logger.debug('RfPage :Checking for error msg ')
        if assert_error == 'true':
            if not self.error_mssg_threshold:
                raise AssertionError("CM Threshold error message is not visible i.e. Traceback: %s" %traceback.format_exc())
        elif assert_error == 'false':        
            if  self.error_mssg_threshold:
                raise AssertionError("Must be a number in range 1-20 i.e. Traceback: %s" %traceback.format_exc())
                
    def assert_cm_calculating_interval_seconds_label(self):
        logger.debug('RfPage :Checking whether cm calculating interval seconds label is  present ')
        if not self.cm_calculating_interval_seconds_label:
            raise AssertionError("assert cm calculating interval seconds label is not present i.e. Traceback: %s" %traceback.format_exc())
            
    def click_on_cm_calculating_interval_seconds_label(self):
        logger.debug('RfPage :Clicking on cm calculating interval seconds label')
        self._buy_time()
        self.cm_calculating_interval_seconds_label.click()
            
    def assert_cm_neighbour_matching_style(self):
        logger.debug('RfPage :Checking whether cm calculating interval seconds label is  present')
        if not self.cm_neighbor_matching_style:
            raise AssertionError("assert cm calculating interval seconds label is not present i.e. Traceback: %s" %traceback.format_exc())
            
    def click_on_cm_neighbour_matching_style(self):
        logger.debug('RfPage :Clicking on Edit icon of cm neighbor matching style')
        self._buy_time()
        self.cm_neighbor_matching_style.click()
    
    def assert_access_point_control_customized_valid_channel_checkbox(self):
        logger.debug('RfPage : Asserting whether the customize valid channel checkbox is checked')
        if self.customize_valid_channels.is_selected():
            raise AssertionError(" CUSTOMIZE VALID CHANNELS is checked i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_access_point_control_customized_valid_channels(self):
        logger.debug('RfPage : Asserting whether the following checkboxes are visible')
        if not self.edit_24_ghz_label:
            raise AssertionError(" CUSTOMIZE VALID CHANNELS 2.4GHz label is not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.edit_5_ghz_label:
            raise AssertionError(" CUSTOMIZE VALID CHANNELS 5GHz label is not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.edit_24_ghz:
            raise AssertionError(" CUSTOMIZE VALID CHANNELS 2.4GHz edit button is not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.edit_5_ghz:
            raise AssertionError(" CUSTOMIZE VALID CHANNELS 5GHz edit button is not present  i.e. Traceback: %s" %traceback.format_exc())
        
    def click_on_edit_24_ghz(self):
        '''
        clicking on CUSTOMIZE VALID CHANNELS edit 24 ghz button
        '''
        logger.debug('RfPage : Clicking on Edit icon of 5ghz channel ')
        self.edit_24_ghz.click()
        
    def click_on_edit_5_ghz(self):
        '''
        clicking on CUSTOMIZE VALID CHANNELS edit 5ghz button
        '''
        logger.debug('RfPage : Clicking on Edit icon of 5ghz channel ')
        self.edit_5_ghz.click()    
    
    def click_on_close_24_ghz(self):
        '''
        clicking on CUSTOMIZE VALID CHANNELS  5ghz close button
        '''
        logger.debug('RfPage : Clicking on Close icon of 2.4ghz channel ')
        self.close_24ghz_channels.click()
    
    def click_on_close_5_ghz(self):
        '''
        clicking on CUSTOMIZE VALID CHANNELS edit 5ghz close button
        '''
        logger.debug('RfPage : Clicking on Close icon of 5ghz channel ')
        self.hide_5ghz_channels.click()
    
    def assert_5ghz_checkbox_values1(self):
        logger.debug('RfPage : Asserting whether the following checkboxes are visible')
        if not self.channel_5ghz_36:
            raise AssertionError("channel 5 checkbox_36 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_40:
            raise AssertionError("channel 5 checkbox_40 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_44:
            raise AssertionError("channel 5 checkbox_44 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_48:
            raise AssertionError("channel 5 checkbox_48 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_52:
            raise AssertionError("channel 5 checkbox_52 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_56:
            raise AssertionError("channel 5 checkbox_56 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_60:
            raise AssertionError("channel 5 checkbox_60 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_64:
            raise AssertionError("channel 5 checkbox_64 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_149:
            raise AssertionError("channel 5 checkbox_149 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_153:
            raise AssertionError("channel 5 checkbox_153 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_157:
            raise AssertionError("channel 5 checkbox_157 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_161:
            raise AssertionError("channel 5 checkbox_161 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_165:
            raise AssertionError("channel 5 checkbox_165 not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_36plus:
            raise AssertionError("channel 5 checkbox_36+ not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_44plus:
            raise AssertionError("channel 5 checkbox_44+ not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_52plus:
            raise AssertionError("channel 5 checkbox_52+ not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_60plus:
            raise AssertionError("channel 5 checkbox_60+ not visible i.e. Traceback: %s" %traceback.format_exc())
        if not self.channel_5ghz_149plus:
            raise AssertionError("channel 5 checkbox_149+ not visible i.e. Traceback: %s" %traceback.format_exc())
            
            
    def assert_min_transmit_power_dropdown_values(self,maximum=False):
        time.sleep(10)
        logger.debug('RfPage : Get all options from min transmit power dropdown. ')
        if maximum:
            self.min_transmit_power.set('3')
            options = self.max_transmit_power.get_options()
        else:
            options = self.min_transmit_power.get_options()
        s = 0
        for x in range(0,10):
            s = s+3
            if not options[x] == str(s):
                
                raise AssertionError(" option %s is missing.  i.e. Traceback: %s " %(options[x],traceback.format_exc()))
        if not options[11] == 'Max':
            raise AssertionError("max option not present in min transmit power dropdown .i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_max_transmit_power_dropdown_values(self,minimum=False):
        time.sleep(10)
        logger.debug('RfPage : Get all options from min transmit power dropdown. ')
        if minimum:
            self.max_transmit_power.set('12')
            options = self.min_transmit_power.get_options()
            s = 0
            for x in range(0,3):
                s = s+3
                if not options[x] == str(s):
                    
                    raise AssertionError(" option %s is missing.  i.e. Traceback: %s " %(options[x],traceback.format_exc()))
        else:
            options = self.max_transmit_power.get_options()
            s = 15
            for x in range(0,5):
                s = s+3
                if not options[x] == str(s):
                    
                    raise AssertionError(" option %s is missing.  i.e. Traceback: %s " %(options[x],traceback.format_exc()))
            if not options[6] == 'Max':
                raise AssertionError("Max option not present in max transmit power dropdown .i.e. Traceback: %s" %traceback.format_exc())
        
    def validating_cm_calculating_interval(self):
        conf = self.config.config_vars
        logger.debug('RfPage :Setting rf arm client control cm calculating interval with empty values')
        self.set_rf_arm_client_control_cm_calculating_interval(conf.empty_value)
        self.save_changes()
        self.assert_cm_calulating_error('true')
        
        logger.debug('RfPage :Setting rf arm client control cm calculating interval with empty values')
        self.set_rf_arm_client_control_cm_calculating_interval(conf.invalid_cm_calculating_interval_value)
        self.save_changes()
        self.assert_cm_calulating_error('true')
        
        logger.debug('RfPage :Setting rf arm client control cm calculating interval with valid values')
        self.set_rf_arm_client_control_cm_calculating_interval(conf.valid_cm_calculating_interval)
        self.click_on_cm_calculating_interval_seconds_label()
        self.assert_cm_calulating_error('false')
        
        logger.debug('RfPage :Setting rf arm client control cm calculating interval to 15')
        self.set_rf_arm_client_control_cm_calculating_interval(conf.new_cm_calculating_interval_value)
        self.save_changes()
        self.assert_cm_calulating_error('true')
        
        logger.debug('RfPage :Setting rf arm client control cm calculating interval to 80')
        self.set_rf_arm_client_control_cm_calculating_interval(conf.cm_calculating_interval_boundry_value)
        self.click_on_cm_calculating_interval_seconds_label()
        self.assert_cm_calulating_error('false')
        
        logger.debug('RfPage :Setting rf arm client control cm calculating interval with zero preceding values')
        self.set_rf_arm_client_control_cm_calculating_interval(conf.zero_preceding_cm_calcultng_interval)
        self.save_changes()
        self.assert_cm_calulating_error('true')
        
        logger.debug('RfPage :Setting rf arm client control cm calculating interval with string values')
        self.set_rf_arm_client_control_cm_calculating_interval(conf.string_cm_calculating_interval)
        self.save_changes()
        self.assert_cm_calulating_error('true')
        
    def validating_client_control_cm_neighbor_matching(self):
        conf = self.config.config_vars
        logger.debug('RfPage :Setting rf arm client control cm neighbor matching with empty values')
        self.set_rf_arm_client_control_cm_neighbor_matching(conf.empty_value)
        self.save_changes()
        self.assert_cm_neighbour_matching('true')
        
        logger.debug('RfPage :Setting rf arm client control cm neighbor matching with 150')
        self.set_rf_arm_client_control_cm_neighbor_matching(conf.new_cm_neighbour_matching_value)
        self.save_changes()
        self.assert_cm_neighbour_matching('true')
        
        logger.debug('RfPage :Setting rf arm client control cm neighbor matching with 100')
        self.set_rf_arm_client_control_cm_neighbor_matching(conf.cm_neighbour_matching_boundry_value)
        self.click_on_cm_neighbour_matching_style()
        self.assert_cm_neighbour_matching('false')
        
        logger.debug('RfPage :Setting rf arm client control cm neighbor matching with 0')
        self.set_rf_arm_client_control_cm_neighbor_matching(conf.zero_cm_neighbour_matching_boundry)
        self.save_changes()
        self.assert_cm_neighbour_matching('true')
        
        logger.debug('RfPage :Setting rf arm client control cm neighbor matching with zero_preceding values')
        self.set_rf_arm_client_control_cm_neighbor_matching(conf.zero_preceding_cm_neighbour_matching)
        self.save_changes()
        self.assert_cm_neighbour_matching('true')
        
        logger.debug('RfPage :Setting rf arm client control cm neighbor matching with 1')
        self.set_rf_arm_client_control_cm_neighbor_matching(conf.one_cm_neighbour_matching)
        self.click_on_cm_neighbour_matching_style()
        self.assert_cm_neighbour_matching('false')
        
        logger.debug('RfPage :Setting rf arm client control cm neighbor matching with string value')
        self.set_rf_arm_client_control_cm_neighbor_matching(conf.string_cm_neighbour_matching)
        self.save_changes()
        self.assert_cm_neighbour_matching('true')
        
    def validating_client_control_cm_threshold(self):
        conf = self.config.config_vars
        logger.debug('RfPage :Setting rf_arm_client_control_cm_threshold with empty values')
        self.set_rf_arm_client_control_cm_threshold(conf.empty_value)
        self.save_changes()
        self.assert_cm_threshold('true')
        
        logger.debug('RfPage :Setting rf_arm_client_control_cm_threshold to 22')
        self.set_rf_arm_client_control_cm_threshold(conf.new_cm_threshold_value)
        self.save_changes()
        self.assert_cm_threshold('true')
        
        logger.debug('RfPage :Setting rf_arm_client_control_cm_threshold to 20')  
        self.set_rf_arm_client_control_cm_threshold(conf.cm_threshold_value2)
        self.click_on_cm_neighbour_matching_style()
        self.assert_cm_threshold('false')
        
        logger.debug('RfPage :Setting rf_arm_client_control_cm_threshold with zero preceding values')
        self.set_rf_arm_client_control_cm_threshold(conf.zero_preceding_cm_threshold_value)
        self.save_changes()
        self.assert_cm_threshold('true')
        
        logger.debug('RfPage :Setting rf_arm_client_control_cm_threshold with string values')
        self.set_rf_arm_client_control_cm_threshold(conf.string_cm_threshold_value)
        self.save_changes()
        self.assert_cm_threshold('true')
        
        logger.debug('RfPage :Setting rf_arm_client_control_cm_threshold to 0')
        self.set_rf_arm_client_control_cm_threshold(conf.zero_cm_threshold_value)
        self.save_changes()
        self.assert_cm_threshold('true')
        
        logger.debug('RfPage :Setting rf_arm_client_control_cm_threshold  to 1')
        self.set_rf_arm_client_control_cm_threshold(conf.one_cm_threshold_value)
        self.click_on_cm_neighbour_matching_style()
        self.assert_cm_threshold('false')
        
    def assert_slb_mode_value1(self):
        logger.debug('RfPage : Asserting slb mode values')
        path = self.config.config_vars
        values_list = self.slb_mode.get_options()
        for value in values_list:
            if not (value == path.slb_mode_value or path.slb_mode_value_2nd or path.slb_mode_value_3rd):
                raise AssertionError("'SLB MODE' drop-down values not found i.e. Traceback: %s" %traceback.format_exc())
                
    def assert_save_cancel_button(self, save = True, cancel = True):
        if save:
            logger.debug("RFPage: Asserting Save Button ")
            self.browser.assert_element(self.save_button,'Save button is not displayed')    
        if cancel:
            logger.debug("RFPage: Asserting Cancel Button ")
            self.browser.assert_element(self.rf_cancel_button,'Cancel button is not displayed')    
            
            
    def check_multiversion_text_availablility(self,elem):
        logger.debug('RFPage:Checking for multiversion flag msg  ')
        time.sleep(10)
        self.browser.key_press(u'\ue009')
        self.browser.key_press( u'\ue00f')
        actions = self.browser.get_action_chain()
        actions.move_to_element(self.elem).perform()
        time.sleep(20)
        if not self.elem:
            raise AssertionError(" 'Supported in 6.3.1.2-4.0.0 and above' message is not visible i.e. Traceback: %s" %traceback.format_exc())
            
    def set_rf_arm_fields(self,set=False):
        '''
        Sets Rf ARM Fields
        '''
        if set:
            conf = self.config.config_vars
            self.set_rf_arm_client_control_band_sterring_mode(conf.band_streering_disable)
            self.set_rf_arm_access_point_control_wide_channel_bands(conf.new_wide_channel_bands_value)
            self.set_rf_arm_client_control_client_match(conf.new_client_match_value)
            self.set_rf_arm_client_control_slb_mode(conf.slb_mode_value_3rd)
            self.set_rf_arm_client_control_cm_calculating_interval(conf.vlanid)
            self.set_rf_arm_client_control_cm_neighbor_matching(conf.cm_calculating_interval_boundry_value1)
            self.set_rf_arm_client_control_cm_threshold(conf.new_cm_calculating_interval_value)
            self.set_rf_arm_access_point_control_max_transmit_power(conf.min_transmit_power_value)
            self.set_rf_arm_access_point_control_min_transmit_power(conf.new_max_transmit_power_value)
            self.set_rf_arm_access_point_control_customized_valid_channel(check='true')
            self.click_on_edit_24_ghz()
            self.channel_24ghz_7plus.click()
            self.channel_24ghz_11.click()
            self.click_on_edit_5_ghz()
            self.channel_5ghz_100.click()
            self.channel_5ghz_104.click()
            self.channel_5ghz_108.click()
            self.channel_5ghz_112.click()
            self.channel_5ghz_116.click()
            self.channel_5ghz_132.click()
            self.channel_5ghz_136.click()
            self.channel_5ghz_140.click()
            self.channel_5ghz_144.click()
            self.channel_5ghz_149.click()
            self.save_changes()
        else:
            self.set_rf_arm_client_control_band_sterring_mode(None)
            self.set_rf_arm_client_control_client_match(None)
            self.set_rf_arm_client_control_cm_calculating_interval(None)
            self.set_rf_arm_client_control_cm_neighbor_matching(None)
            self.set_rf_arm_client_control_cm_threshold(None)
            self.set_rf_arm_client_control_slb_mode(None)
            self.set_rf_arm_access_point_control_min_transmit_power(None)
            self.set_rf_arm_access_point_control_max_transmit_power(None)
            self.set_rf_arm_access_point_control_wide_channel_bands(None)
            self.set_rf_arm_access_point_control_customized_valid_channel(check=False)
        
    def assert_override_flag_button(self,check):
        '''
        Asserts Override flag Button
        '''
        if check == 'True':
            self.browser.assert_element(self.override_flag_button_new, 'Ovveride flag button is not present')
        if check == 'False':    
            self.browser.assert_element(self.override_flag_button_new, 'Ovveride flag button is not present', False)        
            
    def enable_custom_valid_channel_and_set(self):
        '''
        Sets 2.4Ghz 5 Ghz fields values
        '''
        self.click_on_edit_24_ghz()    
        self.channel_24ghz_6plus.click()
        self.channel_24ghz_6.click()
        self.click_on_edit_5_ghz()
        self.channel_5ghz_153.click()
        self.channel_5ghz_157.click()
        self.channel_5ghz_161.click()
        self.channel_5ghz_165.click()
        self.channel_5ghz_157plus.click()
            
    def click_on_override_flag(self):
        '''
        Clicks on Override Flag 
        '''
        logger.debug('Rf Page : Clicking Override Flag')
        self.self.override_flag_button_new.click()
        
    def click_on_resolve_all_overrides(self):
        '''
        Clicks on Resolve All overrides
        '''
        logger.debug('Rf Page : Clicking Resolve All')
        self.override_resolv_button.click()
            
    def aserts_overrides_diff(self):
        '''
        Asserts Changes made in Vc
        '''
        self.browser.assert_element(self.override_diff1, 'changes made in vc is not present')
        self.browser.assert_element(self.override_diff2, 'changes made in vc is not present')
        self.browser.assert_element(self.override_diff3, 'changes made in vc is not present')
        self.browser.assert_element(self.override_diff4, 'changes made in vc is not present')
        self.browser.assert_element(self.override_diff5, 'changes made in vc is not present')
        self.browser.assert_element(self.override_diff6, 'changes made in vc is not present')
        self.browser.assert_element(self.override_diff7, 'changes made in vc is not present')
    
    def click_on_close_overrides_overlay(self):
        '''
        Clicks on close overrides overlay
        '''
        logger.debug('Rf Page : Clicking on close overrides overlay ')
        self.close_overrides_overlay.click()
        
    def assert_min_max_transmit_power_for_country_us_and_in(self):
        time.sleep(10)
        logger.debug('RfPage : Get all options from min transmit power dropdown. ')
        options = self.min_transmit_power.get_options()
        s = 0
        for x in range(0,8):
            s = s+3
            if not options[x] == str(s):
                
                raise AssertionError(" option %s is missing.  i.e. Traceback: %s " %(options[x],traceback.format_exc()))
        options = self.max_transmit_power.get_options()
        s = 6
        for x in range(0,9):
            s = s+3
            if not options[x] == str(s):
                
                raise AssertionError(" option %s is missing.  i.e. Traceback: %s " %(options[x],traceback.format_exc()))
        if not options[9] == 'Max':
            raise AssertionError("Max option not present in max transmit power dropdown .i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_arm_configuration(self,ap,armconfig=''):
        '''
        Asser min and max transmit power values 
        '''
        # logger.debug("FirmwarePage : creating object of Device")
        myDevice = Device.getDeviceObject(ap)
        # logger.debug("FirmwarePage : splitting the firmware version")
        # logger.debug("FirmwarePage : waiting to receive prompt")
        myDevice.receive("#")
        # logger.debug("FirmwarePage : passing command 'show version' ")
        myDevice.transmit("show arm config")
        # logger.debug("FirmwarePage : waiting to receive prompt")
        output = myDevice.receive("#")
        if not armconfig in output:
            raise AssertionError("%s is not pushed to %s" %(armconfig,ap)) 

	def assert_slb_mode_multiversion(self,flag = False):
		logger.debug('RFPage:Checking for multiversion flag msg	 ')
		time.sleep(10)
		# actions = self.browser.get_action_chain()
		# actions.move_to_element(self.slb_mode_multiversion).perform()
		# time.sleep(20)
		if flag == True:
			if not self.slb_mode_multiversion:
				raise AssertionError(" 'Supported in 6.3.1.2-4.0.0 and above' message is not visible i.e. Traceback: %s" %traceback.format_exc())
		else :
			if self.slb_mode_multiversion:
				raise AssertionError(" 'Supported in 6.3.1.2-4.0.0 and above' message is visible i.e. Traceback: %s" %traceback.format_exc())

	def assert_arm_channels(self,ap,channel=''):
		'''
		Assert min and max transmit power values 
		'''
		logger.debug("RFPage : creating object of Device")
		myDevice = Device.getDeviceObject(ap)
		logger.debug("RFPage : waiting to receive prompt")
		myDevice.receive("#")
		logger.debug("RFPage : passing command 'show aem-channels' ")
		myDevice.transmit("show arm-channels")
		logger.debug("RFPage : waiting to receive prompt")
		output = myDevice.receive("#")
		if not channel in output:
			raise AssertionError("%s is not pushed to %s" %(channel,ap))  
				