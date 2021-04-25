from django.shortcuts import render, redirect
import requests
import json
import numpy as np
import talib
from talib import MA_Type
import logging
from .models import Indicator
from .models import Shares_Specifications
from .filters_algos import prepared_filters
from .filters_algos import shares_model_filler
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
token = "36f3d0f1d4ea646bc316b380375a3c33"


# Create your views here.
def home(request):

    # 36f3d0f1d4ea646bc316b380375a3c33 sourenatoken
    # token = "36f3d0f1d4ea646bc316b380375a3c33"
    if request.method == 'POST':
        ticker = request.POST['ticker']

        api_request = requests.get("https://sourcearena.ir/api/?token="+ token +"&name="+ ticker +"")
        #api_request = requests.get("https://sourcearena.ir/api/?token=36f3d0f1d4ea646bc316b380375a3c33&all&type=0")
       # share_request = requests.get("https://sourcearena.ir/api/?token=36f3d0f1d4ea646bc316b380375a3c33&name="+ ticker +"&days=40")

        try:            
            symbol_name = []
            
            api = json.loads(api_request.content)
            # for name in api:
            #     symbol_name.append(name["name"])

            # symbol_name = symbol_name[0:6]
             
            # #api = api[0]['name']
            # share_info = json.loads(share_request.content)
            # li = []
            # for cPrice in share_info:
            #     li.append(float(cPrice['close_price']))

            # arr = np.array(li)
            # #close_numpy = close_numpy[::-1]
            # close = np.flipud(arr)
            
        except Exception as e:
            api = "Error..."

        """ 
        try:            
            sma_close = talib.RSI(close, timeperiod=14)           
            #sma_close = talib.SMA(close_numpy, timeperiod=20)    
            
           
        except Exception as e:
            sma_close = "Error ...." 
            """

        return render(request, 'home.html', 
                    {'api' : api,
                    #'share_info' : share_info,  
                    #'li' : li,                                    
                    #'sma_close' : sma_close,
                    #'symbol_name': symbol_name
                    })
    else:
        api_request = requests.get("https://sourcearena.ir/api/?token="+ token +"&name=وبملت")
        

        try:
            #api = []
            api = json.loads(api_request.content)
        # api = output[1]
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api' : api})


def about(request):
    try :
        if request.method  == "POST":
            filter_kind = request.POST["prepared_filters"]

        else:
            filter_kind = ''
    except Exception as e:
        filter_kind = ''
        value = "Error"

    result = prepared_filters.filter(filter_kind)   

  
    return render(request, 'about.html', {'filter_kind': filter_kind, 'result': result})

