import os
from athenataf.config import fwork
import logging
logger = logging.getLogger('athenataf') 

class ConfigReader:
	def __init__(self, config_name):
		self.gui_map = {}
		self._dict = {}
		self.path = None
		if config_name == 'global_vars':
			self.path = fwork.CONFIG_DIR
		elif config_name == 'config_vars':
			self.path = fwork.CONFIG_VARS_DIR
		for root, dirs, files in os.walk(self.path):
			for file in files:
				if file.endswith(".props"):
					f = open(os.path.join(root, file), "r")
					for line in f.xreadlines():
						line = line.strip()
						if not (line.strip() == ""):
							key, value = [part.strip() for part in line.split(":", 1)]
							try:
								if self._dict.has_key(key):
									raise Exception("The value '%s' in file '%s', also exist in some other config file." % (key, file))
							except Exception, e:
								logger.debug("ConfigReader: caught exception:: %s" % str(e))
								raise
							else:
								self._dict[key] = value
					f.close()
		self.current_test = None
		
	def set_current_test(self, test):
		logger.debug("Set Current Test Case.")
		self.current_test = test
		
	def __getattr__(self, name):
		logger.debug("Now accessing config variable: %s" % name)
		if self.current_test.record is not None and name in self.current_test.record.keys():
			logger.debug("Picking value from test case record for %s:: %s" % (name,self.current_test.record[name]))
			return self.current_test.record[name]
		else:
			logger.debug("Picking value from configuration record %s:: %s" % (name, self._dict[name]))
			return self._dict[name]
	