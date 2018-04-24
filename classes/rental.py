class Rental():
    def get_rental(self, quantity):
        return self.rental * quantity


class RentalHour(Rental):
    rental = 5


class RentalDay(Rental):
    rental = 20


class RentalWeek(Rental):
    rental = 60
