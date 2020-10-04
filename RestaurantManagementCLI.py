from DataIO import *
from Orders import *

def main():
    ingredientsList = loadIngredients()
    foodMenu        = loadFoodMenu()
    prices          = loadPrices()
    prevData        = loadPrevData()    # ingredients sold in the past 3 days

    ### Add Admin Login here to change prices

    ###

    print("Enter -1 to stop, foodId and foodAmount to continue, enter 0 and 0 to end day and save data")

    foodId        = 0
    totalConsumed = 0

    while(True):
        foodId = int(input())
        if(foodId == -1):
            break
        foodAmount = int(input())

        if(foodId == 0):    # Write into daily consumption data
            writeDailyData(totalConsumed,prevData)    # adds a row containing the consumption data
            totalConsumed = 0
            prevData = loadPrevData()

        availIngredients = 1
        consumedIngredients = fetchRequiredIngredients(foodId,foodMenu) * foodAmount
        ingredientsList = ingredientsList - consumedIngredients
        totalConsumed = totalConsumed + consumedIngredients

        ### Insufficient Ingredients
        for x in ingredientsList:
            if(x<0):
                print("Insufficient ingredients\n")
                availIngredients = 0
                ingredientsList = ingredientsList + consumedIngredients
        ###

        if(availIngredients == 1 and foodId != 0):
            updateIngredients(ingredientsList)
            generateBill(foodId,foodAmount,prices)
            orderIngredients = isBelowThreshold(ingredientsList)
            sendOrder(orderIngredients,prevData,prices)


if __name__ == "__main__":
    main()
