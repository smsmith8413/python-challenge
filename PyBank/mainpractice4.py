# Define the function and tell it to print "Hello!" when called
import csv

budgetCsv = os.path.join('PyBank','Resources','budget_data.csv')

def plData(rowInfo):

# Functions that take in and use parameters can also be defined

# -------------#
# The prime use case for functions is in being able to run the same code for different values
dateCount = str(rowInfo[0])
amount_pl = float(rowInfo[1])

    for row in newBudget:
        dates = list(newBudget)
        row_count = len(dates)

def listInformation(simpleList):
    print(f"The values within the list are...")
    for value in simpleList:
        print(value)
    print("The length of this list is... " + str(len(simpleList)))


listInformation(listOne)
listInformation(listTwo)


with open(budgetCsv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    newBudget = csv.reader(csvfile, delimiter=',')
    csv_header = next(newBudget)

