from athenataf.lib.util.WebPage import WebPage
import traceback
import logging
logger = logging.getLogger('athenataf')

class VLANsPage(WebPage):
    def __init__(self, test, browser, config):
        WebPage.__init__(self, "VLANs", test, browser, config)
        self.test.assertPageLoaded(self)
        
        
    def isPageLoaded(self):
        if self.new_vlan:
            return True    
        else:
            return False