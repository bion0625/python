import win32com.client
obj = win32com.client.Dispatch("DsCbo1.StockMst") # 1. 주식마스터 (StockMst) Com 객체를 생성한다
obj.SetInputValue(0, 'A005930') # 2. SetInputValue() 함수로 조회할 데이터를 삼성전자(A005930)로 지정한다.
obj.BlockRequest() # 3. BlockRequest() 함수로 삼성전자에 대한 블록 데이터를 요청한다.
sec = {}
sec['현재가'] = obj.GetHeaderValue(11) # 4. GetHeaderValue() 함수로 현재가 정보(11)를 가져와서 sec 딕셔너리에 넣는다.
sec['전일대비'] = obj.GetHeaderValue(12) # 5. GetHeaderValue() 함수로 전일대비 가격변동 정보(12)를 가져와서 sec 딕셔너리에 넣는다.