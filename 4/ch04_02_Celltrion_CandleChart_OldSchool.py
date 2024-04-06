# ch04_02_Celltrion_CandleChart_OldSchool.py
import pandas as pd
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
from datetime import datetime
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
df = df.iloc[0:30] # 14년간 데이터는 너무 많으므로 최근 데이터 30행만 사용한다.
df = df.sort_values(by='날짜') # 네이버 금융의 데이터가 내림차순으로 되어 있어서 오름차순으로 변경한다.
for idx in range(0, len(df)):
    dt = datetime.strptime(df['날짜'].values[idx], '%Y.%m.%d').date() # 날짜 칼럼의 %Y.%m.%d 형식 문자열을 datetime형으로 변환한다.
    df['날짜'].values[idx] = mdates.date2num(dt) # 위 datetime형을 다시 float형으로 변환한다.
# 날짜(float형). 시가, 고가, 저가, 종가, 칼럼만 갖는 별도의 데이터프레임을 생성한다.
# candlestick_ohlc() 함수를 호출할 때 필요한 두 번째 인수로 사용할 것이다.
ohlc = df[['날짜', '시가', '고가', '저가', '종가']]

# 엠피엘_파이낸스로 캔들 차트 그리기
plt.figure(figsize=(9, 6))
ax = plt.subplot(1, 1, 1)
plt.title('Celltrion (mpl_finance candle stick)')
candlestick_ohlc(ax, ohlc.values, width=0.7, colorup='red', colordown='blue') # candlestick_ohlc() 함수를 이용하여 캔들 차트를 그린다.
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d')) # x축의 레이블 숫자다. %Y-%m-%d 형식 문자열로 변환해서 표시한다.
plt.xticks(rotation=45)
plt.grid(color='gray', linestyle='--')
plt.show()