def prepared_filter(request):
    filter_counter = 0
    share_names = []
    try :
        if request.method  == "POST":
            filter_kind1 = request.POST["prepared_filters1"]
            filter_kind2 = request.POST["prepared_filters2"]
            filter_kind3 = request.POST["prepared_filters3"]
            filter_kind4 = request.POST["prepared_filters4"]
            filter_kind5 = request.POST["prepared_filters5"]       

        else:
            filter_kind1 = ''
            filter_kind2 = ''
    except Exception as e:
        filter_kind1 = ''
        value = "Error"


    if filter_kind1 != 'انتخاب فیلتر مورد نظر':
        filter_counter = filter_counter + 1
        r = prepared_filters.filter(filter_kind1)     
        share_names = r["share_names"]

    if filter_kind2 != 'انتخاب فیلتر مورد نظر':
        filter_counter = filter_counter + 1
        r = prepared_filters.filter(filter_kind2)   
        for item in r["share_names"]:
            share_names.append(item)

    if filter_kind3 != 'انتخاب فیلتر مورد نظر':
        filter_counter = filter_counter + 1
        r = prepared_filters.filter(filter_kind3)   
        for item in r["share_names"]:
            share_names.append(item)

    if filter_kind4 != 'انتخاب فیلتر مورد نظر':
        filter_counter = filter_counter + 1
        r = prepared_filters.filter(filter_kind4)   
        for item in r["share_names"]:
            share_names.append(item)

    if filter_kind5 != 'انتخاب فیلتر مورد نظر':
        filter_counter = filter_counter + 1
        r = prepared_filters.filter(filter_kind5)       
        for item in r["share_names"]:
            share_names.append(item)
    
    share_list = []
    for item in share_names:
        if share_names.count(item) == filter_counter:
            share_list.append(item)

    myset = set(share_list)
    share_names = list(myset)

    

    share_list = Shares_Specifications.objects.all()
    result = []
    for item_api in share_names:
        for item in share_list:
            if item_api == item.NAME:
                temp_dict = {}
                # smart_money1 = api[0]["name"]
                temp_dict["name"] = item.NAME
                temp_dict["trading_volume"] = item.TRADE_VOLUME
                temp_dict["final_price_change"] = item.FINAL_PRICE_CHANGE_PERCENT
                temp_dict["close_price_change"] = item.CLOSE_PRICE_CHANGE_PERCENT
                temp_dict["type"] = item.TYPE
                temp_dict["pe"] = item.PE      
                result.append(temp_dict)
               

  
    return render(request, 'prepared_filter.html', {'filter_kind1': filter_kind1,
                                                    'result': result, 
                                                    "share_names": share_names,})

