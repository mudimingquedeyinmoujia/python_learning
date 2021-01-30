# 用于浮点数运算
import math
# 用于复数运算
import cmath

# ceil向上取整数，floor向下取整数，必须静态调用，无法直接使用
print(abs(-10))
print(abs(-10.))
print(abs(-10.1))
print(math.fabs(-10.1))
print(math.ceil(9.5))
print(math.floor(9.5))

# max 与 min 函数取得list最大最小值
print(math.sqrt(4))
print(max([1,2,4,2,1,6,32,2]))
print(min([i+3 for i in range(10)]))

# 关于随机数的实验
print("about random ")
import random
print(random.choice([1,2,3,4,5,6])) # 从序列随机挑选
print(random.choice([1,2,3,4,5,6]))
print(random.random()*100) # 注意这里是[0,1)范围
print(random.random()*100)
print(random.uniform(0,1)) # 注意这里是[0,1] 右边可以取到
lst_pre=[1,2,3,4,5]
random.shuffle(lst_pre) # 使用shuffle函数，可以改变list的内存数值，打乱随机组合
print(lst_pre)

# 三角函数如下
print("triangle function is shown below")
print(math.sin(math.pi/2))
print(math.degrees(math.pi/2))

