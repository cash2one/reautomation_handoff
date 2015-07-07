from athenataf.lib.util.WebPage import WebPage
import logging
logger = logging.getLogger('athenataf')
import traceback
import time



class WidsPage(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "Wids", test, browser, config)
        self.test.assertPageLoaded(self)
        
    def isPageLoaded(self):
        if self.detect_omerta_attack_page:
            return True
        else:
            return False 
            
    def assert_detection_page_expanded(self):
        if self.detection_form:
            return True
        else:
            
            raise AssertionError("Detection page is not expanded i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_protection_page_collapsed(self):
        if not self.protection_form:
            return True
        else:
            
            raise AssertionError("Protection page is not collapsed i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_detection_infra_threat_detection_level_off(self):
        if self.detection_infrastructure_threat_off.is_selected():
            return True
        else:
            
            raise AssertionError("Infrastructure Threat Detection Level is not Off i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_detection_clients_threat_detection_level_off(self):
        if self.detection_clients_threat_off.is_selected():
            return True
        else:
            
            raise AssertionError("Clients Threat Detection Level is not Off i.e. Traceback: %s" %traceback.format_exc())
            
    def assert_detection_infrastructure_default_values(self):
        
        if not self.detect_windows_bridge:
            raise AssertionError("Infrastructure value 'detect_windows_bridge' in detection, not found i.e. Traceback: %s" %traceback.format_exc())
            
        if not self.signature_deassociation_broadcast:
            raise AssertionError("Infrastructure value 'signature_deassociation_broadcast' in detection, not found i.e. Traceback: %s" %traceback.format_exc())
            
        if not self.signature_deauth_broadcast:
            raise AssertionError("Infrastructure value 'signature_deauth_broadcast' in detection, not found i.e. Traceback: %s" %traceback.format_exc())
            
        if not self.detect_apspoofing:
            raise AssertionError("Infrastructure value 'detect_apspoofing' in detection, not found i.e. Traceback: %s" %traceback.format_exc())
            
        if not self.detect_adhoc_using_valid_ssid:
            raise AssertionError("Infrastructure value 'detect_adhoc_using_valid_ssid' in detection, not found i.e. Traceback: %s" %traceback.format_exc())    
            
        if not self.detect_malformed_large_duration:
            raise AssertionError("Infrastructure value 'detect_malformed_large_duration' in detection, not found i.e. Traceback: %s" %traceback.format_exc())    
            
        if not self.detect_overflow_eapol_key:
            raise AssertionError("Infrastructure value 'detect_overflow_eapol_key' in detection, not found i.e. Traceback: %s" %traceback.format_exc())    
            
        if not self.detect_invalid_addresscombination:
            raise AssertionError("Infrastructure value 'detect_invalid_addresscombination' in detection, not found i.e. Traceback: %s" %traceback.format_exc())    
            
        if not self.detect_ap_impersonation:
            raise AssertionError("Infrastructure value 'detect_ap_impersonation' in detection, not found i.e. Traceback: %s" %traceback.format_exc())    
            
        if not self.detect_ap_flood:
            raise AssertionError("Infrastructure value 'detect_ap_flood' in detection, not found i.e. Traceback: %s" %traceback.format_exc())    
            
        if not self.detect_beacon_wrong_channel:
            raise AssertionError("Infrastructure value 'detect_beacon_wrong_channel' in detection, not found i.e. Traceback: %s" %traceback.format_exc())    
            
        if not self.detect_ht_greenfield:
            raise AssertionError("Infrastructure value 'detect_ht_greenfield' in detection, not found i.e. Traceback: %s" %traceback.format_exc())    
            
        if not self.detect_overflow_ie:
            raise AssertionError("Infrastructure value 'detect_overflow_ie' in detection, not found i.e. Traceback: %s" %traceback.format_exc())    
            
        if not self.detect_rts_rate_anomaly:
            raise AssertionError("Infrastructure value 'detect_rts_rate_anomaly' in detection, not found i.e. Traceback: %s" %traceback.format_exc())    
            
        if not self.detect_malformed_htie:
            raise AssertionError("Infrastructure value 'detect_malformed_htie' in detection, not found i.e. Traceback: %s" %traceback.format_exc())    
            
        if not self.detect_cts_rate_anomaly:
            raise AssertionError("Infrastructure value 'detect_cts_rate_anomaly' in detection, not found i.e. Traceback: %s" %traceback.format_exc())    
            
        if not self.detect_malformed_frame_auth:
            raise AssertionError("Infrastructure value 'detect_malformed_frame_auth' in detection, not found i.e. Traceback: %s" %traceback.format_exc())    
            
        if not self.detect_invalid_mac_oui:
            raise AssertionError("Infrastructure value 'detect_invalid_mac_oui' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

        if not self.detect_malformed_assoc_req:
            raise AssertionError("Infrastructure value 'detect_malformed_assoc_req' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

        if not self.detect_bad_wep:
            raise AssertionError("Infrastructure value 'detect_bad_wep' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

        if not self.detect_wireless_bridge:
            raise AssertionError("Infrastructure value 'detect_wireless_bridge' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

        if not self.detect_ht_40mhz_intolerance:
            raise AssertionError("Infrastructure value 'detect_ht_40mhz_intolerance' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

        if not self.detect_valid_ssid_misuse:
            raise AssertionError("Infrastructure value 'detect_valid_ssid_misuse' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

        if not self.detect_adhoc_network:
            raise AssertionError("Infrastructure value 'detect_adhoc_network' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

        if not self.detect_client_flood:
            raise AssertionError("Infrastructure value 'detect_client_flood' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

    def assert_detection_clients_default_values(self):
        
        if not self.detect_valid_clientmisassociation:
            raise AssertionError("Clients value 'detect_valid_clientmisassociation' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

        if not self.detect_hotspotter_attack:
            raise AssertionError("Clients value 'detect_hotspotter_attack' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

        if not self.detect_power_save_dos_attack:
            raise AssertionError("Clients value 'detect_power_save_dos_attack' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

        if not self.detect_omerta_attack:
            raise AssertionError("Clients value 'detect_omerta_attack' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

        if not self.detect_disconnect_sta:
            raise AssertionError("Clients value 'detect_disconnect_sta' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

        if not self.detect_unencrypted_valid:
            raise AssertionError("Clients value 'detect_unencrypted_valid' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

        if not self.detect_block_ack_attack:
            raise AssertionError("Clients value 'detect_block_ack_attack' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

        if not self.detect_fatajack:
            raise AssertionError("Clients value 'detect_fatajack' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

        if not self.detect_rate_anomalies:
            raise AssertionError("Clients value 'detect_rate_anomalies' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

        if not self.detect_chopchop_attack:
            raise AssertionError("Clients value 'detect_chopchop_attack' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

        if not self.detect_eap_rate_anomaly:
            raise AssertionError("Clients value 'detect_eap_rate_anomaly' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

        if not self.detect_tkip_replay_attack:
            raise AssertionError("Clients value 'detect_tkip_replay_attack' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

        if not self.signature_airjack:
            raise AssertionError("Clients value 'signature_airjack' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

        if not self.signature_asleap:
            raise AssertionError("Clients value 'signature_asleap' in detection, not found i.e. Traceback: %s" %traceback.format_exc())

    def assert_detection_infrastructure_tick_icon(self , level):
        
        if level in ['Low' , 'Medium' , 'High']:
            if not self.detect_windows_bridge_tick:
                raise AssertionError("Infrastructure value 'detect_windows_bridge' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())
                
            if not self.signature_deassociation_broadcast_tick:
                raise AssertionError("Infrastructure value 'signature_deassociation_broadcast' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())
                
            if not self.signature_deauth_broadcast_tick:
                raise AssertionError("Infrastructure value 'signature_deauth_broadcast' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())
                
            if not self.detect_apspoofing_tick:
                raise AssertionError("Infrastructure value 'detect_apspoofing' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())
                
        if level in ['Medium' , 'High']:
            if not self.detect_adhoc_using_valid_ssid_tick:
                raise AssertionError("Infrastructure value 'detect_adhoc_using_valid_ssid' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    
                
            if not self.detect_malformed_large_duration_tick:
                raise AssertionError("Infrastructure value 'detect_malformed_large_duration' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())

        if level in ['High']:
            if not self.detect_overflow_eapol_key_tick:
                raise AssertionError("Infrastructure value 'detect_overflow_eapol_key' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    
                
            if not self.detect_invalid_addresscombination_tick:
                raise AssertionError("Infrastructure value 'detect_invalid_addresscombination' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    
                
            if not self.detect_ap_impersonation_tick:
                raise AssertionError("Infrastructure value 'detect_ap_impersonation' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())
                
            if not self.detect_ap_flood_tick:
                raise AssertionError("Infrastructure value 'detect_ap_flood' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    
                
            if not self.detect_beacon_wrong_channel_tick:
                raise AssertionError("Infrastructure value 'detect_beacon_wrong_channel' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    
                
            if not self.detect_ht_greenfield_tick:
                raise AssertionError("Infrastructure value 'detect_ht_greenfield' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    
                
            if not self.detect_overflow_ie_tick:
                raise AssertionError("Infrastructure value 'detect_overflow_ie' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    
                
            if not self.detect_rts_rate_anomaly_tick:
                raise AssertionError("Infrastructure value 'detect_rts_rate_anomaly' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    
                
            if not self.detect_malformed_htie_tick:
                raise AssertionError("Infrastructure value 'detect_malformed_htie' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    
                
            if not self.detect_cts_rate_anomaly_tick:
                raise AssertionError("Infrastructure value 'detect_cts_rate_anomaly' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    
                
            if not self.detect_malformed_frame_auth_tick:
                raise AssertionError("Infrastructure value 'detect_malformed_frame_auth' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    
                
            if not self.detect_invalid_mac_oui_tick:
                raise AssertionError("Infrastructure value 'detect_invalid_mac_oui' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())

            if not self.detect_malformed_assoc_req_tick:
                raise AssertionError("Infrastructure value 'detect_malformed_assoc_req' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())

            if not self.detect_bad_wep_tick:
                raise AssertionError("Infrastructure value 'detect_bad_wep' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())

            if not self.detect_wireless_bridge_tick:
                raise AssertionError("Infrastructure value 'detect_wireless_bridge' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())

            if not self.detect_ht_40mhz_intolerance_tick:
                raise AssertionError("Infrastructure value 'detect_ht_40mhz_intolerance' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())

            if not self.detect_valid_ssid_misuse_tick:
                raise AssertionError("Infrastructure value 'detect_valid_ssid_misuse' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())

            if not self.detect_adhoc_network_tick:
                raise AssertionError("Infrastructure value 'detect_adhoc_network' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())

            if not self.detect_client_flood_tick:
                raise AssertionError("Infrastructure value 'detect_client_flood' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())

    def set_detection_infra_threat_detection_level(self , level):
        if level == 'High':
            logger.debug('WIDS : Detection : Clicking detect infrastructure threat high')
            self.detection_infrastructure_threat_high.click()
        elif level == 'Medium':
            logger.debug('WIDS : Detection : Clicking detect infrastructure threat : medium')
            self.detection_infrastructure_threat_med.click()
        elif level == 'Low':
            logger.debug('WIDS : Detection : Clicking detect infrastructure threat : low')
            self.detection_infrastructure_threat_low.click()
        elif level == 'Off':
            logger.debug('WIDS : Detection : Clicking detect infrastructure threat : off')
            self.detection_infrastructure_threat_off.click()
        elif level == 'Custom':
            logger.debug('WIDS : Detection : Clicking detect infrastructure threat custom')
            self.detection_infrastructure_threat_custom.click()
            logger.debug('WIDS : Detection : Clicking detect invalid address combination')
            self.detect_invalid_addresscombination_chkbox.click()
            logger.debug('WIDS : Detection : Clicking detect ap impersonation')
            self.detect_ap_impersonation_chkbox.click()
        self.save_settings()

    def assert_detection_infra_custom_level(self):
        
        if not self.detect_invalid_addresscombination_chkbox.is_selected():
            raise AssertionError("'detect_invalid_addresscombination' check-box not selected i.e. Traceback: %s" %traceback.format_exc())
        if not self.detect_ap_impersonation_chkbox.is_selected():
            raise AssertionError("'detect_ap_impersonation' check-box not selected i.e. Traceback: %s" %traceback.format_exc())

    def set_detection_infra_custom_level_to_detect_apspoofing(self):
        logger.debug('WIDS : Detection : Clicking detect ap spoofing')
        self.detect_apspoofing_chkbox.click()
        self.save_settings()
        time.sleep(20)

    def click_detection_infra_tick_icon(self):
        if not self.detect_windows_bridge_tick.is_selected():
            logger.debug('WIDS : Detection : Clicking detect windows bridge')
            self.detect_windows_bridge_tick.click()
        if not self.signature_deassociation_broadcast_tick.is_selected():
            logger.debug('WIDS : Detection : Clicking signature deassociation broadcast')
            self.signature_deassociation_broadcast_tick.click()
        if not self.signature_deauth_broadcast_tick.is_selected():
            logger.debug('WIDS : Detection : Clicking signature deauth broadcast')
            self.signature_deauth_broadcast_tick.click()
        if not self.detect_apspoofing_tick.is_selected():
            logger.debug('WIDS : Detection : Clicking detect ap spoofing')
            self.detect_apspoofing_tick.click()

    def set_detection_clients_threat_detection_level(self , level):
        if level == 'High':
            logger.debug('WIDS : Detection : Clicking clients threat : high')
            self.detection_clients_threat_high.click()
        elif level == 'Medium':
            logger.debug('WIDS : Detection : Clicking clients threat : medium')
            self.detection_clients_threat_med.click()
        elif level == 'Low':
            logger.debug('WIDS : Detection : Clicking clients threat : low')
            self.detection_clients_threat_low.click()
        elif level == 'Off':
            logger.debug('WIDS : Detection : Clicking clients threat : off')
            self.detection_clients_threat_off.click()
        elif level == 'Custom':
            logger.debug('WIDS : Detection : Clicking clients threat : custom')
            self.detection_clients_threat_custom.click()
            logger.debug('WIDS : Detection : Clicking detect chopchop attack')
            self.detect_chopchop_attack_chkbox.click()
            logger.debug('WIDS : Detection : Clicking detect fatajack attack')
            self.detect_fatajack_chkbox.click()
        self.save_settings()
        time.sleep(20)

    def assert_detection_clients_tick_icon(self , level):
        
        if level in ['Low' , 'Medium' , 'High']:
            if not self.detect_valid_clientmisassociation_tick:
                raise AssertionError("Clients value 'detect_valid_clientmisassociation' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())
                
        if level in ['Medium' , 'High']:
            if not self.detect_hotspotter_attack_tick:
                raise AssertionError("Clients value 'detect_hotspotter_attack' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    
                
            if not self.detect_power_save_dos_attack_tick:
                raise AssertionError("Clients value 'detect_power_save_dos_attack' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())
                
            if not self.detect_omerta_attack_tick:
                raise AssertionError("Clients value 'detect_omerta_attack' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    
                
            if not self.detect_disconnect_sta_tick:
                raise AssertionError("Clients value 'detect_disconnect_sta' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    
                
            if not self.detect_unencrypted_valid_tick:
                raise AssertionError("Clients value 'detect_unencrypted_valid' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())
                
            if not self.detect_block_ack_attack_tick:
                raise AssertionError("Clients value 'detect_block_ack_attack' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    
                
            if not self.detect_fatajack_tick:
                raise AssertionError("Clients value 'detect_fatajack' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    
                
        if level in ['High']:
            if not self.detect_rate_anomalies_tick:
                raise AssertionError("Clients value 'detect_rate_anomalies' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    
                
            if not self.detect_chopchop_attack_tick:
                raise AssertionError("Clients value 'detect_chopchop_attack_tick' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    
                
            if not self.detect_eap_rate_anomaly_tick:
                raise AssertionError("Clients value 'detect_eap_rate_anomaly' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    
                
            if not self.detect_tkip_replay_attack_tick:
                raise AssertionError("Clients value 'detect_tkip_replay_attack' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    
                
            if not self.signature_airjack_tick:
                raise AssertionError("Clients value 'signature_airjack' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    
                
            if not self.signature_asleap_tick:
                raise AssertionError("Clients value 'signature_asleap' in detection, not selected i.e. Traceback: %s" %traceback.format_exc())    

    def assert_detection_clients_custom_level(self):
        
        if not self.detect_chopchop_attack_chkbox.is_selected():
            raise AssertionError("'detect_chopchop_attack' check-box not selected i.e. Traceback: %s" %traceback.format_exc())
        if not self.detect_fatajack_chkbox.is_selected():
            raise AssertionError("'detect_fatajack' check-box not selected i.e. Traceback: %s" %traceback.format_exc())
        
    def set_detection_clients_custom_level_to_detect_omerta_attack(self):
        logger.debug('WIDS : Detection : Clicking detect omerta attack')
        self.detect_omerta_attack_chkbox.click()
        self.save_settings()
        time.sleep(20)
        
    def assert_detect_omerta_attack(self):
        if not self.detect_omerta_attack_chkbox.is_selected():
            
            raise AssertionError("'detect_omerta_attack' check-box not selected i.e. Traceback: %s" %traceback.format_exc())
            
    def click_detection_clients_tick_icon(self , level = None):
        if level == 'Low':
            logger.debug('WIDS : Detection : Clicking detect valid client mis association')
            self.detect_valid_clientmisassociation_tick.click()
        else:
            logger.debug('WIDS : Detection : Clicking detect hot spotter attack')
            self.detect_hotspotter_attack_tick.click()
            logger.debug('WIDS : Detection : Clicking detect power save dos attack')
            self.detect_power_save_dos_attack_tick.click()
            logger.debug('WIDS : Detection : Clicking detect omerta attack')
            self.detect_omerta_attack_tick.click()
            
    def assert_threat_detection_level_text(self):
        if not (self.threat_detection_level_text_infra and self.threat_detection_level_text_client):
            
            raise AssertionError("'THREAT DETECTION LEVEL' text not found i.e. Traceback: %s" %traceback.format_exc())


    def save_settings(self):
        time.sleep(5)
        try:
            logger.debug('WIDS :  Clicking Save settings button')
            if self.save:
                logger.debug('WIDS :  Clicking Save settings button')
                self.save.click()
                time.sleep(5)
        except:
            pass
        
    def assert_wids_protection_section_expanded(self):
        logger.debug('WIDS : Protection : Clicking Protection accordion')
        self.protection_accordion.click()
        if not self.protection_section:
            
            raise AssertionError("Wids protection section not expanded  i.e. Traceback: %s" %traceback.format_exc())
        
    def assert_threat_protection_level(self):
        
        if not self.infra_protect_off.is_selected():
            raise AssertionError("Off option button for infrastructure not enabled . i.e. Traceback: %s" %traceback.format_exc())
        if not self.client_protect_off.is_selected():
            raise AssertionError("Off option button for client not enabled .  i.e. Traceback: %s" %traceback.format_exc())
        
    def assert_all_attactks_infrastructure_client(self):
        
        if not self.rogue_containment:
            raise AssertionError("Infrastructure THREAT PROTECTION LEVEL 'rogue_containment' in protection, not listed i.e. Traceback: %s" %traceback.format_exc())    
            
        if not self.protect_ssid:
            raise AssertionError("Infrastructure THREAT PROTECTION LEVEL 'protect_ssid' in protection, not listed i.e. Traceback: %s" %traceback.format_exc())    
            
        if not self.protect_ap_impersonation:
            raise AssertionError("Infrastructure THREAT PROTECTION LEVEL 'protect_ap_impersonation' in protection, not listed i.e. Traceback: %s" %traceback.format_exc())    
            
        if not self.protect_adhoc_network:
            raise AssertionError("Infrastructure THREAT PROTECTION LEVEL 'protect_adhoc_network' in protection, not listed i.e. Traceback: %s" %traceback.format_exc())    
            
        if not self.protect_valid_sta_checked:
            raise AssertionError("Client  THREAT PROTECTION LEVEL 'protect_valid_sta' in protection, not listed i.e. Traceback: %s" %traceback.format_exc())    
            
        if not self.protect_windows_bridge:
            raise AssertionError("Client THREAT PROTECTION LEVEL 'protect_windows_bridge' in protection, not listed i.e. Traceback: %s" %traceback.format_exc())
        if not self.wired_containment.selected == 'Off':
            raise AssertionError(" Wired containment is not 'Off' by default. i.e. Traceback: %s" %traceback.format_exc())
        if not self.wireless_containment.selected == 'None':
            raise AssertionError("Wireless containment is not 'None' by default .  i.e. Traceback: %s" %traceback.format_exc())    

    def assert_containment_methods(self):
        logger.debug('WIDS : Protection : Clicking Protection accordion')
        self.protection_accordion.click()
        
        if not self.wired_containment.selected == 'Off':
            raise AssertionError(" Wired containment is not 'Off' by default. i.e. Traceback: %s" %traceback.format_exc())
        if not self.wireless_containment.selected == 'None':
            raise AssertionError("Wireless containment is not 'None' by default .  i.e. Traceback: %s" %traceback.format_exc())
        
        
    def assert_infrastructure_protection_high_checked(self):
        
        logger.debug('WIDS : Protection : Clicking Protection accordion')
        self.protection_accordion.click()
        logger.debug('WIDS : Protection : Clicking Infra Protect : high')
        self.infra_protect_high.click()
        if not self.rogue_containment_checked:
            raise AssertionError("Infrastructure THREAT PROTECTION LEVEL 'rogue_containment' in protection, not listed i.e. Traceback: %s" %traceback.format_exc())    
        
        if not self.protect_ssid_checked:
            raise AssertionError("Infrastructure THREAT PROTECTION LEVEL 'protect_ssid' in protection, not listed i.e. Traceback: %s" %traceback.format_exc())    
        
        if not self.protect_ap_impersonation_checked:
            raise AssertionError("Infrastructure THREAT PROTECTION LEVEL 'protect_ap_impersonation' in protection, not listed i.e. Traceback: %s" %traceback.format_exc())    
        
        if not self.protect_adhoc_network_checked:
            raise AssertionError("Infrastructure THREAT PROTECTION LEVEL 'protect_adhoc_network' in protection, not listed i.e. Traceback: %s" %traceback.format_exc())
        self.save_settings()
        time.sleep(20)
        
        
    def revert_infrastructure_default_settings(self):
        logger.debug('WIDS : Protection : Clicking Infra Protect : off')
        self.infra_protect_off.click()
        self.save_settings()
        time.sleep(20)
        
    def assert_infrastructure_protection_low_checked(self):
        
        logger.debug('WIDS : Protection : Clicking Protection accordion')
        self.protection_accordion.click()
        logger.debug('WIDS : Protection : Clicking Infra Protect : low')
        self.infra_protect_low.click()
        if not self.rogue_containment_checked:
            raise AssertionError("Infrastructure THREAT PROTECTION LEVEL 'rogue_containment' in protection, not listed i.e. Traceback: %s" %traceback.format_exc())    
        
        if not self.protect_ssid_checked:
            raise AssertionError("Infrastructure THREAT PROTECTION LEVEL 'protect_ssid' in protection, not listed i.e. Traceback: %s" %traceback.format_exc())    
        self.save_settings()
        time.sleep(20)
        
    def assert_infrastructure_protection_off_unchecked(self):
        
        logger.debug('WIDS : Protection : Clicking Protection accordion')
        self.protection_accordion.click()
        logger.debug('WIDS : Protection : Clicking Infra Protect : off')
        self.infra_protect_off.click()
        if self.rogue_containment_unchecked:
            raise AssertionError("Infrastructure THREAT PROTECTION LEVEL 'rogue_containment' in protection, checked. i.e. Traceback: %s" %traceback.format_exc())    
        
        if self.protect_ssid_unchecked:
            raise AssertionError("Infrastructure THREAT PROTECTION LEVEL 'protect_ssid' in protection, checked. i.e. Traceback: %s" %traceback.format_exc())
            
        if self.protect_ap_impersonation_unchecked:
            raise AssertionError("Infrastructure THREAT PROTECTION LEVEL 'protect_ap_impersonation' in protection, checked.d i.e. Traceback: %s" %traceback.format_exc())    
        
        if self.protect_adhoc_network_unchecked:
            raise AssertionError("Infrastructure THREAT PROTECTION LEVEL 'protect_adhoc_network' in protection, checked. i.e. Traceback: %s" %traceback.format_exc())    
        if self.save:
            logger.debug('WIDS : Protection : Clicking save button')
            self.save.click()
             
            time.sleep(6)
        
    def revert_clients_default_settings(self):
        logger.debug('WIDS : Protection : Clicking Protect : off')
        self.client_protect_off.click()
        self.save_settings()
        time.sleep(20)
        
    def assert_clients_protection_high_checked(self):
        
        logger.debug('WIDS : Protection : Clicking Protection accordion')
        self.protection_accordion.click()
        logger.debug('WIDS : Protection : Clicking Protect : high')
        self.client_protect_high.click()
        if not self.protect_valid_sta_checked:
            raise AssertionError("Client  THREAT PROTECTION LEVEL 'protect_valid_sta' in protection, not listed i.e. Traceback: %s" %traceback.format_exc())    
            
        if not self.protect_windows_bridge:
            raise AssertionError("Client THREAT PROTECTION LEVEL 'protect_windows_bridge' in protection, not listed i.e. Traceback: %s" %traceback.format_exc())    
        self.save_settings()
        time.sleep(20)
        
    def assert_clients_protection_low_checked(self):
        
        logger.debug('WIDS : Protection : Clicking Protection accordion')
        self.protection_accordion.click()
        logger.debug('WIDS : Protection : Clicking Protect low')
        self.client_protect_low.click()
        if not self.protect_valid_sta_checked:
            raise AssertionError("Client  THREAT PROTECTION LEVEL 'protect_valid_sta' in protection, not listed i.e. Traceback: %s" %traceback.format_exc())    
        self.save_settings()
        
    def wireless_containment_deauthenticate(self):
        
        logger.debug('WIDS : Protection : Clicking Protection accordion')
        self.protection_accordion.click()
        logger.debug('WIDS : Protection : Writing wireless containment : Deauthenticate ')
        self.wireless_containment.set(self.config.config_vars.Wireless_Containment_Deauthenticate)
        if not self.restore_default:
            raise AssertionError(" Default recommended settings link not displayed.  i.e. Traceback: %s" %traceback.format_exc())
        if not self.default_setting_msg:
            raise AssertionError(" Default recommended settings message not displayed.  i.e. Traceback: %s" %traceback.format_exc())
        self.save_settings()
        time.sleep(6)
        
    def wired_containment_on(self):
        
        logger.debug('WIDS : Protection : Clicking Protection accordion')
        self.protection_accordion.click()
        logger.debug('WIDS : Protection : Writing wired containment : on ')
        self.wired_containment.set(self.config.config_vars.Wired_Containment_On)
        self.save_settings()
        if not self.restore_default:
            raise AssertionError(" Default recommended settings link not displayed.  i.e. Traceback: %s" %traceback.format_exc())
        if not self.default_setting_msg:
            raise AssertionError(" Default recommended settings message not displayed.  i.e. Traceback: %s" %traceback.format_exc())
        
        
    def wireless_tarpit_invalid(self):
        
        logger.debug('WIDS : Protection : Clicking Protection accordion')
        self.protection_accordion.click()
        logger.debug('WIDS : Protection : Writing wireless containment : Deauthenticate ')
        self.wireless_containment.set(self.config.config_vars.Wireless_Containment_Deauthenticate)
        logger.debug('WIDS : Protection : Writing wireless containment : Tarpit_Invalid ')
        self.wireless_containment.set(self.config.config_vars.Wireless_Containment_Tarpit_Invalid)
        self.save_settings()
        if not self.restore_default:
            raise AssertionError(" Default recommended settings link not displayed.  i.e. Traceback: %s" %traceback.format_exc())
        if not self.default_setting_msg:
            raise AssertionError(" Default recommended settings message not displayed.  i.e. Traceback: %s" %traceback.format_exc())
        
    def wireless_tarpit_all(self):
        
        logger.debug('WIDS : Protection : Clicking Protection accordion')
        self.protection_accordion.click()
        logger.debug('WIDS : Protection : Writing wireless containment : Tarpit_Invalid ')
        self.wireless_containment.set(self.config.config_vars.Wireless_Containment_Tarpit_Invalid)
        logger.debug('WIDS : Protection : Writing wireless containment : Tarpit_All ')
        self.wireless_containment.set(self.config.config_vars.Wireless_Containment_Tarpit_All)
        self.save_settings()
        if not self.restore_default:
            raise AssertionError(" Default recommended settings link not displayed.  i.e. Traceback: %s" %traceback.format_exc())
        if not self.default_setting_msg:
            raise AssertionError(" Default recommended settings message not displayed.  i.e. Traceback: %s" %traceback.format_exc())
        
    def restore_defaults_containment_methods(self):
        
        logger.debug('WIDS : Protection : Clicking Protection accordion')
        self.protection_accordion.click()
        logger.debug('WIDS : Protection : Writing wireless containment ')
        self.wireless_containment.set(self.config.config_vars.Wireless_Containment_Tarpit_All)
        self.save_settings()
        if not self.restore_default:
            raise AssertionError(" Default recommended settings link not displayed.  i.e. Traceback: %s" %traceback.format_exc())
        if not self.default_setting_msg:
            raise AssertionError(" Default recommended settings message not displayed.  i.e. Traceback: %s" %traceback.format_exc())
        logger.debug('WIDS : Protection : Clicking restore default ')
        self.restore_default.click()
        self.save_settings()
        if not self.wired_containment.selected == 'Off':
            raise AssertionError(" Wired containment is not 'Off' by default. i.e. Traceback: %s" %traceback.format_exc())
        if not self.wireless_containment.selected == 'None':
            raise AssertionError("Wireless containment is not 'None' by default .  i.e. Traceback: %s" %traceback.format_exc())
        
        if self.restore_default:
            raise AssertionError(" Default recommended settings link is displayed.  i.e. Traceback: %s" %traceback.format_exc())
        if self.default_setting_msg:
            raise AssertionError(" Default recommended settings message is displayed.  i.e. Traceback: %s" %traceback.format_exc())
        
    def assert_threat_protection_tab(self):
        
        logger.debug('WIDS : Protection : Clicking Protection accordion')
        self.protection_accordion.click()
        if not self.infrastructure_threat_protection_level:
            raise AssertionError("Threat protection level text not displayed below infrastucture settings.  i.e. Traceback: %s" %traceback.format_exc())
        if not self.client_threat_protection_level:
            raise AssertionError("Threat protection level text not displayed below clients settings.  i.e. Traceback: %s" %traceback.format_exc())
            
    def protection_tab_clients_off(self):
        
        logger.debug('WIDS : Protection : Clicking Protection accordion')
        self.protection_accordion.click()
        logger.debug('WIDS : Protection : Clicking client protect high')
        self.client_protect_high.click()
        logger.debug('WIDS : Protection : Clicking client protect off')
        self.client_protect_off.click()
        if self.protect_valid_sta_edit:
            raise AssertionError(" Protection type protect_ap_impersonation_edit edit mode on i.e. Traceback: %s" %traceback.format_exc())    
        
        if self.protect_windows_bridge_edit:
            raise AssertionError("Protection type protect_adhoc_network_edit edit mode on i.e. Traceback: %s" %traceback.format_exc())    
        self.save_settings()
        time.sleep(20)        
            
    def clients_custom_settings(self):
        
        logger.debug('WIDS : Protection : Clicking Protection accordion')
        self.protection_accordion.click()
        logger.debug('WIDS : Protection : Clicking client protect custom')
        self.client_protect_custom.click()
        
        if self.protect_valid_sta_edit.is_selected():
            raise AssertionError(" Protection type protect_ap_impersonation_edit edit mode off i.e. Traceback: %s" %traceback.format_exc())    
        
        if self.protect_windows_bridge_edit.is_selected():
            raise AssertionError("Protection type protect_adhoc_network_edit edit mode off i.e. Traceback: %s" %traceback.format_exc())
        
        logger.debug('WIDS : Protection : Clicking protect windows bridge edit button')
        self.protect_windows_bridge_edit.click()
        self.save_settings()
        logger.debug('WIDS : Protection : Clicking client protect off')
        self.client_protect_off.click()
        logger.debug('WIDS : Protection : Clicking client protect custom')
        self.client_protect_custom.click()
        
        time.sleep(5)    
        if not self.protect_windows_bridge_enabled.is_selected():
            raise AssertionError("Protection type protect_windows_bridge_edit edit mode is not enabled i.e. Traceback: %s" %traceback.format_exc())
        logger.debug('WIDS : Protection : Clicking windows bridge enabled ')
        self.protect_windows_bridge_enabled.click()
        logger.debug('WIDS : Protection : Clicking protect valid sta')
        self.protect_valid_sta_edit.click()
        self.save_settings()
        time.sleep(20)
        
    def infrastructure_custom_settings(self):
        
        logger.debug('WIDS : Protection : Clicking Protection accordion')
        self.protection_accordion.click()
        logger.debug('WIDS : Protection : Clicking infrastructure custom')
        self.infrastructure_protect_custom.click()
        
        if self.rogue_containment.is_selected():
            raise AssertionError("Infrastructure THREAT PROTECTION LEVEL 'rogue_containment' in protection, checked. i.e. Traceback: %s" %traceback.format_exc())    
        
        if self.protect_ssid.is_selected():
            raise AssertionError("Infrastructure THREAT PROTECTION LEVEL 'protect_ssid' in protection, checked. i.e. Traceback: %s" %traceback.format_exc())
            
        if self.protect_ap_impersonation.is_selected():
            raise AssertionError("Infrastructure THREAT PROTECTION LEVEL 'protect_ap_impersonation' in protection, checked.d i.e. Traceback: %s" %traceback.format_exc())    
        
        if self.protect_adhoc_network.is_selected():
            raise AssertionError("Infrastructure THREAT PROTECTION LEVEL 'protect_adhoc_network' in protection, checked. i.e. Traceback: %s" %traceback.format_exc())    
            
        logger.debug('WIDS : Protection : Clicking rogue containment edit')
        self.rogue_containment_edit.click()
        logger.debug('WIDS : Protection : Clicking Protection adhoc network edit button')
        self.protect_adhoc_network_edit.click()
        self.save_settings()
        logger.debug('WIDS : Protection : Clicking Client Protection off checkbox')
        self.client_protect_off.click()
        logger.debug('WIDS : Protection : Clicking infrastructure Protect custom checkbox')
        self.infrastructure_protect_custom.click()
        
        time.sleep(5)    
        if not self.rogue_containment_enabled.is_selected():
            raise AssertionError("Protection type rogue_containment edit mode is not enabled i.e. Traceback: %s" %traceback.format_exc())
        if not self.protect_adhoc_network_enabled.is_selected():
            raise AssertionError("Protection type protect_adhoc_network edit mode is not enabled i.e. Traceback: %s" %traceback.format_exc())
        logger.debug('WIDS : Protection : Clicking rogue containment checkbox')
        self.rogue_containment_enabled.click()
        logger.debug('WIDS : Protection : Clicking protect adhoc network checkbox')
        self.protect_adhoc_network_enabled.click()
        logger.debug('WIDS : Protection : Clicking protect ap impersonation edit checkbox')
        self.protect_ap_impersonation_edit.click()
        self.save_settings()
        time.sleep(20)
        
    def infrastructure_custom_changes(self):        
        logger.debug('WIDS : Detection : Clicking invalid address combination checkbox')
        self.detect_invalid_addresscombination_chkbox.click()
        logger.debug('WIDS : DEtection : Clicking ap impersonation checkbox')
        self.detect_ap_impersonation_chkbox.click()
        if not self.detect_apspoofing_chkbox.is_selected():
            logger.debug('WIDS : Detection : Clicking ap spoofing checkbox')
            self.detect_apspoofing_chkbox.click()
        self.save_settings()
        # self.set_detection_infra_threat_detection_level('Off')
        
    def click_high_protection_infra_tick_icon(self):
        logger.debug('WIDS : Protection : Clicking infra protect high checkbox')
        self.infra_protect_high.click()
        logger.debug('WIDS : Protection : Clicking rogue containment checkbox')
        self.rogue_containment_checked.click()
        logger.debug('WIDS : Protection : Clicking protect ssid checkbox')
        self.protect_ssid_checked.click()
        logger.debug('WIDS : Protection : Clicking ap impersonation checkbox')
        self.protect_ap_impersonation_checked.click()
        # self.revert_infrastructure_default_settings()
        
    def click_low_protection_infra_tick_icon(self):
        logger.debug('WIDS : Protection : Clicking infra protect low checkbox')
        self.infra_protect_low.click()
        logger.debug('WIDS : Protection : Clicking protect ssid checkbox')
        self.protect_ssid_checked.click()
        logger.debug('WIDS : Protection : Clicking rogue containment checkbox')
        self.rogue_containment_checked.click()
        # self.revert_infrastructure_default_settings()
        
    def click_low_protection_client_tick_icon(self):
        logger.debug('WIDS : Protection : Clicking client protect low checkbox')
        self.client_protect_low.click()
        logger.debug('WIDS : Protection : Clicking valid sta checkbox')
        self.protect_valid_sta_checked.click()
        
    def click_high_protection_client_tick_icon(self):
        logger.debug('WIDS : Protection : Clicking client protect high checkbox')
        self.client_protect_high.click()
        logger.debug('WIDS : Protection : Clicking valid sta checkbox')
        self.protect_valid_sta_checked.click()
        # self.revert_clients_default_settings()

    def restore_default_ui(self):
        
        time.sleep(5)
        logger.debug('WIDS :  Clicking restore default ')
        self.restore_default.click()
        self.save_settings()
        time.sleep(20)
        
    def set_detection_clients_threat_detection_level_custom_with_changes(self , level):
        if level == 'High':
            logger.debug('WIDS : Detection : Clicking clients threat high checkbox')
            self.detection_clients_threat_high.click()
        elif level == 'Medium':
            logger.debug('WIDS : Detection : Clicking clients threat medium checkbox')
            self.detection_clients_threat_med.click()
        elif level == 'Low':
            logger.debug('WIDS : Detection : Clicking clients threat medium checkbox')
            self.detection_clients_threat_low.click()
        elif level == 'Off':
            logger.debug('WIDS : Detection : Clicking disconnect sta checkbox')
            self.detection_clients_threat_off.click()
        elif level == 'Custom':
            logger.debug('WIDS : Detection : Clicking clients threat custom')
            self.detection_clients_threat_custom.click()
            logger.debug('WIDS : Detection : Clicking save dos attack')
            self.detect_power_save_dos_attack_chbox.click()
            logger.debug('WIDS : Detection : Clicking tkip replay attack checkbox')
            self.detect_tkip_replay_attack_chbox.click()
        self.save_settings()
        time.sleep(20)

    def set_detection_clients_custom_level_to_detect_disconnect_sta(self):
        logger.debug('WIDS : Detection : Clicking disconnect sta checkbox')
        self.detect_disconnect_sta_chbox.click()
        self.save_settings()
        time.sleep(20)

    def assert_detection_clients_level_custom_with_changes(self):
        
        if not self.detect_power_save_dos_attack_chbox.is_selected():
            raise AssertionError("'detect_power_save_dos_attack' check-box not selected i.e. Traceback: %s" %traceback.format_exc())
        if not self.detect_tkip_replay_attack_chbox.is_selected():
            raise AssertionError("'detect_tkip_replay_attack' check-box not selected i.e. Traceback: %s" %traceback.format_exc())

    def assert_detect_disconnect_sta(self):
        if not self.detect_disconnect_sta_chbox.is_selected():
            
            raise AssertionError("'detect_disconnect_sta' check-box not selected i.e. Traceback: %s" %traceback.format_exc())
    
    def set_infra_client_high(self):
        logger.debug('WidsPage : Clicking protection accordion')
        self.protection_accordion.click()
        logger.debug('WidsPage : Clicking infra protect: high')
        self.infra_protect_high.click()
        logger.debug('WidsPage : Clicking client protect: high')
        self.client_protect_high.click()
        self.save_settings()
        time.sleep(20)
        
    def assert_infra_client_high(self):
        
        if not self.infra_protect_high.is_selected():
            raise AssertionError("Infrastructure protect high is not selected i.e. Traceback: %s" %traceback.format_exc())
        if not self.client_protect_high.is_selected():
            raise AssertionError("Client protect low is high selected i.e. Traceback: %s" %traceback.format_exc())
        
    def set_infra_client_low(self):
        logger.debug('WidsPage : Clicking protection accordion')
        self.protection_accordion.click()
        logger.debug('WidsPage : Clicking infrastructure protect: low')
        self.infra_protect_low.click()
        logger.debug('WidsPage : Clicking client protect: low')
        self.client_protect_low.click()
        self.save_settings()
        time.sleep(20)
        
    def assert_infra_client_low(self):
        
        if not self.infra_protect_low.is_selected():
            raise AssertionError("Infrastructure protect low is not selected i.e. Traceback: %s" %traceback.format_exc())
        if not self.client_protect_low.is_selected():
            raise AssertionError("Client protect low is not selected i.e. Traceback: %s" %traceback.format_exc())
        
    def set_infra_client_custom(self):
        logger.debug('WidsPage : Clicking protection accordion')
        self.protection_accordion.click()
        logger.debug('WidsPage : Clicking infrastructure protect custom')
        self.infrastructure_protect_custom.click()
        logger.debug('WidsPage : Clicking protect ap impersonation')
        self.protect_ap_impersonation_checkbox.click()
        logger.debug('WidsPage : Clicking protect adhoc network')
        self.protect_adhoc_network_checkbox.click()
        logger.debug('WidsPage : Clicking client protect custom')
        self.client_protect_custom.click()
        logger.debug('WidsPage : Clicking protect windows bridge')
        self.protect_protect_windows_bridge_checkbox.click()
        self.save_settings()
        time.sleep(20)
        
    def assert_infra_client_custom(self):
        
        if not self.infrastructure_protect_custom.is_selected():
            raise AssertionError("Infrastructure protect custom is not selected i.e. Traceback: %s" %traceback.format_exc())
        if not self.protect_ap_impersonation_checkbox.is_selected():
            raise AssertionError("Infrastructure protect ap impersonation is not checked i.e. Traceback: %s" %traceback.format_exc())
        if not self.protect_adhoc_network_checkbox.is_selected():
            raise AssertionError("Infrastructure protect adhoc network is not checked i.e. Traceback: %s" %traceback.format_exc())
        if not self.client_protect_custom.is_selected():
            raise AssertionError("Client protect custom is not selected i.e. Traceback: %s" %traceback.format_exc())
        if not self.protect_protect_windows_bridge_checkbox.is_selected():
            raise AssertionError("Client protect windows bridge is not selected i.e. Traceback: %s" %traceback.format_exc())
        
    def set_infra_client_custom_negative(self):
        logger.debug('WidsPage : Clicking protection accordion')
        self.protection_accordion.click()
        logger.debug('WidsPage : Clicking infrastructure protect custom')
        self.infrastructure_protect_custom.click()
        logger.debug('WidsPage : Clicking rogue containment')
        self.rogue_containment_checkbox.click()
        logger.debug('WidsPage : Clicking protect ssid')
        self.protect_ssid_checkbox.click()
        logger.debug('WidsPage : Clicking client protect custom')
        self.client_protect_custom.click()
        logger.debug('WidsPage : Clicking protect valid sta edit button')
        self.protect_valid_sta_edit.click()
        self.save_settings()
        logger.debug('WidsPage : Clicking infra protect low')
        self.infra_protect_low.click()
        logger.debug('WidsPage : Clicking client protect low')
        self.client_protect_low.click()
        self.save_settings()
        logger.debug('WidsPage : Clicking infra protect off')
        self.infra_protect_off.click()
        logger.debug('WidsPage : Clicking client protect off')
        self.client_protect_off.click()
        self.save_settings()
        logger.debug('WidsPage : Clicking infrastructure protect custom')
        self.infrastructure_protect_custom.click()
        logger.debug('WidsPage : Clicking client protect custom')
        self.client_protect_custom.click()
        self.save_settings()
        time.sleep(20)
        
    def assert_infra_client_custom_negative(self):
        
        if not self.infrastructure_protect_custom.is_selected():
            raise AssertionError("Infrastructure protect custom is not selected i.e. Traceback: %s" %traceback.format_exc())
        if not self.client_protect_custom.is_selected():
            raise AssertionError("Client protect custom is not selected i.e. Traceback: %s" %traceback.format_exc())
        
    def set_infra_client_custom_default(self):
        logger.debug('WidsPage : Clicking protection accordion')
        self.protection_accordion.click()
        logger.debug('WidsPage : Clicking infra protect off')
        self.infra_protect_off.click()
        logger.debug('WidsPage : Clicking client protect off')
        self.client_protect_off.click()
        self.save_settings()
        time.sleep(20)
        
    def set_infra_client_default(self):
        logger.debug('WidsPage : Clicking protection accordion')
        self.protection_accordion.click()
        logger.debug('WidsPage : Clicking infra protect off')
        self.infra_protect_off.click()
        logger.debug('WidsPage : Clicking client protect off')
        self.client_protect_off.click()
        self.save_settings()
        time.sleep(20)
        
    def edit_infra_client_protection_level(self):
        
        logger.debug('WidsPage : Clicking protection accordion')
        self.protection_accordion.click()
        logger.debug('WidsPage : Clicking infra protect high')
        self.infra_protect_high.click()
        if not self.rogue_containment_checked:
            raise AssertionError("Rough containment is not enabled i.e. Traceback: %s" %traceback.format_exc())
        if not self.protect_ssid_checked:
            raise AssertionError("Protect ssid is not enabled i.e. Traceback: %s" %traceback.format_exc())
        if not self.protect_ap_impersonation_checked:
            raise AssertionError("Protect ap impersonation is not enabled i.e. Traceback: %s" %traceback.format_exc())
        if not self.protect_adhoc_network_checked:
            raise AssertionError("Protect adhoc network is not enabled i.e. Traceback: %s" %traceback.format_exc())
        self.client_protect_high.click()
        if not self.protect_valid_sta_checked:
            raise AssertionError("Protect valid sta is not enabled i.e. Traceback: %s" %traceback.format_exc())
        if not self.protect_windows_bridge_checked:
            raise AssertionError("Protect windows bridge is not enabled i.e. Traceback: %s" %traceback.format_exc())
        self.client_protect_low.click()
        if not self.protect_valid_sta_checked:
            raise AssertionError("Protect valid sta is not enabled i.e. Traceback: %s" %traceback.format_exc())
        self.save_settings()
        time.sleep(20)
        
    def set_infra_client_protection_level_default(self):
        logger.debug('WidsPage : Clicking infra protect off')
        self.infra_protect_off.click()
        logger.debug('WidsPage : Clicking client protect off')
        self.client_protect_off.click()
        self.save_settings()
        time.sleep(20)
        
    def set_wireless_containment(self):
        logger.debug('WidsPage : Clicking protection accordion')
        self.protection_accordion.click()    
        logger.debug('WidsPage : Writing wireless containment')
        self.wireless_containment.set(self.config.config_vars.Wireless_Containment_Deauthenticate)
        self.save_settings()
        if not self.config.config_vars.Wireless_Containment_Deauthenticate == self.wireless_containment.get_selected():
            raise AssertionError("Wireless containment is not selected i.e. Traceback: %s" %traceback.format_exc())
        logger.debug('WidsPage : Writing wireless containment: None')
        self.wireless_containment.set(self.config.config_vars.Wireless_Containment_Tarpit_Invalid)
        self.save_settings()
        if not self.config.config_vars.Wireless_Containment_Tarpit_Invalid == self.wireless_containment.get_selected():
            raise AssertionError("Wireless containment tarpit invalid is not selected i.e. Traceback: %s" %traceback.format_exc())
        logger.debug('WidsPage : Writing wireless containment')
        self.wireless_containment.set(self.config.config_vars.Wireless_Containment_Tarpit_All)
        self.save_settings()
        if not self.config.config_vars.Wireless_Containment_Tarpit_All == self.wireless_containment.get_selected():
            raise AssertionError("Wired containment tarpit all is not selected i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(20)
        
    def assert_wireless_containment(self):
        
        if not self.config.config_vars.Wireless_Containment_Deauthenticate == self.wireless_containment.get_selected():
            raise AssertionError("Wireless containment is not selected i.e. Traceback: %s" %traceback.format_exc())
        if not self.config.config_vars.Wireless_Containment_Tarpit_Invalid == self.wireless_containment.get_selected():
            raise AssertionError("Wireless containment tarpit invalid is not selected i.e. Traceback: %s" %traceback.format_exc())    
        if not self.config.config_vars.Wireless_Containment_Tarpit_All == self.wireless_containment.get_selected():
            raise AssertionError("Wired containment tarpit all is not selected i.e. Traceback: %s" %traceback.format_exc())    
        
    def set_wireless_containment_default(self):
        logger.debug('WidsPage : Writing wireless containment: None')
        self.wireless_containment.set(self.config.config_vars.Wireless_Containment_None)
        self.save_settings()
        time.sleep(20)
        
    def set_wired_containment(self):
        logger.debug('WidsPage : Clicking on protection accordion')
        self.protection_accordion.click()    
        logger.debug('WidsPage : Writing wired containment')
        self.wired_containment.set(self.config.config_vars.Wired_Containment_On) 
        self.save_settings()
        time.sleep(20)
    
    def assert_wired_containment(self):
        
        if not self.config.config_vars.Wired_Containment_On == self.wired_containment.get_selected():
            raise AssertionError("Wired containment is not ON i.e. Traceback: %s" %traceback.format_exc())    
    
    def set_wired_containment_default(self):
        logger.debug('WidsPage : Writing wired containment')
        self.wired_containment.set(self.config.config_vars.Wired_Containment_Off)
        self.save_settings()
        time.sleep(20)
        
    def validate_wid_containment(self):
        logger.debug('WidsPage : clicking protection accordion')
        self.protection_accordion.click()    
        logger.debug('WidsPage : Writing wired containment: on')
        self.wired_containment.set(self.config.config_vars.Wired_Containment_On) 
        logger.debug('WidsPage : Writing wireless containment: Deauthenticate')
        self.wireless_containment.set(self.config.config_vars.Wireless_Containment_Deauthenticate)
        self.save_settings()
        time.sleep(20)
        
    def restore_defaults_wired_wireless_containment_methods(self):
        logger.debug('WidsPage : Clicking restore default button')
        self.restore_default.click()
        self.save_settings()
        time.sleep(20)
        
    def assert_validated_wid_containment(self):
        
        if not self.config.config_vars.Wired_Containment_On == self.wired_containment.get_selected():
            raise AssertionError("Wired containment is not checked i.e. Traceback: %s" %traceback.format_exc())
        if not self.config.config_vars.Wireless_Containment_Deauthenticate == self.wireless_containment.get_selected():
            raise AssertionError("Wireless containment is not checked i.e. Traceback: %s" %traceback.format_exc())
            
    def set_detection_clients_threat_detection_level_custom(self , level):
        if level == 'High':
            logger.debug('WidsPage : Clicking detection_clients_threat_high')
            self.detection_clients_threat_high.click()
        elif level == 'Medium':
            logger.debug('WidsPage : Clicking detection_clients_threat_med')
            self.detection_clients_threat_med.click()
        elif level == 'Low':
            logger.debug('WidsPage : Clicking detection_clients_threat_low')
            self.detection_clients_threat_low.click()
        elif level == 'Off':
            logger.debug('WidsPage : Clicking detection_clients_threat_off')
            self.detection_clients_threat_off.click()
        elif level == 'Custom':
            logger.debug('WidsPage : Clicking detection_clients_threat_custom')
            self.detection_clients_threat_custom.click()
        self.save_settings()
        time.sleep(20)
        
    def set_detection_infra_threat_detection_level_custom(self , level):
        if level == 'High':
            logger.debug('WidsPage : Clicking detection_infrastructure_threat_high')
            self.detection_infrastructure_threat_high.click()
        elif level == 'Medium':
            logger.debug('WidsPage : Clicking detection_infrastructure_threat_med')
            self.detection_infrastructure_threat_med.click()
        elif level == 'Low':
            logger.debug('WidsPage : Clicking detection_infrastructure_threat_low')
            self.detection_infrastructure_threat_low.click()
        elif level == 'Off':
            logger.debug('WidsPage : Clicking detection_infrastructure_threat_off')
            self.detection_infrastructure_threat_off.click()
        elif level == 'Custom':
            logger.debug('WidsPage : Clicking detection_infrastructure_threat_custom')
            self.detection_infrastructure_threat_custom.click()
        self.save_settings()
        time.sleep(20)
        
        
    def set_detection_infra_threat_detection_level_custom_changes(self , level):
        if level == 'High':
            logger.debug('WidsPage : Clicking detection_infrastructure_threat_high')
            self.detection_infrastructure_threat_high.click()
        elif level == 'Medium':
            logger.debug('WidsPage : Clicking detection_infrastructure_threat_med')
            self.detection_infrastructure_threat_med.click()
        elif level == 'Low':
            logger.debug('WidsPage : Clicking detection_infrastructure_threat_low')
            self.detection_infrastructure_threat_low.click()
        elif level == 'Off':
            logger.debug('WidsPage : Clicking detection_infrastructure_threat_off')
            self.detection_infrastructure_threat_off.click()
        elif level == 'Custom':
            logger.debug('WidsPage : Clicking detection_infrastructure_threat_custom')
            self.detection_infrastructure_threat_custom.click()
            logger.debug('WidsPage : Clicking detect_apspoofing_chkbox')
            self.detect_apspoofing_chkbox.click()
            logger.debug('WidsPage : Clicking detect_windows_bridge_chkbox')
            self.detect_windows_bridge_chkbox.click()
            logger.debug('WidsPage : Clicking signature_deauth_broadcast_chkbox')
            self.signature_deauth_broadcast_chkbox.click()
            logger.debug('WidsPage : Clicking signature_deassociation_broadcast_chkbox')
            self.signature_deassociation_broadcast_chkbox.click()
        self.save_settings()
        time.sleep(20)
        
    def set_detection_clients_threat_detection_level_custom_changes(self , level):
        if level == 'High':
            logger.debug('WidsPage : Clicking detection_clients_threat_high')
            self.detection_clients_threat_high.click()
        elif level == 'Medium':
            logger.debug('WidsPage : Clicking detection_clients_threat_med')
            self.detection_clients_threat_med.click()
        elif level == 'Low':
            logger.debug('WidsPage : Clicking detection_clients_threat_low')
            self.detection_clients_threat_low.click()
        elif level == 'Off':
            logger.debug('WidsPage : Clicking detection_clients_threat_off')
            self.detection_clients_threat_off.click()
        elif level == 'Custom':
            logger.debug('WidsPage : Clicking detection_clients_threat_custom')
            self.detection_clients_threat_custom.click()
            logger.debug('WidsPage : Clicking detect_valid_clientmisassociation')
            self.detect_valid_clientmisassociation.click()
        self.save_settings()
        time.sleep(20)
        
    def assert_infrastructure_clients_protection(self):
        
        
        logger.debug('Wids Page : Clicking on Protection Accordion')
        self.assert_wids_protection_section_expanded()
        time.sleep(5)
        if not self.infra_protect_off.is_selected():
            raise AssertionError("Infrastructure Threat Protection Level is not set to OFF i.e. Traceback: %s" %traceback.format_exc())
        if not self.client_protect_off.is_selected():
            raise AssertionError("Infrastructure Client Protection Level is not set to OFF i.e. Traceback: %s" %traceback.format_exc())
    
    def assert_wired_wireless_containment(self):
        
        
        logger.debug('Wids Page : Clicking on Protection Accordion')
        self.assert_wids_protection_section_expanded()
        time.sleep(5)
        if not self.wired_containment.get_selected() == self.config.config_vars.Wired_Containment_Off:
            raise AssertionError("Wired Containment is not set to OFF i.e. Traceback: %s" %traceback.format_exc())
        if not self.wireless_containment.get_selected() == self.config.config_vars.Wireless_Containment_None:
            raise AssertionError("Wireless Containment is not set to None i.e. Traceback: %s" %traceback.format_exc())
        
    def select_custom_infra_threat_detection_level(self):
        logger.debug('WidsPage : Clicking detection infrastructure threat ')
        self.detection_infrastructure_threat_custom.click()
        logger.debug('WidsPage : Clicking invalid address combination')
        self.detect_invalid_addresscombination_chkbox.click()
        logger.debug('WidsPage : Clicking detect ap impersonation')
        self.detect_ap_impersonation_chkbox.click()
        
    def assert_save_alert_pop_up(self,visible=False):
        
        if visible:
            if not self.confirm_save_ok_1 :
                raise AssertionError("Save alert pop up not visible i.e. Traceback: %s" %traceback.format_exc())
            logger.debug('WidsPage : Clicking on save ok')
            self.confirm_save_ok_1.click()
        else:
            if self.confirm_save_ok_1 :
                raise AssertionError("Save alert pop up visible i.e. Traceback: %s" %traceback.format_exc())
                
    def click_help(self):
        logger.debug("Clicking on Help button ")
        self.help_button.click()
        
    def check_detection_help_text_availablility(self):
        
        
        time.sleep(8)
        actions = self.browser.get_action_chain()
        actions.move_to_element(self.detect_infastructure).perform()
        time.sleep(5)
        if not self.detect_infastructure_help_msg:
            raise AssertionError(" help content is not visible i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(5)
        
        actions.move_to_element(self.detect_client).perform()
        time.sleep(5)
        if not self.detect_client_help_msg:
            raise AssertionError(" help content is not visible i.e. Traceback: %s" %traceback.format_exc())
        
        actions.move_to_element(self.detection_accordion).perform()
        time.sleep(5)
        if not self.detection_help_msg:
            raise AssertionError(" help content is not visible i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(15)    
        
    def assert_detection_level_defaults(self):
        
        if not self.infra_detect_off.is_selected():
            raise AssertionError("Off option button for infrastructure not enabled . i.e. Traceback: %s" %traceback.format_exc())
        if not self.client_detect_off.is_selected():
            raise AssertionError("Off option button for client not enabled .  i.e. Traceback: %s" %traceback.format_exc())
            
    def check_protection_help_text_availablility(self):
        
        
        time.sleep(8)
        actions = self.browser.get_action_chain()
        actions.move_to_element(self.protect_infastructure).perform()
        time.sleep(5)
        if not self.protect_infastructure_help_msg:
            raise AssertionError(" help content is not visible i.e. Traceback: %s" %traceback.format_exc())
        time.sleep(5)
        
        actions.move_to_element(self.protect_client).perform()
        time.sleep(5)
        if not self.protect_cleints_help_msg:
            raise AssertionError(" help content is not visible i.e. Traceback: %s" %traceback.format_exc())

    def select_default_instant(self):
        
        
        time.sleep(5)
        logger.debug('WidsPage : Expanding All Groups')
        self.all_group_button.click()
        logger.debug('WidsPage : Expanding default group')
        self.default_expand_button.click()
        logger.debug('WidsPage : Select Instant')
        self.default_group_instant_option.click()
        time.sleep(5)
    
    def change_wids_protection_settings(self):
        
        
        logger.debug('WidsPage : Opening wids protection accordions')
        self.protection_accordion.click()
        time.sleep(5)
        logger.debug('WidsPage : Setting Wired Containment to ON')
        self.wired_containment.set(self.config.config_vars.Wired_Containment_On)
        logger.debug('WidsPage : Setting Wireless Containment to Tarpit invalid station')
        self.wireless_containment.set(self.config.config_vars.Wireless_Containment_Tarpit_Invalid)
        logger.debug('WidsPage : Clicking on Save button')
        self.save_settings()
        time.sleep(120)

    def assert_resolve_override_flag(self):
        
        
        if not self.override_flag_button:
            raise AssertionError("Override flag is not visible i.e. Traceback: %s" %traceback.format_exc())
        logger.debug('WidsPage : Clicking on override flag')
        self.override_flag_button.click()
        time.sleep(5)
        if not self.override_flag_wireless_param:
            raise AssertionError("Wireless parameter is not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.override_flag_wired_param:
            raise AssertionError("Wired parameter is not present i.e. Traceback: %s" %traceback.format_exc())
        # if not self.override_flag_vc_name:
            # raise AssertionError("VC name is not present i.e. Traceback: %s" %traceback.format_exc())
        logger.debug('WidsPage : Clicking Resolve All')
        self.override_resolv_button.click()
        time.sleep(8)

    def set_wids_protection_default(self):
        
        
        logger.debug('WidsPage : Setting Wired Containment to OFF')
        self.wired_containment.set(self.config.config_vars.Wired_Containment_Off)
        logger.debug('WidsPage : Setting Wireless Containment to None')
        self.wireless_containment.set(self.config.config_vars.Wireless_Containment_None)
        logger.debug('WidsPage : Clicking on Save button')
        self.save_settings()
        time.sleep(30)
        
    def change_wids_detection_settings(self):
        
        
        time.sleep(5)
        logger.debug('WidsPage : Choosing infrastructure custom')
        self.detection_infrastructure_threat_custom.click()
        logger.debug('WidsPage : Checking all checkboxs of right panel')
        self.detect_windows_bridge_chkbox.click()
        self.signature_deauth_broadcast_chkbox.click()
        self.signature_deassociation_broadcast_chkbox.click()
        self.detect_apspoofing_chkbox.click()
        logger.debug('WidsPage : Choosing client custom')
        self.detection_clients_threat_custom.click()
        logger.debug('WidsPage : Checking client mis assocoiation checkboxs ')
        self.detect_valid_clientmisassociation_chkbox.click()
        logger.debug('WidsPage : Checking hot spotter')
        self.detect_hotspotter_attack_chkbox.click()
        logger.debug('WidsPage : Checking power save dos attack')
        self.detect_power_save_dos_attack_chbox.click()
        logger.debug('WidsPage : Checking omerta attack')
        self.detect_omerta_attack_chkbox.click()
        logger.debug('WidsPage : Clicking on Save button')
        self.save_settings()
        time.sleep(120)
        
    def assert_detection_resolve_override_flag(self):
        
        
        if not self.override_flag_button:
            raise AssertionError("Override flag is not visible i.e. Traceback: %s" %traceback.format_exc())
        logger.debug('WidsPage : Clicking on override flag')
        self.override_flag_button.click()
        time.sleep(15)
        if not self.override_flag_signature_deassociation:
            raise AssertionError("Signature deassociation is not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.override_flag_detect_omerta_attack:
            raise AssertionError("Detect omerta attack is not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.override_flag_detect_windows_bridge:
            raise AssertionError("Detect windows bridge is not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.override_flag_detect_power_save_dos_attack:
            raise AssertionError("Detect power save dos is not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.override_flag_detect_ap_spoofing:
            raise AssertionError("Detect ap spoofing is not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.override_flag_sig_deauth_broadcast:
            raise AssertionError("Signature deauth broadcast is not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.override_flag_detect_hotspotter_attack:
            raise AssertionError("Detect hotspotter attack is not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.override_flag_detect_valid_client_mis:
            raise AssertionError("Detect valid client is not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.override_flag_infrastructure_detection_level:
            raise AssertionError("Infrastructure detection level is not present i.e. Traceback: %s" %traceback.format_exc())
        if not self.override_flag_client_detection_level:
            raise AssertionError("Client detection level is not present i.e. Traceback: %s" %traceback.format_exc())
        logger.debug('WidsPage : Clicking Resolve All')
        self.override_resolv_button.click()
        time.sleep(8)
        
    def set_wids_detection_default(self):
        
        
        logger.debug('WidsPage : Clicking on Infrastructure OFF')
        self.detection_infrastructure_threat_off.click()
        logger.debug('WidsPage : Clicking on Client OFF')
        self.detection_clients_threat_off.click()
        logger.debug('WidsPage : Clicking on Save')
        self.save_settings()
        time.sleep(30)

    def set_wids_detection_default(self):
        
        
        logger.debug('WidsPage : Clicking on Infrastructure OFF')
        self.detection_infrastructure_threat_off.click()
        logger.debug('WidsPage : Clicking on Client OFF')
        self.detection_clients_threat_off.click()
        logger.debug('WidsPage : Clicking on Save')
        self.save_settings()
        time.sleep(30)

    def click_attacks_protect_infrastructure_custom(self):
        self.protect_ap_impersonation_checked.click()
        self.protect_adhoc_network_checked.click()
        self.rogue_containment_checked.click()
        self.protect_ssid_checked.click()

    def click_confirm_save_cancel(self):
        logger.debug("Clicking on Cancel Confirm button ")
        self.confirm_save_cancel.click()

    def click_cancel_settings(self):
        logger.debug("Clicking on Cancel Confirm button ")
        self.cancel_settings.click()
        time.sleep(8)

    def click_rf_module(self):
        logger.debug("Clicking on rf menu ")
        self.rf_menu.click()
        logger.debug("Clicking on save button ")
        from selenium.webdriver.common.alert import Alert
        try:
           Alert(self.browser._browser).accept()
        except:
           pass
        #self.save_nav.click()
        if not self.page_header:
            raise AssertionError("RF page did not get Loaded i.e. Traceback: %s" %traceback.format_exc())    
                
    def click_monitoring_module(self):
        logger.debug("Clicking on monitoring  ")
        self.monitoring_menu.click()
        logger.debug("Clicking on save button ")
        self.save_nav.click()
        if not self.quicklinks_dropdown:
            raise AssertionError("Monitoring page did not get Loaded i.e. Traceback: %s" %traceback.format_exc())
            
    def click_protection_accordion(self):
        '''
        Clicks on 'PROTECTION' accordion.
        '''
        logger.debug("WIDS page : Clicking on 'PROTECTION' accordion. ")
        if self.protection_accordion:
            self.protection_accordion.click()
        self.buy_time()
        
    def buy_time(self):
        logger.debug("WIDS page : Waits for 12 seconds. ")
        time.sleep(12)
        
    def enable_or_disable_rogue_containment(self,flag=False):
        '''
        Enables or disables rogue containment.
        '''
        if flag:
            logger.debug("WIDS page : Enabling rogue containment checkbox. ")
            if not self.rogue_containment_enabled:
                self.rogue_containment_enabled.click()
                time.sleep(3)
        else:
            logger.debug("WIDS page : Disabling rogue containment checkbox. ")
            if self.rogue_containment_enabled:
                self.rogue_containment_enabled.click()
                time.sleep(3)
                
    def enable_or_disable_protect_ssid(self,flag=False):
        '''
        Enables or disables protect ssid.
        '''
        if flag:
            logger.debug("WIDS page : Enabling protect ssid checkbox. ")
            if not self.protect_ssid:
                self.protect_ssid.click()
                time.sleep(3)
        else:
            logger.debug("WIDS page : Disabling protect ssid checkbox. ")
            if self.protect_ssid:
                self.protect_ssid.click()
                time.sleep(3)
                
    def enable_or_disable_protect_ap_impersonation(self,flag=False):
        '''
        Enables or disables protect ap impersonation.
        '''
        if flag:
            logger.debug("WIDS page : Enabling protect ap impersonation checkbox. ")
            if not self.protect_ap_impersonation_checkbox:
                self.protect_ap_impersonation_checkbox.click()
                time.sleep(3)
        else:
            logger.debug("WIDS page : Disabling protect ap impersonation checkbox. ")
            if self.protect_ap_impersonation_checkbox:
                self.protect_ap_impersonation_checkbox.click()
                time.sleep(3)
                
    def enable_or_disable_protect_adhoc_network(self,flag=False):
        '''
        Enables or disables protect adhoc network.
        '''
        if flag:
            logger.debug("WIDS page : Enabling protect adhoc network checkbox. ")
            if not self.protect_adhoc_network_checkbox:
                self.protect_adhoc_network_checkbox.click()
                time.sleep(3)
        else:
            logger.debug("WIDS page : Disabling protect adhoc network checkbox. ")
            if self.protect_adhoc_network_checkbox:
                self.protect_adhoc_network_checkbox.click()
                time.sleep(3)

    def set_wired_containment_dropdown(self,value='Off'):
        '''
        Sets wired containment dropdown.
        '''
        if self.wired_containment:
            if value == 'Off':
                logger.debug("WidsPage : Selecting wired containment to 'OFF'")
                self.wired_containment.set(self.config.config_vars.Wired_Containment_Off)
            if value == 'On':
                logger.debug("WidsPage : Selecting wired containment to 'ON'")
                self.wired_containment.set(self.config.config_vars.Wired_Containment_On)
                
    def set_wireless_containment_dropdown(self,value='None'):
        '''
        Sets wireless containment dropdown.
        '''
        conf = self.config.config_vars
        if self.wireless_containment:
            if value == 'None':
                logger.debug("WIDS page : Protection : Writing wireless containment : 'None' ")
                self.wireless_containment.set(conf.Wireless_Containment_None)
            elif value == 'Deauthenticate only':
                logger.debug("WIDS page : Protection : Writing wireless containment : 'Deauthenticate only' ")
                self.wireless_containment.set(conf.Wireless_Containment_Deauthenticate)
            elif value == 'Tarpit invalid stations':
                logger.debug("WIDS page : Protection : Writing wireless containment : 'Tarpit invalid stations' ")
                self.wireless_containment.set(conf.Wireless_Containment_Tarpit_Invalid)
            elif value == 'Tarpit all stations':
                logger.debug("WIDS page : Protection : Writing wireless containment : 'Tarpit all stations' ")
                self.wireless_containment.set(conf.Wireless_Containment_Tarpit_All)
            time.sleep(3)
            
    def setting_attacks(self):
        if not self.detect_valid_clientmisassociation_chkbox.is_selected():
            logger.debug('WidsPage : Checking client mis assocoiation checkboxs ')
            self.detect_valid_clientmisassociation_chkbox.click()
        if not self.detect_hotspotter_attack_chkbox.is_selected():    
            logger.debug('WidsPage : Checking hot spotter')
            self.detect_hotspotter_attack_chkbox.click()
        if not self.detect_power_save_dos_attack_chbox.is_selected():
            logger.debug('WidsPage : Checking power save dos attack')
            self.detect_power_save_dos_attack_chbox.click()
        if not self.detect_omerta_attack_chkbox.is_selected():
            logger.debug('WidsPage : Checking omerta attack')
            self.detect_omerta_attack_chkbox.click()
        
    def assert_attacks(self):
        logger.debug('WidsPage : Asserting client mis assocoiation checkboxs ')
        self.browser.assert_check_box_value(self.detect_valid_clientmisassociation_chkbox, "client mis assocoiation checkbox is not checked by default", uncheck=True)
        logger.debug('WidsPage : Asserting hot spotter')
        self.browser.assert_check_box_value(self.detect_hotspotter_attack_chkbox, "hot spotter checkbox is not checked by default", uncheck=True)
        logger.debug('WidsPage : Asserting power save dos attack')
        self.browser.assert_check_box_value(self.detect_power_save_dos_attack_chbox, "power save dos checkbox is not checked by default", uncheck=True)
        logger.debug('WidsPage : Asserting omerta attack')
        self.browser.assert_check_box_value(self.detect_omerta_attack_chkbox, "omerta attack checkbox is not checked by default", uncheck=True)
        
    def set_protection_client_high(self):
        logger.debug('WidsPage : Clicking protection accordion')
        self.protection_accordion.click()
        logger.debug('WidsPage : Clicking client protect: high')
        self.client_protect_high.click()
        self.save_settings()
        time.sleep(20)
        
    def set_protection_infra_low(self):
        logger.debug('WidsPage : Clicking protection accordion')
        self.protection_accordion.click()
        logger.debug('WidsPage : Clicking infra protect: low')
        self.infra_protect_low.click()
        self.save_settings()
        time.sleep(20)
        
    def assert_infra_client_high(self):
        logger.debug("WidsPage: Asserting Infrastructure and Client field")
        if not self.infra_protect_high.is_selected():
            raise AssertionError("Infrastructure protect low is not selected i.e. Traceback: %s" %traceback.format_exc())
        if not self.client_protect_high.is_selected():
            raise AssertionError("Client protect low is high selected i.e. Traceback: %s" %traceback.format_exc())
            
    def select_detect_block_ack_attack(self):
        '''
        Selects Detect Block ack attack checkbox.
        '''
        if self.detect_block_ack_attack:
            logger.debug('WidsPage : Selecting Detect-Block-ack-attack checkbox')
            self.detect_block_ack_attack.click()
            
    def select_detect_adhoc_using_valid_ssid(self):
        '''
        Selects detect_adhoc_using_valid_ssid checkbox.
        '''
        if self.detect_adhoc_using_valid_ssid_tick:
            if not self.detect_adhoc_using_valid_ssid_tick.is_selected():
                logger.debug('WidsPage : Selecting Detect-Block-ack-attack checkbox')
                self.detect_adhoc_using_valid_ssid_tick.click()
            
    def assert_override_flag(self,flag):
        '''
        Checks for Override flag on TopPanel.
        '''
        logger.debug('WidsPage : Checking for top panel override flag.')
        self.browser.refresh()
        if flag:
            if not self.override_flag_on_top_panel:
                raise AssertionError("Override flag not found on top panel i.e. Traceback: %s" %traceback.format_exc())
        else:
            if self.override_flag_on_top_panel:
                raise AssertionError("Override flag found on top panel i.e. Traceback: %s" %traceback.format_exc())
                
    def set_infra_threat_protection_level_high(self):
        '''
        clicks on High radio button
        '''
        if not self.infra_protect_high.is_selected():
            logger.debug('WidsPage : Clicking infra protect high')
            self.infra_protect_high.click()
            
    def assert_infra_level_high(self):        
        '''
        Asserts Infrastructure Threat protection level    
        '''
        if not self.infra_protect_high.is_selected():
            raise AssertionError("Infrastructure Threat Protection Level is not set to High i.e. Traceback: %s" %traceback.format_exc())
        
    def assert_client_level_off(self):    
        '''
        Asserts Infrastructure Threat protection level    
        '''
        if not self.client_protect_off.is_selected():
            raise AssertionError("Client Protection Level is not set to OFF i.e. Traceback: %s" %traceback.format_exc())
    
    def set_client_protect_level_low(self):
        '''
        Sets Clients Threat protection level on Low 
        '''
        if not self.client_protect_low.is_selected():
            logger.debug('WidsPage : Clicking Client protect Low')
            self.client_protect_low.click()        
            
    def assert_override_flag_button(self,check):
        '''
        Asserts Override flag Button
        '''
        if check == 'True':
            self.browser.assert_element(self.override_flag_on_top_panel, 'Ovveride flag button is not present')
        if check == 'False':    
            self.browser.assert_element(self.override_flag_on_top_panel, 'Ovveride flag button is not present', False)
    
    def set_infra_protection_low_and_wired_wireless_containment(self,check):
        '''
        '''
        self.set_protection_infra_low()
        self.set_wired_containment_dropdown(value='On')
        self.set_wireless_containment_dropdown(value='Tarpit all stations')
        self.save_settings()
        self.browser.refresh()
        self.assert_override_flag_button(check)