def checkAvailability(foodId, foodAmount):
    return True

def generateBill(inputList):
    print(inputList)
    confirmBill = input("Confirm? (y/n): ")
    if confirmBill == "y" or confirmBill == "Y":
        print("Bill confirmed")
    else:
        print("Deleted current bill")
    pass

def endDay():
    print("The End\n")
    pass
