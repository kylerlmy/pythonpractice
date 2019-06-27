# 输入十进制，输出对应的二进制、八进制、十六进制；
# 如果输入二进制、八进制、十六进，输出对应的十进制；
import sys

print('Please input the value:')
value = input('Enter value:')


def is_hexs(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False


def is_eight(s):
    try:
        int(s, 8)
        return True
    except ValueError:
        return False


def is_byte(string):

    p = set(string)
    s = {'0', '1'}

    if s == p or p == {'0'} or p == {'1'}:
        True
    else:
        False


def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


if is_integer(value):

    intvalue = int(value)

    value1 = bin(intvalue)
    value2 = oct(intvalue)
    value3 = hex(intvalue)

    print('二进制:{}'.format(value1))
    print('八进制:{}'.format(value2))
    print('十六进制:{}'.format(value3))

elif is_byte(value):

    value7=eval(value)
    value4 = str(int(value, 2))
    print('十进制:{}'.format(value4))
elif is_eight(value):
    value5 = str(int(value, 8))
    print('十进制:{}'.format(value5))
elif is_hexs(value):
    value6 = str(int(value, 16))
    print('十进制:{}'.format(value6))
