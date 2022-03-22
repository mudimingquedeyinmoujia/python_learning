import register.datasets

mu={}

class Student():
    def __init__(self):
        print('student init')


class Person():
    def __init__(self):
        print('person init')

mu={'stu':Student,'per':Person}

mu['stu']()