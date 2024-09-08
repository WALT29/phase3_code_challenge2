from order import Order
from coffee import Coffee
class Customer():
    all=[]
    def __init__(self,name):
        self.name=name
        Customer.all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if isinstance(name,str) and 1<=len(name)<=15:
            self._name=name
        else:
            raise ValueError("Enter a valid customer name")
    
    def orders(self):
        return [order for order in Order.all if order.customer==self]
    
    def coffees(self):
        return[order.coffee for order in self.orders()]
    
    def create_order(coffee, price):
        if not isinstance(coffee,Coffee):
            raise ValueError(f"{coffee} must be an instance of class Coffee")
        
        if not isinstance(price,float) or not 1.0<=price<=10.0:
            raise ValueError("The price must be a float and must be greater or equal to 1 and less than 10")
        order=Order(coffee,price)
        return order
    @classmethod
    def most_aficionado(cls,coffee):
        if not isinstance(coffee,Coffee):
            raise ValueError(f"The coffee must be an instance of class Coffee")
        
        highest_spent=0
        highest_spent_customer=None
        
        for customer in cls.all:
            total_spent=sum(order.price for order in customer.orders())
            if total_spent>highest_spent:
                highest_spent=total_spent
                highest_spent_customer=customer
        return highest_spent_customer
                
        
        
        