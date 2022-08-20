li=[]

for i in [1,2,3]:
    li.append(lambda x:x*i)
print(li[0](3))