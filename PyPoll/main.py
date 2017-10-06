import os

import csv

#Import CSV file
csvpath =os.path.join('/Users/ebony/dev/Python/python-challenge/Pypoll','election_data_2.csv')

#List to store data.

#list to store votes
total_votes = []
candidates = []
percentage_vote = []
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
        
        #Print number of votes.
        total_votes.append(voterID)
        
#A complete list of candidates who received votes
    candidate = 0
    for row in csvreader:
        candidate += 1
    print(candidates)
#The total number of votes each candidate won
    #for row in csvreader:
        #if candidate in candidates == candidate + 1

#The percentage of votes each candidate won



#The winner of the election based on popular vote.

#Write data to file.

#Specify the file to write to.
output_file = open("election_data_final.txt", "w")

# Write the header row
    writer.writerow(["Total Votes","Candidates"])
    # Write in zipped rows
    writer.writerows(total_votes,candidates)



   

