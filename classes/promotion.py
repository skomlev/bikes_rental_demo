class Promotion():
    def apply(self, price):
        return price - (price * self.discount)

    def get_discount(self):
        return self.discount


class NoPromotion(Promotion):
    discount = 0


class FamilyPromotion(Promotion):
    discount = 0.3


class PromotionFactory():

    def __init__(self, quantity, rental=None):
        self.quantity = quantity
        self.rental = rental

    def get_promotion(self):
        if self.quantity in range(3, 6):
            return FamilyPromotion()

        return NoPromotion()
