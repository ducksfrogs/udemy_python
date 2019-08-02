class Kettle(object):
    def __init__(self, make, price):
        self.make =make
        self.price = price
        self.on = False

kenwood = Kettle("kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton =Kettle("hamillton", 15.44)

print("models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))