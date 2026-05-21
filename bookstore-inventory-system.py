# TEC206
# Intermediate Programming
# Bookstore Inventory Management System
# Joan Sebastian Novoa Chala
# Student ID: 1831626





#Define the parent Book class


class Book:
    """Parent class represents a generic book."""

    def __init__(self, title, author, price, quantity, book_type):
       
        #book attributes
        
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity
        self.book_type = book_type

    #Getter methods

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.quantity

    def getType(self):
        return self.book_type

    #Setter methods
    def setPrice(self, newPrice):
        self.price = newPrice

    def setQuantity(self, newQuantity):
        self.quantity = newQuantity

    #String of the book
    def __repr__(self):
        return (f"Title: {self.title}, Author: {self.author}, "
                f"Price: ${self.price:.2f}, Quantity: {self.quantity}, "
                f"Type: {self.book_type}")



#FictionBook subclass


class FictionBook(Book):
   

    def __init__(self, title, author, price, quantity, genre):
        
         #parent class constructor
        
        super().__init__(title, author, price, quantity, 'FictionBook')
        self.genre = genre  #property for fiction books

    #Getter for genre
    
    def getGenre(self):
        return self.genre

    #String representation which includes genre
    
    def __repr__(self):
        return super().__repr__() + f", Genre: {self.genre}"


#NonFictionBook subclass


class NonFictionBook(Book):
   

    def __init__(self, title, author, price, quantity, subject):
       
       #Name parent class constructor
        
        super().__init__(title, author, price, quantity, 'NonFictionBook')
        self.subject = subject  # Additional property for nonfiction books

    #Getter method for subject
    
    def getSubject(self):
        return self.subject

    #String representation including subject
   
    def __repr__(self):
        return super().__repr__() + f", Subject: {self.subject}"



#Test classes


def test_books():
    """Function to test the Books."""

    #Create a FictionBook object
    
    fiction = FictionBook("The Book Thief", "Markus Zusak", 25.50, 17, "historical fiction novel ")
    print(fiction)

    #Generate a NonFictionBook object
    
    nonfiction = NonFictionBook("The Diary of a Young Girl", "Anne Frank", 45.70, 12, "autobiography")
    print(nonfiction)

    #Update the price of the fiction book and the quantity of the nonfiction book
    
    fiction.setPrice(17.99)
    nonfiction.setQuantity(7)

    #Updated book information
    
    print("\nAfter updates:")
    print(fiction)
    print(nonfiction)

    #Use of getter methods
    
    print("\nGetter tests:")
    print("Fiction Book Genre:", fiction.getGenre())
    print("NonFiction Book Subject:", nonfiction.getSubject())



#Run the test 


if __name__ == "__main__":
    test_books()

