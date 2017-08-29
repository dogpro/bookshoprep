class Shop:

    def print_menu(self):
        while True:
            menu_items = ["Create book", "Delete book",
                          "Search book", "Read book",
                          "Edit book", "Quit"]
            print("_______________________")
            for num,element in enumerate(menu_items,1):
                print("|", num, "|", element, "|")
            print("_______________________")