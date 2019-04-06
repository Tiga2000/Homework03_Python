import csv
import os

#assuming we know there are only 4 candidates
#variables for candidates: Khan, Correy, Li, O'Tooley
kvote = 0
cvote = 0
lvote = 0
ovote = 0
totesvotes = 0
wincount = 0

csvpoll = os.path.join("Resources", "election_data.csv")

with open(csvpoll) as csvfile:
    csvreader = csv.DictReader(csvpoll)

    for row in csvreader:
        totesvotes = totesvotes + 1

        if (row[2]) == "Khan":
            kvote = kvote + 1
        if (row[2]) == "Correy":
            cvote = cvote + 1
        if (row[2]) == "Li":
            lvote = lvote + 1
        if (row[2]) == "O'Tooley":
            ovote = ovote + 1

candlist = {"Khan": kvote,"Correy": cvote,"Li" :lvote, "O'Tooley": ovote}
for candidate in candlist.items():
    if votes > wincount:
        wincount = votes
        winner = candidate

kpercent = float(kvote) / float(totesvotes) * 100
cpercent = float(cvote) / float(totesvotes) * 100
lpercent = float(lvote) / float(totesvotes) * 100
opercent = float(ovote) / float(totesvotes) * 100

print(f' Total Votes: {totesvotes}')
print(f' Khan: {kpercent}')
print(f' Correy: {cpercent}')
print(f' Li: {lpercent}')
print(f' OTooley: {opercent}')
print(f' Winner: {winner}')
