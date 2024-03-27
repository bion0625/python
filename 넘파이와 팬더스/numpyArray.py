import numpy as np
A = np.array([[1, 2], [3, 4]])
print(A)

print(type(A))

print(A.ndim) # 배열의 차원

print(A.shape) # 배열 크기

print(A.dtype) # 원소 자료형

print(A.max(), A.mean(), A.min(), A.sum())

print(A[0], A[1])

print(A[0,0], A[0,1])

print(A[1][0], A[1][1])

print(A[A>1])

print(A)

print(A.T)

print(A.flatten())

print(A)

# print(np.add(A, A)) 와 같다
print(A + A)

# print(np.subtract(A,A)) 와 같다
print(A - A)

# print(np.multiply(A, A)) 와 같다
print(A * A)

# print(np.divide(A, A)) 와 같다
print(A / A)

print(A)

B = np.array([10, 100])

print(A * B)

print(B.dot(B))

print(A.dot(B))