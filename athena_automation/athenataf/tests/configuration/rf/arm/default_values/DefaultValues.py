import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DefaultValues(ConfigurationTest):
	'''
	Test class for DefaultValues.
	'''

	def test_ath_11089_arm_default_values_check(self):
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.assert_rf_values()
		