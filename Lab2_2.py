class Author:
    ## Create class named Author
    def __init__(self, name): ## The __init__ method
        self.name = name
        self.books = []           ## Empty book list is created

    def publish(self,book_title):  ## published method with the book_title as an argument
        if book_title in self.books:
            print(f'{book_title}: already published.')
        else:
            self.books.append(book_title)   ## append will add the book_title

    def __str__(self):  ## a string method is added
       ## book_title = ', '.join(self.books) or 'No published books'
       if len(self.books) == 0:
           book_title = "No publish books"
       else:
           book_title = ', '.join(self.books)
       return f'{self.name}: {book_title}'  ## it returns a String with author's name and
    ## all their book's titles

def main():  ## Here is the main function to test the class

    murach = Author('Joel Murach')
    murach.publish("Murach's C# 7th Edition")
    murach.publish("Murach's SQL Server for Developers")
    murach.publish("Murach's Python Programing")
    print(murach)

    adade = Author('Adade Gbadoe')
    print(adade)

    bob = Author("Bob Roberts")
    bob.publish("The Quick Brown Fox")
    bob.publish("Something Else")
    bob.publish("The Quick Brown Fox")
    print(bob)

main()  ## call the main to execute the code