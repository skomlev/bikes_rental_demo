from .promotion import PromotionFactory


class Rent():
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price
        _promotion_factory = PromotionFactory(quantity)
        self.promotion = _promotion_factory.get_promotion()

    def get_rental(self):
        return self.promotion.apply(self.price.get_rental(self.quantity))
