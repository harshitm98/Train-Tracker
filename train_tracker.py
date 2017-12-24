# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 20:57:24 2017

@author: Harshit Maheshwari
"""

from urllib.request import Request, urlopen, URLError
from pandas import DataFrame
import json

train_number = '16382' #You can change the number to your desired train number.
date = '24-12-2017' #Change the date to the date at which the train started.

request_url = "https://api.railwayapi.com/v2/live/train/" + train_number + "/date/" + date + "/apikey/nxhcd5deez/"
request = Request(request_url+"")

try:
    response = urlopen(request)
    print("Opening the requested url...")
    jsonResponse = response.read()
    print("Reading the response...")
    loadedJson = json.loads(jsonResponse)
    print("Loading the JSON response...")

    response_code = int(loadedJson['response_code'])
    if(response_code == 200):  
        route = loadedJson['route']
        nameList = []
        expectedArrival = []
        actualArrival=[]
        finalDelay=[]
        for i in route:
            if(i['has_arrived']):
                nameList.append(i['station']['name'])
                expectedArrival.append(i['scharr'])
                actualArrival.append(i['actarr'])
                finalDelay.append(int(i['status'].split(' ')[0]))
        data = DataFrame({'Name':nameList,'Expected Arrival':expectedArrival,'Actual Arrival':actualArrival,'Delay':finalDelay})
        excel_name = train_number +"_" + date + ".xlsx"
        data.to_excel(excel_name,sheet_name=date,index=False)
        print("Excel file created.")
    else:
        print("Something went wrong. Here's the response code: " + str(response_code))
    
except (URLError, e):
    print ('Some error!', e)
