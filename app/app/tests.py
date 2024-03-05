"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_sum(self):
        res = calc.add(3, 4)
        self.assertEqual(res, 7)

    def test_minus(self):
        res = calc.minus(16, 7)
        self.assertEqual(res, 9)
