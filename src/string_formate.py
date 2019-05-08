#print 总是会以一个不可见的“新一行”字符（ \n ）结尾

age=20
name='kyle'

print('{0} was {1} years old when he wrote this book'.format(name,age))
print('Why is {0} playing that python?'.format(name))

print('{} was {} years old when he wrote this book'.format(name,age))
print('Why is {} playing that python?'.format(name))

#对于浮点数 '0.333' 保留小数点（.） 后三位
print('{0:.3f}'.format(1.0/3))
#使用下划线填充文本，并保持文本处于中间位置
#使用(^) 定义 ’____hello____‘字符长度为11
print('{0:^11}'.format('hello'))
print('{0:_^11}'.format('hello'))
#基于关键词输出，’Swaroop wrote A Byte of Python‘
print('{name} wrote {book}'.format(name=name,book='A byte of python'))#’=‘前面的name 必须要有，类似于匿名参数
print('my name=', end='')
print('kyle', end='')
print(' Li')
#如果你需要指定一些未经过特殊处理的字符串，比如转义序列，那么你需要在字符串前增加 r 或 R 来指定一个 原始（Raw） 字符串
print("Newlines are indicated by \n")
print(r"Newlines are indicated by \n")