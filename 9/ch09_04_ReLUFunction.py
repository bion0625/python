# ch09_04_ReLUFunction.py
import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    # 1. 넘파이의 maximum() 함수는 인수로 주어진 수 중에서 가장 큰 수를 반환한다.
    # 따라서 x가 0보다 작거나 같을 때 0을 반환하고, x가 0보다 크면 x를 반환한다.
    return np.maximum(0, x)

x = np.arange(-10, 10, 0.1) # 2. x값으로부터 -10부터 9.9까지 0.1 간격의 소수로 이루어진 배열을 준비한다.
y = relu(x)

plt.plot(x, y)
plt.title('ReLU function')
plt.show()