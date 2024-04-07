import pymysql
import pandas as pd
import requests
from io import StringIO
from datetime import datetime

# 05_StockPriceAPI/Investar/DBUpdater.py
class DBUpdater:
    def __init__(self): # DBUpdater의 생성자 내부에서 마리아디비에 연결한다.
        """생성자: MariaDB 연결 및 종목코드 딕셔너리 생성"""
        self.conn = pymysql.connect(host='localhost', user='root', 
                                    password='snake.land.', db='INVESTAR', charset='utf8') 
        # connect() 함수를 호출할 때 charset='utf8'로 인코딩 형식을 미리 지정해주어야 한다.
        
        with self.conn.cursor() as curs: # 이미 존재하는 테이블에 CREATE TABLE 구문을 하용하면 오류가 발생하면서 프로그램이 종료되므로 IF NOT EXISTS 추가
            sql = """
            CREATE TABLE IF NOT EXISTS company_info (
                code VARCHAR(20),
                company VARCHAR(40),
                last_update DATE,
                PRIMARY KEY (code))
            """
            curs.execute(sql)
            sql = """
            CREATE TABLE IF NOT EXISTS daily_price (
                code VARCHAR(20),
                date DATE,
                open BIGINT(20),
                high BIGINT(20),
                low BIGINT(20),
                close BIGINT(20),
                diff BIGINT(20),
                volume BIGINT(20),
                PRIMARY KEY (code, date))
            """
            curs.execute(sql)
        self.conn.commit()

        self.codes = dict()
        self.update_comp_info() # KRX 주식 코드를 읽어와서 마리아의 company_info 테이블에 업데이트 한다.
    
    def __del__(self):
        """소멸자:MariaDB 연결 해제"""
        self.conn.close()

    def read_krx_code(self): # KRX로부터 상장법인 목록 파일을 읽어온다.
        """KRX로부터 상장법인목록 파일을 읽어와서 데이터프레임으로 변환"""
        url = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13'
        html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
        krx = pd.read_html(StringIO(html), encoding='euc-kr')[0] # 상장법인목록.xls 파일을 read_html() 함수로읽는다.
        krx = krx[['종목코드', '회사명']] # 종목코드 칼럼과 회사명만 남긴다. 데이터프레임에 [[]]을 사용하면 특정 칼럼만 뽑아서 원하는 순서대로 재구성할 수 있다.
        krx = krx.rename(columns={'종목코드': 'code', '회사명': 'company'}) # 한글 칼럼명을 영문 칼럼명으로 변경한다.
        krx.code = krx.code.map('{:06d}'.format) # 종목코드 형식을 {:06d} 형식의 문자열로 변경한다.
        return krx
    
    def update_comp_info(self):
        """종목코드를 company_info 테이블에 업데이트한 후 딕셔너리에 저장"""
        sql = "SELECT * FROM company_info"
        df = pd.read_sql(sql, self.conn) # company_info 테이블을 read_sql() 함수로 읽는다.
        for idx in range(len(df)):
            self.codes[df['code'].values[idx]]=df['company'].values[idx] # 위에서 읽은 데이터프레임을 이용해서 종목코드와 회사명으로 codes 딕셔너리를 만든다.
        with self.conn.cursor() as curs:
            sql = "SELECT max(last_update) FROM company_info"
            curs.execute(sql)
            rs = curs.fetchone() # SELECT max() ~ 구문을 이용해서 DB에서 가장 최근 업데이트 날짜를 가져온다.
            today = datetime.today().strftime('%Y-%m-%d')

            if rs[0] == None or rs[0].strftime('%Y-%m-%d') < today: # 위에서 구한 날짜가 존재하지 않거나 오늘보다 오래된 경우에만 업데이트한다.
                krx = self.read_krx_code() # KRX 상장기업 목록 파일을 읽어서 rkx 데이터프레임에 저장한다.
                for idx in range(len(krx)):
                    code = krx.code.values[idx]
                    company = krx.company.values[idx]
                    sql = f"REPLACE INTO company_info (code, company, last"\
                    f"_update) VALUES('{code}', '{company}', '{today}')"
                    curs.execute(sql) # REPLACE INTO 구문을 이용해서 '종목코드, 회사명, 오늘날짜' 행을 DB에 저장한다.
                    self.codes[code] = company # codes 딕셔너리에 '키~값'으로 종목코드와 회사명을 추가한다.
                    tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
                    print(f"[{tmnow}] {idx:04d} REPLACE INTO company_info"\
                          f"VALUES ({code}, {company}, {today})")
                self.conn.commit()
                print('')

    def read_naver(self, code, company, pages_to_fetch):
        """네이버 금융에서 주식 시세를 읽어서 데이터프레임으로 반환"""
    
    def replace_info_db(self, df, num, code, company):
        """네이버 금융에서 읽어온 주식 시세를 DB에 REPLACE"""
    
    def update_daily_price(self, pages_to_fetch):
        """KRX 상장법인의 주식 시세를 네이버로부터 읽어서 DB에 업데이트"""
    
    def execute_daily(self):
        """실행 즉시 및 매밀 오후 다섯시에 daily_price 테이블 업데이트"""

if __name__ == '__main__':
    dbu = DBUpdater() # DBUpdater.py가 단독으로 실행되면 DBUpdater 객체를 생성한다.
    dbu.update_comp_info() # company_info 테이블에 오늘 업데이트된 내용이 있는지 확인하고, 없으면 company_info 테이블에 업데이트하고 codes 딕셔너리에도 저장한다.