import proxy
import yfinance as yf
import argparse

#Grab parameter for Symbol data to download
argParser = argparse.ArgumentParser()
argParser.add_argument("-t", "--ticker", help="ticker of stock/index/currency to download data for")
argParser.add_argument("-i", "--interval", help="interval between data - 1d (one day) / 1h (one hour) ")
argParser.add_argument("-s", "--startdate", help="start date in yyyy-mm-dd format")
argParser.add_argument("-e", "--enddate", help="end date in yyyy-mm-dd format")

args = argParser.parse_args()
#print("args=%s" + args)

TICKER = args.ticker
#TICKER= 'GBPUSD=X'
INTERVAL= args.interval
START_DATE = args.startdate
END_DATE = args.enddate

#OUTPUT_FILE = 'GBP-USD' + "-" + INTERVAL + "-" + START_DATE + "-" + END_DATE + ".csv"
OUTPUT_FILE = TICKER + "-" + INTERVAL + "-" + START_DATE + "-" + END_DATE + ".csv"

#Fetch historical data from yahoo
data = yf.download(TICKER, start=START_DATE, end=END_DATE, interval=INTERVAL)

data.rename(columns={'Price': 'Date'}, inplace=True)

print("Writing out data to --> " + OUTPUT_FILE)

#Write out to a csv file
data.to_csv(OUTPUT_FILE, index=True, index_label='Date', encoding='=-&utf8')

#jsonDataFrame = data, columns=['Price', 'Close'].copy()
#data.to_json(OUTPUT_FILE + '.json')
