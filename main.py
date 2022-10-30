import os
import csv
# open the csv
file = r"C:\Users\ektac\python-challenge\PyBank\Resources\budget_data.csv"
with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

#Read the header row first
    csvheader = next(csvreader)
    print(f"Header: {csvheader}")
    
    #create empty list
    month_count = []
    profit = []
    change_profit = []

    #Read values through loop
    for row in csvreader:
        month_count.append(row[1])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])

    #maximum and minimum values
    increase = max(change_profit)
    decrease = min(change_profit)

    month_increase = change_profit.index(max(change_profit))+1
    month_decrease = change_profit.index(min(change_profit))+1

#Print data

    print ("Financial Analysis")
    print("-------------------------------------")
    print (f"Total Months:{len(month_count)}")
    print(f"Total: ${sum(profit)}")
    print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
    print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
    print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")

#Print output to text file
result = os.path.join(".", 'result.txt')
with open(result,"w") as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("------------------------")
    new.write("\n")
    new.write(f"Total Months:{len(month_count)}")
    new.write("\n")
    new.write(f"Total: ${sum(profit)}")
    new.write("\n")
    new.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")