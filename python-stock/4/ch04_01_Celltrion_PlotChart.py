# ch04_01_Celltrion_PlotChart.py
import pandas as pd
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

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
    df = pd.concat([df, pd.read_html(html, header=0, encoding='euc-kr')[0]])

# 차트 출력을 위해 데이터프레임 가공하기
df = df.dropna()
df = df.iloc[0:30] # 14년간 데이터는 너무 많으므로 최근 데이터 30행만 사용한다.
df = df.sort_values(by='날짜') # 네이버 금융의 데이터가 내림차순으로 되어 있어서 오름차순으로 변경한다.

# 날짜, 종가 칼럼으로 차트 그리기
plt.title('Celltrion (close)')
plt.xticks(rotation=45) # x축 레이블의 날짜가 겹쳐서 보기에 어려우므로 90도로 회전하여 표시한다.
plt.plot(df['날짜'], df['종가'], 'co-') # x축은 날짜 데이터로 y축은 종가 데이터로 출력한다. co는 좌표를 청록색(cyan) 원으로, -는 각 좌표를 실선으로 연결해서 표시하는 의미다.
plt.grid(color='gray', linestyle='--')
plt.show()