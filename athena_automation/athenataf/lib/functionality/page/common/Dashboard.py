from athenataf.lib.util.WebPage import WebPage
from athenataf.lib.functionality.page.common.LeftPanel import LeftPanel
from athenataf.lib.functionality.page.reports.ReportsNetworkPage import ReportsNetworkPage
from athenataf.lib.functionality.page.group.ManageGroupsPage import ManageGroupsPage
from athenataf.lib.functionality.page.maintenance.FirmWarePage import FirmWarePage
from athenataf.lib.functionality.page.configuration.security.SecurityPage import SecurityPage
from athenataf.lib.functionality.page.configuration.network.BasicInfoPage import BasicInfoPage
import logging
logger = logging.getLogger('athenataf')
import traceback
import time

class Dashboard(WebPage):
	def __init__(self, test, browser, config):
		WebPage.__init__(self, "DashboardContent", test, browser, config)
		self.test.assertPageLoaded(self)

	def isPageLoaded(self):
		if self.overview_sub_menu:
			return True	
		else:
			return False
				
	def close_welcome_message(self):
		if self.cancel:
			self.cancel.click()
		
	def assert_monitoring_overview_page_elements(self):
		if not self.access_point_element:
			raise AssertionError("'ACCESS POINTS' element is not found.Traceback: %s " %traceback.format_exc())
		elif not self.clients_element:
			raise AssertionError("'CLIENTS' element is not found.Traceback: %s " %traceback.format_exc())
		elif not self.alerts_element:
			raise AssertionError("'ALERTS' element is not found.Traceback: %s " %traceback.format_exc())
		elif not self.graph_element:
			raise AssertionError("'THROUGHPUT' element is not found.Traceback: %s " %traceback.format_exc())
		elif not self.map_element:
			raise AssertionError("'SWITCHES' element is not found.Traceback: %s " %traceback.format_exc())

	def assert_quicklinks_dropdown_elements(self):
		conf = self.config.config_vars
		time.sleep(3)
		options = self.quicklinks_dropdown.get_options()
		logger.debug('Dashboard : Checking for Quicklinks options')
		if not options[0] == conf.quicklinks_selected_value:
			raise AssertionError("'Quick Links' element not found i.e. Traceback: %s" %traceback.format_exc())
		
		if not options[1] == conf.quicklinks_value1:
			raise AssertionError("'Create New Network' element not found i.e. Traceback: %s" %traceback.format_exc())
		
		if not options[2] == conf.quicklinks_value2:
			raise AssertionError("'Create Report' element not found i.e. Traceback: %s" %traceback.format_exc())
		
		if not options[3] == conf.quicklinks_value3:
			raise AssertionError("'Manage Groups' element not found i.e. Traceback: %s" %traceback.format_exc())
		
		if not options[4] == conf.quicklinks_value4:
			raise AssertionError("'Update Device Firmware' element not found i.e. Traceback: %s" %traceback.format_exc())
		
		if not options[5] == conf.quicklinks_value5:
			raise AssertionError("'Set Security' element not found i.e. Traceback: %s" %traceback.format_exc())
		
		if not options[6] == conf.quicklinks_value6:
			raise AssertionError("'Manage Devices' element not found i.e. Traceback: %s" %traceback.format_exc())
		
	def assert_quicklinks_options(self):
		left_panel_object = LeftPanel(self.test, self.browser, self.config)
		basic_info_page = self.select_quicklinks_options(self.config.config_vars.quicklinks_value1)
		time.sleep(8)
		logger.debug('BasicInfoPage : Checking for BasicInfoPage page')
		if basic_info_page is None:
			raise AssertionError("Basic Info Page is not loaded successfully.")
		left_panel_object.go_to_monitoring_page()
		
		report_network_page = self.select_quicklinks_options(self.config.config_vars.quicklinks_value2)
		time.sleep(8)
		logger.debug('ReportsNetworkPage : Checking for ReportsNetworkPage page')
		if report_network_page is None:
			raise AssertionError("Report Network Page is not loaded successfully.")
		left_panel_object.go_to_monitoring_page()
		
		manage_groups_page = self.select_quicklinks_options(self.config.config_vars.quicklinks_value3)
		time.sleep(8)
		logger.debug('ManageGroupsPage : Checking for ManageGroupsPage page')
		if manage_groups_page is None:
			raise AssertionError("Manage groups Page is not loaded successfully.")
		manage_groups_page.manage_group_close.click()
		left_panel_object.go_to_monitoring_page()
		
		firmware_page = self.select_quicklinks_options(self.config.config_vars.quicklinks_value4)
		time.sleep(8)
		logger.debug('FirmWarePage : Checking for FirmWarePage page')
		if firmware_page is None:
			raise AssertionError("Frimware  Page is not loaded successfully.")
		left_panel_object.go_to_monitoring_page()
		
		security_page = self.select_quicklinks_options(self.config.config_vars.quicklinks_value5)
		time.sleep(8)
		logger.debug('SecurityPage : Checking for SecurityPage page')
		if security_page is None:
			raise AssertionError("Security Page is not loaded successfully.")
		left_panel_object.go_to_monitoring_page()
		
	def select_quicklinks_options(self, option_text = None):	
		if option_text == self.config.config_vars.quicklinks_value1:
			logger.debug("Dashboard : Setting 'Create New Network' for 'Quicklinks' dropdown")
			self.quicklinks_dropdown.set(option_text)
			return BasicInfoPage(self.test, self.browser, self.config)
		elif option_text == self.config.config_vars.quicklinks_value2:
			logger.debug("Dashboard : Setting 'Create Report' for 'Quicklinks' dropdown")
			self.quicklinks_dropdown.set(option_text)
			return ReportsNetworkPage(self.test, self.browser, self.config)
		elif option_text == self.config.config_vars.quicklinks_value3:
			logger.debug("Dashboard : Setting 'Manage Groups' for 'Quicklinks' dropdown")
			self.quicklinks_dropdown.set(option_text)
			return ManageGroupsPage(self.test, self.browser, self.config)
		elif option_text == self.config.config_vars.quicklinks_value4:
			logger.debug("Dashboard : Setting 'Update Device Firmware' for 'Quicklinks' dropdown")
			self.quicklinks_dropdown.set(option_text)
			return FirmWarePage(self.test, self.browser, self.config)
		elif option_text == self.config.config_vars.quicklinks_value5:
			logger.debug("Dashboard : Setting 'Set Security' for 'Quicklinks' dropdown")
			self.quicklinks_dropdown.set(option_text)
			return SecurityPage(self.test, self.browser, self.config)
			
	def assert_monitoring_page_switch(self):
		if not self.switch_0:
			import traceback
			raise AssertionError("switch is available in i.e. Traceback: %s" %traceback.format_exc())	

			
			
			
	def enable_help(self):
		'''
		clicks on help button
		'''
		self.buy_time()
		self.help_button.click()
		
	def assert_help_option_for_all_groups_label(self):
		'''
		asserting help content
		'''
		self.buy_time()
		self.buy_time()
		action_chain=self.browser.get_action_chain()
		self.buy_time()
		self.buy_time()
		action_chain.move_to_element(self.all_group_link_label).perform()
		self.buy_time()
		if not self.auto_help_content:
			raise AssertionError("All Groups Help content is not Shown  i.e. Traceback: %s" %traceback.format_exc())
		self.buy_time()
		
	def buy_time(self):
		time.sleep(6)