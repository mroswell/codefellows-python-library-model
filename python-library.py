class Library:
    """ A Library """

    def __init__(self, lib_name, shelf_names = ['Nutrition', 'Travel', 'Politics', 'Tech']):
        """  (Library, str, list of str) -> NoneType
        >>> library1 = Library('Old Alexandria')
        >>>
        """
        self.lib_name = lib_name

        # Every library starts with a set of shelves
        # shelves -> [ ShelfObject1, ShelfObject2 ... ]
        self.shelves=[]

        # set up the library shelves
        for i in shelf_names:
            self.shelves.append(Shelf(i))

        # The library should be aware of a number of shelves. 
        self.num_shelves=len(self.shelves)


    # The library should have a method to report all books it contains.
    def list_books(self):
        """  (Library) -> NoneType
        print a list of books
        """
        print 'Library: %s\n Books:' %(self.lib_name)
        for shelf_object in self.shelves:
            for book in shelf_object.books:
                # print book.book_name + " ("+shelf_object.shelf_name+")"
                print '  %s (%s)' %(book.book_name, shelf_object.shelf_name)

    # We always need more shelves
    def add_shelf (self, shelf):
        """  (Library, Shelf) -> NoneType
        Add a shelf to a book.

        """
        self.shelves.append(shelf)
        self.num_shelves+=1

class Shelf:
    """ A shelf in a library """

    def __init__(self, shelf_name):
        """ (Shelf, str) -> NoneType

        """
        self.shelf_name = shelf_name

        # Each shelf should know what books it contains
        self.books=[]

class Book:
    """ A Book"""

    def __init__(self, book_ID, book_name):
        """  (Book, str,str) -> NoneType
        >>> Book = Book('N10','Raw Food Made Easy') 
        >>>
        """
        self.book_ID=book_ID
        self.book_name = book_name

    # Book objects have "enshelf" and "unshelf" methods to control what shelf the book is sitting on. 
    def enshelf(self, shelf):
        """  (Book, Shelf) -> NoneType
        >>> bookN001.enshelf(nutrition_shelf) 
        >>>
        """
        shelf.books.append(self)


    def unshelf(self, current_shelf):
        """  (Book, Shelf) -> NoneType
        book1.unshelf(nutrition_shelf)
        """
        
        current_shelf.books.remove(self)



if __name__ == '__main__':

    # Create library and shelves
    library1=Library("Old Alexandria")
    nutrition_shelf=library1.shelves[0]
    travel_shelf=library1.shelves[1]
    cookbook_shelf = Shelf("Cookbooks")
    library1.add_shelf(cookbook_shelf)

    # Add books, and enshelf them.
    bookN001=Book("N10", "Raw Food Made Easy")
    bookN001.enshelf(cookbook_shelf)
    bookN002=Book("N11", "Eat Crops, Not Crap")
    bookN002.enshelf(nutrition_shelf)
    bookT101=Book("T20", "Your Guide to Greece")
    bookT101.enshelf(travel_shelf)
    bookT102=Book("T21", "Rome in a Day")
    bookT102.enshelf(travel_shelf)

    # Unshelf a book whose title is not acceptable for children
    bookN002.unshelf(nutrition_shelf) 

    # List the books 
    library1.list_books()

    # Display shelf count, and shelf detail
    print " "+ str(library1.num_shelves) + " Shelves: "
    
    for shelfObj in library1.shelves:
        print "  %s" %(shelfObj.shelf_name)


    

# TODO:
    # Modify unshelf method to set the shelf to "unshelved" to ensure that the book displays in the list_books() function
    #   (Currently unshelved books do not get printed.)
    # I'd also prefer a way to unshelf without having to know the existing shelf.
    # Set shelf during the book instantiation
    
