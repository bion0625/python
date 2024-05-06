# ch09_01_StepFunction.py
import numpy as np
import matplotlib.pyplot as plt

def stepfunc(x):
    # 1. x값이 부등식(x <= 0)을 만족하면 0을 반환하고, x값이 부등식을 만족하지 못하면 1을 반환한다.
    return np.where(x < 0, 0, 1)

# 2. x값으로부터 -10부터 9.9까지 0.1 간격의 소수로 이루어진 배열을 준비한다.
# arange() 함수에서 마지막 값은 제외하므로 마지막 값은 9.9이다.
# e + 01은 앞의 수 * 10**1을 의미하고 e + 00은 앞의 수 * 10 **0을 나타낸다.
x = np.arange(-10, 10, 0.1)
y = stepfunc(x)

plt.plot(x, y)
plt.title('step function')
plt.show()