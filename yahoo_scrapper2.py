import csv
import json
import tabula
import time
import requests
import http.client
import datetime
import os
from pathlib import Path
from datetime import datetime

print('Beginning files download ... \n')

tickers = ['TSLA']

def patch_http_response_read(func):
    def inner(*args):
        try:
            return func(*args)
        except http.client.IncompleteRead as e:
            return e.partial
    return inner


http.client.HTTPResponse.read = patch_http_response_read(http.client.HTTPResponse.read)

end = datetime.now()

start_timestamp = str(int(datetime.timestamp(datetime(2018, 1, 1))))

end_timestamp = str(int(datetime.timestamp(end)))

print(end_timestamp)
print(start_timestamp)
for ticker in tickers:
    url = 'https://query1.finance.yahoo.com/v7/finance/download/'+ticker+'?period1='+start_timestamp+'&period2='+end_timestamp+'&interval=1d&events=history&includeAdjustedClose=true'
    filepath = '/media/morpheus/Nouveau nom/asfim/scvs/'+ticker+'.csv'
    try:
        r = requests.get(url,stream=True,verify=False)
        print('file '+ticker+'.csv downloaded \n')
        with open(filepath, 'wb+') as f:
            f.write(r.content)
            print('file '+ticker+'.csv written from buffer \n')
    except requests.exceptions.ChunkedEncodingError as e:
        # status_code = e.response.status_code
        print('file '+ticker+'.csv unavailable \n request error status :'+str(e)+'\n')
        pass
    with open('/media/morpheus/Nouveau nom/asfim/scvs/'+ticker+'.csv') as csv_file:
            print(csv_file)
            print(csv_file)
            csv_reader1 = csv.reader(csv_file, delimiter=' ')
            print(csv_reader1)
            #csv_reader = []
            for row in csv_reader1:
                    #csv_reader.append(row)
                    #csv_reader2.append(row)
                    print(row)



