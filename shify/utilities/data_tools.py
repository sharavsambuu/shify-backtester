import argparse

from shify.utilities import exchange_binance as binance

def binance_download():
    parser = argparse.ArgumentParser(description='Data downloader tool for Binance')
    parser.add_argument('-t', '--market_type', help='example : -t futures|spot', required=True)
    parser.add_argument('-i', '--interval'   , help="example : -i 1m|3m|15m|30m|1h...", required=False, default='1m')
    parser.add_argument('-s', '--symbols'    , help='example : -s BTCUSDT,ETHUSDT,SHIBUSDT', nargs='+', required=True)
    args = vars(parser.parse_args())

    market_type   = args['market_type']
    interval      = args['interval'   ]
    symbol_list   = args['symbols'    ]

    print("##### data_tools:binance_download")

    binance.download(market_type=market_type, interval=interval, symbol_list=symbol_list)

    pass