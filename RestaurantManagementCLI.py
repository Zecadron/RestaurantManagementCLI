from DataIO import *
from Orders import *

def admin():
    pass

def user():
    pass

def main():
    while True:
        print("\nRestaurant Management System v0.1")
        print("=================================================")
        print("1. Admin")
        print("2. User")

        choice = int(input("Enter Choice (0 to exit): "))
        if choice == 1:
            admin()
        elif choice == 2:
            user()
        elif choice == 0:
            exit()
        else:
            print("Invalid Choice!")
 
if __name__ == "__main__":
    main()
