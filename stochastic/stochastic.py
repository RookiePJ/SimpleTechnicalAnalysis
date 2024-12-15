
#Download necessary libraries
import talib as ta
import pandas as pd
import matplotlib.pyplot as plt
import argparse
import seaborn as sns

argParser = argparse.ArgumentParser()
argParser.add_argument("-f", "--filename", help="name of file containing price data")
argParser.add_argument("-d", "--directory", help="name of directory containing price data")
args = argParser.parse_args()

print("args=%s", args)
print("args.filename=%s", args.filename)

#Setup file locations from arguments
INPUT_FILE = args.filename
INPUT_DIRECTORY= args.directory
OUTPUT_DIRECTORY="./calculated_results/"
GRAPH_DIRECTORY="./graph_results/"

#Import data from file saved on system - skip some rows as the api has changed.
PriceData = pd.read_csv(INPUT_DIRECTORY + "/" + INPUT_FILE, skiprows=[1,2])

#Compute ‘slowk’ and ‘slowd’ values
PriceData['slowk'], PriceData['slowd'] = ta.STOCH(PriceData['High'], PriceData['Low'], PriceData['Close'], fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)

#Generate Buy and sell signals
PriceData['Signal_Buy'] = ((PriceData['slowk'] > PriceData['slowd']) & (PriceData['slowk'].shift(1) < PriceData['slowd'].shift(1))) & (PriceData['slowd'] < 20)
PriceData['Signal_Sell'] = ((PriceData['slowk'] < PriceData['slowd']) & (PriceData['slowk'].shift(1) > PriceData['slowd'].shift(1))) & (PriceData['slowd'] > 80)

#PriceData.rename(columns={'Price': 'Date'}, inplace=True)

#Output results
PriceData.to_csv(OUTPUT_DIRECTORY + "Stochastic-" + INPUT_FILE, index=True, encoding='-&utf8')
print("Outputting calculated data to --> " + OUTPUT_DIRECTORY + "Stochastic-" + INPUT_FILE)

jsonDataFrame = PriceData[['Price', 'Close', 'Signal_Buy', 'Signal_Sell']].copy()
jsonDataFrameLimited = pd.DataFrame(jsonDataFrame, columns=['Price', 'Close', 'Signal_Buy', 'Signal_Sell'].copy())
jsonDataFrameLimited.to_json(OUTPUT_DIRECTORY + "Stochastic-" + INPUT_FILE + ".json")
print("Outputting JSON calculated data to " + OUTPUT_DIRECTORY + "Stochastic-" + INPUT_FILE + ".json")

#print (PriceData)
#Plot Values
fig1, ax = plt.subplots(2, figsize=(15,8))
ax[0].plot(PriceData['Close'])
ax[1].plot(PriceData['slowk'])
ax[1].plot(PriceData['slowd'])
plt.axhline(20, color='red', linestyle='--')
plt.axhline(80, color='red', linestyle='--')
plt.suptitle('Stochastic ' + INPUT_FILE)
plt.savefig(GRAPH_DIRECTORY + "Stochastic-" + INPUT_FILE + ".pdf", bbox_inches='tight')
# plt.show()
