# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

class Pirate():
    rum = 0

    def drink_rum(self):
        self.rum += 1

    def hows_goin_mate(self):
        if self.rum > 4:
            return "Arrrr!"
        else:
            return "Nothin"

bill = Pirate()
print(bill.rum)
bill.drink_rum()
bill.drink_rum()
bill.drink_rum()
print(bill.hows_goin_mate())
bill.drink_rum()
bill.drink_rum()
print(bill.rum)
print(bill.hows_goin_mate())
