
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import argparse

from datetime import datetime

#Grab parameter for Symbol data to download
argParser = argparse.ArgumentParser()
argParser.add_argument("-s", "--symbol", help="symbol of stock/index/currency to download data for")
args = argParser.parse_args()
SYMBOL = args.symbol
OUTPUT_FILE = SYMBOL + "-2020-2024.csv"

#Fetch historical data from yahoo
data = yf.download(SYMBOL, start="2020-01-01", end="2024-04-16")

print("Writing out data to --> " + OUTPUT_FILE)

#Write out to a csv file
data.to_csv(OUTPUT_FILE, index=True, encoding='=-&utf8')
