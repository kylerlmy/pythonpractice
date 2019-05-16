L=[1,2,3]

it=iter(L)

print("The Iteration:{}".format(it))

print("item is:{}".format(it.__next__()))
print("item is:{}".format(next(it)))
print("item is:{}".format(next(it)))
print("item is:{}".format(next(it)))

# 在代码段 for X in Y 中，Y必须是个迭代器或者可以通过使用 iter() 创建迭代器的一些对象

obj=(12,34)

for i in iter(obj):
    print(i)

for i in obj:
    print(i)

# 可以使用list（）或tuple（）构造函数将迭代器实现为列表或元组：
L=[1,2,3]
iterator=iter(L)
t=tuple(iterator)
print(t)

# 如果你知道迭代器将返回N个元素,你可以将它们解压缩成为一个N元组：
L=[1,2,3]
iterator=iter(L)
a,b,c=iterator
print(a,b,c)

# 特别的，在迭代器中只能逐个元素从第一个到最后一个进行枚举，
# 但不能访问前一个元素，也不能重置枚举器或者获取一份枚举器的拷贝
# Iterator对象可以选择提供这些附加功能，但是迭代器协议只指定了 __next__() 方法
# 因此，函数可能会消耗所有迭代器的输出，如果需要对相同的数据流做一些不一样的事情，需要创建一个新的迭代器

#Python 的 sequence 类型，例如 string 将支持自动创建迭代器

m = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,\
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

for key in m:
    print(key,m[key])

# 可以调用 字典的 values() 和 items() 方法获取适当的迭代器
# dict() 构造器可以接收一个返回（key，value）元组的有限流的迭代器

L = [('Italy', 'Rome'), ('France', 'Paris'), ('US', 'Washington DC')]
values=dict(iter(L))
for value in values:
    print(value,values[value])


# 文件也可以通过调用readline()来获得枚举器
file=open('poem.txt')
for line in file:
    # do something for each line
    print(line)


    