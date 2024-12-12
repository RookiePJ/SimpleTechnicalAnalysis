
#Simple shell script to run the stochastics against price data, given the price data within a file for each stock/index/currency

#Define some constants
INPUT_DIRECTORY=../data

#Loop through price files
for DataFile in $(ls -1 $INPUT_DIRECTORY/*.csv)
do
    PriceDataFile=$(basename $DataFile)
    echo "Processing data within file -->" $PriceDataFile
    python stochastic.py -d ${INPUT_DIRECTORY} -f ${PriceDataFile}
done

