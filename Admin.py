from DatabaseAPI import *

db = Database.getInstance()

class Admin:

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

    def addIngredientQuantity(ingId, qty):
        stock = db.ingredients.getStock(ingId)
        db.ingredients.setStock(ingId, stock + qty)

    def addMonthExpense(amt):
        curAmt = float(db.persistentData.getValue(PersistentData.KEY_MONTH_EXPEN))
        db.persistentData.setValue(PersistentData.KEY_MONTH_EXPEN, curAmt + amt)

    def getMonthExpense():
        return float(db.persistentData.getValue(PersistentData.KEY_MONTH_EXPEN))

    def getMonthDishSales():
        allDishSales = dict()
        for dishId in db.dishes.getNamesByIds():
            allDishSales[dishId] = 0
        yearMonthStr = Admin.getCurDate()[:-2]
        for i in range(1,32):
            dayStr = ('0' + str(i)) if i < 10 else str(i)
            dateStr = yearMonthStr + dayStr
            billIds = db.bills.getBillIdsOnDate(dateStr)
            if not type(billIds) is list:
                billIds = [billIds]
            for billId in billIds:
                dishIds  = db.billDishes.getDishIds(billId)
                dishQtys = db.billDishes.getDishQtys(billId)
                if not type(dishIds) is list:
                    dishIds = [dishIds]
                if not type(dishQtys) is list:
                    dishQtys = [dishQtys]
                for i in range(len(dishIds)):
                    allDishSales[dishIds[i]] += dishQtys[i]
        return allDishSales

    def canWithdrawCash(cash):
        if cash <= float(db.persistentData.getValue(PersistentData.KEY_CASH)):
            return True
        else:
            return False

    def withdrawCash(cash):
        currentCash = float(db.persistentData.getValue(PersistentData.KEY_CASH))
        currentCash = currentCash - cash
        db.persistentData.setValue(PersistentData.KEY_CASH, currentCash)

    def depositCash(cash):
        currentCash = float(db.persistentData.getValue(PersistentData.KEY_CASH))
        currentCash = currentCash + cash
        db.persistentData.setValue(PersistentData.KEY_CASH, currentCash)

    def getCash():
        return db.persistentData.getValue(PersistentData.KEY_CASH)

    def getCurDate():
        return db.persistentData.getValue(PersistentData.KEY_CUR_DATE)

    def initPersistentData():
        if not db.persistentData.keyExists(PersistentData.KEY_CUR_DATE):
            db.persistentData.insertKey(PersistentData.KEY_CUR_DATE, db.getDateNow())
        if not db.persistentData.keyExists(PersistentData.KEY_MONTH_EXPEN):
            db.persistentData.insertKey(PersistentData.KEY_MONTH_EXPEN, 0)
        if not db.persistentData.keyExists(PersistentData.KEY_CASH):
            db.persistentData.insertKey(PersistentData.KEY_CASH, 0)

    def exportBillData(fname):
        billIds = db.bills.getAllId()
        billData = open(fname, "w")
        for billId in billIds:
            entry = str(billIds[billId]) + "," + db.bills.getDate(billId) \
                    + "," + str(db.bills.getTotal(billId)) + "\n"
            billData.write(entry)
        billData.close()
