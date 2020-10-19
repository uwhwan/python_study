def find_max_and_min(items):
    '''找出列表中最大和最小的元素'''
    max_one,min_one = items[0],items[0]
    for item in items:
        if item > max_one:
            max_one = item
        elif item < min_one:
            min_one = item
    return max_one,min_one

if __name__ == '__main__':
    items = input('请输入：')
    print(find_max_and_min(items))
