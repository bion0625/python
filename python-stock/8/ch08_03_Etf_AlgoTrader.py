# ch08_03_Etf_AlgoTrader.py
import ctypes
import win32com.client

# CREON plus 공통 Object
cpStatus = win32com.client.Dispatch('CpUtil.CpCybos') # 시스템 상태 정보
cpTradeUtil = win32com.client.Dispatch('CpTrade.CpTdUtil') # 주문 관련 도구

# CREON Plus 시스템 점검 함수
def check_creon_system():
    # 관리자 권한으로 프로세스 실행 여부
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print('check_creon_system(): admin user -> FAILED')
        return False;
    
    # 연결 여부 체크
    if (cpStatus.IsConnect == 0):
        print('check_creon_system(): connect to server -> FAILED')
        return False;
    
    # 주문 관련 초기화
    if (cpTradeUtil.TradeInit(0) != 0):
        print('check_creon_system(): init trade -> FAILED')
        return False;
    
    return True;


# 32비트 가상 머신 명령어 저장
# python -m venv {폴더명}
# 주의사항: 해당 명령어를 수행하는 python(w).exe 파일 속성을 관리자 모드로 실행 상태가 되어야 acticate를 포함한 파일들이 전부 생성
# 폴더 생성 후에, cmd로 해당 폴더 아래 Script 폴더 아래 activate 실행하면 가상 머신 상태로 CLI 사용 가능
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

from datetime import datetime

def get_target_price(code):
    try:
        time_now = datetime.now()
        str_today = time_now.strftime('%Y%m%d')
        ohlc = get_ohlc(code, 10) # 1. 인수로 받은 종목의 열흘치 OHLC 데이터를 조회한다.
        # 2. 첫 번째 OHLC 행의 인덱스 날짜가 오늘이면 두 번째 OHLC 행을 어제의 OHLC 데이터로 사용하고
        # 첫 번째 OHLC 행의 인덱스 날짜가 오늘이 아니라면 첫 번째 OHLC 행을 어제의 OHLC 데이터로 사용한다.
        if str_today == str(ohlc.iloc[0].name):
            today_open = ohlc.iloc[0].open # 3. 오늘의 시가는 첫 번째 OHLC 행의 '시가'열을 사용한다.
            lastday = ohlc.iloc[1]
        else:
            lastday = ohlc.iloc[0]
            today_open = lastday[3] # 4. 만일 오늘의 시가가 존재하지 않을 경우 어제의 종가를 대신 사용한다.
        lastday_high = lastday[1]
        lastday_low = lastday[2]
        # 5. 목표 매수가는 오늘 시가 + (어제 최고가 - 어제 최저가 * K)로 계산한다.
        target_price = today_open + (lastday_high - lastday_low) * 0.5
        return target_price
    except Exception as ex:
        dbgout("'get_target_price() -> exception! " + str(ex) + "'")
        return None