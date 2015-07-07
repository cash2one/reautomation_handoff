from athenataf.lib.util.WebPage import WebPage
import time
import traceback
import logging
logger = logging.getLogger('athenataf')

class NetworkAssignmentPage(WebPage):
	def __init__(self, test, browser, config):
		WebPage.__init__(self, "NetworkAssignment", test, browser, config)
		self.test.assertPageLoaded(self)

	def isPageLoaded(self):
		if self.finish:
			return True    
		else:
			return False

	def assert_network_assigned(self):
		if not self.wired_profile.selected=='default_wired_port_profile':
			raise AssertionError("   port 0 not set to 'default_wired_port_profile' .Traceback: %s " %traceback.format_exc())
		if not self.assignment_profile1.selected=='wired-instant':
			raise AssertionError("   port 1 not set to 'wired-instant' .Traceback: %s " %traceback.format_exc())
		if not self.assignment_profile2.selected=='wired-instant':
			raise AssertionError("   port 2 not set to 'wired-instant' .Traceback: %s " %traceback.format_exc())
		if not self.assignment_profile3.selected=='wired-instant':
			raise AssertionError("   port 3 not set to 'wired-instant' .Traceback: %s " %traceback.format_exc())
		if not self.assignment_profile4.selected=='wired-instant':
			raise AssertionError("   port 4 not set to 'wired-instant' .Traceback: %s " %traceback.format_exc())

	def finish_network_setup(self):
		'''
		Clicks on Finish button
		'''
		logger.debug(' NetworkAssignmentPage page :clicking on Finish button')
		time.sleep(10)
		self.finish.click()
		time.sleep(10)

	def set_network_port(self):
		'''
		sets wired profile value
		'''
		if self.wired_profile.get_selected() == self.config.config_vars.default_assign_port :
			logger.debug(' NetworkAssignmentPage page :setting wired profile to testwired')
			self.wired_profile.set(self.config.config_vars.wired_network_name)
			time.sleep(4)

	def click_back(self):
		'''
		Clicks on Back button
		'''
		logger.debug(' NetworkAssignmentPage page :clicking on Back button')
		self.back.click()

	def set_new_network_port(self,name):
		'''
		sets wired profile value
		'''
		if self.wired_profile.get_selected() == self.config.config_vars.default_assign_port :
			logger.debug(' NetworkAssignmentPage page :setting wired profile value')
			self.wired_profile.set(name)
			time.sleep(4)
