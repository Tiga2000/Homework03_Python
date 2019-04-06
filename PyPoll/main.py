import os
import csv

csvfile = os.path.join('Resources', 'election_data.csv')
#Sanity check
open(csvfile)

electioncsv = csv.reader(open(csvfile))
header = next(electioncsv)

#assuming we know there are only 4 candidates
#variables for candidates: Khan, Correy, Li, O'Tooley
kvote = 0
cvote = 0
lvote = 0
ovote = 0
totesvotes = 0

#For any vote count add 1 to total votes
#If row matches "candidate" then add 1 to the candidate's vote count
for row in electioncsv:
    totesvotes = totesvotes + 1
    if (row[2]) == "Khan":
            kvote = kvote + 1
    if (row[2]) == "Correy":
            cvote = cvote + 1
    if (row[2]) == "Li":
            lvote = lvote + 1
    if (row[2]) == "O'Tooley":
            ovote = ovote + 1

#Calculate percent votes of each candidate
#Round ommitted trailing 0 so I used ***'{:.3f}'.format*** to show 3 0's
kpercent = '{:.3f}'.format(float(kvote) / float(totesvotes) * 100)
cpercent = '{:.3f}'.format(float(cvote) / float(totesvotes) * 100)
lpercent = '{:.3f}'.format(float(lvote) / float(totesvotes) * 100)
opercent = '{:.3f}'.format(float(ovote) / float(totesvotes) * 100)

#Put candidate name and votes into a dictionary
candlist = {"Khan": kvote,"Correy": cvote,"Li" :lvote, "O'Tooley": ovote}
#Find whoever has the highest vote count
winner = max(candlist, key=candlist.get)

output = (
    f" Total Votes: {totesvotes}\n"
    f"---------------------------\n"
    f" Khan: {kpercent}% ({kvote})\n"
    f" Correy: {cpercent}% ({cvote})\n"
    f" Li: {lpercent}% ({lvote})\n"
    f" O'Tooley: {opercent}% ({ovote})\n"
    f"---------------------------\n"
    f" Winner: {winner}\n"
    f"---------------------------\n")

print(output)

with open("electionresults.txt", "w") as txt_file:
    txt_file.write(output)
