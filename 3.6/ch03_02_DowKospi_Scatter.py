# ch03_02_DowKospi_Scatter.py
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

dow = pdr.get_data_yahoo('^DJI', '2000-01-04')
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')

df = pd.DataFrame({'DOW': dow['Close'], 'KOSPI': kospi['Close']}) # 다우존스 지수의 종가 칼럼과 코스피 지수의 종가 칼럼으로 데이터프레임을 생성

import matplotlib.pyplot as plt
plt.figure(figsize=(7, 7))
plt.scatter(df['DOW'], df['KOSPI'], marker='.') # 다우존스 지수를 x로, KOSPI 지수를 y로 산점도를 그리되, 검은 작은 원(.) 모양으로 표시한다.
plt.xlabel('Dow Jones Industrial Average')
plt.ylabel('KOSPI')
plt.show()