import csv
import os

csvpoll = os.path.join("Resources", "election_data.csv")

totesvotes = 0
candlist = []
candpercent = []
candvotes = []
wincount = 0
winner = ""

with open(csvpoll) as csvfile:
    csvreader = csv.DictReader(csvpoll)

    for row in csvreader:
        totesvotes = totesvotes + 1
        candname = (row[2])
        if candname not in candlist:
            candlist.append(row[2])
            candvotes[candname] = 0
        candvotes[candname] = candvotes[candname] + 1

    for candidate in candvotes:
        votes = candvotes.get(candidate)
        candpercent = float(candvotes) / float(totesvotes) * 100

    if (votes > wincount):
        wincount = candvotes
        winner = candidate

print(f'Total Votes: {totesvotes}')
