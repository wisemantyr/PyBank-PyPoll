'''
#PYPOLL
#Your task is to create a Python script that analyzes the votes and calculates each of the following:
'''
#import modules
import os
import csv

#define file path
pypoll_csvpath = os.path.join("..","..","..", "UR-RICH-DATA-PT-01-2020-U-C","03-Python","HW",
"Instructions","PyPoll","Resources", "election_data.csv")

#create empty lists and dictionaries
AllVotes = []
AllCandidates = []
CandidateVotes = {}
CandidatePercentages = {}

#open csv, create reader, skip header
with open(pypoll_csvpath, newline="") as PyPollCsv:
    pypoll_csvreader = csv.reader(PyPollCsv, delimiter=",")
    pypoll_header = next(pypoll_csvreader)
    '''
    The total number of votes cast
    '''
    #search file
    for row in pypoll_csvreader:
        #append lists
        AllVotes.append(int(row[0]))
        AllCandidates.append(row[2])
        
    #sum the votes
    TotalVotes = sum(AllVotes)
    print(TotalVotes)
    
    '''
    #A complete list of candidates who received votes
    '''

    #create list of unique candidates
    UniqueCandidates = list(set(AllCandidates))
    print(UniqueCandidates)

    '''
    #The percentage of votes each candidate won
    '''
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
                CandidateVotes[candidate].append(int(index[0]))
 
    '''
    #The total number of votes each candidate won
    '''

    '''
    #The winner of the election based on popular vote.
    '''
    
    '''
    In addition, your final script should both print the analysis to the terminal and export a text file with the results.
    '''