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

def addNewIngredient():
    pass

def updateIngredient():
    pass

def printIngredientList():
    pass

def addNewDish():
    pass

def updateDishIngredients():
    pass

def updateDishPrice():
    pass

def printDishMenu():
    pass

def exportBillData():
    pass

def admin():
    while True:
        print("\n=================================================")
        print("1. Add new Ingredient")
        print("2. Update Ingredient Price")
        print("3. Print Ingredient List")
        print("4. Add new Dish")
        print("5. Update Dish Ingredients")
        print("6. Update Dish Price")
        print("7. Print Dish Menu")
        print("8. Export Bill Data")

        choice = int(input("Enter Choice (0 to go back): "))
        if choice == 1:
            addNewIngredient()
        elif choice == 2:
            updateIngredient()
        elif choice == 3:
            printIngredientList()
        elif choice == 4:
            addNewDish()
        elif choice == 5:
            updateDishIngredients()
        elif choice == 6:
            updateDishPrice()
        elif choice == 7:
            printDishMenu()
        elif choice == 8:
            exportBillData()
        elif choice == 0:
            break
        else:
            print("Invalid Choice!")

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
