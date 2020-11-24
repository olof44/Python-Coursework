from stock import Stock
price = Stock(1, 0)
price.price()
price2 = Stock(2, 0)
price2.price()
price3 = Stock(3, 0)
price3.price()
class Catalog:
    def __init__(self):
        print("============= Catalog =============")
        print("Pig: " + str(price.v) + "$/kg")
        print("Horse: " + str(price2.v) + "$/kg")
        print("Dog: " + str(price3.v) + "$/kg")
        print("===================================\n")



