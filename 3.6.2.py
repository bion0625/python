from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

dow = pdr.get_data_yahoo('^DJI', '2000-01-04') # 2000년 이후의 다우존스 지수(^DJI) 데이터를 야후 파이낸스로부터 다운로드한다.
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04') # 2000년 이후의 KOSPI(^KS11) 데이터를 야후 파이낸스로부터 다운로드한다.

d = (dow.Close / dow.Close.loc['2000-01-04']) * 100 # 지수화: 금일 다우존스 지수를 2000년 1월 4일 다우존스 지수로 나눈 뒤 100을 곱한다.
k = (kospi.Close / kospi.Close.loc['2000-01-04']) * 100 # 지수화: 금일 KOSPI 지수를 2000년 1월 4일 KOSPI 지수로 나눈 뒤 100을 곱한다.

import matplotlib.pyplot as plt
plt.figure(figsize=(9, 5))
plt.plot(d.index, d, 'r--', label='Dow Jones Industrial') # 다우존스 지수를 붉은 점선으로 출력한다.
plt.plot(k.index, k, 'b', label='KOSPI') # KOSPI를 푸른 실선으로 출력한다.
plt.grid(True)
plt.legend(loc='best')
plt.show()