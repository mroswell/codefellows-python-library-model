class Library:
    """ A Library """

    def __init__(self, lib_name, shelf_names = ['Nutrition', 'Travel', 'Politics', 'Tech']):
        """  (Library, str, list of str) -> NoneType
        >>> library1 = Library('Old Alexandria')
        >>>
        """
        self.lib_name = lib_name
        self.unshelf_rack = Shelf(".Unshelved.")

        # Every library starts with a set of shelves
        # shelves -> [ ShelfObject1, ShelfObject2 ... ]
        self.shelves=[]
        self.shelves.append(self.unshelf_rack)

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

    # every book knows which library it belongs to

    def __init__(self, book_ID, book_name, mylib):
        """  (Book, str,str) -> NoneType
        >>> Book = Book('N10','Raw Food Made Easy') 
        >>>
        """
        self.book_ID=book_ID
        self.book_name = book_name
        self.library=mylib

    # Book objects have "enshelf" and "unshelf" methods to control what shelf the book is sitting on. 
    def enshelf(self, shelf):
        """  (Book, Shelf) -> NoneType
        >>> bookN001.enshelf(nutrition_shelf) 
        >>>
        """
        shelf.books.append(self)
        # print 'Book  %s -> (%s)' %(self.book_name, shelf.shelf_name)


    def unshelf(self, current_shelf):
        """  (Book, Shelf) -> NoneType
        book1.unshelf(nutrition_shelf)
        """

        # remove from current shelf
        current_shelf.books.remove(self)

        # move to .Unshelved. rack
        self.enshelf(self.library.unshelf_rack)



if __name__ == '__main__':

    # Create library and shelves
    library1=Library("Old Alexandria")
    nutrition_shelf=library1.shelves[1]
    travel_shelf=library1.shelves[2]
    cookbook_shelf = Shelf("Cookbooks")
    library1.add_shelf(cookbook_shelf)

    # Add books, and enshelf them.
    bookN101=Book("N10", "Raw Food Made Easy", library1)
    bookN101.enshelf(cookbook_shelf)
    bookN102=Book("N11", "Eat Crops, Not Crap", library1)
    bookN102.enshelf(nutrition_shelf)
    bookT201=Book("T20", "Your Guide to Greece", library1)
    bookT201.enshelf(travel_shelf)
    bookT202=Book("T21", "Rome in a Day", library1)
    bookT202.enshelf(travel_shelf)

    # Unshelf a book whose title is not acceptable for children
    bookN102.unshelf(nutrition_shelf) 

    # List the books 
    library1.list_books()

    # Display shelf count, and shelf detail
    print " "+ str(library1.num_shelves) + " Shelves: "
    
    for shelfObj in library1.shelves:
        print "  %s" %(shelfObj.shelf_name)


    

# TODO:
    # DONE. Modify unshelf method to set the shelf to "unshelved" to ensure that the book displays in the list_books() function
    # I'd also prefer a way to unshelf without having to know the existing shelf.
    # Set shelf during the book instantiation
    
