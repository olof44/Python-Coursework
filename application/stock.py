class Stock:
    def __init__(self, stockId, quantity):
        self.stockId = stockId
        self.q = quantity
        self.stock = {self.stockId : self.q}


    def add_item(self, how_much):
        self.s = self.stock[self.stockId] = self.q + how_much
        print(str(how_much) + "kg. added to the stock")


    def price(self):
        self.prices = {
            1 : 3,
            2 : 5,
            3 : 9,
            4 : 2,
            5 : 1
        }
        self.v = self.prices[self.stockId]

