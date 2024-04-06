# ch03_01_KOSPI_MDD.py
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
import matplotlib.pyplot as plt

kospi = pdr.get_data_yahoo('^KS11', '2004-01-04') # KOSPI 지수 데이터를 다운로드한다. KOSPI 지수의 심볼은 ^KS11이다.

window = 252 # 산정 기간에 해당하는 window값은 1년 동안의 개장일을 252일로 어림잡아 설정했다.
peak = kospi['Adj Close'].rolling(window, min_periods=1).max() # KOSPI 종가 칼럼에서 1년(거래일 기준) 기간 단위로 최고치 peak를 구한다.
drawdown = kospi['Adj Close']/peak - 1.0 # drawdown은 최고치(peak) 대비 현재 KOSPI 종가가 얼마나 하락했는지를 구한다.
# drawdown에서 1년 기간 단위로 최저치 max_dd를 구한다. 마이너스값이기 때문에 최저치가 바로 최대 손실 낙폭이 된다.
max_dd = drawdown.rolling(window, min_periods=1).min()


print(max_dd.min())
print(max_dd[max_dd==-0.5453665130144085])
print(max_dd[max_dd==max_dd.min()]) # 2008년 10월 24일부터 2009년 10월 22일까지 1년(252일) 동안 주어진 max_dd과 일치했다.

plt.figure(figsize=(9,7))
plt.subplot(211) # 2행 1열 중 1행에 그린다.
kospi['Close'].plot(label='KOSPI', title='KOSPI MDD', grid=True, legend=True)
plt.subplot(212) # 2행 1열 중 2행에 그린다.
drawdown.plot(c='blue', label='KOSPI DD', grid=True, legend=True)
max_dd.plot(c='red', label='KOSPI MDD', grid=True, legend=True)
plt.show()