# ch09_03_TanhFunction.py
import numpy as np
import matplotlib.pyplot as plt

def tanh(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

x = np.arange(-10, 10, 0.1) # 1. x값으로부터 -10부터 9.9까지 0.1 간격의 소수로 이루어진 배열을 준비한다.
y = tanh(x) # 2. 넘파이에서 제공하는 np.tanh() 함수를 사용해도 결과는 동일하다.

plt.plot(x, y)
plt.title('tanh function')
plt.show()