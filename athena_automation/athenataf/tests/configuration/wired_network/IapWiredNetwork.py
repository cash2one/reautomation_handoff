import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class IapWiredNetwork(ConfigurationTest):
    '''
        Test class for Iap wired networks testcases.
    '''
    
    def test_ath_4001_create_wired_network_spanning_tree_enabled(self):
        self.take_s1_snapshot()
        self.NetworkPage.delete_wired_network_if_present()
        basic_info= self.NetworkPage.create_new_network()
        virtual_lan= basic_info.create_wired_network()
        security= virtual_lan.wired_network_vlan_defaults()
        access = security.wired_security_defaults()
        network_assignment=access.use_access_defaults()
        network_assignment.finish_network_setup()
        self.NetworkPage.assert_wired_network()
        self.take_s2_snapshot()
        self.NetworkPage.delete_wired_network_if_present()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(0)
        self.assert_s1_s3_diff()
        self.clear()