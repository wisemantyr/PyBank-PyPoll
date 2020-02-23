#define variables
Months = []
Profits = []
ProfitChanges = []
    
#create csv path string
import os
import csv
pybank_csvpath = os.path.join("Resources", "budget_data.csv")

#open CSV, create reader object, skip header

with open (pybank_csvpath, newline="") as PyBankCsv:
    pybank_csvreader = csv.reader(PyBankCsv, delimiter = ",")
    pybank_header = next(pybank_csvreader)
    
    for row in pybank_csvreader:
        #fill list with months
        Months.append(row[0])
                
      
        #fill list with profits
        Profits.append(int(row[1]))
                
    TotalMonths = len(Months)
    TotalProfit = sum(Profits)
    
    #create tuple pairs of each number in profits and the number after it
    #subtract first value from second value to calculate change
    #fill list with values
    ProfitChanges = [second - first for first,second in zip(Profits, Profits[1:])]


    #calculate average of list
    TotalChange = sum(ProfitChanges)
    AverageChange = round((TotalChange/(len(ProfitChanges))), 2)
    
    #add value to beginning of list for accurate indexes
    ProfitChanges.insert(0,0)
    str("${:,.2f}".format(*ProfitChanges))
    
    #find the largest number in change list and its index
    GreatestIncrease = max(ProfitChanges)
    GreatestIncreaseIndex = ProfitChanges.index(GreatestIncrease)       
        
    #find the smallest number in change list and its index
    GreatestDecrease = min(ProfitChanges)
    GreatestDecreaseIndex = ProfitChanges.index(GreatestDecrease)

    #create list filled with tuples of months and changes formtted as dollars
    CombinedList = list(zip(Months, ProfitChanges))

    #save results as lines
    Line1 = "Total Months: " + str(TotalMonths)
    Line2 = "Total: $" + str(TotalProfit)
    Line3 = "Average Change: $" + str(AverageChange)
    Line4 = "Greatest Increase in Profits: " + str(CombinedList[GreatestIncreaseIndex])
    Line5 = "Greatest Decrease in Profits: " + str(CombinedList[GreatestDecreaseIndex])

    #print results
    print(Line1)
    print(Line2)
    print(Line3)
    print(Line4)
    print(Line5)        
    
    #export results to text file
    output = os.path.join("results.txt")
    with open(output, "w", newline="") as resultsfile:
        resultsfile.writelines([Line1+"\n", Line2+"\n", Line3+"\n", Line4+"\n", Line5])
    
