import json

import requests


def get_trade_days_from_pt_api():
    res = requests.get("https://www.quantuaninvest.cn/api/trading_day")
    data_str = bytes.decode(res.content)
    data_json = json.loads(data_str)
    today_str = data_json['data'][0]['day']
    pre_day_str = data_json['data'][1]['day']
    print(today_str, pre_day_str)
    return today_str, pre_day_str


get_trade_days_from_pt_api()
