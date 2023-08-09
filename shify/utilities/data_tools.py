import argparse

def download():
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-e' , '--exchange'   , help='example : -e binance', required=True)
    parser.add_argument('-mt', '--market_type', help='example : -mt futures|spot', required=True)
    parser.add_argument('-s' , '--symbols'    , help='example : -s BTCUSDT,ETHUSDT,SHIBUSDT', nargs='+', required=True)
    args = vars(parser.parse_args())

    exchange_name = args['exchange'   ]
    market_type   = args['market_type']
    symbol_list   = args['symbols'    ]

    print("##### data_tools:download")
    print(f"exchange name : {exchange_name}")
    print(f"market type   : {market_type}"  )
    print(f"symbols       : {symbol_list}"  )

    pass