import sys
import os
import pytz
import pandas   as pd
import numpy    as np
from   pytz     import timezone
from   mt5linux import MetaTrader5
from   datetime import datetime
from   pandas.tseries.offsets import BDay


mt5    = MetaTrader5()
utc_tz = pytz.timezone("Etc/UTC")


def fetch_data(instrument, timeframe=1, shift=0, lookback_size=100):
    d = {
        1   : mt5.TIMEFRAME_M1 ,
        5   : mt5.TIMEFRAME_M5 ,
        10  : mt5.TIMEFRAME_M10,
        15  : mt5.TIMEFRAME_M15,
        30  : mt5.TIMEFRAME_M30,
        60  : mt5.TIMEFRAME_H1 , 
        120 : mt5.TIMEFRAME_H2 ,
        180 : mt5.TIMEFRAME_H3 , 
        240 : mt5.TIMEFRAME_H4 ,
        1440: mt5.TIMEFRAME_D1
    }
    timeframe_mt5 = d.get(timeframe, mt5.TIMEFRAME_M1)

    if not mt5.initialize():
        mt5.shutdown()

    rates = mt5.copy_rates_from_pos(instrument, timeframe_mt5, shift, lookback_size)
    if rates is None:
        return None

    df = pd.DataFrame(rates)
    df['datetime'] = pd.to_datetime(df['time'], unit='s').dt.tz_localize(utc_tz)
    df.rename(columns={
        "open"       : "Open" , 
        "high"       : "High" ,
        "low"        : "Low"  ,
        "close"      : "Close",
        "tick_volume": "Volume"
        }, inplace=True)
    df = df.set_index(pd.DatetimeIndex(df['datetime']))
    
    mt5.shutdown()

    return df[['Open', 'High', 'Low', 'Close', 'Volume']]


def collect_history(folder_path, instrument, timeframe, from_year, lookback_size=100):
    print(f"downloading {instrument} ...")
    from_datetime = f"{from_year}-01-01 00:00:00"
    to_datetime   = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    date_range    = pd.bdate_range(from_datetime, to_datetime, freq=f"{timeframe}Min")
    date_range_df = pd.DataFrame(index=date_range)
    date_range_df = date_range_df[date_range_df.index.dayofweek<5]
    
    df_list = []
    for idx, shift in enumerate(reversed(list(np.arange(0, len(date_range_df), lookback_size)))):
        df = fetch_data(instrument=instrument, timeframe=timeframe, shift=shift, lookback_size=lookback_size)
        if df is not None:
            print(df)
            df_list.append(df)
    all_df = pd.concat(df_list)
    all_df = all_df[~all_df.index.duplicated(keep='last')]
    all_df = all_df.iloc[:-1]
    all_df = all_df["2000-01-01":]

    all_df.to_csv(f"{folder_path}/{instrument}.csv", header=True)
    print(f"saved to {folder_path}/{instrument}.csv")


def download(broker_name, interval, from_year, symbol_list):
    print(f"broker : {broker_name}, interval : {interval}, from year : {from_year}")
    print(f"symbols : {symbol_list}")

    folder_path = f"data/{broker_name}_mt5/klines/{interval}m/"
    if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    for symbol in symbol_list:
        collect_history(folder_path, symbol, int(interval), from_year, lookback_size=1000)
        
    pass



