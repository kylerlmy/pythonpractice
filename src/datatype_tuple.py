# 元组是不可变的，不可以编辑或更改元组
#元组通常用于保证某一语句或某一用户定义的函数可以安全地采用一组数值，即元组内的数值不可改变

#（）用于指明元组的开始和结束

zoo=('python','elephant','penguin')

print('Number of animals in the zoo is',len(zoo))

new_zoo=('monkey','camel',zoo)
print('Number os cages in the new zoo is',len(new_zoo))
print('All animals in new zoo are',new_zoo)
print('Animals brought from old zoo are',new_zoo[2])
print('Last animal brought from old zoo is',new_zoo[2][2])
print('Number of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2]))

#-------------以下定义的singgle不是一个元组，而是一个用括号括着的字符串-----------------
single=('one')
print(single[0])

#------单个元素的元组的正确定义------------
single2=('one',)
print(single2[0])

#查看帮助信息
help(tuple)