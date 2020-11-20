from stock import Stock
from catalog import Catalog
from customer import Customer
#Функциите на Class "Stock" се демонстрират в началото на Class "Customer"
#За да може класа да използва параметрите на Class "Stock"

cat = Catalog()
cat.Catalog()

c = Customer("Hristo", 30000, "Pig")
c.how_much_food_you_need(15, 30)
c.buy()
c = Customer("Petyr", 3000, "Dog")
c.how_much_food_you_need(3, 30)
c.buy()
c = Customer("Joro", 64510, "Horse")
c.how_much_food_you_need(5, 30)
c.buy()




