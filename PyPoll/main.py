#import modules
import os
import csv

#define file path
pypoll_csvpath = os.path.join("..","..","..", "UR-RICH-DATA-PT-01-2020-U-C","03-Python","HW",
"Instructions","PyPoll","Resources", "election_data.csv")

#create empty lists and dictionaries
TotalVotes = 0
AllCandidates = []
CandidateVotes = {}
CandidateTotals = {}

#open csv, create reader, skip header
with open(pypoll_csvpath, newline="") as PyPollCsv:
    pypoll_csvreader = csv.reader(PyPollCsv, delimiter=",")
    pypoll_header = next(pypoll_csvreader)
 
    #search file
    for row in pypoll_csvreader:
        #count votes
        TotalVotes = TotalVotes + 1
        #append list of each candidate mention
        AllCandidates.append(row[2])

    #create list of unique candidates
    UniqueCandidates = list(set(AllCandidates))

    #reset csvreader and skip header to search data again
    PyPollCsv.seek(0)
    next(pypoll_csvreader)
  
    #search data
    for index in pypoll_csvreader:
        #iterate through unique candidates
        for candidate in UniqueCandidates:
            #create a dictionary with each unique candidate as a key
            CandidateVotes.setdefault(candidate, [])
            #when unique candidate key is found in the data
            if index[2] == candidate:
                #append the associated value list with the votes
                CandidateVotes[candidate].append(index[0])
 
    #iterate through CandidateVotes dictionary
    for key, value in CandidateVotes.items():
        #fill dictionary with same keys as CandidateVotes dictionary
        CandidateTotals.setdefault(key, [])
        #add number of votes to value list
        CandidateTotals[key].append(len(value))
        #calculate percentage and format
        CandidatePercentage = ("{:.0%}".format((len(value))/TotalVotes))
        #add percentage to value list
        CandidateTotals[key].append(CandidatePercentage)

    #put Candidate Totals value pairs into list
    ListofTotals = (list(CandidateTotals.values()))
    #find highest value of list
    HighestTotal = max(ListofTotals)

    #loop through Candidate Totals dictionary values
    for candidate, totals in CandidateTotals.items():
        # if values match max
        if totals == HighestTotal:
            #then associated key is the winner
            Winner = candidate

    #assign strings to variables for export
    Line1="Election Results"
    Dashes="-----"
    Line2="Total Votes: " + str(TotalVotes)
    ListToPrint = []
    for x,y in CandidateTotals.items():
        line=(x + ": " + str(y[0]) + " (" +str(y[1]) + ")")
        ListToPrint.append(line)
    Line4="Winner: " + Winner
  
    #print results
    print(Line1)
    print(Dashes)
    print(Line2)
    print(Dashes)
    for line in ListToPrint:
        print(line)
    print(Dashes)
    print(Line4)
   
    #export results to text file
    output = os.path.join("results.txt")
    with open(output, "w", newline="") as resultsfile:
        resultsfile.writelines([Line1+"\n", Dashes+"\n", Line2+"\n", Dashes+"\n"])
        for item in ListToPrint:
            resultsfile.write(str(item) + "\n")
        resultsfile.writelines([Dashes+"\n", Line4])
    