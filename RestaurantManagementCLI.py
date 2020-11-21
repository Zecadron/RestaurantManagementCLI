import User
import Admin

def doAddNewIngredient():
    name = input("Enter Ingredient Name: ")
    price = float(input("Enter Ingredient Price: "))
    stock = input("Enter Ingredient Stock: ")
    ingId = Admin.addNewIngredient(name, price, stock)
    print("Added Ingredient with ID: " + str(ingId))

def doUpdateIngredientPrice():
    ingId = int(input("Enter Ingredient ID: "))
    price = int(input("Enter new Price: "))
    Admin.updateIngredientPrice(ingId, price)
    print("Updated Ingredient Price")

def doPrintIngredientList():
    print(Admin.getIngredientList())

def doAddNewDish():
    name = input("Enter Dish Name: ")
    price = float(input("Enter Dish Price: "))
    n = int(input("Enter no. of Ingredients: "))
    ingReq = dict()
    for i in range(n):
        ingId = int(input("Ingredient ID #" + str(i) + ": "))
        ingReq[ingId] = int(input("Ingredient Qty #" + str(i) + ": "))

    dishId = Admin.addNewDish(name, price, ingReq)
    print("Added Dish with ID: " + str(dishId))

def doUpdateDishIngredients():
    dishId = int(input("Enter Dish ID: "))
    n = int(input("Enter new no. of Ingredients: "))
    ingReq = dict()
    for i in range(n):
        ingId = int(input("Ingredient ID #" + str(i) + ": "))
        ingReq[ingId] = int(input("Ingredient Qty #" + str(i) + ": "))

    Admin.updateDishIngredients(dishId, ingReq)
    print("Updated Dish Ingredients")

def doUpdateDishPrice():
    dishId = int(input("Enter Dish ID: "))
    price = float(input("Enter new Price: "))
    Admin.updateDishPrice(dishId, price)
    print("Updated Dish Price")

def doPrintDishMenu():
    print(Admin.getDishMenu())

def doExportBillData():
    Admin.exportBillData()

def doAddIngredientQuantity():
    ingId = int(input("Enter Ingredient ID: "))
    qty = int(input("Enter Quantity to be Added: "))
    Admin.addIngredientQuantity(ingId, qty)

def doWithdrawCash():
    cash = float(input("Enter Amount to Withdraw: "))
    if Admin.canWithdrawCash(cash) == True:
        Admin.withdrawCash(cash)
        print("Succesfully withdrawn Rs. " + str(cash))
        doGetCash()
    else:
        print("(!)Insufficient Cash")

def doDepositCash():
    cash = float(input("Enter Amount to Deposit: "))
    Admin.depositCash(cash)
    print("Succesfully Deposited Rs. " + str(cash))
    doGetCash()

def doGetCash():
    print("Available Cash: " + Admin.getCash())

def adminMenu():
    while True:
        print("\n=================================================")
        print("1.  Add New Ingredient")
        print("2.  Update Ingredient Price")
        print("3.  Print Ingredient List")
        print("4.  Add new Dish")
        print("5.  Update Dish Ingredients")
        print("6.  Update Dish Price")
        print("7.  Print Dish Menu")
        print("8.  Export Bill Data")
        print("9.  Add Ingredient Quantity")
        print("10. Show Available Cash")
        print("11. Deposit Cash")
        print("12. Withdraw Cash")

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
        elif choice == 9:
            doAddIngredientQuantity()
        elif choice == 10:
            doGetCash()
        elif choice == 11:
            doDepositCash()
        elif choice == 12:
            doWithdrawCash()
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
            dishId       = int(input("Enter Dish ID: "))
            dishQuantity = int(input("Enter Dish Qty: "))
            if User.checkAvailability(dishId, dishQuantity) == True:
                inputList[dishId] = dishQuantity
            else:
                print("(!)Insufficient ingredients")

        elif choice == 2:
            print(inputList)
            confirmBill = input("Confirm? (y/n): ")
            if confirmBill == "y" or confirmBill == "Y":
                print("Bill confirmed")
                billText = User.generateBill(inputList)
                print(billText)
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
    Admin.initDate()

    while True:
        print("\nDate: " + Admin.getCurDate())
        print("=================================================")
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
