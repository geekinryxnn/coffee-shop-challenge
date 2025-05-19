import pytest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee:
    def test_coffee_init(self):
        """Test Coffee initialization"""
        coffee = Coffee("Latte")
        assert coffee.name == "Latte"

    def test_name_validation(self):
        """Test name validation"""
        with pytest.raises(TypeError):
            Coffee(123)  
        with pytest.raises(ValueError):
            Coffee("A")  # Too short
        coffee = Coffee("Valid")
        with pytest.raises(AttributeError):
            coffee.name = "New Name"  # Immutable

    def test_orders_property(self):
        """Test orders property"""
        coffee = Coffee("Espresso")
        customer = Customer("Eve")
        order1 = Order(customer, coffee, 4.0)
        order2 = Order(customer, coffee, 4.5)
        assert len(coffee.orders()) == 2
        assert order1 in coffee.orders()
        assert order2 in coffee.orders()

    def test_customers_property(self):
        """Test customers property"""
        coffee = Coffee("Mocha")
        customer1 = Customer("Frank")
        customer2 = Customer("Grace")
        Order(customer1, coffee, 5.0)
        Order(customer2, coffee, 5.5)
        assert len(coffee.customers()) == 2
        assert customer1 in coffee.customers()
        assert customer2 in coffee.customers()

    def test_num_orders(self):
        """Test num_orders method"""
        coffee = Coffee("Americano")
        assert coffee.num_orders() == 0
        customer = Customer("Hank")
        Order(customer, coffee, 3.5)
        assert coffee.num_orders() == 1

    def test_average_price(self):
        """Test average_price method"""
        coffee = Coffee("Macchiato")
        customer = Customer("Ivy")
        Order(customer, coffee, 4.0)
        Order(customer, coffee, 6.0)
        assert coffee.average_price() == 5.0
        assert Coffee("New").average_price() == 0  # No orders
