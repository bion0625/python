# ch03_03_DowKospi_regression.py
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
from scipy import stats
import matplotlib.pyplot as plt

dow = pdr.get_data_yahoo('^DJI', '2000-01-04') # 다우존스 지수를 야후 파이낸스로부터 다운로드받는다.
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')

df = pd.DataFrame({'X': dow['Close'], 'Y': kospi['Close']}) # 다우존스 지수를 X칼럼으로 KOSPI 지수를 Y칼럼으로 갖는 데이터프레임을 생성한다.
df = df.bfill() # NaN을 제거한다.
df = df.ffill()

regr = stats.linregress(df.X, df.Y) # 다우존스 지수 X와 KOSPI 지수 Y로 선형회귀 모델 객체 regr을 생성한다.
regr_line = f'Y = {regr.slope:.2f} * X + {regr.intercept:.2f}' # 범례에 회귀식을 표시하는 레이블 문자다.

plt.figure(figsize=(7, 7))
plt.plot(df.X, df.Y, '.') # 산점도를 작은 원으로 나타낸다.
plt.plot(df.X, regr.slope * df.X + regr.intercept, 'r') # 회귀선을 붉은 색으로 그린다.
plt.legend(['DOW x KOSPI', regr_line])
plt.title(f'DOW x KOSPI (R = {regr.rvalue:.2f})')
plt.xlabel('DOW Jones Industrial Average')
plt.ylabel('KOSPI')
plt.show()