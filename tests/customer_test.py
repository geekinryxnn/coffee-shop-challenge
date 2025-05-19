import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def test_customer_init(self):
        
        customer = Customer("Alice")
        assert customer.name == "Alice"

    def test_name_validation(self):
        
        with pytest.raises(TypeError):
            Customer(123)  
        with pytest.raises(ValueError):
            Customer("")  
        with pytest.raises(ValueError):
            Customer("ThisNameIsWayTooLong") 

    def test_create_order(self):
    
        customer = Customer("Bob")
        coffee = Coffee("Latte")
        order = customer.create_order(coffee, 5.0)
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 5.0

    def test_orders_property(self):
        
        customer = Customer("Charlie")
        coffee = Coffee("Espresso")
        order1 = Order(customer, coffee, 4.5)
        order2 = Order(customer, coffee, 5.0)
        assert len(customer.orders()) == 2
        assert order1 in customer.orders()
        assert order2 in customer.orders()

    def test_coffees_property(self):
    
        customer = Customer("Dana")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Cappuccino")
        Order(customer, coffee1, 4.5)
        Order(customer, coffee2, 5.0)
        assert len(customer.coffees()) == 2
        assert coffee1 in customer.coffees()
        assert coffee2 in customer.coffees()