#check video 2 of python to figure out where to start
import os
import csv
import pandas as pd

election_data_csv = os.path.join("Resources", "election_data.csv")

# Objective 3: Create the lists to store data. 

votes = []
candidates = []
list_canidates = {} #dictionary, but also attach 0/int to be able to count
countervote_canidates = {"Khan": 0, "Correy": 0, "O'Tooley": 0, "Li": 0}
#print(f'hi')



# Open the CSV using the set path PyBankcsv

with open(election_data_csv, encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")

    for row in csv_reader:
        #append to make lists
        candidates.append(row[2])
        votes.append(row)
        
        #next put the votes to each candidate
    for vote_per_canidate in candidates:
        if vote_per_canidate == "Khan":
            countervote_canidates["Khan"] = countervote_canidates["Khan"] + 1
        elif vote_per_canidate == "Li":
            countervote_canidates["Li"] = countervote_canidates["Li"] + 1
        elif vote_per_canidate == "O'Tooley":
            countervote_canidates["O'Tooley"] = countervote_canidates["O'Tooley"] + 1
        
        elif vote_per_canidate == "Correy":
            countervote_canidates["Correy"] = countervote_canidates["Correy"] + 1
        
        #this how you turn them to integers, so math functions work, make a seperate variable that is an int, tho revisit 
        votes_for_khan = int(countervote_canidates["Khan"])
        votes_for_Li = int(countervote_canidates["Li"])
        votes_for_Correy = int(countervote_canidates["Correy"])
        votes_for_OTooley = int(countervote_canidates["O'Tooley"])

        total_votes = votes_for_khan + votes_for_Li + votes_for_Correy + votes_for_OTooley
        #now do the percent portion
        percent_khan = (votes_for_khan / total_votes) * 100
        percent_Li = (votes_for_Li / total_votes) * 100
        percent_OTooley = (votes_for_OTooley / total_votes) * 100
        percent_Correy = (votes_for_Correy / total_votes) * 100
    
    #print(f'{total_votes}')

    #just some it up to one variable so it's easy tp print and export
    final_presentation = (
    f"----------------------------\n"
    f"Total votes: {total_votes}\n"
    f"----------------------------\n"
    f"Khan: {('{:.2f}'.format(percent_khan))}% ({votes_for_khan})\n"
    f"Correy: {('{:.2f}'.format(percent_Correy))}% ({votes_for_Correy})\n"
    f"Li: {('{:.2f}'.format(percent_Li))}% ({votes_for_Li}) \n"
    f"O'Tooley: {('{:.2f}'.format(percent_OTooley))}% ({votes_for_OTooley})\n"
    f"----------------------------\n"
    f"Winner: Khan\n"
    f"----------------------------\n")
    
    print(final_presentation)
#look at the end video three but also youtube because we only learned how to export csv and not text files
output_path = os.path.join("Resources", "textfile.txt")


with open(output_path, "w", newline='') as text_file:
    text_file.write(final_presentation)

