#Andy Szeto
#9-2-2019
#Car Inventory Info storage project, practicing classes

import datetime, shelve, re, csv

#car class
class carInv:

    def __init__(self, inVmodelNo, mileage,
                 year, make, model,
                 vehID, condition, color, titleStatus, price,
                 transType, engType, driveType, intColor):  # constructor

        self._mileage = mileage  # instance variables
        self._year = year
        self._make = make
        self._model = model
        self._titleStat = titleStatus
        self._price = price
        self._inventoryID = inVmodelNo
        self._color = color
        self._VIN = vehID
        self._transMi = transType
        self._engine = engType
        self._drive = driveType
        self._intColor = intColor
        self._cond = condition


    def __mul__(self, price):
        grandTot = (self._price * 1.10) + 600
        return '$ ' + str(round(grandTot, 2))

    def carColor(self, color):
        return self._color

    def intColor(self, intColor):
        return self._intColor.upper()

    def condition(self, condition):
        return self._cond.upper()

    def vehicleID(self, vehID):
        return self._VIN.upper()

    def MakeModel(self, year, make, model):
        return self._year + ' ' + self._make.upper() + ' ' + self._model.upper()

    def idNumber(self, inVmodelNo):
        return 'Inv SER.No: ' + self._inventoryID.upper()

    def mileage(self, mileage):
        return self._mileage

    def titleStatus(self, titleStatus):
        if titleStatus == 'clean':
            return 'Clean. No major accidents'
        if titleStatus == 'rebuilt':
            accDet = input('Input details of prior accidents and rebuilt work done: ')
            return 'Accident History, Rebuilt, Det: ' + accDet
        if titleStatus == 'salvage':
            accDet = input('Input details of prior major accidents: ')
            return 'Major work required, Det: ' + accDet

    def transType(self, type):
        if type == 'manual':
            speed = str(input('How many speeds on manual? '))
            return speed + ' speed manual'.upper()
        else:
            return self._transMi.upper()

    def engine_Type(self, engType):
        return self._engine.upper()

    def drive_Type(self, driveType):
        return self._drive.upper()


#MAIN MENU
def mainMenu():
    print('WELCOME TO THE MAIN MENU\n-----------------')
    print('$$$ ________ $$$')
    print(' _ / /_| [_]\___.*.')
    print('|______|________|o|')
    print('  ( o )   ( o ) \n')
    print('[A] SEARCH INVENTORY\n[B] ADD INV ITEM')
    print('[C] DELETE INV ITEM\n[D] CUSTOMER FINANCE OPTIONS')
    print('[E] EXIT')

    userChoice = str(input('What would you like to do? '))

    if userChoice.upper() == 'A':
        noEnter = str(input('Enter Inventory Serial Number: ')).upper()
        readDet = open('/Users/neptune/Desktop/CarInventory.csv', 'r')
        csvRdr = csv.reader(readDet)
        outData = list(csvRdr)
        OCC = 0

        #NEEDS WORK ON THE ELSE STATEMENT
        for row in outData:
            OCC += 1
            if noEnter in row[0]:
                print('Details for: ' + str(noEnter) + '' + str(row))

            elif noEnter not in row[0] and OCC > 1:
                print(str(noEnter) + ' is not in the inventory\n')
                break


    elif userChoice.upper() == 'B':
        return True

    elif userChoice.upper() == 'C':
        return True

    elif userChoice.upper() == 'D':
        def finance_options(rate):
            term = int(input('How long of a term is the customer looking for? (months) '))
            vehPrice = int(input('What is the price of the vehicle?: $'))
            cost = (vehPrice * 1.1) + 600
            downPMT = int(input("What is the customer's desired down payment?: $ "))
            principal = cost - downPMT

            mo_pmt = principal * ((rate * ((1 + rate) ** term)) / (((1 + rate) ** term) - 1))
            tot_int_paid = round(((mo_pmt * term) + downPMT), 2) - cost

            print('With APR of ' + str(round(rate * 1200, 2)) + '%, the total cost is: $' + str(
                round(mo_pmt, 2)) + ' per month')
            print('The total cost over the entire term is: $' + str(round(((mo_pmt * term) + downPMT), 2)))
            print('The total interest paid is: $' + str(round(tot_int_paid, 2)))

        creditScore = int(input("What is the customer's credit score? "))
        if creditScore < 500:
            print('financing is not available, credit score inadequate')

        if creditScore >= 500 and creditScore <= 589:
            apr = 0.14 / 12
            finance_options(apr)

        if creditScore >= 590 and creditScore <= 619:
            apr = .13 / 12
            finance_options(apr)

        if creditScore >= 620 and creditScore <= 659:
            apr = .095 / 12
            finance_options(apr)

        if creditScore >= 660 and creditScore <= 689:
            apr = .07 / 12
            finance_options(apr)

        if creditScore >= 690 and creditScore <= 719:
            apr = .045 / 12
            finance_options(apr)

        if creditScore >= 720 and creditScore <= 850:
            apr = .033 / 12
            finance_options(apr)


    elif userChoice.upper() == 'E':
        print('Goodbye')
        exit()


print('Hello, welcome to the car inventory program!')
print('$$$ ________ $$$')
print(' _ / /_| [_]\___.*.' )
print('|______|________|o|')
print('  ( o )   ( o ) ')
print('')

inventory = {}

#Asks user for vehicle details
while True:
    addCar = input("Would you like to add a(nother) car? Enter: 'yes' or 'no'? ")
    if addCar.lower() == 'yes':
        invNum = str(input('Enter the inventory serial number: ')).upper()
        veh_ID = str(input('What is the VID? ')).upper()
        mk = input('What is the make? ')
        mdl = input('What model is it? ')
        yr = input('What year is it? ')
        cdtn = input('Is the car new or used? ')
        colr = input('What is the color of the car? ').upper()
        inColr = str(input('What is the interior color? '))
        miles = input('What is the mileage? ')
        ttlS = input('What is the title status? ')
        cst = int(input('What is the price?: $'))
        trans = str(input('What is the transmission type? (AUTO/MANUAL) '))
        engT = str(input('What is the engine type? (GAS/DIESEL/ELECTRIC/HYBRID) '))
        driT = str(input('What is the drive type? '))


        carEntry = carInv(invNum, miles, yr, mk, mdl, veh_ID, cdtn, colr,
                          ttlS, cst, trans, engT, driT, inColr)

        inventory.update({carEntry.idNumber(invNum): [carEntry.MakeModel(mk, mdl, yr),
                                                      carEntry.vehicleID(veh_ID),
                                                      carEntry.condition(cdtn),
                                                      carEntry.carColor(colr),
                                                      carEntry.intColor(inColr),
                                                      carEntry.titleStatus(ttlS),
                                                      carEntry.transType(trans),
                                                      carEntry.engine_Type(engT),
                                                      carEntry.drive_Type(driT),
                                                      carEntry.mileage(miles),
                                                      carEntry.__mul__(cst)]})

        continue

    if addCar.lower() == 'no':
        # for i in inventory:
        #     print(i,':', inventory[i])
        #     print('')
        # mainMenu()
        break


#Bottom section designed to write all the details into a csv file
outputDet = open('/Users/neptune/Desktop/CarInventory.csv','a')
outDetWrit = csv.writer(outputDet)

carList = []
for k, v in inventory.items():
    currentDT2 = datetime.datetime.now()
    carList.append(k)
    for items in v:
        carList.append(items)
    carList.append(str(currentDT2))
outDetWrit.writerow(carList)

outputDet.close()






