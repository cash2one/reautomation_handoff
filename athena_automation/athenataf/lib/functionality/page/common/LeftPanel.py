from athenataf.lib.util.WebPage import WebPage    
from athenataf.lib.functionality.page.common.AllGroupPage import AllGroupPage
from athenataf.lib.functionality.page.configuration.security.SecurityPage import SecurityPage
from athenataf.lib.functionality.page.configuration.accessPoints.AccessPointsPage import AccessPointsPage
from athenataf.lib.functionality.page.configuration.vpn.VpnPage import VpnPage
from athenataf.lib.functionality.page.configuration.network.NetworkPage import NetworkPage
from athenataf.lib.functionality.page.configuration.services.ServicesPage import ServicesPage
from athenataf.lib.functionality.page.configuration.rf.RfPage import RfPage
from athenataf.lib.functionality.page.configuration.dhcp.DhcpPage import DhcpPage
from athenataf.lib.functionality.page.configuration.wids.WidsPage import WidsPage
from athenataf.lib.functionality.page.configuration.system.SystemPage import SystemPage
from athenataf.lib.functionality.page.maintenance.userManagement.UserManagementPage import UserManagementPage
from athenataf.lib.functionality.page.maintenance.subscription_keys.SubscriptionKeysPage import SubscriptionKeysPage
from athenataf.lib.functionality.page.maintenance.device_management.DeviceManagementPage import DeviceManagementPage
from athenataf.lib.functionality.page.switch.PortsPage import PortsPage
from athenataf.lib.functionality.page.switch.SwitchesPage import SwitchesPage
from athenataf.lib.functionality.page.switch.SwitchVlansPage import SwitchVlansPage
from athenataf.lib.functionality.page.switch.SwitchSystemPage import SwitchSystemPage
from athenataf.lib.functionality.page.maintenance.FirmWarePage import FirmWarePage
from athenataf.lib.functionality.page.reports.ReportsNetworkPage import ReportsNetworkPage
from athenataf.lib.functionality.page.reports.ReportsSecurityPage import ReportsSecurityPage
from athenataf.lib.functionality.page.reports.ReportsPciCompliancePage import ReportsPciCompliancePage
from athenataf.lib.functionality.page.switch.SwitchDhcpPage import SwitchDhcpPage
from athenataf.lib.functionality.page.monitoring.MonitoringPage import MonitoringPage
from athenataf.lib.functionality.page.monitoring.MonitoringAccessPointPage import MonitoringAccessPointPage
from athenataf.lib.functionality.page.monitoring.MonitoringSwitchesPage import MonitoringSwitchesPage
from athenataf.lib.functionality.page.monitoring.MonitoringClientPage import MonitoringClientPage
from athenataf.lib.functionality.page.monitoring.MonitoringWidsPage import MonitoringWidsPage
from athenataf.lib.functionality.page.monitoring.MonitoringEventLogsPage import MonitoringEventLogsPage
from athenataf.lib.functionality.page.monitoring.MonitoringNotificationPage import MonitoringNotificationPage

import time

