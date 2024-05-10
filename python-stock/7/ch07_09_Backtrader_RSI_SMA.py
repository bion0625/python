# ch07_09_Backtrader_RSI_SMA.py
# backtrader 버전 이슈 대문에 아래 링크 참조해서 해결
# https://stackoverflow.com/questions/60715059/python-backtrader-error-filenotfounderror-errno-2-no-such-file-or-directory
from datetime import datetime # 버전 이슈로 안 쓰게 됨
import backtrader as bt
import yfinance as yf # 버전이슈로 추가

class MyStrategy(bt.Strategy):
    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None
        self.buyprice = None
        self.buycomm = None
        self.rsi = bt.indicators.RSI_SMA(self.data.close, period=21)

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        if order.status in [order.Completed]: 
            if order.isbuy():
                self.log(f'BUY : 주가 {order.executed.price:,.0f}, '
                         f'수량 {order.executed.size:,.0f}, '
                         f'수수료 {order.executed.comm:,.0f} '
                         f'자산 {cerebro.broker.getvalue():,.0f}')
                self.price = order.executed.price
                self.buycomm = order.executed.comm
            else:
                self.log(f'SELL : 주가 {order.executed.price:,.0f}, '
                         f'수량 {order.executed.size:,.0f}, '
                         f'수수료 {order.executed.comm:,.0f} '
                         f'자산 {cerebro.broker.getvalue():,.0f}')
            self.bar_executed = len(self)
        elif order.status in [order.Canceled]:
            self.log('ORDER CANCELD')
        elif order.status in [order.Margin]:
            self.log('ORDER MARGIN')
        elif order.status in [order.Rejected]:
            self.log('ORDER REJECTED')
        self.order = None

    def next(self):
        if not self.position:
            if self.rsi < 30:
                self.order = self.buy()
        else:
            if self.rsi > 70:
                self.order = self.sell()
            
    def log(self, txt, dt=None):
        dt = self.datas[0].datetime.date(0)
        print(f'[{dt.isoformat()}] {txt}')

cerebro = bt.Cerebro()
cerebro.addstrategy(MyStrategy)

# 버전 이슈로 로직 변경
data = bt.feeds.PandasData(dataname=yf.download("036570.KS",
                                            start="2023-01-01", end="2024-04-11"))

cerebro.adddata(data)
cerebro.broker.setcash(10000000)
cerebro.broker.setcommission(commission=0.0014)
cerebro.addsizer(bt.sizers.PercentSizer, percents=90)

print(f'Initial Portfolio Value : {cerebro.broker.getvalue():,.0f} KRW')
cerebro.run()
print(f'Final Portfolio Value : {cerebro.broker.getvalue():,.0f} KRW')
cerebro.plot(style='candlestick')