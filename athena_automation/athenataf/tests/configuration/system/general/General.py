import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.common import DeviceLibrary
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest
from Device_Module.ObjectModule import Device
import os
import pdb

class General(ConfigurationTest):
	'''
	Test class for System General.
	'''
	
	def test_ath_1412_check_default_values(self):
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.assert_default_values()
		self.take_s2_snapshot()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(None)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1413_vc_name_edit(self):
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.edit_vc_name()
		self.take_s2_snapshot()
		system_page.set_default_vc_name()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1414_vc_ip_edit(self):
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.edit_vc_ip()
		self.take_s2_snapshot()
		self.assert_s1_s2_diff(0)
		self.clear()
		
	def test_ath_1415_nondefault_dynamic_radius_proxy_and_mas(self):
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.set_nondefault_proxy_and_mas()
		system_page.assert_nondefault_proxy_and_mas()
		self.take_s2_snapshot()
		system_page.set_default_proxy_and_mas()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1416_ntp_server(self):
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.set_ntp_server_ip('wrong')
		system_page.assert_ntp_server_error_msg()
		system_page.set_ntp_server_ip('right')
		self.take_s2_snapshot()
		system_page.set_ntp_server_ip()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1417_timezone_changed_value(self):
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.set_dropdown_value_nondefault('timezone')
		system_page.assert_dropdown_nondefault_value('timezone')
		self.take_s2_snapshot()
		system_page.set_dropdown_value_default('timezone')
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1418_preferred_band_changed_value(self):
		system_page = self.LeftPanel.go_to_system_page()
		system_page.set_dropdown_value_default('preferred band')
		self.take_s1_snapshot("show_summary_Band")
		system_page = self.LeftPanel.go_to_system_page()
		system_page.set_dropdown_value_nondefault('preferred band')
		system_page.assert_dropdown_nondefault_value('preferred band')
		self.take_s2_snapshot("show_summary_Band")
		system_page.set_dropdown_value_default('preferred band')
		self.take_s3_snapshot("show_summary_Band")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1419_auto_join_mode_changed_value(self):
		self.take_s1_snapshot("show_summary")
		system_page = self.LeftPanel.go_to_system_page()
		system_page.set_dropdown_value_nondefault('auto join mode')
		system_page.assert_dropdown_nondefault_value('auto join mode')
		self.take_s2_snapshot("show_summary")
		system_page.set_dropdown_value_default('auto join mode')
		self.take_s3_snapshot("show_summary")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1420_terminal_access_changed_value(self):
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.set_dropdown_value_nondefault('terminal access')
		system_page.assert_dropdown_nondefault_value('terminal access')
		self.take_s2_snapshot()
		system_page.set_dropdown_value_default('terminal access')
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(8)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1421_led_display_changed_value(self):
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.set_dropdown_value_nondefault('led display')
		system_page.assert_dropdown_nondefault_value('led display')
		self.take_s2_snapshot()
		system_page.set_dropdown_value_default('led display')
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1422_extended_ssid_changed_value(self):

		system_page = self.LeftPanel.go_to_system_page()
		# system_page.set_dropdown_value_default('extended ssid')
		self.take_s1_snapshot("show_summary_extended_ssid")
		system_page.set_dropdown_value_nondefault('extended ssid')
		system_page.assert_dropdown_nondefault_value('extended ssid')
		self.take_s2_snapshot("show_summary_extended_ssid")
		system_page.set_dropdown_value_default('extended ssid')
		self.take_s3_snapshot("show_summary_extended_ssid")
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1423_deny_inter_using_bridging_changed_value(self):
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.set_dropdown_value_nondefault('deny inter')
		system_page.assert_dropdown_nondefault_value('deny inter')
		self.take_s2_snapshot()
		system_page.set_dropdown_value_default('deny inter')
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_1424_deny_local_routing_changed_value(self):
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.set_dropdown_value_nondefault('deny local routing')
		system_page.assert_dropdown_nondefault_value('deny local routing')
		self.take_s2_snapshot()
		system_page.set_dropdown_value_default('deny local routing')
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8304_telnet_server_non_default_value(self):
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.set_dropdown_value_nondefault('telnet server')
		system_page.assert_dropdown_nondefault_value('telnet server')
		self.take_s2_snapshot()
		system_page.set_dropdown_value_default('telnet server')
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8305_virtual_controller_non_default_value(self):
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.assert_virtual_controller_values()
		system_page.configure_virtual_controller_values()
		self.take_s2_snapshot()
		system_page.restore_virtual_controller_values()
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_8307_dynamic_cpu_utilization_non_default_value(self):
		self.take_s1_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.set_dropdown_value_nondefault('dynamic cpu utilization disabled')
		system_page.assert_dropdown_nondefault_value('dynamic cpu utilization disabled')
		system_page.set_dropdown_value_nondefault('dynamic cpu utilization enabled')
		system_page.assert_dropdown_nondefault_value('dynamic cpu utilization enabled')
		import time
		time.sleep(20)
		self.take_s2_snapshot()
		system_page.set_dropdown_value_default('dynamic cpu utilization')
		self.take_s3_snapshot()
		self.assert_s1_s2_diff(0)
		self.assert_s1_s3_diff()
		self.clear()
		
	def test_ath_11046_check_non_default_values_vc_name(self):
		myDevice = Device.getDeviceObject("IAP_1")
		vlan_id = myDevice.get("vlan")
		conf = self.config.config_vars
		system_page = self.LeftPanel.go_to_system_page()
		system_page.set_new_vc_name("IAP_1",conf.vc_name)
		system_page.set_new_vc_ip("IAP_1",conf.ip_add)
		system_page.check_non_default_values_vc_name_2()
		system_page._save_settings()
		system_page.assert_system_page_vc_field_values("IAP_1","sh ru | inc name",conf.vc_name)
		system_page.assert_system_page_vc_field_values("IAP_1","sh ru | inc virtual",conf.ip_add)
		system_page.assert_system_page_vc_field_values("IAP_1","sh ru | inc time","Pacific-Time -07")
		system_page.assert_system_page_vc_field_values("IAP_1","sh ru | inc ntp",conf.ntp_server)
		system_page.assert_system_page_vc_field_values("IAP_1","sh ru | inc band","2.4ghz")
		system_page.assert_system_page_vc_field_values("IAP_1","sh ru | inc vlan",vlan_id)
		system_page.assert_system_page_vc_field_values("IAP_1","sh ru | inc cpu","dynamic-cpu-mgmt disable")
		
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
		# system_page.setting_original_vc_name("IAP_1",conf.vc_name)
		# system_page.setting_original_vc_ip("IAP_1",conf.ip_add)
		system_page.setting_default_values_2()
		system_page._save_settings()

	def test_ath_11303_dynamic_cpu_and_telnet_server(self):
		'''
		Snapshot command is remaining for multiple devices
		'''
		conf = self.config.config_vars
		system_page = self.LeftPanel.go_to_system_page()
		os.environ['device'] = "IAP_1"
		self.take_s1_snapshot()
		os.environ['device'] = "IAP_2"
		self.take_s1_snapshot()
		system_page.check_non_default_values_vc_name()
		system_page._save_settings()
		system_page.set_dropdown_nondefault_value(conf.sys_disable,conf.sys_disable,conf.sys_enable,conf.sys_disable,conf.sys_disable,conf.sys_enable,conf.sys_enable,conf.sys_enable,conf.sys_enable,timezone1=None,band=None,utilization=None)
		system_page._save_settings()
		system_page.buy_time_2()
		DeviceLibrary.getPrompt("IAP_1")
		DeviceLibrary.connect_device_to_server("IAP_1")
		system_page.buy_time_2()
		DeviceLibrary.getPrompt("IAP_2")
		DeviceLibrary.connect_device_to_server("IAP_2")
		self.browser.refresh()
		os.environ['device'] = "IAP_1"
		self.take_s2_snapshot()
		os.environ['device'] = "IAP_2"
		self.take_s2_snapshot()
		system_page = self.LeftPanel.go_to_system_page()
		system_page.setting_default_values()
		system_page.set_dropdown_default_value()
		system_page._save_settings()
		system_page.buy_time_2()
		DeviceLibrary.getPrompt("IAP_1")
		DeviceLibrary.connect_device_to_server("IAP_1")
		system_page.buy_time_2()
		DeviceLibrary.getPrompt("IAP_2")
		DeviceLibrary.connect_device_to_server("IAP_2")
		os.environ['device'] = "IAP_1"
		self.take_s3_snapshot()
		os.environ['device'] = "IAP_2"
		self.take_s3_snapshot()
		os.environ['device'] = "IAP_1"
		self.assert_s1_s2_diff(0)
		os.environ['device'] = "IAP_2"
		self.assert_s1_s2_diff(0)
		os.environ['device'] = "IAP_1"
		self.assert_s1_s3_diff()
		os.environ['device'] = "IAP_2"
		self.assert_s1_s3_diff()
		