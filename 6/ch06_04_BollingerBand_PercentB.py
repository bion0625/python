# ch06_04_BollingerBand_PercentB.py
import matplotlib.pyplot as plt
from Investar import Analyzer

mk = Analyzer.MarketDB()
df = mk.get_daily_price('NAVER', '2023-04-11')

df['MA20'] = df['close'].rolling(window=20).mean() # 20개 종가를 이용해서 평균을 구한다.
df['stddev'] = df['close'].rolling(window=20).std() # 20개 종가를 이용해서 표준편차를 구한 뒤 stddev 칼럼으로 df에 추가한다.
df['upper'] = df['MA20'] + (df['stddev'] * 2) # 중간 볼린저 밴드 + (2 X 표준편차)를 상단 볼린저 밴드로 계산한다.
df['lower'] = df['MA20'] - (df['stddev'] * 2) # 중간 볼린저 밴드 - (2 X 표준편차)를 상단 볼린저 밴드로 계산한다.
df['PB'] = (df['close'] - df['lower'])/(df['upper'] - df['lower']) # (종가 - 하단밴드) / (상단밴드 - 하단밴드)를 구해 %B 칼럼을 생성한다.
df = df[19:] # 위 내용은 19번째 행까지 NaN이므로 (20개씩 계산) 값이 있는 20번째 행부터 사용한다.

plt.figure(figsize=(9, 8))
plt.subplot(2, 1, 1) # 기존의 볼린저 밴드 차트를 2행 1열의 그리드에서 1열에 배치한다.
plt.plot(df.index, df['close'], color='#0000ff', label='Close') # x좌표 df.index에 해당하는 종가를 y좌표로 설정해 파란색(#0000ff) 실선으로 표시한다.
plt.plot(df.index, df['upper'], 'r--', label='Upper band') # x좌표 df.index에 해당하는 상단 볼린저 밴드값을 y좌표로 설정해 검은 실선(k--)으로 표시한다.
plt.plot(df.index, df['MA20'], 'k--', label='Moving average 20')
plt.plot(df.index, df['lower'], 'c--', label='Lower band')
plt.fill_between(df.index, df['upper'], df['lower'], color='0.9') # 상단 볼린저 밴드와 하단 볼린저 밴드 사이를 회색으로 칠한다.
plt.title('NAVER Bollinger Band (20 day, 2 std)')
plt.legend(loc='best')

plt.subplot(2, 1, 2) # %B 차트를 2행 1열의 그리드에서 2열에 배치한다.
plt.plot(df.index, df['PB'], color='b', label='%B') # x좌표 df.idnex에 해당하는 %d값을 y좌표로 설정해 파란(b) 실선으로 표시한다.
plt.grid(True)
plt.legend(loc='best')
plt.show()