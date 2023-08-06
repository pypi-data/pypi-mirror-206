
def get_account(ContextInfo, get_trade_detail_data):
    account_info = {}
    result_list = get_trade_detail_data(ContextInfo.accID, ContextInfo.datatype, "ACCOUNT")
    if result_list:
        obj = result_list[0]
        account_info['m_dAvailable'] = obj.m_dAvailable
        account_info['m_dBalance'] = obj.m_dBalance
    return account_info
