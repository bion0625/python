# ch07_08_Backtrader_RSI.py
# backtrader 버전 이슈 대문에 아래 링크 참조해서 해결
# https://stackoverflow.com/questions/60715059/python-backtrader-error-filenotfounderror-errno-2-no-such-file-or-directory
from datetime import datetime # 버전 이슈로 안 쓰게 됨
import backtrader as bt
import yfinance as yf # 버전이슈로 추가

class MyStrategy(bt.Strategy): # 1. bt.Stategy 클래스를 상속받아서 MyStategy 클래스를 작성한다.
    def __init__(self):
        self.rsi = bt.indicators.RSI(self.data.close) # 2. RSI 지표를 사용하려면 MyStrategy 클래스 생성자에서 RSI 지표로 사용할 변수를 지정한다.
    def next(self): # 3. next() 메서드는 주어진 데이터와 지표indicator를 만족시키는 최소 주기마다 자동으로 호출된다. 시장에 참여하고 있지 않을 때 RSI가 30미만이면 매수하고, 시샂에 참여하고 있을 때 RSI가 70을 초과하면 매도하도록 구현한다.
        if not self.position:
            if self.rsi < 30:
                self.order = self.buy()
        else:
            if self.rsi > 70:
                self.order = self.sell()

cerebro = bt.Cerebro() # 4. Cerebro 클래스는 백트레이더의 핵심 클래스로서, 데이터를 취합하고 백테스트 또는 라이브 트레이딩을 실행한 뒤 그 겨과를 출력ㅏ는 기능을 담당한다.
cerebro.addstrategy(MyStrategy)

# 버전 이슈로 로직 변경
data = bt.feeds.PandasData(dataname=yf.download("036570.KS", # 5. 엔씨소프트(036570.KS)의 종가 데이터는 야후 파이낸스 데이터를 이용해서 취합한다.
                                            start="2023-01-01", end="2024-04-11"))

cerebro.adddata(data)
cerebro.broker.setcash(10000000) # 6. 초기 투자 자금을 천만 원으로 설정한다.
cerebro.addsizer(bt.sizers.SizerFix, stake=30) # 7. 엔씨소프트 주식의 매매 단위는 30주로 설정한다. 보유한 현금에 비해 매수하려는 주식의 총 매수 금액(주가 X 매매 단위)이 크면 매수가 이루어지지 않음에 유의하자.

print(f'Initial Portfolio Value : {cerebro.broker.getvalue():,.0f} KRW')
cerebro.run() # 8. Cerebro 클래스로 백테스트를 실행한다.
print(f'Final Portfolio Value : {cerebro.broker.getvalue():,.0f} KRW')
cerebro.plot() # 9. 백테스트 결과를 차트로 출력한다.