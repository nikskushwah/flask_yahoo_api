import requests
import os
from flask import Flask, jsonify, request
import json

app = Flask(__name__)


url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-summary"
url_stock =  "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"


querystring = {"region":"US","lang":"en"}

querystring_stock = {"region":"US","symbol":"AMRN"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "b9a7d35c13msh436be85dbf1852dp143bc9jsne2131367d259"
    }


@app.route('/',methods=['GET','POST'])
def get_summary():
    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = json.loads(response.text)
    return json.dumps(json_data)

@app.route('/stocks',methods=['GET','POST'])
def get_stock_summary():
    response = requests.request("GET", url_stock, headers=headers, params=querystring_stock)
    json_data = json.loads(response.text)
    return json.dumps(json_data)


if __name__ == "__main__":
    app.run()
