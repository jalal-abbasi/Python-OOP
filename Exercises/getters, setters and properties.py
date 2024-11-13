# exercise with Property()

class BouncyBall:

    SIZE_LIST = ["S", "M",  "L"]

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
    property(get_price,set_price)


    def get_size(self):
        return self._size

    def set_size(self, newsize):
        if newsize in SIZE_LIST:
            self._size = newprice
        else:
            print("please enter a correct value")
    property(get_size,set_size)


    def get_brand(self):
        return self._brand

    def set_brand(self, newbrand):
        self._size = newbrand
    property(get_brand,set_brand)


#example:
my_Bouncyball = BouncyBall(4, "medium", "Nike")

my_Bouncyball.price = 4.5
print(my_Bouncyball.price)


# execise with @property

class BouncyBall:

    SIZE_LIST = ["S", "M",  "L"]

    def __init__(self, price, size, brand):
        self._price = price 
        self._size = size 
        self._brand = brand

    

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, newprice):
        if isinstance(newprice, float) or isinstance(newprice, int) and newprice > 0:
            self._price = newprice
        else:
            print("please enter a correct value")

    @property
    def size(self):
        return self._size

    @size.setter
    def set_size(self, newsize):
        if newsize in SIZE_LIST:
            self._size = newprice
        else:
            print("please enter a correct value")
    

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, newbrand):
        self._size = newbrand
    


#example:
my_Bouncyball = BouncyBall(7, "large", "Addidas")

my_Bouncyball.price = 10.5
print(my_Bouncyball.price)


