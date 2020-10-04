import numpy as np
import csv

def loadIngredients():
    data = np.genfromtxt("ingredients.csv", delimiter=",")
    return data[:,1]

def updateIngredients(ingredientsList):
    print("#0") #dummy text

def loadFoodMenu():
    data = np.genfromtxt("foodmenu.csv", delimiter=",", skip_header=1)
    return data

def loadPrices():
    data = np.genfromtxt("prices.csv", delimiter=",")
    return data[:,1]

def loadPrevData():
    data = np.genfromtxt("dailydata.csv", delimiter=",", skip_header=1)
    return data[-3:,:]

def fetchRequiredIngredients(foodId,foodMenu):
    data = foodMenu[foodId-1,1:]
    return data

def writeDailyData(totalConsumed,prevData):
    currentDate   = prevData[-1,0] + 1
    totalConsumed = np.append(currentDate,totalConsumed)
    with open("dailydata.csv",'a') as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(totalConsumed)
