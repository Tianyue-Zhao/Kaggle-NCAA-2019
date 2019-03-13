#NEURALNET

# FEATURES TO USE:
# 1. Ranking System Difference Scaled
# 	Formula: (TeamARank - TeamBRank)/(# of Total Ranks)
# 	e.g. (5th Place - 40th Place)/122 Ranks = -35/122 = -0.286..

# 2. Ranking of Team A
# 	e.g. 5th Place = 5

# 3. Ranking of Team B
# 	e.g. 40th Place = 40

# 4. ??


#IMPORTS
from rankings import teamRankings
import pandas as pd

TeamList = pd.read_csv('womens-machine-learning-competition-2019/WDataFiles/WTeams.csv')
teams = TeamList["TeamID"].tolist()

teamA = teams[15] #Fake Test ID
teamB = teams[22] #Fake Test ID

#1
posA = teamRankings.keys().index(teamA)
posB = teamRankings.keys().index(teamB)
ONE = posA-posB
print(ONE)

#2
TWO = posA

#3
THREE = posB

#4