import pandas as pd
krx_list = pd.read_html('4/상장법인목록.xls')
krx_list[0].종목코드 = krx_list[0].종목코드.map('{:06d}'.format)
print(krx_list[0])

# 더 나은 방법 찾아서 추가
# import requests
# from io import StringIO

# html = requests.get('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', headers={'User-agent': 'Mozilla/5.0'}).text
# html = StringIO(html)

df = pd.read_html(html, encoding='euc-kr')[0]
df['종목코드'] = df['종목코드'].map('{:06d}'.format)
df = df.sort_values(by='종목코드')
print(df)