# Open input files for reading
with open('input1.txt', 'r') as f1, open('input2.txt', 'r') as f2:
    input1 = f1.readlines()
    input2 = f2.readlines()

# Extract team wise leaderboard from input1
teams = {}
for line in input1[1:]:
    fields = line.strip().split('\t')
    teams[fields[1]] = fields[2]
score=[]
for line in input2[1:]:
    fields = line.strip().split('\t')
    if(fields[1] in teams):
        score.append([(teams[fields[1]]),int(fields[3]),int(fields[4])])
teams={}
for i in score:
   if(i[0] in teams):
        statement=teams[i[0]][0]
        reason=teams[i[0]][1]
        freq=teams[i[0]][2]
        teams[i[0]]=[(statement+i[1]),(reason+i[2]),(freq+1)]
   else:
        freq=1
        teams[i[0]]=[i[1],i[2],freq]    


# Extract individual leaderboard from input2
individuals = []
for line in input2[1:]:
    fields = line.strip().split('\t')
    individuals.append([fields[1], fields[2], int(fields[3]),int(fields[4])])

# Sort individuals by number of statements and reasons
individuals.sort(key=lambda x: (-x[2], -x[3]))

# Open output files for writing
with open('output1.txt', 'w') as f1, open('output2.txt', 'w') as f2:
    # Write team wise leaderboard to output1
    f1.write('Team Wise Leaderboard\n\n')
    f1.write('Team Rank\tThinking Teams Leaderboard\tAverage Statements\tAverage Reasons\n')
    rank = 1
    for team, scores in sorted(teams.items(), key=lambda x: (-x[1][1], -x[1][0])):
        f1.write(f"{rank}\t{team}\t\t\t{(scores[0]/scores[2]):.2f}\t\t\t{(scores[1]/scores[2]):.2f}\n")
        rank += 1

    # Write individual leaderboard to output2
    f2.write('Individual Leaderboard\n\n')
    f2.write('Rank\tName\t\t\tUID\tNo. of Statements\tNo. of Reasons\n')
    rank = 1
    for i, record in enumerate(individuals):
        f2.write(f"{rank}\t{record[0]}\t\t{record[1]}\t{record[2]}\t\t\t{record[3]}\n")
        rank += 1
        
