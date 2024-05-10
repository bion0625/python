import pandas as pd
df = pd.DataFrame({'KOSPI':[1915, 1961, 2026, 2467, 2041]})
print(df)

df = pd.DataFrame({'KOSPI':[1915, 1961, 2026, 2467, 2041],
                  'KOSDAQ':[542, 682, 631, 798, 675]},
                  index=[2014, 2015, 2016, 2017, 2018])
print(df)

print(df.describe())
# count     5.000000    5.000000 #  원소 개수
# mean   2082.000000  665.600000 #  평균
# std     221.117616   92.683871 #  표준편차
# min    1915.000000  542.000000 #  최솟값
# 25%    1961.000000  631.000000 #  제1 사분위수
# 50%    2026.000000  675.000000 #  제2 사분위수
# 75%    2041.000000  682.000000 #  제3 사분위수
# max    2467.000000  798.000000 #  최댓값

print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# Index: 5 entries, 2014 to 2018        # 인덱스 정보
# Data columns (total 2 columns):       # 전체 칼럼 정보
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   KOSPI   5 non-null      int64    # 첫 번째 칼럼 정보    
#  1   KOSDAQ  5 non-null      int64    # 두 번째 칼럼 정보
# dtypes: int64(2)                      # 자료형
# memory usage: 120.0 bytes             # 메모리 사용량

kospi = pd.Series([1915, 1961, 2026, 2467, 2041],
                  index=[2014, 2015, 2016, 2017, 2018], name='KOSPI')
print(kospi)

kosdaq = pd.Series([542, 682, 631, 798, 675],
                   index=[2014, 2015, 2016, 2017, 2018], name='KOSDAQ')
print(kosdaq)

df = pd.DataFrame({kospi.name:kospi, kosdaq.name:kosdaq})
print(df)

columns = ['KOSPI', 'KOSDAQ']
index = [2014, 2015, 2016, 2017, 2018]
rows = []
rows.append([1916, 542])
rows.append([1961, 682])
rows.append([2026, 631])
rows.append([2467, 798])
rows.append([2041, 675])
df = pd.DataFrame(rows, columns=columns, index=index)
print(df)

for i in df.index:
    print(i, df['KOSPI'][i], df['KOSDAQ'][i])

for row in df.itertuples(name='KRX'):
    print(row)

for row in df.itertuples():
    print(row[0], row[1], row[2])

for idx, row in df.iterrows():
    print(idx, row[0], row[1])