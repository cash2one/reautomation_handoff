
class TestCase(object):
	def __init__(self, config):
		super(TestCase,self).__init__()
		self.config = config
		self.record = {}
		
	def setUpTestClass(self):
		pass
		
	def tearDownTestClass(self):
		pass
		
	def setUp(self):
		pass
		
	def run(self):
		pass
			
	def tearDown(self):
		pass
		
	def _get_msg(self, msg):
		'''
			_Private method called by Assertion related methods to pass 
			any message if needed with the Assertion taking place
		'''
		if msg is None: 
			msg = ""
		else:
			msg = msg + ".\n"
		return msg			
		
	def assertEquals(self, left, right, msg=None):
		'''
			assertEquals() method asserts the Equality of the left and right values,
			if found not equal raises ASSERTION_ERROR else Passes
		'''
		msg = self._get_msg(msg)
		if left != right:
			raise AssertionError("Assert Equals Failure:\n%s%s != %s" % (msg, left, right))
			
	def assertIsNone(self, input, msg=None):
		'''
			assertIsNone() method asserts the input value to be as None,
			if found not None raises ASSERTION_ERROR else Passes
		'''
		msg = self._get_msg(msg)
		if input is not None:
			raise AssertionError("Assert None Failure:\n%s%s is not None." % (msg, input))	
			
	def fail(self, msg=None):
		'''
			fail() method raises Assertion failure Error when called for
		'''
		msg = self._get_msg(msg)
		raise AssertionError("Assert  Failure:\n%s " % msg)
				
