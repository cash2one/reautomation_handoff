import logging
logger = logging.getLogger('athenataf')
from athenataf.lib.functionality.test.ConfigurationTest import ConfigurationTest
import time
from athenataf.lib.functionality.common import DeviceLibrary
from Device_Module.ObjectModule import Device

class Multiversion(ConfigurationTest):
    '''
    Test class for Multiversion.
    '''

    def test_ath_10985_downgrade_41_iap_to_40_iap(self):
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_network_if_present()
        # self.take_s1_snapshot()
        conf = self.config.config_vars
        # self.take_s1_snapshot("show_version")
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.select_virtual_controller()
        security.configure_security_level(enterprise=True)
        security.configure_security_radio_fields(okc=True)
        security.enable_fast_roaming_option('802.11r')
        security.enable_fast_roaming_option('802.11k')
        security.enable_fast_roaming_option('802.11v')
        access = security.return_acces_page()
        access.click_role_access()
        access.delete_default_rule_if_present()
        access.create_multiple_app_category_rules()
        access.finish_network_setup()
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.select_first_vc()
        firmware_page.clicking_on_upgrade_firmware()
        firmware_page.setting_firmware_upgrade_manual_option(option=conf.version_type_value_2,version=conf.firmware_upgrade_version)
        firmware_page.upgrade_firmware()
        firmware_page.buy_time()
        DeviceLibrary.connect_device_to_server('IAP_1')
        firmware_page.assert_firmware_version('IAP_1',conf.firmware_upgrade_version)
        # self.take_s2_snapshot()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_network_if_present()
        firmware_page = self.LeftPanel.go_to_maintenance_Firmware_page()
        firmware_page.select_first_vc()
        firmware_page.clicking_on_upgrade_firmware()
        firmware_page.setting_firmware_upgrade_manual_option(option=conf.version_type_value_2,version=conf.firmware_base_version)
        firmware_page.click_post_firmware_upgrade()
        firmware_page.buy_time()
        DeviceLibrary.connect_device_to_server("IAP_1")
        # self.take_s3_snapshot()
        # self.assert_s1_s2_diff(0)
        # self.assert_s1_s3_diff()
        # self.clear()
        
        
    def test_ath_11004_configure_gre_per_ap_tunnel_in_a_mixed_group(self):
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_network_if_present()
        import os
        os.environ['device'] = "IAP_1"
        self.take_s1_snapshot()
        import os
        os.environ['device'] = "IAP_2"
        self.take_s1_snapshot()
        conf = self.config.config_vars
        basic_info = self.NetworkPage.create_new_network()
        virtual_lan = basic_info.employee_network_info()
        security = virtual_lan.select_virtual_controller()
        security.configure_security_level(enterprise=True)
        security.configure_security_radio_fields(okc=True)
        security.enable_fast_roaming_option('802.11r')
        security.enable_fast_roaming_option('802.11k')
        security.enable_fast_roaming_option('802.11v')
        access = security.return_acces_page()
        access.finish_network_setup()
        vpn_obj = self.LeftPanel.go_to_vpn()
        vpn_obj.set_protocol(conf.vpn_ArubaGre_protocol)
        vpn_obj.set_primary_host_field(conf.vcip,'false')
        vpn_obj.set_backup_host(conf.vcip1,'false')
        vpn_obj.set_per_ap_tunnel('true')
        vpn_obj.save_settings()
        os.environ['device'] = "IAP_1"
        self.take_s2_snapshot()
        os.environ['device'] = "IAP_2"
        self.take_s2_snapshot()
        vpn_obj.set_backup_host('','false')
        vpn_obj.set_primary_host_field('','true')
        vpn_obj.restore_Ipsec_default()
        self.LeftPanel.go_to_network_page()
        self.NetworkPage.delete_network_if_present()
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
    # def configure_deny_inter_user_bridging(self,ap):
        # import time
        # myDevice = Device.getDeviceObject(ap)
        # myDevice.receive("#")
        # myDevice.transmit("configure terminal")
        # myDevice.receive("(config) #") comment this
        # time.sleep(4)
        # myDevice.receive("#")
        # myDevice.transmit("wlan ssid-profile em1")
        # time.sleep(4)
        # myDevice.receive("#")
        # myDevice.transmit("deny-inter-user-bridging")
        # time.sleep(4)
        # myDevice.receive("#")
        # myDevice.transmit("end")
        # time.sleep(4)
        # myDevice.receive("#")
        # myDevice.transmit("commit apply")
        # time.sleep(4)
        # myDevice.receive("#")       
        # raw_input('watot')def configure_deny_inter_user_bridging(self,ap):
        # import time
        # myDevice = Device.getDeviceObject(ap)
        # myDevice.receive("#")
        # myDevice.transmit("configure terminal")
        # myDevice.receive("(config) #") comment this
        # time.sleep(4)
        # myDevice.receive("#")
        # myDevice.transmit("wlan ssid-profile em1")
        # time.sleep(4)
        # myDevice.receive("#")
        # myDevice.transmit("deny-inter-user-bridging")
        # time.sleep(4)
        # myDevice.receive("#")
        # myDevice.transmit("end")
        # time.sleep(4)
        # myDevice.receive("#")
        # myDevice.transmit("commit apply")
        # time.sleep(4)
        # myDevice.receive("#")       
        # raw_input('watot')
        
    def assert_running_config_include_deny(self,ap,denyconfig='',exists=False):
        myDevice = Device.getDeviceObject(ap)   
        myDevice.receive("#")
        time.sleep(8)
        myDevice.transmit("sh ru | inc deny")
        time.sleep(8)
        output = myDevice.receive("#")
        if not exists:
            if denyconfig in output:
                raise AssertionError("%s is pushed to %s" %(denyconfig,ap))
        else:
            if not denyconfig in output:
                raise AssertionError("%s is not pushed to %s" %(denyconfig,ap))
            
            
    def test_ath_10984_attach_iap_with_deny_inter_user_bridging_and_deny_local_routing_options(self):
        conf = self.config.config_vars
        DeviceLibrary.disconnect_device_from_server('IAP_2')
        DeviceLibrary.factoryReset('IAP_2')
        time.sleep(350)
        DeviceLibrary.configure_deny_inter_user_bridging_and_deny_local_routing('IAP_2')
        DeviceLibrary.connect_device_to_server('IAP_2')
        time.sleep(400)
        self.browser.refresh()
        inner_left_panel = self.TopPanel.click_slider_icon()
        inner_left_panel.select_unprovision_iap()
        manage_group_page = inner_left_panel.click_configuration_page_existing_group_button()
        manage_group_page.move_unprovisioned_device('IAP_2',group_name='group1')
        time.sleep(20)
        DeviceLibrary.reconnect('IAP_2')
        time.sleep(400)
        self.assert_running_config_include_deny('IAP_2','deny-inter-user-bridging')
        time.sleep(20)
        self.assert_running_config_include_deny('IAP_2','deny-local-routing')
        time.sleep(20)
        DeviceLibrary.disconnect_device_from_server('IAP_2')
        DeviceLibrary.factoryReset('IAP_2')
        time.sleep(350)
        DeviceLibrary.configure_deny_inter_user_bridging_and_deny_local_routing('IAP_2')
        DeviceLibrary.connect_device_to_server('IAP_2')
        time.sleep(400)
        self.browser.refresh()
        inner_left_panel = self.TopPanel.click_slider_icon()
        inner_left_panel.select_unprovision_iap()
        create_group_page = inner_left_panel.click_configuration_page_new_group_button()
        create_group_page.move_unprovisional_device_to_new_group('group2')
        time.sleep(20)
        DeviceLibrary.reconnect('IAP_2')
        time.sleep(400)
        self.assert_running_config_include_deny('IAP_2','deny-inter-user-bridging',exists=True)
        time.sleep(20)
        self.assert_running_config_include_deny('IAP_2','deny-local-routing',exists=True)
        
        self.browser.refresh()
        inner_left_panel = self.TopPanel.click_slider_icon()
        manage_group_page = inner_left_panel.manage_group()
        manage_group_page.move_vc_to_group('group2','IAP_1')
        time.sleep(20)
        # DeviceLibrary.connect_device_to_server('IAP_2')
        # time.sleep(700)
        # self.assert_running_config_include_deny('IAP_2','deny-inter-user-bridging',exists=True)
        # self.assert_running_config_include_deny('IAP_2','deny-local-routing',exists=True)