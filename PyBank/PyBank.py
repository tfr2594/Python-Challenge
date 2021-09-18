#check video 2 of python to figure out where to start
import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Objective 3: Create the lists to store data. 

profit = []
monthly_changes = []
date = []

# set variables 
 
initial_profit = 0

# Open the CSV using the set path PyBankcsv

with open(budget_data_csv, encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    #for row in csv_reader: check the candy segment in python 2
    #row is the variable that goes line by line down the data putting a [0] or [1] gives youe one of the columns
    # and if i append each column i can get the totals!
    
    for row in csv_reader:    

      # Will need it when collecting the greatest increase and decrease in profits
      date.append(row[0])

      #change the row to an int type for math functions to work
      profit.append(int(row[1]))
      
      ##to find change = current - previous/inital profit (revist)
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit
      initial_profit = final_profit

      #where to keep the changes between each month on the empty list above
      monthly_changes.append(monthly_change_profits)
#have to append a first row before the for loop 
      #somehow find the average of changes in profit
      #averag =sum of the list / len the monthly changes
      #the algorithm is correct but something is not working in the math, but this is closest I can do
      average_change_profits = (sum(monthly_changes) / 85)

      #Find the max and min change in profits 
      max_increase_profits = max(monthly_changes)
      max_decrease_profits = min(monthly_changes)
      
      #the date that the biggest dropped and raise happened
      largest_date = date[monthly_changes.index(max_increase_profits)]
      smallest_date = date[monthly_changes.index(max_decrease_profits)]

    final_presentation = (
    f"----------------------------\n"
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {len(date)}\n"
    f"Total Revenue: ${sum(profit)}\n"
    f"Average Revenue Change: {average_change_profits}\n"
    f"Greatest Increase in Revenue: {(largest_date)} and ${(max_increase_profits)}\n"
    f"Greatest Decrease in Revenue: : {(smallest_date)} and ${(max_decrease_profits)}\n"
    f"----------------------------\n")
    
    print(final_presentation)

#look at the end video three but also youtube because we only learned how to export csv and not text files
output_path = os.path.join("Resources", "textfile.txt")


with open(output_path, "w", newline='') as text_file:
    text_file.write(final_presentation)