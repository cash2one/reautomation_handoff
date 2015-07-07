import logging
logger = logging.getLogger('athenataf')
import traceback


from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class FieldValidation(ConfigurationTest):
	'''
	Test class  for AccessPoints FieldValidation.
	'''
	
	def test_ath_11235_external_antenna_gain_validation(self):
		conf = self.config.config_vars
		access_point = self.LeftPanel.go_to_access_points()
		access_point.click_134_edit_iap()
		access_point.click_external_antenna_accordion()
		access_point.validate_antenna_gain_fields(conf.gain_alpha_numeric,True)
		access_point.validate_antenna_gain_fields(conf.channel_5ghz_value,True)
		access_point.validate_antenna_gain_fields(conf.valid_transmit_power_24g_zero_preceded_value,True)
		access_point.validate_antenna_gain_fields(conf.no_value,True)
		