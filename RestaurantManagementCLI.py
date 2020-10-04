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
    while(foodId != -1):
        foodId     = input()
        foodAmount = input()

        if(foodId == 0):    # Write into daily consumption data
            writeDailyData(totalConsumed)    # adds a row containing the consumption data
            totalConsumed = 0
            prevData = loadPrevData()

        availIngredients = 1
        consumedIngredients = fetchRequiredIngredients(foodId) * foodAmount
        ingredientsList = ingredientsList - consumedIngredients
        totalConsumed = totalConsumed + consumedIngredients

        ### Insufficient Ingredients
        for x in ingredientsList:
            if(x<0):
                print("Insufficient ingredients\n")
                availIngredients = 0
                ingredientsList = ingredientsList + consumedIngredients
        ###

        if(availIngredients == 1):
            generateBill(foodId,foodAmount,prices)
            orderIngredients = isBelowThreshold(ingredientsList)
            sendOrder(orderIngredients,prevData,prices)


if __name__ == "__main__":
    main()
