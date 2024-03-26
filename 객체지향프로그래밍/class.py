# 클레스

class MyFirstClass:
    clsVar = 'The best way to predict the future is to invent it.'
    def clsMethod(self):
        print(MyFirstClass.clsVar + '\t- Alan Curtis Kay -')

mfc = MyFirstClass() # 인스턴스화
print(mfc.clsVar) # 변수에 접근
print(mfc.clsMethod()) # 클래스 메서드 호출


# 상속

class A:
    def methodA(self):
        print("Calling A's methodA")
    def method(self):
        print("Calling A's method")

class B:
    def methodB(self):
        print("Calling B's methodB")

class C(A, B):
    def methodC(self):
        print("Calling C's methodC")
    def method(self):
        print("Calling C's overidden method")
        super().method()

c = C()
print(c.method())
print(c.methodA())
print(c.methodB())
print(c.methodC())


# 클레스 메서드

class NasdaqStock:
    """Class for NASDAQ stocks""" # 독스트링
    count = 0 # 클레스 변수
    def __init__(self, symbol, price):
        """Constructor for NasdaqStock""" # 독스트링
        self.symbol = symbol # 인스턴스 변수
        self.price = price # 인스턴스 변수
        NasdaqStock.count += 1
        print('Calling __init__({}, {:.2f}) > count: {}'.format(self.symbol, self.price, NasdaqStock.count))
    
    def __del__(self):
        """Destructor for NasdaqStock"""
        print('Calling __del__({})'.format(self))

gg = NasdaqStock('GOOG', 1154.05)
del(gg)
ms = NasdaqStock('MSFT', 102.44)
del(ms)
amz = NasdaqStock('AMZN', 1746.00)
del(amz)

# print(help(NasdaqStock)) //이거 왜 안되지, 파이썬 새로 깔아야 하는 듯 하지만 일단 패스
print(NasdaqStock.__doc__)