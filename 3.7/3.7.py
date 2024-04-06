import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

dow = pdr.get_data_yahoo('^DJI', '2000-01-04')
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')

df = pd.DataFrame({'DOW': dow['Close'], 'KOSPI': kospi['Close']}) # 다우존스 지수의 종가 칼럼과 코스피 지수의 종가 칼럼으로 데이터프레임을 생성
df = df.bfill() # NaN가 있으면, 뒤값으로 대체
df = df.ffill() # 마지막 값은 뒤값이 없으므로, 마지막 값이 NaN인 경우 NaN이 있는 것이르모, NaN 있으면 앞에 값으로 대체

# 3.7.1 데이터프레임으로 상관계수 구하기
print(df.corr())

# 3.7.2 시리즈로 상관계수 구하기
print(
    df['DOW'].corr(df['KOSPI']) # df.DOW.forr(df.KOSPI)와 같다.
    )