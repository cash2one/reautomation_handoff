import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DestinationNatToAParticularServer(ConfigurationTest):
    '''
    Test class
    '''
    def test_ath_1512_dst_nat_gre_to_a_server(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.configure_employee_security()
        access.click_network_access()
        access.delete_default_rule_if_present()
        access.set_rule_service_action_and_destination(conf.service_role_gre, conf.action_role_destination_nat, conf.Destination_Role1_To_a_particular_server)
        access.set_destination_ip_mask_domain(conf.valid_destination_ip,'','')
        access.set_action_ip_port(conf.action_ip4,conf.action_port4)
        access.finish_network_setup()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.assert_new_rule_created('gre', 'To a particular server')
        edit_network_page.assert_new_rule_destination_nat()
        self.take_s2_snapshot()
        edit_network_page.delete_access_rule()
        self.NetworkPage.delete_network_if_present()        
        self.LeftPanel.assert_delta_config_icon()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_1513_dst_nat_h323_tcp_to_a_server(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.configure_employee_security()
        access.click_network_access()
        access.delete_default_rule_if_present()
        access.set_rule_service_action_and_destination(conf.service_role_h323_tcp, conf.action_role_destination_nat, conf.Destination_Role1_To_a_particular_server)
        access.set_destination_ip_mask_domain(conf.valid_destination_ip,'','')
        access.set_action_ip_port(conf.action_ip4,conf.action_port4)
        access.finish_network_setup()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.assert_new_rule_created('h323-tcp', 'To a particular server')
        edit_network_page.assert_new_rule_destination_nat()
        self.take_s2_snapshot()
        edit_network_page.delete_access_rule()
        self.NetworkPage.delete_network_if_present()        
        self.LeftPanel.assert_delta_config_icon()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()    
        
    def test_ath_1514_dst_nat_h323_udp_to_a_server(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.configure_employee_security()
        access.click_network_access()
        access.delete_default_rule_if_present()
        access.set_rule_service_action_and_destination(conf.action_h323_udp, conf.action_role_destination_nat, conf.Destination_Role1_To_a_particular_server)
        access.set_destination_ip_mask_domain(conf.valid_destination_ip,'','')
        access.set_action_ip_port(conf.action_ip4,conf.action_port4)
        access.finish_network_setup()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.assert_new_rule_created('h323-udp', 'To a particular server')
        edit_network_page.assert_new_rule_destination_nat()
        self.take_s2_snapshot()
        edit_network_page.delete_access_rule()
        self.NetworkPage.delete_network_if_present()        
        self.LeftPanel.assert_delta_config_icon()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_1515_dst_nat_http_proxy2_to_a_server(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.configure_employee_security()
        access.click_network_access()
        access.delete_default_rule_if_present()
        access.set_rule_service_action_and_destination(conf.service_http_proxy, conf.action_role_destination_nat, conf.Destination_Role1_To_a_particular_server)
        access.set_destination_ip_mask_domain(conf.valid_destination_ip,'','')
        access.set_action_ip_port(conf.action_ip4,conf.action_port4)
        access.finish_network_setup()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.assert_new_rule_created('http-proxy2', 'To a particular server')
        edit_network_page.assert_new_rule_destination_nat()
        self.take_s2_snapshot()
        edit_network_page.delete_access_rule()
        self.NetworkPage.delete_network_if_present()        
        self.LeftPanel.assert_delta_config_icon()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_1516_dst_nat_http_proxy3_to_a_server(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.configure_employee_security()
        access.click_network_access()
        access.delete_default_rule_if_present()
        access.set_rule_service_action_and_destination(conf.Service_Role1_http_proxy3, conf.action_role_destination_nat, conf.Destination_Role1_To_a_particular_server)
        access.set_destination_ip_mask_domain(conf.valid_destination_ip,'','')
        access.set_action_ip_port(conf.action_ip4,conf.action_port4)
        access.finish_network_setup()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.assert_new_rule_created('http-proxy3', 'To a particular server')
        edit_network_page.assert_new_rule_destination_nat()
        self.take_s2_snapshot()
        edit_network_page.delete_access_rule()
        self.NetworkPage.delete_network_if_present()        
        self.LeftPanel.assert_delta_config_icon()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_1517_dst_nat_http_to_a_server(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.configure_employee_security()
        access.click_network_access()
        access.delete_default_rule_if_present()
        access.set_rule_service_action_and_destination(conf.Service_Role1_http_proxy, conf.action_role_destination_nat, conf.Destination_Role1_To_a_particular_server)
        access.set_destination_ip_mask_domain(conf.valid_destination_ip,'','')
        access.set_action_ip_port(conf.action_ip4,conf.action_port4)
        access.finish_network_setup()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.assert_new_rule_created('http', 'To a particular server')
        edit_network_page.assert_new_rule_destination_nat()
        self.take_s2_snapshot()
        edit_network_page.delete_access_rule()
        self.NetworkPage.delete_network_if_present()        
        self.LeftPanel.assert_delta_config_icon()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_1518_dst_nat_https_to_a_server(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.configure_employee_security()
        access.click_network_access()
        access.delete_default_rule_if_present()
        access.set_rule_service_action_and_destination(conf.service_http, conf.action_role_destination_nat, conf.Destination_Role1_To_a_particular_server)
        access.set_destination_ip_mask_domain(conf.valid_destination_ip,'','')
        access.set_action_ip_port(conf.action_ip4,conf.action_port4)
        access.finish_network_setup()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.assert_new_rule_created('https', 'To a particular server')
        edit_network_page.assert_new_rule_destination_nat()
        self.take_s2_snapshot()
        edit_network_page.delete_access_rule()
        self.NetworkPage.delete_network_if_present()        
        self.LeftPanel.assert_delta_config_icon()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_1519_dst_nat_icmp_to_a_server(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.configure_employee_security()
        access.click_network_access()
        access.delete_default_rule_if_present()
        access.set_rule_service_action_and_destination(conf.Service_Role1_icmp, conf.action_role_destination_nat, conf.Destination_Role1_To_a_particular_server)
        access.set_destination_ip_mask_domain(conf.valid_destination_ip,'','')
        access.set_action_ip_port(conf.action_ip4,conf.action_port4)
        access.finish_network_setup()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.assert_new_rule_created('icmp', 'To a particular server')
        edit_network_page.assert_new_rule_destination_nat()
        self.take_s2_snapshot()
        edit_network_page.delete_access_rule()
        self.NetworkPage.delete_network_if_present()        
        self.LeftPanel.assert_delta_config_icon()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_1520_dst_nat_ike_to_a_server(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.configure_employee_security()
        access.click_network_access()
        access.delete_default_rule_if_present()
        access.set_rule_service_action_and_destination(conf.Service_Role1_ike, conf.action_role_destination_nat, conf.Destination_Role1_To_a_particular_server)
        access.set_destination_ip_mask_domain(conf.valid_destination_ip,'','')
        access.set_action_ip_port(conf.action_ip4,conf.action_port4)
        access.finish_network_setup()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.assert_new_rule_created('ike', 'To a particular server')
        edit_network_page.assert_new_rule_destination_nat()
        self.take_s2_snapshot()
        edit_network_page.delete_access_rule()
        self.NetworkPage.delete_network_if_present()        
        self.LeftPanel.assert_delta_config_icon()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
    def test_ath_1521_dst_nat_kerberos_to_a_server(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.configure_employee_security()
        access.click_network_access()
        access.delete_default_rule_if_present()
        access.set_rule_service_action_and_destination(conf.Service_Role1_kerberos, conf.action_role_destination_nat, conf.Destination_Role1_To_a_particular_server)
        access.set_destination_ip_mask_domain(conf.valid_destination_ip,'','')
        access.set_action_ip_port(conf.action_ip4,conf.action_port4)
        access.finish_network_setup()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.assert_new_rule_created('kerberos', 'To a particular server')
        edit_network_page.assert_new_rule_destination_nat()
        self.take_s2_snapshot()
        edit_network_page.delete_access_rule()
        self.NetworkPage.delete_network_if_present()        
        self.LeftPanel.assert_delta_config_icon()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
        