# About the Shify backtester
Well, I needed to know whats going on behind the scene.
And also I want to iterate faster when trying new strategies.
In that regards, I've already tried some other libraries like Zipline etc
and I couldn't even bundle 1minute timeframe data but I still 
think Zipline's approach to handle the problem is very good.
This library gonna become Frankenstein's monster so don't expect much.
The name Shify is just a random name.

So whats inside my mind are currently followings : 

    - Multi universe
    - Auto caching
    - Multi bars
    - Pluggable 
    - Extensible, ie add other trading cost calculation
    - Portfolio
    - Multi Strategy
    - Asynchronous
    - Configurable
    - Use common libraries like TALib, quantstats


# Install

    pip install git+https://github.com/sharavsambuu/shify-backtester


# Usage

    Download data from Binance
        `shifydownload -e binance -mt spot -s BTCUSDT ETHUSDT BNBUSDT`

# Examples

    https://github.com/sharavsambuu/shify-examples


# Tasks

    - Universe downloaded, for examples binance
    - 1m bar event streamer from the universe
    - Enable multi timeframes like 5m 15m 30m etc
    - Simple pluggable script
    - Position trackers
    - Commission calculation based simple BPS
    
    - I will add other tasks when they will comes into my mind...



# References
    - Talib should be compiled from the source code
        https://github.com/TA-Lib/ta-lib-python
    - Create custom python library
        https://github.com/mike-huls/toolbox







