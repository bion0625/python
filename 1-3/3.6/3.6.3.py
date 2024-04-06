from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

dow = pdr.get_data_yahoo('^DJI', '2000-01-04') # 2000년 이후의 다우존스 지수(^DJI) 데이터를 야후 파이낸스로부터 다운로드한다.
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04') # 2000년 이후의 KOSPI(^KS11) 데이터를 야후 파이낸스로부터 다운로드한다.

d = (dow.Close / dow.Close.loc['2000-01-04']) * 100 # 지수화: 금일 다우존스 지수를 2000년 1월 4일 다우존스 지수로 나눈 뒤 100을 곱한다.
k = (kospi.Close / kospi.Close.loc['2000-01-04']) * 100 # 지수화: 금일 KOSPI 지수를 2000년 1월 4일 KOSPI 지수로 나눈 뒤 100을 곱한다.

# 다우존스 지수 데이터 개수와 KOSPI 지수 데이터 개수를 len() 함수로 출력해보면 데이터개수가 다르다.
print(len(dow))
print(len(kospi))

import matplotlib.pyplot as plt
# plt.scatter(dow, kospi, marker='.') # 산점도를 그리려면 x, y의 사이즈가 동일해야 한다. 지금 이대로는 오류가 발생한다.

# 다우존스 지수의 종가 칼럼과 KOSPI 지수의 종가 칼럼을 합쳐서 데이터프레임 df를 생성하자.
# 한 쪽에 데이터가 없으면 값이 없다는 의미의 NaN으로 자동적으로 채워주기 때문에 전체 데이터 개수가 둘 다 동일하게 늘었다.
import pandas as pd
df = pd.DataFrame({'DOW': dow['Close'], 'KOSPI': kospi['Close']})

print(df)

plt.scatter(df['DOW'], df['KOSPI'], marker='.')
plt.show()
