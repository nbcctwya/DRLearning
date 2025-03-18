import numpy as np

low = -1.0
high = 1.0
n = 1000000  # 随机数个数

# 估计Pi的值
random_x = np.random.uniform(low, high, n)
random_y = np.random.uniform(low, high, n)

m = 0

for i in range(n):
    x = random_x[i]
    y = random_y[i]
    if x ** 2 + y ** 2 <= 1:
        m += 1

pi = 4 * m / n
print(f'pi is {pi}')