# “ab”是地址（Address）簿（Book）的缩写
ab = {
'Swaroop': 'swaroop@swaroopch.com',
'Larry': 'larry@wall.org',
'Matsumoto': 'matz@ruby-lang.org',
'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is",ab['Swaroop'])

del ab['Spammer']

print('\n There are {} contacts in the address-book\n'.format(len(ab)))

for name,address in ab.items():#注意itmes是方法，不是字段
    print('Contact {} at {}'.format(name,address))

#添加一对键值对
ab['Guido']='auido@python.org'

if 'Guido' in ab:
    print("\n Guido's address is",ab['Guido'])

#查看帮助信息
help(dict)