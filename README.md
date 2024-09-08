# PHASE 3 WEEK 2 CODE CHALLENGE    6/9/2024

BY `WALTER DAVID IRUNGU`

# Coffee Ordering program

This project consists of a program for managing customers, coffees, and orders. It includes three main classes: `Customer`, `Coffee`, and `Order`. 

## Classes

### 1. `Customer`

The `Customer` class represents a customer who can create orders for different coffees.

- **Attributes:**
  - `name` (str): The name of the customer. It must be between 1 and 15 characters long and be of type `str`.

- **Methods:**
  - `__init__(self, name)`: Initializes a customer with a valid name.
  - `name`: Property to get or set the customer's name. Must be between 1 and 15 characters long.
  - `create_order(coffee, price)`: Creates and returns a new `Order` instance associated with the customer and a coffee. Price must be a float between 1.0 and 10.0.
  - `orders()`: Returns a list of all orders for the customer. Orders must be of type `Order`.
  - `coffees()`: Returns a unique list of all coffees the customer has ordered. Coffees must be of type `Coffee`.
  - `most_aficionado(coffee)`: Class method that returns the `Customer` who has spent the most on the provided coffee instance. Returns `None` if there are no customers for the coffee.

### 2. `Coffee`

The `Coffee` class represents a type of coffee that can be ordered by customers.

- **Attributes:**
  - `name` (str): The name of the coffee. It must be at least 3 characters long and be of type `str`.

- **Methods:**
  - `__init__(self, name)`: Initializes a coffee with a valid name.
  - `name`: Property to get the coffee's name. Once set, it cannot be changed.
  - `orders()`: Returns a list of all orders for the coffee. Orders must be of type `Order`.
  - `customers()`: Returns a unique list of all customers who have ordered the coffee. Customers must be of type `Customer`.
  - `num_orders()`: Returns the total number of times the coffee has been ordered. Returns 0 if the coffee has never been ordered.
  - `average_price()`: Returns the average price for the coffee based on its orders. Returns 0 if the coffee has never been ordered.

### 3. `Order`

The `Order` class represents an order placed by a customer for a specific coffee.

- **Attributes:**
  - `customer` (Customer): The customer who placed the order.
  - `coffee` (Coffee): The coffee ordered.
  - `price` (float): The price of the order, which must be between 1.0 and 10.0.

- **Methods:**
  - `__init__(self, customer, coffee, price)`: Initializes an order with a customer, coffee, and price.
  - `price`: Property to get or set the price of the order. Price cannot be changed once set and must be between 1.0 and 10.0.

## Usage

1. **Creating Instances:**
   ```python
   from customer import Customer
   from coffee import Coffee
   from order import Order

   # Create coffee instances
   black_coffee=Coffee("Black Coffee")
   white_coffee=Coffee("White Coffee")
   iced_coffee=Coffee("iced Coffee")


   # Create customer instances
   morara=Customer("kebaso")
   platnumz=Customer("Platnumz")
   joel=Customer("Joel")
   moraa=Customer("Moraa")

   # Create orders
   order1 = morara.create_order(black_coffee, 5.0)
   order2 = joel.create_order(white_coffee, 6.0)

   # Accessing data
   print(morara.orders())  # List of orders by morara kebaso
   print(black_coffee.orders())  # List of orders for black_coffee
   print(black_coffee.num_orders())  # Number of orders for black_coffee
   print(black_coffee.average_price())  # Average price of black_coffee orders

   # Find the customer who has spent the most on a coffee
   print(Customer.most_aficionado(black_coffee))  # Customer who spent the most on black_coffee
