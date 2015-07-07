from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase

import logging
logger = logging.getLogger('athenataf')

class ReportsTest(AthenaGUITestCase):
 
    def __init__(self, config):
        super(ReportsTest, self).__init__(config)
        self.config = config  
    
    def setUpTestClass(self):
        logger.debug("ReportsTest: setUpTestClass")    
        AthenaGUITestCase.setUpTestClass(self)
        logger.debug("ReportsTest: Go To Maintenance.")
        maintenance_page = self.LeftPanel.go_to_reports()
    
    def assertPageLoaded(self, page_name, msg=None):
        msg = msg or ""
        if page_name.isPageLoaded():
            logger.debug("Page Loaded Successfully")
        else:
            raise AssertionError("%s.\n%s Page does not get loaded" % (msg, page_name))

    def tearDown(self):
        self.LeftPanel.go_to_reports()