import pandas as pd
s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0])
print(s)

s.index = pd.Index([0.0, 1.2, 1.8, 3.0, 3.6, 4.8]) # 인덱스 변경
s.index.name = 'MY_IDX' # 인덱스 명 설정

print(s)

s.name = 'MY_SERIES'

print(s)

s[5.9] = 5.5

print(s)

ser = pd.Series([6.7, 4.2], index=[6.8, 8.0])
s = pd.concat([s, ser])

print(s)

print(s.index[-1])

print(s.values[-1])

print(s.loc[8.0]) # 로케이션 인덱서

print(s.iloc[-1]) # 인티저 로케이션 인덱서

print(s.values[:])

print(s.iloc[:])

print(s.drop(8.0))

print(s.describe())

# count    9.000000 # 원소 개수
# mean     4.444444 # 평균
# std      2.430078 # 표준편차
# min      0.000000 # 최솟값
# 25%      3.600000 # 제1 사분위수
# 50%      4.200000 # 제2 사분위수
# 75%      5.800000 # 제3 사분위수
# max      8.000000 # 최댓값

import pandas as pd
s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0, 5.5, 6.7, 4.2]) # 시리즈 생성
s.index = pd.Index([0.0, 1.2, 1.8, 3.0, 3.6, 4.8, 5.9, 6.8, 8.0]) # 시리즈 인덱스
# 변경
s.index.name = 'MY_IDX' # 시리즈 인덱스명 설정
s.name = 'MY_SERIES' # 시리즈 이름 설정

import matplotlib.pyplot as plt
plt.title("ELLIOTT_WAVE")
plt.plot(s, "bs--") # 시리즈를 bs--(푸른 사각형과 점선) 형태로 출력
plt.xticks(s.index) # x축의 눈금값을 s 시리즈의 인덱스값으로 설정
plt.yticks(s.values) # y축의 눈금값을 s 시리즈의 데이터값으로 설정
plt.grid(True)
plt.show()