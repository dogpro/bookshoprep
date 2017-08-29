import pickle

class Books:

    def __init__(self):
        self.books = []
        self.found_book = []


    def getCreateBookArgs(self):
        print("Input Author: ")
        author = input()
        print("Input name book: ")
        name = input()
        print("Input year of publication: ")
        year = int(input())
        if year > 0:
            return (author, name, year)
        else:
            raise ValueError("Year must be positive!")

    def getCreateBookArgsFromFile(self):
        pass

    def createBook(self, author, name, year):
        self.books.append({"id":str(len(self.books)+1), "author":author, "name":name, "year":str(year)})

    def SaveFile(self):
        with open("test.pickle", "wb") as file:
            pickle.dump(self.books, file)

    def LoadFile(self):
        with open("test.pickle", "wb") as file:
            load_file = pickle.load(file)
            print(load_file)

    def deleteBookById(self, id):

        for book in self.books:
            if book["id"] == id:
                self.books.remove(book)
                break


    def searchBook_ID(self, sought_book):
        for book in self.books:
            if book["id"] == sought_book:
                self.found_book.append(book)
        print(self.found_book)

    def searchBook_author(self, sought_book):
        for book in self.books:
            if book["author"] == sought_book:
                self.found_book.append(book)
        print(self.found_book)

    def searchBook_name(self, sought_book):
        for book in self.books:
            if book["name"] == sought_book:
                self.found_book.append(book)
        print(self.found_book)

    def searchBook_year(self, sought_book):
        for book in self.books:
            if book["year"] == sought_book:
                self.found_book.append(book)
        print(self.found_book)


    def printBooks(self):
        for book in self.books:
            print(book)
