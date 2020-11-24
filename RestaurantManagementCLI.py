from Admin import *
from User import *
from time import sleep
from os import system, name

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
    dictPrint(Admin.getIngredientList())

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
    listPrint(Admin.getDishMenu())

def doExportBillData():
    fname = "BillData.txt"
    Admin.exportBillData(fname)
    print("Bill data exported to: " + fname)

def doGenIngOrderInvoice():
    n = int(input("Enter new no. of Ingredients: "))
    for i in range(n):
        ingId = int(input("Ingredient ID #" + str(i) + ": "))
        qty   = int(input("Ingredient Qty #" + str(i) + ": "))
        Admin.addIngredientQuantity(ingId, qty)

    amt = float(input("Enter Total Bill Amount: "))
    print("Generating Invoice...")
    Admin.addMonthExpense(amt)
    if Admin.canWithdrawCash(amt) == True:
        print("Printing cheque for Rs. " + str(amt) + "...")
        Admin.withdrawCash(amt)
        doGetCash()
    else:
        print("(!) Insufficient Cash")
        print("(!) Please write cheque manually")

def doWithdrawCash():
    cash = float(input("Enter Amount to Withdraw: "))
    if Admin.canWithdrawCash(cash) == True:
        Admin.withdrawCash(cash)
        print("Succesfully withdrawn Rs. " + str(cash))
        doGetCash()
    else:
        print("(!) Insufficient Cash")

def doDepositCash():
    cash = float(input("Enter Amount to Deposit: "))
    Admin.depositCash(cash)
    print("Succesfully Deposited Rs. " + str(cash))
    doGetCash()

def doGetCash():
    print("Available Cash: " + Admin.getCash())

def doPrintMonthlyStats():
    dishMenu  = Admin.getDishMenu()
    dishSales = Admin.getMonthDishSales()
    print("=======================================")
    print("Dish Name: Sale Quantity: Sale Amount")
    print("=======================================")
    totalAmt = 0
    for entry in dishMenu:
        dishId, name, price = entry[0], entry[1], entry[2]
        saleAmt = dishSales[dishId] * price
        print(name + ": " + str(dishSales[dishId]) + ": " + str(saleAmt))
        totalAmt += saleAmt

    print("=======================================")
    print("Total Sale Amount: ", totalAmt)
    print("Total Expenditure: ", Admin.getMonthExpense())
    print("Total Profit/Loss: ", totalAmt - Admin.getMonthExpense())

def adminMenu():
    while True:

        print("===================== ADMIN =====================")
        print("1.  Add New Ingredient")
        print("2.  Update Ingredient Price")
        print("3.  Print Ingredient List")
        print("4.  Add new Dish")
        print("5.  Update Dish Ingredients")
        print("6.  Update Dish Price")
        print("7.  Print Dish Menu")
        print("8.  Export Bill Data")
        print("9.  Generate Ingredient Order Invoice")
        print("10. Show Available Cash")
        print("11. Deposit Cash")
        print("12. Withdraw Cash")
        print("13. Print Monthly Statistics")

        choice = int(input("Enter Choice (0 to go back): "))
        if choice == 1:
            bannerDisplay(0)
            menuBar("a")
            print("Add New Ingredient\n")
            doAddNewIngredient()
            bannerDisplay(1)

        elif choice == 2:
            bannerDisplay(0)
            menuBar("a")
            print("Update Ingredient Price\n")
            doUpdateIngredientPrice()
            bannerDisplay(1)

        elif choice == 3:
            bannerDisplay(0)
            menuBar("a")
            print("Print Ingredient List\n")
            doPrintIngredientList()
            bannerDisplay(1)

        elif choice == 4:
            bannerDisplay(0)
            menuBar("a")
            print("Add new Dish\n")
            doAddNewDish()
            bannerDisplay(1)

        elif choice == 5:
            bannerDisplay(0)
            menuBar("a")
            print("Update Dish Ingredients\n")
            doUpdateDishIngredients()
            bannerDisplay(1)

        elif choice == 6:
            bannerDisplay(0)
            menuBar("a")
            print("Update Dish Price\n")
            doUpdateDishPrice()
            bannerDisplay(1)

        elif choice == 7:
            bannerDisplay(0)
            menuBar("a")
            print("Print Dish Menu\n")
            doPrintDishMenu()
            bannerDisplay(1)

        elif choice == 8:
            bannerDisplay(0)
            menuBar("a")
            print("Export Bill Data\n")
            doExportBillData()
            bannerDisplay(1)

        elif choice == 9:
            bannerDisplay(0)
            menuBar("a")
            print("Generate Ingredient Order Invoice \n")
            doGenIngOrderInvoice()
            bannerDisplay(1)

        elif choice == 10:
            bannerDisplay(0)
            menuBar("a")
            print("Show Available Cash\n")
            doGetCash()
            bannerDisplay(1)

        elif choice == 11:
            bannerDisplay(0)
            menuBar("a")
            print("Deposit Cash\n")
            doDepositCash()
            bannerDisplay(1)

        elif choice == 12:
            bannerDisplay(0)
            menuBar("a")
            print("Withdraw Cash\n")
            doWithdrawCash()
            bannerDisplay(0)

        elif choice == 13:
            bannerDisplay(0)
            menuBar("a")
            print("Print Monthly Statistics\n")
            doPrintMonthlyStats()
            bannerDisplay(1)

        elif choice == 0:
            bannerDisplay(0)
            break
        else:
            bannerDisplay(0)
            print("(!) Invalid Choice")
            bannerDisplay(1)

