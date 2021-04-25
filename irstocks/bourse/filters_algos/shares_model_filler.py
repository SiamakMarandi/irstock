import json
import requests
from bourse.models import Shares_Specifications
import logging

def filler(token):
    logging.basicConfig(level=logging.DEBUG, filename="baseline.log")
    logger = logging.getLogger(' ')
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    name = []
    arr_arr = []
    rsi = []
    mfi = []
    cci = []
    highest_price = []        
    volume = []  
    # api_req =  requests.get("https://sourcearena.ir/api/?token=36f3d0f1d4ea646bc316b380375a3c33&all&type=0")
    # api_arr = json.loads(api_req.content)
    # for name in api_arr:
    #     arr_arr.append(name["name"])
    
    Shares_Specifications.objects.all().delete()
    api_request =  requests.get("https://sourcearena.ir/api/?token="+ token +"&all&type=0")
    api_shares = json.loads(api_request.content)

    for share in api_shares:
        try:
            # ###################### all
            share_indicator = Shares_Specifications()
            share_indicator.NAME = share["name"]
            share_indicator.INSTANCE_CODE = share["instance_code"]
            share_indicator.FULL_NAME = share["full_name"]
            share_indicator.FIRST_PRICE = share["first_price"]
            share_indicator.CLOSE_PRICE = share["close_price"]
            share_indicator.CLOSE_PRICE_CHANGE = share["close_price_change"]
            share_indicator.CLOSE_PRICE_CHANGE_PERCENT = share["close_price_change_percent"]
            share_indicator.FINAL_PRICE = share["final_price"]
            share_indicator.FINAL_PRICE_CHANGE = share["final_price_change"]
            share_indicator.FINAL_PRICE_CHANGE_PERCENT = share["final_price_change_percent"]
            share_indicator.HIGHEST_PRICE = share["highest_price"]
            share_indicator.LOWEST_PRICE = share["lowest_price"]
            share_indicator.EPS = share["eps"]
            share_indicator.PE = share["P:E"]
            share_indicator.SELL_COUNT_1 = share["1_sell_count"]
            share_indicator.SELL_COUNT_2 = share["2_sell_count"]
            share_indicator.SELL_COUNT_3 = share["3_sell_count"]
            share_indicator.SELL_VOLUME_1 = share["1_sell_volume"]
            share_indicator.SELL_VOLUME_2 = share["2_sell_volume"]
            share_indicator.SELL_VOLUME_3 = share["3_sell_volume"]
            share_indicator.SELL_PRICE_1 = share["1_sell_price"]
            share_indicator.SELL_PRICE_2 = share["2_sell_price"]
            share_indicator.SELL_PRICE_3 = share["3_sell_price"]
            share_indicator.BUY_COUNT_1 = share["1_buy_count"]
            share_indicator.BUY_COUNT_2 = share["2_buy_count"]
            share_indicator.BUY_COUNT_3 = share["3_buy_count"]
            share_indicator.BUY_VOLUME_1 = share["1_buy_volume"]
            share_indicator.BUY_VOLUME_2 = share["2_buy_volume"]
            share_indicator.BUY_VOLUME_3 = share["3_buy_volume"]
            share_indicator.BUY_PRICE_1 = share["1_buy_price"]
            share_indicator.BUY_PRICE_2 = share["2_buy_price"]
            share_indicator.BUY_PRICE_3 = share["3_buy_price"]
            share_indicator.CO_BUY_COUNT = share["co_buy_count"]
            share_indicator.REAL_BUY_COUNT = share["real_buy_count"]
            share_indicator.REAL_SELL_COUNT = share["real_sell_count"]
            share_indicator.CO_SELL_COUNT = share["co_sell_count"]
            share_indicator.REAL_BUY_VOLUME = share["real_buy_volume"]
            share_indicator.CO_BUY_VOLUME = share["co_buy_volume"]
            share_indicator.REAL_SELL_VOLUME = share["real_sell_volume"]
            share_indicator.CO_SELL_VOLUME = share["co_sell_volume"]
            share_indicator.REAL_BUY_VALUE = share["real_buy_value"]
            share_indicator.CO_BUY_VALUE = share["co_buy_value"]
            share_indicator.REAL_SELL_VALUE = share["real_sell_value"]
            share_indicator.CO_SELL_VALUE = share["co_sell_value"]
            share_indicator.TRADE_NUMBER = share["trade_number"]
            share_indicator.TRADE_VOLUME = share["trade_volume"]
            share_indicator.TRADE_VALUE = share["trade_value"]
            share_indicator.ALL_STOCKS = share["all_stocks"]
            share_indicator.BASIS_VOLUME = share["basis_volume"]
            name = share["name"]
            # ###################### symbol
            api_request = requests.get("https://sourcearena.ir/api/?token="+ token +"&name="+ name)                        
            api_symbol = json.loads(api_request.content) 
            share_indicator.TYPE = api_symbol["type"]
            # ############################## Stats
            api_request = requests.get("http://sourcearena.ir/api/?token="+ token +"&stats="+ name)                        
            api_stats = json.loads(api_request.content) 
            share_indicator.N_DAY_3M = api_stats["n_day_3m"]
            share_indicator.N_DAY_12M = api_stats["n_day_12m"]
            share_indicator.N_PERCENT_12M = api_stats["n_percent_12m"]
            share_indicator.N_RANK_3M = api_stats["n_rank_3m"]
            share_indicator.N_RANK_12M = api_stats["n_rank_12m"]
            share_indicator.P_DAY_3M = api_stats["p_day_3m"]
            share_indicator.P_DAY_12M = api_stats["p_day_12m"]            
            share_indicator.P_PERCENT_12M = api_stats["p_percent_12m"]
            share_indicator.P_RANK_3M = api_stats["p_rank_3m"]
            share_indicator.P_RANK_12M = api_stats["p_rank_12m"]
            share_indicator.TRADE_NDAY_3M = api_stats["trade_nday_3m"]
            share_indicator.TRADE_NDAY_12M = api_stats["trade_nday_12m"]
            share_indicator.TRADE_DAY_3M = api_stats["trade_day_3m"]
            share_indicator.TRADE_DAY_12M = api_stats["trade_day_12m"]
            share_indicator.TRADE_RANK_3M = api_stats["trade_rank_3m"]
            share_indicator.TRADE_RANK_12M = api_stats["trade_rank_12m"]
            share_indicator.TN_AVERAGE_3M = api_stats["tn_average_3m"]
            share_indicator.TN_AVERAGE_12M = api_stats["tn_average_12m"]
            share_indicator.TN_RANK_3M = api_stats["tn_rank_3m"]
            share_indicator.TN_RANK_12M = api_stats["tn_rank_12m"]
            share_indicator.TN_LAST_DAY = api_stats["tn_last_day"]  
            share_indicator.TVAL_AVERAGE_3M = api_stats["tval_average_3m"]
            share_indicator.TVAL_AVERAGE_12M = api_stats["tval_average_12m"]
            share_indicator.TVAL_RANK_3M = api_stats["tval_rank_3m"]
            share_indicator.TVAL_RANK_12M = api_stats["tval_rank_12m"]
            share_indicator.TVAL_LAST_DAY = api_stats["tval_last_day"]

            # ###################### indicators
            api_request = requests.get("http://sourcearena.ir/api/?token="+ token +"&all_indicators&name="+ name)
            api_indicator = json.loads(api_request.content) 

            # share_indicator.ADX = int(float(api_indicator["adx_14"]))
            if api_indicator["adx_14"]:
                share_indicator.ADX = api_indicator["adx_14"]
            if api_indicator["rsi_14"]:    
                share_indicator.RSI = int(float(api_indicator["rsi_14"])) 
            if api_indicator["cci_14"]: 
                share_indicator.CCI = int(float(api_indicator["cci_14"]))
            if api_indicator["so_14"]["k_value"]:  
                share_indicator.STOCHASTIC_VALUE = int(float(api_indicator["so_14"]["k_value"]))
            if api_indicator["so_14"]["d_value"]: 
                share_indicator.STOCHASTIC_SIGNAL = int(float(api_indicator["so_14"]["d_value"]))
            if api_indicator["mfi_14"]:
                share_indicator.MFI = int(float(api_indicator["mfi_14"]))        
            if api_indicator["macd_26"]["macd_value"]:
                share_indicator.MACD_VALUE = int(float(api_indicator["macd_26"]["macd_value"]))
            if api_indicator["macd_26"]["macd_signal_value"]:
                share_indicator.MACD_SIGNAL = int(float(api_indicator["macd_26"]["macd_signal_value"])) 
            if api_indicator["bb_20"]["upper"]:
                share_indicator.BOLLINGER_UPPERBAND = int(float(api_indicator["bb_20"]["upper"]))        
            if api_indicator["bb_20"]["lower"]:
                share_indicator.BOLLINGER_LOWERBAND = int(float(api_indicator["bb_20"]["lower"]))  
            if api_indicator["stoch_rsi_14"]:
                share_indicator.STOCHASTIC_RSI = int(float(api_indicator["stoch_rsi_14"])) 
            if api_indicator["ichimoku_9_26_52_26"]["tenken_sen_value"]:
                share_indicator.ICHIMOKU_TENKEN_SEN = int(float(api_indicator["ichimoku_9_26_52_26"]["tenken_sen_value"])) 
            if api_indicator["ichimoku_9_26_52_26"]["kijun_sen_value"]:
                share_indicator.ICHIMOKU_KIJUN_SEN = int(float(api_indicator["ichimoku_9_26_52_26"]["kijun_sen_value"])) 
            if api_indicator["wr_14"]:
                share_indicator.WILLIAMS_PERCENT_RANGE = int(float(api_indicator["wr_14"]))
            if api_indicator["ema_5"]:
                share_indicator.EMA_5 = int(float(api_indicator["ema_5"]))
            if api_indicator["ema_10"]:
                share_indicator.EMA_10 = int(float(api_indicator["ema_10"]))
            if api_indicator["ema_20"]:
                share_indicator.EMA_20 = int(float(api_indicator["ema_20"]))
            if api_indicator["ema_30"]:
                share_indicator.EMA_30 = int(float(api_indicator["ema_30"]))
            if api_indicator["ema_50"]:
                share_indicator.EMA_50 = int(float(api_indicator["ema_50"]))
            if api_indicator["sma_5"]:
                share_indicator.SMA_5 = int(float(api_indicator["sma_5"]))
            if api_indicator["sma_10"]:
                share_indicator.SMA_10 = int(float(api_indicator["sma_10"]))
            if api_indicator["sma_20"]:
                share_indicator.SMA_20 = int(float(api_indicator["sma_20"]))
            if api_indicator["sma_30"]:
                share_indicator.SMA_30 = int(float(api_indicator["sma_30"]))
            if api_indicator["sma_50"]:
                share_indicator.SMA_50 = int(float(api_indicator["sma_50"]))
            
            share_indicator.save()
        except Exception as e:
            result = False
          

    if result is True:
        return True

    else:
        return False
