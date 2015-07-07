import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.MaintenanceTest import MaintenanceTest

class SubscriptionKeys(MaintenanceTest):
    '''
    Test class for SubsciptionKeys.
    '''
    def test_ath_108108_assert_customer(self):
        sub_key=self.LeftPanel.go_to_subscription_keys()