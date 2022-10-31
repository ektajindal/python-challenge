import os
import csv
# open the csv
file = r"C:\Users\ektac\python-challenge\PyPoll\Resources\election_data.csv"
with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

#Read the header row first
    csvheader = next(csvreader)
    print(f"Header: {csvheader}")

    #Create empty list

    total_votes = 0
    poll = {}
    candidates = []
    num_votes = []

    #Read values through loop
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
#calculation for number of votes for candidates
for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)

vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 1))

finaldata = list(zip(candidates, num_votes, vote_percent))

winnerlst = []

for name in finaldata:
    if max(num_votes) == name[1]:
        winnerlst.append(name[0])
#create empty winner list
winner = winnerlst[0]

#Print data
print ("Election Results")
print("-------------------------------------")
print (f"Total Votes: {str(total_votes)}")
print("-------------------------------------")
for entry in finaldata:
    print(f"{entry[0]}: ({(str(entry[2]))}%) ({(str(entry[1]))})")
print("-------------------------------------")
print(f"Winner: {str(winner)}")

#Print output to text file
result = os.path.join(".", 'resultPyPoll.txt')
with open(result,"w") as new:
    new.write("Election Results")
    new.write("\n")
    new.write("-------------------------------------")
    new.write("\n")
    new.write(f"Total Votes: {str(total_votes)}")
    new.write("\n")
    new.write("-------------------------------------")
    new.write("\n")
    for entry in finaldata:
        new.write(f"{entry[0]}: ({(str(entry[2]))}%) ({(str(entry[1]))})")
    new.write("\n")
    new.write("-------------------------------------")
    new.write("\n")
    new.write(f"Winner: {str(winner)}")

