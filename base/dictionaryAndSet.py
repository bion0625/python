crispr = {'EDIT':'Editas Medicine', 'NTLA':'Intellia Therapeutics'};

# error
# print(crispr[1])

print(crispr)

print(crispr['EDIT'])

crispr['CRSP'] = 'CRISPR Therapeutics'

print(crispr)

for x in crispr:
    print('%s : %s' % (x, crispr[x])) # old school format

for x in crispr:
    print("{} : {}".format(x, crispr[x]))

for x in crispr:
    print(f"{x} : {crispr[x]}")

s = {'a', 'p', 'p', 'l', 'e'} # SET 중복을 허용하지 않음
print(s)
mySet = {'B', 6, 1, 2}
print(mySet) # SET은 순서도 지맘대로

if 'B' in mySet:
    print(f"'B' exists in {mySet}")

setA = {1,2,3,4,5}
setB = {3,4,5,6,7}

print(setA & setB)
print(setA | setB)
print(setA - setB)
print(setB - setA)

s = {} # 빈 dictionary
s = set() # 빈 set

ls = [1,3,5,2,2,3,4,2,1,1,1,5]
print(set(ls))
print(list(set(ls)))

import timeit

iteration_test = """
for i in itr :
    pass
"""

l = timeit.timeit(iteration_test, setup='itr= list(range(10000))', number=1000)
t = timeit.timeit(iteration_test, setup='itr= tuple(range(10000))', number=1000)
s = timeit.timeit(iteration_test, setup='itr= set(range(10000))', number=1000)

print(f'l: {l}')
print(f't: {t}')
print(f's: {s}')

# 순환 속도는 비슷

search_test = """
import random
x = random.randint(0, len(itr)-1)
if x in itr :
    pass
"""

s = timeit.timeit(search_test, setup='itr = set(range(10000))', number=1000)
l = timeit.timeit(search_test, setup='itr = list(range(10000))', number=1000)
t = timeit.timeit(search_test, setup='itr = tuple(range(10000))', number=1000)

print(f's: {s}')
print(f'l: {l}')
print(f't: {t}')

# 검색은 SET이 압도적으로 빠름