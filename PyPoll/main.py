# Import csv file
import csv
import os

# Read and open csv file
csvPath = os.path.join("..", "Resources", "election_data.csv")

# Output results to txt file
outputFile = os.path.join("FinancialAnalysis.txt")


# Variables 
totalVotes = 0      # total number of votes
candidateNames = [] # empty list for candidate names
candidateVotes = {} # empty dictionary for candidate votes
winnerCount = 0     # count for winner
winnerName = ""     # name of winner is open string


# Read file
with open(csvPath) as electionData:
    csvReader = csv.reader(electionData, delimiter=",")
 
    # Read header row
    header = next(csvReader)
    
    # Rows lists
        # Ballot ID is index 0
        # County is index 1
        # Candidate Name is index 2
    

    for row in csvReader:
        # Calculate total Votes
        totalVotes += 1

        # Check names from candidateNames list and add names to list
        if row[2] not in candidateNames:
            candidateNames.append(row[2])

            # Add value of candidateNames to dictionary and start counting at 1
            candidateVotes[row[2]] = 1

        else:
            # if the candidate's name is in the list of names, count each name as 1 vote
            candidateVotes[row[2]] += 1

# Create vote output as open string
voteOutput = ""

# Get list of candidates that received votes and their percentages
for candidate in candidateVotes:
    votes = candidateVotes.get(candidate)
    votePCT = (float(votes) / float(totalVotes)) * 100.00

    # Compare and update new winner count to votes; candidate with most vote count is equal to winner's name
    if votes > winnerCount:
        winnerCount = votes
        winnerName = candidate

    voteOutput += f"{candidate}: {votePCT:.3f}% ({votes})\n \n"


# Generate results
output = (
    f"\nElection Results\n"
    f"\n"
    f"-----------------------\n"
    f"\n"
    f"Total Votes: {totalVotes}\n"
    f"\n"
    f"-----------------------\n"
    f"\n"
    f"{voteOutput}"
    f"\n"
    f"Winner: {winnerName} \n"
    f"\n"
    f"-----------------------\n"
    )
print(output)


# Export to txt
with open(outputFile, "w") as textFile:
    textFile.write(output)

