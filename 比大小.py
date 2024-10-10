from random import randint

Number = randint(1,100)
# Number = 16
count = 0
num = -1

print("猜猜奈奈现在心里想的是哪一个数字？(ps: 你一共有8次机会呦~)")

while num != Number:
    if count == 8:
        break
    num = int(input("你的答案："))
    count += 1

    if num == Number:
        if count == 1:
            print("可恶~竟然一次就猜对啦~")
        else:
            print("可恶~竟然猜对了~")
    else:
        if num > Number:
            print("猜大了哦，小一点吧~")
        else:
            print("猜小了哦，大一点吧~")
    print(8-count)

if count == 8:
    print("啊？这么菜？")
print("哼，不玩啦，睡觉！")
