from athenataf.lib.util.MapReader import MapReader
import logging
logger = logging.getLogger('athenataf')

class WebPage:
	def __init__(self, page_name, test, browser, config):
		self._dict = MapReader(page_name).gui_map
		self.name = self.__class__.__name__
		self.browser = browser
		self.config = config
		self.test = test
	
	def field(self, elem_name, element_meta, format="delimited", disp_flag = False):
		if format == "delimited":
			value_parts = [part.strip() for part in element_meta.split("&")]
			element_meta = {
									"CONTROL_TYPE"	: value_parts[0],
									"BY_TYPE"		: value_parts[1],
									"BY_VALUE"		: value_parts[2]
								}
			if len(value_parts) > 3:
				element_meta["INDEX"] = int(value_parts[3])								

		if element_meta.has_key("INDEX"):
			if element_meta["BY_TYPE"] == "xpath":
				kwargs = {"selector" : element_meta["BY_VALUE"] , "index" : element_meta["INDEX"]}
				element = self.browser.wait_for(self.browser.get_elements_by_xpath, **kwargs)
			elif element_meta["BY_TYPE"] == "css":
				kwargs = {"selector" : element_meta["BY_VALUE"] , "index" : element_meta["INDEX"]}
				element = self.browser.wait_for(self.browser.get_elements_by_css, **kwargs)
			else:
				kwargs = {element_meta["BY_TYPE"] : element_meta["BY_VALUE"], "index" : element_meta["INDEX"]}
				element = self.browser.wait_for(self.browser.get_elements, **kwargs)			
		else:
			if element_meta["BY_TYPE"] == "xpath":
				kwargs = {element_meta["BY_VALUE"]}
				element = self.browser.wait_for(self.browser.get_element_by_xpath, *kwargs)
			elif element_meta["BY_TYPE"] == "css":
				kwargs = {element_meta["BY_VALUE"]}
				element = self.browser.wait_for(self.browser.get_element_by_css, *kwargs)
			else:
				kwargs = {element_meta["BY_TYPE"] : element_meta["BY_VALUE"]}
				element = self.browser.wait_for(self.browser.get_element, **kwargs)
		if disp_flag:
			print element
		else:	
			ret_element = self.browser.get_custom_element(self.name, element_meta["CONTROL_TYPE"], elem_name, element)
			return ret_element
	
	def __getattr__(self, elem_name):
		logger.debug("Now retrieving: %s::%s" % (self.__class__.__name__,elem_name))
		if self._dict.has_key(elem_name):
			element_meta = self._dict[elem_name]
			return self.field(elem_name,element_meta, "map")
		else:
			raise Exception("This page does not contain the mentioned element name")
	
	def display(self, elem_name):
		logger.debug("Retrieving object to display: %s::%s" % (self.__class__.__name__,elem_name))
		if self._dict.has_key(elem_name):
			element_meta = self._dict[elem_name]
			return self.field(elem_name,element_meta, "map", disp_flag=True)
		else:
			raise Exception("This page does not contain the mentioned element name")

	def isPageLoaded(self):
		pass
		# Override at a page as per the page requirements
		
	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.__class__.__name__		