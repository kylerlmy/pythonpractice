def say_hello():
    #function body block start
    print('hello world')
#function body block end

say_hello() #call function
say_hello() #call function again


def print_max(a,b):
    if a>b:
        print('{} is maximum'.format(a))
    elif a==b:
        say_hello()
        print('{} is equal to {}'.format(a,b))
    else:
        print('{} is maximum'.format(b) )


print_max(8,5)


x=50
def func():
    global x

    print('x is:',x)
    x=2
    print('Changed global x to',x)
func()
print('Value of global x is',x)


def say(message,times=1):
    print(message * times)

say(1,5)
say('Hello')
say('Hello',5)


#命名参数

def func(a,b=5,c=10):
    print('a is',a,'and b is',b,'and c is',c)


func(3,7)
func(25,c=24)
func(c=50,a=100)

