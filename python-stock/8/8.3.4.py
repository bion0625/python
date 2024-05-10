import win32com.client

cpTradeUtil = win32com.client.Dispatch('CpTrade.CpTdUtil') # 주문 관련 도구
cpCash = win32com.client.Dispatch('CpTrade.CpTdNew5331A') # 주문 가능 금액

def get_current_cash():
    cpTradeUtil.TradeInit()
    acc = cpTradeUtil.AccountNumber[0] # 계좌번호
    accFlag = cpTradeUtil.GoodsList(acc, 1) # -1:전체, 1:주식, 2:선물/옵션
    cpCash.SetInputValue(0, acc) # 계좌번호
    cpCash.SetInputValue(1, accFlag[0]) # 상품 구분 - 주식 상품 중 첫 번째
    cpCash.BlockRequest()

    return cpCash.GetHeaderValue(9) # 증거금 100% 주문 가능 금액