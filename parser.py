import os
def extract_data(input_dir):
    infile=open(os.path.join(input_dir,'WRegularSeasonCompactResults.csv'),'r')
    raw_data=infile.read()
    raw_data=raw_data.split('\n')
    raw_data=[raw_row.split(',') for raw_row in raw_data]
    return raw_data

raw_data=extract_data('/home/victor/Documents/WDataFiles')
