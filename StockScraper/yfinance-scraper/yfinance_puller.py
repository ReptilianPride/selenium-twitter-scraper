import pandas as pd
import yfinance as yf
import argparse
import os

# Define ticker symbols
nvda_ticker = "NVDA"
sp500_ticker = "^GSPC"

# Define/Get date range
parser=argparse.ArgumentParser(description="To fetch start and end date for api calls")
parser.add_argument('-s','--start',required=True,help="Start Value")
parser.add_argument('-e','--end',required=True,help='End Value')
args=parser.parse_args()

start_date=args.start
end_date=args.end

# start_date = "2024-01-01"
# end_date = "2024-02-01"

# Download stock data (hourly)
print('[]Downloading Data')
nvda_data = yf.download(nvda_ticker, start=start_date, end=end_date, interval='1h')
sp500_data = yf.download(sp500_ticker, start=start_date, end=end_date, interval='1h')

print('[]Flattening multiindex')
nvda_data.columns=[col[0] for col in nvda_data.columns]
sp500_data.columns=[col[0] for col in sp500_data.columns]

# Convert index to London timezone
print('[]Converting to london timezone')
nvda_data.index = nvda_data.index.tz_convert("Europe/London")
sp500_data.index = sp500_data.index.tz_convert("Europe/London")

# Reset Index and Extract Date & Time Separately
print('[]Updating tables')
nvda_data = nvda_data.reset_index()
nvda_data["Date"] = nvda_data["Datetime"].dt.date
nvda_data["Time"] = nvda_data["Datetime"].dt.time
nvda_data.drop(columns=["Datetime"], inplace=True)

sp500_data = sp500_data.reset_index()
sp500_data["Date"] = sp500_data["Datetime"].dt.date
sp500_data["Time"] = sp500_data["Datetime"].dt.time
sp500_data.drop(columns=["Datetime"], inplace=True)

# Drop original datetime column (optional)

# Save to CSV
print('Exporting to CSV file')

if not os.path.exists('Datasets'):
    print('[]Creating output directory')
    os.makedirs('Datasets')

nvda_data.to_csv(os.path.join('Datasets',f'NVDA_{start_date}_stockdata.csv'), index=False)
sp500_data.to_csv(os.path.join('Datasets',f'SP500_{start_date}_stockdata.csv'), index=False)

print("Stock Dataset Generated!")
