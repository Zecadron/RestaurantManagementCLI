from SQLiteDBHelper import SQLiteDBHelper

# DB info
DB_NAME                 = "RMS.db"

# DB table names
TAB_INGREDIENTS         = "Ingredients"
TAB_DISH_INGREDIENTS    = "DishIngredients"
TAB_DISHES              = "Dishes"
TAB_BILL_DISHES         = "BillDishes"
TAB_BILLS               = "Bills"
TAB_PERSISTENT_DATA     = "PersistentData"

# Used for auto increment primary keys
# DO NOT CHANGE ITS VALUE!
COL_AUTO                = "auto"

class Ingredients:
    COL_ID          = "IngID"
    COL_NAME        = "IngName"
    COL_PRICE       = "IngPrice"
    COL_STOCK       = "Stock"
    COL_USED_D1     = "UsedD1"
    COL_USED_D2     = "UsedD2"
    COL_USED_D3     = "UsedD3"
    COL_USED_AVG    = "UsedAvg" 

    CREATE_TABLE = 'create table ' + TAB_INGREDIENTS + ' (' + \
        COL_ID + ' integer primary key autoincrement, ' + \
        COL_NAME + ' text not null, ' + \
        COL_PRICE + ' real, ' + \
        COL_STOCK + ' integer not null, ' + \
        COL_USED_D1 + ' integer not null, ' + \
        COL_USED_D2 + ' integer not null, ' + \
        COL_USED_D3 + ' integer not null, ' + \
        COL_USED_AVG + ' real);'

    def __init__(self, db):
        self.db = db

    def getId(self, name):
        return self.db.select(TAB_INGREDIENTS,
                self.COL_ID, (self.COL_NAME,), (name,))[name]

    def getStock(self, ingId):
        return self.db.select(TAB_INGREDIENTS,
                self.COL_STOCK, (self.COL_ID,), (ingId,))[ingId]

    def getAverage(self, ingId):
        return self.db.select(TAB_INGREDIENTS,
                self.COL_USED_AVG, (self.COL_ID,), (ingId,))[ingId]

    def getPrice(self, ingId):
        return self.db.select(TAB_INGREDIENTS,
                self.COL_PRICE, (self.COL_ID,), (ingId,))[ingId]

    def getName(self, ingId):
        return self.db.select(TAB_INGREDIENTS,
                self.COL_NAME, (self.COL_ID,), (ingId,))[ingId]

    def getNamesByIds(self):
        return self.db.select(TAB_INGREDIENTS, self.COL_NAME, (self.COL_ID,))

    def addIngredient(self, name, price, stock):
        self.db.insert(TAB_INGREDIENTS, (COL_AUTO, name, price, stock, 0, 0, 0, 0))

    def setPrice(self, ingId, price):
        self.db.update(TAB_INGREDIENTS, self.COL_PRICE, price, self.COL_ID, ingId)

class Dishes:
    COL_ID      = "DishID"
    COL_NAME    = "DishName"
    COL_PRICE   = "DishPrice"

    CREATE_TABLE = 'create table ' + TAB_DISHES + ' (' + \
        COL_ID + ' integer primary key autoincrement, ' + \
        COL_NAME + ' text not null, ' + \
        COL_PRICE + ' real);'

    def __init__(self, db):
        self.db = db

    def getId(self, name):
        return self.db.select(TAB_DISHES,
                self.COL_ID, (self.COL_NAME,), (name,))[name]

    def getName(self, dishId):
        return self.db.select(TAB_DISHES,
                self.COL_NAME, (self.COL_ID,), (dishId,))[dishId]

    def getPrice(self, dishId):
        return self.db.select(TAB_DISHES,
                self.COL_PRICE, (self.COL_ID,), (dishId,))[dishId]

    def getPricesByIds(self):
        return self.db.select(TAB_DISHES, self.COL_PRICE, (self.COL_ID,))

    def getNamesByIds(self):
        return self.db.select(TAB_DISHES, self.COL_NAME, (self.COL_ID,))

    def setPrice(self, dishId, price):
        self.db.update(TAB_DISHES, self.COL_PRICE, price, self.COL_ID, dishId)

    def addDish(self, name, price):
        self.db.insert(TAB_DISHES, (COL_AUTO, name, price))

class Bills:
    COL_ID      = "BillID"
    COL_DATE    = "BillDate"
    COL_TOTAL   = "TotalAmt"

    CREATE_TABLE = 'create table ' + TAB_BILLS + ' (' + \
        COL_ID + ' integer primary key autoincrement, ' + \
        COL_DATE + ' text not null, ' + \
        COL_TOTAL + ' real);'

    def __init__(self, db):
        self.db = db

    def getDate(self, billId):
        return self.db.select(TAB_BILLS,
                self.COL_DATE, (self.COL_ID,), (billId,))[billId]

    def getTotal(self, billId):
        return self.db.select(TAB_BILLS,
                self.COL_TOTAL, (self.COL_ID,), (billId,))[billId]

