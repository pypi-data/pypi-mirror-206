from tool.get_data import get_current_data
from tool.trade_functions.position import get_holdings


def algo_trade_s_num(ContextInfo, stock, s_num, opType, prType, buy_record, sell_type,
                     dbp_holding_stock_sell_max_amout_map, algo_passorder):
    print("================= algo_trade rz start ===============")
    s_num = int(s_num)
    order_num = s_num
    userparam = generate_algo_order_user_param_by_s_num(ContextInfo, stock, s_num)
    m_strRemark = get_sell_remark_info(ContextInfo, stock, sell_type, buy_record)

    if ContextInfo.test:
        if opType == 24:
            print(opType, 1101, ContextInfo.accID, stock, prType, -1, s_num, 'pt3', 1, m_strRemark, userparam,
                  ContextInfo,
                  type(opType), 1101, type(ContextInfo.accID), type(stock), type(prType), -1,
                  type(s_num), 'pt3', 1, type(m_strRemark), type(userparam), type(ContextInfo))
            m_strRemark = "remark"
            holding_info = get_holdings(ContextInfo.accID, ContextInfo.datatype)
            m_nCanUseVolume = holding_info[stock]['m_nCanUseVolume']

            print("stock s_num m_nCanUseVolume ", stock, s_num, m_nCanUseVolume)
            assert s_num <= m_nCanUseVolume

            algo_passorder(opType, 1101, ContextInfo.accID, stock, prType, -1, s_num, 'pt3', 1, m_strRemark, userparam,
                           ContextInfo)
            print("信用账户 算法下单  %s ,操作类型 %s 下单数量 %s" % (stock, str(opType), str(s_num)))

            return

    if opType == 34:
        print("do dbp selling ", stock)
        # 获得可以担保品卖出的数量
        dbp_sell_info = dbp_holding_stock_sell_max_amout_map['data']
        # todo  去掉测试时候的注释
        if stock not in dbp_sell_info.keys():
            print(stock, "not in dbp_sell_info")
            return
        else:
            dbp_mqhk_num = dbp_sell_info[stock]
            if dbp_mqhk_num <= 0:
                return
            else:
                order_num = dbp_mqhk_num

    algo_passorder(opType, 1101, ContextInfo.accID, stock, prType, -1, order_num, 'pt3', 1,
                   m_strRemark, userparam, ContextInfo)
    print("信用账户 算法下单  %s ,操作类型 %s 下单数量 %s" % (stock, str(opType), str(order_num)))

    print("================= algo_trade rz start ===============")


def get_sell_remark_info(ContextInfo, stock_code, type_, buy_remark):
    return str(stock_code + "|" + buy_remark + "|" + type_)


# 根据买入、卖出类型生成算法下单的user_param
def generate_algo_order_user_param_s(ContextInfo, stock, ratio, get_trade_detail_data):
    # userparam={"OrderType":1,"MaxOrderCount":1,'PlaceOrderInterval':15,"SingleNumMax":1000000,"SingleNumMin":100000}
    # 获得持仓信息
    holding_info = get_holdings(ContextInfo, get_trade_detail_data)
    # 获得股票的持仓市值
    total_market_value = holding_info[stock]['market_value']
    # 卖出下单金额
    order_value = total_market_value * (1 - ratio)

    # 计算总下单次数
    MaxOrderCount_ = calculate_order_count(ContextInfo, stock, order_value)
    # 设置下单间隔
    PlaceOrderInterval_ = ContextInfo.PlaceOrderInterval_limit
    # 设置最大拆单下单的股票数量
    num = calculate_SingleNumMax(ContextInfo, stock, order_value, 'S')

    SingleNumMax_ = SingleNumMin_ = num

    return {"OrderType": 1, "MaxOrderCount": MaxOrderCount_, "PlaceOrderInterval": PlaceOrderInterval_,
            "SingleNumMax": SingleNumMax_, "SingleNumMin": SingleNumMin_}


# 根据买入、卖出类型生成算法下单的user_param
def generate_algo_order_user_param_by_s_num(ContextInfo, stock, s_num):
    # 计算总下单次数
    MaxOrderCount_ = int(calculate_order_count_s_num(ContextInfo, stock, s_num))
    # 设置下单间隔
    PlaceOrderInterval_ = ContextInfo.PlaceOrderInterval_limit
    # 设置最大拆单下单的股票数量
    num = int(calculate_SingleNumMax_s_num(ContextInfo, stock, s_num, 'S'))

    SingleNumMax_ = SingleNumMin_ = num

    return {"OrderType": 1, "MaxOrderCount": MaxOrderCount_, "PlaceOrderInterval": PlaceOrderInterval_,
            "SingleNumMax": SingleNumMax_, "SingleNumMin": SingleNumMin_}


