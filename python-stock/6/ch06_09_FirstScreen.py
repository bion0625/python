# ch06_09_FirstScreen.py
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from mpl_finance import candlestick_ochl
import matplotlib.dates as mdates
from Investar import Analyzer

mk = Analyzer.MarketDB()
df = mk.get_daily_price('엔씨소프트', '2022-04-11')

ema60 = df.close.ewm(span=60).mean()    # 1. 종가의 12주 지수 이동평균
ema130 = df.close.ewm(span=130).mean()  # 2. 종가의 26주 지수 이동평균
macd = ema60 - ema130                   # 3. MACD선
signal = macd.ewm(span=45).mean()       # 4. 신호선(MACD의 9주 지수 이동평균)
macdhist = macd - signal                # 5. MACD 히스토그램

df = df.assign(ema130=ema130, ema60=ema60, macd=macd, signal=signal, macdhist=macdhist).dropna()
df['number'] = df.index.map(mdates.date2num) # 6. 캔들차트에 사용할 수 있는 날짜(date)형 인덱스를 숫자형으로 변환한다.
ohlc = df[['number', 'open', 'high', 'low', 'close']]

plt.figure(figsize=(9, 7))
p1 = plt.subplot(2, 1, 1)
plt.title('Triple Screen Trading - First Screen (NCSOFT)')
plt.grid(True)
candlestick_ochl(p1, ohlc.values, width=.6, colorup='red', colordown='blue') # 7. ohlc의 숫자형 일자, 시가, 고가, 저가, 종가 값을 이용해서 캔들 차트를 그린다.
p1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.plot(df.number, df['ema130'], color='c', label='EMA130')
plt.legend(loc='best')

p2 = plt.subplot(2, 1, 2)
plt.grid(True)
p2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.bar(df.number, df['macdhist'], color='m', label='MACD-hist')
plt.bar(df.number, df['macd'], color='b', label='MACD')
plt.bar(df.number, df['signal'], color='gray', label='MACD-Signal')
plt.legend(loc='best')
plt.show()