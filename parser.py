import os
def extract_data(input_dir, file_name):
    infile=open(os.path.join(input_dir,file_name),'r')
    raw_data=infile.read()
    raw_data=raw_data.split('\n')
    raw_data=[raw_row.split(',') for raw_row in raw_data]
    return raw_data

WCities=extract_data('womens-machine-learning-competition-2019/WDataFiles', 'WCities.csv')
WGameCities=extract_data('womens-machine-learning-competition-2019/WDataFiles', 'WGameCities.csv')
WNCAATourneyCompactResults=extract_data('womens-machine-learning-competition-2019/WDataFiles', 'WNCAATourneyCompactResults.csv')
WNCAATourneyDetailedResults=extract_data('womens-machine-learning-competition-2019/WDataFiles', 'WNCAATourneyDetailedResults.csv')
WNCAATourneySeeds=extract_data('womens-machine-learning-competition-2019/WDataFiles', 'WNCAATourneySeeds.csv')
WNCAATourneySlots=extract_data('womens-machine-learning-competition-2019/WDataFiles', 'WNCAATourneySlots.csv')
WRegularSeasonCompactResults=extract_data('womens-machine-learning-competition-2019/WDataFiles', 'WRegularSeasonCompactResults.csv')
WRegularSeasonDetailedResults=extract_data('womens-machine-learning-competition-2019/WDataFiles', 'WRegularSeasonCompactResults.csv')
WSeasons=extract_data('womens-machine-learning-competition-2019/WDataFiles', 'WSeasons.csv')
WTeams=extract_data('womens-machine-learning-competition-2019/WDataFiles', 'WTeams.csv')
WTeamSpellings=extract_data('womens-machine-learning-competition-2019/WDataFiles', 'WTeamSpellings.csv')
