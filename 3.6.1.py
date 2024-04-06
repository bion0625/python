from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

dow = pdr.get_data_yahoo('^DJI', '2000-01-04') # 2000년 이후의 다우존스 지수(^DJI) 데이터를 야후 파이낸스로부터 다운로드한다.
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04') # 2000년 이후의 KOSPI(^KS11) 데이터를 야후 파이낸스로부터 다운로드한다.

import matplotlib.pyplot as plt
plt.figure(figsize=(9, 5))
plt.plot(dow.index, dow.Close, 'r--', label='Dow Jones Industrial') # 다우존스 지수를 붉은 점선으로 출력한다.
plt.plot(kospi.index, kospi.Close, 'b', label='KOSPI') # KOSPI를 푸른 실선으로 출력한다.
plt.grid(True)
plt.legend(loc='best')
plt.show()