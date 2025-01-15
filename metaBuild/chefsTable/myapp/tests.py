from django.test import TestCase
from datetime import datetime
from .models import Shifts

# Create your tests here.
# @classmethod
class ShiftsModelTest(TestCase):
    def setUpTestData(cls):
        cls.shifts = Shifts.objects.create(
            time_allocated = 'simba',
            time_in = '12:23',
            time_out = '14:23'
        )

    def testfield(self):
        self.assertIsInstance(self.Shifts.time_allocated, str)
        self.assertIsInstance(self.Shifts.time_in, datetime)
        self.assertIsInstance(self.Shifts.time_out, datetime)