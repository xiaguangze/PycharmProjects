import random

name = ["董金川", "韦东杰", "李震", "张秀东", "陈瑞鲜"]
"""
start_num = int(input("请输入开始的数字"))
stop_num = int(input("请输入结束的数字"))
step_num = int(input("请输入步长"))
count_num = int(input("请输入要随机的数字"))
list_num = []
"""
start_num = 0
stop_num = len(name)-1
step_num = 1
count_num = len(name)
list_num = []
if count_num > (stop_num-start_num+1) / step_num:
    print("超出随机范围")
else:
    for i in range(start_num, stop_num+1, step_num):
        list_num.append(i)
    for m in range(count_num, 0, -1):
        random_num = random.randint(0, len(list_num) - 1)
        pop_num = list_num.pop(random_num)
        print(name[pop_num], end="  ")
