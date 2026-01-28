'''
Simple Personal Library
Author: Alex Ortiz
Version: 1.0

'''
def show_menue():
    '''
    This is going to display the main menue options to the user
    '''
    print("\nPersonal Library Menue")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. List all Books")
    print("4. Search for a Book")
    print("5. Exit")

def add_book():
    pass

def remove_book():
    pass

def list_books():
    pass

def search_books():
    pass


def main():
    '''
    This is going to loop the menue options
    '''
    while True:
        show_menue()
        choice = input("choose an option: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            list_books()
        elif choice == "4":
            search_books()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Not valid, please try again.")
        

if __name__ == "__main__":
    main()