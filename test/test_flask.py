import pytest
import requests

api_host = 'localhost'
api_port = '5003'
api_prefix = f'http://{api_host}:{api_port}'

def test_data_laod():
    route = f'{api_prefix}/download_data'
    response = requests.post(route)
    assert response.ok == True
    assert response.content == b'Data has been loaded.\n'

def test_data_get():
    route = f'{api_prefix}/feature/mag'
    response = requests.get(route)
    
    assert response.ok == True
