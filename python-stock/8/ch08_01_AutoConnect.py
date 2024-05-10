# ch08_01_AutoConnect.py
from pywinauto import application
import os, time

# 1. 프로세스 종료 명령 taskkill로 실행중인 크레온 관련 프로세스(coStarter.exe, CpStart.exe, DibServer.exe)를 종료했다.
os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('taskkill /IM DibServer* /F /T')

# 2. WMIC는 윈도우 시스템 정보를 조회하거나 변경할 때 사용하는 명령이다.
# 크레온 프로그램은 강제 종료 신호를 받으면 확인 창을 띄우기 때문에 강제로 한 번 더 프로세스를 종료해야 한다.
os.system('wmic process where "name like \'%coStarter\'" call terminate')
os.system('wmic process where "name like \'%CpStart\'" call terminate')
os.system('wmic process where "name like \'%DibServer\'" call terminate')

time.sleep(5)
app = application.Application()
# 3. 파이윈오토를 이용하여 크래온 프로그램(coStarter.exe)을 크레온 플러스 모드(/prj:cp)로 자동으로 시작한다.
# 사용자 ID(id:), 암호(/pwd:), 공인인증서 암호(/pwdcert:)를 실행 인수로 지정해 놓으면 로그인 창에 자동으로 입력된다.
app.start('C:\CREON\STARTER\coStarter.exe /prj:cp '
          '/id:/pwd:/pwdcert:/autostart')
time.sleep(60)