# Import csv file
import csv
import os

# Read and open csv file
csvPath = os.path.join("..", "Resources", "budget_data.csv")

# Output results to txt file
outputFile = os.path.join("FinancialAnalysis.txt")

# variables
totalMonths = 0    # calculate total months
totalNet = 0       # calculate total net
monthChanges = []  # list of monthly profit/losses changes
months = []        # list of months


with open(csvPath) as budgetData:
    csvReader = csv.reader(budgetData, delimiter=",")
 
    # Read header row
    header = next(csvReader)
    
    # Skip first row
    firstRow = next(csvReader)
    
    # Calculate total Months
    totalMonths += 1
    
    # Calculate net total amount "Profit/Losses"
    totalNet += float(firstRow[1])
    
    # Previous Profit/Losses is in Index 1
    previousPandL = float(firstRow[1])


    for row in csvReader:
        # Calculate total Months
        totalMonths += 1
        
        # Calculate net total amount "Profit/Losses"
        totalNet += float(row[1])

        # Calculate Monthly Profilt/Losses Changes
        monthlyPandL_Changes = float(row[1]) - previousPandL

        # Append(add) to list of monthly profit/losses changes
        monthChanges.append(monthlyPandL_Changes)

        # Append(add) month changes to list of months
        months.append(row[0])

        # Udpate prev. profit/losses
        previousPandL = float(row[1])

# Calculate Average Profilt/Losses Changes
averagePandLChanges = sum(monthChanges) / len(monthChanges)

greatestIncrease = [months[0], monthChanges[0]]   # greatest increase in profits
greatestDecrease = [months[0], monthChanges[0]]   # greatest decrease in profits

# Calculate greatest increase/decrease of index
for m in range(len(monthChanges)):
    if (monthChanges[m] > greatestIncrease[1]):
        greatestIncrease[1] = monthChanges[m]
        greatestIncrease[0] = months[m]

    if (monthChanges[m] < greatestDecrease[1]):
        greatestDecrease[1] = monthChanges[m]
        greatestDecrease[0] = months[m]


# Generate results
output = (
    f"\nFinancial Analysis\n"
    f"\n"
    f"-----------------------\n"
    f"\n"
    f"Total Months: {totalMonths}\n"
    f"\n"
    f"Total: ${totalNet:.0f}\n"
    f"\n"
    f"Average Change: ${averagePandLChanges:.2f}\n"
    f"\n"
    f"Greatest Increase in Profits: {greatestIncrease[0]} ${greatestIncrease[1]:.0f}\n"
    f"\n"
    f"Greatest Decrease in Profits: {greatestDecrease[0]} ${greatestDecrease[1]:.0f}\n"
    )
print(output)


# Export to txt
with open(outputFile, "w") as textFile:
    textFile.write(output)
