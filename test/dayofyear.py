#计算指定的年月是这一年的第几天

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year,month,date):
    '''计算传入的日期是这一年的第几天'''
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ]
    #布尔值false和true可以转换成整数0和1
    #平年会选中嵌套列表中的第一个列表（2月是28天）
    #闰年会选中嵌套列表中的第二个列表（2月是29天）
    days = days_of_month[is_leap_year(year)]
    total = 0
    for index in range(month-1):
        total += days[index]
    return total + date

print(which_day(1980, 11, 28))
