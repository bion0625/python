# ch06_10_SecondScreen.py
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from mpl_finance import candlestick_ochl
import matplotlib.dates as mdates
from Investar import Analyzer

mk = Analyzer.MarketDB()
df = mk.get_daily_price('엔씨소프트', '2022-04-11')

ema60 = df.close.ewm(span=60).mean()
ema130 = df.close.ewm(span=130).mean()
macd = ema60 - ema130
signal = macd.ewm(span=45).mean()
macdhist = macd - signal

df = df.assign(ema130=ema130, ema60=ema60, macd=macd, signal=signal, macdhist=macdhist).dropna()
df['number'] = df.index.map(mdates.date2num)
ohlc = df[['number', 'open', 'high', 'low', 'close']]

# 1. 14일 동안의 최댓값을 구한다. min_periods=1을 지정할 경우, 14일 기간에 해당하는 데이터가 모두 누적되지 않았더라도 최소 기간이 1일 이상의 데이터만 존재하면 최댓값을 구하라는 의미다.
nday_highs = df.high.rolling(window=14, min_periods=1).max()   
# 2. 14일 동안의 최솟값을 구한다. min_periods=1을 지정할 경우, 14일 치 데이터 모두 누적되지 않았더라도 최소 기간이 1일 이상의 데이터만 존재하면 최솟값을 구하라는 의미다.
nday_lows = df.low.rolling(window=14, min_periods=1).min()          
fast_k = (df.close - nday_lows) / (nday_highs - nday_lows) * 100    # 3. 빠른 선 %K를 구한다.
slow_d = fast_k.rolling(window=3).mean()                            # 4. 3일 동안의 %K의 평균을 구해서 느린 선 %D에 저장한다.
df = df.assign(fast_k=fast_k, slow_d=slow_d).dropna()               # 5. %K와 %D로 데이터프레임을 생성한 뒤 결측치는 제거한다.

plt.figure(figsize=(9, 7))
p1 = plt.subplot(2, 1, 1)
plt.title('Triple Screen Trading - Second Screen (NCSOFT)')
plt.grid(True)
candlestick_ochl(p1, ohlc.values, width=.6, colorup='red', colordown='blue')
p1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.plot(df.number, df['ema130'], color='c', label='EMA130')
plt.legend(loc='best')

p1 = plt.subplot(2, 1, 2)
plt.grid(True)
p1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.plot(df.number, df['fast_k'], color='c', label='%K')
plt.plot(df.number, df['slow_d'], color='k', label='%D')
plt.yticks([0, 20, 80, 100]) # 6. y축 눈금을 0, 20, 80, 100으로 설정하여, 스토캐스틱의 기준선을 나타낸다.
plt.legend(loc='best')
plt.show()