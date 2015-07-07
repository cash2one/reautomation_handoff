import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class MultipleRule(ConfigurationTest):
    '''
    Test class for Multiple Rule of netwrok based module.
    '''
    
    def test_ath_1391_create_multiple_rules(self):
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        vlan = basic_info.guest_network_info()
        security  = vlan.use_vlan_defaults()
        access_page = security.click_on_next()
        access_page.network_based.click()
        access_page.create_external_captive_portal()
        access_page.create_vlan_rule_assignment()
        access_page.access_rule_to_a_network()
        access_page.create_single_vlan_rule_calea()
        access_page.finish_network_setup()
        self.take_s2_snapshot()        
        self.NetworkPage.delete_network_if_present()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()


    def test_ath_1392_move_rules(self):
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        vlan = basic_info.guest_network_info()
        security  = vlan.use_vlan_defaults()
        access_page = security.click_on_next()
        access_page.network_based.click()
        access_page.create_external_captive_portal()
        access_page.create_vlan_rule_assignment()
        access_page.access_rule_to_a_network()
        access_page.create_single_vlan_rule_calea()
        access_page.move_access_rule()
        access_page.finish_network_setup()
        self.take_s2_snapshot()    
        self.NetworkPage.delete_network_if_present()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
