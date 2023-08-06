import json

import requests
import datetime as dt


def get_request_url():
    base_url = "http://www.szse.cn/api/report/exchange/onepersistenthour/monthList?month="
    current_month = get_current_month()
    request_url = base_url + current_month
    return request_url


def get_current_month():
    today_str = dt.datetime.now().strftime("%Y%m%d")
    year = today_str[:4]
    month = today_str[4:6]
    return year + "-" + month


def get_trade_day_for_a_month():
    request_url = get_request_url()
    res = requests.get(request_url)
    print(res.content)


def format_bytes_to_json(res):
    data_str = bytes.decode(res.content)
    data_json = json.loads(data_str)
    return data_json

def get_trade_days_from_json_res(json_res):
    json_data = json_res['data']
    trade_days_len = len(json_data)
    trade_days_list = []
    for i in range(trade_days_len):
        jyrq = trade_days_len[i]['jyrq']
        jybz = trade_days_len[i]['jybz']
        if jybz == 1:
            trade_days_list.append(jyrq)



get_trade_day_for_a_month()
