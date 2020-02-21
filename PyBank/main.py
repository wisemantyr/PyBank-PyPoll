#PYBANK
#Your task is to create a Python script that analyzes the records to calculate each of the following:
'''open csv file
create csv reader
skip the header
define variables
'''
import os
import csv
Months = []
Profits = []
ProfitLosses = []
profit = 0

PyBankCSVpath = os.path.join('Resources', 'budget_data.csv')
with open (PyBankCSVpath, newline='') as PyBankCSV:
    PyBank_csvreader = csv.reader(PyBankCSV, delimiter = ',')
    PyBank_header = next(PyBank_csvreader)
    #The total number of months included in the dataset
    '''
    append empty list with months
    calculate len of list and print outside of loop
    '''
    for row in PyBank_csvreader:
        Months.append(row[0])
            
        #The net total amount of "Profit/Losses" over the entire period
        '''
        create a list
        fill it with index (1) of every row
        sum the list
        '''
        ProfitLosses.append(int(row[1]))

        profit = int(profit) + int(row[1])
        Profits.append(int(profit))
        profit = int((row-1)[1])


        
#The average of the changes in "Profit/Losses" over the entire period
'''
sum each item in the index(1) list with the item after it
put in a new list
calculate the average
'''
TotalMonths = int(len(Months))
TotalProfitLosses = int(sum(ProfitLosses))
AverageProfitLosses = int(sum(Profits)/(len(Profits)))
#The greatest increase in profits (date and amount) over the entire period
'''
find the largest number in above list
find what row it is
grab index(0) and index (1)
'''
GreatestIncrease = int(max(Profits))
GreatestIncreaseIndex = Profits.index(GreatestIncrease)
print (GreatestIncrease)
        
     
#The greatest decrease in losses (date and amount) over the entire period
'''
find the smallest number in above list
find what row it is
grab index(0) and index (1)
'''
GreatestDecrease = int(min(Profits))
GreatestDecreaseIndex = Profits.index(GreatestDecrease)
print (GreatestDecrease)

CombinedList = list(zip(Months, Profits))

print("Total Months: " + str(TotalMonths))
print("Total: " + str(TotalProfitLosses))
print("Average Change: " + str(AverageProfitLosses))
print("Greatest Increase in Profits: " + str(CombinedList[GreatestIncreaseIndex]))
print("Greatest Decrease in Profits: " + str(CombinedList[GreatestDecreaseIndex]))        
#In addition, your final script should both print the analysis to the terminal 
#and export a text file with the results




