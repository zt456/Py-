# coding= utf-8

import random

#循环次数
n=0
while n <= 4:
    n+=1
    # 生成电脑答案
    npc = random.randint(0, 1)
    # 玩家输入
    try:
        player = input('请玩家输入一个整数：')
        player = int(player)
        if int(player) > int(npc):
            print(player,"大于",npc,"失败")
        elif int(player) < int(npc):
            print(player,"小于",npc,"失败")
        else:
            print('胜利,挑战结束')
            break
    except ValueError:
            print('输入错误,请重新输入')
else:
    print('失败，挑战次数用完')