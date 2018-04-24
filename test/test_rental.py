from unittest import TestCase
from ..classes.rental import (
    RentalHour, RentalDay, RentalWeek
)


class RentalTestCase(TestCase):

    def test_rental_hour(self):
        _rental = RentalHour()
        self.assertTrue(_rental.get_rental(1) == 5)

    def test_rental_day(self):
        _rental = RentalDay()
        self.assertTrue(_rental.get_rental(1) == 20)

    def test_rental_week(self):
        _rental = RentalWeek()
        self.assertTrue(_rental.get_rental(1) == 60)
