# 通过算法判断，打印1900到2100间（包括1900和2100）的所有闰年

years = range(1900, 2101, 1)


def is_leap_year(year):
    ''' 判断一个年份是否为闰年

    year 代表一个正确的年份
    年份是4的倍数而不是100的倍数的年份是闰年
    年份是400的倍数的年份是闰年。
    '''
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


for year in years:
    if is_leap_year(year):
        print("the Year {} a Leap Year".format(year))
    else:
        continue
