# 定义一个代表二维坐标系中某个点的 Point类，为 Point 类定义减法运算符支持
# 可以计算二维坐标系中任意两个点之间的距离，输入时两个点用空格隔开
import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def get_distance(selfpoint, x, y):

        xdiff = math.fabs(selfpoint.x-x)
        ydiff = math.fabs(selfpoint.y-y)

        # 使用勾股定理计算两点间的距离
        xpow = math.pow(xdiff, 2)
        ypow = math.pow(ydiff, 2)

        value = math.sqrt(xpow+ypow)

        return value

    def __sub__(self, newpoint):
        x = newpoint.x
        y = newpoint.y
        return self.get_distance(self, x, y)


print('请输入两个点，两个点之间以空格隔开，如：1,2 3,2：')
inputpoints = input('输入点集:')
if inputpoints.__contains__('，'):
    print('存在非法字符， ‘，’为中文符号')
    inputpoints = input('请重新输入点集:')

pointslist = inputpoints.split(' ')
if pointslist.__len__() < 2:
    print('必须输入两个点！')
    inputpoints = input('请重新输入点集:')
    pointslist = inputpoints.split(' ')

point1 = pointslist[0]
point1 = point1.split(',')

point1x = int(point1[0])
point1y = int(point1[1])

point2 = pointslist[1]
point2 = point2.split(',')

point2x = int(point2[0])
point2y = int(point2[1])

currentpoint = Point(point1x, point1y)
nextpoint = Point(point2x, point2y)

distance = currentpoint-nextpoint
print('两个点的距离为:{0}'.format(distance))
