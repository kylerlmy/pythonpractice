# 提示用户输入3个点的x,y 坐标值，判断这三个点是否在同一条直线上
# 输入时两个点用空格隔开
# 要求 使用异常处理机制

# 思路：你先判断横坐标是否相同，如果相同则显然在同一条直线上如果不同，再判断三点两两之间确定直线的斜率，如果三个斜率相同，则共线，否则就不共线


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Isonline:

    def is_line(self, point1, point2, point3):
        # 两点共点（p1与p2共点，p1与p3共点，p2与p3共点）
        if(point1.x == point2.x and point1.y == point2.y) or (point1.x == point3.x and point1.y == point3.y) or (point2.x == point3.x and point2.y == point3.y):
            return True
        # 三点纵坐标相等，横坐标不相等
        if(point1.y == point2.y and point1.y == point3.y) and (point1.x != point2.x and point1.x != point3.x):
            return True
        # 三点横坐标相等，且纵坐标不相等
        if(point1.x == point2.x and point1.x == point3.x) and (point1.y != point2.y and point1.y != point3.y):
            return True
        # 横坐标不相等则不存在除数为0问题
        else:
            k1 = (point3.y-point2.y)/(point3.x-point2.x)
            k2 = (point1.y-point2.y)/(point1.x-point2.x)

            if k1 == k2:
                return True
            else:
                return False


def get_point(value):

    try:
        value = value.split(',')
        x = int(value[0])
        y = int(value[1])
    except:
        return None
    else:
        return Point(x, y)


print('请输入三个点，每点之间以空格隔开，如：1,2 3,2 3,2：')
inputpoints = input('输入点集:')
if inputpoints.__contains__('，'):
    print('存在非法字符， ‘，’为中文符号')
    inputpoints = input('请重新输入点集:')

pointslist = inputpoints.split(' ')
if pointslist.__len__() < 3:
    print('必须输入三个点！')
    inputpoints = input('请重新输入点集:')
    pointslist = inputpoints.split(' ')

firstpoint = get_point(pointslist[0])
secondpoint = get_point(pointslist[1])
thirdpoint = get_point(pointslist[2])

if firstpoint == None or secondpoint == None or thirdpoint == None:
    print('输入不合法')
else:
    online = Isonline()
    result = online.is_line(firstpoint, secondpoint, thirdpoint)
    print('三个点是否在一条直线上：{0}'.format(result))
