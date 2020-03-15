import datetime, time
from flask import request, jsonify
from connect.connect import app_ib


def get_price_hist():
    timeStr = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d %H:%M:%S')
    print(timeStr)
    #app_ib.reqHistoricalData(18002, ContractSamples.ContFut(), timeStr, "1 Y", "1 month", "TRADES", 0, 1, False, []);
    action = request.json['action']
    asset = request.json['asset']
    print(asset)
    start = request.json['start']
    print(start         )
    end = request.json['end']
    print(end)
    response = {'price':'teste'}
    return jsonify(response)

def create_contract():
    pass