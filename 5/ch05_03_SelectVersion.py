# ch05_03_SelectVersion.py
import pymysql

connection = pymysql.connect(host='localhost', port=3306, db='INVESTAR', 
                             user='root', password='snake.land.', autocommit=True) # connect() 함수를 사용해 connection 객체를 생성한다.

cursor = connection.cursor() # cursor() 함수를 사용해 cursor 객체를 생성한다.
cursor.execute("SELECT VERSION();") # cursor 객체의 execute() 함수를 사용해 SELECT문을 실행한다.
result = cursor.fetchone() # cursor 객체의 fetchone() 함수를 사용해 위의 실행 결과를 튜플로 받는다.

print("MariaDB version : {}".format(result))

connection.close()