import os
import csv
from datetime import datetime

# Open the CSV file
csvpath = r'/Users/davidgoeller/Desktop/mod_3_chal/mod_3_instructions/PyBank/Resources/budget_data.csv'
with open(csvpath) as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
       # Initialize variables
    num_months = 0
    gross_profit_loss = 0
    prev_month_profit_loss = 0
    avg_profit_loss = 0
    highest_profit = float('-inf')
    highest_profit_date = None
    lowest_profit = float('inf')
    lowest_profit_date = None
    # Loop through the rows
    for row in reader:
        # Parse the date from the first column
        date = datetime.strptime(row[0], '%b-%d')
        # Calculate the profit/loss from the second column
        profit_loss = int(row[1])
        # Calculate the number of months
        if num_months == 0:
            start_date = date
        num_months += 1
        end_date = date
        # Calculate the gross profit/loss
        gross_profit_loss += profit_loss
        # Calculate the average profit/loss from month to month
        if num_months > 1:
            avg_profit_loss += profit_loss - prev_month_profit_loss
        prev_month_profit_loss = profit_loss
        # Update the highest and lowest profits
        if profit_loss > highest_profit:
            highest_profit = profit_loss
            highest_profit_date = date
        if profit_loss < lowest_profit:
            lowest_profit = profit_loss
            lowest_profit_date = date

# Calculate the average profit/loss from month to month
if num_months > 1:
    avg_profit_loss /= num_months - 1

# Print/output the results
with open("bank_results.txt", "w") as output_file:
    print("Financial Analysis", file=output_file)
    print("--------------------------", file=output_file)
    print(f"Number of months: {num_months}", file=output_file)
    print(f"Gross profit/loss: {gross_profit_loss}", file=output_file)
    print(f"Average profit/loss from month to month: {avg_profit_loss}", file=output_file)
    print(f"Highest profit: {highest_profit_date:%b-%d} {highest_profit}", file=output_file)
    print(f"Lowest profit: {lowest_profit_date:%b-%d} {lowest_profit}", file=output_file)










