import datetime as dt


# 获得当前时间
def get_current_time(ContextInfo, _timetag_to_datetime_):
    # 日线级别运行第一个时间是 00:00:00
    # 获得当前运行的bar
    index = ContextInfo.barpos
    # 获得bar对应的时间戳
    realtimetag = ContextInfo.get_bar_timetag(index)
    # 将时间戳转换为指定格式字符串
    current_time = _timetag_to_datetime_(realtimetag, ContextInfo.YmdHMS)
    print(_timetag_to_datetime_(realtimetag, '%Y%m%d %H:%M:%S'))
    if current_time == '19700101080000':
        return dt.datetime.now().strftime(ContextInfo.YmdHMS)
    return _timetag_to_datetime_(realtimetag, ContextInfo.YmdHMS)


# 获得当前股票的最新价格，获得当前的价格，和周期相关，默认周期是日线，获得的是日线级别数据，默认的是分钟，获得的是分钟级别的数据
# 9点30分在回测时，一分钟数据不能获得，在9点31分的时候，可用获得1分钟数据
def get_current_data(ContextInfo, stock, _timetag_to_datetime_):
    # 获得最新bar对应的时间
    current_time = get_current_time(ContextInfo, _timetag_to_datetime_)
    # 获得股票对应时间的k线数据
    data = ContextInfo.get_market_data_ex(fields=['open', 'close', 'high', 'low'], stock_code=[stock], period='follow',
                                          end_time=current_time, count=1,
                                          dividend_type='follow', fill_data=True, subscribe=True)
    return data[stock]


# 获得股票的涨停价
def get_high_limit_price(ContextInfo, stock):
    # 获得上一个交易日的涨停价
    data = ContextInfo.get_market_data_ex(fields=['open', 'close', 'high', 'low'], stock_code=[stock], period='follow',
                                          end_time=ContextInfo.previous_date, count=1,
                                          dividend_type='follow', fill_data=True, subscribe=True)
    # print("data[stock]   %s", data[stock])
    if not data[stock].empty:
        stock_name = ContextInfo.get_stock_name(stock)
        pre_close = data[stock]['close'].values[0]
        if stock.startswith("3") or stock.startswith("688"):  # 创业板或者科创板 20% 涨幅
            return round(pre_close * 1.2, 2)
        elif 'ST' in stock_name:  # ST 五个点涨幅
            return round(pre_close * 1.05, 2)
        return round(pre_close * 1.1, 2)


# 获得股票的涨停价
def get_low_limit_price(ContextInfo, stock):
    # 获得上一个交易日的涨停价
    data = ContextInfo.get_market_data_ex(fields=['open', 'close', 'high', 'low'], stock_code=[stock], period='follow',
                                          end_time=ContextInfo.previous_date, count=1,
                                          dividend_type='follow', fill_data=True, subscribe=True)
    if not data[stock].empty:
        stock_name = ContextInfo.get_stock_name(stock)
        pre_close = data[stock]['close'].values[0]
        if stock.startswith("3") or stock.startswith("688"):
            return round(pre_close * 0.8, 2)
        elif 'ST' in stock_name:
            return round(pre_close * 0.95, 2)
        return round(pre_close * 0.9, 2)


def get_current_data_local(ContextInfo, stock):
    end_time = get_current_time(ContextInfo)
    dict_stock = ContextInfo.get_local_data(stock_code=stock, end_time=end_time, period='5m', divid_type='none', count=1)
    return dict_stock
