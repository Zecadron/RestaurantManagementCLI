from DatabaseAPI import *

db = Database.getInstance()

def checkAvailability(dishId, dishQuantity):
    consumedIngredientIds = db.dishIngredients.getIngredientIds(dishId)
    for ingId in consumedIngredientIds:
        if db.dishIngredients.getQuantity(dishId, ingId) * dishQuantity > db.ingredients.getStock(ingId):
            return False
    return True

def deductIngredients(dishId, dishQuantity):
    consumedIngredientIds = db.dishIngredients.getIngredientIds(dishId)
    for ingId in consumedIngredientIds:
        consumedStock = db.dishIngredients.getQuantity(dishId, ingId) * dishQuantity
        newStock      = db.ingredients.getStock(ingId) - consumedStock
        db.ingredients.setStock(ingId, newStock)
        db.ingredients.setUsedD3(ingId, db.ingredients.getUsedD3(ingId) + consumedStock)

def generateBill(inputList):
    total = db.persistentData.getValue(PersistentData.KEY_CASH)
    for dishId in inputList:
        deductIngredients(dishId, inputList[dishId])
        priceDish = db.ingredients.getPrice * inputList[dishId]
        total     = total + priceDish
        print("Sample Text 1")
    print("Total: " + total)
    db.persistentData.setValue(PersistentData.KEY_CASH, total)
    pass

def orderIngredient(ingId, orderQuantity):
    print("Sample Text 2")
    pass

def endDay():
    for ingId in db.ingredients.getAllId():
        if db.ingredients.getStock(ingId) < db.persistentData.getValue(PersistentData.KEY_THRESHOLD):
            orderIngredient(ingId, db.ingredients.getUsedAverage())

        usedD1 = db.ingredients.getUsedD1(ingId)
        usedD2 = db.ingredients.getUsedD2(ingId)
        usedD3 = db.ingredients.getUsedD3(ingId)
        newAvg = (usedD1 + usedD2 + usedD3)/3
        db.setUsedD1(ingId, usedD2)
        db.setUsedD2(ingId, usedD3)
        db.setUsedD3(ingId, 0)
        db.ingredients.setUsedAverage(ingId, newAvg)

    print("The End\n")
