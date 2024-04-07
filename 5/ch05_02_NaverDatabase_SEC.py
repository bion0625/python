import matplotlib.pyplot as plt
from Investar import Analyzer

mk = Analyzer.MarketDB() # MarketDB 클래스로부터 mk 객체를 생성한다.
df = mk.get_daily_price('005930', '2017-07-10', '2018-06-30') # 야후 파이낸스 API와 마찬가지로조회할 종목과 조회할 기간만 인수로 넘겨주면 사용할 수 있다.

plt.figure(figsize=(9, 6))
plt.subplot(2, 1, 1)
plt.title('Samsung Electronics (Investar Data)')
plt.plot(df.index, df['close'], 'c', label='Close') # 네이버 금융에서는 수정 종가를 제공하지 않기 때문에 종가만 청록색으로 표시했다.
plt.legend(loc='best')
plt.subplot(2, 1, 2)
plt.bar(df.index, df['volume'], color='g', label='Volume')
plt.legend(loc='best')
plt.show()