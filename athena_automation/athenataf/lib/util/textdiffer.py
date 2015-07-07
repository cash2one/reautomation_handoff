
class TextDiffer:
	'''
	Class for finding the difference between two files or strings
	'''
	def __init__(self):
		self.left_lines = []
		self.right_lines = []
		
	def get_difference(self , left_file_or_str , right_file_or_str, num_of_context_lines = None):
		import difflib
		file1_object = None
		file2_object = None
		try:
			file1_object = open(left_file_or_str , 'r')
			file2_object = open(right_file_or_str , 'r')			
			self.left_lines = [line.strip() for line in file1_object.xreadlines()]
			self.right_lines = [line.strip() for line in file2_object.xreadlines()]
			file1_object.close()			
			file2_object.close()
			file1_object = None
			file2_object = None			
		except (IOError, TypeError):	
			# Treat both as strings
			left_str = left_file_or_str
			right_str = right_file_or_str			
			self.left_lines = left_str.strip().splitlines()
			self.right_lines = right_str.strip().splitlines()
		finally:
			if file1_object is not None: file1_object.close()
			if file2_object is not None: file2_object.close()
		
		if num_of_context_lines == None:
			num_of_context_lines = 3
		diff = difflib.context_diff(self.left_lines, self.right_lines, n = 0)
		diff_list = list(diff)
		difference = []
		for line in diff_list:
			if not(line.startswith("*") or line.startswith("-") or line == ("+ ")):
				if not(line.startswith("! controller config")):
					difference.append(line.strip())
				else:
					difference.append("")
		final_diff_str = "\n".join(difference)
		self.left_lines = []
		self.right_lines = []
		return final_diff_str
			