from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase

import logging
logger = logging.getLogger('athenataf')

class MaintenanceTest(AthenaGUITestCase):
 
    def __init__(self, config):
        super(MaintenanceTest, self).__init__(config)
        self.config = config  
    
    def setUpTestClass(self):
        logger.debug("MaintenanceTest: setUpTestClass")    
        AthenaGUITestCase.setUpTestClass(self)
        logger.debug("MaintenanceTest: Go To Maintenance.")
        maintenance_page = self.LeftPanel.go_to_maintenance()
    
    def assertPageLoaded(self, page_name, msg=None):
        msg = msg or ""
        if page_name.isPageLoaded():
            logger.debug("Page Loaded Successfully")
        else:
            raise AssertionError("%s.\n%s Page does not get loaded" % (msg, page_name))

    def tearDown(self):
		if not self.only_close_browser:
			if self.LeftPanel.save_pop_up:
				self.LeftPanel.save_pop_up.click()
				import time
				time.sleep(10)
			self.LeftPanel.configuration.click()
		else: pass