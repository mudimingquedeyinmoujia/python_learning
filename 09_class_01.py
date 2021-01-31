# 类的注释写在类的下面第一行
class Student:
    '''
    this is the class of student
    '''
    def callname(self):
        print("i am a student")

print(Student.__doc__)

# 类里面self是关键，代表类的实例，在类里面的时候，self.xxx是成员变量，而不带self的赋值是类变量
# 下面的例子展示了类变量和成员变量的区别，类变量共享，成员变量各个实例独占
# 实例的引用当然可以使用类变量，但是当实例引用类变量进行赋值的时候并不会改变类变量的值，而是新建一个属于实例自己的与类变量重名的变量
# 总之如果一个实例中的类变量和成员变量重名，优先使用实例变量，因为类变量可以直接用类名进行使用的
class Worker:
    '''
    this is the class of worker
    '''
    class_var=12
    def __init__(self,name="xiaoming"):
        self.name=name
        self.age=10

worker1=Worker(name="yanming")
print(worker1.class_var,Worker.class_var,worker1.name,worker1.age)
worker2=Worker()
worker2.class_var=15
worker2.new_var=14
print(worker1.class_var,worker2.new_var,Worker.class_var)
Worker.class_var=18
print(worker1.class_var,worker2.class_var)