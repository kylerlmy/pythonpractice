#----------------------------------函数----------------------------------

def say_hello():
    #function body block start
    print('hello world')
#function body block end

say_hello() #call function
say_hello() #call function again

#-----------------函数参数-----------------

def print_max(a,b):
    if a>b:
        print('{} is maximum'.format(a))
    elif a==b:
        say_hello()
        print('{} is equal to {}'.format(a,b))
    else:
        print('{} is maximum'.format(b) )


print_max(8,5)

#-----------------global语句，局部变量-----------------

x=50
def func():
    global x

    print('x is:',x)
    x=2
    print('Changed global x to',x)
func()
print('Value of global x is',x)


#-----------------默认参数值-----------------

def say(message,times=1):
    print(message * times)

say(1,5)
say('Hello')
say('Hello',5)


#-----------------关键字参数（命名参数）-----------------

def func(a,b=5,c=10):
    print('a is',a,'and b is',b,'and c is',c)


func(3,7)
func(25,c=24)
func(c=50,a=100)


#-----------------可变参数 params-------------------------
def total(a=5,*numbers,**phonebook):
    print('a',a)

    #遍历元组中所有项目
    for singgle_item in numbers:
        print('single_item',singgle_item)
    
    #遍历字典中的所有项目
    for first_part,second_part in phonebook.items():
        print(first_part,second_part)
    
print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))
print(total(1,2,3,Jack=1123,John=2231,Inge=1560))


#-----------------------return--------------------

# return 语句没有搭配任何一个值则代表着 返回 None，None 在Python中是一个特殊的类型，代表着虚无，
# 例如：每个函数都在其末尾部分，隐含了一句 return None
def maximum(x,y):
    if(x>y):
        return x
    elif x==y:
        return 'The numbers are equal'
    else:
        return y

print(maximum(2,3))


#---------Retun None---------------------------
def some_function():
    pass #pass 语句用于指示一个没有内容的语句块

print(some_function()) #返回None


#--------------文档字符串 DocString----------

# 函数的第一行逻辑行中的字符串是该函数的 文档字符串（DocString）
#该文档字符串所约定的是一串多行字符串，其中第一行以某一大写字母开始，以句号结束。
#第二行为空行，后跟的第三行开始是任何详细的解释说明
def print_max(x,y):
    '''print maximum of the numbers.

       the two numbers must type of int'''
    #如果可能，将其转换至整数类型
    x=int(x)
    y=int(y)

    if x>y:
        print(x,'is maximum')
    else:
        print(y,'is maximum')

print_max(3,5)
print(print_max.__doc__)#Python将所有东西都视为一个对象，这其中自然包括函,__doc__为函数的属性
help(print_max)#查看函数说明
