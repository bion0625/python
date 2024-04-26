import win32com.client

cpStock = win32com.client.Dispatch("DsCbo1.StockMst") # 주식 종목별 정보

def get_current_price(code):
    cpStock.SetInputValue(0, code) # 종목코드에 대한 가격 정보
    cpStock.BlockRequest()

    item = {}
    item['cur_price'] = cpStock.GetHeaderValue(11) # 현재가
    item['ask'] = cpStock.GetHeaderValue(16) # 매수호가
    item['bid'] = cpStock.GetHeaderValue(17) # 매도호가

    return item['cur_price'], item['ask'], item['bid']