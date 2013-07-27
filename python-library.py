
class Library:
    """ A Library """

    def __init__(self, libname, numshelves):
        """  (Library, str, int) -> NoneType
        >>> library1 = Library('Old Alexandria', 545)
        >>>
        """
        self.libname = libname
        self.numshelves = numshelves

    def list_books(self):
        """  (Library) -> NoneType
        print a list of books
        (This method does not currently work.)

        """
        for book in self.Book:
            print book.bookname

        #return self.book

class Shelf:
    """ A shelf in a library """

    def __init__(self, shelfname, booksonshelf):
        """ (Shelf, str, list of str) -> NoneType

        """
        self.shelfname = shelfname
        self.booksonshelf = booksonshelf  

class Book:
    """ A Book"""

    def __init__(self, bookname, shelfname='No Shelf'):
        """  (Book, str, str) -> NoneType
        >>> Book = Book('Raw Food Made Easy', "Nutrition") 
        >>>
        """
        self.bookname = bookname
        self.shelfname = shelfname

    def enshelf(self, shelfname):
        """  (Book, str) -> NoneType
        >>> Book.enshelf("Nutrition") 
        >>> 
        """
        self.shelfname = shelfname

    def unshelf(self):
        """
        (This method does not currently work.)
        """
        self.shelfname = self.enshelf('No Shelf')
        # return self.enshelf('No Shelf')
        # self.shelfname = "No Shelf"
        # return self.shelfname

if __name__ == '__main__':

    library1 = Library('Old Alexandria', 545)
    shelf = Shelf('Nutrition',500)
    rawbook1  = Book('Raw Food Made Easy', "Nutrition")
    print library1.libname
    print rawbook1.bookname
    print rawbook1.shelfname
    rawbook1.enshelf("Cookbooks")
    print '"%s" is now on the %s shelf.'%(rawbook1.bookname, rawbook1.shelfname)
    # my unshelf method does not work
    rawbook1.unshelf 
    print rawbook1.shelfname + ', but this should be "No Shelf" (if the unshelf method worked)'
    # I'm having the same issue with the list_books method as I had on the ruby side
    # print library1.list_books


