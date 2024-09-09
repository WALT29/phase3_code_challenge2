class Coffee():
    def __init__(self,name):
        self.name=name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if hasattr(self,'_name'):
            raise ValueError("The name cannot be changed")
        if not isinstance(name,str):
            raise ValueError("The name must be of type string")
        if len(name)<3:
            raise ValueError("The name is short it should have more than 3 characters")
        self._name=name
    
    def orders(self):
        from order import Order
        return[order for order in Order.all if order.coffee ==self]
    
    def customers(self):
        return[order.name for order in self.orders()]
    
    def num_orders(self):
        orders=self.orders();
        if not orders:
            return 0;
        return len(orders)
    
    def average_price(self):
        orders=self.orders()
        if not orders:
            return 0;
        total_price=sum(order.price for order in orders)
        return total_price
    