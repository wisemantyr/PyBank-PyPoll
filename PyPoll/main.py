#PYPOLL
#Your task is to create a Python script that analyzes the votes and calculates each of the following:
'''
open csv file
create csv reader
skip the header
'''
import os
import csv
pypoll_csvpath = os.path.join("Resources", "election_data.csv")

AllVotes = []
AllCandidates = []
CandidateVotes = {}


with open(pypoll_csvpath, newline="") as PyPollCsv:
    pypoll_csvreader = csv.reader(PyPollCsv, delimiter=",")
    pypoll_header = next(pypoll_csvreader)
      
    #The total number of votes cast
    '''
    sum of index (0)
    '''
    for row in pypoll_csvreader:
        AllVotes.append(int(row[0]))
        AllCandidates.append(row[2])
        

    TotalVotes = sum(AllVotes)
    print(TotalVotes)
    UniqueCandidates = list(set(AllCandidates))
    print(UniqueCandidates)
    #A complete list of candidates who received votes
    '''
    list of index(2) unique values
    '''
    

    #The percentage of votes each candidate won
    #search data for candidate

        
    #find all corrosponding index (0) Values
    #sum them
    #create a dictionary of candidates and sums 
    #divide sum by the total votes cast
    #create another dictionary of candidates and percentages
    #format as a percent


    #The total number of votes each candidate won
    '''found above'''

    #The winner of the election based on popular vote.
    '''
    print candidate with highest number
    '''
    #In addition, your final script should both print the analysis to the terminal and export a text file with the results.