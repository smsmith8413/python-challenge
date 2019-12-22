#bring in csv file
import os
import csv

from collections import Counter
#read csv file
budget_csv = os.path.join('python-challenge','PyBank','Resources','budget_data.csv')
#open csv and specify delimiter
#with open(budget_csv, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
#    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    # Loop through looking for the video
    # Read each row of data after the header
    ##data = list(csvreader)
    ##date_count = len(data)
    ##print(date_count) 
#    dateCount = len(row[0])
#    print(dateCount)
# Test your function with the following:
#print(length)
#with open(udemy_csv, newline="") as csvfile:
##csvreader = csv.reader(csvfile, delimiter=",")
#def netPL
#for row in csvreader:
    # Determine percent of review left to 2 decimal places
#    netPL = sum(float(row[2])
with open(budget_csv) as csvfile:
    csvfile.next()
    total = sum(int(r[1]) for r in csv.reader(csvfile))