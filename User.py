from DatabaseAPI import *

db = Database.getInstance()

def checkAvailability(dishId, dishQuantity):
    consumedIngredientIds = db.dishIngredients.getIngredientIds(dishId)
    for ingId in consumedIngredientIds:
        if db.dishIngredients.getQuantity(dishId, x) * dishQuantity > db.ingredients.getStock():
            return False
    return True

def deductIngredients(dishId, dishQuantity):
    consumedIngredientIds = db.dishIngredients.getIngredientIds(dishId)
    for ingId in consumedIngredientIds:
        consumedStock = db.dishIngredients.getQuantity(dishId, ingId) * dishQuantity
        newStock = db.ingredients.getStock(ingId) - consumedStock
        db.ingredients.setStock(ingId,newStock)

def generateBill(inputList):
    total = 0
    for dishId in inputList:
        total = total + inputList[dishId]

    billText = "Sample Text"
    return billText

def endDay():
    print("The End\n")
