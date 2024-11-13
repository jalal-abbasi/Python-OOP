class BouncyBall:

    def __init__(self, price, size, brand):
        self._price = price 
        self._size = size 
        self._brand = brand

    def get_price(self):
        return self._price

    def set_price(self, newprice):
        if isinstance(newprice, float) or isinstance(newprice, int) and newprice > 0:
            self._price = newprice
        else:
            print("please enter a correct value")


my_Bouncyball = BouncyBall(400, "medium", "Nike")

#print(my_Bouncyball.get_price())
my_Bouncyball.set_price(450)
print(my_Bouncyball.get_price())




