class Person:
    pass # 一个空的代码块

p=Person()
print(p)


class Person2:
    def say_hi(self):
        print('Hello,how are you?')


p=Person2()
p.say_hi()


class Person3:
    def __init__(self, name):
        self.name=name
    def say_hi(self):
        print('Hello,my name is',self.name)


p=Person3('Kyle')
p.say_hi()
