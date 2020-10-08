from DatabaseAPI import *

DishIngredients = DishIngredients()
Ingredients = Ingredients()
Dishes = Dishes()
BillDishes = BillDishes()
Bill = Bill()

def checkAvailability(dishId, dishQuantity):
    consumedIngredientsId = DishIngredients.getIngredientIds(dishId)
    for ingId in consumedIngredientsId:
        if DishIngredients.getQuantity(dishId,x)*dishQuantity > Ingredients.getStock():
            return False
    return True

def deductIngredients(dishId, dishQuantity):
    consumedIngredientsId = DishIngredients.getIngredientIds(dishId)
    for ingId in consumedIngredientsId:
        consumedStock = DishIngredients.getQuantity(dishId, ingId) * dishQuantity
        newStock = Ingredients.getStock(ingId) - consumedStock
        Ingredients.setStock(ingId,newStock)
    pass

def generateBill(inputList):
    Total = 0
    for dishId in inputList:
        Total = Total + inputList[dishId]

    billText = "Sample Text"
    return billText

def endDay():
    print("The End\n")
    pass
