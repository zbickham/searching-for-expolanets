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
    #inputfile = pd.read_csv(r'koi_candidates.csv',nrows=10,usecols = ["kepid","kepoi_name","kepler_name","koi_disposition","koi_pdisposition","koi_score"])
    jsonarray = []
    jsonpath = r'data.json'
    csvpath = 'koi_candidates.csv'
    with open(csvpath, 'r') as inputfile:
        csvReader = csv.DictReader(inputfile)
        global data
        data = {}
        data['Candidates'] = []
        for row in csvReader:
            if len(data['Candidates']) == 10:
                break
            data['Candidates'].append(dict(row))
        print('\ndata has been successfully loaded. \n')
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
    global epoch_length
    global epoch_list #also output
    global epoch_data
    planet_list = "\n"
    datasave = data['Candidates']
    data_length = len(datasave)
    num = 0
    for i in range(data_length):        
        current_planet = datasave[i]['kepler_name']
        if current_planet is not "":
            planet_list = planet_list + current_planet + '\n'
    print('\nList of Confirmed Planets:\n',planet_list)
    return planet_list


if __name__ == '__main__':
    load_data()
    return_confirmed_planets()
