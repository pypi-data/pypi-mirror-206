from enum import Enum


class enum_holding_type(Enum):
    DBP = 1  # 担保品持仓类型
    RZ = 2  # 融资持仓类型
    NORMAL = 3  # 普通账户


class enum_trade_type(Enum):
    B = 1  # 买入类型
    S = 2  # 卖出类型


class enum_EOffset_Flag_Type(Enum):  # 操作类型

    EOFF_THOST_FTDC_OF_INVALID = -1
    EOFF_THOST_FTDC_OF_Open = 48  # 买入，开仓
    EOFF_THOST_FTDC_OF_Close = 49  # 卖出，平仓
    EOFF_THOST_FTDC_OF_ForceClose = 50  # 强平
    EOFF_THOST_FTDC_OF_CloseToday = 51  # 平今
    EOFF_THOST_FTDC_OF_CloseYesterday = 52  # 平昨
    EOFF_THOST_FTDC_OF_ForceOff = 53  # 强减
    EOFF_THOST_FTDC_OF_LocalForceClose = 54  # 本地强平
    EOFF_THOST_FTDC_OF_PLEDGE_IN = 81  # 质押入库
    EOFF_THOST_FTDC_OF_PLEDGE_OUT = 66  # 质押出库
    EOFF_THOST_FTDC_OF_ALLOTMENT = 67  # 股票配股


class enum_EEntrustBS(Enum):
    """
    买卖方向
    """
    ENTRUST_BUY = 48  # // 买入，多
    ENTRUST_SELL = 49  # // 卖出，空
    ENTRUST_PLEDGE_IN3 = 81  # // 质押入库
    ENTRUST_PLEDGE_OUT = 66  # // 质押出库


class enum_EEntrustTypes(Enum):
    """
    委托类型
    """

    ENTRUST_BUY_SELL = 48  # 买卖
    ENTRUST_QUERY = 49  # 查询
    ENTRUST_CANCE = 50  # 撤单
    ENTRUST_APPEND = 51  # 补单
    ENTRUST_COMFIRM = 52  # 确认
    ENTRUST_BIG = 53  # 大宗
    ENTRUST_FIN = 54  # 融资委托
    ENTRUST_SLO = 55  # 融券委托
    ENTRUST_CLOSE = 56  # 信用平仓
    ENTRUST_CREDIT_NORMAL = 57  # 信用普通委托
    ENTRUST_CANCEL_OPEN = 58  # 撤单补单
    ENTRUST_TYPE_OPTION_EXERCISE = 59  # 行权
    ENTRUST_TYPE_OPTION_SECU_LOCK = 60  # 锁定
    ENTRUST_TYPE_OPTION_SECU_UNLOCK = 61  # 解锁
    ENTRUST_QUOTATION_REPURCHASE = 62  # 报价回购
    ENTRUST_TYPE_OPTION_ABANDON = 63  # 放弃行权
    ENTRUST_AGREEMENT_REPURCHASE = 64  # 协议回购
    ENTRUST_TYPE_OPTION_COMB_EXERCISE = 65  # 组合行权
    ENTRUST_TYPE_OPTION_BUILD_COMB_STRATEGY = 66  # 构建组合策略持仓
    ENTRUST_TYPE_OPTION_RELEASE_COMB_STRATEGY = 67  # 解除组合策略持仓
    ENTRUST_TYPE_LMT_LOAN = 68  # 转融通出借
    ENTRUST_TYPE_LMT_LOAN_DEFER = 69  # 转融通出借展期
    ENTRUST_TYPE_LMT_LOAN_FINISH_AHEAD = 70  # 转融通出借提前了结
    ENTRUST_CROSS_MARKET_IN = 71  # 跨市场场内
    ENTRUST_CROSS_MARKET_OUT = 72  # 跨市场场外


# 用于判断成交的类型
class enum_m_strOptName(Enum):
    DBPMR = '担保品买入'
    DBPMC = '担保品卖出'
    RZMR = '融资买入'
    MQHK = '卖券还款'
    PTMR = '普通买入'
    PTMC = '普通卖出'


class enum_error(Enum):
    WRONG_ORDER = '错误委托'
    RUNNING_ERROR = '运行错误'
    TASK_ERROR = '任务失败'


class enum_notice_info(Enum):
    DBP_FIRM_BARGAIN = '担保品实盘交易'
    RZ_FIRM_BARGAIN = '融资实盘交易'
