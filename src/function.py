def say_hello():
    #function body block start
    print('hello world')
#function body block end

say_hello() #call function
say_hello() #call function again


def print_max(a,b):
    if a>b:
        print('{} is maximum'.format(a))
        say_hello()
    elif a==b:
        print('{} is equal to {}'.format(a,b))
    else:
        print('{} is maximum'.format(b) )


print_max(8,5)

