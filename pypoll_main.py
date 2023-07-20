import os
import csv

# Variables
tot_votes = 0
votes = 0
candidates = []
candidate_winning = ""
vote_tracker = {}

# Read csv file
csvpath = os.path.join('/Users/sarahjohn/Desktop/python-challenge/Starter_Code/PyPoll', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) # skips header

    # Iterates over each row in file (after the header)
    for row in csvreader:
        tot_votes += 1
        candidate = row[2]
        votes += 1
        if candidate not in candidates:
            candidates.append(candidate) # add candidate name to the list
            vote_tracker[candidate] = [0]
        vote_tracker[candidate][0] += 1 # add to the candidates vote tracker

    # Calculate percentages and add to the dictionary
    for key, value in vote_tracker.items():
        percentage = round(value[0] / tot_votes * 100, 3)
        value.append(percentage)

# Find winning candidate
max_percentage = 0
for key, value in vote_tracker.items():
    if value[1] > max_percentage:
        max_percentage = value[1]
        candidate_winning = key

# Write to a new csv file
output_path = os.path.join("/Users/sarahjohn/Desktop/python-challenge/Starter_Code/PyPoll", "Resources", "pypoll.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {tot_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate in candidates:
        txtfile.write(f"{candidate}: {vote_tracker[candidate][1]}% ({vote_tracker[candidate][0]})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {candidate_winning}\n")
    txtfile.write("-------------------------\n")

# Print to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {tot_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {vote_tracker[candidate][1]}% ({vote_tracker[candidate][0]})")
print("-------------------------")
print(f"Winner: {candidate_winning}")
print("-------------------------")
        

