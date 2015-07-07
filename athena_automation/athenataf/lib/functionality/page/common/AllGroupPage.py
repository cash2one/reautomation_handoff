from athenataf.lib.util.WebPage import WebPage
from athenataf.lib.functionality.page.configuration.network.NetworkPage import NetworkPage
from athenataf.lib.functionality.page.switch.SwitchesPage import SwitchesPage

class AllGroupPage(WebPage):
	def __init__(self, test, browser, config):
		WebPage.__init__(self, "AllGroup", test, browser, config)
		self.test.assertPageLoaded(self)
		
		
	def isPageLoaded(self):
		if self.group_babel:
			return True	
		else:
			return False 
			
	def go_to_networks(self):
		self.default_group.click()
		import time
		time.sleep(8)
		return NetworkPage(self.test, self.browser, self.config)
		
	def go_to_switches(self):
		import time
		time.sleep(8)		
		self.switch_group.click()
		time.sleep(4)				
		try:
			if self.switch_group:
				self.switch_group.click()
				time.sleep(8)				
		except:
			pass
		
		return SwitchesPage(self.test, self.browser, self.config)
		
	def go_to_samplegroup(self):
		self.sample_group.click()
		import time
		time.sleep(8)
		return SwitchesPage(self.test, self.browser, self.config)
		
	def assert_group1(self):
		if not self.group1_group:
			import traceback
			raise AssertionError("group1 does not exist i.e. Traceback: %s" %traceback.format_exc())
		
	def assert_group2(self):
		if not self.group2_group:
			import traceback
			raise AssertionError("group2 does not exist i.e. Traceback: %s" %traceback.format_exc())
	
	def assert_group_name_and_aps(self):
	  if not (self.group_name_label and self.ap_label and self.default_group and self.default_aps and self.samplegroup and self.samplegroup_aps) :
	   import traceback
	   raise AssertionError("Group names and APS does not exist i.e. Traceback: %s" %traceback.format_exc())		