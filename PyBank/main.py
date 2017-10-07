#Dependencies
import os
import csv


#import CSV files.
# Choose file one or two.
file_num = 2

#Create file path and save as file

budget_data_csv = os.path.join('Resources','budget_data_' + str(file_num) + '.csv')



#Empty Lists to store data.
total_months = []
total_revenue = []
average_revenue_change = []
greatest_increase_revenue = []
greatest_decrease_revenue = []

with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#total months
numMonths = 0
#Add months to counter
numMonths += 1
#Loop through csv file.
for row in csvreader:  
   #The total number of months included in the dataset.
       total_months.append(numMonths)
       print(numMonths) 
    
   #The total amount of revenue gained over the entire period.
       revenue = sum(int(row[1]))
       total_revenue.append(revenue)
       print(revenue)       
    
    #The average change in revenue between months over the entire period
       average = revenue/numMonths
       average_revenue_change.append(average)
       print(average)

    #The greatest increase in revenue (date and amount) over the entire period
revenue_list = []
numRevenue = 0
numRevenue += 1
for row in csvreader:
    revenue_list.append(numRevenue)
    max(revenue_list)
    greatest_increase_revenue.append(max(revenue_list))
    print(max(revenue_list))       
    #The greatest decrease in revenue (date and amount) over the entire period
    min(revenue_list)   
    greatest_decrease_revenue.append(min(revenue_list))
    print(min(revenue_list))       

#Zip lists together
pyBank_txt = zip(total_months, total_revenue, average_revenue_change, greatest_increase_revenue, greatest_decrease_revenue)

#Set variable for the output file.
output_file = os.path.join(PyBank.txt)
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_file, 'w', newline='') as datafile:
    writer = txt.writer(datfile)






