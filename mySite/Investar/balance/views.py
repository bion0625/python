# ch07_04_balance_views.py
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

def get_data(symbol):
    url = "https://finance.naver.com/item/sise.nhn?code={}".format(symbol)
    html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
    soup = BeautifulSoup(html, "lxml", from_encoding='euc-kr')
    cur_price = soup.find('strong', id='_nowVal') # 1. id가 '_nowVal'인 <strong> 태그를 찾는다.
    cur_rate = soup.find('strong', id='_rate') # 2. id가 '_rate'인 <strong> 태그를 찾는다.
    stock = soup.find('title') # 3. <title> 태그를 찾는다.
    stock_name = stock.text.split(':')[0].strip() # 4. <title> 태그에서 콜론(':') 문자를 기준으로 문자열을 분리하여 종목명을 구한 뒤 문자열 좌우의 공백문자를 제거한다.
    return cur_price.text, cur_rate.text.strip(), stock_name

def main_view(request):
    querydict = request.GET.copy()
    mylist = querydict.lists() # 5. GET 방식으로 넘어온 QueryDict 형태의 URL을 리스트 형태로 변환한다.
    rows = []
    total = 0

    for x in mylist:
        cur_price, cur_rate, stock_name = get_data(x[0]) # 6. mylist의 종목코드로 get_data 함수를 호출하여 현재가, 등락률, 종목명을 구한다.
        price = cur_price.replace(',', '')
        stock_count = format(int(x[1][0]), ',') # 7. mylist의 종목수를 int형으로 변환한 뒤 천 자리마다 쉼표(',')를 포함하는 문자열로 변환한다.
        sum = int(price) * int(x[1][0])
        stock_sum = format(sum, ',')
        rows.append([stock_name, x[0], cur_price, stock_count, cur_rate, 
            stock_sum]) # 8. 종목명, 종목코드, 현재가, 주식수, 등락률, 평가금액을 리스트로 생성해서 rows 리스트에 추가한다.
        total = total + int(price) * int(x[1][0]) # 9. 평가금액을 주식수로 곱한 뒤 total 변수에 더한다.
    
    total_amount = format(total, ',')
    values = {'rows': rows, 'total': total_amount} # 10. balance.html 파일에 전달할 값들을 values 딕셔너리에 저장한다.
    return render(request, 'balance.html', values) # 11. balance.html 파일을 표시하도록 render() 함수를 호출하면서 인숫값에 해당하는 values 딕셔너리를 넘겨준다.
