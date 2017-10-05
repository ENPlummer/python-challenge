#Dependencies
import os
import csv
import statistics

#import CSV files

budget_data_1CSV = os.path.join('Resources','budget_data_1.csv')
budget_data_2CSV = os.path.join('Resources','budget_data_2.csv')


#Create out put file name.
file_output_pybank = "pybank_data.csv"

#Lists to store data.
total_months = []
total_revenue = []
average_revenue_change = []
greatest_revenue_increase = []
greatest_revenue_decrease = []


def pybankData(budget_data_1,budget_data_2):
    

    #The total number of months included in the dataset.
    total_months.append(row[0])

    #The total amount of revenue gained over the entire period.
    total_revenue.append(row[1])

    The average change in revenue between months over the entire period
    mean(average_revenue_change).append(row[1])

    #The greatest increase in revenue (date and amount) over the entire period
    max(greatest_revenue_increase).append(rows[0],[1])

    #The greatest decrease in revenue (date and amount) over the entire period
    min(greatest_revenue_decrease).append(row[0],[1])

#Open and read CSV file budget_data_1.
with open(budget_data_1CSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter='')
    #Loop through the data
    for row in csvreader:
        if row == row[0] or row ==[1]
            pybankData(row)

#Open and read CSV file budget_data_2.
with open(budget_data_2CSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter='')
        csvreader = csv.reader(csvfile, delimiter='')
    #Loop through the data
    for row in csvreader:
        if row == row[0] or row ==[1]
            pybankData(row)






