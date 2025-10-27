import time
print("欢迎使用查找数字工具：")
min_val = int(input("请输入范围最小值："))
max_val = int(input("请输入范围最大值："))
if min_val < 0 or min_val > max_val:
    print("条件输入错误")
    exit()
bs = int(input("请输入要找的数字的倍数："))
bh = int(input("请输入要包含的数字："))
print("------------开始执行---------------")
time.sleep(2)
number = min_val
box = []
while number <= max_val:
    if number % bs == 0 or str(bh) in str(number):
        box.append(number)
    number = number + 1
    #print(number)
print(f"找到符合条件的数字有{box}")




