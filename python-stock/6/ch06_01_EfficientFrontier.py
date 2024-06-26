import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Investar import Analyzer

# ch06_01_EfficientFrontier.py
mk = Analyzer.MarketDB()
stocks = ['삼성전자', 'SK하이닉스', '현대자동차', 'NAVER']
df = pd.DataFrame()
for s in stocks:
    df[s] = mk.get_daily_price(s, '2022-04-11', '2024-04-11')['close']

# 시총 상위 4 종목의 수익률을 비교하려면 종가 대신 일간 변동률로 비교를 해야 하기 때문에 데이터프레임에서 제공하는 pct_change() 함수를 사용해 4 종목의 일간 변동률을 구한다.
daily_ret = df.pct_change()

# 일간 변동률의 평균값에 252를 곱해서 연간 수익률을 구한다. 252는 미국의 1년 평균 개장일로,우리나라 실정에 맞게 다른 숫자로 바꾸어도 무방하다.
annual_ret = daily_ret.mean() * 252 

# 일간 리스크는 cov() 함수를 사용해 일간 변동률의 공분산으로 구한다.
daily_cov = daily_ret.cov() #

# 연간 공분산은 일간 공분산에 252를 곱해 계산한다.
annual_cov = daily_cov * 252

port_ret = []
port_risk = [] # 시총 상위 4 종목 비중을 다르게 해 포트폴리오 20,000개를 생성한다. 포트폴리오 수익률, 리스크, 종목 비중을 저장할 각 리스트를 생성한다.
port_weights = []

for _ in range(20000): # 포트폴리오 2000개를 생성하는 데 range() 함수와 for in 구문을 사용했다.
    weights = np.random.random(len(stocks)) # 4개의 랜덤 숫자로 구성된 배열을 생성한다.
    weights /= np.sum(weights) # 위에서 구한 4개의 랜덤 숫자를 랜덤 숫자의 총합으로 나눠 4 종목 비중의 합이 1이 되도록 조정한다.

    returns = np.dot(weights, annual_ret) # 랜덤하게 생성한 종목별 비중 배열과 종목별 연간 수익률을 곱해 해당 포트폴리오 전체 수익률(returns)을 구한다.
    # 종목별 연간 공분산과 종목별 비중 배열을 곱한 뒤 이를 다시 종목별 비중의 전치로 곱한다.
    # 이렇게 구한 결괏값의 제곱근을 sqrt() 함수로 구하면 해당 포트폴리오 전체 리스크(Risk)를 구할 수 있다.
    risk = np.sqrt(np.dot(weights.T, np.dot(annual_cov, weights)))

    port_ret.append(returns)        #
    port_risk.append(risk)          # 포트폴리오 20,000개 수익률, 리스크, 종목별 비중을 각각 리스트에 추가한다.
    port_weights.append(weights)    #

portfolio = {'Returns': port_ret, 'Risk': port_risk}
for i, s in enumerate(stocks): # i값은 0, 1, 2, 3 순으로 변한다. 이때 s값은 '삼성전자', 'SK하이닉스', '현대자동차', 'NAVER' 순으로 변한다.
    portfolio[s] = [weight[i] for weight in port_weights] # portfolio 딕셔너리에 '심성전자', 'SK하이닉스', '현대자동차', 'NAVER' 순서로 비중값을 추가한다.
df = pd.DataFrame(portfolio)
df = df[['Returns', 'Risk'] + [s for s in stocks]] #

df.plot.scatter(x='Risk', y='Returns', figsize=(10, 7), grid=True)
plt.title('Efficient Frontier')
plt.xlabel('Risk')
plt.ylabel('Expected Returns')
plt.show()