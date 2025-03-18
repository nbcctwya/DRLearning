from numpy.random import choice

samples = choice(['R', 'G', 'B'], size=100, p=[0.2, 0.5, 0.3])
print(samples)
total = {'R': 0, 'G': 0, 'B': 0}
# 输出各种颜色出现次数
for sample in samples:
    total[sample] += 1
print(total)