import re
start_date = "2020 year 8/30"
start_lst = re.split('\D+', start_date) # 정규표현식 /D+로 분리하면 연, 월, 일에 해당하는 숫자만 남게 된다.
start_year = int(start_lst[0])
start_month = int(start_lst[1])
start_day = int(start_lst[2])

# 분리된 연, 월, 일을 다시 {:04d}-{:02d}-{:02d} 형식 문자열로 구성하면 DB에서 저장된 날짜 형식과 같게 된다.
# {:02d}는 2자리 숫자로 표시하되 앞 자리가 비었으면 0으로 채우라는 뜻이다.
start_date = f"{start_year:04d}-{start_month:02d}-{start_day:02d}"
print("start_date: ", start_date)