from DataIO import *
from Orders import *

def checkAvailability(foodId, foodAmount):
    return True

def generateBill(inputList):
    print(inputList)
    pass

def endDay():
    print("The End\n")
    pass
def admin():
    pass

def user():
    inputList = dict()
    while True:
        print("\n=================================================")
        print("1: Enter items in the Bill\n2: Process Bill\n0: End the day and exit\n")
        choice = int(input())

        if(choice == 1):
            print("Enter Food ID and Amount:")
            foodId     = int(input())
            foodAmount = int(input())
            if(checkAvailability(foodId, foodAmount) == True):
                inputList[foodId] = foodAmount
            else:
                print("(!)Insufficient ingredients")

        elif(choice == 2):
            generateBill(inputList)
            inputList.clear()
            print("Bill succesfully processed")

        elif(choice == 0):
            dayendchoice = input("Are you sure? (y/n): ")
            if(dayendchoice == "y"):
                endDay()
                break
        else:
            print("Invalid Choice")
    pass

def main():
    while True:
        print("=================================================")
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