def filter(request):  
    import requests
    import json  

    share_name = []
    try:
        if request.method  == "POST":
            # api_request = requests.get("https://sourcearena.ir/api/?token=36f3d0f1d4ea646bc316b380375a3c33&all&type=0")
            indicator1 = request.POST["indicator1"]
            value1 = request.POST["value1"]
            sign1 = request.POST["sign1"]
            indicator2 = request.POST["indicator2"]
            value2 = request.POST["value2"]
            sign2 = request.POST["sign2"]
            indicator3 = request.POST["indicator3"]
            value3 = request.POST["value3"]
            sign3 = request.POST["sign3"]
            indicator4 = request.POST["indicator4"]
            value4 = request.POST["value4"]
            sign4 = request.POST["sign4"]
            indicator5 = request.POST["indicator5"]
            value5 = request.POST["value5"]
            sign5 = request.POST["sign5"]
            indicator6 = request.POST["indicator6"]
            value6 = request.POST["value6"]
            sign6 = request.POST["sign6"]
            type1 = request.POST["type1"]
            pe = request.POST["pe_value"]
            sign7 = request.POST["pe_sign"]            
            # api = json.loads(api_request.content)  
            # for name in api:
            #     if int(name["close_price"]) > 13000:
            #         share_name.append(name["name"])

        else:
            value1 = ''
            sign1 = ''
            indicator1 = ''
            # api = "eroorrr"
            value2 = ''
            sign2 = ''
            indicator2 = ''
            value3 = ''
            sign3 = ''
            indicator3 = ''            
            value4 = ''
            sign4 = ''
            indicator4 = ''
            value5 = ''
            sign5 = ''
            indicator5 = ''
            value6 = ''
            sign6 = ''
            indicator6 = ''
            type1 = ''
            pe = ''
            sign7 = ''

            
    except Exception as e:
        value = "Error"   

    # share_name = share_name[0:10]
    # ###################
    filtered_share = []
    # share_type = []
    share_list = Shares_Specifications.objects.all()
    # share_type = Shares_Specifications.objects.all().values_list("TYPE")
    share_types = Shares_Specifications.objects.all().values("TYPE").distinct()
    # share_type = Shares_Specifications.objects.all().only("TYPE")
    # share_type = Shares_Specifications.objects.order_by('TYPE')
    indicator_name = []
    result = []
    for item in share_list:
        temp_dict = {}
        # temp_dict["name"] = item 
        flag = True
        if indicator1 != '': 
            indi1 = getattr(item, indicator1)
            if sign1 == '>':
                if indi1 > int(value1):                     
                    flag = True
                    indicator_name.append(indicator1)                   
                    
                    temp_dict[f"{indicator1}"] = indi1                    
                    
                else:
                    flag = False
                   
            elif sign1 == '<':
                if indi1 < int(value1): 
                    flag = True
                    indicator_name.append(indicator1)  
                  
                    temp_dict[f"{indicator1}"] = indi1
                          
                else:
                    flag = False
                    
            else:
                if indi1 == int(value1): 
                    flag = True
                    indicator_name.append(indicator1)
                    # indicator_name.append(indi1)
                    temp_dict[f"{indicator1}"] = indi1                 
                    
                else:
                    flag = False 
                    
        if indicator2 != '' and flag == True: 
            indi2 = getattr(item, indicator2)
            if sign2 == '>':
                if indi2 > int(value2):                     
                    flag = True
                    indicator_name.append(indicator2)
                    temp_dict[f"{indicator2}"] = indi2 
                    
                    
                else:
                    flag = False
                  
            elif sign2 == '<':
                if indi2 < int(value2): 
                    flag = True
                    indicator_name.append(indicator2)
                    # indicator_name.append(indi2)
                    temp_dict[f"{indicator2}"] = indi2                     
                    
                else:
                    flag = False
                    
            else:
                if indi2 == int(value2): 
                    flag = True
                    indicator_name.append(indicator2)
                    temp_dict[f"{indicator2}"] = indi2               
                    
                else:
                    flag = False 
                    
        if indicator3 != '' and flag == True: 
            indi3 = getattr(item, indicator3)
            if sign3 == '>':
                if indi3 > int(value3):                     
                    flag = True
                    indicator_name.append(indicator3)
                    temp_dict[f"{indicator3}"] = indi3 
                    
                else:
                    flag = False
            elif sign3 == '<':
                if indi3 < int(value3): 
                    flag = True
                    indicator_name.append(indicator3)
                    temp_dict[f"{indicator3}"] = indi3  
                    
                else:
                    flag = False
            else:
                if indi3 == int(value3): 
                    flag = True
                    indicator_name.append(indicator3)
                    temp_dict[f"{indicator3}"] = indi3  
                    
                else:
                    flag = False  

        if indicator4 != ''  and flag == True: 
            indi4 = getattr(item, indicator4)
            if sign4 == '>':
                if indi4 > int(value4):                     
                    flag = True
                    indicator_name.append(indicator4)
                    temp_dict[f"{indicator3}"] = indi4                 

                else:
                    flag = False
            elif sign4 == '<':
                if indi4 < int(value4): 
                    flag = True
                    indicator_name.append(indicator4)
                    temp_dict[f"{indicator4}"] = indi4  
                    
                else:
                    flag = False
            else:
                if indi4 == int(value4): 
                    flag = True
                    indicator_name.append(indicator4)
                    temp_dict[f"{indicator4}"] = indi4
                    
                else:
                    flag = False  
        if indicator5 != '' and flag == True: 
            indi5 = getattr(item, indicator5)   
            if sign5 == '>':
                if indi5 > int(value5):                     
                    flag = True
                    indicator_name.append(indicator5)
                    temp_dict[f"{indicator5}"] = indi5                   
                    
                else:
                    flag = False
            elif sign5 == '<':
                if indi5 < int(value5): 
                    flag = True
                    indicator_name.append(indicator5)
                    temp_dict[f"{indicator5}"] = indi5
                    
                else:
                    flag = False
            else:
                if indi5 == int(value5): 
                    flag = True
                    indicator_name.append(indicator5)
                    temp_dict[f"{indicator5}"] = indi5
                    
                else:
                    flag = False  


        if indicator6 != '' and flag == True: 
            indi6 = getattr(item, indicator6)   
            if sign6 == '>':
                if indi6 > int(value6):                     
                    flag = True
                    indicator_name.append(indicator6)
                    temp_dict[f"{indicator6}"] = indi6                    
                    
                else:
                    flag = False
            elif sign6 == '<':
                if indi6 < int(value6): 
                    flag = True
                    indicator_name.append(indicator6)
                    temp_dict[f"{indicator6}"] = indi6                    
                    
                else:
                    flag = False
            else:
                if indi6 == int(value6): 
                    flag = True
                    indicator_name.append(indicator6)
                    temp_dict[f"{indicator6}"] = indi6

                else:
                    flag = False  
        
        if pe != '' and sign7 != '' and flag == True: 
            indi6 = getattr(item, "PE")   
            if sign7 == '>':
                if indi6 > int(pe):                     
                    flag = True                
                    
                else:
                    flag = False
            elif sign7 == '<':
                if indi6 < int(pe): 
                    flag = True
                    
                else:
                    flag = False
            else:
                if sign7 == int(pe): 
                    flag = True

                else:
                    flag = False 



        if type1 != '' and flag == True: 
            # share_type = getattr(item, "TYPE")
            share_type = item.TYPE
            if share_type == type1:
                flag = True   
            else:
                flag = False

        if flag == True:  
            temp_dict["name"] = item.NAME
            temp_dict["trading_volume"] = item.TRADE_VOLUME
            temp_dict["final_price_change"] = item.FINAL_PRICE_CHANGE_PERCENT
            temp_dict["close_price_change"] = item.CLOSE_PRICE_CHANGE_PERCENT
            temp_dict["type"] = item.TYPE
            temp_dict["pe"] = item.PE      
            result.append(temp_dict)
            
            # resul_dict = 
            filtered_share.append(item.NAME)


    # ###################
    ranges = [1, 2, 3, 4, 5, 6]
    # ta = talib.get_functions()
    ta = ["ADX", "CCI", "STOCHASTIC_VALUE", "STOCHASTIC_SIGNAL", "STOCHASTIC_SIGNAL", "STOCHASTIC_RSI", "RSI", "MFI", "MOMENTUM",
    "VOLUME", "MACD_VALUE", "MACD_HISTOGRAM", "MACD_SIGNAL", "BOLLINGER_UPPERBAND", "BOLLINGER_MIDDLEBAND", "BOLLINGER_LOWERBAND"
    , "ICHIMOKU_TENKEN_SEN", "ICHIMOKU_KIJUN_SEN", "EMA_5", "EMA_10", "EMA_20", "EMA_30", "EMA_50", "SMA_5", "SMA_10", "SMA_20", "SMA_50"
    , "WILLIAMS_PERCENT_RANGE"]
 
    indicator_name = list(dict.fromkeys(indicator_name))
    return render(request, 'filter.html', {
    
        'ta' : ta,       
        # 'api' : api,
        'share_list' : share_list,
        'filtered_share': filtered_share,  
        'sign': sign1,
        'indicator': indicator1,
        'value' : value1,
        'indicator_name': indicator_name,
        "result": result,  
        "share_types": share_types,
        "ranges": ranges,
        
        })

