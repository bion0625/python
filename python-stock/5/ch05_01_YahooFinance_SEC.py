from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
import matplotlib.pyplot as plt

df = pdr.get_data_yahoo('005930.KS', '2017-01-01') # 삼성전자 데이터를 2017년 1월 1일부터 조회한다.

plt.figure(figsize=(9, 6))
plt.subplot(2, 1, 1) # 2행 1열 영역에서 첫 번째 영역을 선택한다.
plt.title('Samsung Electronics (Yahoo Finance)')
plt.plot(df.index, df['Close'], 'c', label='Close') # 삼성전자 종가(Close)를 청록색 실선으로 표시한다.
plt.plot(df.index, df['Adj Close'], 'b--', label='Adj Close') # 삼성전자의 수정 종가(Adj Close)를 파란색 점선으로표시한다.
plt.legend(loc='best')
plt.subplot(2, 1, 2) # 2행 1열의 영역에서 두 번째 영역을 선택한다.
plt.bar(df.index, df['Volume'], color='g', label='Volume') # 삼성전자 거래량을 바 차트로 그린다.
plt.legend(loc='best')
plt.show()