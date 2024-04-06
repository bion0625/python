# 4.4.3 맨 뒤 페이지 숫자 구하기

from bs4 import BeautifulSoup
import requests
url = 'https://finance.naver.com/item/sise_day.naver?code=068270&page=1'
html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text

# 뷰티풀 수프 생성자의 첫 번째 인수로 HTML/XML, 페이지를 넘겨주고, 두번째 인수로 페이지를 파싱할 방식을 넘겨준다.
bs = BeautifulSoup(html, 'lxml')

# find 함수를 통해서 class 속성이 'pgRR'인 td 태그를 찾으면, 결괏값은 "bs4.element.Tag" 타입으로 pgrr 변수에 반환된다.
# 'pgRR'은 Page Right Right 즉, 맨 마지막 (오른쪽) 페이지를 의미한다.
# find() 함수의 인수인 class 속성을 굳이 class_로 적은 이유는 파이썬에 이미 class라는 지시어가 존재하기 때문에,
# 인터프리터가 구분할 수 있도록 하기 위함이다.
pgrr = bs.find('td', class_='pgRR')
print(pgrr.a['href'])
print(pgrr.prettify())
print(pgrr.text)

s = str(pgrr.a['href']).split('=') # pgrr.a['href]로 구한 문자열을 '=' 문자를 기준으로 split() 함수로 분리해 3개 문자열을 리스트로 얻었다.
# s는 ['/item/sise_day.naver?code', '068270&page', '463']

last_page = s[-1] # 리스트 제일 마지막 원소가 바로 구하려는 전체 페이지 수다.