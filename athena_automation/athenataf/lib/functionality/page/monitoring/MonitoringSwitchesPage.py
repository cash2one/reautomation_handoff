from athenataf.lib.util.WebPage import WebPage
import traceback
import logging
logger = logging.getLogger('athenataf')
import time
from Device_Module.ObjectModule import Device
class MonitoringSwitchesPage(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "MonitoringSwitches", test, browser, config)
        self.test.assertPageLoaded(self)

    def isPageLoaded(self):
        if self.switches_label:
            return True    
        else:
            return False
            
    def delete_switch_device_based_on_ip(self,device):
        myDevice = Device.getDeviceObject(device)
        switch_ip=myDevice.get("ip")
        if self.browser._browser.find_element_by_xpath("//span[contains(.,'%s')]/../following-sibling::td[5]/a" %switch_ip):
            self.browser._browser.find_element_by_xpath("//span[contains(.,'%s')]/../following-sibling::td[5]/a" %switch_ip).click()
        if self.confirm_delete_switch_ok_button:
            self.confirm_delete_switch_ok_button.click()
        time.sleep(15)
        