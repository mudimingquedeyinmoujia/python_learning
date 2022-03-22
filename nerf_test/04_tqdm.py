# from tqdm import  tqdm
# list_a=[i for i in range(1000)]
# a=1
# for ele in tqdm(list_a):
#     for i in range(1000000):
#         a=a+i


from tqdm import tqdm, trange
import time

a = [1, 2, 3]

for i in tqdm(a):
    print('打印a[%d]：' % (i - 1), i)
    time.sleep(5)


for i in trange(1, 4):
    print('第%d次执行' % i)
    time.sleep(5)