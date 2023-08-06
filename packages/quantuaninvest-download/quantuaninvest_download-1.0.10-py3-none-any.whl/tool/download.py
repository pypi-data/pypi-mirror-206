import datetime
import traceback

import requests
import os


def mkdir_if_not_exist(save_file_path):
    if not os.path.exists(save_file_path):
        os.makedirs(save_file_path)


def save_file_to_ref_path(respose, save_path):
    if respose.status_code == 200:
        print("现在时间是 ", datetime.datetime.now())
        # 保存
        with open(save_path, 'wb') as f:
            f.write(respose.content)


def download_file_from_ref_url(url_path):
    print("download file path is %s " % url_path)
    r = requests.get(url_path)  # 发送请求
    return r


def get_download_path(download_url_path, last_trade_day):
    url = download_url_path + last_trade_day + '.xlsx'  # 目标下载链接
    return url


def get_save_file_path(save_file_path, last_trade_day):
    file_path = save_file_path + last_trade_day + '.xlsx'
    return file_path


def down_load_file(download_url, save_file_path, last_trade_day):
    try:
        print("down_load_file 执行 ", datetime.datetime.now())
        url_path = get_download_path(download_url, last_trade_day)
        res = download_file_from_ref_url(url_path)
        file_path = get_save_file_path(save_file_path, last_trade_day)
        mkdir_if_not_exist(save_file_path)

        print("code is ", res.status_code)
        save_file_to_ref_path(res, file_path)
        return res.status_code
    except Exception as e:
        print("error ", e)
        info = traceback.format_exc()
        print("error info ", info)
        return 500

if __name__ == '__main__':
    download_url = 'https://www.quantuaninvest.cn/zidian/shipan_156368/'
    save_file_path = 'C:/data/pa_qmt/dk_sp/b_s_signal_file/'
    last_trade_day = '20230428'
    down_load_file(download_url, save_file_path, last_trade_day)