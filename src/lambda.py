# 需要一个参数，后跟一个表 lambda 达式作为函数体，这一表达式执行的值将作为这个新函数的返回值

points=[{'x':2,'y':3},{'x':4,'y':1}]
points.sort(key=lambda i:i['y'])
print(points)


class Person:
pass # 一个空的代码块
p = Person()
print(p)