from customer import Customer
from coffee import Coffee



class Order():
    all=[]
    def __init__(self,customer, coffee, price):
        self.customer=customer
        self.coffee=coffee
        self.price=price
        Order.all.append(self)
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,price):
        if hasattr(self,'_price'):
            raise ValueError("The price of the order cannot be changed")
        if not isinstance(price,float):
            raise ValueError("Price must be of type float.")
        if not 1.0<=price<=10.0:
            raise ValueError("Price must be between 1.0 and 10.0.")
        self._price=price
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self,customer):
        if not isinstance(customer,Customer):
            raise ValueError(f"{customer} must be an instance of class Customer")
        self._customer=customer
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self,coffee):
        if not isinstance(coffee,Coffee):
            raise ValueError(f"{coffee} must be an instance of class Coffee")
        self._coffee=coffee        