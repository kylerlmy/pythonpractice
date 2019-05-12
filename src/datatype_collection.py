#当集合中的项目 存在与否 比起次序或其出现次数更加重要时，我们就会使用集合。
#通过使用集合，你可以测试某些对象的资格或情况，
# 检查它们是否是其它集合的子集，找到两个集合的交集

bri=set(['brazil','russia','india'])
if 'india' in bri:
    print('True')
else:
    print('False')

if 'usa' in bri:
    print('True')
else:
    print('False')

bric=bri.copy()
bric.add('china')

if bric.issuperset(bri):#判断集合bric是否包含集合bri 
     print('True')
else:
    print('False')

bri.remove('russia')
print(bri & bric)

help(set)