import pandas as pd
from pandas import read_csv
from collections import OrderedDict
	#Access any file with "FileName" - e.g. print(WTeams[0])

#RANKING ALGORITHM
TourneyResults = pd.read_csv('womens-machine-learning-competition-2019/WDataFiles/WNCAATourneyCompactResults.csv')
SeasonResults = pd.read_csv('womens-machine-learning-competition-2019/WDataFiles/WRegularSeasonCompactResults.csv')
TeamList = pd.read_csv('womens-machine-learning-competition-2019/WDataFiles/WTeams.csv')
teams = TeamList["TeamID"].tolist()

teamsWL = {}
for team in teams:
    #TOURNEY RESULTS
    TourneyWinList = TourneyResults["WTeamID"].tolist()
    TourneyLossList = TourneyResults["LTeamID"].tolist()
    TourneyWins = TourneyWinList.count(team)
    TourneyLosses = TourneyLossList.count(team)
    
    #SEASON RESULTS
    SeasonWinList = SeasonResults["WTeamID"].tolist()
    SeasonLossList = SeasonResults["LTeamID"].tolist()
    SeasonWins = SeasonWinList.count(team)
    SeasonLosses = SeasonLossList.count(team)

    if (TourneyWins+SeasonWins+TourneyLosses+SeasonLosses > 0):
        WLRatio = (TourneyWins+SeasonWins)/float(TourneyLosses+SeasonLosses)
    else:
        WLRatio = "No Data"
    teamsWL.update({team:WLRatio})

teamRankings = OrderedDict(sorted(teamsWL.items(), key=lambda x: x[1], reverse=True))
print(teamRankings)




# NON-PANDAS VERSION -- DO NOT DELETE
# TourneyResults = WNCAATourneyCompactResults
# SeasonResults = WRegularSeasonCompactResults
# TeamList = WTeams
# teams = [item[0] for item in TeamList] #TeamNames

# teamsWL = {}
# for team in teams[0:2]:
#     #TOURNEY RESULTS
#     TourneyWinList = [item[2] for item in TourneyResults] #WTeamID
#     TourneyLossList = [item[4] for item in TourneyResults] #LTeamID
#     TourneyWins = TourneyWinList.count(team)
#     TourneyLosses = TourneyLossList.count(team)
#     #SEASON RESULTS
#     SeasonWinList = [item[2] for item in SeasonResults] #WTeamID
#     SeasonLossList = [item[4] for item in SeasonResults] #WTeamID
#     SeasonWins = SeasonWinList.count(team)
#     SeasonLosses = SeasonLossList.count(team)

#     if (TourneyWins+SeasonWins+TourneyLosses+SeasonLosses > 0):
#         WLRatio = (TourneyWins+SeasonWins)/float(TourneyLosses+SeasonLosses)
#     else:
#         WLRatio = "No Games"
#     teamsWL.update({team:WLRatio})

# print(teamsWL)
