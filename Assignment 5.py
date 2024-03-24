class Bookshow:

    def __init__(self):
        self.all_books={}


    def __str__(self,book_department,book_name,price):
        return f"Bookshow Book_department:{book_department}.\n Book_name:{book_name} .\n Price:{price} "
    

    def insert_book(self,book_department,book_name,price,quality):
        self.all_books[book_department]={'Name':book_name, 'price':price  ,'quality':quality} 
        return f"Added BOOK : {book_department} their book {book_name}"
    

    def remove_book(self, book_name):
        if book_name in self.all_books:
            del self.books[book_name]
            return f"Removed book: {book_name}"
        else:
            return f"Book not found in the shop."


    def select_book(self,book_name,price):
        if book_name in self.all_books:
            books=self.all_books[book_name]
            return f"book founded : {book_name} their {price}"
        else:
            return f"Book not found in the shop."
        

    def list_books(self):
        if self.all_books.__len__()==0:
            return f"Books available in the bookshop"
        else:
            return f"No books available."
        

    def checkout(self, book_name):
        if book_name in self.all_books and self.all_books[book_name]['quantity'] > 0:
            self.books[book_name]['quantity'] -= 1
            print(f"Checked out book: {book_name}. Remaining quantity: {self.all_books[book_name]['quantity']}")
        else:
            print("Book not available for checkout.")

my_bookshop = Bookshow()
print ("__str__ : \n",my_bookshop.__str__("Maths","matrices and calculas",550)) 
print ("insert_book:\n",my_bookshop.insert_book("maths",'statistics and numerical methods',647,10))
print ("checkout : \n",my_bookshop.checkout('matrices and calculas'))
print ("list_books : \n",my_bookshop.list_books())
print ("Remove the data : \n",my_bookshop.remove_book('matrices and calculas'))

"""
output:
__str__ : 
 Bookshow Book_department:Maths.
 Book_name:matrices and calculas .
 Price:550
insert_book:
 Added BOOK : maths their book statistics and numerical methods
Book not available for checkout.
checkout :
 None
list_books :
 No books available.
Remove the data :
 Book not found in the shop."""
                              

