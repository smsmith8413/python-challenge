# Modules
import os
import csv

# Set path for file
csvpath = os.path.join('python-challenge', 'PyBank', 'Resources', 'budget_data.csv')


# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")



    def totalProfit():
    for row in csvreader:
        total = sum(int(r[1]) for r in csv.reader(csvfile))
        print(total)