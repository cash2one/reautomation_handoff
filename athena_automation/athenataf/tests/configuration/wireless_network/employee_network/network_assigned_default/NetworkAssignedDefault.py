import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class NetworkAssignedDefault(ConfigurationTest):
    '''
    Test class for Field Validation of netwrok assigned module.
    '''

    def test_ath_3369_ssid_field_validation(self):
        conf = self.config.config_vars
        self.NetworkPage.delete_network_if_present()
        self.take_s1_snapshot()
        
        basic_info = self.NetworkPage.create_new_network()
        vlan_obj = basic_info.employee_network_info()
        security = vlan_obj.use_vlan_defaults()
        access = security.configure_employee_security()
        access.finish_network_setup()        
        
        basic_info = self.NetworkPage.create_new_network()
        vlan_page = basic_info.set_invalid_network_name(conf.ntwrk_name_spcl_char_invalid)
        basic_info.set_invalid_network_name(conf.ntwrk_name_max)
        
        vlan_page = basic_info.name_field_validation(conf.valid_network_name2,'valid')
        vlan_page.assert_vlan_page()
        
        basic_info.set_name_field()
        basic_info.assert_duplicate_network_error_message()
        
        self.take_s2_snapshot()
        self.NetworkPage.delete_network_if_present()
        self.take_s3_snapshot()
        self.assert_s1_s2_diff(None)
        self.assert_s1_s3_diff()
        self.clear()