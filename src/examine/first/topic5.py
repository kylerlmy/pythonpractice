# 请根据自己的理解编写计数算法，接收如下文字，输出其中每个字母出现的次数，以字典形式输出；（忽略大小写）
# 文字内容：
# Understanding object-oriented programming will help you see the world as a programmer does.
# It will help you really know your code, not just what is happening line by line, but also the bigger concepts behind it.
# Knowing the logic behind classes will train you to think logically so you can write programs that effectively address almost any problem you encounter.

print('Please input the content:')
value = input('Enter content:')

values = value.lower().replace('.', '').replace(',', '').replace(' ', '')


dic={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,}
for item in values:
    if(item in dic):
        dic[item]=dic[item]+1


for key,value in dic.items():
    print('{0} 出现次数：{1:^2} 次'.format(key,value))

