#Import dependencies
import os
import csv

#Set file path
csvfile = os.path.join('Resources', 'budget_data.csv')
open(csvfile)

#Instead of just opening file, makes it reread the csvfile from start. Hold file in memory
budgetcsv = csv.reader(open(csvfile))
header = next(budgetcsv)

#Use list comprehension
#Exploit that its only 2 columns; much easier to look up by key since its with unique dates
mydata = {k:int(v) for k,v in budgetcsv}

totalsum = sum(mydata.values())
monthcount = len(mydata)

mymonths = list(mydata.keys())
currentkey, prevkey = mymonths[1:], mymonths[:-1]

#Thisdoesnt remember which month is the greatest difference
#[mydata[c] -mydata[p] for c,p in zip(currentkey, prevkey)]

#This "c" assigns the month to the calculated difference
netchange = {c: mydata[c] -mydata[p] for c,p in zip(currentkey, prevkey)}

averagechange = round(sum(netchange.values()) / len(netchange), 2)

greatestincrease = max(netchange, key=netchange.get)
greatestdecrease = min(netchange, key=netchange.get)

#This short line calling upon dictionary took me hours to find
monthincrease = netchange[greatestincrease]
monthdecrease = netchange[greatestdecrease]

output = (
    f"Financial Analysis\n"
    f"---------------------------\n"
    f"Total Months: {monthcount}\n"
    f"Total: ${totalsum}\n"
    f"Average Change: ${averagechange}\n"
    f"Greatest Increase in Profits: {greatestincrease} (${monthincrease})\n"
    f"Greatest Decrease in Profits: {greatestdecrease} (${monthdecrease})\n")

print(output)

with open("budgetdata.txt", "w") as txt_file:
    txt_file.write(output)
