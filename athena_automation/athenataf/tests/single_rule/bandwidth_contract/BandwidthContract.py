import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class BandwidthContract(ConfigurationTest):
    '''
        Test class for Bandwidth Contract.
    '''

    def test_ath_8889_create_bandwidth_contract_rule(self):
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.guest_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.use_security_default()
        access.create_bandwidth_contract_rule(True)
        self.NetworkPage.assert_new_network()
        self.NetworkPage.delete_network_if_present()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.guest_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.use_security_default()
        access.create_bandwidth_contract_rule(False)
        self.NetworkPage.assert_new_network()
        self.take_s2_snapshot()
        self.NetworkPage.delete_network_if_present()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
        
    def test_ath_8964_delete_bandwidth_contract_rule(self):
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.guest_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.use_security_default()
        access.create_bandwidth_contract_rule(True)
        self.NetworkPage.assert_new_network()
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.delete_existing_bandwidth_contract_rule()
        self.NetworkPage.assert_new_network()
        self.take_s2_snapshot()
        self.NetworkPage.delete_network_if_present()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()
        
        
    def test_ath_8953_change_to_another_rule(self):
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.guest_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.use_security_default()
        access.create_bandwidth_contract_rule(True)
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.change_bw_to_vlan()
        self.NetworkPage.delete_network_if_present()
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.guest_network_info()
        security = virtual_lan.use_vlan_defaults()
        access = security.use_security_default()
        access.create_bandwidth_contract_rule(True)
        edit_network_page = self.NetworkPage.edit_network()
        edit_network_page.change_bw_to_captive_portal()
        self.take_s2_snapshot()
        self.NetworkPage.delete_network_if_present()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()