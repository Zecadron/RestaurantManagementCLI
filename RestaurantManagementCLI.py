import User
import Admin

def doAddNewIngredient():
    Admin.addNewIngredient()

def doUpdateIngredientPrice():
    Admin.updateIngredientPrice()

def doPrintIngredientList():
    Admin.getIngredientList()

def doAddNewDish():
    Admin.addNewDish()

def doUpdateDishIngredients():
    Admin.updateDishIngredients()

def doUpdateDishPrice():
    Admin.updateDishPrice()

def doPrintDishMenu():
    Admin.getDishMenu()

def doExportBillData():
    Admin.exportBillData()

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
            doAddNewIngredient()
        elif choice == 2:
            doUpdateIngredientPrice()
        elif choice == 3:
            doPrintIngredientList()
        elif choice == 4:
            doAddNewDish()
        elif choice == 5:
            doUpdateDishIngredients()
        elif choice == 6:
            doUpdateDishPrice()
        elif choice == 7:
            doPrintDishMenu()
        elif choice == 8:
            doExportBillData()
        elif choice == 0:
            break
        else:
            print("(!)Invalid Choice")

def userMenu():
    inputList = dict()
    while True:
        print("\n=================================================")
        print("1. Add Bill Item")
        print("2. Process Bill")
        choice = int(input("Enter Choice: (0 to end day & save): "))

        if choice == 1:
            print("Enter Dish ID and Quantity:")
            dishId       = int(input())
            dishQuantity = int(input())
            if User.checkAvailability(dishId, dishQuantity) == True:
                inputList[dishId] = dishQuantity
            else:
                print("(!)Insufficient ingredients")

        elif choice == 2:
            print(inputList)
            confirmBill = input("Confirm? (y/n): ")
            if confirmBill == "y" or confirmBill == "Y":
                print("Bill confirmed")
                User.generateBill(inputList)
                inputList.clear()
            else:
                inputList.clear()
                print("Deleted current bill")
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
