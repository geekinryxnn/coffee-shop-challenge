from customer import Customer
from coffee import Coffee
from order import Order


customer1 = Customer("Ryan")
customer2 = Customer("Gabriel")
customer3 = Customer("Alice")
customer4 = Customer("Bob")
customer5 = Customer("Victoria")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")
coffee3 = Coffee("Cappuccino")
coffee4 = Coffee("Americano")
coffee5 = Coffee("Mocha")

order1 = Order(customer1, coffee1, 5.0)
order2 = Order(customer1, coffee2, 4.5)
order3 = Order(customer2, coffee1, 6.0)
order4 = Order(customer3, coffee3, 7.0)
order5 = Order(customer4, coffee4, 3.5)

print(f"{customer1.name} has ordered:")
for order in customer1.orders():
    print(f"  - {order.coffee.name} (${order.price})")

print(f"\n{customer1.name}'s favorite drinks:")
for coffee in customer1.coffees():
    print(f"  - {coffee.name}")

print(f"\nPeople who love {coffee1.name}:")
for customer in coffee1.customers():
    print(f"  - {customer.name}")

print(f"\n{coffee1.name} statistics:")
print(f"  Total orders: {coffee1.num_orders()}")
print(f"  Average price: ${coffee1.average_price():.2f}")

print(f"☕ {customer1.name} has ordered:")
for order in customer1.orders():
    print(f"  - {order.coffee.name} (${order.price})")


