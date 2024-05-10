# ch09_05_SoftmaxFunction.py
import numpy as np
import matplotlib.pyplot as plt

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))

print(softmax([1, 1, 2]))