
class deal:
    m_strExchangeID = ""  #: 证券市场，交易所代码
    m_strExchangeName = ""  # : 交易市场，交易所名称
    m_strProductID = ""  # : 品种代码
    m_strProductName = ""  # : 品种名称
    m_strInstrumentID = ""  # : 证券代码
    m_strInstrumentName = ""  # : 证券名称
    m_strTradeID = ""  # : 成交编号
    m_nTaskId = 0  # ：任务号
    m_strOrderRef = ""  # : 下单引用，等于股票的内部委托号
    m_strOrderSysID = ""  # : 合同编号，报单编号，委托号
    m_nDirection = 0  #: EEntrustBS，买卖方向
    m_nOffsetFlag = 0  #: EOffset_Flag_Type，开平，股票的买卖
    m_nHedgeFlag = 0  #: EHedge_Flag_Type，投保，股票不需要
    m_dPrice = 0  #: 成交均价
    m_nVolume = 0  #: 成交量，期货单位手，股票做到股
    m_strTradeDate = ""  # : 成交日期
    m_strTradeTime = ""  # : 成交时间
    m_dComssion = 0  #: 手续费
    m_dTradeAmount = 0  #: 成交额，期货 = 均价 * 量 * 合约乘数
    m_nOrderPriceType = 0  #: EBrokerPriceType 类型，例如市价单、限价单
    m_strOptName = ""  # ：买卖标记，展示委托属性的中文
    m_eEntrustType = 0  # : EEntrustTypes 类型，委托类别
    m_eFutureTradeType = 0  #: EFutureTradeType 类型，成交类型
    m_nRealOffsetFlag = 0  # : EOffset_Flag_Type 类型，实际开平，主要是区分平今和平昨
    m_eCoveredFlag = 0  #: ECoveredFlag类型，备兑标记 '0' - 非备兑，'1' - 备兑
    m_nCloseTodayVolume = 0  #: 平今量，不显示
    m_dOrderPriceRMB = 0  #: 委托价格（人民币），目前用于港股通
    m_dPriceRMB = 0  #: 成交价格（人民币），目前用于港股通
    m_dTradeAmountRMB = 0  # ：成交金额（人民币），目前用于港股通
    m_dReferenceRate = 0  #: 汇率，目前用于港股通
    m_strXTTrade = ""  # : 是否是迅投交易
    m_strCompactNo = ""  # : 合约编号
    m_dCloseProfit = 0  #: 平仓盈亏 ，目前用于外盘
    m_strRemark = ""  # ：投资备注

    deal_name_list = ["m_strExchangeID",  # 证券市场，交易所代码
                      "m_strExchangeName",  # 交易市场，交易所名称
                      "m_strProductID",  # 品种代码
                      "m_strProductName",  # 品种名称
                      "m_strInstrumentID",  # 证券代码
                      "m_strInstrumentName",  # 证券名称
                      "m_strTradeID",  # 成交编号
                      "m_nTaskId",  # 任务号
                      "m_strOrderRef",  # 下单引用，等于股票的内部委托号
                      "m_strOrderSysID",  # 合同编号，报单编号，委托号
                      "m_nDirection",  # EEntrustBS，买卖方向
                      "m_nOffsetFlag",  # EOffset_Flag_Type，开平，股票的买卖
                      "m_nHedgeFlag",  # EHedge_Flag_Type，投保，股票不需要
                      "m_dPrice",  # 成交均价
                      "m_nVolume",  # 成交量，期货单位手，股票做到股
                      "m_strTradeDate",  # 成交日期
                      "m_strTradeTime",  # 成交时间
                      "m_dComssion",  # 手续费
                      "m_dTradeAmount",  # 成交额，期货 = 均价 * 量 * 合约乘数
                      "m_nOrderPriceType",  # EBrokerPriceType 类型，例如市价单、限价单
                      "m_strOptName",  # 买卖标记，展示委托属性的中文
                      "m_eEntrustType",  # EEntrustTypes 类型，委托类别
                      "m_eFutureTradeType",  # EFutureTradeType 类型，成交类型
                      "m_nRealOffsetFlag",  # EOffset_Flag_Type 类型，实际开平，主要是区分平今和平昨
                      "m_eCoveredFlag",  # ECoveredFlag类型，备兑标记 '0' - 非备兑，'1' - 备兑
                      "m_nCloseTodayVolume",  # 平今量，不显示
                      "m_dOrderPriceRMB",  # 委托价格（人民币），目前用于港股通
                      "m_dPriceRMB",  # 成交价格（人民币），目前用于港股通
                      "m_dTradeAmountRMB",  # 成交金额（人民币），目前用于港股通
                      "m_dReferenceRate",  # 汇率，目前用于港股通
                      "m_strXTTrade",  # 是否是迅投交易
                      "m_strCompactNo",  # 合约编号
                      "m_dCloseProfit",  # 平仓盈亏 ，目前用于外盘
                      "m_strRemark"]  # 投资备注

    def __str__(self):
        return " 股票代码 %s.%s 持仓量 %d 成交价格 %f 当前交易日 %s" % (
            self.m_strInstrumentID, self.m_strExchangeID, self.m_nVolume, self.m_dPrice, self.m_strTradeDate)

