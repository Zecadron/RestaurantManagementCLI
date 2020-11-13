from DatabaseAPI import *

db = Database.getInstance()

def addNewIngredient(name, price, stock):
    db.ingredients.addIngredient(name, price, stock)
    return db.ingredients.getId(name)

def updateIngredientPrice(ingId, price):
    db.ingredients.setPrice(ingId, price)

def getIngredientList():
    return db.ingredients.getNamesByIds()

def addNewDish(name, price, ingReq):
    db.dishes.addDish(name, price)
    dishId = db.dishes.getId(name)
    for ingId in ingReq:
        db.dishIngredients.addDishIngredient(dishId, ingId, ingReq[ingId])
    return dishId

def updateDishIngredients(dishId, ingReq):
    db.dishIngredients.deleteDishIngredients(dishId)
    for ingId in ingReq:
        db.dishIngredients.addDishIngredient(dishId, ingId, ingReq[ingId])

def updateDishPrice(dishId, price):
    db.dishes.setPrice(dishId, price)

def getDishMenu():
    names = db.dishes.getNamesByIds()
    prices = db.dishes.getPricesByIds()
    menu = []
    for ingId in names:
        menu.append((ingId, names[ingId], prices[ingId]))
    return menu 

def exportBillData():
    pass