class LeftPanel(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "DashboardLeftpanel", test, browser, config)
        self.test.assertPageLoaded(self)

    def isPageLoaded(self):
        if self.monitoring:
            return True    
        else:
            return False 
            
    def goto_configuration_page(self):
        self.configuration.click()
        
    def go_to_configuration(self):
        self.configuration.click()
        self.buy_time()
        return AllGroupPage(self.test, self.browser, self.config)
            
    def go_to_security(self):
        time.sleep(4)
        self.security_menu.click()
        if self.save_pop_up:
            self.save_pop_up.click()
            self.security_menu.click()
        return SecurityPage(self.test, self.browser, self.config)

    def go_to_access_points(self):
        self.access_points_menu.click()
        self.buy_time()
        return AccessPointsPage(self.test, self.browser, self.config)
        
    def go_to_vpn(self):
        time.sleep(4)
        self.vpn_menu.click()
        time.sleep(4)
        self.vpn_menu.click()
        if self.save_pop_up:
            self.save_pop_up.click()
            self.vpn_menu.click()
        return VpnPage(self.test, self.browser, self.config)
        
    def go_to_network_page(self):
        self.configuration.click()
        return NetworkPage(self.test, self.browser, self.config)
    
    def go_to_services(self):
        time.sleep(4)
        self.services_menu.click()
        if self.save_pop_up:
            self.save_pop_up.click()
            self.services_menu.click()        
        return ServicesPage(self.test, self.browser, self.config)

    def go_to_rf_page(self):
        time.sleep(4)
        time.sleep(7)
        self.rf_menu.click()
        time.sleep(7)
        self.rf_menu.click()
        return RfPage(self.test, self.browser, self.config)
                
    def go_to_dhcp_page(self):
        time.sleep(4)
        self.dhcp_menu.click()
        if self.save_pop_up:
            self.save_pop_up.click()
            self.dhcp_menu.click()            
        return DhcpPage(self.test, self.browser, self.config)

    def goto_monitoringPage(self):
        self.monitoring.click()
        self.buy_time()
        return MonitoringPage(self.test, self.browser, self.config)

    def go_to_monitoring_access_page(self):
        self.monitoring_access_points.click()
        self.buy_time()
        return MonitoringAccessPointPage(self.test, self.browser, self.config)

    def go_to_monitoring_clients_page(self):
        self.monitoring_clients.click()
        self.buy_time()
        return MonitoringClientPage(self.test, self.browser, self.config)

    def goto_monitoring_notification_page(self):
        self.go_to_monitoring_page()
        self.monitoring_notifications.click()
        time.sleep(2)
        return MonitoringNotificationPage(self.test, self.browser, self.config)
        
    def go_to_monitoring_notification_page(self):
        self.monitoring_notifications.click()
        
    def go_to_monitoring_wids(self):
        self.buy_time()
        self.monitoring_wids.click()
        self.buy_time()
        return MonitoringWidsPage(self.test, self.browser, self.config)
        
    def go_to_wids_page(self):
        time.sleep(4)
        self.wids_menu.click()
        if self.save_pop_up:
            self.save_pop_up.click()
            self.wids_menu.click()
        return WidsPage(self.test, self.browser, self.config)

    def go_to_system_page(self):
        self.system_menu.click()

        return SystemPage(self.test, self.browser, self.config)
    
    def go_to_maintenance(self):
        self.maintenance.click()
        return FirmWarePage(self.test, self.browser, self.config)
        
    def go_to_user_management(self):
        time.sleep(5)
        self.maintenance.click()
        self.buy_time()
        self.user_management.click()
        self.buy_time()
        return UserManagementPage(self.test, self.browser, self.config)

    def go_to_monitoring_page(self):
        self.buy_time()
        self.monitoring.click()
        self.buy_time()
        return MonitoringPage(self.test, self.browser, self.config)

    def go_to_monitoring_access_points(self):
        self.monitoring_access_points.click()
        self.buy_time()
        return MonitoringAccessPointPage(self.test, self.browser, self.config)
        
    def go_to_monitoring_clients_page(self):
        self.monitoring_clients.click()
        self.buy_time()
        return MonitoringClientPage(self.test, self.browser, self.config)

    def goto_monitoring_notification_page(self):
        self.go_to_monitoring_page()
        self.monitoring_notifications.click()
        time.sleep(2)
        return MonitoringNotificationPage(self.test, self.browser, self.config)
    
    
    def go_to_monitoring_event_log_page(self):
        self.monitoring_event_log.click()
        return MonitoringEventLogsPage(self.test, self.browser, self.config)

    
    
    
    def go_to_monitoring_clients(self):
        self.monitoring_clients.click()
        
    def go_to_monitoring_wids(self):
        self.monitoring_wids.click()
        
    def go_to_monitoring_event_log(self):
        self.monitoring_event_log.click()
        
    def go_to_monitoring_notifications(self):
        self.monitoring_notifications.click()

    
    def go_to_monitoring_wids_page(self):
        self.monitoring_wids.click()
        self.buy_time()
        return MonitoringWidsPage(self.test, self.browser, self.config)

    
    def buy_time(self):
        time.sleep(8)

    def assert_delta_config_icon(self):
        import traceback
        # self.buy_time()
        import time
        time.sleep(120)
        self.slider_menu_icon.click()
        if self.expand_plus_button:
            self.expand_plus_button.click()
        else:
            if self.delta_config_icon:
                raise AssertionError("Repeated delta config has been occured.Traceback: %s " %traceback.format_exc())
        self.slider_menu_icon.click()

    def go_to_subscription_keys(self):
        self.buy_time()
        self.maintenance.click()
        self.buy_time()
        self.maintenance_subscription_keys.click()
        self.buy_time()
        return SubscriptionKeysPage(self.test, self.browser, self.config)
        
    def go_to_device_management(self):
        self.buy_time()
        self.maintenance.click()
        self.buy_time()
        self.maintenance_device_management.click()
        self.buy_time()
        return DeviceManagementPage(self.test, self.browser, self.config)
    
    def go_to_switch_configuration(self):
        self.switch_configuration.click()
        return AllGroupPage(self.test, self.browser, self.config)
        
    def go_to_switch_configuration_ports(self):
        self.buy_time()
        self.switch_configuration.click()
        self.buy_time()
        self.ports.click()
        self.buy_time()
        return PortsPage(self.test, self.browser, self.config)
    
    def go_to_switch_configuration_vlans(self):
        self.buy_time()
        self.switch_configuration.click()
        self.buy_time()
        self.vlans.click()
        self.buy_time()
        return SwitchVlansPage(self.test, self.browser, self.config)
    
    def go_to_switch_configuration_system(self):
        self.buy_time()
        self.switch_configuration.click()
        self.buy_time()
        self.system.click()
        self.buy_time()
        return SwitchSystemPage(self.test, self.browser, self.config)
    
    def go_to_reports(self):
        self.reports.click()
        return ReportsNetworkPage(self.test, self.browser, self.config)
    
    def go_to_reports_network(self):
        self.buy_time()
        self.reports.click()
        self.buy_time()
        self.reports_network.click()
        return ReportsNetworkPage(self.test, self.browser, self.config)
    
    def go_to_reports_security(self):
        self.buy_time()
        self.reports.click()
        self.buy_time()
        self.reports_security.click()
        return ReportsSecurityPage(self.test, self.browser, self.config)
    
    def go_to_maintenance_Firmware_page(self):
        self.maintenance.click()
        self.buy_time()
        self.maintenance_firmware.click()
        self.buy_time()
        return FirmWarePage(self.test, self.browser, self.config)
    
    def go_to_reports_pci_compliance(self):
        self.buy_time()
        self.reports.click()
        self.buy_time()
        self.reports_pci_compliance.click()
        return ReportsPciCompliancePage(self.test, self.browser, self.config)
        
    def go_to_switch_configuration_switch(self):
        self.buy_time()
        self.switch_configuration.click()
        self.buy_time()
        self.switches.click()
        self.buy_time()
        return SwitchesPage(self.test, self.browser, self.config)

    def go_to_switch_configuration_dhcp_pools(self):
        self.buy_time()
        self.switch_configuration.click()
        self.buy_time()
        self.dhcp_pools.click()
        self.buy_time()
        return SwitchDhcpPage(self.test, self.browser, self.config)

    def go_to_reports_page(self):
        self.reports.click()

    def go_to_monitoring_switches_page(self):
        self.buy_time()
        self.monitoring.click()
        if self.SwitchesSubMenu:
            self.SwitchesSubMenu.click()
        return MonitoringSwitchesPage(self.test, self.browser, self.config)
        
    def go_to_monitoring_switches_page(self):
        self.buy_time()
        self.monitoring.click()     
        if self.SwitchesSubMenu:
            self.SwitchesSubMenu.click()
        return MonitoringSwitchesPage(self.test, self.browser, self.config)