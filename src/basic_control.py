## 控制流

number=12
guess=12#int(input('Enter an integer:'))
if guess==number:
    #新块在这里开始23
    print('congradulation ,you guessed it.')
    #块结束
elif guess<number:
    #另一代码块
    print('No,it is little higher than that')
    #end block
else:
    print('No,it is a littler lower than that')

print('Done')

### for 循环 ，for循环与 C# 中的 foreach 循环相似。

for i in list(range(1,5)): #或者 for i in range(1,5) range应该实现了枚举器功能
    print(i)
else:
    print('the for loop is over')



### while 语句

number=12
running=False

while running:

    guess=int(input('Enter an integer:'))

    if guess==number:
        #新块在这里开始23
        print('congradulation ,you guessed it.')
        running=False
        #块结束
    elif guess<number:
        #另一代码块
        print('No,it is little higher than that')
        #end block
    else:
        print('No,it is a littler lower than that')

    print('Done')

### continue
while True:
    s=input('Enter something: ')
    if s=='quit':
        break
    if len(s)<3:
        print('too small')
        continue
    print('input is of sufficient length')

