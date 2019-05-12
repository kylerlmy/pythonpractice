print('Sample assignment')

#定义一个 元组（不可变的，不可以编辑或更改元组，即不可修改元素的内容）
shoplist=['apple','mango','carrot','banana']
#mylist 只是指向同一对象的另一种名称

mylist=shoplist

del shoplist[0]

print('shoplist is',shoplist)
print('mylist is',mylist)

#shoplist 和 mylist 输出了同样的结果，因此我们确认它们指向的是同一个对象

print('Copy by making a full slice')
mylist=shoplist[:]#通过生成一份完整的切片制作一份列表的副本
del mylist[0]#删除mylist中的内容，不影响 shoplist的内容

print('shoplist is',shoplist)
print('mylist is',mylist)

#你要记住如果你希望创建一份诸如序列等复杂对象的副本（而非整数这种简单的对象（Object）），
# 你必须使用切片操作来制作副本
