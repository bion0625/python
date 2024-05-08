# ch09_08_LinearRegression.py
import matplotlib.pylab as plt
import tensorflow as tf

x_data = [1, 2, 3, 4, 5]
y_data = [2, 3, 4, 5, 6] # 1. y = 1 * x + 1 인 데이터를 준비한다.

w = tf.Variable(0.7) # 2. 가중치 w를 임의의 값 0.7로 초기화한다.
b = tf.Variable(0.7) # 3. 편향 b를 임의의 값 0.7로 초기화한다.
learn_rate = 0.01 # 4. 학습률은 보통 0.01 ~ 0.001 사이의 값으로 설정한다.

print(f'step|   w|   b| cost')
print(f'----|----|----|-----')

for i in range(1, 1101): # 7. 1회부터 1100회까지 반복해서 학습한다.
    # 8. with tf.GradientTape() as tape: 내부의 계산 과정을 tape에 기록해두면,
    # 나중에 tape.gradient() 함수를 이용해서 미분값을 구할 수 있다.
    with tf.GradientTape() as tape:
        hypothesis = w * x_data + b # 9. 가설은 w * x + b로 정한다.
        # 10. 손실 비용을 오차제곱평균으로 구한다.
        cost = tf.reduce_mean((hypothesis - y_data)**2)
    dw, db = tape.gradient(cost, [w, b]) # 11. w와 b에 대해 손실을 미분해서 dw, db값을 구한다.
    
    # 12. 텐서플로의 a.assign_sub(b)는 파이썬의 a = a - b와 동일한 연산을 수행한다.
    # w값에서 '학습률 * dw'를 뺀 값을 새로운 w값으로 설정한다.
    w.assign_sub(learn_rate * dw)
    b.assign_sub(learn_rate * dw)
    
    if i in [1, 3, 5, 10, 1000, 1100]:
        print(f'{i:4d}| {w.numpy():.2f}| {b.numpy():.2f}| {cost:.2f}')
        plt.figure(figsize=(7,7))
        plt.title(f'[Step {i:d}] h(x) = { w.numpy():.2f}x + '
            f'{b.numpy():.2f}')
        plt.plot(x_data, y_data, 'o')
        plt.plot(x_data, w * x_data + b, 'r', label='hypothesis')
        plt.xlabel('x_data')
        plt.ylabel('y_data')
        plt.xlim(0, 6)
        plt.ylim(1, 7)
        plt.legend(loc='best')
        plt.show()