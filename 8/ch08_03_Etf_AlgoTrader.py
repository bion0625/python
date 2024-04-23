# ch08_03_Etf_AlgoTrader.py
import ctypes
import win32com.client

# CREON plus 공통 Object
cpStatus = win32com.client.Dispatch('CpUtil.CpCybos') # 시스템 상태 정보
cpTradeUtil = win32com.client.Dispatch('CpTrade.CpTdUtil') # 주문 관련 도구

# CREON Plus 시스템 점검 함수
def check_creon_system():
    # 관리자 권한으로 프로세스 실행 여부
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print('check_creon_system(): admin user -> FAILED')
        return False;
    
    # 연결 여부 체크
    if (cpStatus.IsConnect == 0):
        print('check_creon_system(): connect to server -> FAILED')
        return False;
    
    # 주문 관련 초기화
    if (cpTradeUtil.TradeInit(0) != 0):
        print('check_creon_system(): init trade -> FAILED')
        return False;
    
    return True;


# 32비트 가상 머신 명령어 저장
# python -m venv {폴더명}
# 주의사항: 해당 명령어를 수행하는 python(w).exe 파일 속성을 관리자 모드로 실행 상태가 되어야 acticate를 포함한 파일들이 전부 생성
# 폴더 생성 후에, cmd로 해당 폴더 아래 Script 폴더 아래 activate 실행하면 가상 머신 상태로 CLI 사용 가능