from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')

print(type(sec['Close']))

print(sec['Close'])

print(sec['Close'].shift(1))

sec_dpc = (sec['Close'] / sec['Close'].shift(1) - 1) * 100
msft_dpc = (msft['Close'] / msft['Close'].shift(1) -1) * 100
print(sec_dpc.head())

sec_dpc.iloc[0] = 0
msft_dpc.iloc[0] = 0
print(sec_dpc.head())
print(msft_dpc.head())

print(sec_dpc.describe())