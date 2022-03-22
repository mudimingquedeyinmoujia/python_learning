import torch
import numpy as np

# filter返回一个迭代器对象，想要变成list在前面加上list即可
a = [12,3,23,121,45,1,2]

print(filter(lambda p: p > 6, a))


def is_odd(n):
    return n % 2 == 1


newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(newlist))