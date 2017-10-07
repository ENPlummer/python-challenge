#Dependencies
import os
import csv
import datetime

#Tmport CSV files. 
#choose one or two.
file_num = 2
#Create file path and save as file.
employee_data_csv = os.path.join('raw_data', 'employee_data' + str(file_num) + '.csv')

#Lists to store data.
empID = []
first_name = []
last_name = []
date_of_birth = []
ssNumber = []
state_abbrev = []
#Open and read csv files.

with open(employee_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:

        #Add employee ID
        empID.append(row[0])
        print(empID)    

        #Split first and last name.
        name = row[1].split()row[0] 
        #takes name and splits on space in a list, then takes index 0 which is first name 
        first_name.append(name_list[0])
        last_name.append(name_list[1])
        print(first_name_str)

        #dates of birth.
        date_of_birth.append(row[2])


        #Mask first five numbers of SS Number format.
        str(row[3])[-4:].rjust(len(str(row[3])), "*")
    try:
       List of States
       us_state_abbrev = {
       'Alabama': 'AL',
       'Alaska': 'AK',
       'Arizona': 'AZ',
       'Arkansas': 'AR',
       'California': 'CA',
       'Colorado': 'CO',
       'Connecticut': 'CT',
       'Delaware': 'DE',
       'Florida': 'FL',
       'Georgia': 'GA',
       'Hawaii': 'HI',
       'Idaho': 'ID',
       'Illinois': 'IL',
       'Indiana': 'IN',
       'Iowa': 'IA',
       'Kansas': 'KS',
       'Kentucky': 'KY',
       'Louisiana': 'LA',
       'Maine': 'ME',
       'Maryland': 'MD',
       'Massachusetts': 'MA',
       'Michigan': 'MI',
       'Minnesota': 'MN',
       'Mississippi': 'MS',
       'Missouri': 'MO',
       'Montana': 'MT',
       'Nebraska': 'NE',
       'Nevada': 'NV',
       'New Hampshire': 'NH',
       'New Jersey': 'NJ',
       'New Mexico': 'NM',
       'New York': 'NY',
       'North Carolina': 'NC',
       'North Dakota': 'ND',
       'Ohio': 'OH',
       'Oklahoma': 'OK',
       'Oregon': 'OR',
       'Pennsylvania': 'PA',
       'Rhode Island': 'RI',
       'South Carolina': 'SC',
       'South Dakota': 'SD',
       'Tennessee': 'TN',
       'Texas': 'TX',
       'Utah': 'UT',
       'Vermont': 'VT',
       'Virginia': 'VA',
       'Washington': 'WA',
       'West Virginia': 'WV',
       'Wisconsin': 'WI',
      'Wyoming': 'WY',

    #Loop through U.S. State abbreviation dictionary to find the two letter abbreviation.
    for row in csvreader:
        if state in us_state_abbrev.value():
            state_abbrev.append(row[4])
        else:
            next row
     except SyntaxError:
        pass
      else:

#Zip lists together.
pyBoss_csv = zip(empID,first_name, last_name, date_of_birth, ssNumber, state_abbrev)

#write to csv file.
# Specify the file to write to
output_file = os.path.join("pyBoss.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)


    # Write the first row (column headers)
    writer.writerow(['Emp ID', 'First Name','Last Name', 'DOB','SSN','State'])

    #Write in row.
    writer.writerows(pyBoss_csv)