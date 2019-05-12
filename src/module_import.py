import mymodule

mymodule.say_hi()
print('Version',mymodule.__version__)



if __name__=='__main__':
    print('this program is being run by itself')
else:
    print('I am being imprted from another module')