# 类的继承与重载运算符
class Parent:
    def __init__(self, name="parent", age=10):
        self.name = name
        self.age = age

    def __add__(self, other): # 运算符进行重载
        return Parent(name="added parent", age=self.age + other.age)

    def get_age(self):
        return self.age

class Child(Parent): # 在括号里写上父类的名称
    def get_name(self):
        return self.name

father=Parent("xiaoming",34)
wawa=Child("baby",11)
wawa2=Child("baby2",12)
wawa_add=wawa+wawa2
print(wawa_add.get_age())

# 类的私有属性与方法
# 类属性里面,带有__的前缀的为私有属性,带有__的前缀的方法为私有方法
# 私有方法可以是类内部的访问，如下所示
class Apple:
    __private_var=10
    public_var=15
    def public_method(self):
        print("this is public method")
        self.__private_method()

    def __private_method(self):
        print("this is private")

app=Apple()
app.public_method()
# 但是可以强制访问
print(app._Apple__private_var)