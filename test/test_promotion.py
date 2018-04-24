from unittest import TestCase
from ..classes.promotion import (
    PromotionFactory, FamilyPromotion, NoPromotion
)


class PromotionTestCase(TestCase):

    def test_promotion_factory_family_promotion(self):
        quantity = 5
        _promotion = PromotionFactory(quantity)
        self.assertTrue(isinstance(
            _promotion.get_promotion(),
            FamilyPromotion
        ))

    def test_promotion_factory_no_promotion(self):
        quantity = 1
        _promotion = PromotionFactory(quantity)
        self.assertTrue(isinstance(_promotion.get_promotion(), NoPromotion))

    def test_promotion_family_promotion(self):
        _promotion = FamilyPromotion()
        self.assertTrue(_promotion.get_discount() == 0.3)

    def test_promotion_no_promotion(self):
        _promotion = NoPromotion()
        self.assertTrue(_promotion.get_discount() == 0)
