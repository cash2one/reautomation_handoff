import os
from athenataf.config import fwork
import logging
logger = logging.getLogger('athenataf')

class MapReader:
	'''
	Read map files and creates a GUI map dictionary.
	'''
	def __init__(self, map_name):
		self.gui_map = {}
		f = open(os.path.join(fwork.MAPS_DIR, "%s.map" % map_name), "r")
		for line in f.xreadlines():
			line = line.strip()
			if not (line.strip() == ""):
				key, value = [part.strip() for part in line.split(":", 1)]
				value_parts = [part.strip() for part in value.split("&")]
				try:
					if self.gui_map.has_key(key):
						raise Exception("Duplicate entry for '%s' found in '%s.map' file." % (key, map_name))
					for keys in self.gui_map.keys():
						if (value_parts[2] == self.gui_map[keys]["BY_VALUE"]) and ((len(value_parts) == 3 and not self.gui_map[keys].has_key("INDEX")) or (len(value_parts) > 3 and self.gui_map[keys].has_key("INDEX") and value_parts[3] == self.gui_map[keys]["INDEX"])):
							raise Exception("The element '%s' in '%s.map' file has a similar element '%s'" % (key, map_name, keys))
				except Exception, e:
					logger.debug("MapReader: caught exception:: %s" % str(e))
					raise
				else:
					self.gui_map[key] = {
											"CONTROL_TYPE"	: value_parts[0],
											"BY_TYPE"		: value_parts[1],
											"BY_VALUE"		: value_parts[2]
										}
					if len(value_parts) > 3:
						self.gui_map[key]["INDEX"] = int(value_parts[3])
		f.close()