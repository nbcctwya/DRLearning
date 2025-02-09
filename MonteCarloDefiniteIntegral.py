import numpy as np

# 求函数f(x)在区间[a,b]上的定积分f=
a = 0.8
b = 3.0
n = 10


def f(x):
    return 1 / (np.sin(x) * (np.log(x) ** 2))


random_x = np.random.uniform(a, b, n)
random_y = f(random_x)
print(random_x)
print(random_y)
average_y = np.sum(random_y) / n
s = average_y * (b - a)
print(f'The definite integral of function fx on the interval [a,b] is {s}')