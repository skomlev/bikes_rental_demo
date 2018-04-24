from unittest import TestCase
from ..classes.rental import RentalHour
from ..classes.rent import Rent


class RentTestCase(TestCase):

    def test_rent_by_hour_no_promotion(self):
        _rental = RentalHour()
        _rent = Rent(1, _rental)
        self.assertTrue(_rent.get_rental() == 5)

    def test_rent_by_hour_family_promotion(self):
        _rental = RentalHour()
        _rent = Rent(4, _rental)
        self.assertTrue(_rent.get_rental() == 14)
