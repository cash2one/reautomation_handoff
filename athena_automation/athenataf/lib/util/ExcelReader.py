import xlrd

import logging
logger = logging.getLogger('athenataf')

class ExcelReader:
	'''
		Excel reading base class for Data Driven Support
	'''
	def __init__(self, file_path):
		'''
			Base Excel reader class Initiator
		'''
		logger.info("Initializing ExcelReader")
		self.wb = xlrd.open_workbook(file_path)
		self.sh = self.wb.sheet_by_index(0)
		self.headers = self.sh.row_values(0)
		# print "ExcelReader:__init__: Headers: %s" % str(self.headers)
		self.current_index = 1
		self._row_values = []
		
	def get_next_record(self):
		'''
			Gets the next record 
		'''
		logger.debug("Getting next Record")
		try:
			#print self.current_index
			self._row_values = [u"%s" % i for i in self.sh.row_values(self.current_index)]
			#print "ExcelReader:__init__: Row: %s" % str(self._row_values)		
			self.current_index += 1
			return dict(zip(self.headers,self._row_values))			
		except IndexError,e:
			logger.debug("Records finished.")
			return None
		
	def close(self):
		# no need to close
		pass
		
	def get_full_file_as_dict(self):
		'''
			Returns the Content as Dict{}  
		'''
		logger.debug("Returning Content As Dictionary")
		contents = {}
		while True:
			line_dict = self.get_next_line()
			if line_dict is None:
				break
			contents[line_dict["QUERY_NAME"]] = line_dict["QUERY"]	
		return contents