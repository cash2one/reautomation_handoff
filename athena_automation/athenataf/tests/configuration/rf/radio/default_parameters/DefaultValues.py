from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class DefaultValues(ConfigurationTest):
	'''
	Test class for RF Radio-> Default values.
	'''
	def test_ath_11098_check_radio_default_values(self):
		rf_page = self.LeftPanel.go_to_rf_page()
		rf_page.open_radio_accordion()
		rf_page.assert_radio_default_values()