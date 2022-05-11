from flask import Flask
import xmltodict
import json
import logging
import sys
import csv
import pandas as pd
from wget import download
import os
app = Flask(__name__)


@app.route('/load_data', methods = ['POST'])
def load_data():
    #os.remove('koi_candidates.csv')
    print('\nDownloading Files.\n\nGive me a Second!')
    #download("https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&format=csv", out = "koi_candidates.csv", bar=None)

    success = '\nFile has been successfully loaded into the memory.\n'
    logging.info('File is being loaded into the memory.\n')
    inputfile = pd.read_csv(r'koi_candidates.csv',nrows=10,usecols = ["kepid","kepoi_name","kepler_name","koi_disposition","koi_pdisposition","koi_score"])
    '''
    with open('koi_candidates.csv', encoding='utf-8') as inputfile:
        csvReader = csv.DictReader(inputfile)
        global data
        data = {}
        #jsonf.write(json.dumps(data, indent=4))
    '''
    listdata = []
    global data
    inputfile.to_json(r'data.json',orient='records',lines=True)
    with open('data.json','r') as inputjson:
        #inputjson.write(json.dumps(data, indent=4))
        data =inputjson.read()
        print(data)
        newdata = json.loads(data)
        #listdata.append(data)
        #newdata = []
        #for x in range(10):
         #   newdata.append(json.loads(data[x])['kepid'])
        #jsondata = {'Foo' : newdata}
        #data = json.loads(data)
        print(newdata)
        print(success)
    return 'Data loading is complete.\n'


@app.route('/help', methods=['GET'])
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

@app.route('/confirmed_planets', methods=['GET'])
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
    planet_list = ""
    
    data_length = len(data)
    num = 0
    for i in range(data_length):
        #json.loads(data[i])['kepler_name']
        current_planet = json.loads(data[i])['kepler_name']
        current_planet = data[i]['kepler_name']
        if current_planet is None:
            planet_list = planet_list + current_planet + '\n'
        #num = num +1
    return planet_list
'''
@app.route('/epoch/<epoch>', methods=['GET'])
def return_specific_epoch(epoch: str):
    """
    Yea
    """
    logging.info("Looking for requested epoch")
    epoch_data = epochsdata['ndm']['oem']['body']['segment']['data']['stateVector']
    output_list = []
    for pos in range(len(epoch_data)):
        current_epoch = epoch_data[pos]['EPOCH']
        if epoch == current_epoch:
            specific_epoch_data = epoch_data[pos]
            output_list.append(specific_epoch_data)
    
    return json.dumps(output_list, indent=2)

@app.route('/delete_data/<data>', methods = ['DELETE'])
def detelte_data():
    
    logging.info('Whatever\n')


    return 'Data loading is complete.\n' 
  
@app.route('/update/<newdata>', methods = ['PUT'])
def detelte_data():
    
    logging.info('Whatever\n')


    return 'Data loading is complete.\n'  
'''        
if __name__ == '__main__':
    load_data()
    return_confirmed_planets()
    #app.run(debug=True, host='0.0.0.0')
