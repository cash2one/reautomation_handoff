import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class EditRules(ConfigurationTest):
    '''
        
    '''
    
    def test_ath_1402_Apply_all_the_options(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.configure_employee_security()
        access.click_network_access()
        access.delete_default_rule_if_present()
        access.set_rule_service_action_and_destination(conf.service_https, conf.action_default_value, conf.dest_to_a_ntwrk)
#         access.set_destination_ip_mask_domain(conf.valid_destination_ip,conf.dest2_net_mask,'')
        access.set_ip_mask_domain_checkbox_select_options(conf.valid_destination_ip_1,conf.dest2_net_mask,'')
#         access.checkbox_select_options()
        access.select_dscp_priority_option(conf.dscp_tag_value_DS10,conf.priority_value_7)
        
        access.finish_network_setup()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.assert_new_rule_created('http', 'To a network')
        edit_network_page.assert_on_action('Allow')
        self.take_s2_snapshot()
        edit_network_page.delete_access_rule()
        self.LeftPanel.assert_delta_config_icon()
        self.NetworkPage.delete_network_if_present()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()