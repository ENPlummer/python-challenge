#Dependencies
import os
import csv


#import CSV files.
# Choose file one or two.
file_num = 2

#Create file path and save as file

csvpath = os.path.join('Resources','budget_data_' + str(file_num) + '.csv')



#Empty Lists to store data.
total_months = []
total_revenue = []
average_revenue_change = []
greatest_revenue_increase = []
greatest_revenue_decrease = []

with open(csvpath, newline="") as csvfile
    csvreader = csv.reader(csvfile, delimiter=",")
   #Loop through csv file.
   for row in csv reader:  
   #The total number of months included in the dataset.
   #total months
   numMonths = 0
       #Add months to counter
       numMonths += 1
       #Add to list.
       total_months.append(numMonths)
   print(date)

    
   #The total amount of revenue gained over the entire period.
   revenue = 0
       #Add revenue to counter
       revenue += 1
   #Add to list.
   total_revenue.append(revenue)
    

    #The average change in revenue between months over the entire period
        average = revenue/numMonths

    #The greatest increase in revenue (date and amount) over the entire period
        increase = max(row[1])

    #The greatest decrease in revenue (date and amount) over the entire period
        decrease = min(row[2])   
               
        

#Open and read CSV file budget_data_2.
#with open(budget_data_2CSV, 'r') as csvfile:
    #csvreader = csv.reader(csvfile, delimiter='')
        #csvreader = csv.reader(csvfile, delimiter='')
    #Loop through the data
    #for row in csvreader:
        #if row == row[0] 
            #pybankData(row)






