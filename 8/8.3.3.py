import slack_sdk
from datetime import datetime

# 1. '07장 장고 웹 서버 구축 및 자동화'에서 발급한 토큰을 입력한다.
slack = slack_sdk.WebClient(token="") # 슬랙 봇 토큰


def dbgout(message):
    # 2. datetime.now() 함수로 현재 시간을 구한 후 [월/일 시:분:초] 형식으로 출력 후
    # 한 칸 띄우고 함수 호출 시 인수로 받은 message 문자열을 출력한다.
    print(datetime.now().strftime('[%m/%d %H:%M:%S]'), message)
    strbuf = datetime.now().strftime('[%m/%d %H:%M:%S] ') + message
    # 3. #etf-algo-trading 채널로 메시지를 보내려면 워크스페이스에 etf-algo-trading 채널을 미리 만들어둬야 한다.
    # 별도의 채널을 만들기 #etf-algo-trading 대신 #general을 인수로 주어 일반 채널로 메시지를 보내도 된다.
    slack.chat_postMessage(channel="#etf-algo-trading", text=strbuf)

def printlog(message, *arg):
    print(datetime.now().strftime('[%m/%d %H:%M:%S]'), message, *arg)
    
    
import win32com.client

cpTradeUtil = win32com.client.Dispatch('CpTrade.CpTdUtil') # 주문 관련 도구
cpBalance = win32com.client.Dispatch('CpTrade.CpTd6033') # 계좌 정보
cpCodeMgr = win32com.client.Dispatch('CpUtil.CpStockCode') # 종목 코드

def get_stock_balance(code):
    cpTradeUtil.TradeInit()
    acc = cpTradeUtil.AccountNumber[0] # 계좌번호
    accFlag = cpTradeUtil.GoodsList(acc, 1) # -1:전체, 1:주식, 2:선물/옵션
    cpBalance.SetInputValue(0, acc) # 계좌번호
    cpBalance.SetInputValue(1, accFlag[0]) # 상품 구분 - 주식 상품 중 첫 번째
    cpBalance.SetInputValue(2, 50) # 요청 건수(최대 50)
    cpBalance.BlockRequest()

    if code == 'ALL':
        dbgout('계좌명: ' + str(cpBalance.GetHeaderValue(0)))
        dbgout('결제잔고수량: ' + str(cpBalance.GetHeaderValue(1)))
        dbgout('평가금액: ' + str(cpBalance.GetHeaderValue(3)))
        dbgout('평가손익: ' + str(cpBalance.GetHeaderValue(4)))
        dbgout('종목수: ' + str(cpBalance.GetHeaderValue(7)))
    
    stocks = []
    for i in range(cpBalance.GetHeaderValue(7)):
        stock_code = cpBalance.GetDataValue(12, i) # 종목코드
        stock_name = cpBalance.GetDataValue(0, i) # 종목명
        stock_qty = cpBalance.GetDataValue(15, i) # 수량
        if code == 'ALL':
            dbgout(str(i+1) + ' ' + stock_code + '(' + stock_name + ')'
                   + ':' + str(stock_qty))
            stocks.append({'code': stock_code, 'name': stock_name, 
                           'qty': stock_qty})
        if stock_code == code:
            return stock_name, stock_qty
    if code == 'ALL':
        return stocks
    else:
        stock_name = cpCodeMgr.CodeToName(code)
        return stock_name, 0