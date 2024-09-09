from customer import Customer
from coffee import Coffee
from order import Order

############################################################CUSTOMERS###############################################################################################
morara=Customer("kebaso")
platnumz=Customer("Platnumz")
joel=Customer("Joel")
moraa=Customer("Moraa")

#############################################################COFFEE###############################################################################################
black_coffee=Coffee("Black Coffee")
white_coffee=Coffee("White Coffee")
iced_coffee=Coffee("iced Coffee")

##############################################################ORDERS#############################################################################################
order1 = morara.create_order(black_coffee, 5.0)
order2 = joel.create_order(white_coffee, 6.0)
#order3=platnumz.create_order(iced_coffee,23) ##this throws an error since the price should between 1.0 to 10.0
order3=moraa.create_order(iced_coffee,5.0)
order5 = joel.create_order(iced_coffee, 6.0)
##############################################################PRINTING DATA#######################################################################################
print(joel.orders())
print(joel.coffees())
print(next({"coffee":order.coffee.name ,"price":order.price} for order in joel.orders()))
print(black_coffee.orders())
