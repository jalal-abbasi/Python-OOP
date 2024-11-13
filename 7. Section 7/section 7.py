class BouncyBall:
    def __init__(self, price, size, brand):
        self._price = price 
        self._size = size 
        self._brand = brand

    #def get_price(self):
    #    return self._price

    #def set_price(self, new_price):
    #    self._price = new_price

    #price = property(get_price, set_price)

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price):
        self._price = new_price

my_bouncy = BouncyBall(1000, 12, 'nike')
print (my_bouncy.price)

my_bouncy.price = 1200
print(my_bouncy.price)



        