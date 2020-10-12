#寻找水仙花数
for i in range(100,1000):
    low = i%10
    mid = i // 10 % 10   #//表示整除，返回的是整数；/表示浮点数除法，返回的是浮点数
    high = i // 100
    if i == low ** 3+mid ** 3+high ** 3:
        print(i)
