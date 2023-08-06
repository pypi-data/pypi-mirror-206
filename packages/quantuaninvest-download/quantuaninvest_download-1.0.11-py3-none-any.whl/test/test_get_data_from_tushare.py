import datetime as dt
import tushare as ts
# 从tushare 获得交易日历信息
def get_trade_days_from_tushare():
	today = dt.datetime.now().strftime("%Y%m%d")[:8]
	# 初始化pro接口
	pro = ts.pro_api('5967bbdd6afcd6f0e4b8e89ca0371facf76f323b1e98b5a417b30cf9')

	# 拉取数据
	df = pro.trade_cal(**{
		"exchange": "",
		"cal_date": today,
		"start_date": "",
		"end_date": "",
		"is_open": "",
		"limit": "",
		"offset": ""
	}, fields=[
		"exchange",
		"cal_date",
		"is_open",
		"pretrade_date"
	])
	return df

df = get_trade_days_from_tushare()
print(df)