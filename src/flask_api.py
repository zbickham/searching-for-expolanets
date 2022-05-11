from flask import Flask
import xmltodict
import json
import logging
import sys
import pandas as pd
app = Flask(__name__)


@app.route('/load_data', methods = ['POST'])
def load_data():
    
    logging.info('Files have been loaded into the memory.\n')
    inputfile = pd.read_csv(r'koi_candidates.csv',usecols = ["kepid","kepoi_name","kepler_name","koi_disposition","koi_pdisposition","koi_score"])
    inputfile.to_json(r'data.json',orient='records',lines=True)
    print(inputfile)
    return inputfile
#return 'Data loading is complete.\n'

# All the GET Defintions
'''
@app.route('/help', methods=['GET'])
def return_instructions():
    '''
'''
    This Route returns all of the available commands and instructions on
    how to use them.
   ''' '''
    logging.info("Instructions on requesting data printed below.")
    output = "/help - (GET) - o"
    output = output + "\n/load_data - (POST) -  "
    output = output + "\n/epoch - (GET) - Returns all EPOCHs. "
    output = output + "\n/epoch/<epoch> - (GET) - R" 


    return output

@app.route('/epoch', methods=['GET'])
def return_epoch():
    """
    This route grabs all of the epochs and makes it a list.
    Return: it returns the list of epochs
    """
    output = "\n"
    logging.info("Looking for all of the Epoch Positions\n")
    global epoch_length
    global epoch_list #also output
    global epoch_data
    epoch_list = ""
    epoch_data = epochsdata['ndm']['oem']['body']['segment']['data']['stateVector']
    epoch_length = len(epoch_data)
    for i in range(epoch_length):
        epoch_list = epoch_list + epoch_data[i]['EPOCH'] + '\n'

    return epoch_list

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

    #app.run(debug=True, host='0.0.0.0')
