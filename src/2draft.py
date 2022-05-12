import json
import logging
import sys
import csv
import pandas as pd
from wget import download
import os
import redis

#app = Flask(__name__)


#@app.route('/load_data', methods = ['POST'])
def load_data():
    #os.remove('koi_candidates.csv')
    print('\nDownloading Files.\n\nGive me a Second!')
    #download("https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&format=csv", out = "koi_candidates.csv", bar=None)

    success = '\nFile has been successfully loaded into the memory.\n'
    logging.info('File is being loaded into the memory.\n')
    
    jsonarray = []
    jsonpath = r'data.json'
    csvpath = 'koi_candidates.csv'
    with open(csvpath, 'r') as inputfile:
        csvReader = csv.DictReader(inputfile)
        global data
        data = {}
        data['Candidates'] = []
        for row in csvReader:
            if len(data['Candidates']) == 20:
                break
            data['Candidates'].append(dict(row))
        print('\ndata has been successfully loaded. \n')
    global datasave
    datasave = data['Candidates']
    global wanted_data
    wanted_data = ['kepid','kepoi_name','kepler_name','koi_disposition','koi_pdisposition','koi_score','koi_time0bk']
    return '\ndata has been successfully loaded. \n'

#@app.route('/help', methods=['GET'])
def return_instructions():
    '''
    This Route returns all of the available commands and instructions on
    how to use them.
    '''
    logging.info("Instructions on requesting data printed below.")
    output = "/help - (GET) - output these instructions"
    output = output + "\n/load_data - (POST) -  "
    output = output + "\n/epoch - (GET) - Returns all EPOCHs. "
    output = output + "\n/epoch/<epoch> - (GET) - R" 


    return output

#@app.route('/confirmed_planets', methods=['GET'])
def return_confirmed_planets():
    """
    This route grabs all of the epochs and makes it a list.
    Return: it returns the list of epochs
    """
    output = "\n"
    logging.info("Looking for all of the Epoch Positions\n")
    planet_list = "\n"
    datasave = data['Candidates']
    data_length = len(datasave)
    num = 0
    for i in range(data_length):        
        current_planet = datasave[i]['kepler_name']
        if current_planet is not "":
            planet_list = planet_list + current_planet + '\n'
    #print('\nList of Confirmed Planets:\n',planet_list)
    return planet_list

#@app.route('/epoch/<epoch>', methods=['GET'])
def reorganize_by_dispositions():
    """
    Yea
    """
    logging.info("Data")
    global updated_data
    updated_data = {'CONFIRMED' : [[],["Total Confirmed: ",0]],'FALSE POSITIVE': [[],["Total False Positives: ",0]],'NOT DISPOSITIONED': [[],["Total Not Dispositioned: ",0]],'CANDIDATE': [[],["Total Candidates: ",0]]}
    
    for i in range(len(datasave)):
        current_og_candidate = datasave[i]['koi_disposition']
        candidate_dict = {}
        for j in wanted_data:
            candidate_dict[j] = datasave[i][j]
        if current_og_candidate == 'CONFIRMED':
            updated_data['CONFIRMED'][0].append(candidate_dict)
            updated_data['CONFIRMED'][1][1] += 1

        if current_og_candidate == 'FALSE POSITIVE':
            updated_data['FALSE POSITIVE'][0].append(candidate_dict)
            updated_data['FALSE POSITIVE'][1][1] += 1

        if current_og_candidate == 'NOT DISPOSITIONED':
            updated_data['NOT DISPOSITIONED'][0].append(candidate_dict)
            updated_data['NOT DISPOSITIONED'][1][1] += 1

        if current_og_candidate == 'CANDIDATE':
            updated_data['CANDIDATE'][0].append(candidate_dict)
            updated_data['CANDIDATE'][1][1] += 1
    data = updated_data        
    
    return 'data has been updated to be categorized by dispositions.'
#@app.route('/epoch/<epoch>', methods=['GET'])
def reorganize_by_initial_dispositions():
    """
    Yea
    """
    logging.info("Data")
    global updated_data
    updated_data = {'FALSE POSITIVE': [[],["Total False Positives: ",0]],'NOT DISPOSITIONED': [[],["Total Not Dispositioned: ",0]],'CANDIDATE': [[],["Total Candidates: ",0]]}
    
    for i in range(len(datasave)):
        current_og_candidate = datasave[i]['koi_pdisposition']
        candidate_dict = {}
        for j in wanted_data:
            candidate_dict[j] = datasave[i][j]

        if current_og_candidate == 'FALSE POSITIVE':
            updated_data['FALSE POSITIVE'][0].append(candidate_dict)
            updated_data['FALSE POSITIVE'][1][1] += 1

        if current_og_candidate == 'NOT DISPOSITIONED':
            updated_data['NOT DISPOSITIONED'][0].append(candidate_dict)
            updated_data['NOT DISPOSITIONED'][1][1] += 1

        if current_og_candidate == 'CANDIDATE':
            updated_data['CANDIDATE'][0].append(candidate_dict)
            updated_data['CANDIDATE'][1][1] += 1
    pre_data = updated_data        
    
    return 'data has been updated to be categorized by dispositions.'

#@app.route('/epoch/<epoch>', methods=['GET'])
def return_initial_dispositions():
    """
    Yea
    """
    logging.info("Data")
    output = [pre_data['FALSE POSITIVE'][1],pre_data['NOT DISPOSITIONED'][1],pre_data['CANDIDATE'][1]]
    print(output[0][0],output[0][1])
    print(output[1][0],output[1][1])
    print(output[2][0],output[2][1],'\n')
    
    return '\nOutput complete.'

def return_final_dispositions():
    """
    Yea
    """
    logging.info("Data")
    output = [data['CONFIRMED'][1],data['FALSE POSITIVE'][1],data['NOT DISPOSITIONED'][1],data['CANDIDATE'][1]]
    print(output[0][0],output[0][1])
    print(output[1][0],output[1][1])
    print(output[2][0],output[2][1])
    print(output[3][0],output[3][1],'\n')
    
    return '\nOutput complete.'

if __name__ == '__main__':
    load_data()
    return_confirmed_planets()
    return_final_dispositions()