def userMenu():
    inputList = dict()
    while True:

        print("===================== USER ======================")
        print("1. Add Bill Item")
        print("2. Process Bill")
        print("3. End Day and Save")
        choice = int(input("Enter Choice (0 to go back): "))

        if choice == 1:
            bannerDisplay(0)
            menuBar("u")
            print("Add Bill Item\n")
            dishId       = int(input("Enter Dish ID: "))
            dishQuantity = int(input("Enter Dish Qty: "))
            if User.checkAvailability(dishId, dishQuantity) == True:
                inputList[dishId] = dishQuantity
                bannerDisplay(0)
            else:
                print("(!) Insufficient ingredients")
                bannerDisplay(1)

        elif choice == 2:
            bannerDisplay(0)
            menuBar("u")
            print("Process Bill\n")
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
            bannerDisplay(1)

        elif choice == 3:
            bannerDisplay(0)
            menuBar("u")
            print("End Day and Save\n")
            dayEndChoice = input("Are you sure? (y/n): ")
            if dayEndChoice == "y" or dayEndChoice == "Y":
                User.endDay()
            bannerDisplay(0)

        elif choice == 0:
            bannerDisplay(0)
            break

        else:
            bannerDisplay(1)
            print("(!) Invalid Choice")

def dictPrint(dictObject):
    for i in dictObject:
        print(str(i) + " " + dictObject[i])
def listPrint(listObject):
    for i in listObject:
        temp = ""
        for j in i:
            temp += '{:20}'.format(str(j)+" ")
        print(temp)

def menuBar(choice):
    if choice == "-":
        print("=================================================")
    if choice == "u":
        print("===================== USER ======================")
    if choice == "a":
        print("===================== ADMIN =====================")

def clear(choice):
    if choice == 1:
        temp = input("\n\nPress Enter to Continue")

    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def bannerDisplay(choice):
    clear(choice)
    print("\nDate: " + Admin.getCurDate())
    print("=================================================")
    print("####### Restaurant Management System v1.0 #######\n\n")

def main():
    Admin.initPersistentData()
    while True:
        bannerDisplay(0)
        print("(+) Press CTRL+C anywhere to return to main menu\n")
        print("===================== Menu ======================")
        print("Choose Operator: ")
        print("1. Admin")
        print("2. User")

        try:
            choice = int(input("Enter choice(0 to Exit): "))
            if choice == 1:
                bannerDisplay(0)
                adminMenu()
            elif choice == 2:
                bannerDisplay(0)
                userMenu()

            elif choice == 0:
                print("\nExiting...\n")
                sleep(1)
                clear(0)
                exit()
            else:
                bannerDisplay(0)
                print("(!) Invalid Choice")
                bannerDisplay(1)

        except ValueError:
            bannerDisplay(0)
            print("(!) Invalid Input")
            bannerDisplay(1)
        except LookupError:
            bannerDisplay(0)
            print("(!) Lookup Error Occured: Please check your input")
            bannerDisplay(1)
        except KeyboardInterrupt:
            bannerDisplay(0)
        except Exception:
            raise

if __name__ == "__main__":
    main()
