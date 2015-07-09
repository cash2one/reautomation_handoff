import logging
logger = logging.getLogger('athenataf')
import time
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest
from Device_Module.ObjectModule import Device
from athenataf.lib.functionality.common import DeviceLibrary

class NonDefaultValue(ConfigurationTest):
	'''
	Test class for System General->NonDeafault value .
	'''
	
	def test_ath_11302_check_non_default_values_cpu_util(self):
		myDevice = Device.getDeviceObject("IAP_1")
		vlan_id = myDevice.get("vlan")
		conf = self.config.config_vars
		system_page = self.LeftPanel.go_to_system_page()
		system_page.set_new_vc_name("IAP_1",conf.vc_name)
		system_page.set_new_vc_ip("IAP_1",conf.ip_add)
		system_page.set_non_default_values_cpu_util("IAP_1")
		system_page._save_settings()
		time.sleep(10)
		system_page.assert_system_page_vc_field_values("IAP_1","sh ru | inc name",conf.vc_name)
		system_page.assert_system_page_vc_field_values("IAP_1","sh ru | inc virtual",conf.ip_add)
		system_page.assert_system_page_vc_field_values("IAP_1","sh ru | inc time","Pacific-Time -07")
		system_page.assert_system_page_vc_field_values("IAP_1","sh ru | inc ntp",conf.ntp_server)
		system_page.assert_system_page_vc_field_values("IAP_1","sh ru | inc band","5ghz")
		system_page.assert_system_page_vc_field_values("IAP_1","sh ru | inc vlan",vlan_id)
		system_page.assert_system_page_vc_field_values("IAP_1","sh ru | inc cpu","dynamic-cpu-mgmt enable")
		
		time.sleep(10)
		DeviceLibrary.factoryReset("IAP_1")
		time.sleep(10)
		DeviceLibrary.getPrompt("IAP_1")
		DeviceLibrary.reconnect("IAP_1")
		time.sleep(90)
		inner_left_panel = self.TopPanel.click_slider_icon()
		inner_left_panel.click_expand_default_group_icon()
		inner_left_panel.select_vc("IAP_1")
		inner_left_panel.select_country_code(self.config.config_vars.country_india)
		# system_page.setting_original_vc_name("IAP_1",conf.vc_name) // After factory_reset, automatically take default name on system page
		# system_page.setting_original_vc_ip("IAP_1",conf.ip_add) // After factory_reset, automatically take default ip on system page
		system_page.set_cpu_util_default_values()