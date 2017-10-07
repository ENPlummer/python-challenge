#Dependencies
 import os
 import csv
 import datetime

 #Tmport CSV files. 
 #choose one or two.
 file_num = 2
#Create file path and save as file.
file = os.path.join('raw_data', 'employee_data' + str(file_num) + '.csv')

#Lists to store data.
empID = []
first_name = []
last_name = []
date_of_birth = []
ssNumber = []
state = []
#Open and read csv files.

with open(employee_data, newline="") as csvfile
    csvreader = csvreader(csvfile, delimiter=",")
    for row in csvreader

    #Add employee ID
    empID.append(row[0])
    #Split first and last name.
    row[1] = s.split(" ")

    #Change DOB format.
    row([2]).strftime("%d-%m-%y")

    #Mask first five numbers of SS Number format.

    #Change state formation. Two letter abbreivation