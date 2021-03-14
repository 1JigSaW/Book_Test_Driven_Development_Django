from django.test import TestCase

class SmokeTest(TestCase):
	''' toxic test '''

	def test_bad_maths(self):
		''' bad maths calculations'''
		self.assertEqual(1 + 1, 3)
		