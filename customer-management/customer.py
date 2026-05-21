class Customer:
    def __init__(self, name: str, email: str, phone_number: str):

        #start with customer name, email, and phone number

        self.name = name
        self.email = email
        self.phone_number = phone_number

    def getName(self):

        #return their name

        return self.name

    def getEmail(self):

        #return their email address

        return self.email

    def getPhoneNumber(self):

        #return their phone number

        return self.phone_number

    def setName(self, newName):

        #set a new name for the customer

        self.name = newName

    def setEmail(self, newEmail):

        #set a new email for the customer

        self.email = newEmail

    def setPhoneNumber(self, newPhoneNumber):

        #set a new phone number for the customer

        self.phone_number = newPhoneNumber

    def __repr__(self):

        #return a string representation of the customer

        return f"Customer(Name: {self.name}, Email: {self.email}, Phone: {self.phone_number})"
