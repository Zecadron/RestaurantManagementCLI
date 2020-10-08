from DatabaseAPI import *

DishIngredients = DishIngredients()
Ingredients = Ingredients()
Dishes = Dishes()
BillDishes = BillDishes()
Bill = Bill()

def checkAvailability(dishId, dishQuantity):
    consumedIngredientsId = DishIngredients.getIngredientIds(dishId)
    for x in consumedIngredientsId:
        if DishIngredients.getQuantity(dishId,x)*dishQuantity > Ingredients.getStock():
            return False
    return True

def generateBill(inputList):
    pass

def endDay():
    print("The End\n")
    pass
