from athenataf.lib.util.WebPage import WebPage
from athenataf.lib.functionality.page.configuration.network.BasicInfoPage import BasicInfoPage
from athenataf.lib.functionality.page.configuration.network.EditNetworkPage import EditNetworkPage
from athenataf.lib.functionality.page.configuration.network.EditWiredNetworkPage import EditWiredNetworkPage
import traceback
import logging
logger = logging.getLogger('athenataf')
import time

class NetworkPage(WebPage):
    def __init__(self, test, browser, config):
        time.sleep(5)
        WebPage.__init__(self, "Networks", test, browser, config)
        self.test.assertPageLoaded(self)
        
        
    def isPageLoaded(self):
        if self.createnetwork:
            return True    
        else:
            return False 
            
    def create_new_network(self):
        #if self.group_close_icon:
        #    logger.debug("NetworkPage: Clicking on Group Close icon button")
        #    self.group_close_icon.click()
        #    time.sleep(5)
        logger.debug("NetworkPage: Clicking on CreateNetwork button")
        self.createnetwork.click()
        self.buy_time()
        return BasicInfoPage(self.test, self.browser, self.config)

    def assert_new_network(self, expected_network_name = "test1"):
        logger.info("Verifying Newly Created Network: %s existence at networks table." %expected_network_name)
        time.sleep(5)
        network_name_existing = False
        network_table_entries = self.browser._browser.find_elements_by_xpath("//table[@id='wireless-config-networkstable']/tbody/tr/td[1]")
        for entry in network_table_entries:
            if expected_network_name == entry.text:
                network_name_existing = True
                break
        if not network_name_existing:
            logger.info("FAIL: Created Network is not existing at networks table.")
            raise AssertionError("Newly Created network is missing in networks table")
        else:
            logger.info("PASS: Created Network \"%s\"is existing at networks table." %expected_network_name)
            return True
        
    def assert_wired_network(self):
        if self.wired_network:
            return True
        else:
            raise AssertionError("Wired network %s setup failed .Traceback: %s " %(self.wired_network,traceback.format_exc()))
        
    def assert_wired_network_2(self):
        if self.wired_network2:
            return True
        else:
            raise AssertionError("Wired network %s setup failed .Traceback: %s " %(self.wired_network2,traceback.format_exc()))
            
    def buy_time(self):
        time.sleep(20)
                    
    def delete_network_if_present(self, network_name="test1"):
        '''
        Delete network i.e wpa2 or wpa2_wpa if present.
        '''
        #if self.left_panel_add_button:
        #import pdb
        #pdb.set_trace()
        #if self.group_controls:
        #    logger.debug("NetworkPage: Clicking on  left panel close button ")
            #self.left_panel_close_button.click()
        #    self.left_panel_close_group_button.click()
        try:
            self.browser._browser.\
                find_element_by_xpath("//table[@id='wireless-config-networkstable']/tbody/tr/td[@title ='%s']/following-sibling::td[4]/div/a[2]" %network_name).click()
            time.sleep(1)
            self.browser.accept_alert()
            time.sleep(1)
        except:
            pass
            
    def delete_all_networks(self):
        '''
        Delete non-default networks
        '''
        logger.debug("NetworkPage: Delete the existing non-default networks")
        current_networks = self.browser._browser.find_elements_by_xpath("//a[contains(@id,'delete_network_button_') and @class='icosolo delete icon_delete ng-scope']")
        while not current_networks == []:
            current_networks[0].click()
            self.browser.accept_alert()
            time.sleep(2)
            current_networks = self.browser._browser.find_elements_by_xpath("//a[contains(@id,'delete_network_button_') and @class='icosolo delete icon_delete ng-scope']")


    def delete_wired_network_if_present(self):
        time.sleep(8)
        if self.left_panel_add_button:
            logger.debug("NetworkPage: Clicking on  left panel close button ")
            self.left_panel_close_button
        if self.wired_network:
            logger.debug("NetworkPage: Clicks on  Wired Network  ")
            self.wired_network.click()
            logger.debug("NetworkPage: Clicks on  Delete button  ")
            self.new_wired_network_delete_button.click()
            logger.debug("NetworkPage: Clicks on ok")
            self.browser.accept_alert()
        self.buy_time()
        
    def delete_wired2_network_if_present(self):    
        if self.left_panel_add_button:
            logger.debug("NetworkPage: Clicking on  left panel close button ")
            self.left_panel_close_button
        if self.wired_network2:
            logger.debug("NetworkPage: Clicks on existing Wired network")
            self.wired_network2.click()
            logger.debug("NetworkPage: Clicks on  Delete button  ")
            self.delete_wired.click()
            logger.debug("NetworkPage: Clicks on ok")
            self.browser.accept_alert()
        self.buy_time()
        
    def change_port_settings(self):
        if self.wired_network:
            logger.debug("NetworkPage: Clicks on  Wired Network  ")
            self.wired_network.click()
            logger.debug("NetworkPage: Clicks on  Wired Network Edit button ")
            self.edit_wired.click()    
            if self.uplink:
                logger.debug("NetworkPage: Clicks on  Network Network Assignment Accordion   ")
                self.network_accor.click()
                if self.network_drop.get_selected() == self.config.config_vars.Network_name :
                    logger.debug("NetworkPage: setting  default wired port profile  ")
                    self.network_drop.set(self.config.config_vars.default_assign_port)
                    logger.debug("NetworkPage: Clicks on  Save button ")
                    self.save.click()    
                    
        
    def edit_network(self):
        self.buy_time()
        logger.debug("NetworkPage: Clicking on created network")
        # self.network_name.click()
        logger.debug("NetworkPage: Clicks on  Edit button ")
        self.edit.click()
        self.buy_time()
        return EditNetworkPage(self.test, self.browser, self.config)
    
    def assert_editable_default_wired_port(self):
        '''
            Asserts wired_port network is editable in network page.
        '''
        if self.def_wired_port  :
            logger.debug("NetworkPage: Clicks on  default wired port profile ")
            self.def_wired_port.click()
            if self.edit_port_profile:
                return True
            else:
                raise AssertionError("Exception occured in identification of button  i.e %s button . Traceback: %s" % (self.edit, traceback.format_exc()))
        else:
            raise AssertionError("Exception occured in identification of default network  i.e %s  . Traceback: %s" % (self.def_wired_port , traceback.format_exc()))


    def assert_editable_default_wired_instant(self):
        '''
            Asserts wired_instant network is editable in network page.
        '''
        if  self.wired_instant :
            logger.debug("NetworkPage: Clicks on wired instant ")
            self.wired_instant.click()
            if self.edit_instant:
                return True
            else:
                raise AssertionError("Exception occured in identification of button  i.e %s button . Traceback: %s" % (self.edit_instant, traceback.format_exc()))
            
        else:
            raise AssertionError("Exception occured in identification of default network  i.e %s . Traceback: %s" % (self.wired_instant, traceback.format_exc()))
        
    def edit_wired_network(self):
        logger.debug("NetworkPage: Clicks on  Wired Network  ")
        self.wired_network.click()
        self.buy_time()
        logger.debug("NetworkPage: Clicks on  Wired Network Edit button ")
        self.edit_wired.click()
        self.buy_time()
        return EditWiredNetworkPage(self.test, self.browser, self.config)
        
    def assert_network_not_exist(self):
        if not self.network_name:
            return True
        else:
            raise AssertionError("New network %s deletion failed .Traceback: %s " %(self.new_network,traceback.format_exc()))
            
    def delete_new_network_if_present(self):
        '''
        Delete network i.e wpa2 or wpa2_wpa if present.
        '''
        if self.left_panel_add_button:
            logger.debug("NetworkPage: Clicking on  left panel close button ")
            self.left_panel_close_button
        if self.new_network_name:
            logger.debug("NetworkPage: Clicks on existing  network")
            self.new_network_name.click()
            logger.debug("NetworkPage: Clicks on existing  network delete Button")
            self.new_network_delete_button.click()
            logger.debug("NetworkPage: Clicks on ok")
            self.browser.accept_alert()
            self.buy_time()
            
    def edit_new_network(self):
        self.new_network_name.click()
        self.new_edit.click()
        return EditNetworkPage(self.test, self.browser, self.config)
        
    def delete_custom_guest_network_if_present(self):
        '''
        Delete custom guest network if present.
        '''
        if self.left_panel_add_button:
            logger.debug("NetworkPage: Clicking on  left panel close button ")
            self.left_panel_close_button
        if self.custom_guest_network:
            self.buy_time()
            logger.debug("NetworkPage: Clicks on existing guest wired network")
            self.custom_guest_network.click()
            logger.debug("NetworkPage: Clicks on existing guest wired network delete button")
            self.delete_wired_network1.click()
            logger.debug("NetworkPage: Clicks on ok")
            self.browser.accept_alert()
            self.buy_time()
    
    def delete_wired_network_new(self):
        if self.left_panel_add_button:
            logger.debug("NetworkPage: Clicking on  left panel close button ")
            self.left_panel_close_button
        if self.network_name1:
            logger.debug("NetworkPage: Clicks on existing  wired network")
            self.network_name1.click()
            logger.debug("NetworkPage: Clicks on existing  wired network delete button")
            self.delete_wired_network1.click()
            logger.debug("NetworkPage: Clicks on ok")
            self.browser.accept_alert()
            self.buy_time()

    def assert_new_test_network(self):
        if self.new_test_network_name:
            return True
        else:
            raise AssertionError("New network %s setup failed .Traceback: %s " %(self.new_network,traceback.format_exc()))

    def delete_new_test_network_if_present(self):
        '''
        Delete network i.e wpa2 or wpa2_wpa if present.
        '''
        if self.left_panel_add_button:
            logger.debug("NetworkPage: Clicking on  left panel close button ")
            self.left_panel_close_button
        if self.new_test_network_name:
            logger.debug("NetworkPage: Clicks on existing  network")
            self.new_test_network_name.click()
            logger.debug("NetworkPage: Clicks on existing network delete button")
            self.new_test_delete_network_button.click()
            logger.debug("NetworkPage: Clicks on ok")
            self.browser.accept_alert()
            self.buy_time()
            
    def assert_wireless_network_overview(self):
        logger.debug("Selecting the exixting wireless network.")
        self.network_name.click()
        logger.debug("Validating the existing fields in the network overview.")
        if not self.network_name and self.general_primary_usage and self.eneral_security_level:
            raise AssertionError("The displayed information is not correct. Traceback: %s " %(self.new_network,traceback.format_exc()))
        self.buy_time()
            
    def delete_wired_network(self):
        if self.left_panel_add_button:
            logger.debug("NetworkPage: Clicking on  left panel close button ")
            self.left_panel_close_button
        logger.debug("NetworkPage: Selecting network with name 'Test1949'")
        self.wired_network_name.click()
        logger.debug("NetworkPage: Clicking delete button")
        self.wired_network_delete.click()
        logger.debug("NetworkPage: Clicks on ok")
        self.browser.accept_alert()
        self.buy_time()

    def delete_specific_wired_network_if_present(self,name):
        time.sleep(8)
        if self.left_panel_add_button:
            logger.debug("NetworkPage: Clicking on  left panel close button ")
            self.left_panel_close_button
        if name == 'network1':
            if self.wired_network_1:
                logger.debug("NetworkPage: Clicks on existing wired network")
                self.wired_network_1.click()
                logger.debug("NetworkPage: Clicks on existing network delete button")
                self.wired_network_1_delete.click()
                logger.debug("NetworkPage: Clicks on ok")
                self.browser.accept_alert()
                self.buy_time()
        if name == 'network2':
            if self.wired_network_2:
                logger.debug("NetworkPage: Clicks on existing wired network")
                self.wired_network_2.click()
                logger.debug("NetworkPage: Clicks on existing network delete button")
                self.wired_network_2_delete.click()
                logger.debug("NetworkPage: Clicks on ok")
                self.browser.accept_alert()
                self.buy_time()
        if name == 'network3':
            if self.wired_network_3:
                logger.debug("NetworkPage: Clicks on existing wired network")
                self.wired_network_3.click()
                logger.debug("NetworkPage: Clicks on existing network delete button")
                self.wired_network_3_delete.click()
                logger.debug("NetworkPage: Clicks on ok")
                self.browser.accept_alert()
                self.buy_time()
        if name == 'network4':
            if self.wired_network_4:
                logger.debug("NetworkPage: Clicks on existing wired network")
                self.wired_network_4.click()
                logger.debug("NetworkPage: Clicks on existing network delete button")
                self.wired_network_4_delete.click()
                logger.debug("NetworkPage: Clicks on ok")
                self.browser.accept_alert()
                self.buy_time()        

    def edit_new_wired_network_4(self):
        logger.debug("NetworkPage: Clicks on existing wired network")
        self.wired_network_4.click()
        self.buy_time()
        logger.debug("NetworkPage: Clicks on wired network Edit button")
        self.edit_wired_network_4.click()
        self.buy_time()
        return EditWiredNetworkPage(self.test, self.browser, self.config)
        
    def delete_new_wired_network(self):
        if self.left_panel_add_button:
            logger.debug("NetworkPage: Clicking on  left panel close button ")
            self.left_panel_close_button
        if self.wired_network_name:
            logger.debug("NetworkPage: Selecting network with name 'Test1949'")
            self.wired_network_name.click()
            logger.debug("NetworkPage: Clicking delete button")
            self.wired_network_delete.click()
            logger.debug("NetworkPage: Clicks on ok")
            self.browser.accept_alert()
            self.buy_time()
            
    def delete_test_1934_if_present(self):
        time.sleep(8)
        if self.left_panel_add_button:
            logger.debug("NetworkPage: Clicking on  left panel close button ")
            self.left_panel_close_button
        if self.new_test_1934_network:
            logger.debug("NetworkPage: Selecting network with name 'Test1934'")
            self.new_test_1934_network.click()
            logger.debug("NetworkPage: Clicking delete button")
            self.new_test_1934_delete_button.click()
            logger.debug("NetworkPage: Clicks on ok")
            self.browser.accept_alert()
        self.buy_time()

    def assert_test_1934_network(self):
        if self.new_test_1934_network:
            return True
        else:
            raise AssertionError("New Test1934 setup failed .Traceback: %s " %(self.new_network,traceback.format_exc()))
            
            
    def delete_new_wired_network_1948(self):
        '''
        Delete new Wired network 1948
        '''
        if self.wired_network_1948:
            logger.debug("NetworkPage: Selecting network with name 'Test1949'")
            self.wired_network_1948.click()
            logger.debug("NetworkPage: Clicking delete button")
            self.wired_network_1948_delete.click()
            logger.debug("NetworkPage: Clicks on ok")
            self.browser.accept_alert()
            self.buy_time()
            
    def delete_specific_network_if_present(self,name):
        '''
        Deletes specific network.
        '''
        time.sleep(8)
        if name == 'network1':
            if self.wired_network_1_delete:
                logger.debug("NetworkPage: Clicks on existing network delete button")
                self.wired_network_1_delete.click()
                logger.debug("NetworkPage: Clicks on ok")
                self.browser.accept_alert()
                self.buy_time()
        if name == 'network2':
            if self.wired_network_2_delete:
                logger.debug("NetworkPage: Clicks on existing network delete button")
                self.wired_network_2_delete.click()
                logger.debug("NetworkPage: Clicks on ok")
                self.browser.accept_alert()
                self.buy_time()
        if name == 'network3':
            if self.wired_network_3_delete:
                logger.debug("NetworkPage: Clicks on existing network delete button")
                self.wired_network_3_delete.click()
                logger.debug("NetworkPage: Clicks on ok")
                self.browser.accept_alert()
                self.buy_time()
        if name == 'network4':
            if self.wired_network_4_delete:
                logger.debug("NetworkPage: Clicks on existing network delete button")
                self.wired_network_4_delete.click()
                logger.debug("NetworkPage: Clicks on ok")
                self.browser.accept_alert()
                self.buy_time()
    
    def delete_guest_nw1_if_present(self):
        '''
        Delete network i.e wpa2 or wpa2_wpa if present.
        '''
        if self.left_panel_add_button:
            logger.debug("NetworkPage: Clicking on  left panel close button ")
            self.left_panel_close_button
        if self.guest_nw1:
            logger.debug("NetworkPage: Clicks on existing  network")
            self.guest_nw1.click()
            logger.debug("NetworkPage: Clicks on existing  network delete Button")
            self.guest_nw1_delete.click()
            logger.debug("NetworkPage: Clicks on ok")
            self.browser.accept_alert()
            self.buy_time()
    
    def delete_guest_nw2_if_present(self):
        '''
        Delete network i.e wpa2 or wpa2_wpa if present.
        '''
        if self.left_panel_add_button:
            logger.debug("NetworkPage: Clicking on  left panel close button ")
            self.left_panel_close_button
        if self.guest_nw2:
            logger.debug("NetworkPage: Clicks on existing  network")
            self.guest_nw2.click()
            logger.debug("NetworkPage: Clicks on existing  network delete Button")
            self.guest_nw2_delete.click()
            logger.debug("NetworkPage: Clicks on ok")
            self.browser.accept_alert()
            self.buy_time()