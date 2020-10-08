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

    def getStock(self, ingId):
        pass
    def getAverage(self, ingId):
        pass
    def getPrice(self, ingId):
        pass
    def getIngredientName(self, ingId):
        pass

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

    def getDishName(self, dishId):
        pass
    def getPrice(self, dishId):
        pass

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
        pass
    def getTotal(self, billId):
        pass

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

    def getIngredientIds(self, dishId): #Gives list with all ingId associated with dishId
        return []
    def getQuantity(self, dishId, ingId):
        pass

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

    def getDishIds(self, billId): #Gives a list with all dishId associated with billId
        pass
    def getQuantity(self, billId, dishId):
        pass

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
        pass
    def setValue(self, key):
        pass
    def insertKey(self, key, value):
        pass

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
