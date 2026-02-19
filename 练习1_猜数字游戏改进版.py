"""
练习1：猜数字游戏改进版

要求：
1. 使用random模块生成1-100的随机数
2. 用户有10次机会猜数字
3. 每次猜完后提示"大了"或"小了"
4. 如果猜对了，显示用了几次猜中
5. 如果10次都没猜中，显示正确答案
6. 使用break和continue语句优化代码

请在此处编写你的代码：
"""

import random

# 在这里编写你的代码
# 提示：
# 1. 使用 random.randint(1, 100) 生成随机数
# 2. 使用 for 循环限制10次机会
# 3. 使用 if-elif-else 判断大小
# 4. 使用 break 在猜对时退出循环

# 你的代码开始：

answer=random.randint(1,100)
for i in range(10):
    number=int(input('你猜多少？'))
    if number==answer:
        print('你用了',i,'次就猜对了')
        break
    else:
        if number<answer:
            print('小了')
        elif number>answer:
            print('大了')
