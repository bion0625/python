# print(help('modules'))

# print(help('modules time'))

# print(help('datetime')) // 왜 안되지? 환경변수 재설정해야 하는데 귀찮다

import keyword
print(keyword.kwlist)
print(keyword.__file__)

import calendar
print(calendar.month(2020, 1)) # 모듈명(calendar) 생략 불가

from calendar import month
print(month(2020, 1)) # 모듈명(calendar) 생략 가능

import datetime
print(datetime.datetime.now()) # 별칭을 사용하지 않은 경우

from datetime import datetime as dt
print(dt.now()) # 별칭(dt)을 사용한 경우