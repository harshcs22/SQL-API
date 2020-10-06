#Title : Unit Test for API
#Descripstion : USing pytest
#Company : Kugelblitz Pvt. LTd.
#Author : Harsh Verma
#Date: 29 September 2020 

# importing required library
#from api import app
import pytest
import requests
import json
   

# for api 1
# checking status code 
# content type / format returned 
# validating results for query 
def test_1():

    response = requests.get("http://0.0.0.0:5000/title?title=bloody%20mama")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    response_body = response.json()
    assert response_body[0]['Year'] == 1970

# for api 2
def test_2():

    response = requests.get("http://0.0.0.0:5000/year?year=1971")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    response_body = response.json()
    assert response_body[0]['Movie.Title'] == "Born to Win"


# coverage testing contd..