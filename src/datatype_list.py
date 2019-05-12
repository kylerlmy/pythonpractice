# [] 用于指明列表的开始和结束

# this is my shopping list
shoplist=['apple','mango','carror','banana']

print('I have ',len(shoplist),'items to purchase.')

print('There items are:',end='')

for item in shoplist:
    print(item,end=' ')

print('\nI also have to buy rice.')

shoplist.append('rice')
print('My shopping list is now',shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is ',shoplist)

print('The first item I will buy is',shoplist[0])

olditem=shoplist[0]

del shoplist[0]

print('I bought the',olditem)

print('My shopping list is now',shoplist)

#查看帮助信息
help(list)