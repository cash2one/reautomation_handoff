import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DenyToNetwork(ConfigurationTest):
    '''
        
    '''
    
    def test_ath_1403_deny_http_proxy3_to_a_particular_server(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.configure_employee_security()
        access.click_network_access()
        access.delete_default_rule_if_present()
        access.set_rule_service_action_and_destination(conf.Service_Role1_netbios_ssn, conf.action_dropdown_deny, conf.dest_to_a_ntwrk)
        access.set_destination_ip_mask_domain(conf.netbios_destination_ip_1,conf.dest1_net_mask,'')
        access.finish_network_setup()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.assert_new_rule_created('netbios-ssn', 'To a network')
        edit_network_page.assert_new_rule_deny()
        self.take_s2_snapshot()
        edit_network_page.delete_access_rule()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.delete_network_if_present()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_1404_deny_http_proxy3_to_a_particular_server(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.configure_employee_security()
        access.click_network_access()
        access.delete_default_rule_if_present()
        access.set_rule_service_action_and_destination(conf.service_nterm, conf.action_dropdown_deny, conf.dest_to_a_ntwrk)
        access.set_destination_ip_mask_domain(conf.netbios_destination_ip_1,conf.dest2_net_mask,'')
        access.finish_network_setup()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.assert_new_rule_created('nterm', 'To a network')
        edit_network_page.assert_new_rule_deny()
        self.take_s2_snapshot()
        edit_network_page.delete_access_rule()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.delete_network_if_present()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
    
    def test_ath_1405_deny_http_proxy3_to_a_particular_server(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.configure_employee_security()
        access.click_network_access()
        access.delete_default_rule_if_present()
        access.set_rule_service_action_and_destination(conf.Service_Role1_ntp, conf.action_dropdown_deny, conf.dest_to_a_ntwrk)
        access.set_destination_ip_mask_domain(conf.ntp_destination_ip_2,conf.dest_netmask,'')
        access.finish_network_setup()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.assert_new_rule_created('ntp', 'To a network')
        edit_network_page.assert_new_rule_deny()
        self.take_s2_snapshot()
        edit_network_page.delete_access_rule()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.delete_network_if_present()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
    
    def test_ath_1406_deny_http_proxy3_to_a_particular_server(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.configure_employee_security()
        access.click_network_access()
        access.delete_default_rule_if_present()
        access.set_rule_service_action_and_destination(conf.action_papi, conf.action_dropdown_deny, conf.dest_to_a_ntwrk)
        access.set_destination_ip_mask_domain(conf.papi_destination_ip_1,conf.dest2_net_mask,'')
        access.finish_network_setup()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.assert_new_rule_created('papi', 'To a network')
        edit_network_page.assert_new_rule_deny()
        self.take_s2_snapshot()
        edit_network_page.delete_access_rule()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.delete_network_if_present()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
    
    def test_ath_1407_deny_http_proxy3_to_a_particular_server(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.configure_employee_security()
        access.click_network_access()
        access.delete_default_rule_if_present()
        access.set_rule_service_action_and_destination(conf.Service_Role1_pop3, conf.action_dropdown_deny, conf.dest_to_a_ntwrk)
        access.set_destination_ip_mask_domain(conf.pop3_destination_ip_1,conf.dest2_net_mask,'')
        access.finish_network_setup()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.assert_new_rule_created('pop3', 'To a network')
        edit_network_page.assert_new_rule_deny()
        self.take_s2_snapshot()
        edit_network_page.delete_access_rule()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.delete_network_if_present()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_1408_deny_pptp_to_a_network(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.configure_employee_security()
        access.click_network_access()
        access.delete_default_rule_if_present()
        access.set_rule_service_action_and_destination(conf.service_pptp, conf.action_role_deny, conf.dest_to_a_ntwrk)
        import time
        time.sleep(5)
        access.set_destination_ip_mask_domain(conf.pop3_destination_ip_1,conf.dest2_net_mask,'')
        time.sleep(5)
        access.finish_network_setup()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.assert_new_rule_created('pptp', 'To a network')
        time.sleep(5)
        edit_network_page.assert_new_rule_deny()
        self.take_s2_snapshot()
        edit_network_page.delete_access_rule()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.delete_network_if_present()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_7152_deny_snmp_to_a_network(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.configure_employee_security()
        access.click_network_access()
        access.delete_default_rule_if_present()
        import time
        time.sleep(5)
        access.set_rule_service_action_and_destination(conf.service_snmp, conf.action_role_deny, conf.dest_to_a_ntwrk)
        time.sleep(5)
        access.set_destination_ip_mask_domain(conf.pop3_destination_ip_1,conf.dest2_net_mask,'')
        time.sleep(5)
        access.finish_network_setup()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.assert_new_rule_created('snmp', 'To a network')
        time.sleep(5)
        edit_network_page.assert_new_rule_deny()
        self.take_s2_snapshot()
        edit_network_page.delete_access_rule()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.delete_network_if_present()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_7153_deny_telnet_to_a_network(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.configure_employee_security()
        access.click_network_access()
        access.delete_default_rule_if_present()
        import time
        time.sleep(5)
        access.set_rule_service_action_and_destination(conf.Service_Role1_telnet, conf.action_role_deny, conf.dest_to_a_ntwrk)
        time.sleep(5)
        access.set_destination_ip_mask_domain(conf.pop3_destination_ip_1,conf.dest2_net_mask,'')
        time.sleep(5)
        access.finish_network_setup()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.assert_new_rule_created('telnet', 'To a network')
        time.sleep(5)
        edit_network_page.assert_new_rule_deny()
        self.take_s2_snapshot()
        edit_network_page.delete_access_rule()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.delete_network_if_present()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_7154_deny_vocera_to_a_network(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.configure_employee_security()
        access.click_network_access()
        access.delete_default_rule_if_present()
        import time
        time.sleep(5)
        access.set_rule_service_action_and_destination(conf.Service_Role1_vocera, conf.action_role_deny, conf.dest_to_a_ntwrk)
        time.sleep(5)
        access.set_destination_ip_mask_domain(conf.pop3_destination_ip_1,conf.dest2_net_mask,'')
        time.sleep(5)
        access.finish_network_setup()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.assert_new_rule_created('vocera', 'To a network')
        time.sleep(5)
        edit_network_page.assert_new_rule_deny()
        self.take_s2_snapshot()
        edit_network_page.delete_access_rule()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.delete_network_if_present()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_7155_deny_rtsp_to_a_network(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.configure_employee_security()
        access.click_network_access()
        access.delete_default_rule_if_present()
        import time
        time.sleep(5)
        access.set_rule_service_action_and_destination(conf.Service_Role1_rtsp, conf.action_role_deny, conf.dest_to_a_ntwrk)
        time.sleep(5)
        access.set_destination_ip_mask_domain(conf.pop3_destination_ip_1,conf.dest2_net_mask,'')
        time.sleep(5)
        access.finish_network_setup()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.assert_new_rule_created('rtsp', 'To a network')
        time.sleep(5)
        edit_network_page.assert_new_rule_deny()
        self.take_s2_snapshot()
        edit_network_page.delete_access_rule()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.delete_network_if_present()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()