import User

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

def adminMenu():
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

def userMenu():
    inputList = dict()
    while True:
        print("\n=================================================")
        print("1. Enter Bill Item")
        print("2. Process Bill")
        choice = int(input("Enter Choice: (0 to end day & save): "))

        if choice == 1:
            print("Enter Food ID and Amount:")
            dishId       = int(input())
            dishQuantity = int(input())
            if User.checkAvailability(dishId, dishQuantity) == True:
                inputList[dishId] = dishQuantity
            else:
                print("(!)Insufficient ingredients")

        elif choice == 2:
            User.generateBill(inputList)
            inputList.clear()
            print("Bill succesfully processed")

        elif choice == 0:
            dayEndChoice = input("Are you sure? (y/n): ")
            if dayEndChoice == "y" or dayEndChoice == "Y":
                User.endDay()
                break
        else:
            print("(!)Invalid Choice")

def main():
    while True:
        print("\n=================================================")
        print("Restaurant Management System v0.1")
        print("=================================================")
        print("1. Admin")
        print("2. User")

        choice = int(input("Enter Choice (0 to exit): "))
        if choice == 1:
            adminMenu()
        elif choice == 2:
            userMenu()
        elif choice == 0:
            exit()
        else:
            print("(!)Invalid Choice")

if __name__ == "__main__":
    main()
