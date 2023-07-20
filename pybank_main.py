import os
import csv

# Variables
tot_months = 0
tot = 0
previous_value = 0
differences_in_profit_loss = []
sum_of_differences = 0
num_of_differences = 0
date_greatest_increase = ""
date_greatest_decrease = ""
previous_change_max = 0
previous_change_min = 0
change_in_profit_loss = 0

# Read csv file
csvpath = os.path.join('/Users/sarahjohn/Desktop/python-challenge/Starter_Code/PyBank', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) # skips header

    # Iterate through each row in csv file (after the header)
    for row in csvreader:
        if previous_value != 0:
            change_in_profit_loss = int(row[1]) - int(previous_value)
            differences_in_profit_loss.append(change_in_profit_loss)
        previous_value = row[1]
        if change_in_profit_loss > previous_change_max:
            previous_change_max = change_in_profit_loss
            date_greatest_increase = row[0]
        if change_in_profit_loss < previous_change_min:
            previous_change_min = change_in_profit_loss
            date_greatest_decrease = row[0]
        tot_months += 1
        tot += int(row[1])

    for value in differences_in_profit_loss:
        sum_of_differences += value
        num_of_differences += 1

    avg_of_differences = round(sum_of_differences / num_of_differences, 2)

# Write to a new csv file
output_path = os.path.join("/Users/sarahjohn/Desktop/python-challenge/Starter_Code/PyBank", "Resources", "pybank.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {tot_months}\n")
    txtfile.write(f"Total: ${str(tot)}\n")
    txtfile.write(f"Average Change: ${str(avg_of_differences)}\n")
    txtfile.write(f"Greatest Increase in Profits: {date_greatest_increase} (${str(previous_change_max)})\n")
    txtfile.write(f"Greatest Decrease in Profits: {date_greatest_decrease} (${str(previous_change_min)})\n")

# Print to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {tot_months}")
print(f"Total: ${str(tot)}")
print(f"Average Change: ${str(avg_of_differences)}")
print(f"Greatest Increase in Profits: {date_greatest_increase} (${str(previous_change_max)})")
print(f"Greatest Decrease in Profits: {date_greatest_decrease} (${str(previous_change_min)})")