def test(request):
    arr_arr = []
    adx_value = []
    cci_value = []
    bbands_value = []
    sar_value = []
    adxh = []
    sarh = []
    ccih = []
    rsih = []
    nameh = []    
    final_result = []
    share_name = []
    
    api_req =  requests.get("https://sourcearena.ir/api/?token="+ token +"&all&type=0")
    api_arr = json.loads(api_req.content)
    for name in api_arr:
        arr_arr.append(name["name"])
    
    share_name = ["فولاد", "ذوب", "کیسون", "وبانک", "خساپا"] 
    arr_arr = arr_arr[0 : 10]
    result = []   
    rsi_value = []
    i =0;
  #close = np.flipud(arr)
    for share in share_name:  
        try: 
            share_dict = {}      
            open_price = []
            close_price = []
            lowest_price = []
            highest_price = []        
            volume = []  
            api_request = requests.get("https://sourcearena.ir/api/?token="+ token +"&name="+ share +"&days=34")

            api = json.loads(api_request.content)         
            # rsi_api = requests.get(" http://sourcearena.ir/api/?token=36f3d0f1d4ea646bc316b380375a3c33&indicator=rsi&period=14&name="+ share +"")
            # rsi_value.append(json.loads(rsi_api.content))

            for item in api:       
                open_price.append(float(item["first_price"]))
                close_price.append(float(item["close_price"]))
                lowest_price.append(float(item["lowest_price"]))
                highest_price.append(float(item["highest_price"]))
                volume.append(float(item["trade_volume"]))           
            share_dict["name"] = share          
            share_dict["open_price"] = open_price
            share_dict["close_price"] = close_price
            share_dict["lowest_price"] = lowest_price
            share_dict["highest_price"] = highest_price
            share_dict["volume"] = volume      
            result.append(share_dict)

        except Exception as e:
            pass   

            # upperband, middleband, lowerband = BBANDS(close, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
    for item in result:  
        try:

            result_dict = {}      
            share_indicator = Indicator()
            share_indicator.name = item["name"]
            """
            openn = np.flipud(np.asarray(item["open_price"]))
            close = np.flipud(np.asarray(item["close_price"]))
            higest = np.flipud(np.asarray(item["highest_price"]))
            lowest = np.flipud(np.asarray(item["lowest_price"]))        
            sar_value = talib.SAR(np.asarray(item["highest_price"]), np.asarray(item["lowest_price"]), acceleration=0, maximum=0)
            adx_value = talib.ADX(np.asarray(item["highest_price"]), np.asarray(item["lowest_price"]), np.asarray(item["close_price"]), timeperiod=14)
            cci_value = talib.CCI(np.asarray(item["highest_price"]), np.asarray(item["lowest_price"]), np.asarray(item["close_price"]), timeperiod=14)        
            bbands_value = talib.RSI(np.asarray(item["close_price"]), timeperiod=14)
            """
            openn = np.asarray(item["open_price"])
            close = np.asarray(item["close_price"])
            higest = np.asarray(item["highest_price"])
            lowest = np.asarray(item["lowest_price"])
            volume = np.asarray(item["volume"])

            sar_value = talib.SAR(higest, lowest, acceleration=0.02, maximum=0.2)
            adx_value = talib.ADX(higest, lowest, close, timeperiod=14)
            cci_value = talib.CCI(higest, lowest, close, timeperiod=14)        
            rsi_value = talib.RSI(close, timeperiod=14)
            slowk, slowd = talib.STOCH(higest, lowest, close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
            mfi_value = talib.MFI(higest, lowest, close, volume, timeperiod=14)
            momentum_value = talib.MOM(close, timeperiod=10)
            macd, macdsignal, macdhist = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
            upperband, middleband, lowerband = talib.BBANDS(close, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
            # x = x[~numpy.isnan(x)]
            x = []
            x = sar_value[~np.isnan(sar_value)]
            sar_value = x        
            x = adx_value[~np.isnan(adx_value)]
            adx_value = x
            x = cci_value[~np.isnan(cci_value)]
            cci_value = x
            x = rsi_value[~np.isnan(rsi_value)]
            rsi_value = x
            x = slowk[~np.isnan(slowk)]
            stochastic_value = x
            x = slowd[~np.isnan(slowd)]
            stochastic_signal = x
            x = mfi_value[~np.isnan(mfi_value)]
            mfi_value = x
            x = momentum_value[~np.isnan(momentum_value)]
            momentum_value = x
            x = macd[~np.isnan(macd)]
            macd_value = x
            x = macdsignal[~np.isnan(macdsignal)]
            macd_signal = x
            x = macdhist[~np.isnan(macdhist)]
            macd_histogram = x
            x = upperband[~np.isnan(upperband)]
            bollinger_upperband = x
            x = middleband[~np.isnan(middleband)]
            bollinger_middleband = x
            x = lowerband[~np.isnan(lowerband)]
            bollinger_lowerband = x
            x = volume[~np.isnan(volume)]
            volume = x
            share_indicator.ADX = int(adx_value[0])     
            share_indicator.SAR = int(sar_value[0])
            share_indicator.RSI = int(rsi_value[0]) 
            share_indicator.CCI = int(cci_value[0]) 
            share_indicator.STOCHASTIC_VALUE = int(stochastic_value[0])
            share_indicator.STOCHASTIC_SIGNAL = int(stochastic_signal[0])
            share_indicator.MFI = int(mfi_value[0])
            share_indicator.MOMENTUM = int(momentum_value[0])
            share_indicator.MACD_VALUE = int(macd_value[0])
            share_indicator.MACD_SIGNAL = int(macd_signal[0])
            share_indicator.MACD_HISTOGRAM = int(macd_histogram[0])
            share_indicator.BOLLINGER_UPPERBAND = int(bollinger_upperband[0])
            share_indicator.BOLLINGER_MIDDLEBAND = int(bollinger_middleband[0])
            share_indicator.BOLLINGER_LOWERBAND = int(bollinger_lowerband[0])
            share_indicator.VOLUME = int(volume[0])

            share_indicator.save()
            result_dict["name"] = item["name"]         
            result_dict["sar"] = share_indicator.SAR
            result_dict["rsi"] = share_indicator.RSI
            result_dict["adx"] = share_indicator.ADX
            result_dict["cci"] = share_indicator.CCI
            result_dict["stochastic_value"] = share_indicator.STOCHASTIC_VALUE
            result_dict["stochastic_signal"] = share_indicator.STOCHASTIC_SIGNAL
            result_dict["mfi"] = share_indicator.MFI
            result_dict["momentum_value"] = share_indicator.MOMENTUM
            result_dict["macd_value"] = share_indicator.MACD_VALUE
            result_dict["macd_signal"] = share_indicator.MACD_SIGNAL
            result_dict["macd_histogram"] = share_indicator.MACD_HISTOGRAM
            final_result.append(result_dict) 
        
        except Exception as e:
            pass   

       

    with open('data.json', 'w') as fp:
        json.dump(share_dict, fp)
    real = talib.EMA(np.asarray(share_dict["close_price"]), timeperiod=30)
    
    counter = [0, 1 , 2, 3]
    
    return render(request, "test.html", 
        {'api' : api,       
        'open_price' : open_price,
        'close_price' : close_price,
        'lowest_price' : lowest_price,
        'highest_price' : highest_price,
        'volume' : volume,
        'share_dict' : share_dict,
        'result' : result,  
        'arr_arr' : arr_arr,
        'real' : real,
        'adxh' : adxh,
        'sarh' : sarh,
        'rsih' : rsih,
        'ccih' : ccih,
        'nameh' : nameh,
        'counter' : counter,
        'final_result' : final_result,    
        'adx_value' : adx_value, 
        'cci_value' : cci_value,
        'bbands_value' : bbands_value,
        'openn' : openn,
        # 'rsi_value' : rsi_value,  
        })


def alaki(request):
    return render(request, 'alaki.html', {})

def shares_info(request):

    context ={}
 
    # # add the dictionary during initialization
    context["shares"] = Shares_Specifications.objects.all()
 
    return render(request, 'shares_info.html',   context )


def database_filler(request):
         
     result = shares_model_filler.filler(token)   
     if result == True:
        name = "Filling Was Successfull"
     else:
        name = "Failed"
    # 'so_14': {'k_value': '8.28', 'd_value': '13.21'}
    # api = api["so_14"]["k_value"]
     return render(request, 'database_filler.html', {"arr_arr" : name})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})