class DishIngredients:
    COL_QTY     = "Quantity"

    CREATE_TABLE = 'create table ' + TAB_DISH_INGREDIENTS + ' (' + \
        Dishes.COL_ID + ' integer not null references ' \
        + TAB_DISHES + '(' + Dishes.COL_ID + '), ' + \
        Ingredients.COL_ID + ' integer not null references ' \
        + TAB_INGREDIENTS + '(' + Ingredients.COL_ID + '), ' + \
        COL_QTY + ' integer not null, ' + \
        'primary key (' + Dishes.COL_ID + ',' + Ingredients.COL_ID + '));' 

    def __init__(self, db):
        self.db = db

    def getIngredientIds(self, dishId): 
        return self.db.select(TAB_DISH_INGREDIENTS,
                Ingredients.COL_ID, (Dishes.COL_ID,), (dishId,))[dishId]

    def getQuantity(self, dishId, ingId):
        return self.db.select(TAB_DISH_INGREDIENTS, self.COL_QTY,
                (Dishes.COL_ID, Ingredients.COL_ID), (dishId, ingId))[dishId]

    def addDishIngredient(self, dishId, ingId, ingQty):
        self.db.insert(TAB_DISH_INGREDIENTS, (dishId, ingId, ingQty))

    def deleteDishIngredients(self, dishId):
        self.db.delete(TAB_DISH_INGREDIENTS, Dishes.COL_ID, dishId)

class BillDishes:
    COL_QTY     = "Quantity"

    CREATE_TABLE = 'create table ' + TAB_BILL_DISHES + ' (' + \
        Bills.COL_ID + ' integer not null references ' \
        + TAB_BILLS + '(' + Bills.COL_ID + '), ' + \
        Dishes.COL_ID + ' integer not null references ' \
        + TAB_DISHES + '(' + Dishes.COL_ID + '), ' + \
        COL_QTY + ' integer not null, ' + \
        'primary key (' + Bills.COL_ID + ',' + Dishes.COL_ID + '));' 

    def __init__(self, db):
        self.db = db

    def getDishIds(self, billId):
        return self.db.select(TAB_BILL_DISHES,
                Dishes.COL_ID, (Bills.COL_ID,), (billId,))[billId]

    def getQuantity(self, billId, dishId):
        return self.db.select(TAB_BILL_DISHES, self.COL_QTY,
                (Bills.COL_ID, Dishes.COL_ID), (billId, dishId))[billId]

class PersistentData:
    COL_ID          = "DataID"
    COL_KEY         = "DataName"
    COL_VAL         = "DataVal"
    KEY_CASH        = "Cash"
    KEY_THRESHOLD   = "IngredientThreshold"

    CREATE_TABLE = 'create table ' + TAB_PERSISTENT_DATA + ' (' + \
        COL_ID + ' integer primary key autoincrement, ' + \
        COL_KEY + ' text not null, ' + \
        COL_VAL + ' text not null);'

    def __init__(self, db):
        self.db = db

    def getValue(self, key):
        return self.db.select(TAB_PERSISTENT_DATA,
                self.COL_VAL, (self.COL_KEY,), (key,))[key]

    def setValue(self, key, value):
        self.db.update(TAB_PERSISTENT_DATA, self.COL_VAL, value, self.COL_KEY, key)
        
    def insertKey(self, key, value):
        self.db.insert(TAB_PERSISTENT_DATA, (COL_AUTO, key, value))

class Database:
    TAB_CREATE_DICT = {
        TAB_INGREDIENTS: Ingredients.CREATE_TABLE,
        TAB_DISH_INGREDIENTS: DishIngredients.CREATE_TABLE,
        TAB_DISHES: Dishes.CREATE_TABLE,
        TAB_BILL_DISHES: BillDishes.CREATE_TABLE,
        TAB_BILLS: Bills.CREATE_TABLE,
        TAB_PERSISTENT_DATA: PersistentData.CREATE_TABLE
    }

    __instance = "placeholder"

    @staticmethod
    def getInstance():
        if Database.__instance == "placeholder":
            Database()
        return Database.__instance

    def __init__(self):
        if Database.__instance != "placeholder":
            raise Exception("class Database is a singleton class!")
        else:
            self.db = SQLiteDBHelper(DB_NAME, self.TAB_CREATE_DICT)
            self.ingredients = Ingredients(self.db)
            self.dishIngredients = DishIngredients(self.db)
            self.dishes = Dishes(self.db)
            self.billDishes = BillDishes(self.db)
            self.bills = Bills(self.db)
            self.persistentData = PersistentData(self.db)
            Database.__instance = self
