#猜数游戏，练习选择和分支结构的python语法
from random import randint

money = 1000
while money > 0:
    print('资产为：'+str(money))
    go_on = False
    #下注金额必须大于0，小于等于玩家总资产
    while True:
        debt = int(input('请下注：'))
        if 0 < debt <= money:
            break
    #第一次摇色子
    #用1到6均匀分布的随机数模拟摇色子得到的点数
    first = randint(1,6)+randint(1,6)
    print('玩家摇出了'+str(first)+'点')
    if first == 7 or first ==11:
        print('玩家胜！')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜')
        money -= debt
    else:
        go_on = True
    #第一次摇色子没有分出胜负游戏继续
    while go_on:
        go_on = False
        current = randint(1,6)+randint(1,6)
        print('玩家摇出了'+str(current)+'点')
        if current == 7:
            print('庄家胜')
            money -= debt
        elif current == first:
            print('玩家胜')
            money += debt
        else:
            go_on = True
print('你破产了，游戏结束！')