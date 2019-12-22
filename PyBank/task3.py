import os
import csv
    #print(csvreader)
    # Read the header row first (skip this step if there is now header)
   # csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    # Read each row of data after the header

budgetCsv = os.path.join('PyBank','Resources','budget_data.csv')

with open(budgetCsv, 'r', newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    newBudget = csv.reader(csvfile, delimiter=',')
    csv_header = next(newBudget)

    length = []
    total = 0
    average = total / length



    for row in newBudget:
        length.append(row[0])
        total += float(row[1])


            

    print(len(length))
    print(total)
    print(average)

