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
    
    
dbgout('This is test log')