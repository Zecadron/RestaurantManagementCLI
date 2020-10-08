class Ingredients:
    def getStock(self, ingId):
        pass
    def getAverage(self, ingId):
        pass
    def getPrice(self, ingId):
        pass
    def getIngredientName(self, ingId):
        pass

class DishIngredients:
    def getIngredientIds(self, dishId): #Gives list with all ingId associated with dishId
        return []
    def getQuantity(self, dishId, ingId):
        pass

class Dishes:
    def getDishName(self, dishId):
        pass
    def getPrice(self, dishId):
        pass

class BillDishes:
    def getDishIds(self, billId): #Gives a list with all dishId associated with billId
        pass
    def getQuantity(self, billId, dishId):
        pass

class Bill:
    def getDate(self, billId):
        pass
    def getTotal(self, billId):
        pass
