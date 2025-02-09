import numpy as np
from spyder_kernels.utils.lazymodules import numpy

low = 0.0
high = 2.0
n = 100000

random_x = np.random.uniform(low, high, n)
random_y = np.random.uniform(low, high, n)


def in_big_circle(x, y):
    return x ** 2 + y ** 2 <= 4


def in_small_circle(x, y):
    return (x - 1) ** 2 + (y - 1) ** 2 <= 1


m = 0

for i in range(n):
    x = random_x[i]
    y = random_y[i]
    # print(in_big_circle(x, y))
    # print(x, y)
    if in_small_circle(x, y) and not in_big_circle(x, y):
        m += 1


s = 4 * m / n
print(f'the area of the shadow is {s}')