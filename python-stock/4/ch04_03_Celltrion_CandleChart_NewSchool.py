# ch04_03_Celltrion_CandleChart_NewSchool.py
import pandas as pd
import requests
from bs4 import BeautifulSoup
import mplfinance as mpf
from io import StringIO


# 맨 뒤 페이지 숫자 구하기
url = 'https://finance.naver.com/item/sise_day.naver?code=068270&page=1'
html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
bs = BeautifulSoup(html, 'lxml')
pgrr = bs.find('td', class_='pgRR')
s = str(pgrr.a['href']).split('=')
last_page = s[-1]

# 전체 페이지 읽어오기
df = pd.DataFrame()
sise_url='https://finance.naver.com/item/sise_day.naver?code=068270'
for page in range(1, int(3)+1): # last_page -> 3으로 변경 (3페이지면 30개 될 것으로 보임)
    url= '{}&page={}'.format(sise_url, page)
    html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
    df = pd.concat([df, pd.read_html(StringIO(html), header=0, encoding='euc-kr')[0]])

# 차트 출력을 위해 데이터프레임 가공하기
df = df.dropna()
df = df.iloc[0:30] # 
df = df.rename(columns={'날짜': 'Date', '시가': 'Open', '고가': 'High', '저가': 'Low', '종가': 'Close', '거래량': 'Volume'}) #
df = df.sort_values(by='Date') #
df.index = pd.to_datetime(df.Date) #
df = df[['Open', 'High', 'Low', 'Close', 'Volume']] #


# 엠피엘파이낸스로 캔들 차트 그리기
# 캔들 차트 버전
mpf.plot(df, title='Celltrion candle chart', type='candle')

# ohlc 버전
# mpf.plot(df, title='Celltrion ohlc chart', type='ohlc')

# 이동 평균선 버전
# kwargs = dict(title='Celltrion customized chart', type='candle', mav=(2, 4, 6), volume=True, ylabel='ohlc candles') # kwargs는 keyword arguments의 약자이며, mpf.plot() 함수를 호출할 때 쓰이는 여러 인수를 담는 딕셔너리다.
# mc = mpf.make_marketcolors(up='r', down='b', inherit=True) # 마켓 색상은 스타일을 지정하는 필수 객체로서, 상승은 빨간색(red)으로 하락은 파란색(blue)으로 지정하고, 관련 색상은 이를 따르도록 한다.
# s = mpf.make_mpf_style(marketcolors=mc) # 마켓 색상을 인수로 넘겨줘서 스타일 객체를 생성한다.
# mpf.plot(df, **kwargs, style=s) # 셀트리온 시세 OHLCV 데이터와 kwargs로 설정한 인수들과 스타일 객체를 인수로 넘겨주면서 mpf.plot() 함수를 호출하여 차트를 출력한다.