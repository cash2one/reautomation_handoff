from athenataf.lib.functionality.test.AthenaGUITestCase import AthenaGUITestCase
# from athenataf.lib.functionality.page.configuration.network.NetworkPage import NetworkPage
# from athenataf.lib.functionality.page.configuration.accessPoints.AccessPointsPage import AccessPointsPage
from athenataf.lib.functionality.page.maintenance.device_management.DeviceManagementPage import DeviceManagementPage
import time
import logging
logger = logging.getLogger('athenataf')    

class DeviceManagementTest(AthenaGUITestCase):

    def __init__(self, config):
        super(DeviceManagementTest, self).__init__(config)
        self.NetworkPage = None
        self.config = config
        
    # def setUp(self):
        # code to license the device if manage license pop's up before ui
        # try:
            # if inner_left_panel.manage_license:
                # inner_left_panel.manage_license.click()
                # time.sleep(10)
                # device_management_page = self.LeftPanel.go_to_device_management()
                # device_management_page.search_device_using_mac_address()
                # logger.debug("DeviceManagement Page : Changing device to assigned. ")
                # device_management_page.device_selector_1.click()
                # device_management_page.click_assign_license_button()
                # logger.debug("DeviceManagement Page : Clicking on 'Assign' button.. ")
                # if device_management_page.assign_button_enable:
                    # device_management_page.assign_button_enable.click()
        # except:
            # pass
            
    def setUpTestClass(self, IAP=False):
        logger.debug("DeviceManagementTest: setUpTestClass")    
        AthenaGUITestCase.setUpTestClass(self, IAP)
        # inner_left_panel = self.TopPanel.click_slider_icon()
        # code to delete the groups 
        # if inner_left_panel.assert_group_is_present_or_not(inner_left_panel.group1_with_vc):
            # manage_group = inner_left_panel.manage_group()
            # manage_group.move_virtual_controller_from_Mygroup(group1=True)
            # manage_group = inner_left_panel.manage_group()
            # manage_group.delete_group1()
        # elif inner_left_panel.assert_group_is_present_or_not(inner_left_panel.group1_without_vc):
            # manage_group = inner_left_panel.manage_group()
            # manage_group.delete_group1()
        # elif inner_left_panel.assert_group_2():
            # manage_group_page = inner_left_panel.manage_group()
            # manage_group_page.delete_empty_group2()
        # if inner_left_panel.group_close_icon:
            # inner_left_panel.click_on_close_icon()
            # time.sleep(4)
            
            

    def assertPageLoaded(self, page_name, msg=None):
        msg = msg or ""
        if page_name.isPageLoaded():
            logger.debug("Page Loaded Successfully")
        else:
            raise AssertionError("%s.\n%s Page does not get loaded" % (msg, page_name))

    def tearDown(self):
        # self.browser.refresh()
        # import time
        # time.sleep(10)
        # self.browser.refresh()
        try:
            device_management_page = self.LeftPanel.go_to_device_management()
        except:
            self.LeftPanel.go_to_maintenance()
            device_management_page = self.LeftPanel.go_to_device_management()
        device_management_page.search_device_using_mac_address()
        logger.debug("DeviceManagement Page : Changing device to assigned. ")
        if device_management_page.unassigned_licence_text:      
            device_management_page.device_selector_1.click()
            device_management_page.click_assign_license_button()
            logger.debug("DeviceManagement Page : Clicking on 'Assign' button.. ")
            if device_management_page.assign_button_enable:
                device_management_page.assign_button_enable.click()