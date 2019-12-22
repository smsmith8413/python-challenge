#bring in csv file
import os
import csv

from collections import Counter
#read csv file
budget_csv = os.path.join('python-challenge','PyBank','Resources','budget_data.csv')
#wrestling_csv = os.path.join('..', 'Resources', 'WWE-Data-2016.csv')

# Define the function and have it accept the 'wrestler_data' as its sole parameter
def totalNet(budget_data):
    # For readability, it can help to assign your values to variables with descriptive names
    dateCol = str(budget_data[0])
    amountCol = int(budget_data[1])
print(totalNet())
