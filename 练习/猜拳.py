# coding= utf-8

import random
# 随机机器的选择
NPC_seletc=random.randint(0,2)
if NPC_seletc == 0:
    NPC = "石头"
elif NPC_seletc == 1:
    NPC = "剪刀"
else :
    NPC = "布"
# 玩家输入

player = input("请输入石头，剪刀或布:")
if player !="石头" and player !="剪刀" and player !="布":
    print ("输入错误,请重新输入")
else:
    # 对比结果
    if NPC == "石头":
        if player == "石头":
            print ("平局")
        elif player == "剪刀":
            print ("你输了")
        else:
            print("你赢了")
    if NPC == "剪刀" :
        if player == "剪刀":
            print ("平局")
        elif player == "布":
            print ("你输了")
        else:
            print ("你赢了")
    if NPC == "布":
        if player == "布":
            print ("平局")
        elif player == "石头":
            print ("你输了")
        else:
            print("你赢了")

