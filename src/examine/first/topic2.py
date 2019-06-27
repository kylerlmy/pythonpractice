# 输入一组数字，一空格分隔；接收数据后，提示用户是否按升序排列，
# 如果输入 Y 则按升序输出，如果输入 N 则按降序输出（忽略大小写）
# 要求：代码中至少有一处使用lambda表达式
import sys

print('Please input some numbers that split with space:')
inputvalues = input('Enter numbers:')
numbers = inputvalues.split(' ')
# 需要将字符串转换为整数，否则，一位数与两位数同时存在时，排序结果有偏差。如：08 和 8 将造成排序结果不一致
numbers = [int(i) for i in numbers]


def bubble_sort(valuelist, sortmethod):
    ''' 冒泡排序

    valuelist 为需要排序的序列
    '''

    i = 0
    length = len(valuelist)
    while(i < length):

        j = 0
        n = length-i-1
        while(j < n):
            if sortmethod(valuelist[j+1], valuelist[j]):
                temp = valuelist[j]
                valuelist[j] = valuelist[j+1]
                valuelist[j+1] = temp

            j = j+1

        i = i+1

    return valuelist


print('Please select sort method (Y/ascending order,N/descending order)')
issort = input("Please input Y(yes) or N(no):")
issort = issort.upper()
# ascending sort
if issort == 'Y':
    numbers = bubble_sort(numbers, lambda x, y: x < y)
# descending sort
else:
    numbers = bubble_sort(numbers, lambda x, y: x > y)

print('the sort result is:')
for num in numbers:
    print('num is {}'.format(num))
