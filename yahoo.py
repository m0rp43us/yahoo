import requests

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-chart"

querystring = {"interval":"5m","symbol":"AMRN","range":"1d","region":"US"}

headers = {
    'x-rapidapi-key': "your api key",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring,verify=False)

print(response.text)