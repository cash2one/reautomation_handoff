
import logging
logger = logging.getLogger('athenataf')


from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class FieldValidation(ConfigurationTest):
    '''
    Test class for Field Validation and usability.
    '''
		
    def test_ath_7032_validation_vlan_assignment_rules(self):
        basic_info = self.NetworkPage.create_new_network()
        vlan_obj = basic_info.guest_network_info()
        vlan_obj.validate_vlan_assignment_rules()