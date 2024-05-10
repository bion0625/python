# ch06_11_TripleScreen.py
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from mpl_finance import candlestick_ochl
import matplotlib.dates as mdates
from Investar import Analyzer

mk = Analyzer.MarketDB()
# df = mk.get_daily_price('삼성전자', '2022-04-11', '2022-10-11')
# df = mk.get_daily_price('삼성전자', '2023-01-01', '2023-06-30')
# df = mk.get_daily_price('삼성전자', '2023-07-01', '2023-12-31')
# df = mk.get_daily_price('에스바이오메딕스', '2024-01-01', '2024-04-16')
df = mk.get_daily_price('에스바이오메딕스', '2023-09-01')

ema60 = df.close.ewm(span=60).mean()
ema130 = df.close.ewm(span=130).mean()
macd = ema60 - ema130
signal = macd.ewm(span=45).mean()
macdhist = macd - signal

df = df.assign(ema130=ema130, ema60=ema60, macd=macd, signal=signal, macdhist=macdhist).dropna()
df['number'] = df.index.map(mdates.date2num)
ohlc = df[['number', 'open', 'high', 'low', 'close']]

nday_highs = df.high.rolling(window=14, min_periods=1).max()
nday_lows = df.low.rolling(window=14, min_periods=1).min()

fast_k = (df.close - nday_lows) / (nday_highs - nday_lows) * 100
slow_d = fast_k.rolling(window=3).mean()
df = df.assign(fast_k=fast_k, slow_d=slow_d).dropna()

plt.figure(figsize=(9, 9))
p1 = plt.subplot(3, 1, 1)
plt.title('Triple Screen Trading (NCSOFT)')
plt.grid(True)
candlestick_ochl(p1, ohlc.values, width=.6, colorup='red', colordown='blue')
p1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.plot(df.number, df['ema130'], color='c', label='EMA130')
for i in range(1, len(df.close)):
    if df.ema130.values[i-1] < df.ema130.values[i] and \
        df.slow_d.values[i-1] >= 20 and df.slow_d.values[i] < 20: # 1. 130일 이동 지수 평균이 상승하고 %D가 20 아래로 떨어지면 (아래 주석)
        plt.plot(df.number.values[i], df.close.values[i], 'y^')               # 2. 빨간색 삼각형으로 매수 신호를 표시한다.
    elif df.ema130.values[i-1] > df.ema130.values[i] and \
        df.slow_d.values[i-1] <= 80 and df.slow_d.values[i] > 80: # 3. 130일 이동 지수 평균이 하락하고 %D가 80 위로 상승하면 (아래 주석)
        plt.plot(df.number.values[i], df.close.values[i], 'bv')               # 4. 파란색 삼각형으로 매도 신호를 표시한다.
plt.legend(loc='best')

p2 = plt.subplot(3, 1, 2)
plt.grid(True)
p2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.bar(df.number, df['macdhist'], color='m', label='MACD-hist')
plt.bar(df.number, df['macd'], color='b', label='MACD')
plt.bar(df.number, df['signal'], color='gray', label='MACD-Signal')
plt.legend(loc='best')

p3 = plt.subplot(3, 1, 3)
plt.grid(True)
p3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.plot(df.number, df['fast_k'], color='c', label='%K')
plt.plot(df.number, df['slow_d'], color='k', label='%D')
plt.yticks([0, 20, 80, 100])
plt.legend(loc='best')
plt.show()