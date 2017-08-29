from Book_Shop.Books import Books

Book = Books()

def create_book():
    Book.createBook( *Book.getCreateBookArgs() )

def delete_book():
    print_books()
    print("Input ID book: ")
    id = int(input())
    Book.deleteBookById(id)

def back_to_menu():
    main_menu()

def search_book():
    while True:
        dec_menu_search_book = {
            "1": Book.searchBook_ID,
            "2": Book.searchBook_author,
            "3": Book.searchBook_name,
            "4": Book.searchBook_year,
            "5": back_to_menu
        }
        menu_items_search_book = ["Search by ID", "Search by Author","Search by name",
                                  "Search by year", "Back"]

        print("     Search book")
        print("_______________________")
        for num, element in enumerate(menu_items_search_book, 1):
            print("|", num, "|", element)
        print("_______________________")
        print("Input value: ")

        input_value = input()

        if input_value != list(dec_menu_search_book.keys())[-1]:
            print("Введите критерий поиска: ")
            sought_book = input()
            print(dec_menu_search_book[input_value](sought_book))
        elif input_value == list(dec_menu_search_book.keys())[-1]:
            dec_menu_search_book[input_value]()
        else:
            print("Invalid input")


def print_books():

    Book.printBooks()

def save_file():
    Book.SaveFile()

def load_file():
    Book.LoadFile()

def main_menu():
    while True:
        dec_menu = {
            "1": create_book,
            "2": delete_book,
            "3": save_file,
            "4": load_file,
            "5": search_book,
            "6": print_books,
            "7": quit
        }



        menu_items = ["Create book", "Delete book", "Save file",
                      "Load file","Search book",
                      "Print books", "Quit"]

        print("         Menu")
        print("_______________________")
        for num, element in enumerate(menu_items, 1):
            print("|", num, "|", element)
        print("_______________________")
        print("Input value: ")

        input_value = input()

        if input_value in dec_menu:
            dec_menu[input_value]()
        else:
            print("Invalid input")

main_menu()


#TODO сохранение/загрузку из файла с помощью pickle
#TODO тесты для каждого метода класса Books
