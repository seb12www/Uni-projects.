from customer import Customer

class CustomerManager:
    def __init__(self):

        #create an empty list to save customers data

        self.customers = []
    

    def addCustomer(self, customer: Customer):

        #insert any customer to the list, email need to be unique and object must be valid

        if not isinstance(customer, Customer):
            raise TypeError("Only Customer instances can be added.")
        if self.getCustomerByEmail(customer.getEmail()):
            raise ValueError("Customer with this email already exists.")
        self.customers.append(customer)

    def removeCustomer(self, customer: Customer):

        #delete a customer from the list

        try:
            self.customers.remove(customer)
        except ValueError:
            raise ValueError("Customer not found in the list.")

    def getCustomerByEmail(self, email: str):

        #find any costumer by their email

        for customer in self.customers:
            if customer.getEmail() == email:
                return customer
        return None

    def getCustomersByName(self, name: str):

        #prompt the right list that matches the inserted name

        return [customer for customer in self.customers if customer.getName() == name]
