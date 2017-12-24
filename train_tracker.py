# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 20:57:24 2017

@author: Harshit Maheshwari
"""

from urllib.request import Request, urlopen, URLError

train_list=[16382]

request = Request('https://api.railwayapi.com/v2/live/train/16382/date/24-12-2017/apikey/nxhcd5deez/')

try:
	response = urlopen(request)
	jsonResponse = response.read()
	print (jsonResponse)
except (URLError, e):
    print ('Some error!', e)
