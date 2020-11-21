from DatabaseAPI import *

db = Database.getInstance()

def checkAvailability(dishId, dishQuantity):
    consumedIngredientIds = db.dishIngredients.getIngredientIds(dishId)
    if isinstance(consumedIngredientIds, int):
        ingId = consumedIngredientIds
        if db.dishIngredients.getQuantity(dishId, ingId) * dishQuantity > db.ingredients.getStock(ingId):
            return False
    else:
        for ingId in consumedIngredientIds:
            if db.dishIngredients.getQuantity(dishId, ingId) * dishQuantity > db.ingredients.getStock(ingId):
                return False
    return True

def deductIngredients(dishId, dishQuantity):
    consumedIngredientIds = db.dishIngredients.getIngredientIds(dishId)
    if isinstance(consumedIngredientIds, int):
            ingId = consumedIngredientIds
            consumedStock = db.dishIngredients.getQuantity(dishId, ingId) * dishQuantity
            newStock      = db.ingredients.getStock(ingId) - consumedStock
            db.ingredients.setStock(ingId, newStock)
            db.ingredients.setUsedD3(ingId, db.ingredients.getUsedD3(ingId) + consumedStock)
    else:
        for ingId in consumedIngredientIds:
            consumedStock = db.dishIngredients.getQuantity(dishId, ingId) * dishQuantity
            newStock      = db.ingredients.getStock(ingId) - consumedStock
            db.ingredients.setStock(ingId, newStock)
            db.ingredients.setUsedD3(ingId, db.ingredients.getUsedD3(ingId) + consumedStock)

def generateBill(inputList):
    billText = ""
    total = 0
    for dishId in inputList:
        deductIngredients(dishId, inputList[dishId])
        priceDish = db.ingredients.getPrice(dishId) * inputList[dishId]
        total     = total + priceDish
        billText = billText + db.dishes.getName(dishId) + " : " + str(int(inputList[dishId])) + " : " + str(priceDish) + "\n"
    billText = billText + "------------------------------\nTotal : " + str(total) + "\n"

    billId = db.bills.addBill(db.persistentData.getValue(PersistentData.KEY_CUR_DATE), total)
    for dishId in inputList:
        db.billDishes.addBillDishes(billId, dishId, inputList[dishId])

    currentCash = float(db.persistentData.getValue(PersistentData.KEY_CASH))
    db.persistentData.setValue(PersistentData.KEY_CASH, currentCash + total)
    billText = "Dish Name : Quantity : Price\n" + billText
    return billText

def orderIngredient(ingId, orderQuantity):
    orderText = db.persistentData.getValue(PersistentData.KEY_CUR_DATE) + "," + str(ingId) + "," + db.ingredients.getName(ingId) + "," + str(int(orderQuantity)) + "\n"
    orderHistory = open("OrderHistory.txt", "a")
    orderHistory.write(orderText)
    orderHistory.close()

def endDay():
    for ingId in db.ingredients.getAllId():
        if db.ingredients.getStock(ingId) < float(db.persistentData.getValue(PersistentData.KEY_THRESHOLD)):
            orderIngredient(ingId, db.ingredients.getUsedAverage(ingId))

        usedD1 = db.ingredients.getUsedD1(ingId)
        usedD2 = db.ingredients.getUsedD2(ingId)
        usedD3 = db.ingredients.getUsedD3(ingId)
        newThreshold = int((usedD1 + usedD2 + usedD3)/3)
        newAverage   = newThreshold * 2

        db.ingredients.setUsedD1(ingId, usedD2)
        db.ingredients.setUsedD2(ingId, usedD3)
        db.ingredients.setUsedD3(ingId, 0)
        db.persistentData.setValue(PersistentData.KEY_THRESHOLD, newThreshold)
        db.ingredients.setUsedAverage(ingId, newAverage)

    curDate = db.persistentData.getValue(PersistentData.KEY_CUR_DATE)
    newDate = db.getDateNext(curDate, 1)
    db.persistentData.setValue(PersistentData.KEY_CUR_DATE, newDate)
