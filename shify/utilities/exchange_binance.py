import os
import csv
import sys
import time
import requests
import glob
import zipfile
import pandas as pd
from urllib.parse                      import urlparse
from bs4                               import BeautifulSoup
from selenium                          import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome          import ChromeDriverManager


def download(market_type, interval, symbol_list):
    print(f"market type : {market_type}, interval : {interval}")
    print(f"symbols : {symbol_list}")

    if not market_type in ["spot", "futures"]:
        print("parameter should be one of spot or futures")
        sys.exit()

    for symbol in symbol_list:
        try:
            if market_type=="spot":
                data_url = f"https://data.binance.vision/?prefix=data/spot/monthly/klines/{symbol}/{interval}/"
            elif market_type=="futures":
                data_url = f"https://data.binance.vision/?prefix=data/futures/um/monthly/klines/{symbol}/{interval}/"
            folder_path = f"data/binance/klines/{market_type}_{interval}_raw/{symbol}/"
            os.makedirs(folder_path, exist_ok=True)

            soup = None
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            with webdriver.Chrome(service=ChromeService(), options=options) as driver:
                driver.get(data_url)
                print("waiting for dynamic web content is assembled...")
                time.sleep(5)
                html = driver.page_source
                soup = BeautifulSoup(html, "html.parser")

            if soup is None:
                print("Soup is none...")
                sys.exit()

            list_html = soup.find(id="listing")

            links = list_html.findAll('a')
            for a in links:
                if not "CHECKSUM" in a.text:
                    download_file_url = a["href"]
                    if "zip" in download_file_url:
                        a = urlparse(download_file_url)
                        filename = os.path.basename(a.path)
                        if os.path.exists(f"{folder_path}/{filename}"):
                            print(f"{filename} is already downloaded, so skipping to download it.")
                            continue
                        print(f"downloading {filename} ...")
                        response = requests.get(download_file_url)
                        open(f"{folder_path}/{filename}", "wb").write(response.content)

            for el in glob.glob(f"{folder_path}/*"):
                filename = os.path.basename(el)
                if "zip" in filename:
                    print(f"unzipping {el} ...")
                    with zipfile.ZipFile(el, 'r') as zip_ref:
                        zip_ref.extractall(f"{folder_path}/")

            # integration into one csv file
            folder_path = f"./data/binance/klines/{market_type}_{interval}_raw/{symbol}/"
            if not os.path.exists(folder_path):
                print(f"Please download {symbol} {market_type} aggTrades ...")
                sys.exit()

            def detect_header(input_csv_file):
                has_headings = False
                with open(input_csv_file, "r") as f:
                    try:
                        has_headings = csv.Sniffer().has_header(f.read(3024))
                    except csv.Error:
                        has_headings = False
                return has_headings

            csv_files = []
            for el in glob.glob(f"{folder_path}/*"):
                filename = os.path.basename(el)
                if "csv" in filename:
                    csv_path = f"{folder_path}/{filename}"
                    csv_files.append(csv_path)

            csv_files.sort()

            for filename in csv_files:
                has_headings = detect_header(filename)
                print(f"{filename} {has_headings}")

            df_list = []

            for idx, csv_path in enumerate(csv_files):
                print(f"reading : {csv_path}")

                if detect_header(csv_path)==True:
                    df = pd.read_csv(csv_path)
                    df = df.rename(columns={"open": "Open", "high": "High", "low": "Low", "close": "Close", "volume": "Volume"})
                    df = df.astype({"open_time": "datetime64[ms]"})
                    df["datetime"] = df["open_time"]
                    df = df.set_index("datetime")
                    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
                    df_list.append(df)
                else:
                    df = pd.read_csv(csv_path, header=None, names=['open_time','Open','High', 'Low', 'Close', 'Volume', 'close_time', 'quote_volume', 'count', 'taker_buy_volume', 'taker_buy_quote_volume', 'ignore'])
                    df = df.astype({"open_time": "datetime64[ms]"})
                    df["datetime"] = df["open_time"]
                    df = df.set_index("datetime")
                    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
                    df_list.append(df)


            print("integrating all dataframes...")
            all_df = pd.concat(df_list)
            all_df = all_df.sort_index()
            all_df = all_df[~all_df.index.duplicated(keep='first')]

            output_folder = f"./data/binance/klines/{market_type}_{interval}"
            os.makedirs(output_folder, exist_ok=True)
            all_df.to_csv(f"{output_folder}/{symbol}-{interval}.csv", header=True)

            print(f"saved to {output_folder}/{symbol}-{interval}.csv")

        except Exception as e:
            print(f"Exception at processing {symbol}")
