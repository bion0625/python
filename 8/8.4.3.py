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

import pandas as pd
import win32com.client

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

def get_movingaverage(code, window):
    try:
        time_now = datetime.now()
        str_today = time_now.strftime('%Y%m%d')
        ohlc = get_ohlc(code, 40) # 1. 인수로 받은 두 달치 OHLC 데이터를 조회한다.
        # 2. 첫 번째 OHLC 행의 인덱스 날짜가 오늘이면 두 번째 OHLC 행의 인덱스 날짜를 어제 날짜로 사용하고,
        # 첫 번째 OHLC 행의 인덱스 날짜가 오늘이 아니라면 첫 번째 OHLC 행의 인덱스 날짜를 어제 날짜로 사용한다.
        if str_today == str(ohlc.iloc[0].name):
            lastday = ohlc.iloc[1].name
        else:
            lastday = ohlc.iloc[0].name
        closes = ohlc['close'].sort_index() # 3. 종가 칼럼을 인덱스 날짜 기준으로 오름차순 정렬한다.
        ma = closes.rolling(window=window).mean() # 4. 종가 칼럼의 이동 평균을 구한다.
        return ma.loc[lastday] # 5. 어제에 해당하는 날짜 인덱스를 이용하여 이동 평균값을 구한 뒤 반환한다.
    except Exception as ex:
        dbgout('get_movingaverage() -> exception! ' + str(ex) + "'")
        return None
    
print(get_movingaverage('A005930', 10))