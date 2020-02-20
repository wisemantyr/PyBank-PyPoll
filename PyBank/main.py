#PYBANK
    #Your task is to create a Python script that analyzes the records to calculate each of the following:
    '''
    open csv file
    create csv reader
    skip the header
    define variables
    '''
    import os
    import csv
    Months = []
    ProfitLosses = []

    PyBankCSVpath = os.path.join('')
    with open (PyBankCSVpath, newline='') as PyBankCSV
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
            ProfitLosses.append(row[1])
    #The average of the changes in "Profit/Losses" over the entire period
    '''
    sum each item in the index(1) list with the item after it
    put in a new list
    calculate the average
    '''
        TotalMonths = len(Months)
        TotalProfitLosses = sum(ProfitLosses)
        AverageProfitLosses = TotalProfitLosses/(len(ProfitLosses))
    #The greatest increase in profits (date and amount) over the entire period
    '''
    find the largest number in above list
    find what row it is
    grab index(0) and index (1)
    '''
        GreatestIncrease = max(ProfitLosses)
        GreatestIncreaseIndex = ProfitLosses.index(GreatestIncrease)
        
     
    #The greatest decrease in losses (date and amount) over the entire period
    '''
    find the smallest number in above list
    find what row it is
    grab index(0) and index (1)
    '''
        GreatestDecrease = min(ProfitLosses)
        GreatestDecreaseIndex = ProfitLosses.index(GreatestDecrease)

        CombinedList = zip(Months, ProfitLosses)

        print("Total Months: " + TotalMonths)
        print("Total: " + TotalProfitLosses)
        print("Average Change: " + AverageProfitLosses)
        print("Greatest Increase in Profits: " + CombinedList[GreatestDecreaseIndex])
        print("Greatest Decrease in Profits: " + CombinedList[GreatestIncreaseIndex])        
    #In addition, your final script should both print the analysis to the terminal 
    #and export a text file with the results




