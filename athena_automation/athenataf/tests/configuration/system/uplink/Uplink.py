import logging
logger = logging.getLogger('athenataf')

from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest

class Uplink(ConfigurationTest):
    '''
    Test class for System uplink module.
    '''
    
    def test_ath_1429_3g_4g_nondefaults_values(self):
        system_page = self.LeftPanel.go_to_system_page()
        #system_page.select_modem_country_isp()        
        system_page.cofigure_3g_settings()         
    
    def test_ath_1430_new_wifi(self):
        system_page = self.LeftPanel.go_to_system_page()
        system_page.create_new_wifi()
        
	def test_ath_1431_edit_management(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.assert_new_wifi_setup()        
		system_page.edit_management_settings()
		system_page.set_default_uplink_management_settings()
        
    def test_ath_1432_pppoe_nondefault_values(self):
        system_page = self.LeftPanel.go_to_system_page()
        system_page.assert_new_service_setup()        
        system_page.create_new_ppoe()         