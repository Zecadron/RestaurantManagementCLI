from DatabaseAPI import *

db = Database.getInstance()

class User:
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
        if not type(consumedIngredientIds) is list:
            consumedIngredientIds = [consumedIngredientIds]
        for ingId in consumedIngredientIds:
            consumedStock = db.dishIngredients.getQuantity(dishId, ingId) * dishQuantity
            newStock      = db.ingredients.getStock(ingId) - consumedStock
            db.ingredients.setStock(ingId, newStock)
            db.ingredients.setUsedD3(ingId, db.ingredients.getUsedD3(ingId) + consumedStock)

    def generateBill(inputList):
        billText = ""
        total = 0
        for dishId in inputList:
            User.deductIngredients(dishId, inputList[dishId])
            priceDish = db.dishes.getPrice(dishId) * inputList[dishId]
            total     = total + priceDish
            billText = billText + '{:20}'.format(db.dishes.getName(dishId)) + '{:20}'.format(str(int(inputList[dishId]))) +'{:20}'.format(str(priceDish)) + "\n"
        billText = billText + "------------------------------------------------\nTotal : " + str(total) + "\n"

        billId = db.bills.addBill(db.persistentData.getValue(PersistentData.KEY_CUR_DATE), total)
        for dishId in inputList:
            db.billDishes.addBillDishes(billId, dishId, inputList[dishId])

        currentCash = float(db.persistentData.getValue(PersistentData.KEY_CASH))
        db.persistentData.setValue(PersistentData.KEY_CASH, currentCash + total)
        billText = "\n" + '{:20}'.format("Dish Name") + '{:20}'.format("Quantity") + '{:20}'.format("Price") + "\n" + billText
        return billText

    def orderIngredient(ingId, orderQuantity):
        orderText = db.persistentData.getValue(PersistentData.KEY_CUR_DATE) + "," + str(ingId) + "," + db.ingredients.getName(ingId) + "," + str(int(orderQuantity)) + "\n"
        orderHistory = open("OrderHistory.txt", "a")
        orderHistory.write(orderText)
        orderHistory.close()

    def endDay():
        for ingId in db.ingredients.getAllId():
            if db.ingredients.getStock(ingId) < int(db.ingredients.getUsedAverage(ingId)*2):
                orderIngredient(ingId, db.ingredients.getUsedAverage(ingId)*2)

            usedD1 = db.ingredients.getUsedD1(ingId)
            usedD2 = db.ingredients.getUsedD2(ingId)
            usedD3 = db.ingredients.getUsedD3(ingId)
            newAverage = int((usedD1 + usedD2 + usedD3)/3)

            db.ingredients.setUsedD1(ingId, usedD2)
            db.ingredients.setUsedD2(ingId, usedD3)
            db.ingredients.setUsedD3(ingId, 0)
            db.ingredients.setUsedAverage(ingId, newAverage)

        curDate = db.persistentData.getValue(PersistentData.KEY_CUR_DATE)
        newDate = db.getDateNext(curDate, 1)
        db.persistentData.setValue(PersistentData.KEY_CUR_DATE, newDate)
