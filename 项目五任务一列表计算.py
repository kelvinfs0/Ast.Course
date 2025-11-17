#求列表的最大值、最小值、平均数和总和
list = [59,54,89,45,78,45,12,59,54,89]
#求最大值
list_max = max(list)
print("最大值为:", list_max)
#求最小值
list_min = min(list)
print("最小值为:", list_min)
#求列表平均数
sum = 0
for i in list:          
    sum = sum + i
pjs = sum / len(list)
print("平均数为:", pjs)
#求和
total = 0
for i in list:
    total = total + i
print("总和为:", total)



