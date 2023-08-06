import pandas as pd
import traceback


def get_sheet_df_from_xlsx(ContextInfo, path, sheetname_):
    """
    从xlsx文件中获得指定sheet的内容
    """
    file_name = ContextInfo.previous_date
    path = path + file_name + ".xlsx"

    try:
        data_ = pd.read_excel(path, sheetname=sheetname_)
        print("data ", data_[-10:])
    except Exception as e:
        print("read xlsx file error")
        traceback.print_stack()
        print("error ", e)
        info = traceback.format_exc()
        send_email(ContextInfo, info, e)
        return pd.DataFrame()

    if data_.empty:
        return data_
    data_['GPDM'] = format_series_jq_to_xt_series(data_['GPDM'])
    data_.index = data_['GPDM']
    return data_


# series 的股票代码转换成讯投格式的股票代码
def format_series_jq_to_xt_series(series):
    return pd.Series({x: format_jq_stockcode_to_xt(series[x]) for x in series.index})


# 把聚宽格式的股票代码转换成讯投
def format_jq_stockcode_to_xt(stock):
    if stock.startswith("6"):
        stock = stock[:6] + ".SH"
    elif stock.startswith("0") or stock.startswith("3"):
        stock = stock[:6] + ".SZ"
    return stock
