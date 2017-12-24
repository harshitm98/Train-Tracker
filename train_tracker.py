# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 20:57:24 2017

@author: Harshit Maheshwari
"""

from urllib.request import Request, urlopen, URLError
import json

train_list=[16382]



request = Request('https://api.railwayapi.com/v2/live/train/16382/date/24-12-2017/apikey/nxhcd5deez/')

try:
    response = urlopen(request)
    print("Opening the requested url...")
    jsonResponse = response.read()
    print("Reading the response...")
    loadedJson = json.loads(jsonResponse)
    print("Loading the JSON response...")

    response_code = loadedJson['response_code']
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
    
        
    
except (URLError, e):
    print ('Some error!', e)
