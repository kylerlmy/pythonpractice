# 将一个正整数分解因数，如输入90 打印 2*3*3*5
print("Please input a number:")
number = input("Enter Number:")
number = int(number)


def prime_num(num):
    r_value = []

    for i in range(2, num+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            r_value.append(i)
    return r_value


def prime_factor_solve(num, prime_list):
    for n in prime_list:
        if num % n == 0:
            return[n, num // n]


def prime_divisor(num):
    prime_range = prime_num(num)
    ret_vale = []

    while num not in prime_range:
        factor_list = prime_factor_solve(num, prime_range)
        ret_vale.append(factor_list[0])
        num = factor_list[1]
    else:
        ret_vale.append(num)

    return list(ret_vale)


vaules = prime_divisor(number)

result = ""
vaules.reverse()
for i in vaules:
    result = '{}*'.format(i)+result

print('{0}={1}'.format(number, result.strip('*')))
