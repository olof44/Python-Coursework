from stock import Stock

f1 = Stock(1, 0)
f2 = Stock(2, 0)
f3 = Stock(3, 0)
f1.add_item(50000)
f1.price()
f2.add_item(30000)
f2.price()
f3.add_item(45000)
f3.price()

class Customer:
    def __init__(self, name, money, animal):
        self.name = name
        self.money = money
        self.animal = animal


    def how_much_food_you_need(self, how_animals, how_days):
        self.how_animals = how_animals
        self.how_days = how_days
        self.how_food = 0
        if self.animal == "Pig":
            self.pig = 5
            self.how_food = (self.how_animals * self.pig) * self.how_days
            print("============== " + str(self.name) + " ==============")
            print("For " + str(self.how_animals)+ " Pigs, for " + str(self.how_days) + " days you need: " + str(self.how_food) + "kg. of food")
        elif self.animal == "Horse":
            self.horse = 9
            self.how_food = (self.how_animals * self.horse) * self.how_days
            print("============== " + str(self.name) + " ==============")
            print("For " + str(self.how_animals)+ " Horses, for " + str(self.how_days) + " days you need: " + str(self.how_food) + "kg. of food")
        elif self.animal == "Dog":
            self.dog = 1
            self.how_food = (self.how_animals * self.dog) * self.how_days
            print("============== " + str(self.name) + " ==============")
            print("For " + str(self.how_animals)+ " Dogs, for " + str(self.how_days) + " days you need: " + str(self.how_food) + "kg. of food")


    def buy(self):
        self.quan = self.how_food
        print("Your balance is: " + str(self.money) + "$")
        if self.animal == "Pig":
            print("================ Pig ===============")
            print("We have: " + str(f1.stock[f1.stockId]) + "kg. of pig food.")
            self.k = f1.v * self.quan
            if self.money >= self.k:
                if f1.stock[f1.stockId] >= self.quan:
                   f1.stock[f1.stockId] = f1.stock[f1.stockId] - self.quan
                   print("You bought: " + str(self.quan) + "kg." + "\nTotal amount to pay: " + str(self.k)+ "$")
                   print("You have: " + str(self.money - self.k) + "$ left")
                   print(str(f1.stock[f1.stockId]) + "kg. of pig food left in stock.")
                   print("====================================\n")
                else:
                   print("We don't have " + str(self.quan) + "kg. of that food!\n")
                   print("====================================\n")
            else:
                   print("You don't have enough money for " + str(self.quan) + "kg.!\n")
        elif self.animal == "Horse":
            print("=============== Horse ===============")
            print("We have: " + str(f2.stock[f2.stockId]) + "kg. of horse food.")
            self.k = f2.v * self.quan
            if self.money >= self.k:
                if f2.stock[f2.stockId] >= self.quan:
                   f2.stock[f2.stockId] = f2.stock[f2.stockId] - self.quan
                   print("You bought: " + str(self.quan) + "kg." + "\nTotal amount to pay: " + str(self.k)+ "$")
                   print("You have: " + str(self.money - self.k) + "$ left")
                   print(str(f2.stock[f2.stockId]) + "kg. of horse food left in stock.")
                   print("====================================\n")
                else:
                   print("We don't have " + str(self.quan) + "kg. of that food!")
                   print("====================================\n")
            else:
                   print("You don't have enough money for " + str(self.quan) + "kg.!\n")
        elif self.animal == "Dog":
            print("=============== Dog ================")
            print("We have: " + str(f3.stock[f3.stockId]) + "kg. of dog food.")
            self.k = f3.v * self.quan
            if self.money >= self.k:
                if f3.stock[f3.stockId] >= self.quan:
                   f3.stock[f3.stockId] = f3.stock[f3.stockId] - self.quan
                   print("You bought: " + str(self.quan) + "kg." + "\nTotal amount to pay: " + str(self.k)+ "$")
                   print("You have: " + str(self.money - self.k) + "$ left")
                   print(str(f3.stock[f3.stockId]) + "kg. of dog food left in stock.")
                   print("====================================\n")
                else:
                   print("We don't have " + str(self.quan) + "kg. of that food!")
                   print("====================================\n")
            else:
                   print("You don't have enough money for " + str(self.quan) + "kg.!\n")
        else:
            print("=================== " + str(self.animal) + " ===================\n")
            print("We don't have "+ str(self.animal) + " food right now!\n")
