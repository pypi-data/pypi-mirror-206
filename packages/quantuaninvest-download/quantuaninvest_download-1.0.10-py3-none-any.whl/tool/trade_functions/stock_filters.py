import current_data
from position import get_holdings
from tool.trade_functions.account import get_account

"""
只保留 3 或者 6 或者 0 开头的股票
"""


def startswith_3_6_0_filter(ContextInfo, stock_list):
    cond_list = []
    for stock in stock_list:
        if stock.startswith("3") or stock.startswith("6") or stock.startswith("0"):
            cond_list.append(stock)
    return cond_list


'''
过滤掉有跌停的股票
'''


def dt_filter(ContextInfo, stock_list, _timetag_to_datetime_):
    cond_list = []
    print("dt_filter ", stock_list)
    for stock in stock_list:
        curent_stock_data = current_data.get_current_data(ContextInfo, stock, _timetag_to_datetime_)
        if not curent_stock_data.empty:
            last_price = curent_stock_data['close'].values[0]
            low_limit = current_data.get_low_limit_price(ContextInfo, stock, _timetag_to_datetime_)
            if last_price != low_limit:
                cond_list.append(stock)

    return cond_list


def can_sell_num_filter(ContextInfo, stock_list, get_trade_detail_data):
    """
    要卖出的股票必须在持仓中，并且可卖出数量大于零,
    卖券还款不做判断，信用账户股票可卖，可以选择卖券还款方式


    """
    cond_list = []
    holding_info = get_holdings(ContextInfo.accID, ContextInfo.datatype, get_trade_detail_data)
    holding_stock = list(holding_info.keys())
    for stock in stock_list:
        if stock in holding_stock:
            if holding_info[stock]['m_nCanUseVolume'] > 0:
                cond_list.append(stock)

    return cond_list


def new_stock_filter(ContextInfo, stock_list):
    return [x for x in stock_list if x not in ContextInfo.new_stock_list]


def before_sell_filter(ContextInfo, stock_list):
    stock_list = new_stock_filter(ContextInfo, stock_list)
    stock_list = dt_filter(ContextInfo, stock_list)
    stock_list = can_sell_num_filter(ContextInfo, stock_list)
    stock_list = startswith_3_6_0_filter(ContextInfo, stock_list)
    return stock_list


def before_buy_filter(ContextInfo, stock_list):
    """
    买入前过滤
    :param ContextInfo:
    :param stock_list: 过滤前股票池
    :return: 过滤后的股票池
    """
    # 过滤涨停
    stock_list = zt_filter(ContextInfo, stock_list)
    print("zt_filter ", zt_filter)
    # 过滤 688 开头的股票
    if not ContextInfo.test:
        stock_list = not_startswith_688_filter(stock_list)
    # 过滤到持仓超过ratio的股票
    stock_list = holding_amo_ratio_filter(ContextInfo, stock_list)
    print("holding_amo_ratio_filter ", stock_list)

    # 过滤掉停牌的股票
    stock_list = tp_filter(ContextInfo, stock_list)
    print("tp_filter ", stock_list)

    return stock_list


def zt_filter(ContextInfo, stock_list):
    """
    过滤掉有涨停的股票
    """
    cond_list = []
    print("zt_filter ", stock_list)
    for stock in stock_list:
        curent_stock_data = current_data.get_current_data(ContextInfo, stock)
        if not curent_stock_data.empty:
            last_price = curent_stock_data['close'].values[0]
            high_limit = current_data.get_high_limit_price(ContextInfo, stock)
            if last_price != high_limit:
                cond_list.append(stock)

    return cond_list


def not_startswith_688_filter(stock_list):
    """

    :param stock_list: 股票代码列表
    :return: 非688开头的股票列表
    """
    return [x for x in stock_list if not x.startswith("688")]


def tp_filter(ContextInfo, stock_list):
    """
    当前交易日没有停牌的股票列表
    :param ContextInfo:
    :param stock_list:
    :return:
    """
    return [x for x in stock_list if not ContextInfo.is_suspended_stock(x)]


def holding_amo_ratio_filter(ContextInfo, stock_list, get_trade_detail_data):
    """
    持仓市值超过总资产 * ratio 的股票剔除掉，保持买入前持仓股的市值不超过 总资产 * ratio
    :param get_trade_detail_data:
    :param ContextInfo:
    :param stock_list:
    :return:
    """
    holding_info = get_holdings(ContextInfo.accID, ContextInfo.datatype)
    holding_stock = list(holding_info.keys())
    account_info = get_account(ContextInfo, get_trade_detail_data)
    total_value = account_info['m_dBalance']
    amo_limit = total_value * ContextInfo.holding_amo_ratio_limit
    print("amo_limit ", amo_limit)
    print("stock_list ", stock_list)
    print("holding_stock ", holding_stock)
    print("holding_info ", holding_info)
    cond_list = []
    for stock in stock_list:
        if stock not in holding_stock:
            cond_list.append(stock)
        else:
            print("holding_info[stock]['market_value'] < amo_limit", holding_info[stock]['market_value'] < amo_limit,
                  holding_info[stock]['market_value'], amo_limit)
            if holding_info[stock]['market_value'] < amo_limit:
                print("stock ", stock, holding_info[stock]['market_value'])
                cond_list.append(stock)
    return cond_list
