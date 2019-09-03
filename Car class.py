#Andy Szeto
#9-2-2019
#Car Inventory Info storage project, practicing classes

import datetime
import shelve

class carInv:

    def __init__(self, mileage, year, make, model, titleStatus, price, inVmodelNo):  # constructor

        self._mileage = mileage  # instance variables
        self._year = year
        self._make = make
        self._model = model
        self._titleStat = titleStatus
        self._price = price
        self._inventoryID = inVmodelNo

    def __mul__(self, price):
        grandTot = self._price * 1.10
        return 'Price + Tx: ' + str(round(grandTot, 2))

    def MakeModel(self, year, make, model):
        return self._year + ' ' + self._make.upper() + ' ' + self._model.upper()

    def idNumber(self, inVmodelNo):
        return 'SER.No: ' + self._inventoryID.upper()

    def mileage(self, mileage):
        return self._mileage

    def titleStatus(self, titleStatus):
        if titleStatus == 'clean':
            return 'No major accidents'
        if titleStatus == 'rebuilt':
            return 'Accident History, Rebuilt'
        if titleStatus == 'salvage':
            return 'Major work required'

def mainMenu(): #NEEDS WORK
    print('WELCOME TO THE MAIN MENU\n-----------------\n[A] SEARCH INVENTORY\n[B] ADD INV ITEM')
    print('[C] DELETE INV ITEM\n[D] EXIT')
    userChoice = str(input('What would you like to do? '))
    if userChoice.upper() == 'A':
        noEnter = print(input('Enter Inventory Serial Number '))
        carSearch = open('/Users/neptune/desktop/carInventory.txt', 'r')
        if noEnter in carSearch:
            print('We have that vehicle')
        carSearch.close()
        #print(inventory[noEnter])
    elif userChoice.upper() == 'B':
        return True
    elif userChoice.upper() == 'C':
        return True
    elif userChoice.upper() == 'D':
        print('Goodbye')
        exit()



print('Hello, welcome to the car inventory program!')
print('')
inventory = {}

while True:
    addCar = input("Would you like to add a(nother) car? Enter: 'yes' or 'no'? ")
    if addCar.lower() == 'yes':
        invNum = str(input('Enter the inventory serial number: '))
        mk = input('What is the make? ')
        mdl = input('What model is it? ')
        yr = input('What year is it? ')
        mils = input('What is the mileage? ')
        ttlS = input('What is the title status? ')
        cst = int(input('What is the price? '))

        carEntry = carInv(mils, yr, mk, mdl, ttlS, cst, invNum)

        inventory.update({carEntry.idNumber(invNum): [carEntry.MakeModel(mk, mdl, yr),
                                                      carEntry.titleStatus(ttlS),
                                                      carEntry.mileage(mils),
                                                      carEntry.__mul__(cst)]})

        continue

    if addCar.lower() == 'no':
        for i in inventory:
            print(i,':', inventory[i])
            print('')
        mainMenu()
        break

inv2 = str(inventory)
currentDT = datetime.datetime.now() #entry timestamp
carFile = open('/Users/neptune/desktop/carInventory.txt', 'a') #writing entry to plaintxt file
carFile.write('\n***Added:' + str(currentDT) + ': ' + inv2)
carFile.close()

## SHELVING: NEEDS WORK
# carDB = shelve.open('/Users/neptune/desktop/CARDatabase.db')
# carDB['cars'] = inventory
# carDB.close()
#
# carDB = shelve.open('/Users/neptune/desktop/CARDatabase.db')
# print(carDB['cars'])
# carDB.close()
