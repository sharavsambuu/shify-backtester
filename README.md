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


# Tasks

    - Universe downloaded, for examples binance
    - 1m bar event streamer from the universe
    - Enable multi timeframes like 5m 15m 30m etc
    - Simple pluggable script
    - Position trackers
    - Commission calculation based simple BPS
    
    - I will add other task when they will comes in my mind...


# Setup
    virtualenv -p pytho3.9 env && source env/bin/activate && pip install -r requirements.txt


# References
    - Talib should be compiled from the source code
        https://github.com/TA-Lib/ta-lib-python






