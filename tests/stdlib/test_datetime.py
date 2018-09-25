

from .. utils import TranspileTestCase

class DateModuleTests(TranspileTestCase):
	def test_today(self):
		self.assertCodeExecution("""
		from datetime import date
		print (date.today())
		""")

	def test_creation(self):
		self.assertCodeExecution("""
		from datetime import date
		try:
			print (date(10000, 6, 3))
		except ValueError as err:
			print(err)
		""")

	def test_creation_invalid_year(self):
		self.assertCodeExecution("""
		from datetime import date
		try:
			print (date(0, 6, 3))
		except ValueError as err:
			print(err)
		""")

	def test_creation_invalid_month(self):
		self.assertCodeExecution("""
		from datetime import date
		try:
			print (date(1, 0, 3))
		except ValueError as err:
			print(err)
		""")
	
	def test_creation_invalid_day(self):
		self.assertCodeExecution("""
		from datetime import date
		try:
			print (date(1, 5, 0))
		except ValueError as err:
			print(err)
		""")

	def test_creation_null_input(self):
		self.assertCodeExecution("""
		from datetime import date
		try:
			print (date(1, None, 3))
		except TypeError as err:
			print(err)
		""")

	def test_kwargs(self):
		self.assertCodeExecution("""
		from datetime import date
		print (date(year=4, day=3, month=10))
		""")

	def test_year_attr(self):
		self.assertCodeExecution("""
		from datetime import date
		d = date(1337, 1, 1)
		print(d.year)
		""")

	def test_month_attr(self):
		self.assertCodeExecution("""
		from datetime import date
		d = date(1338, 12, 1)
		print(d.month)
		""")

	def test_day_attr(self):
		self.assertCodeExecution("""
		from datetime import date
		d = date(1339, 1, 4)
		print(d.day)
		""")
	
	def test_min_attr(self):
		self.assertCodeExecution("""
		from datetime import date
		d = date(1300, 1, 4)
		print(d.min)
		""")

	def test_max_attr(self):
		self.assertCodeExecution("""
		from datetime import date
		d = date(1300, 1, 4)
		print(d.max)
		""")

	def test_ctime(self):
		self.assertCodeExecution("""
		from datetime import date
		d = date(2018, 9, 21)
		print(d.ctime())
		""")

	def test_ctime_2(self):
		self.assertCodeExecution("""
		from datetime import date
		d = date(9191, 1, 31)
		print(d.ctime())
		""")

	def test_ctime_3(self):
		self.assertCodeExecution("""
		from datetime import date
		d = date(9491, 12, 31)
		print(d.ctime())
		""")

	def test_repr(self):
		self.assertCodeExecution("""
		from datetime import date
		d = date(9491, 12, 31)
		print(d.__repr__())
		""")

	def test_str(self):
		self.assertCodeExecution("""
		from datetime import date
		d = date(9491, 12, 31)
		print(d.__str__())
		""")