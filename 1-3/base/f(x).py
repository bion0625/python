# 정수형
i = 3
print(type(i))

f = 1.0
print(type(f))

# 정수형과 실수형의 계산 결과는 실수형으로 처리된다.

var = i * f
print('{} : {}'.format(var, type(var)))

googol = 10 ** 100 # pow(10, 100)
print(type(googol))
print(googol)

s = 'string' # 문자열
print(type(s))
print(dir(s))

print(help('keywords'))

# 연평균 성장률(처음 값, 마지막 값, 처음 값과 마지막 값 사이의 연(year) 수)
def getCAGR(first, last, years):
    return (last/first)**(1/years) - 1

# 삼성전자 1998-04-27~2018-04-27
cagr = getCAGR(65300, 2669000, 20)
print("SEC CAGR : {:.2%}".format(cagr))


def func1():
    pass

def func2():
    pass

def func3():
    pass

print(func1());print(func2());print(func3()); # 반환갑싱 없을 때는 None 반환

print(func1() == None)
print(func1() is None)

def myFunc():
    var1 = 'a'
    var2 = [1,2,3]
    var3 = max
    return var1, var2, var3 # 여러 개의 결괏값은 기본적으로 튜플 타입으로 반환된다.

print(myFunc());

s, l, f = myFunc()

print(s)
print(l)
print(f)

insertComma = lambda x : format(x, ',')
print(insertComma(1234567890))

abs = 1
abs(-100)