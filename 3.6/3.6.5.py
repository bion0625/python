import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

dow = pdr.get_data_yahoo('^DJI', '2000-01-04')
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')

df = pd.DataFrame({'DOW': dow['Close'], 'KOSPI': kospi['Close']}) # 다우존스 지수의 종가 칼럼과 코스피 지수의 종가 칼럼으로 데이터프레임을 생성
df = df.bfill() # NaN가 있으면, 뒤값으로 대체
df = df.ffill() # 마지막 값은 뒤값이 없으므로, 마지막 값이 NaN인 경우 NaN이 있는 것이르모, NaN 있으면 앞에 값으로 대체

from scipy import stats
# linregress() 함수를 이용하면 시리즈 객체 두 개만으로 간단히 선형 회귀 모델을 생성하여 분석할 수 있다.
regr = stats.linregress(df['DOW'], df['KOSPI'])
print(regr)

# LinregressResult(
    # slope=0.06505359275110478,            # 기울기
    # intercept=611.5542127653287,          # y절편
    # rvalue=0.8240329564157621,            # r값(상관계수)
    # pvalue=0.0,                           # p값
    # stderr=0.0005640303167304836,         # 표준편차
    # intercept_stderr=10.875019843219302   # ?
# )