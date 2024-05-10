import win32com.client
import pandas as pd

cpOhlc = win32com.client.Dispatch("CpSysDib.StockChart") # OHLC 정보

def get_ohlc(code, qty):
    cpOhlc.setInputValue(0, code) # 종목코드
    cpOhlc.setInputValue(1, ord('2')) # 1:기간, 2:개수
    cpOhlc.setInputValue(4, qty) # 요청 개수
    cpOhlc.setInputValue(5, [0, 2, 3, 4, 5]) # 0:날짜, 2~5:OHLC
    cpOhlc.setInputValue(6, ord('D')) # D:일단위
    cpOhlc.setInputValue(9, ord('1')) # 0:무수정주가, 1:수정주가
    cpOhlc.BlockRequest()
    
    count = cpOhlc.GetHeaderValue(3) # 3:수신 개수
    columns = ['open', 'high', 'low', 'close']
    index = []
    rows = []
    
    for i in range(count): # 1. count값은 수신한 데이터 개수를 의미하며, 인수로 받은 qty값과 동일해야 정상값이다.
        index.append(cpOhlc.GetDataValue(0, i)) # 2. 첫 번째 칼럼에서 날짜 데이터를 구해서 index 리스트에 추가한다.
        # 3. 두 번째 칼럼부터 시가, 고가, 저가, 종가 데이터를 차례로 구해서 rows 리스트에 추가한다.
        rows.append([cpOhlc.GetDataValue(1, i), cpOhlc.GetDataValue(2, i),cpOhlc.GetDataValue(3, i), cpOhlc.GetDataValue(4, i)])
        
    # 4. 날짜 데이터를 인덱스로 갖고 OHLC를 각각의 칼럼으로 갖는 데이터 프레임을 생성한다.
    df = pd.DataFrame(rows, columns=columns, index=index)
    return df