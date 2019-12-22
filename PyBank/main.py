# import CSV
import os
import csv

#set patch to csv with relative ref
budgetCsv = os.path.join('PyBank','Resources','budget_data.csv')

# open csv as csvfile
with open(budgetCsv, 'r', newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    newBudget = csv.reader(csvfile, delimiter=',')
    csv_header = next(newBudget)

# declare variables (iterators)
    totalMonths = []
    netPL = []
    monthlyChange = []
    avgChange = []

#loop through data in csv, appending along the way to be able to get # months and net P&L
    for row in newBudget:
        totalMonths.append(row[0])
        netPL.append(float(row[1]))

#loop through second 'column', calculating changes between rows and min/max values 
    for i in range(1,len(netPL)):
        monthlyChange.append(netPL[i] - netPL[i-1])
        avgChange = sum(monthlyChange)/len(monthlyChange)
        maxChangeDate = str(totalMonths[monthlyChange.index(max(monthlyChange))+1])
        minChangeDate = str(totalMonths[monthlyChange.index(min(monthlyChange))+1])
        maxChange = max(monthlyChange)
        minChange = min(monthlyChange)

#print results
    print("Financial Analysis")
    print("--------------------")
    print("Total Months: ",len(totalMonths))
    print("Total: $", round(sum(netPL)))
    print("Average change: $",round(avgChange, 2))
    print("Greatest increase in Profits: ",maxChangeDate, "($",round(maxChange),")")
    print("Greatest decrease in Profits: ",minChangeDate,"($",round(minChange),")")


