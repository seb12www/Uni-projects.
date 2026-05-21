# Joan Sebastian Novoa Chala
# Final Assessment
# TEC206
# Student ID: 1831626


import unittest
from customer import Customer
from customer_manager import CustomerManager

class TestCustomerSystem(unittest.TestCase):

    def setUp(self):

        #set up initial test data 

        self.customer1 = Customer("Alice", "alice@example.com", "1234567890")
        self.customer2 = Customer("Bob", "bob@example.com", "0987654321")
        self.manager = CustomerManager()

    def test_add_and_get_customer(self):

        #test adding a customer and as a result it retrieves their email

        self.manager.addCustomer(self.customer1)
        result = self.manager.getCustomerByEmail("alice@example.com")
        self.assertEqual(result, self.customer1)

    def test_add_duplicate_email(self):

        #test in order to avoid addition of a customer with a duplicate email

        self.manager.addCustomer(self.customer1)
        with self.assertRaises(ValueError):
            self.manager.addCustomer(Customer("Alice Clone", "alice@example.com", "0000000000"))

    def test_remove_customer(self):

        #test deleting a customer from the manager

        self.manager.addCustomer(self.customer1)
        self.manager.removeCustomer(self.customer1)
        self.assertIsNone(self.manager.getCustomerByEmail("alice@example.com"))

    def test_get_customers_by_name(self):

        #test multiple customers with the same name

        self.manager.addCustomer(self.customer1)
        self.manager.addCustomer(Customer("Alice", "alice2@example.com", "1112223333"))
        results = self.manager.getCustomersByName("Alice")
        self.assertEqual(len(results), 2)

    def test_invalid_add(self):

        #test error raised when adding an invalid  object (when there is no costumers)

        with self.assertRaises(TypeError):
            self.manager.addCustomer("NotACustomer")

if __name__ == '__main__':

    #run final tests

    unittest.main()



