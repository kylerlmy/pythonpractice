import sys
import os
import math

from math import sqrt#应使用import，不推荐使用from...import...

print('The command line argumets are:')
for i in sys.argv:
    print(i)

print('\n\n the PYTHONPATH is',sys.path,'\n')


print('local dir is:',os.getcwd())


print('Sequare root of 16 is',sqrt(16))
print('Sequare root of 16 is',math.sqrt(16))


#模块的__name__属性可以用来确定模块是独立运行的还是被导入运行的

if __name__=='__main__':
    print('this program is being run by itself')
else:
    print('I am being imprted from another module')

#-------------------del--------------------------
a=6
print(a)
del a
print(a)

#-------------------dir()--------------------------
print(dir(sys))#dir 返回对象（模块等）所定义的名称列表



