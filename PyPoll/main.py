import os

import csv

#Import CSV file
csvpath =os.path.join('/Users/ebony/dev/Python/python-challenge/Pypoll','election_data_2.csv')

#List to store data.

#list to store votes
total_votes = []
candidate_list = []
vote_percentage = []
candidate_votes = []
winner = []

#Open the CSV.

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Loop through rows
    #The total number of votes cast
    #vote counter
    voterID = 0
    for row in csvreader:

        voterID += 1
        
        #Add to voterID list.
        total_votes.append(voterID)
    len(total_votes)
    print(len(total_votes))   
        
#A complete list of candidates who received votes
    
    
    for row in csvreader:
        #Add candidate to candidate_list
        candidate_list.append(row[2])
        #Remove the duplicates
        candidates = []
        for candidate in candidate_list:
            if candidate not in candidates:
                candidates.append(candidate)
            print(candidates)    


#The total number of votes each candidate won
    #Correy
    correy = 0
    correy_total =[]
    for row in csvreader:
        #Vote count for Correy.
        correy += 1 
        #Add to Correy vote total.
        correy_total.append(correy)

     #Khan
     khan = 0
     khan_total =[]
     for row in csvreader:
        #Vote count for Khan.
        khan += 1 
        #Add to Khan vote total.
        khan_total.append(khan)

     #Li
     li = 0
     li_total =[]
     for row in csvreader:
        #Vote count for Li.
        li += 1 
        #Add to Li vote total.
        li_total.append(li)

     #O'Tooley
     otooley = 0
     otooley_total =[]
     for row in csvreader:
        #Vote count for Correy.
        otooley += 1 
        #Add to O'Tooley vote total.
        otooley_total.append(otooley)

#The percentage of votes each candidate won
#Correy vote percentage.
percentageC = correy/voterID
#Add to vote percentage list.
vote_percentage.append(percentageC)
#Khan vote percentage.
percentageK = khan/voterID
#Add to vote percentage list.
vote_percentage.append(percentageK)
#Li vote percentage.
percentageL = li/voterID
#Add to vote percentage list.
vote_percentage.append(percentageL)
#O'Tooley vote percentage
percentageO = otooley/voterID 


#The winner of the election based on popular vote.

totalVotes = {
  
}

#Write data to file.

#Specify the file to write to.
#output_file = open("election_data_final.txt", "w")

# Write the header row
    #writer.writerow(["Total Votes","Candidates"])
    # Write in zipped rows
    #writer.writerows(total_votes,candidates)



   

