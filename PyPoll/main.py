import os
import csv

csvfile = os.path.join('Resources', 'election_data.csv')
#Sanity check
open(csvfile)

electioncsv = csv.reader(open(csvfile))
header = next(electioncsv)
#Create dictionary
results = {}
#Initializing key inside dictionary
results["Total Votes"] = 0

#Index matching
for vid,cnty,cand in electioncsv:

    results["Total Votes"] += 1

    if cand in results.keys():
        results[cand] += 1
    else:
        results[cand] = 1

results
#Need to find 2nd max so instead use sort and found the 2nd value
winner=sorted(results, key=results.get)[-2]

#I had trouble saving "for k in results:..." so i saved it as function

for k in results:
    #Round ommitted trailing 0 so I used ***'{:.3f}'.format*** to show 3 0's
    print(k,'{:.3f}'.format(round(results[k] / results["Total Votes"] * 100)),'%')

output = (
    f"Election Results\n"
    f"---------------------------\n"
    f"{results}")
print(output)

float(xxx)
