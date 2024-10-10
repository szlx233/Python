#这是一个简单的预测机，有两个输入（千米，英里），一个参数（两者转换的一次函数斜率）
from time import sleep

km = float(input("请输入千米数："))
mile = float((input("请输入英里数:")))


#定义训练函数
def learning_moudle(km, mile):
    #定义参数
    k = 0.5
    step = 0.00001

    count = 0

    pre_mile = km * k
    e = pre_mile - mile

    while abs(e) > 0.0001:
        if e >0:
            k -= step
        else:
            k += step

        print(k)
        pre_mile = km * k #更新k后的预测值
        e = pre_mile - mile #更新误差值
        count += 1
    print("count: ", count)
    return k

def apply_func(k):
    while True:
        choose = input("选择千米(1)/英里(2)：")
        input_number = float(input("输入数值："))
        if choose == "1":
            cal = input_number * k
        elif choose == "2":
            cal = input_number / k
        else:
            print("输入正确数值！")
            continue
        
        print("结果是：", cal)

if __name__ == "__main__":
    k_after = learning_moudle(km, mile)
    apply_func(k_after)