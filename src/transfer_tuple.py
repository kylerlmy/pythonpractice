# 使用元组从一个函数中返回两个不同的值
# a, b = <some expression> 的用法会将表达式的结果解释为具有两个值的一个元组。

def get_error_details():
    return(2,'details')

errnum,errstr=get_error_details()

def swap(a,b):
    print("a:{},b:{}".format(a,b))
    a,b=b,a
    print("a:{},b:{}".format(a,b))

swap(5,8)
