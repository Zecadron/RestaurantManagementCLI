from DatabaseAPI import *

dishIngredients = DishIngredients()
ingredients = Ingredients()
dishes = Dishes()
billDishes = BillDishes()
bill = Bill()

def checkAvailability(dishId, dishQuantity):
    consumedIngredientIds = dishIngredients.getIngredientIds(dishId)
    for ingId in consumedIngredientIds:
        if dishIngredients.getQuantity(dishId, x) * dishQuantity > ingredients.getStock():
            return False
    return True

def deductIngredients(dishId, dishQuantity):
    consumedIngredientIds = dishIngredients.getIngredientIds(dishId)
    for ingId in consumedIngredientIds:
        consumedStock = dishIngredients.getQuantity(dishId, ingId) * dishQuantity
        newStock = ingredients.getStock(ingId) - consumedStock
        ingredients.setStock(ingId,newStock)

def generateBill(inputList):
    total = 0
    for dishId in inputList:
        total = total + inputList[dishId]

    billText = "Sample Text"
    return billText

def endDay():
    print("The End\n")
