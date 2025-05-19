import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def test_customer_init(self):
        """Test Customer initialization"""
        customer = Customer("Alice")
        assert customer.name == "Alice"

    def test_name_validation(self):
        """Test name validation"""
        with pytest.raises(TypeError):
            Customer(123)  # Not a string
        with pytest.raises(ValueError):
            Customer("")  # Too short
        with pytest.raises(ValueError):
            Customer("ThisNameIsWayTooLong")  # Too long

    def test_create_order(self):
        """Test order creation"""
        customer = Customer("Bob")
        coffee = Coffee("Latte")
        order = customer.create_order(coffee, 5.0)
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 5.0

    def test_orders_property(self):
        """Test orders property"""
        customer = Customer("Charlie")
        coffee = Coffee("Espresso")
        order1 = Order(customer, coffee, 4.5)
        order2 = Order(customer, coffee, 5.0)
        assert len(customer.orders()) == 2
        assert order1 in customer.orders()
        assert order2 in customer.orders()

    def test_coffees_property(self):
        """Test coffees property"""
        customer = Customer("Dana")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Cappuccino")
        Order(customer, coffee1, 4.5)
        Order(customer, coffee2, 5.0)
        assert len(customer.coffees()) == 2
        assert coffee1 in customer.coffees()
        assert coffee2 in customer.coffees()