# ch09_02_SigmoidFunction.py
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    # 1. 넘파이의 exp(x) 함수는 e**x를 구하는 지수함수다 (e는 자연상수).
    # x값이 0으로부터 음수 방향으로 멀어지면 분모(1 + np.exp(-x))의 값이 커지므로 y값은 0에 가까워진다.
    # x값이 0으로부터 양수 방향으로 멀어지면 exp(-x)가 0에 가까워지므로 y값은 1에 가까워진다.
    return 1 / (1 + np.exp(-x))

# 2. x값으로 -10부터 9.9까지 0.1 간격의 소수로 이루어진 배열을 준비한다.
# -1.00000000e + n은 -1.00000000 * 10**n 을 의미하므로, x의 첫 번째 수 -1.00000000e + 01은 -1.00000000 * 10**1이 되어 -10을 나타낸다.
x = np.arange(-10, 10, 0.1)
y = sigmoid(x)

plt.plot(x, y)
plt.title('sigmoid function')
plt.show()