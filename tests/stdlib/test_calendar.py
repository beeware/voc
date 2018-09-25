from .. utils import TranspileTestCase

from unittest import expectedFailure

class CalendarModuleTests(TranspileTestCase):

	
	def test_leapdays(self):
	        self.assertCodeExecution("""
	        	import calendar
	        	print(calendar.leapdays(2015,2018))
	        	""")
	def test_leapdays_double(self):
	        self.assertCodeExecution("""
	        	import calendar
	        	print(calendar.leapdays(2015.4,2018))
	        	""")
	def test_leapdays_descending(self):
	        self.assertCodeExecution("""
	        	import calendar
	        	print(calendar.leapdays(2018,2015))
	        	""")
	def test_leapdays_booltrue(self):
	        self.assertCodeExecution("""
	        	import calendar
	        	print(calendar.leapdays(2015,True))
	        	""")
	def test_leapdays_boolfalse(self):
	        self.assertCodeExecution("""
	        	import calendar
	        	print(calendar.leapdays(2015,False))
	        	""")
	@expectedFailure
	def test_leapdays_str1(self):
	        self.assertCodeExecution("""
	        	import calendar
	        	print(calendar.leapdays(2015,'abc'))
	        	""")
	@expectedFailure
	def test_leapdays_str2(self):
	        self.assertCodeExecution("""
	        	import calendar
	        	print(calendar.leapdays('abc',2015))
	        	""")
	@expectedFailure
	def test_leapdays_str3(self):
	        self.assertCodeExecution("""
	        	import calendar
	        	print(calendar.leapdays('cba','abc'))
	        	""")