
def get_holdings(ContextInfo, get_trade_detail_data):
    """
    获得持仓信息
    m_nCanUseVolume: 可用余额，可用持仓，期货不用这个字段，股票的可用数量
    m_nVolume: 当前拥股，持仓量
    m_dOpenPrice: 持仓成本
    m_dMarketValue: 市值，合约价值
    m_strInstrumentName:证券名称
    m_bIsToday: 是否今仓
    m_nYesterdayVolume: 昨夜拥股，期货不用这个字段，股票的股份余额
    m_strOpenDate: 成交日期
    """
    holding_info = {}
    result_list = get_trade_detail_data(ContextInfo.accID, ContextInfo.datatype, "POSITION")
    if result_list:
        obj = result_list[0]
        holding_info[obj.m_strInstrumentID + "." + obj.m_strExchangeID] = {"m_nVolume": obj.m_nVolume,
                                                                              "avg_cost": obj.m_dOpenPrice,
                                                                              "m_nYesterdayVolume": obj.m_nYesterdayVolume,
                                                                              "market_value": obj.m_dMarketValue,
                                                                              "m_bIsToday": obj.m_bIsToday,
                                                                              "m_nCanUseVolume": obj.m_nCanUseVolume,
                                                                              "m_strOpenDate": obj.m_strOpenDate}
    return holding_info


def get_ref_holding(ContextInfo, get_trade_detail_data):
    """
    获取昨天的持仓股票信息
    :param get_trade_detail_data:
    :param ContextInfo:
    :return:
    """
    holding_info = get_holdings(ContextInfo, get_trade_detail_data)
    holding_list = list(holding_info.keys())

    return {stock: holding_info[stock] for stock in holding_list if int(holding_info[stock]['m_nYesterdayVolume']) > 0}