# 根据买入、卖出类型生成算法下单的user_param
def generate_algo_order_user_param_b(ContextInfo, stock, order_value, _timetag_to_datetime_):
    # 计算总下单次数
    MaxOrderCount_ = calculate_order_count(ContextInfo, stock, order_value)
    # 设置下单间隔
    PlaceOrderInterval_ = ContextInfo.PlaceOrderInterval_limit
    # 设置最大拆单下单的股票数量
    SingleNumMax_ = SingleNumMin_ = calculate_SingleNumMax(ContextInfo, stock, order_value, 'B', _timetag_to_datetime_)

    return {"OrderType": 1, "MaxOrderCount": MaxOrderCount_, "PlaceOrderInterval": PlaceOrderInterval_,
            "SingleNumMax": SingleNumMax_, "SingleNumMin": SingleNumMin_}


# 计算下单的总次数；下单总次数 = round(下单金额/下单拆单阈值,0)，包括失败的委托
def calculate_order_count(ContextInfo, stock, order_value):
    # 如果下单金额小于阈值，最小下单次数调整为20，考虑到废单重新委托
    if order_value < ContextInfo.split_stock_limit_value:
        return 20
    # 下单金额 拆算成单数 加上 20 ，考虑到废单重新委托
    return int(round(order_value / ContextInfo.split_stock_limit_value, 0) + 20)


# 计算下单的总次数；下单总次数 = round(下单金额/下单拆单阈值,0)，包括失败的委托
def calculate_order_count_s_num(ContextInfo, stock, s_num):
    # 如果下单金额小于阈值，最小下单次数调整为20，考虑到废单重新委托
    current_data = get_current_data(ContextInfo, stock)
    last_price = current_data['close'].values[0]
    order_value = s_num * last_price
    if order_value < ContextInfo.split_stock_limit_value:
        return 20
    # 下单金额 拆算成单数 加上 20 ，考虑到废单重新委托
    return int(round(order_value / ContextInfo.split_stock_limit_value, 0) + 20)


# 按照股票的价值进行拆单
def calculate_SingleNumMax(ContextInfo, stock, order_value, buy_or_sell, _timetag_to_datetime_):
    last_price = get_current_data(ContextInfo, stock, _timetag_to_datetime_)['close'].values[0]
    # 实际可用的下单价值
    order_value_ = 0

    # 除去买入、卖出的手续费
    if buy_or_sell == "B":

        order_value_ = order_value / ContextInfo.buy_stock_sxf
        if order_value_ > ContextInfo.split_stock_limit_value:
            order_value_ = ContextInfo.split_stock_limit_value

    elif buy_or_sell == "S":
        order_value_ = order_value / ContextInfo.sell_stock_sxf
        if order_value_ <= ContextInfo.split_stock_limit_value:
            # 不需要拆单
            # 获得当前股票的所有持仓
            holding_info = get_holdings(ContextInfo.accID, ContextInfo.datatype)
            m_nCanUseVolume = holding_info[stock]['m_nCanUseVolume']
            return m_nCanUseVolume

    num = int(int(order_value_ / last_price / 100) * 100)
    return num


# 按照股票的价值进行拆单
def calculate_SingleNumMax_s_num(ContextInfo, stock, s_num, buy_or_sell):
    last_price = get_current_data(ContextInfo, stock)['close'].values[0]
    # 实际可用的下单价值
    order_value_ = s_num * last_price

    # 除去买入、卖出的手续费

    order_value_ = order_value_ / ContextInfo.sell_stock_sxf
    if order_value_ <= ContextInfo.split_stock_limit_value:
        # 不需要拆单
        # 获得当前股票的所有持仓
        holding_info = get_holdings(ContextInfo.accID, ContextInfo.datatype)
        m_nCanUseVolume = holding_info[stock]['m_nCanUseVolume']
        return m_nCanUseVolume
    else:
        order_value_ = ContextInfo.split_stock_limit_value
    num = int(int(order_value_ / last_price / 100) * 100)
    return num


def allocate_fund_between_min_amo_and_capital_unit(ContextInfo, stock_list, rz_money_left, rz_capital_uint, rz_min_amo):
    """

    :param ContextInfo:
    :param stock_list:
    :param rz_money_left:
    :param rz_capital_uint:
    :param rz_min_amo:
    :return:
    """
    if rz_capital_uint < rz_min_amo:
        return {}

    rz_buy_map = {}

    # 分配每个股票的买入资金
    for stock in stock_list:
        if rz_money_left >= rz_capital_uint:
            rz_buy_map[stock] = rz_capital_uint
            rz_money_left -= rz_capital_uint

        else:
            if rz_money_left > rz_min_amo:
                rz_buy_map[stock] = rz_money_left
                rz_money_left = 0
        if rz_money_left == 0:
            break
        print("rz_money_left   %s", rz_money_left)
    print("rz_buy_map   %s", rz_buy_map)

    return rz_buy_map
