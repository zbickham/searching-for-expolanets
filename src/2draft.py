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
            if len(data['Candidates']) == 1:
                break
            data['Candidates'].append(dict(row))

        print(data)




if __name__ == '__main__':
    load_data()
