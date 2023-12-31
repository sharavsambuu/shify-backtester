import argparse



def binance_download():
    parser = argparse.ArgumentParser(description='Data downloader tool for Binance')
    parser.add_argument('-t', '--market_type', help='example : -t futures|spot', required=True)
    parser.add_argument('-i', '--interval'   , help="example : -i 1m|3m|15m|30m|1h...", required=False, default='1m')
    parser.add_argument('-s', '--symbols'    , help='example : -s BTCUSDT ETHUSDT SHIBUSDT', nargs='+', required=True)
    args = vars(parser.parse_args())

    market_type   = args['market_type']
    interval      = args['interval'   ]
    symbol_list   = args['symbols'    ]

    print("##### data_tools:binance_download")

    from shify.utilities import exchange_binance as binance
    binance.download(market_type=market_type, interval=interval, symbol_list=symbol_list)

    pass


def mt5_download():
    parser = argparse.ArgumentParser(description='Data downloader tool for MetaTrader5')
    parser.add_argument('-b' , '--broker'    , help="example : -b ava", required=False, default='fx')
    parser.add_argument('-i' , '--interval'  , help="example : -i 1|15|30|60|240|1440...", required=False, default='1')
    parser.add_argument('-y' , '--year'      , help="example : -i 2000 ", required=False, default='2000')
    parser.add_argument('-s' , '--symbols'   , help='example : -s EURUSD USDJPY GBPUSD', nargs='+', required=True)
    parser.add_argument('-rv', '--realvolume', help="example : -rv true", required=False, default=False)
    args = vars(parser.parse_args())

    broker_name = args['broker'    ]
    interval    = args['interval'  ]
    from_year   = args['year'      ] 
    symbol_list = args['symbols'   ]
    real_volume = args['realvolume']

    print("##### data_tools:mt5_download")

    from shify.utilities import exchange_mt5 as emt5
    emt5.download(broker_name=broker_name, interval=interval, from_year=from_year, symbol_list=symbol_list, real_volume=real_volume)
