import csv

total = 0
with open('budget_data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
    for row in spamreader:
       total += int(row[1])

